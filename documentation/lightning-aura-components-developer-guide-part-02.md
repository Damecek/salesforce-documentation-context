Alternatively, use the `Full` layout type, which loads all fields from the full layout to display a form that creates a record. The `columns`
attribute displays the record fields in two columns that are evenly sized.

```
   <aura:component>

      <lightning:recordForm objectApiName="Account"

                   layoutType="Full"

                   columns="2"/>

   </aura:component>

```

Customize Error Handling in **`lightning:recordForm`**

When an error is encountered during save, `lightning:recordForm` displays an error message at the top of the form. You can
provide additional error handling using the `onerror` event handler.

This example displays a toast message when an error is returned.

```
   <aura:component>

      <aura:attribute name="fields"

               type="String[]"

               default="['Name', 'Industry']"/>

      <!-- Displays toast notifications -->

      <lightning:notificationsLibrary aura:id="notifLib" />

      <lightning:recordForm

        objectApiName="Account"

        fields="{!v.fields}"

        onerror="{!c.handleError}"/>

   </aura:component>

```

To return the error message, use `event.getParam("message")` .

```
   ({

      handleError: function (cmp, event, helper) {

        cmp.find('notifLib').showToast({

           "title": "Something has gone wrong!",

           "message": event.getParam("message"),

           "variant": "error"

        });

      }

   })

```

To customize the form behavior when a record saves successfully, use the `onsuccess` event handler.


Working with Salesforce Data Creating a Record

If you want to provide a custom layout or load custom field values when the form displays, use the `lightning:recordEditForm`
component as shown in the next section.

Create a Record with a Custom Layout Using **`lightning:recordEditForm`**

To provide a custom layout for your form fields, use the `lightning:recordEditForm` component.

Pass in the fields to `lightning:inputField`, which displays an input control based on the record field type.

This example creates a custom layout using the Grid utility classes in Lightning Design System.

```
   <aura:component>

      <lightning:recordEditForm objectApiName="Account">

        <lightning:messages />

           <div class="slds-grid">

             <div class="slds-col slds-size_2-of-3">

               <lightning:inputField fieldName="Name"/>

             </div>

             <div class="slds-col slds-size_1-of-3">

               <lightning:inputField fieldName="Industry"/>

             </div>

           </div>

        <lightning:button class="slds-m-top_small" type="submit" label="Create new" />

      </lightning:recordEditForm>

   </aura:component>

```

When a server error is encountered, `lightning:recordEditForm` displays an error message above the form fields. To enable
automatic error handling, include the `lightning:messages` component. Alternatively, provide your own error handling using
the `onerror` event handler.

Another feature that `lightning:recordEditForm` provides that’s not available with `lightning:recordForm` is preset
custom field values, as shown in the next section.

Prepopulate Field Values

To provide a custom field value when the form displays, use the `value` attribute on `lightning:inputField` . If you're providing
a record ID, the value returned by the record on load does not override this custom value.

Alternatively, set the field value using this syntax.

```
   cmp.find("nameField").set("v.value", "My New Account Name");

```

[Note: For more information, see lightning:recordEditForm.](https://developer.salesforce.com/docs/component-library/bundle/lightning:recordEditForm/documentation)

If you require more customization when creating a record than what `lightning:recordForm` and
`lightning:recordEditForm` allow, consider using `force:recordData` .

Create a Record via a Custom User Interface Using **`force:recordData`**

To create a record using `force:recordData`, leave out the `recordId` attribute. Load a record template by calling the
`getNewRecord` function on `force:recordData` . Finally, apply values to the new record, and save the record by calling the
`saveRecord` function on `force:recordData` .

**1.** Call `getNewRecord` to create an empty record from a record template. You can use this record as the backing store for a form
or otherwise have its values set to data intended to be saved.


Working with Salesforce Data Creating a Record

**2.** Call `saveRecord` to commit the record. This is described in Editing a Record.

Create an Empty Record from a Record Template

To create an empty record from a record template, you can’t set a `recordId` on the `force:recordData` tag. Without a
`recordId`, Lightning Data Service doesn’t load an existing record.

In your component’s `init` or another handler, call the `getNewRecord` on `force:recordData` . `getNewRecord` takes the
following arguments.

**Attribute Name** **Type** **Description**

`objectApiName` String The object API name for the new record.

`recordTypeId` String

The 18 character ID of the record type for the new record.

If not specified, the default record type for the object is used, as defined in the
user’s profile.

`skipCache` Boolean Whether to load the record template from the server instead of the client-side
Lightning Data Service cache. Defaults to `false` .

`callback` Function A function invoked after the empty record is created. This function receives no
arguments.

`getNewRecord` doesn’t return a result. It simply prepares an empty record and assigns it to the `targetRecord` attribute.

Example: **Creating a Record**

The following example illustrates the essentials of creating a record using Lightning Data Service. This example is intended to be
added to an account record Lightning page.

```
  ldsCreate.cmp

   <aura:component implements="flexipage:availableForRecordHome, force:hasRecordId">

     <aura:attribute name="newContact" type="Object"/>

     <aura:attribute name="simpleNewContact" type="Object"/>

     <aura:attribute name="newContactError" type="String"/>

     <aura:handler name="init" value="{!this}" action="{!c.doInit}"/>

     <force:recordData aura:id="contactRecordCreator"

                fields="FirstName,LastName,Title"

                targetRecord="{!v.newContact}"

                targetFields="{!v.simpleNewContact}"

                targetError="{!v.newContactError}" />

     <!-- Display the new contact form -->

     <div class="Create Contact">

        <lightning:card iconName="action:new_contact" title="Create Contact">

          <div class="slds-p-horizontal--small">

            <lightning:input aura:id="contactField" label="First Name"

   value="{!v.simpleNewContact.FirstName}"/>

            <lightning:input aura:id="contactField" label="Last Name"

```


Working with Salesforce Data Creating a Record

```
      value="{!v.simpleNewContact.LastName}"/>

               <lightning:input aura:id="contactField" label="Title"

      value="{!v.simpleNewContact.Title}"/>

               <br/>

               <lightning:button label="Save Contact" variant="brand"

      onclick="{!c.handleSaveContact}"/>

             </div>

           </lightning:card>

        </div>

        <!-- Display Lightning Data Service errors -->

        <aura:if isTrue="{!not(empty(v.newContactError))}">

           <div class="recordError">

             {!v.newContactError}</div>

        </aura:if>

      </aura:component>

```

Note: To improve performance, we recommend using the `fields` attribute to query only the fields you need. Use
`layoutType` only if you want the administrator, not the component, to control the fields that are provisioned. The
component must handle receiving every field that is assigned to the layout for the context user.

This component doesn’t set the `recordId` attribute of `force:recordData` . This tells Lightning Data Service to expect a
new record. Here, that’s created in the component’s `init` handler.

```
     ldsCreateController.js

      ({

        doInit: function(component, event, helper) {

           // Prepare a new record from template

           component.find("contactRecordCreator").getNewRecord(

             "Contact", // sObject type (objectApiName)

             null, // recordTypeId

             false, // skip cache?

             $A.getCallback(function() {

               var rec = component.get("v.newContact");

               var error = component.get("v.newContactError");

               if(error || (rec === null)) {

                  console.log("Error initializing record template: " + error);

                  return;

               }

               console.log("Record template initialized: " + rec.apiName);

             })

           );

        },

        handleSaveContact: function(component, event, helper) {

           if(helper.validateContactForm(component)) {

            component.set("v.simpleNewContact.AccountId", component.get("v.recordId"));

             component.find("contactRecordCreator").saveRecord(function(saveResult) {

               if (saveResult.state === "SUCCESS" || saveResult.state === "DRAFT") {

                  // record is saved successfully

                  var resultsToast = $A.get("e.force:showToast");

```


Working with Salesforce Data Creating a Record

```
                  resultsToast.setParams({

                    "title": "Saved",

                    "message": "The record was saved."

                  });

                  resultsToast.fire();

               } else if (saveResult.state === "INCOMPLETE") {

                  // handle the incomplete state

                  console.log("User is offline, device doesn't support drafts.");

               } else if (saveResult.state === "ERROR") {

                  // handle the error state

                  console.log('Problem saving contact, error: ' +

      JSON.stringify(saveResult.error));

               } else {

                  console.log('Unknown problem, state: ' + saveResult.state + ',

      error: ' + JSON.stringify(saveResult.error));

               }

             });

           }

        }

      })

```

The `doInit` init handler calls `getNewRecord()` on the `force:recordData` component, passing in a simple callback
[handler. This call returns a Record object to create an empty contact record, which is used by the contact form in the component’s](https://developer.salesforce.com/docs/atlas.en-us.260.0.uiapi.meta/uiapi/ui_api_responses_record.htm)
markup.

Note: The callback passed to `getNewRecord()` must be wrapped in `$A.getCallback()` to ensure correct access
context when the callback is invoked. If the callback is passed in without being wrapped in `$A.getCallback()`, any
attempt to access private attributes of your component results in access check failures.

Even if you’re not accessing private attributes, it’s a best practice to always wrap the callback function for `getNewRecord()`
in `$A.getCallback()` . Never mix (contexts), never worry.

The `handleSaveContact` handler is called when the **Save Contact** button is clicked. It’s a straightforward application of
saving the contact, as described in Editing a Record, and then updating the user interface.

Note: The helper function, `validateContactForm`, isn’t shown. It simply validates the form values. For an example
of this validation, see Lightning Action Examples.

SEE ALSO:

_Component Library_ : `[lightning:recordForm](https://developer.salesforce.com/docs/component-library/bundle/lightning:recordForm/documentation)`

_Component Library_ : `[lightning:recordEditForm](https://developer.salesforce.com/docs/component-library/bundle/lightning:recordEditForm/documentation)`

Editing a Record

Configure Components for Lightning Experience Record Pages

Configure Components for Record-Specific Actions

Controlling Access


### Working with Salesforce Data Deleting a Record Deleting a Record

To delete a record using Lightning Data Service, call `deleteRecord` on the `force:recordData` component, and pass in a
callback function to be invoked after the delete operation completes. The form-based components, such as `lightning:recordForm`,
don’t currently support deleting a record.

Delete operations with Lightning Data Service are straightforward. The `force:recordData` tag can include minimal details. If you
don’t need any record data, set the `fields` attribute to just `Id` . If you know that the only operation is a delete, any `mode` can be
used.

To perform the delete operation, call `deleteRecord` on the `force:recordData` component from the appropriate controller
action handler. `deleteRecord` takes one argument, a callback function to be invoked when the operation completes. This callback
function receives a `SaveRecordResult` as its only parameter. `SaveRecordResult` includes a `state` attribute that indicates
success or error, and other details you can use to handle the result of the operation.

### Example: Deleting a Record

The following example illustrates the essentials of deleting a record using Lightning Data Service. This component adds a **Delete**
**Record** button to a record page, which deletes the record being displayed. The record ID is supplied by the implicit `recordId`
attribute added by the `force:hasRecordId` interface.

```
     ldsDelete.cmp

      <aura:component implements="flexipage:availableForRecordHome,force:hasRecordId">

        <aura:attribute name="recordError" type="String" access="private"/>

        <force:recordData aura:id="recordHandler"

           recordId="{!v.recordId}"

           fields="Id"

           targetError="{!v.recordError}"

           recordUpdated="{!c.handleRecordUpdated}" />

        <!-- Display the delete record form -->

        <div class="Delete Record">

           <lightning:card iconName="action:delete" title="Delete Record">

             <div class="slds-p-horizontal--small">

               <lightning:button label="Delete Record" variant="destructive"

      onclick="{!c.handleDeleteRecord}"/>

             </div>

           </lightning:card>

        </div>

        <!-- Display Lightning Data Service errors, if any -->

        <aura:if isTrue="{!not(empty(v.recordError))}">

           <div class="recordError">

             {!v.recordError}</div>

        </aura:if>

      </aura:component>

```

Notice that the `force:recordData` tag includes only the `recordId` and a nearly empty `fields` list—the absolute
minimum required. If you want to display record values in the user interface, for example, as part of a confirmation message, define
the `force:recordData` tag as you would for a load operation instead of this minimal delete example.


Working with Salesforce Data Deleting a Record

```
     ldsDeleteController.js

      ({

        handleDeleteRecord: function(component, event, helper) {

      component.find("recordHandler").deleteRecord($A.getCallback(function(deleteResult) {

             // NOTE: If you want a specific behavior(an action or UI behavior) when

      this action is successful

             // then handle that in a callback (generic logic when record is changed

      should be handled in recordUpdated event handler)

             if (deleteResult.state === "SUCCESS" || deleteResult.state === "DRAFT") {

               // record is deleted

               console.log("Record is deleted.");

             } else if (deleteResult.state === "INCOMPLETE") {

               console.log("User is offline, device doesn't support drafts.");

             } else if (deleteResult.state === "ERROR") {

               console.log('Problem deleting record, error: ' +

      JSON.stringify(deleteResult.error));

             } else {

              console.log('Unknown problem, state: ' + deleteResult.state + ', error:

      ' + JSON.stringify(deleteResult.error));

             }

           }));

        },

        /**

         * Control the component behavior here when record is changed (via any component)

         */

        handleRecordUpdated: function(component, event, helper) {

           var eventParams = event.getParams();

           if(eventParams.changeType === "CHANGED") {

            // record is changed

           } else if(eventParams.changeType === "LOADED") {

             // record is loaded in the cache

           } else if(eventParams.changeType === "REMOVED") {

             // record is deleted, show a toast UI message

             var resultsToast = $A.get("e.force:showToast");

             resultsToast.setParams({

               "title": "Deleted",

               "message": "The record was deleted."

             });

             resultsToast.fire();

           } else if(eventParams.changeType === "ERROR") {

             // there’s an error while loading, saving, or deleting the record

           }

        }

      })

```


### Working with Salesforce Data Record Changes

When the record is deleted, navigate away from the record page. Otherwise, you see a “record not found” error when the component
refreshes. Here the controller uses the `objectApiName` property in the `SaveRecordResult` provided to the callback
function, and navigates to the object home page.

SEE ALSO:

SaveRecordResult

Configure Components for Lightning Experience Record Pages

Configure Components for Record-Specific Actions

### Record Changes

To perform more advanced tasks using `force:recordData` when the record changes, handle the `recordUpdated` event.
You can handle record loaded, updated, and deleted changes, applying different actions to each change type.

If a component performs logic that’s specific to the record data, it must run that logic again when the record changes. A common
example is a business process in which the actions that apply to a record change depending on the record’s values. For example, different
actions apply to opportunities at different stages of the sales cycle.

Note: Lightning Data Service notifies listeners about data changes only if the changed fields are the same as in the listener’s fields
or layout.

Example: Declare that your component handles the `recordUpdated` event. To improve performance, we recommend using
the `fields` attribute to query only the fields you need. Use `layoutType` only if you want the administrator, not the component,
to control the fields that are provisioned. The component must handle receiving every field that is assigned to the layout for the
context user.

```
      <force:recordData aura:id="forceRecord"

        recordId="{!v.recordId}"

        fields="Name,Title,Email"

        targetRecord="{!v._record}"

        targetFields="{!v.simpleRecord}"

        targetError="{!v._error}"

        recordUpdated="{!c.recordUpdated}" />

```

Implement an action handler that handles the change.

```
      ({

       recordUpdated: function(component, event, helper) {

        var changeType = event.getParams().changeType;

        if (changeType === "ERROR") { /* handle error; do this first! */ }

        else if (changeType === "LOADED") { /* handle record load */ }

        else if (changeType === "REMOVED") { /* handle record removal */ }

        else if (changeType === "CHANGED") { /* handle record change */ }

      })

```


### Working with Salesforce Data Handling Errors

When loading a record in edit mode, the record isn’t automatically updated to prevent edits currently in progress from being
overwritten. To update the record, use the `reloadRecord` method in the action handler.

```
      <force:recordData aura:id="forceRecord"

        recordId="{!v.recordId}"

        fields="Name,Title,Email"

        targetRecord="{!v._record}"

        targetFields="{!v.simpleRecord}"

        targetError="{!v._error}"

        mode="EDIT"

        recordUpdated="{!c.recordUpdated}" />

      ({

       recordUpdated : function(component, event, helper) {

        var changeType = event.getParams().changeType;

        if (changeType === "ERROR") { /* handle error; do this first! */ }

        else if (changeType === "LOADED") { /* handle record load */ }

        else if (changeType === "REMOVED") { /* handle record removal */ }

        else if (changeType === "CHANGED") {

         /* handle record change; reloadRecord will cause you to lose your current record,

      including any changes you’ve made */

         component.find("forceRecord").reloadRecord(); }

        }

      })

### Handling Errors

```

Lightning Data Service returns an error when a resource, such as a record or an object, is inaccessible on the server.

For example, an error occurs if you pass in an invalid input to the form-based components, such as an invalid record ID or missing required
fields. An error is also returned if the record isn’t in the cache and the server is offline. Also, a resource can become inaccessible on the
server when it’s deleted or has its sharing or visibility settings updated.

Handle Errors For Form-Based Components

Two types of errors—field-level errors and Lightning Data Service errors—are handled by `lightning:recordForm`,
`lightning:recordEditForm`, and `lightning:recordViewForm` . Field-validation errors display below a field and cannot
be customized. For example, an error is shown below a required field when it’s empty. Lightning Data Service errors are handled in the
following ways.

```
   lightning:recordForm
```

Automatically displays an error message above the form fields. You can provide additional error handling using the `onerror`
event handler.

```
   lightning:recordEditForm
```

To automatically display an error message above or below the form fields, include `lightning:messages` before or after your
`lightning:inputField` components.

You can provide additional error handling using the `onerror` event handler.


Working with Salesforce Data Handling Errors

```
   lightning:recordViewForm
```

To automatically display an error message above or below the form fields, include `lightning:messages` before or after your
`lightning:outputField` components.

If a single field has multiple validation errors, the form shows only the first error on the field. Similarly, if a submitted form has multiple
errors, the form displays only the first error encountered. When you correct the displayed error, the next error is displayed.

The error object looks like this.

```
   {

     "message": "Disconnected or Canceled",

     "detail": "",

     "output": {

     },

     "error": {

      "ok": false,

      "status": 400,

      "statusText": "Bad Request",

      "body": {

       "message": "Disconnected or Canceled"

      }

     }

   }

```

Get the error object using this syntax.

```
   handleError: function (cmp, event, helper) {

      var error = event.getParams();

      // Get the error message

      var errorMessage = event.getParam("message");

   }

```

Handle Errors For **`force:recordData`**

To act when an error occurs, handle the `recordUpdated` event and handle the case where the `changeType` is “ERROR”.

Example: Declare that your component handles the `recordUpdated` event.

```
      <force:recordData aura:id="forceRecord"

        recordId="{!v.recordId}"

        fields="Name,Title,Email"

        targetRecord="{!v._record}"

        targetFields="{!v.simpleRecord}"

        targetError="{!v._error}"

        recordUpdated="{!c.recordUpdated}" />

```

Implement an action handler that handles the error.

```
      ({

       recordUpdated: function(component, event, helper) {

        var changeType = event.getParams().changeType;

```


### Working with Salesforce Data Changing the Display Density

```
        if (changeType === "ERROR") { /* handle error; do this first! */ }

        else if (changeType === "LOADED") { /* handle record load */ }

        else if (changeType === "REMOVED") { /* handle record removal */ }

        else if (changeType === "CHANGED") { /* handle record change */ }

      })

```

If an error occurs when the record begins to load, `targetError` is set to a localized error message. An error occurs if:

**•** Input is invalid because of an invalid attribute value, or combination of attribute values. For example, an invalid `recordId`,
or omitting both the `layoutType` and the `fields` attributes.

**•** The record isn’t in the cache and the server is unreachable (offline).

If the record becomes inaccessible on the server, the `recordUpdated` event is fired with `changeType` set to "REMOVED."
No error is set on `targetError`, since records becoming inaccessible is sometimes the expected outcome of an operation.
For example, after lead convert the lead record becomes inaccessible.

Records can become inaccessible for the following reasons.

**•** Record or entity sharing or visibility settings restrict access.

**•** Record or entity is deleted.

When the record becomes inaccessible on the server, the record’s JavaScript object assigned to `targetRecord` is unchanged.

### Changing the Display Density

In Lightning Experience, the display density setting determines how densely content is displayed and where field labels are located.
Display density is controlled for the org in Setup, and users can also set display density to their liking from their profile menu.

An org’s comfy setting places the labels on the top of fields and adds more space between page elements. Contrastingly, compact is a
denser view with labels on the same line as the fields and less space between lines. The cozy setting resembles compact, but with more
space between lines.

You can design your form to respect the display density setting, or set the form density to override the display density setting. Overriding
display density gives you more control over the label location, but doesn’t affect spacing. In addition, you can set individual fields in your
form to use variants that change the label location for the field.

Use the Org’s Default Display Density in a Form

`lightning:recordEditForm`, `lightning:recordViewForm`, and `lightning:recordForm` adapt to your org's
display density by default or when you set `density="auto"` .

```
   <lightning:card iconName="standard:contact" title="recordEditForm">

      <div class="slds-p-horizontal_small">

        <!-- Replace the recordId with your own -->

        <lightning:recordEditForm recordId="003RM0000066Y82YAE"

                        objectApiName="Contact"

                        density="auto">

           <lightning:messages />

           <lightning:inputField fieldName="FirstName" />

           <lightning:inputField fieldName="LastName" />

           <lightning:inputField fieldName="Email" />

           <lightning:inputField fieldName="Phone" />

```


Working with Salesforce Data Changing the Display Density

```
        </lightning:recordEditForm>

      </div>

   </lightning:card>

```

Override the Org’s Display Density

To override the org's display density, specify `density="compact"` or `density="comfy"` . The `cozy` value isn’t supported
on the `density` attribute. If an org's display density is set to cozy, labels and fields are on the same line by default.

The following table lists the org’s display density settings and how they relate to the form density on `lightning:recordEditForm`,
`lightning:recordViewForm`, and `lightning:recordForm` .

Reduce Space Between the Label and Field

When the form density is `compact`, the labels and fields can appear too far apart for a single column form in a larger region. To reduce
the space between the label and field when the form uses compact density, use the `slds-form-element_1-col` class on
`lightning:inputField` or `lightning:outputField` .

```
   <lightning:card iconName="standard:contact" title="recordEditForm">

      <div class="slds-p-horizontal_small">

        <!-- Replace the recordId with your own -->

        <lightning:recordEditForm recordId="003RM0000066Y82YAE"

                        objectApiName="Contact"

                        density="compact">

           <lightning:messages />

          <lightning:inputField fieldName="FirstName" class="slds-form-element_1-col"/>

           <lightning:inputField fieldName="LastName" class="slds-form-element_1-col"/>

           <lightning:inputField fieldName="Email" class="slds-form-element_1-col"/>

           <lightning:inputField fieldName="Phone" class="slds-form-element_1-col"/>

        </lightning:recordEditForm>

      </div>

   </lightning:card>

```

Set Label Variants on Form Fields

You can set a variant on `lightning:inputField` if you want specific fields to have a label and field alignment that’s different
than that used by the form. A variant overrides the display density for that field.


Working with Salesforce Data Changing the Display Density

`lightning:inputField` supports these variants: `standard` (default), `label-hidden`, `label-inline`, and
`label-stacked` .

This example displays two input fields with inline labels, while the rest of the fields have labels displayed on top of fields due to the
comfy form density.

```
   <lightning:card iconName="standard:contact" title="recordEditForm">

      <div class="slds-p-horizontal_small">

        <!-- Replace the recordId with your own -->

        <lightning:recordEditForm recordId="003RM0000066Y82YAE"

                        objectApiName="Contact"

                        density="comfy">

           <lightning:messages/>

           <lightning:inputField fieldName="FirstName" variant="label-inline"/>

           <lightning:inputField fieldName="LastName" variant="label-inline"/>

           <lightning:inputField fieldName="Email"/>

           <lightning:inputField fieldName="Phone"/>

        </lightning:recordEditForm>

      </div>

   </lightning:card>

```

`lightning:outputField` supports these variants: `standard` (default) and `label-hidden` .

This example displays output field values without labels when the form density is `comfy` . Hidden labels are available to assistive
technology.

```
   <lightning:card iconName="standard:contact" title="recordViewForm">

      <div class="slds-p-horizontal_small">

        <!-- Replace the recordId with your own -->

        <lightning:recordViewForm recordId="003RM0000066Y82YAE"

                        objectApiName="Contact"

                        density="comfy">

           <lightning:messages />

           <lightning:outputField fieldName="FirstName" variant="label-hidden"/>

           <lightning:outputField fieldName="LastName" variant="label-hidden"/>

           <lightning:outputField fieldName="Email" variant="label-hidden"/>

           <lightning:outputField fieldName="Phone" variant="label-hidden"/>

        </lightning:recordViewForm>

      </div>

   </lightning:card>

```

Additionally, to reduce the space between the label and field when the label variant is `label-inline`, use the
`slds-form-element_1-col` class on `lightning:inputField` .

Usage Considerations

Admins can set the default display density for the org on the Density Settings setup page. Users can choose their own display density
at any time. Admins can’t override a user’s display density setting. The org’s default display setting depends on the Salesforce edition.
Density changes don’t apply to Salesforce Classic, Experience Builder sites, or the Salesforce mobile app. For more information, see
[Configure User Interface Settings.](https://help.salesforce.com/articleView?id=customize_ui_settings.htm&language=en_US)

SEE ALSO:

_Component Library_ : `[lightning:recordEditForm](https://developer.salesforce.com/docs/component-library/bundle/lightning:recordEditForm/documentation)`

_Component Library_ : `[lightning:recordViewForm](https://developer.salesforce.com/docs/component-library/bundle/lightning:recordViewForm/documentation)`


### Working with Salesforce Data Considerations Considerations

Lightning Data Service is powerful and simple to use. However, it’s not a complete replacement for writing your own data access code.
Here are some considerations to keep in mind when using it.

Lightning Data Service is available in the following containers:

**•** Lightning Experience

**•** Salesforce app

**•** Experience Builder sites

**•** Lightning Out

**•** Lightning Components for Visualforce

**•** Standalone Lightning apps

**•** Lightning for Gmail

**•** Lightning for Outlook

Lightning Data Service supports primitive DML operations—create, read, update, and delete. It operates on one record at a time, which
you retrieve or modify using the record ID. Lightning Data Service supports spanned fields with a maximum depth of five levels. Support
for working with collections of records or for querying for a record by anything other than the record ID isn’t available. If you must support
higher-level operations or multiple operations in one transaction, use standard `@AuraEnabled` Apex methods.

Lightning Data Service shared data storage provides notifications to all components that use a record whenever a component changes
that record. It doesn’t notify components if that record is changed on the server, for example, if someone else modifies it. Records
changed on the server aren’t updated locally until they’re reloaded. Lightning Data Service notifies listeners about data changes only if
the changed fields are the same as in the listener’s fields or layout.

Lightning Data Service does a lot of work to make code perform well.

**•** Loads record data progressively.

**•** Caches results on the client.

**•** Invalidates cache entries when dependent Salesforce data and metadata changes.

**•** Optimizes server calls by bulkifying and deduping requests.

Use Base Components

To work with record data, use the following base components.

**•** `lightning:recordForm`

**•** `lightning:recordEditForm`

**•** `lightning:recordViewForm`

Use these base components to:

**•** Create a metadata-driven UI or form-based UI similar to the record detail page in Salesforce.

**•** Display record values based on the field metadata.

**•** Display or hide localized field labels.

**•** Display the help text on a custom field.

**•** Perform client-side validation and enforce validation rules.

Alternatively, use `force:recordData` to:

**•** Create your own custom UI


### Working with Salesforce Data Lightning Action Examples

**•** Return raw record data for a small number of fields

**•** Create UI that’s not metadata-driven

When using `force:recordData`, load the data once and pass it to child components as attributes. This approach reduces the
number of listeners and minimizes server calls, which improves performance and ensures that your components show consistent data.
[For more information, see the force:recordData documentation.](https://developer.salesforce.com/docs/component-library/bundle/force:recordData/documentation)

For examples of base components in action, see Lightning Action Examples on page 407.

The base components and `force:recordData` are built on Lightning Data Service. If Lightning Data Service detects a change to
a record or any data or metadata it supports, the components receive the new value. The detection is triggered if:

**•** An Aura or Lightning web component mutates the record.

**•** The Lightning Data Service cache entry expires and then a component built on Lightning Data Service triggers a read. The cache
entry and the Lightning web component must be in the same browser and app (for example Lightning Experience) for the same
user.

Note: To improve performance, we recommend specifying the fields you need instead of using a layout. Use a layout only if you
want the administrator, not the component, to control the fields that are provisioned. The component must handle receiving
[every field that is assigned to the layout for the context user. For more information, see Page Layouts in Salesforce Help.](https://help.salesforce.com/articleView?id=customize_layout.htm&language=en_US)

Supported Objects

[Lightning Data Service supports custom objects and the standard objects that User Interface API supports.](https://developer.salesforce.com/docs/atlas.en-us.260.0.uiapi.meta/uiapi/ui_api_get_started_supported_objects.htm)

### Lightning Action Examples

Here are some examples that use the base components to create a Quick Contact action panel.

Let’s say you want to create a Lightning action that enables users to create contacts on an account record. You can do this easily using
`lightning:recordViewForm` and `lightning:recordEditForm` . If you require granular customization, use
`force:recordData` .

The following examples can each be added as a Lightning action on the account object. Clicking the action’s button on the account
layout opens a panel to create a contact.

Example: **Create a Lightning Action Using** **`lightning:recordViewForm`** **and** **`lightning:recordEditForm`**

The Quick Contact action panel includes a header with the account name and a form that creates a contact for that account record.
Display the account name using `lightning:recordViewForm` and display the contact form using
`lightning:recordEditForm` .


Working with Salesforce Data Lightning Action Examples

```
     formQuickContact.cmp

      <aura:component implements="force:lightningQuickActionWithoutHeader,force:hasRecordId">

        <div class="slds-page-header" role="banner">

          <lightning:recordViewForm recordId="{!v.recordId}"

                          objectApiName="Account">

            <div class="slds-text-heading_label">

               <lightning:outputField fieldName="Name" variant="label-hidden"/>

            </div>

            <lightning:messages/>

          </lightning:recordViewForm>

          <h1 class="slds-page-header__title slds-m-right_small

                   slds-truncate slds-align-left">Create New Contact</h1>

        </div>

        <lightning:recordEditForm aura:id="myform"

                        objectApiName="Contact"

                        onsubmit="{!c.handleSubmit}"

                        onsuccess="{!c.handleSuccess}">

           <lightning:messages/>

           <lightning:inputField fieldName="FirstName"/>

           <lightning:inputField fieldName="LastName"/>

           <lightning:inputField fieldName="Title"/>

```


Working with Salesforce Data Lightning Action Examples

```
           <lightning:inputField fieldName="Phone"/>

           <lightning:inputField fieldName="Email"/>

           <div class="slds-m-top_medium">

             <lightning:button label="Cancel" onclick="{!c.handleCancel}" />

             <lightning:button type="submit" label="Save Contact" variant="brand"/>

           </div>

        </lightning:recordEditForm>

      </aura:component>

     formQuickContactController.js

      ({

        handleCancel: function(cmp, event, helper) {

           $A.get("e.force:closeQuickAction").fire();

        },

        handleSubmit: function(cmp, event, helper) {

           event.preventDefault();

           var fields = event.getParam('fields');

           fields.AccountId = cmp.get("v.recordId");

           cmp.find('myform').submit(fields);

        },

        handleSuccess: function(cmp, event, helper) {

           // Success! Prepare a toast UI message

           var resultsToast = $A.get("e.force:showToast");

           resultsToast.setParams({

             "title": "Contact Saved",

             "message": "The new contact was created."

           });

           // Update the UI: close panel, show toast, refresh account page

           $A.get("e.force:closeQuickAction").fire();

           resultsToast.fire();

           // Reload the view

           $A.get("e.force:refreshView").fire();

        }

      })

```

Using `lightning:recordEditForm`, you can nest the `lightning:inputField` components in `<div>` containers
and add custom styling. You also need to provide your own cancel and submit buttons.

Consider the simpler `lightning:recordForm` component, which provides default **Cancel** and **Save** buttons. You can
achieve the same result by replacing the `lightning:recordEditForm` component with the following.

```
      <aura:attribute name="fields" type="String[]"

      default="['FirstName','LastName','Title','Phone','Email']" />

      <lightning:recordForm objectApiName="Contact"

                   fields="{!v.fields}"

                   onsubmit="{!c.handleSubmit}"

                   onsuccess="{!c.handleSuccess}" />

```


Working with Salesforce Data Lightning Action Examples

Example: **Create a Lightning Action Using** **`force:recordData`**

The Quick Contact action panel includes a header with the account name and a form that creates a contact for that account record.
Display the account name and display the contact form using two separate instances of `force:recordData` .

This `force:recordData` example is similar to the example provided in Configure Components for Record-Specific Actions.
Compare the two examples to better understand the differences between using `@AuraEnabled` Apex controllers and using
Lightning Data Service.

```
     ldsQuickContact.cmp

      <aura:component implements="force:lightningQuickActionWithoutHeader,force:hasRecordId">

        <aura:attribute name="account" type="Object"/>

        <aura:attribute name="simpleAccount" type="Object"/>

        <aura:attribute name="accountError" type="String"/>

        <force:recordData aura:id="accountRecordLoader"

           recordId="{!v.recordId}"

           fields="Name,BillingCity,BillingState"

           targetRecord="{!v.account}"

           targetFields="{!v.simpleAccount}"

           targetError="{!v.accountError}"

        />

```


Working with Salesforce Data Lightning Action Examples

```
        <aura:attribute name="newContact" type="Object" access="private"/>

        <aura:attribute name="simpleNewContact" type="Object" access="private"/>

        <aura:attribute name="newContactError" type="String" access="private"/>

        <force:recordData aura:id="contactRecordCreator"

           layoutType="FULL"

           targetRecord="{!v.newContact}"

           targetFields="{!v.simpleNewContact}"

           targetError="{!v.newContactError}"

           />

        <aura:handler name="init" value="{!this}" action="{!c.doInit}"/>

        <!-- Display a header with details about the account -->

        <div class="slds-page-header" role="banner">

           <p class="slds-text-heading_label">{!v.simpleAccount.Name}</p>

           <h1 class="slds-page-header__title slds-m-right_small

             slds-truncate slds-align-left">Create New Contact</h1>

        </div>

        <!-- Display Lightning Data Service errors, if any -->

        <aura:if isTrue="{!not(empty(v.accountError))}">

             {!v.accountError}

        </aura:if>

        <aura:if isTrue="{!not(empty(v.newContactError))}">

           {!v.newContactError}

        </aura:if>

        <!-- Display the new contact form -->

        <lightning:input aura:id="contactField" name="firstName" label="First Name"

                  value="{!v.simpleNewContact.FirstName}" required="true"/>

        <lightning:input aura:id="contactField" name="lastname" label="Last Name"

                  value="{!v.simpleNewContact.LastName}" required="true"/>

        <lightning:input aura:id="contactField" name="title" label="Title"

                  value="{!v.simpleNewContact.Title}" />

        <lightning:input aura:id="contactField" type="phone" name="phone" label="Phone

      Number"

                  pattern="^(1?(-?\d{3})-?)?(\d{3})(-?\d{4})$"

                  messageWhenPatternMismatch="The phone number must contain 7, 10,

      or 11 digits. Hyphens are optional."

                  value="{!v.simpleNewContact.Phone}" required="true"/>

        <lightning:input aura:id="contactField" type="email" name="email" label="Email"

                  value="{!v.simpleNewContact.Email}" />

        <lightning:button label="Cancel" onclick="{!c.handleCancel}"

      class="slds-m-top_medium" />

        <lightning:button label="Save Contact" onclick="{!c.handleSaveContact}"

                   variant="brand" class="slds-m-top_medium"/>

      </aura:component>

```


Working with Salesforce Data Lightning Action Examples

```
     ldsQuickContactController.js

      ({

        doInit: function(component, event, helper) {

           component.find("contactRecordCreator").getNewRecord(

             "Contact", // objectApiName

             null, // recordTypeId

             false, // skip cache?

             $A.getCallback(function() {

               var rec = component.get("v.newContact");

               var error = component.get("v.newContactError");

               if(error || (rec === null)) {

                  console.log("Error initializing record template: " + error);

               }

               else {

                  console.log("Record template initialized: " + rec.apiName);

               }

             })

           );

        },

        handleSaveContact: function(component, event, helper) {

           if(helper.validateContactForm(component)) {

            component.set("v.simpleNewContact.AccountId", component.get("v.recordId"));

             component.find("contactRecordCreator").saveRecord(function(saveResult) {

               if (saveResult.state === "SUCCESS" || saveResult.state === "DRAFT") {

                  // Success! Prepare a toast UI message

                  var resultsToast = $A.get("e.force:showToast");

                  resultsToast.setParams({

                    "title": "Contact Saved",

                    "message": "The new contact was created."

                  });

                  // Update the UI: close panel, show toast, refresh account page

                  $A.get("e.force:closeQuickAction").fire();

                  resultsToast.fire();

                  // Reload the view so components not using force:recordData

                  // are updated

                  $A.get("e.force:refreshView").fire();

               }

               else if (saveResult.state === "INCOMPLETE") {

                  console.log("User is offline, device doesn't support drafts.");

               }

               else if (saveResult.state === "ERROR") {

                  console.log('Problem saving contact, error: ' +

                          JSON.stringify(saveResult.error));

               }

               else {

                  console.log('Unknown problem, state: ' + saveResult.state +

                         ', error: ' + JSON.stringify(saveResult.error));

               }

```


Working with Salesforce Data Lightning Action Examples

```
             });

           }

        },

        handleCancel: function(component, event, helper) {

           $A.get("e.force:closeQuickAction").fire();

        },

      })

```

Note: The callback passed to `getNewRecord()` must be wrapped in `$A.getCallback()` to ensure correct access
context when the callback is invoked. If the callback is passed in without being wrapped in `$A.getCallback()`, any
attempt to access private attributes of your component results in access check failures.

Even if you’re not accessing private attributes, it’s a best practice to always wrap the callback function for `getNewRecord()`
in `$A.getCallback()` . Never mix (contexts), never worry.

```
     ldsQuickContactHelper.js

      ({

        validateContactForm: function(component) {

           var validContact = true;

           // Show error messages if required fields are blank

           var allValid = component.find('contactField').reduce(function (validFields,

      inputCmp) {

             inputCmp.showHelpMessageIfInvalid();

             return validFields && inputCmp.get('v.validity').valid;

           }, true);

           if (allValid) {

             // Verify we have an account to attach it to

             var account = component.get("v.account");

             if($A.util.isEmpty(account)) {

               validContact = false;

               console.log("Quick action context doesn't have a valid account.");

             }

             return(validContact);

           }

        }

      })

```

Usage Differences

Consider the following differences between the previous examples.

**Field labels and values**
`lightning:recordViewForm` and `lightning:recordEditForm` obtain labels and the requiredness properties
from the object schema. In the first example, the `Last Name` field is a required field on the contact object. The component
provides field-level validation.

With `force:recordData`, you must provide your own labels and requiredness property for each field. You can also provide
your own field-level validation, as shown by the `lightning:input` component with the `pattern` and
`messageWhenPatternMismatch` attributes.


### Working with Salesforce Data SaveRecordResult

**Saving the record**
`lightning:recordEditForm` saves the record automatically when you provide a `lightning:button` component
with the `submit` type.

With `force:recordData`, you must call the `saveRecord` function.

**Lightning Data Service errors**
`lightning:recordViewForm` and `lightning:recordEditForm` display Lightning Data Service errors automatically
using `lightning:messages`, and provide custom error handling via the `onerror` event handler.

With `force:recordData`, you must handle and display the errors on your own.

SEE ALSO:

Configure Components for Record-Specific Actions

Controlling Access

### SaveRecordResult

Represents the result of a Lightning Data Service operation that makes a persistent change to record data.

### SaveRecordResult Object Callback functions for the saveRecord and deleteRecord functions receive a SaveRecordResult object as their only

argument.

**Attribute Name** **Type** **Description**

`objectApiName` String The object API name for the record.

`entityLabel` String The label for the name of the sObject of the record.

`error` String Error is one of the following.

**•** A localized message indicating what went wrong.

**•** An array of errors, including a localized message indicating what went wrong.
It might also include further data to help handle the error, such as field- or
page-level errors.

`error` is undefined if the save `state` is SUCCESS or DRAFT.

`recordId` String The 18-character ID of the record affected.

`state` String The result state of the operation. Possible values are:

**•** SUCCESS—The operation completed on the server successfully.

**•** DRAFT—The server wasn’t reachable, so the operation was saved locally as
a draft. The change is applied to the server when it’s reachable.

**•** INCOMPLETE—The server wasn’t reachable, and the device doesn’t support
drafts. (Drafts are supported only in the Salesforce app.) Try this operation
again later.

**•** ERROR—The operation couldn’t be completed. Check the `error` attribute
for more information.


### Working with Salesforce Data Displaying the Create and Edit Record Modals Displaying the Create and Edit Record Modals

You can take advantage of built-in events to display modals that let you create or edit records via an Aura component.

The `force:createRecord` and `force:editRecord` events display a create record page and edit record page in a modal
based on the default custom layout type for that object.

The following example contains a button that calls a client-side controller to display the edit record page. Add this example component
to a record page to inherit the record ID via the `force:hasRecordId` interface.

```
   <aura:component implements="flexipage:availableForRecordHome,force:hasRecordId" >

      <aura:attribute name="recordId" type="String" />

      <lightning:button label="Edit Record" onclick="{!c.edit}"/>

   </aura:component>

```

The client-side controller fires the `force:editRecord` event, which displays the edit record page for a given record ID.

```
   edit : function(component, event, helper) {

      var editRecordEvent = $A.get("e.force:editRecord");

      editRecordEvent.setParams({

        "recordId": component.get("v.recordId")

      });

      editRecordEvent.fire();

   }

```

Firing this event on a record page is similar to clicking the default Edit button on a record page’s header. Records updated using the
`force:editRecord` event are persisted automatically.

Note: If you don’t need the edit record page to display in a modal or if you need to specify a subset of fields, consider using
Lightning Data Service via `lightning:recordForm` or `lightning:recordEditForm` instead.

## Using Apex

Use Apex to write server-side code, such as controllers and test classes. Use Apex only if you need to customize your user interface to
do more than what Lightning Data Service allows, such as using a SOQL query to select certain records. Apex provisions data that’s not
managed and you must handle data refresh on your own.

Apex controllers handle requests from client-side controllers. For example, a client-side controller might handle an event and call an
Apex controller action to persist a record. An Apex controller can also load your record data.

Use Apex in these scenarios:

**•** [To work with objects that aren’t supported by User Interface API, such as Task and Event.](https://developer.salesforce.com/docs/atlas.en-us.260.0.uiapi.meta/uiapi/ui_api_get_started_supported_objects.htm)

**•** To work with operations that User Interface API doesn’t support, like loading a list of records by criteria (for example, to load the first
200 Accounts with Amount > $1M).

**•** To perform a transactional operation. For example, to create an account and create an opportunity associated with the new account.
If either create fails, the entire transaction is rolled back.

**•** To call a method imperatively, such as in response to clicking a button, or to delay loading to outside the critical path.


### Working with Salesforce Data Creating Server-Side Logic with Controllers

IN THIS SECTION:

### Creating Server-Side Logic with Controllers

The framework supports client-side (JavaScript) and server-side (Apex) controllers. An event is always wired to a client-side controller
action, which can in turn call an Apex controller action. For example, a client-side controller might handle an event and call an Apex
controller action to persist a record.

Testing Your Apex Code
Before you can upload a managed package, you must write and execute tests for your Apex code to meet minimum code coverage
requirements. Also, all tests must run without errors when you upload your package to AppExchange.

Making API Calls from Apex
Make API calls from an Apex controller. You can’t make Salesforce API calls from JavaScript code.

Make Long-Running Callouts with Continuations
Use the `Continuation` class in Apex to make a long-running request to an external web service. Process the response in a
callback method. Continuations are the preferred way to manage callouts because they can provide substantial improvements to
the user experience.

Creating Components in Apex
Creating components on the server side in Apex, using the `Cmp.<myNamespace>.<myComponent>` syntax, is deprecated.
Use `$A.createComponent()` in client-side JavaScript code instead.

### Creating Server-Side Logic with Controllers

The framework supports client-side (JavaScript) and server-side (Apex) controllers. An event is always wired to a client-side controller
action, which can in turn call an Apex controller action. For example, a client-side controller might handle an event and call an Apex
controller action to persist a record.

Server-side actions make a round trip from the client to the server and back again, so they usually complete more slowly than client-side
actions.

For more details on the process of calling a server-side action, see Calling a Server-Side Action on page 426.

IN THIS SECTION:

Apex Server-Side Controller Overview
Create a server-side controller in Apex and use the `@AuraEnabled` annotation to enable access to the controller method.

AuraEnabled Annotation Annotation
The `AuraEnabled` annotation enables Lightning components to access Apex methods and properties.

Creating an Apex Server-Side Controller
Use the Developer Console to create an Apex server-side controller.

Using Apex to Work with Salesforce Records
Use Apex only if you need to customize your user interface to do more than what Lightning Data Service allows, such as using a
SOQL query to select certain records. Apex provisions data that’s not managed and you must handle data refresh on your own.

Granting User Access for Apex Classes
An authenticated or guest user can access an `@AuraEnabled` Apex method only when the user’s profile or an assigned permission
set allows access to the Apex class.


Working with Salesforce Data Creating Server-Side Logic with Controllers

Securing Data in Apex Controllers
By default, Apex runs in system mode, which means that it runs with substantially elevated permissions, acting as if the user had
most permissions and all field- and object-level access granted. Because these security layers aren’t enforced like they are in the
Salesforce UI, you must write code to enforce them. Otherwise, your components may inadvertently expose sensitive data that
would normally be hidden from users in the Salesforce UI.

Calling a Server-Side Action
Call a server-side controller action from a client-side controller. In the client-side controller, you set a callback, which is called after
the server-side action is completed. A server-side action can return any object containing serializable JSON data.

Queuing of Server-Side Actions
The framework queues up actions before sending them to the server. Actions are grouped together into batches, and then sent to
the server together. This process enables the framework to reduce network traffic by batching multiple actions into fewer, more
efficient requests.

Storable Actions
Enhance your component’s performance by marking actions as storable (cacheable) to quickly show cached data from client-side
storage without waiting for a server trip. If the cached data is stale, the framework retrieves the latest data from the server. Caching
is especially beneficial for users on high latency, slow, or unreliable connections such as 3G networks.

Abortable Actions
Mark an action as abortable to make it potentially abortable while it's queued to be sent to the server. An abortable action in the
queue is not sent to the server if the component that created the action is no longer valid, that is `cmp.isValid() == false` .
A component is automatically destroyed and marked invalid by the framework when it is unrendered.

Action Limits and Considerations
Keep the following limits and other considerations in mind when using server-side actions.

#### Apex Server-Side Controller Overview

Create a server-side controller in Apex and use the `@AuraEnabled` annotation to enable access to the controller method.

Only methods that you have explicitly annotated with `@AuraEnabled` are exposed. Calling server-side actions aren’t counted against
your org’s API limits. However, your server-side controller actions are written in Apex, and as such are subject to all the usual Apex limits.
Apex limits are applied per action.

This Apex controller contains a `serverEcho` action that prepends a string to the value passed in.

```
   public with sharing class SimpleServerSideController {

      //Use @AuraEnabled to enable client- and server-side access to the method

      @AuraEnabled

      public static String serverEcho(String firstName) {

        return ('Hello from the server, ' + firstName);

      }

   }

```

In addition to using the `@AuraEnabled` annotation, your Apex controller must follow these requirements.

**•** Methods must be `static` and marked `public` or `global` . Non-static methods aren’t supported.

**•** If a method returns an object, instance methods that retrieve the value of the object’s instance field must be `public` .

**•** Use unique names for client-side and server-side actions in a component. A JavaScript function (client-side action) with the same
name as an Apex method (server-side action ) can lead to hard-to-debug issues. In debug mode, the framework logs a browser
console warning about the clashing client-side and server-side action names.


Working with Salesforce Data Creating Server-Side Logic with Controllers

Tip: Don’t store component state in your controller (client-side or server-side). Store state in a component’s client-side attributes
instead.

[For more information, see Classes in the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/)

SEE ALSO:

Calling a Server-Side Action

Creating an Apex Server-Side Controller

#### AuraEnabled Annotation Annotation

Apex Class Considerations for Packages

#### AuraEnabled Annotation Annotation The AuraEnabled annotation enables Lightning components to access Apex methods and properties. The AuraEnabled annotation is overloaded, and is used for two separate and distinct purposes.

**•** Use `@AuraEnabled` on Apex **class static methods** to make them accessible as remote controller actions in your Lightning
components.

**•** Use `@AuraEnabled` on Apex **instance methods and properties** to make them serializable when an instance of the class is
returned as data from a server-side action.

Important:

**•** Don’t mix-and-match these different uses of `@AuraEnabled` in the same Apex class.

**•** Only static `@AuraEnabled` Apex methods can be called from client-side code. Visualforce-style instance properties and
getter/setter methods aren’t available. Use client-side component attributes instead.

**•** You can’t use an Apex inner class as a parameter or return value for an Apex method that's called by an Aura component.

**•** You can't use the `@NamespaceAccessible` Apex annotation for an `@AuraEnabled` Apex method referenced from
an Aura component.

Component Security

In Apex, every method that is annotated `@AuraEnabled` should be treated as a web service interface. That is, the developer should
assume that an attacker can call this method with any parameter, even if the developer's client-side code does not invoke the method
[or invokes it using only sanitized parameters. For more information, see the Secure Coding Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.secure_coding_guide.meta/secure_coding_guide/secure_coding_lightning_security.htm)

For API version of 50.0 or higher, you must specify which users can access Apex classes that contain `@AuraEnabled` methods. For
[more information, see Salesforce Developers Blog: Breezing Through the Upcoming @AuraEnabled Critical Update.](https://developer.salesforce.com/blogs/2020/08/breezing-through-the-upcoming-auraenabled-critical-update)

Caching Method Results

To improve runtime performance, set `@AuraEnabled(cacheable=true)` to cache the method results on the client. To set
`cacheable=true`, a method must only get data. It can’t mutate data.

Marking a method as storable (cacheable) improves your component’s performance by quickly showing cached data from client-side
storage without waiting for a server trip. If the cached data is stale, the framework retrieves the latest data from the server. Caching is
especially beneficial for users on high latency, slow, or unreliable connections such as 3G networks.


Working with Salesforce Data Creating Server-Side Logic with Controllers

To cache data returned from an Apex method for any component with an API version of 44.0 or higher, you must annotate the Apex
method with `@AuraEnabled(cacheable=true)` . For example:

```
   @AuraEnabled(cacheable=true)

   public static Account getAccount(Id accountId) {

      // your code here

   }

```

Prior to API version 44.0, to cache data returned from an Apex method, you had to call `setStorable()` in JavaScript code on every
action that called the Apex method. For API version of 44.0 or higher, you must mark the Apex method as storable (cacheable) and you
can get rid of any `setStorable()` calls in JavaScript code. The Apex annotation approach is better because it centralizes your
caching notation for a method in the Apex class.

Note: Client-side storage is automatically configured in Lightning Experience and the Salesforce mobile app. A component
shouldn’t assume a cache duration because it may change as we optimize the platform.

Example: The `AccountController.cls` [Apex class from the github.com/trailheadapps/lwc-recipes repo shows how to](https://github.com/trailheadapps/lwc-recipes)
use `@AuraEnabled(cacheable=true)` .

Using Continuations

Use the `Continuation` class in Apex to make a long-running request to an external Web service.

Continuations use the `@AuraEnabled` annotation. Here are the rules for usage.

```
   @AuraEnabled(continuation=true)
```

An Apex controller method that returns a continuation must be annotated with `@AuraEnabled(continuation=true)` .

```
   @AuraEnabled(continuation=true cacheable=true)
```

To cache the result of a continuation action, set `cacheable=true` on the annotation for the Apex callback method.

Note: There’s a space, **not a comma**, between `continuation=true cacheable=true` .

SEE ALSO:

Returning Data from an Apex Server-Side Controller

Custom Apex Class Types

Storable Actions

Securing Data in Apex Controllers

@AuraEnabled Annotations for Continuations

_Apex Developer Guide_ [: NamespaceAccessible Annotation](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_annotation_NamespaceAccessible.htm)

#### Creating an Apex Server-Side Controller

Use the Developer Console to create an Apex server-side controller.

**1.** Open the Developer Console.

**2.** Click **File**    - **New**    - **Apex Class** .

**3.** Enter a name for your server-side controller.

**4.** Click **OK** .

**5.** Enter a method for each server-side action in the body of the class.


Working with Salesforce Data Creating Server-Side Logic with Controllers

Add the `@AuraEnabled` annotation to a method to expose it as a server-side action. Additionally, server-side actions must be

`static` methods, and either `global` or `public` .

**6.** Click **File**    - **Save** .

**7.** Open the component that you want to wire to the new controller class.

**8.** Add a `controller` system attribute to the `<aura:component>` tag to wire the component to the controller. For example:

```
     <aura:component controller="SimpleServerSideController">

```

SEE ALSO:

_Salesforce Help_ [: Open the Developer Console](https://help.salesforce.com/HTViewHelpDoc?id=code_dev_console_opening.htm&language=en_US)

Returning Data from an Apex Server-Side Controller

AuraEnabled Annotation Annotation

Granting User Access for Apex Classes

Apex Class Considerations for Packages

#### Using Apex to Work with Salesforce Records

Use Apex only if you need to customize your user interface to do more than what Lightning Data Service allows, such as using a SOQL
query to select certain records. Apex provisions data that’s not managed and you must handle data refresh on your own.

The term `sObject` refers to any object that can be stored in Lightning Platform. This could be a standard object, such as Account, or
a custom object that you create, such as a Merchandise object.

An `sObject` variable represents a row of data, also known as a record. To work with an object in Apex, declare it using the SOAP
API name of the object. For example:

```
   Account a = new Account();

   MyCustomObject__c co = new MyCustomObject__c();

```

[For more information on working on records with Apex, see Working with Data in Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_data_intro.htm)

This example controller persists an updated Account record. Note that the `update` method has the `@AuraEnabled` annotation,
which enables it to be called as a server-side controller action.

```
   public with sharing class AccountController {

      @AuraEnabled

      public static void updateAnnualRevenue(String accountId, Decimal annualRevenue) {

        Account acct = [SELECT Id, Name, BillingCity FROM Account WHERE Id = :accountId];

        acct.AnnualRevenue = annualRevenue;

        // Perform isAccessible() and isUpdateable() checks here

        update acct;

      }

   }

```

Note: When using Apex controllers, load the data once and pass it to child components as attributes. This approach reduces the
number of listeners and minimizes server calls, which improves performance and ensures that your components show consistent
data.


Working with Salesforce Data Creating Server-Side Logic with Controllers

Differences Between Lightning Data Service and Apex

The `lightning:record*Form` on page 382 and `force:recordData` components are the easiest way to work with records.
They are built on top of Lightning Data Service, which manages field-level security and sharing for you in addition to managing data
[loading and refresh. You can use these components for objects that are supported by User Interface API](https://developer.salesforce.com/docs/atlas.en-us.260.0.uiapi.meta/uiapi/ui_api_get_started_supported_objects.htm)

Use Apex only if you’re working with a scenario listed at Using Apex on page 415, You can call the Apex method imperatively, such as
in response to a button click, as shown in the **Loading Record Data from a Standard Object** section. Alternatively, to load record
data during component initialization, use the `init` handler, as shown in the **Loading Record Data By Criteria** section. When using
Apex to load or provision data, you must handle data refresh on your own by invoking the Apex method again.

Loading Record Data from an Object

Load records from an object in an Apex controller. The following Apex controller has methods that return a list of tasks. Task is an object
that isn’t supported by Lightning Data Service and the User Interface API. Therefore, we recommend using Apex to load task record data.

```
   public with sharing class TaskController {

      @AuraEnabled(cacheable=true)

      public static List<Task> getTasks() {

        return [SELECT Subject, Priority, Status FROM Task]; }

   }

```

This example component uses the previous Apex controller to display a list of task record data when you press a button. The
`flexipage:availableForAllPageTypes` interface denotes that you can use this example on a Lightning page.

```
   <!-- apexForTasks.cmp -->

   <aura:component implements="flexipage:availableForAllPageTypes" controller="TaskController">

      <aura:attribute name="tasks" type="Task[]"/>

      <lightning:card iconName="standard:task">

        <lightning:button label="Get Tasks" onclick="{!c.getMyTasks}"/>

        <aura:iteration var="task" items="{!v.tasks}">

           <p>{!task.Subject} : {!task.Priority}, {!task.Status}</p>

        </aura:iteration>

      </lightning:card>

   </aura:component>

```

When you press the button, the following client-side controller calls the `getTasks()` method and sets the `tasks` attribute on the
component. For more information about calling server-side controller methods, see Calling a Server-Side Action on page 426.

```
   // apexForTasksController.js

   ({

      getMyTasks: function(cmp){

        var action = cmp.get("c.getTasks");

        action.setCallback(this, function(response){

           var state = response.getState();

           if (state === "SUCCESS") {

             cmp.set("v.tasks", response.getReturnValue());

           }

        });

     $A.enqueueAction(action);

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

```
      }

   })

```

Loading Record Data By Criteria

As we’ve learned, to load a simple list of record data, you can use base components or `force:recordData`, as shown at Loading
a Record on page 383. But to use a SOQL query to select certain records, use an Apex controller.

Remember that the method must be `static`, and `global` or `public` . The method must be decorated with
`@AuraEnabled(cacheable=true)` .

For example, query related cases based on an account Id and limit the result to 10 records.

```
   public with sharing class CaseController {

      @AuraEnabled(cacheable=true)

      public static List<Case> getCases(String accountId) {

        return [SELECT AccountId, Id, Subject, Status, Priority, CaseNumber

             FROM Case

             WHERE AccountId = :accountId LIMIT 10];

      }

   }

```

The client-side controller loads related cases using the `init` handler. The `action.setParams()` method passes in the record
Id of the account record being viewed to the Apex controller,

```
   // casesForAccountController.js

   ({

      init : function(cmp, evt) {

        var action = cmp.get("c.getCases");

        action.setParams({

           "accountId": cmp.get("v.recordId")

        });

        action.setCallback(this, function(response){

           var state = response.getState();

           if (state === "SUCCESS") {

             cmp.set("v.cases", response.getReturnValue());

           }

        });

        $A.enqueueAction(action);

      }

   })

```

In your custom component, load a form that enables editing and updating of cases on an account record using
`lightning:recordEditForm`, by performing these steps.

**•** Query the relevant cases and set the result to the component attribute `v.cases` .

**•** Iterate over the cases by passing in the case Id to the `recordId` attribute on `lightning:recordEditForm` .

The example implements the `flexipage:availableForRecordHome` and `force:hasRecordId` interfaces so you can
use the example on an account record page.

```
   <!-- casesForAccount.cmp -->

   <aura:component implements="flexipage:availableForRecordHome,force:hasRecordId"

   controller="CaseController">

      <aura:attribute name="cases" type="Case[]"/>

      <aura:attribute name="recordId" type="Id" />

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

```
      <aura:handler name="init" value="{! this }" action="{! c.init }"/>

      <aura:iteration items="{!v.cases}" var="case">

        <lightning:card title="{!case.Id}" iconName="standard:case">

           <lightning:recordEditForm objectApiName="Case" recordId="{!case.Id}">

             <lightning:inputField fieldName="Subject"/>

             <lightning:inputField fieldName="Status"/>

             <!– Read-only field -->

             <lightning:outputField fieldName="Origin" variant="label-hidden"/>

             <lightning:button label="Update case" type="submit"/>

           </lightning:recordEditForm>

        </lightning:card>

      </aura:iteration>

   </aura:component>

```

Note: The case data on the account record is managed by Lightning Data Service since it uses `lightning:recordEditForm` ;
therefore, the case data that’s referenced (subject, status, and origin) reflects the latest data. However, if a case on the account is
deleted or a new case is added to the account, you must invoke the Apex method again to query the new results.

For read-only data, use `lightning:outputField` . To work with read-only data only, use `lightning:recordViewForm`
or `lightning:recordForm` . For granular control of your UI, use `force:recordData` . For more information, see Lightning
Data Service on page 382.

SEE ALSO:

#### Securing Data in Apex Controllers Granting User Access for Apex Classes

An authenticated or guest user can access an `@AuraEnabled` Apex method only when the user’s profile or an assigned permission
set allows access to the Apex class.

[For details on configuring user profile or permission set access to an Apex class, see Class Security in the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_security.htm)

SEE ALSO:

Creating an Apex Server-Side Controller

AuraEnabled Annotation Annotation

#### Securing Data in Apex Controllers Securing Data in Apex Controllers

By default, Apex runs in system mode, which means that it runs with substantially elevated permissions, acting as if the user had most
permissions and all field- and object-level access granted. Because these security layers aren’t enforced like they are in the Salesforce UI,
you must write code to enforce them. Otherwise, your components may inadvertently expose sensitive data that would normally be
hidden from users in the Salesforce UI.

Note: To work with Salesforce records, we recommend using Lightning Data Service, which handles sharing rules, CRUD, and
field-level security for you.


Working with Salesforce Data Creating Server-Side Logic with Controllers

Enforce Sharing Rules

When you declare a class, it’s a best practice to specify `with sharing` to enforce sharing rules when a component uses the Apex
controller.

```
   public with sharing class SharingClass {

      // Code here

   }

```

An `@AuraEnabled` Apex class that doesn’t explicitly set `with sharing` or `without sharing`, or is defined with `inherited`
`sharing`, uses a default or implicit value of `with sharing` . However, an Apex class that doesn’t explicitly set `with sharing`
or `without sharing` inherits the value from the context in which it runs. So when a class without explicit sharing behavior is called
by a class that sets one of the keywords, it operates with the sharing behavior of the calling class. To ensure that your class enforces
sharing rules, set `with sharing` .

The `with sharing` keyword enforces record-level security. It doesn’t enforce object-level and field-level security. You must manually
enforce object-level and field-level security separately in your Apex classes.

Enforce Object and Field Permissions (CRUD and FLS)

There are a few alternatives to enforce object-level and field-level permissions in your Apex code.

**Easiest enforcement using** **`WITH USER_MODE`**
To enforce object-level and field-level permissions, use the `WITH USER_MODE` clause for `SOQL SELECT` queries in Apex code,
including subqueries and cross-object relationships.

The `WITH USER_MODE` clause is ideal if you have minimal experience developing secure code and for applications that don’t
require graceful degradation on permissions errors.

This example queries fields on a custom expense object with an insecure method, `get_UNSAFE_Expenses()` . Don't use this
class!

```
     // This class is an anti-pattern.

     public with sharing class UnsafeExpenseController {

       // ns refers to namespace; leave out ns__ if not needed

       // This method is vulnerable because it doesn't enforce FLS.

       @AuraEnabled

       public static List<ns__Expense__c> get_UNSAFE_Expenses() {

          return [SELECT Id, Name, ns__Amount__c, ns__Client__c, ns__Date__c,

            ns__Reimbursed__c, CreatedDate FROM ns__Expense__c];

       }

     }

```

This next example uses a secure method, `getExpenses()`, which uses the `WITH USER_MODE` clause to enforce object-level
and field-level permissions. Use this class instead of `UnsafeExpenseController` .

```
     public with sharing class ExpenseController {

       // This method is recommended because it enforces FLS.

       @AuraEnabled

       public static List<ns__Expense__c> getExpenses() {

       // Query the object safely

       return [SELECT Id, Name, ns__Amount__c, ns__Client__c, ns__Date__c,

            ns__Reimbursed__c, CreatedDate

             FROM ns__Expense__c WITH USER_MODE];

       }

     }

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

[For more details, see Enforce User Mode for Database Operations in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_enforce_usermode.htm) _Apex Developer Guide_ .

**Graceful degradation with** **`stripInaccessible()`**
For more graceful degradation on permissions errors, use the `stripInaccessible()` method to enforce field- and object-level
data protection. This method strips the fields and relationship fields from query and subquery results that the user can’t access. You
can find out if any fields were stripped and throw an `AuraHandledException` with a custom error message, if desired.

You can also use the method to remove inaccessible sObject fields before DML operations to avoid exceptions and to sanitize
sObjects that have been deserialized from an untrusted source.

This example updates `ExpenseController` to use `stripInaccessible()` instead of the `WITH USER_MODE` SOQL
clause. The results are the same but `stripInaccessible()` gives you the opportunity to gracefully degrade instead of failing
on an access violation when using `WITH USER_MODE` .

```
     public with sharing class ExpenseControllerStripped {

       @AuraEnabled

       public static List<ns__Expense__c> getExpenses() {

          // Query the object but don't use WITH USER_MODE

          List<ns__Expense__c> expenses =

            [SELECT Id, Name, ns__Amount__c, ns__Client__c, ns__Date__c,

               ns__Reimbursed__c, CreatedDate

               FROM ns__Expense__c];

          // Strip fields that are not readable

          SObjectAccessDecision decision = Security.stripInaccessible(

              AccessType.READABLE,

              expenses);

          // Throw an exception if any data was stripped

          if (!decision.getModifiedIndexes().isEmpty()) {

            throw new AuraHandledException('Data was stripped');

          }

          return expenses;

       }

     }

```

[For more details and examples, see Enforce Security with the stripInaccessible Method in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_with_security_stripInaccessible.htm) _Apex Developer Guide_ .

**Legacy code using** **`DescribeSObjectResult`** **and** **`DescribeFieldResult`** **methods**
Before the `WITH USER_MODE` clause and `stripInaccessible()` method were available, the only way to enforce object
and field permissions was to check the current user’s access permission levels by calling the `Schema.DescribeSObjectResult`
and `Schema.DescribeFieldResult` methods. Then, if a user has the necessary permissions, perform a specific DML
operation or a query.

For example, you can call the `isAccessible`, `isCreateable`, or `isUpdateable` methods of
`Schema.DescribeSObjectResult` to verify whether the current user has read, create, or update access to an `sObject`,
respectively. Similarly, `Schema.DescribeFieldResult` exposes access control methods that you can call to check the
current user’s read, create, or update access for a field.

This example uses the describe result methods. This approach requires many more lines of boilerplate code so we recommend using
the `WITH USER_MODE` clause or `stripInaccessible()` method instead.

```
     public with sharing class ExpenseControllerLegacy {

       @AuraEnabled

       public static List<ns__Expense__c> getExpenses() {

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

```
          String [] expenseAccessFields = new String [] {'Id',

                                      'Name',

                                      'ns__Amount__c',

                                      'ns__Client__c',

                                      'ns__Date__c',

                                      'ns__Reimbursed__c',

                                      'CreatedDate'

                                      };

       // Obtain the field name/token map for the Expense object

       Map<String,Schema.SObjectField> m = Schema.SObjectType.ns__Expense__c.fields.getMap();

       for (String fieldToCheck : expenseAccessFields) {

          // Call getDescribe to check if the user has access to view field

          if (!m.get(fieldToCheck).getDescribe().isAccessible()) {

            // Pass error to client

            throw new System.NoAccessException();

          }

       }

       // Query the object safely

       return [SELECT Id, Name, ns__Amount__c, ns__Client__c, ns__Date__c,

            ns__Reimbursed__c, CreatedDate FROM ns__Expense__c];

       }

     }

```

SEE ALSO:

_Apex Developer Guide_ [: Enforcing Sharing Rules](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_security_sharing_rules.htm)

_Apex Developer Guide_ [: Enforcing Object and Field Permissions](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_perms_enforcing.htm)

_Apex Developer Guide_ [: Using the with sharing, without sharing, and inherited sharing Keywords](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

#### Calling a Server-Side Action

Call a server-side controller action from a client-side controller. In the client-side controller, you set a callback, which is called after the
server-side action is completed. A server-side action can return any object containing serializable JSON data.

A client-side controller is a JavaScript object in object-literal notation containing a map of name-value pairs.

Let’s say that you want to trigger a server-call from a component. The following component contains a button that’s wired to a client-side
controller `echo` action. `SimpleServerSideController` contains a method that returns a string passed in from the client-side
controller.

```
   <aura:component controller="SimpleServerSideController">

      <aura:attribute name="firstName" type="String" default="world"/>

      <lightning:button label="Call server" onclick="{!c.echo}"/>

   </aura:component>

```

This client-side controller includes an `echo` action that executes a `serverEcho` method on a server-side controller.


Working with Salesforce Data Creating Server-Side Logic with Controllers

Tip: Use unique names for client-side and server-side actions in a component. A JavaScript function (client-side action) with the
same name as an Apex method (server-side action ) can lead to hard-to-debug issues. In debug mode, the framework logs a
browser console warning about the clashing client-side and server-side action names.

```
   ({

      "echo" : function(cmp) {

        // create a one-time use instance of the serverEcho action

        // in the server-side controller

        var action = cmp.get("c.serverEcho");

        action.setParams({ firstName : cmp.get("v.firstName") });

        // Create a callback that is executed after

        // the server-side action returns

        action.setCallback(this, function(response) {

           var state = response.getState();

           if (state === "SUCCESS") {

             // Alert the user with the value returned

             // from the server

             alert("From server: " + response.getReturnValue());

             // You would typically fire a event here to trigger

             // client-side notification that the server-side

             // action is complete

           }

           else if (state === "INCOMPLETE") {

             // do something

           }

           else if (state === "ERROR") {

             var errors = response.getError();

             if (errors) {

               if (errors[0] && errors[0].message) {

                  console.log("Error message: " +

                       errors[0].message);

               }

             } else {

               console.log("Unknown error");

             }

           }

        });

        // optionally set storable, abortable, background flag here

        // A client-side action could cause multiple events,

        // which could trigger other events and

        // other server-side action calls.

        // $A.enqueueAction adds the server-side action to the queue.

        $A.enqueueAction(action);

      }

   })

```

In the client-side controller, we use the value provider of `c` to invoke a server-side controller action. We also use the `c` syntax in markup
to invoke a client-side controller action.

The `cmp.get("c.serverEcho")` call indicates that we’re calling the `serverEcho` method in the server-side controller. The
method name in the server-side controller must match everything after the `c.` in the client-side call. In this case, that’s `serverEcho` .


Working with Salesforce Data Creating Server-Side Logic with Controllers

The implementation of the `serverEcho` Apex method is shown in Apex Server-Side Controller Overview.

Use `action.setParams()` to set data to be passed to the server-side controller. The following call sets the value of the `firstName`
argument on the server-side controller’s `serverEcho` method based on the `firstName` attribute value.

```
   action.setParams({ firstName : cmp.get("v.firstName") });

```

`action.setCallback()` sets a callback action that is invoked after the server-side action returns.

```
   action.setCallback(this, function(response) { ... });

```

The server-side action results are available in the `response` variable, which is the argument of the callback.

`response.getState()` gets the state of the action returned from the server.

Note: You don’t need a `cmp.isValid()` check in the callback in a client-side controller when you reference the component
associated with the client-side controller. The framework automatically checks that the component is valid.

`response.getReturnValue()` gets the value returned from the server. In this example, the callback function alerts the user
with the value returned from the server.

`$A.enqueueAction(action)` adds the server-side controller action to the queue of actions to be executed. Actions that are
enqueued will run at the end of the event loop. Rather than sending a separate request for each individual action, the framework
processes the event chain and batches the queued actions into fewer, more efficient requests.

Actions are sent to the server asynchronously, and can execute and return in any order. Action callbacks are also asynchronous, and can
execute in a different order than the actions themselves. See Batching of Server-side Actions on page 437.

IN THIS SECTION:

##### Passing Data to an Apex Controller

Use `action.setParams()` in JavaScript to set data to pass to an Apex controller.

Returning Data from an Apex Server-Side Controller
Return results from a server-side controller to a client-side controller using the `return` statement. Results data must be serializable
into JSON format.

Returning Errors from an Apex Server-Side Controller
Create and throw a `System.AuraHandledException` from your Apex controller to return a custom error message to a
JavaScript controller.

Action States
Call a server-side controller action from a client-side controller. The action can have different states during processing.

SEE ALSO:

Handling Events with Client-Side Controllers

##### Passing Data to an Apex Controller

Queuing of Server-Side Actions

Action States

Checking Component Validity

Action Limits and Considerations

##### Passing Data to an Apex Controller

Use `action.setParams()` in JavaScript to set data to pass to an Apex controller.


Working with Salesforce Data Creating Server-Side Logic with Controllers

This example sets the value of the `firstName` argument on an Apex controller’s `serverEcho` method based on the `firstName`
attribute value.

```
   var action = cmp.get("c.serverEcho");

   action.setParams({ firstName : "Jennifer" });

```

The request payload includes the action data serialized into JSON.

Here's the Apex controller method.

```
   @AuraEnabled

   public static String serverEcho(String firstName) {

      return ('Hello from the server, ' + firstName);

   }

```

The framework deserializes the action data into the appropriate Apex type. In this example, we have a `String` parameter called
`firstName` .

Example with Different Data Types

Let's look at an application that sends data of various types to an Apex controller. Each button starts the sequence of passing data of a
different type.

```
   <!-- actionParamTypes.app -->

   <aura:application controller="ApexParamTypesController">

      <lightning:button label="putboolean" onclick="{!c.putbooleanc}"/>

      <lightning:button label="putint" onclick="{!c.putintc}"/>

      <lightning:button label="putlong" onclick="{!c.putlongc}"/>

      <lightning:button label="putdecimal" onclick="{!c.putdecimalc}"/>

      <lightning:button label="putdouble" onclick="{!c.putdoublec}"/>

      <lightning:button label="putstring" onclick="{!c.putstringc}"/>

      <lightning:button label="putobject" onclick="{!c.putobjectc}"/>

      <lightning:button label="putblob" onclick="{!c.putblobc}"/>

      <lightning:button label="putdate" onclick="{!c.putdatec}"/>

      <lightning:button label="putdatetime" onclick="{!c.putdatetimec}"/>

      <lightning:button label="puttime" onclick="{!c.puttimec}"/>

      <lightning:button label="putlistoflistoflistofstring"

   onclick="{!c.putlistoflistoflistofstringc}"/>

      <lightning:button label="putmapofstring" onclick="{!c.putmapofstringc}"/>

      <lightning:button label="putcustomclass" onclick="{!c.putcustomclassc}"/>

   </aura:application>

```

Here's the application's JavaScript controller. Each action calls the helper's `putdatatype` method, which queues up the actions to
send to the Apex controller. The method has three parameters:

**1.** The component

**2.** The Apex method name

**3.** The data to pass to the Apex method

```
   // actionParamTypesController.js

   ({

      putbooleanc : function(component, event, helper) {

        helper.putdatatype(component, "c.pboolean", true);

      },

      putintc : function(component, event, helper) {

        helper.putdatatype(component, "c.pint", 10);

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

```
      },

      putlongc : function(component, event, helper) {

        helper.putdatatype(component, "c.plong", 2147483648);

      },

      putdecimalc : function(component, event, helper) {

        helper.putdatatype(component, "c.pdecimal", 10.80);

      },

      putdoublec : function(component, event, helper) {

        helper.putdatatype(component, "c.pdouble", 10.80);

      },

      putstringc : function(component, event, helper) {

        helper.putdatatype(component, "c.pstring", "hello!");

      },

      putobjectc : function(component, event, helper) {

        helper.putdatatype(component, "c.pobject", true);

      },

      putblobc : function(component, event, helper) {

        helper.putdatatype(component, "c.pblob", "some blob as string");

      },

      // Date value is in ISO 8601 date format

      putdatec : function(component, event, helper) {

        helper.putdatatype(component, "c.pdate", "2020-01-31");

      },

      // Datetime value is in ISO 8601 datetime format

      putdatetimec : function(component, event, helper) {

        helper.putdatatype(component, "c.pdatetime", "2020-01-31T15:08:16.000Z");

      },

      // Set time in milliseconds.

      // You can use (new Date()).getTime() to set the milliseconds

      puttimec : function(component, event, helper) {

        helper.putdatatype(component, "c.ptime", 3723004);

        //helper.putdatatype(component, "c.ptime", (new Date()).getTime());

      },

      putlistoflistoflistofstringc : function(component, event, helper) {

        helper.putdatatype(component, "c.plistoflistoflistofstring",

   [[['a','b'],['c','d']],[['e','f']]]);

      },

      putmapofstringc : function(component, event, helper) {

        helper.putdatatype(component, "c.pmapofstring", {k1: 'v1'});

      },

      putcustomclassc : function(component, event, helper) {

        helper.putdatatype(component, "c.pcustomclass", {

           s: 'my string',

           i: 10,

           l: ['list value 1','list value 2'],

           m: {k1: 'map value'},

           os: {b: true}

        });

      },

   })

```

The helper has a utility method to send the data to an Apex controller.

```
   // actionParamTypesHelper.js

   ({

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

```
      putdatatype : function(component, actionName, val) {

        var action = component.get(actionName);

        action.setParams({ v : val });

        action.setCallback(this, function(response) {

           console.log(response.getReturnValue());

        });

        $A.enqueueAction(action);

      }

   })

```

Here's the Apex controller.

```
   public class ApexParamTypesController {

      @AuraEnabled

      public static Boolean pboolean(Boolean v){

        System.debug(v);

        return v;

      }

      @AuraEnabled

      public static Integer pint(Integer v){

        System.debug(v+v);

        return v;

      }

      @AuraEnabled

      public static Long plong(Long v){

        System.debug(v);

        return v;

      }

      @AuraEnabled

      public static Decimal pdecimal(Decimal v){

        System.debug(v);

        return v;

      }

      @AuraEnabled

      public static Double pdouble(Double v){

        System.debug(v);

        return v;

      }

      @AuraEnabled

      public static String pstring(String v){

        System.debug(v.capitalize());

        return v;

      }

      @AuraEnabled

      public static Object pobject(Object v){

        System.debug(v);

        return v;

      }

      @AuraEnabled

      public static Blob pblob(Blob v){

         System.debug(v.toString());

        return v;

      }

      @AuraEnabled

      public static Date pdate(Date v){

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

```
         System.debug(v);

        return v;

      }

      @AuraEnabled

      public static DateTime pdatetime(DateTime v){

        System.debug(v);

        return v;

      }

      @AuraEnabled

      public static Time ptime(Time v){

        System.debug(v);

        return v;

      }

      @AuraEnabled

     public static List<List<List<String>>> plistoflistoflistofstring(List<List<List<String>>>

    v){

        System.debug(v);

        return v;

      }

      @AuraEnabled

      public static Map<String, String> pmapofstring(Map<String, String> v){

        System.debug(v);

        return v;

      }

      @AuraEnabled

      public static MyCustomApexClass pcustomclass(MyCustomApexClass v){

        System.debug(v);

        return v;

      }

   }

```

The `pcustomclass()` Apex method has a parameter that's a custom Apex type, `MyCustomApexClass` . Each property in the
Apex class must have an `@AuraEnabled` annotation, as well as a getter and setter.

```
   public class MyCustomApexClass {

      @AuraEnabled

      public String s {get; set;}

      @AuraEnabled

      public Integer i {get; set;}

      @AuraEnabled

      public List<String> l {get; set;}

      @AuraEnabled

      public Map <String, String> m {get; set;}

      @AuraEnabled

      public MyOtherCustomApexClass os {get; set;}

   }

```

The `MyCustomApexClass` Apex class has a property with a type of another custom Apex class, `MyOtherCustomApexClass` .

```
   public class MyOtherCustomApexClass {

      @AuraEnabled

      public Boolean b {get; set;}

   }

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

[Note: When Lightning Web Security is enabled, you can’t use an Apex inner class as a parameter or return value for an Apex](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-intro.html)
method that's called by an Aura component.

SEE ALSO:

Queuing of Server-Side Actions

Apex Server-Side Controller Overview

##### Returning Data from an Apex Server-Side Controller

Return results from a server-side controller to a client-side controller using the `return` statement. Results data must be serializable
into JSON format.

Return data types can be any of the following.

**•** Simple—String, Integer, and so on. See Basic Types for details.

**•** sObject—standard and custom sObjects are both supported. See Standard and Custom Object Types.

**•** Apex—an instance of an Apex class. See Custom Apex Class Types. You can’t use an Apex inner class as a return value for an Apex
method that's called by an Aura component.

**•** Collection—a collection of any of the other types. See Collection Types.

Returning Apex Objects

Here’s an example of a controller that returns a collection of custom Apex objects.

```
   public with sharing class SimpleAccountController {

      @AuraEnabled

      public static List<SimpleAccount> getAccounts() {

        // Perform isAccessible() check here

        // SimpleAccount is a simple "wrapper" Apex class for transport

        List<SimpleAccount> simpleAccounts = new List<SimpleAccount>();

        List<Account> accounts = [SELECT Id, Name, Phone FROM Account LIMIT 5];

        for (Account acct : accounts) {

           simpleAccounts.add(new SimpleAccount(acct.Id, acct.Name, acct.Phone));

        }

        return simpleAccounts;

      }

   }

```

When an instance of an Apex class is returned from a server-side action, the framework serializes the return data into JSON format. Only
the values of `public` instance properties and methods annotated with `@AuraEnabled` are serialized and returned.

These Apex data types are serialized from `@AuraEnabled` properties and methods. They are supported as Aura component attributes.

**•** Primitive types except for BLOB

**•** Objects

**•** sObjects

**•** Lists and Maps if they hold elements of a supported type


Working with Salesforce Data Creating Server-Side Logic with Controllers

For example, here’s a wrapper Apex class that contains a few details for an account record. This class is used to package a few details of
an account record in a serializable format.

```
   public class SimpleAccount {

      @AuraEnabled public String Id { get; set; }

      @AuraEnabled public String Name { get; set; }

      public String Phone { get; set; }

      // Trivial constructor, for server-side Apex -> client-side JavaScript

      public SimpleAccount(String id, String name, String phone) {

        this.Id = id;

        this.Name = name;

        this.Phone = phone;

      }

      // Default, no-arg constructor, for client-side -> server-side

      public SimpleAccount() {}

   }

```

When returned from a remote Apex controller action, the Id and Name properties are defined on the client-side. However, because it
doesn’t have the `@AuraEnabled` annotation, the Phone property isn’t serialized on the server side, and isn’t returned as part of the
result data.

Note: Standard Apex limits, such as the maximum number of records retrieved by SOQL queries, apply when returning data from
[a server-side controller. See Execution Governors and Limits in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm) _Apex Developer Guide_ .

SEE ALSO:

AuraEnabled Annotation Annotation

Custom Apex Class Types

Calling a Server-Side Action

##### Returning Errors from an Apex Server-Side Controller

Create and throw a `System.AuraHandledException` from your Apex controller to return a custom error message to a JavaScript
controller.

Errors happen. Sometimes they’re expected, such as invalid input from a user, or a duplicate record in a database. Sometimes they’re
unexpected, such as... Well, if you’ve been programming for any length of time, you know that the range of unexpected errors is nearly
infinite.

When your Apex controller code experiences an error, two things can happen. You can use a catch block and handle the error in Apex.
Otherwise, the error is passed back in the controller’s response.

If you handle the error in Apex, you again have two ways you can go. You can process the error in a catch block, perhaps recovering
from it, and return a normal response to the client. Or, you can create and throw an `AuraHandledException` .

The benefit of throwing `AuraHandledException`, instead of letting a system exception be returned, is that you have a chance
to handle the exception more gracefully in your JavaScript controller code. System exceptions have important details stripped out for
security purposes, and result in the dreaded “An internal server error has occurred…” message. Nobody likes that. When you use an
`AuraHandledException` you have an opportunity to add some detail back into the response returned to your client-side code.
More importantly, you can choose a better message to show your users.


Working with Salesforce Data Creating Server-Side Logic with Controllers

Here’s an example of creating and throwing an `AuraHandledException` in response to bad input. However, the real benefit of
using `AuraHandledException` comes when you use it in response to a system exception. For example, throw an
`AuraHandledException` in response to catching a DML exception, instead of allowing the DML exception to propagate to your
client component code.

```
   public with sharing class SimpleErrorController {

      static final List<String> BAD_WORDS = new List<String> {

        'bad',

        'words',

        'here'

      };

      @AuraEnabled

      public static String helloOrThrowAnError(String name) {

        // Make sure we're not seeing something naughty

        for(String badWordStem : BAD_WORDS) {

           if(name.containsIgnoreCase(badWordStem)) {

             // How rude! Gracefully return an error...

             throw new AuraHandledException('NSFW name detected.');

           }

        }

        // No bad word found, so...

        return ('Hello ' + name + '!');

      }

   }

```

This JavaScript controller code handles the `AuraHandledException` thrown by the Apex controller.

```
   ({

      "callServer" : function(cmp) {

        var action = cmp.get("c.helloOrThrowAnError");

        action.setParams({ name : "bad" });

        action.setCallback(this, function(response) {

           var state = response.getState();

           if (state === "SUCCESS") {

             console.log("From server: " + response.getReturnValue());

           }

           else if (state === "INCOMPLETE") {

             // do something

           }

           else if (state === "ERROR") {

             var errors = response.getError();

             if (errors) {

               if (errors[0] && errors[0].message) {

                  // log the error passed in to AuraHandledException

                  console.log("Error message: " +

                       errors[0].message);

               }

             } else {

               console.log("Unknown error");

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

```
             }

           }

        });

        $A.enqueueAction(action);

      }

   })

```

When an Apex controller throws an `AuraHandledException`, the response state in the JavaScript controller is set to `ERROR` and
you can get the error message by processing `response.getError()` .

This example simply logs the error to the console. To display an error prompt in the UI, use the
`lightning:notificationsLibrary` component.

SEE ALSO:

_Salesforce Developers Blog_ [: Error Handling Best Practices for Lightning and Apex](https://developer.salesforce.com/blogs/2017/09/error-handling-best-practices-lightning-apex.html)

##### Action States

Call a server-side controller action from a client-side controller. The action can have different states during processing.

The possible action states are:

**NEW**
The action was created but is not in progress yet

**RUNNING**
The action is in progress

**SUCCESS**
The action executed successfully

**ERROR**
The server returned an error

**INCOMPLETE**
The server didn’t return a response. The server might be down or the client might be offline. The framework guarantees that an
action’s callback is always invoked as long as the component is valid. If the socket to the server is never successfully opened, or closes
abruptly, or any other network error occurs, the XHR resolves and the callback is invoked with state equal to `INCOMPLETE` .

**ABORTED**
The action was aborted. This action state is deprecated. A callback for an aborted action is executed only if you explicitly add a handler
for it.

SEE ALSO:

Calling a Server-Side Action

#### Queuing of Server-Side Actions

The framework queues up actions before sending them to the server. Actions are grouped together into batches, and then sent to the
server together. This process enables the framework to reduce network traffic by batching multiple actions into fewer, more efficient
requests.


Working with Salesforce Data Creating Server-Side Logic with Controllers

The framework uses a stack to track the actions to send to the server. When the browser finishes processing events and JavaScript on
the client, enqueued actions on the stack are sent to the server in a batch, or _boxcar_ . Multiple actions sent in the same boxcar are
processed in one transaction.

This mechanism is largely transparent to you when you’re writing code, as long as you follow a few simple guidelines. The most important
thing to keep in mind is that actions and responses are _asynchronous_ . Responses to actions can return in a different order than they were
sent. If one action depends on the results of another, **you** must manage the sequence and timing of the actions in your code. See
##### Batching of Server-side Actions on page 437 for more details and guidelines.

IN THIS SECTION:

##### Batching of Server-side Actions

Multiple queued actions are batched together into a group, and then sent to the server in a single request (XHR) to minimize network
round trips. The batching of actions is also known as _boxcar’ing_, similar to a train that couples boxcars together.

Foreground and Background Actions
Actions run in the foreground by default. You can set an action to run in the background. This feature is useful if you want your app
to remain responsive to a user while it executes a low priority, long-running action. A rough guideline is to use a background action
if it takes more than a few seconds for the response to return from the server.

SEE ALSO:

Action Limits and Considerations

Action States

##### Batching of Server-side Actions

Multiple queued actions are batched together into a group, and then sent to the server in a single request (XHR) to minimize network
round trips. The batching of actions is also known as _boxcar’ing_, similar to a train that couples boxcars together.

Important: The framework doesn’t guarantee any specific order of execution of actions or action callbacks. XHR responses can
return in a different order than the order in which the XHR requests were sent due to server processing time. If two actions must
execute sequentially, the component must orchestrate the ordering. For example, the component can enqueue the first action.
Then, in the first action’s callback, the component can enqueue the second, dependent action.

All actions sent in the same boxcar are processed in one transaction. If you see an error for “uncommitted work pending”, it’s possible
that a later action can’t be completed due to uncommitted work for an earlier action in the same transaction. For example, if the first
action updates a record, an Apex callout in a second action can’t be completed due to the uncommitted work from the first action.

The server returns the XHR response to the client when **all** actions have been processed on the server. If a long-running action is in the
boxcar, the XHR response is held until that long-running action completes.

Note: Set a long-running action as a background action to send that action separately from foreground actions. The separate
transmission ensures that the background action doesn’t impact the response time of the foreground actions. The motivation for
background actions is to isolate long-running actions into a separate request to avoid slowing the response for foreground actions.
See Foreground and Background Actions on page 441 for additional details.

IN THIS SECTION:

Boxcar Grouping and Optimization
On the client, the Aura Framework uses a process called _boxcar’ing_ to group together multiple server-side controller actions into
one network request. Boxcar’ing requests uses network resources more efficiently than sending each action separately.


Working with Salesforce Data Creating Server-Side Logic with Controllers

Manage Synchronous Action Dependencies
When your code has dependencies that require a prior action to complete, don’t call the dependent actions until the earlier action
completes. For example, render a dependent element conditionally, based on the result of the earlier action being available. Or call
the dependent action from the earlier action’s callback function. This ensures that the dependent call isn’t made until after the earlier
call completes.

Disable Dynamic Boxcar Optimization for Aura Actions
Dynamic boxcar optimization improves performance for most Lightning components and apps, including Lightning Experience
itself. If your org has components that are adversely affected by dynamic boxcar optimization, you can disable it for your org in Setup.

###### Boxcar Grouping and Optimization

On the client, the Aura Framework uses a process called _boxcar’ing_ to group together multiple server-side controller actions into one
network request. Boxcar’ing requests uses network resources more efficiently than sending each action separately.

Boxcar’ing of requests is handled automatically by the framework. Likewise, the framework determines when a boxcar is ready to be
[sent to the server, automatically managing network resources (XMLHttpRequest, or XHR).](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)

Beginning in Winter ’26, there are two boxcar optimization strategies.

**•** Dynamic (new in Winter ’26)

**•** Standard

Dynamic Boxcar Optimization

_Dynamic boxcar optimization_ is the new default way of grouping Aura actions into boxcars. It’s designed to improve the performance of
all Aura applications, and is especially effective with highly customized pages and heavy action loads.

Dynamic boxcar optimization limits the number of actions per boxcar based on the number of available XHR slots. It distributes actions
more evenly across available resources, allowing more parallel execution and improving overall responsiveness.

Although more actions from different components can execute in parallel, dynamic boxcar optimization ensures that actions from the
same component are kept together to preserve functional dependencies. The overall result is more efficient use of network resources,
faster response times, and a better user experience for Aura applications.

Standard Boxcar Optimization

With standard boxcar optimization, all queued actions could be combined into a single network request (XHR), with no upper limit on
the number of Aura actions in a single boxcar. This could lead to performance bottlenecks, especially if one slow action delayed the
response for all others.

Standard boxcar’ing works fine for most Aura applications. However, for some complex customization patterns, or in cases where it’s
impossible to separate long-running requests from shorter requests due to dependencies, standard boxcar’ing can be overwhelmed by
the number of requests added to a single boxcar. This bottleneck can lead to components and pages that behave poorly, with undesirable
lag times between loading a page, taking an action, and seeing results.

Choose a Boxcar Optimization Strategy

Recall that the framework doesn’t guarantee the order of execution of action callbacks. XHR responses can return in a different order
than the order in which the XHR requests were sent due to server processing time. This behavior is intentional and not new.

However, the improved performance of dynamic boxcar optimization can create greater variance in the order in which Aura actions are
sent to and returned from Salesforce. These timing changes have the potential to expose logic errors in your component code, where
calls that depend on synchronous execution no longer run in the same, specific order.


Working with Salesforce Data Creating Server-Side Logic with Controllers

That is, standard boxcar optimization very often produced sequential behavior, even though the framework doesn’t _guarantee_ it. Your
code can have logic errors that depend on this sequential behavior, which you’ve never had a problem with previously. Dynamic boxcar
optimization, while performing better, can expose those software defects in real world use.

If you discover that you have implicit sequential dependencies in your component code, you have two options.

###### • Fix the problem. Manage Synchronous Action Dependencies on page 439 explains the issue in more detail, and provides code-based

solutions.

**•** **Disable dynamic boxcar optimization.** This resolution is quick to implement in Setup, but you lose the benefits of dynamic boxcar
optimization on **all** of your components, not just the components with problems. See Disable Dynamic Boxcar Optimization for
Aura Actions on page 441.

###### Manage Synchronous Action Dependencies

When your code has dependencies that require a prior action to complete, don’t call the dependent actions until the earlier action
completes. For example, render a dependent element conditionally, based on the result of the earlier action being available. Or call the
dependent action from the earlier action’s callback function. This ensures that the dependent call isn’t made until after the earlier call
completes.

Example: **Hidden Dependencies in a Canvas Component**

When a child component calls hidden lifecycle actions, timing errors can occur more frequently with dynamic boxcar optimization.
For example, this Aura component uses the `fetchCanvasParameters` action to retrieve values from a server-side Apex
controller in its `init` handler, and then passes the retrieved values as parameters to a child component.

```
      <!-- canvasExample.cmp -->

      <aura:component controller="CanvasExampleController" >

        <aura:attribute name="canvasParameters" type="Map"/>

        <aura:handler name="init" value="{!this}"

            action="{!c.fetchCanvasParameters}"/>

        <force:canvasApp developerName="{!v.AppName}" scrolling="auto"

            width="100%" height="100%" title="{!v.title}"

            parameters="{!v.canvasParameters}" />

      </aura:component>

```

Note: The component helper and server-side Apex controller aren’t relevant to understanding this issue, and don’t require
changes. They are included after the explanation and fix, for completeness.

Behind the scenes, the child `<force:canvasApp>` component calls its own lifecycle action `getCanvasAppData` to
retrieve the Canvas app’s metadata. The order of these two action calls— `fetchCanvasParameters` and
`getCanvasAppData` —isn’t obvious because the call to `getCanvasAppData` is implicit. More importantly, the order in
which they return isn’t guaranteed. With standard boxcar grouping, both calls were _usually_ grouped together in the same boxcar,
which _usually_ ensured that they completed in the correct order.

With dynamic boxcar optimization, the framework has more flexibility in how it groups actions into boxcars, using more XHR slots
to send actions separately to avoid bottlenecks. It's much more likely that the two actions are sent in different boxcars. The use of
separate boxcars greatly increases the possibility that the `<force:canvasApp>` component is instantiated and makes another
call in another boxcar before the component parameters are returned in the parent component’s `init` handler. As you can
imagine, this change in sequence can cause any number of problems.

Important: **This behavior of the framework is intentional** . Even with standard boxcar grouping, it was always possible
for the original code to have timing problems because of its dependency on sequential action in an asynchronous framework.
Boxcar grouping behavior is an implementation detail, and the behavior changes with dynamic boxcar optimization. Design


Working with Salesforce Data Creating Server-Side Logic with Controllers

your components and apps to avoid synchronous dependencies because synchronous behavior isn’t guaranteed by the
framework, regardless of boxcar implementation.

The simplest and easiest way to resolve this issue is to conditionally render the `<force:canvasApp>` component only if the
initial response values are available, that is, after the `fetchCanvasParameters` action has completed.

```
      <!-- canvasExampleFixed.cmp -->

      <aura:component controller="CanvasExampleController" >

        <aura:attribute name="canvasParameters" type="Map"/>

        <aura:handler name="init" value="{!this}"

            action="{!c.fetchCanvasParameters}"/>

         <aura:if isTrue="{!v.canvasParameters}">

           <force:canvasApp developerName="{!v.AppName}" scrolling="auto"

            width="100%" height="100%" title="{!v.title}"

            parameters="{!v.canvasParameters}" />

         </aura:if>

      </aura:component>

```

By wrapping the child `<force:canvasApp>` component in an `<aura:if>` block, the creation of the
`<force:canvasApp>` component is deferred until after the call to the `fetchCanvasParameters` action completes.

For completeness, here’s the Aura component helper, which contains the `fetchCanvasParameters` action, and the
server-side Apex controller method that returns the Canvas app parameters that the child `<force:canvasApp>` component
can use.

```
      # canvasExampleHelper.js

      ({

        fetchCanvasParameters : function(component, event, helper) {

           var action = component.get("c.getCanvasParameters");

           action.setCallback(this, function(response) {

             var state = response.getState();

             if (state === "SUCCESS") {

               component.set("v.canvasParameters",

                  response.getReturnValue());

             }

           });

           $A.enqueueAction(action);

        }

      })

      # CanvasExampleController.apex

      public with sharing class CanvasExampleController {

        @AuraEnabled

        public static Map<String, Object> getCanvasParameters() {

           // Example: return some parameters

           Map<String, Object> params = new Map<String, Object>();

           params.put('param1', 'value1');

           params.put('param2', 123);

           return params;

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

```
        }

      }

```

SEE ALSO:

Boxcar Grouping and Optimization

###### Disable Dynamic Boxcar Optimization for Aura Actions

Dynamic boxcar optimization improves performance for most Lightning components and apps, including Lightning Experience itself.
If your org has components that are adversely affected by dynamic boxcar optimization, you can disable it for your org in Setup.

Dynamic boxcar optimization was introduced in Winter ’26, and improves the performance of the Lightning Components Framework
for all orgs. You should only disable it if your component code contains timing dependencies that depend on standard boxcar grouping.
Treat such dependencies as software defects that need to be corrected.

**1.** From Setup, in the Quick Find box, enter _`Session Settings`_, and then select **Security**    - **Session Settings** .

**2.** In the **Aura action Settings** section, check the **Disable new Aura boxcar mechanism that efficiently batches Aura actions**
**across available XHR slots for optimal performance** option.

**3.** Click **Save** .

We strongly recommend that you only disable dynamic boxcar optimization as a temporary measure while you correct your component
code. Sequential or synchronous timing dependencies in your code are to be avoided, no matter which boxcar’ing strategy is enabled
for your org.

##### Foreground and Background Actions

Actions run in the foreground by default. You can set an action to run in the background. This feature is useful if you want your app to
remain responsive to a user while it executes a low priority, long-running action. A rough guideline is to use a background action if it
takes more than a few seconds for the response to return from the server.

When enqueued actions are grouped into boxcars and sent to the server, foreground actions are processed first, followed by background
actions. Don’t rely on each background action being sent in its own request as that behavior isn’t guaranteed. On the server, foreground
actions run in parallel with background actions, and responses for foreground and background actions can come back in either order.

Framework-Managed Request Throttling

The framework manages and enqueues foreground and background requests separately. This means that the framework can control
the number of foreground requests and the number of background actions running at any time. The framework automatically throttles
the rate of sending these requests. Other than setting an action to run in the background, you can’t control the framework’s request
processing. The framework manages the number of foreground and background XHRs, which varies depending on available resources
and the boxcar’ing strategy enabled in your org.

Even with separate throttling, background actions can affect performance in some conditions, such as when there is an excessive number
of requests to the server.

Setting Background Actions

To set an action as a background action, call the `setBackground()` method on the action object in JavaScript.

```
   // create a server-side action

   var action = cmp.get("c.serverEcho");

```


Working with Salesforce Data Creating Server-Side Logic with Controllers

```
   // optionally set actions params

   // action.setParams({ firstName : cmp.get("v.firstName") });

   // set as a background action

   action.setBackground();

```

Note: A background action can’t be set back to a foreground action. `setBackground` takes no arguments, and calling
`setBackground` more than once has no effect.

SEE ALSO:

Boxcar Grouping and Optimization

Queuing of Server-Side Actions

Calling a Server-Side Action

#### Storable Actions

Enhance your component’s performance by marking actions as storable (cacheable) to quickly show cached data from client-side storage
without waiting for a server trip. If the cached data is stale, the framework retrieves the latest data from the server. Caching is especially
beneficial for users on high latency, slow, or unreliable connections such as 3G networks.

Warning:

**•** A storable action might result in no call to the server. Never mark as storable an action that updates or deletes data.

**•** For storable actions in the cache, the framework returns the cached response immediately and also refreshes the data if it’s
stale. Therefore, storable actions might have their callbacks invoked more than once: first with cached data, then with updated
data from the server.

Most server requests are read-only and idempotent, which means that a request can be repeated or retried as often as necessary without
causing data changes. The responses to idempotent actions can be cached and quickly reused for subsequent identical actions. For
storable actions, the key for determining an identical action is a combination of:

**•** Apex controller name

**•** Method name

**•** Method parameter values

Note: Client-side storage is automatically configured in Lightning Experience and the Salesforce mobile app. A component
shouldn’t assume a cache duration because it may change as we optimize the platform.

Marking an Action as Storable

To cache data returned from an Apex method for any component with an API version of 44.0 or higher, you must annotate the Apex
method with `@AuraEnabled(cacheable=true)` . For example:

```
   @AuraEnabled(cacheable=true)

   public static Account getAccount(Id accountId) {

      // your code here

   }

```

Prior to API version 44.0, to cache data returned from an Apex method, you had to call `setStorable()` in JavaScript code on every
action that called the Apex method. For API version of 44.0 or higher, you can mark the Apex method as storable (cacheable) and get


Working with Salesforce Data Creating Server-Side Logic with Controllers

rid of any `setStorable()` calls in JavaScript code. The Apex annotation approach is better because it centralizes your caching
notation for a method in the Apex class.

Call `setStorable()` on an action in JavaScript code, as follows.

```
   action.setStorable();

```

The `setStorable` function takes an optional argument, which is a configuration map of key-value pairs representing the storage
options and values to set. You can only set the following property:

```
   ignoreExisting
```

Set to `true` to bypass the cache. The default value is `false` .

This property is useful when you know that any cached data is invalid, such as after a record modification. This property should be
used rarely because it explicitly defeats caching.

To set the storage options for the action response, pass this configuration map into `setStorable(` _**`configObj`**_ `)` .

IN THIS SECTION:

##### Lifecycle of Storable Actions

This image describes the sequence of callback execution for storable actions.

Enable Storable Actions in an Application
To use storable actions in a standalone app ( `.app` resource), you must configure client-side storage for cached action responses.

Storage Service Adapters
The Storage Service supports multiple implementations of storage and selects an adapter at runtime based on browser support and
specified characteristics of persistence and security. Storage can be persistent and secure. With persistent storage, cached data is
preserved between user sessions in the browser. With secure storage, cached data is encrypted.

##### Lifecycle of Storable Actions

This image describes the sequence of callback execution for storable actions.

Note: An action might have its callback invoked more than once:

**•** First with the cached response, if it’s in storage.

**•** Second with updated data from the server, if the stored response has exceeded the time to refresh entries.


Working with Salesforce Data Creating Server-Side Logic with Controllers

Cache Miss

If the action is not a cache hit as it doesn’t match a storage entry:

**1.** The action is sent to the server-side controller.

**2.** If the response is `SUCCESS`, the response is added to storage.

**3.** The callback in the client-side controller is executed.

Cache Hit

If the action is a cache hit as it matches a storage entry:

**1.** The callback in the client-side controller is executed with the cached action response.

**2.** If the response has been cached for longer than the refresh time, the storage entry is refreshed.

When an application enables storable actions, a refresh time is configured. The refresh time is the duration in seconds before an
entry is refreshed in storage. The refresh time is automatically configured in Lightning Experience and the Salesforce mobile app.

**3.** The action is sent to the server-side controller.

**4.** If the response is `SUCCESS`, the response is added to storage.

**5.** If the refreshed response is different from the cached response, the callback in the client-side controller is executed for a second
time.

SEE ALSO:

Storable Actions

##### Enable Storable Actions in an Application Enable Storable Actions in an Application

To use storable actions in a standalone app ( `.app` resource), you must configure client-side storage for cached action responses.


Working with Salesforce Data Creating Server-Side Logic with Controllers

Note: Client-side storage is automatically configured in Lightning Experience and the Salesforce mobile app. A component
shouldn’t assume a cache duration because it may change as we optimize the platform.

To configure client-side storage for your standalone app, use `<auraStorage:init>` in the `auraPreInitBlock` attribute of
your application’s template. For example:

```
   <aura:component isTemplate="true" extends="aura:template">

      <aura:set attribute="auraPreInitBlock">

        <auraStorage:init

         name="actions"

         persistent="false"

         secure="true"

         maxSize="1024"

         defaultExpiration="900"

         defaultAutoRefreshInterval="30" />

      </aura:set>

   </aura:component>

   name
```

The storage name must be `actions` . Storable actions are the only currently supported type of storage.

```
   persistent
```

Set to `true` to preserve cached data between user sessions in the browser.

```
   secure
```

Set to `true` to encrypt cached data.

```
   maxsize
```

The maximum size in KB of the storage.

```
   defaultExpiration
```

The duration in seconds that an entry is retained in storage.

```
   defaultAutoRefreshInterval
```

The duration in seconds before an entry is refreshed in storage.

Storable actions use the Storage Service. The Storage Service supports multiple implementations of storage and selects an adapter at
runtime based on browser support and specified characteristics of persistence and security.

SEE ALSO:

##### Storage Service Adapters Storage Service Adapters

The Storage Service supports multiple implementations of storage and selects an adapter at runtime based on browser support and
specified characteristics of persistence and security. Storage can be persistent and secure. With persistent storage, cached data is preserved
between user sessions in the browser. With secure storage, cached data is encrypted.

**Storage Adapter Name** **Persistent** **Secure**

IndexedDB `true` `false`

Memory `false` `true`


Working with Salesforce Data Creating Server-Side Logic with Controllers

**IndexedDB**
(Persistent but not secure) Provides access to an API for client-side storage and search of structured data. For more information, see
[the Indexed Database API.](http://www.w3.org/TR/IndexedDB/)

**Memory**
(Not persistent but secure) Provides access to JavaScript memory for caching data. The stored cache persists only per browser page.
Browsing to a new page resets the cache.

The Storage Service selects a storage adapter on your behalf that matches the persistent and secure options you specify when initializing
the service. For example, if you request a persistent and insecure storage service, the Storage Service returns the IndexedDB storage if
the browser supports it.

#### Abortable Actions

Mark an action as abortable to make it potentially abortable while it's queued to be sent to the server. An abortable action in the queue
is not sent to the server if the component that created the action is no longer valid, that is `cmp.isValid() == false` . A component
is automatically destroyed and marked invalid by the framework when it is unrendered.

Note: We recommend that you only use abortable actions for read-only operations as they are not guaranteed to be sent to the
server.

An abortable action is sent to the server and executed normally unless the component that created the action is invalid before the action
is sent to the server.

A non-abortable action is always sent to the server and can't be aborted in the queue.

If an action response returns from the server and the associated component is now invalid, the logic has been executed on the server
but the action callback isn’t executed. This is true whether or not the action is marked as abortable.

Marking an Action as Abortable

#### Mark a server-side action as abortable by using the setAbortable() method on the Action object in JavaScript. For example:

```
   var action = cmp.get("c.serverEcho");

   action.setAbortable();

```

SEE ALSO:

Events Fired During the Rendering Lifecycle

Creating Server-Side Logic with Controllers

Queuing of Server-Side Actions

Calling a Server-Side Action

#### Action Limits and Considerations

Keep the following limits and other considerations in mind when using server-side actions.

Client Payload Data Limit

Use `action.setParams()` to set data for an action to be passed to a server-side controller.

The framework batches the actions in the queue into one server request. The request payload includes all of the actions and their data
serialized into JSON. The request payload limit is 4 MB.


### Working with Salesforce Data Testing Your Apex Code

Action Limit in a Boxcar Request

The framework returns a 413 HTTP response status code if there are more than 250 actions in a boxcar request. If a user sees this rare
error, consider redesigning your custom component to follow best practices and reduce the number of actions in a request.

Actions and the Component Lifecycle

If your action isn’t executing, make sure that you’re not executing code outside the framework’s normal rendering lifecycle. For example,
if you use `window.setTimeout()` in an event handler to execute some logic after a time delay, wrap your code in
`$A.getCallback()` .

You don't need to use `$A.getCallback()` if your code is executed as part of the framework's call stack; for example, your code is
handling an event or in the callback for a server-side controller action.

SEE ALSO:

Events Fired During the Rendering Lifecycle

Modifying Components Outside the Framework Lifecycle

### Testing Your Apex Code

Before you can upload a managed package, you must write and execute tests for your Apex code to meet minimum code coverage
requirements. Also, all tests must run without errors when you upload your package to AppExchange.

To package your application and components that depend on Apex code, the following must be true.

**•** Unit tests must cover at least 75% of your Apex code, and all of those tests must complete successfully.

Note the following.

**–** When deploying Apex to a production organization, each unit test in your organization namespace is executed by default.

**–** Calls to `System.debug` aren’t counted as part of Apex code coverage.

**–** Test methods and test classes aren’t counted as part of Apex code coverage.

**–** While only 75% of your Apex code must be covered by tests, don’t focus on the percentage of code that is covered. Instead,
make sure that every use case of your application is covered, including positive and negative cases, as well as bulk and single
records. This approach ensures that 75% or more of your code is covered by unit tests.

**•** Every trigger must have some test coverage.

**•** All classes and triggers must compile successfully.

This sample shows an Apex test class for a custom object that’s wired up to a component.

```
   @isTest

   class TestExpenseController {

      static testMethod void test() {

        //Create new expense and insert it into the database

        Expense__c exp = new Expense__c(name='My New Expense',

                     amount__c=20, client__c='ABC',

                     reimbursed__c=false, date__c=null);

         ExpenseController.saveExpense(exp);

        //Assert the name field and saved expense

        System.assertEquals('My New Expense',

                    ExpenseController.getExpenses()[0].Name,

```


### Working with Salesforce Data Making API Calls from Apex

```
                   'Name does not match');

        System.assertEquals(exp, ExpenseController.saveExpense(exp));

      }

   }

```

Note: Apex classes must be manually added to your package.

[For more information on distributing Apex code, see Debugging, Testing, and Deploying Apex in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_debug_test_deploy.htm) _Apex Developer Guide_ .

SEE ALSO:

Distributing Applications and Components

### Making API Calls from Apex

Make API calls from an Apex controller. You can’t make Salesforce API calls from JavaScript code.

For security reasons, the Lightning Component framework places restrictions on making API calls from JavaScript code. To call third-party
APIs from your component’s JavaScript code, add the API endpoint as a CSP Trusted Site.

To call Salesforce APIs, make the API calls from your component’s Apex controller. Use a named credential to authenticate to Salesforce.

Note: By security policy, sessions created by Lightning components aren’t enabled for API access. This prevents even your Apex
code from making API calls to Salesforce. Using a named credential for specific API calls allows you to carefully and selectively
bypass this security restriction.

The restrictions on API-enabled sessions aren’t accidental. Carefully review any code that uses a named credential to ensure you’re
not creating a vulnerability.

[For information about making API calls from Apex, see the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts.htm)

SEE ALSO:

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

Making API Calls from Components

### Make Long-Running Callouts with Continuations

Use the `Continuation` class in Apex to make a long-running request to an external web service. Process the response in a callback
method. Continuations are the preferred way to manage callouts because they can provide substantial improvements to the user
experience.

Using continuations has some advantages, including the capability to make callouts in parallel.

The framework queues up actions before sending them to the server. This mechanism is largely transparent to you when you’re writing
code but it enables the framework to minimize network traffic by batching multiple actions into one request (XHR). The batching of
actions is also known as boxcar’ing, similar to a train that couples boxcars together. Since continuations can be long-running requests,
the framework essentially treats continuations as background actions. Continuations aren't boxcar'ed with other requests so they don't
block other actions while they are running.

An asynchronous callout made with a continuation doesn’t count toward the Apex limit of synchronous requests that last longer than
five seconds. Since Winter ’20, all callouts are excluded from the long-running request limit so continuations no longer offer an advantage
for working with limits compared to regular callouts. However, we recommend using continuations to manage callouts due to the
improved user experience.


Working with Salesforce Data Make Long-Running Callouts with Continuations

IN THIS SECTION:

#### Work with a Continuation in an Apex Class

To work with a continuation in an Apex class, use the Apex `Continuation` object.

@AuraEnabled Annotations for Continuations
Continuations use the `@AuraEnabled` annotation for Apex code. Here are the rules for usage.

Aura Component Continuations Example
Here’s the markup for a component with a button that starts the process of calling a continuation.

Continuation-Specific Limits
Because continuations can lead to multiple long-running actions, there are some limits on their usage.

SEE ALSO:

Queuing of Server-Side Actions

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Continuation.htm)_ : Continuation Class

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

#### Work with a Continuation in an Apex Class

To work with a continuation in an Apex class, use the Apex `Continuation` object.

**1.** Before you can call an external service, you must add the remote site to a list of authorized remote sites in the Salesforce user interface.
From **Setup**, in the **Quick Find** box, enter _`Remote Site Settings`_ . Select **Remote Site Settings**, and then click **New**
**Remote Site** . Add the callout URL corresponding to `LONG_RUNNING_SERVICE_URL` in the Apex Class Continuation example
below.

If the callout specifies a named credential as the endpoint, you don’t need to configure remote site settings. A named credential
specifies the URL of a callout endpoint and its required authentication parameters in one definition. In your code, specify the named
credential URL instead of the long-running service URL.

**2.** To make a long-running callout, define an Apex method that returns a `Continuation` object. (Don’t worry about the attributes
of the `@AuraEnabled` annotation yet. We explain that soon.)

```
     @AuraEnabled(continuation=true cacheable=true)

     public static Object startRequest() {

       // Create continuation. Argument is timeout in seconds.

       Continuation con = new Continuation(40);

       // more to come here

       return con;

     }

```

**3.** Set an Apex callback method to be invoked after the callout completes in the `continuationMethod` property of the
`Continuation` object. In this example, the callback method is `processResponse` . The callback method must be in the
same Apex class.

```
     con.continuationMethod='processResponse';

```

**4.** Set the endpoint for a callout by adding an `HttpRequest` object to the `Continuation` object. A single `Continuation`
object can contain a maximum of three callouts. Each callout must have a remote site or named credential defined in Setup.

```
     HttpRequest req = new HttpRequest();

     req.setMethod('GET');

```


Working with Salesforce Data Make Long-Running Callouts with Continuations

```
     req.setEndpoint(LONG_RUNNING_SERVICE_URL);

     con.addHttpRequest(req);

```

**5.** Set data to pass to the callback method in the `state` property of the `Continuation` object. The `state` property has an

`Object` type so you can pass in any data type that’s supported in Apex.

```
     con.state='Hello, World!';

```

**6.** Code the logic in the Apex callback. When all the callouts set in the `Continuation` object have completed, the Apex callback
method, `processResponse`, is invoked. The callback method has two parameters that you can access.

```
     public static Object processResponse(List<String> labels, Object state)

```

**a.** `labels` —A list of labels, one for each request in the continuation. These labels are automatically created.

**b.** `state` —The state that you set in the `state` property in your `Continuation` object.

**7.** Get the response for each request in the continuation. For example:

```
     HttpResponse response = Continuation.getResponse(labels[0]);

```

**8.** Return the results to the JavaScript controller.

Complete Apex Class Example with Continuation

Here’s a complete Apex class that ties together all the earlier steps.

```
   public with sharing class SampleContinuationClass {

      // Callout endpoint as a named credential URL

      // or, as shown here, as the long-running service URL

      private static final String LONG_RUNNING_SERVICE_URL =

        '<insert your callout URL here>';

      // Action method

      @AuraEnabled(continuation=true cacheable=true)

      public static Object startRequest() {

       // Create continuation. Argument is timeout in seconds.

       Continuation con = new Continuation(40);

       // Set callback method

       con.continuationMethod='processResponse';

       // Set state

       con.state='Hello, World!';

       // Create callout request

       HttpRequest req = new HttpRequest();

       req.setMethod('GET');

       req.setEndpoint(LONG_RUNNING_SERVICE_URL);

       // Add callout request to continuation

       con.addHttpRequest(req);

       // Return the continuation

       return con;

      }

      // Callback method

      @AuraEnabled(cacheable=true)

      public static Object processResponse(List<String> labels, Object state) {

```


Working with Salesforce Data Make Long-Running Callouts with Continuations

```
       // Get the response by using the unique label

       HttpResponse response = Continuation.getResponse(labels[0]);

       // Set the result variable

       String result = response.getBody();

       return result;

      }

   }

```

SEE ALSO:

Make Long-Running Callouts with Continuations

#### @AuraEnabled Annotations for Continuations Continuations use the @AuraEnabled annotation for Apex code. Here are the rules for usage.

```
   @AuraEnabled(continuation=true)
```

An Apex controller method that returns a continuation must be annotated with `@AuraEnabled(continuation=true)` .

```
   @AuraEnabled(continuation=true cacheable=true)
```

To cache the result of a continuation action, set `cacheable=true` on the annotation for the Apex callback method.

Note: There’s a space, **not a comma**, between `continuation=true cacheable=true` .

Caching Considerations

It's best practice to set `cacheable=true` on all methods involved in the continuation chain, including the method that returns a
`Continuation` object. The `cacheable=true` setting is available for API version 44.0 and higher. Before API version 44.0, to
cache data returned from an Apex method, you had to call `setStorable()` in JavaScript code on every action that called the Apex
method.

In this example, the Apex method that returns the continuation, `startRequest()`, and the callback, `processResponse()`,
#### both contain cacheable=true in their @AuraEnabled annotation.

```
   // Action method

   @AuraEnabled(continuation=true cacheable=true)

   public static Object startRequest() { }

   // Callback method

   @AuraEnabled(cacheable=true)

   public static Object processResponse(List<String> labels,

     Object state) { }

#### Here's a table that summarizes the behavior with different settings of the cacheable attribute in @AuraEnabled .

```


Working with Salesforce Data Make Long-Running Callouts with Continuations

SEE ALSO:

Make Long-Running Callouts with Continuations

AuraEnabled Annotation Annotation

#### Aura Component Continuations Example

Here’s the markup for a component with a button that starts the process of calling a continuation.

The component is wired to the Apex class that uses a continuation by setting the controller attribute in the `<aura:component>`
tag.

```
<aura:component controller="SampleContinuationClass">

   <lightning:button label="Call Continuation" onclick="{!c.callContinuation}"/>

</aura:component>

```

Here’s the component’s JavaScript controller. The code calls the `startRequest` Apex method that uses a `Continuation` object.
The `response.getReturnValue()` value for a successful response in the JavScript controller corresponds to the value returned
by the Apex callback method defined in the `Continuation` object.

```
({

   callContinuation : function(cmp) {

     var action = cmp.get("c.startRequest");

     action.setCallback(this, function(response) {

        var state = response.getState();

        if (state === "SUCCESS") {

          console.log("From server: "

           + response.getReturnValue()

           + '\n' + JSON.stringify(response.getReturnValue()));

        }

        else if (state === "INCOMPLETE") {

          alert("Continuation action is INCOMPLETE");

        }

        else if (state === "ERROR") {

          var errors = response.getError();

          if (errors) {

            if (errors[0] && errors[0].message) {

               console.log("Error message: " +

                    errors[0].message);

```


### Working with Salesforce Data Creating Components in Apex

```
               }

             } else {

               console.log("Unknown error");

             }

           }

        });

        // Enqueue action that returns a continuation

        $A.enqueueAction(action);

      }

   })

```

This JavaScript controller code is similar to any other component that calls an Apex method.

SEE ALSO:

Make Long-Running Callouts with Continuations

#### Continuation-Specific Limits

Because continuations can lead to multiple long-running actions, there are some limits on their usage.

[The limits for using continuations in Apex are listed in the Apex Reference Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Continuation.htm)

Here are a few more limits specific to usage in Aura components.

**Up to three callouts per continuation**
#### A single Continuation object can contain a maximum of three callouts.

**Serial processing for continuation actions**
The framework processes actions containing a continuation serially from the client. The previous continuation action call must have
completed before the next continuation action call is made. At any time, you can have only one continuation in progress on the
client.

**DML operation restrictions**
#### An Apex method that returns a Continuation object can’t perform Data Manipulation Language (DML) operations. DML

statements insert, update, merge, delete, and restore data in Salesforce. If a DML operation is performed within the continuation
method, the continuation execution doesn’t proceed, the transaction is rolled back, and an error is returned.

You can perform DML operations in the Apex callback method for the continuation.

SEE ALSO:

Make Long-Running Callouts with Continuations

Queuing of Server-Side Actions

### Creating Components in Apex

Creating components on the server side in Apex, using the `Cmp.<myNamespace>.<myComponent>` syntax, is deprecated. Use
`$A.createComponent()` in client-side JavaScript code instead.

SEE ALSO:

Dynamically Creating Components


# CHAPTER 12 Testing Components

Automated tests are the best way to achieve predictable, repeatable assessments of the quality of your
custom code. Writing automated tests for your custom components gives you confidence that they
work as designed, and allows you to evaluate the impact of changes, such as refactoring, or of new
versions of Salesforce or third-party JavaScript libraries.

Use your testing framework of choice. Here are some popular testing tools.

**•** [Jest](https://jestjs.io/)

**•** [UTAM](https://utam.dev/guide/introduction)

**•** [Jasmine](https://jasmine.github.io/)

**•** [Mocha](https://mochajs.org/)

**•** [Selenium](https://www.selenium.dev/)

**•** [WebdriverIO](https://webdriver.io/)

Note: We used to recommend Lightning Testing Service (LTS) but it’s deprecated and no longer
supported.


# CHAPTER 13 Debugging

In this chapter ... There are a few basic tools and techniques that can help you to debug applications.

Use Chrome DevTools to debug your client-side code.

**•** Disable Caching
Setting During **•** To open DevTools on Windows and Linux, press Control-Shift-I in your Google Chrome browser. On
Development Mac, press Option-Command-I.

**•** Log Messages **•** To quickly find which line of code is failing, enable the **Pause on all exceptions** option before
running your code.

[To learn more about debugging JavaScript on Google Chrome, refer to the Google Chrome's DevTools](https://developers.google.com/web/tools/chrome-devtools/)
website.

Check out this video on how to troubleshoot your Aura components.

[Watch a video](https://salesforce.vidyard.com/watch/KmDx6HX7byNX26M9x9Cat2)


## Debugging Disable Caching Setting During Development Disable Caching Setting During Development

Disable the secure and persistent browser caching setting during development in a sandbox or Developer Edition org to see the effect
of any code changes without needing to empty the cache.

The caching setting improves page reload performance by avoiding extra round trips to the server.

Warning: Disabling secure and persistent browser caching has a significant negative performance impact on Lightning Experience.
Always enable the setting in production orgs.

**1.** From Setup, enter _`Session`_ in the `Quick Find` box, and then select **Session Settings** .

**2.** Deselect the checkbox for “Enable secure and persistent browser caching to improve performance”.

**3.** Click **Save** .

SEE ALSO:

Enable Secure Browser Caching

## Log Messages

To help debug your client-side code, you can write output to the JavaScript console of a web browser using `console.log()` if your
browser supports it..

For instructions on using the JavaScript console, refer to the instructions for your web browser.


# CHAPTER 14 Performance

In this chapter ... There are a few settings and techniques that can help you to improve application performance.

# • Performance Settings

**•** Fixing Performance
Warnings

Only enable debug mode for users who are actively debugging JavaScript. Salesforce is slower for users
who have debug mode enabled.

SEE ALSO:

_Salesforce Help:_ [Enable Debug Mode for Lightning Components](https://help.salesforce.com/articleView?id=aura_debug_mode.htm&language=en_US)


## Performance Performance Settings Performance Settings

There are a few Setup settings that can help you to improve application performance.

IN THIS SECTION:

### Enable Secure Browser Caching

Enable secure data caching in the browser to improve page reload performance by avoiding extra round trips to the server.

### Use Lightning CDN to Load Applications Faster

To load Lightning Experience faster, the Lightning content delivery network (CDN) is enabled for your org by default. The Lightning
CDN serves static content for the Lightning component framework.

### Enable Secure Browser Caching

Enable secure data caching in the browser to improve page reload performance by avoiding extra round trips to the server.

This setting is selected by default.

Warning: Disabling secure and persistent browser caching has a significant negative performance impact on Lightning Experience.
Only disable in these scenarios.

**•** Your company’s policy doesn’t allow browser caching, even if the data is encrypted.

**•** During development in a sandbox or Developer Edition, you want to see the effect of any code changes without emptying
the secure cache.

Secure and persistent data caching isn't available for Salesforce mobile app.

To disable secure data caching:

**1.** From Setup, enter _`Session`_ in the `Quick Find` box, and then select **Session Settings** .

**2.** Deselect the checkbox for “Enable secure and persistent browser caching to improve performance”.

**3.** Click **Save** .

### Use Lightning CDN to Load Applications Faster

To load Lightning Experience faster, the Lightning content delivery network (CDN) is enabled for your org by default. The Lightning CDN
serves static content for the Lightning component framework.

Salesforce uses a CDN partner to serve the static content for the Lightning Component framework over a CDN. CDNs are the industry
standard for web applications because they provide faster and more secure content delivery. A CDN is a geographically distributed
network of servers that store cached versions of web assets. To optimize page load times and site performance, a CDN efficiently delivers
publicly cacheable content to users.

Lightning CDN is enabled by default for new and existing orgs. When enabled, this setting turns on the Lightning CDN for the static
JavaScript and CSS in the Lightning Component framework at the org level. It doesn’t distribute your Salesforce data or metadata in a
CDN. Admins can turn off this preference in Setup | Session Settings by deselecting the **Enable Content Delivery Network (CDN) for**
**Lightning Component framework** checkbox. However, disabling the CDN isn’t recommended because it can impact performance.

If you experience any issues, ask your IT department if your company’s firewall blocks CDN content. Your IT department can make sure
that `static.lightning.force.com`, `a.static.lightning.force.com`, `b.static.lightning.force.com`,
and `*.static.lightning.force.com` are added to any allowlist or firewall that your company operates. If you’re using
Lightning Out, make sure that Content Security Policy doesn't block `a.static.lightning.force.com` and


## Performance Fixing Performance Warnings

`b.static.lightning.force.com` domains. You can ping `static.lightning.force.com` but you can’t browse
directly to the root URL at `https://static.lightning.force.com` .

Important: Don’t use IP addresses for network filtering because that can cause connection issues with
`https://static.lightning.force.com` . IP addresses for `https://static.lightning.force.com` are
dynamic and aren’t maintained in Salesforce’s list of allowed IP addresses.

SEE ALSO:

_Salesforce Help:_ [Options to Serve a Custom Domain](https://help.salesforce.com/articleView?id=domain_mgmt_domain_config_options.htm&type=5&language=en_US)

_Knowledge Article:_ [Salesforce Lightning CDN Preference Auto Enablement](https://help.salesforce.com/s/articleView?id=005115596&type=1&language=en_US)

_Knowledge Article:_ [Salesforce IP Addresses and Domains to Allow](https://help.salesforce.com/articleView?id=000003652&type=1&language=en_US)

## Fixing Performance Warnings

A few common performance anti-patterns in code prompt the framework to log warning messages to the browser console. Fix the
warning messages to speed up your components!

The warnings display in the browser console only if you enabled debug mode.

IN THIS SECTION:

### <aura:if> —Clean Unrendered Body —Clean Unrendered Body This warning occurs when you change the isTrue attribute of an <aura:if> tag from true to false in the same rendering cycle. The unrendered body of the <aura:if> must be destroyed, which is avoidable work for the framework that slows down

rendering time.

<aura:iteration> —Multiple Items Set —Multiple Items Set
This warning occurs when you set the `items` attribute of an `<aura:iteration>` tag multiple times in the same rendering
cycle.

SEE ALSO:

_Salesforce Help:_ **[Enable Debug Mode for Lightning Components](https://help.salesforce.com/articleView?id=aura_debug_mode.htm&language=en_US)**

### <aura:if> —Clean Unrendered Body —Clean Unrendered Body This warning occurs when you change the isTrue attribute of an <aura:if> tag from true to false in the same rendering cycle. The unrendered body of the <aura:if> must be destroyed, which is avoidable work for the framework that slows down

rendering time.

Example

This component shows the anti-pattern.

```
   <!--c:ifCleanUnrendered-->

   <aura:component>

      <aura:attribute name="isVisible" type="boolean" default="true"/>

      <aura:handler name="init" value="{!this}" action="{!c.init}"/>

      <aura:if isTrue="{!v.isVisible}">

```


Performance <aura:if> —Clean Unrendered Body —Clean Unrendered
Body

```
        <p>I am visible</p>

      </aura:if>

   </aura:component>

```

Here’s the component’s client-side controller.

```
   /* c:ifCleanUnrenderedController.js */

   ({

      init: function(cmp) {

        /* Some logic */

        cmp.set("v.isVisible", false); // Performance warning trigger

      }

   })

```

When the component is created, the `isTrue` attribute of the `<aura:if>` tag is evaluated. The value of the `isVisible` attribute
is `true` by default so the framework creates the body of the `<aura:if>` tag. After the component is created but before rendering,
the `init` event is triggered.

The `init()` function in the client-side controller toggles the `isVisible` value from `true` to `false` . The `isTrue` attribute
of the `<aura:if>` tag is now `false` so the framework must destroy the body of the `<aura:if>` tag. This warning displays in
the browser console only if you enabled debug mode.

```
   WARNING: [Performance degradation] markup://aura:if ["5:0"] in c:ifCleanUnrendered ["3:0"]

   needed to clear unrendered body.

```

Click the expand button beside the warning to see a stack trace for the warning.

Click the link for the `ifCleanUnrendered` entry in the stack trace to see the offending line of code in the Sources pane of the
browser console.

How to Fix the Warning

Reverse the logic for the `isTrue` expression. Instead of setting the `isTrue` attribute to `true` by default, set it to `false` . Set the
`isTrue` expression to true in the `init()` method, if needed.

Here’s the fixed component:

```
   <!--c:ifCleanUnrenderedFixed-->

   <aura:component>

      <!-- FIX: Change default to false.

         Update isTrue expression in controller instead. -->

      <aura:attribute name="isVisible" type="boolean" default="false"/>

      <aura:handler name="init" value="{!this}" action="{!c.init}"/>

      <aura:if isTrue="{!v.isVisible}">

        <p>I am visible</p>

      </aura:if>

   </aura:component>

```


### Performance <aura:iteration> —Multiple Items Set —Multiple Items Set

Here’s the fixed controller:

```
   /* c:ifCleanUnrenderedFixedController.js */

   ({

      init: function(cmp) {

        // Some logic

        // FIX: set isVisible to true if logic criteria met

        cmp.set("v.isVisible", true);

      }

   })

```

SEE ALSO:

_Salesforce Help:_ **[Enable Debug Mode for Lightning Components](https://help.salesforce.com/articleView?id=aura_debug_mode.htm&language=en_US)**

### <aura:iteration> —Multiple Items Set —Multiple Items Set This warning occurs when you set the items attribute of an <aura:iteration> tag multiple times in the same rendering cycle.

There’s no easy and performant way to check if two collections are the same in JavaScript. Even if the old value of `items` is the same
### as the new value, the framework deletes and replaces the previously created body of the <aura:iteration> tag.

Example

This component shows the anti-pattern.

```
   <!--c:iterationMultipleItemsSet-->

   <aura:component>

      <aura:attribute name="groceries" type="List"

              default="[ 'Eggs', 'Bacon', 'Bread' ]"/>

      <aura:handler name="init" value="{!this}" action="{!c.init}"/>

      <aura:iteration items="{!v.groceries}" var="item">

        <p>{!item}</p>

      </aura:iteration>

   </aura:component>

```

Here’s the component’s client-side controller.

```
   /* c:iterationMultipleItemsSetController.js */

   ({

      init: function(cmp) {

        var list = cmp.get('v.groceries');

        // Some logic

        cmp.set('v.groceries', list); // Performance warning trigger

      }

   })

### When the component is created, the items attribute of the <aura:iteration> tag is set to the default value of the groceries
```

attribute. After the component is created but before rendering, the `init` event is triggered.


Performance <aura:iteration> —Multiple Items Set —Multiple Items Set

The `init()` function in the client-side controller sets the `groceries` attribute, which resets the `items` attribute of the
`<aura:iteration>` tag. This warning displays in the browser console only if you enabled debug mode.

```
   WARNING: [Performance degradation] markup://aura:iteration [id:5:0] in

   c:iterationMultipleItemsSet ["3:0"]

   had multiple items set in the same Aura cycle.

```

Click the expand button beside the warning to see a stack trace for the warning.

Click the link for the `iterationMultipleItemsSet` entry in the stack trace to see the offending line of code in the Sources
pane of the browser console.

How to Fix the Warning

Make sure that you don’t modify the `items` attribute of an `<aura:iteration>` tag multiple times. The easiest solution is to
remove the default value for the `groceries` attribute in the markup. Set the value for the `groceries` attribute in the controller
instead.

The alternate solution is to create a second attribute whose only purpose is to store the default value. When you’ve completed your
logic in the controller, set the `groceries` attribute.

Here’s the fixed component:

```
   <!--c:iterationMultipleItemsSetFixed-->

   <aura:component>

      <!-- FIX: Remove the default from the attribute -->

      <aura:attribute name="groceries" type="List" />

      <!-- FIX (ALTERNATE): Create a separate attribute containing the default -->

      <aura:attribute name="groceriesDefault" type="List"

              default="[ 'Eggs', 'Bacon', 'Bread' ]"/>

      <aura:handler name="init" value="{!this}" action="{!c.init}"/>

      <aura:iteration items="{!v.groceries}" var="item">

        <p>{!item}</p>

      </aura:iteration>

   </aura:component>

```

Here’s the fixed controller:

```
   /* c:iterationMultipleItemsSetFixedController.js */

   ({

      init: function(cmp) {

        // FIX (ALTERNATE) if need to set default in markup

        // use a different attribute

        // var list = cmp.get('v.groceriesDefault');

        // FIX: Set the value in code

        var list = ['Eggs', 'Bacon', 'Bread'];

```


Performance <aura:iteration> —Multiple Items Set —Multiple Items Set

```
        // Some logic

        cmp.set('v.groceries', list);

      }

   })

```

SEE ALSO:

_Salesforce Help:_ **[Enable Debug Mode for Lightning Components](https://help.salesforce.com/articleView?id=aura_debug_mode.htm&language=en_US)**


# CHAPTER 15 Reference

In this chapter ... This section contains links to reference documentation.

**•** Lightning Component
Library

**•** System Tag
# Reference

**•** JavaScript API


## Reference Lightning Component Library Lightning Component Library

The Lightning Component Library is your hub for component reference information, including the Component Reference with live
examples, and tools for Lightning Web Security and Lightning Locker.

You can find the Component Library in two places: a public site and an authenticated one that’s linked to your Salesforce org. In the
authenticated site, the Component Reference section of the Component Library has some additional features.

**Public Component Library**
[View this site without logging in to Salesforce. The Component Reference includes documentation and reference information for](https://developer.salesforce.com/docs/platform/lightning-component-reference)
the Lightning base components.

**Component Library for your org**
View this site by logging in to your Salesforce org and navigating to
`https://` _`MyDomainName`_ `.my.salesforce.com/docs/component-library` .

The authenticated site has additional features for the Component Reference.

**•** View Aura Lightning components that are unique to your org.

**•** View Aura Lightning components that are installed in a managed package. You can filter to view components owned by your
org or installed in packages. Find the filtering options at

```
      https:// MyDomainName .my.salesforce.com/docs/component-library/overview/components
```

and expand the Filters list to find the Owners filters.

Component Reference

The Component Reference contains usage information for base components.

**•** [The legacy Component Reference is available as part of the Component Library, which is no longer updated and will no longer be](https://developer.salesforce.com/docs/component-library)
published in Spring ’26.

**•** [The new Lightning Component Reference is at https://developer.salesforce.com/docs/platform/lightning-component-reference.](https://developer.salesforce.com/docs/platform/lightning-component-reference)

**•** The authenticated Component Library continues to display your custom Aura components that are unique to your org or that are
installed in a managed package.

[Note: The Lightning Component Reference lists base components for the Aura programming model under Legacy Components.](https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/legacy.html)
We recommend that you use Lightning Web Components (LWC) where possible for new development.

IN THIS SECTION:

### Differences Between Documentation Sites

Here’s a breakdown of the differences between the Component Library and the reference section of this developer guide.

### Differences Between Documentation Sites

Here’s a breakdown of the differences between the Component Library and the reference section of this developer guide.

The Component Library is the place to find reference information and interactive examples. The Reference section in this Developer
Guide provides information on system-level tags that are not available elsewhere, as well as the JavaScript API.


## Reference System Tag Reference

**Component Library** **Reference Section in Lightning Aura Components**
**Developer Guide**

Component documentation
and code samples

(Documentation tab)

Interactive examples

(Example tab)

Lightning Design System
support

Components in custom
namespaces and packages

JavaScript API

System tags

( `aura:method`, `aura:set`, etc.)

Event documentation

System event documentation

Interface documentation

Components in custom namespaces display both global and non-global attributes and methods in the authenticated Component
Library displayed in an org. Components in managed and unmanaged packages display only global attributes and methods.

## System Tag Reference

System tags represent framework definitions and are not available in the Component Library.


### Reference aura:application

IN THIS SECTION:

### aura:application

An app is a special top-level component whose markup is in a `.app` resource.

aura:dependency
The `<aura:dependency>` tag enables you to declare dependencies, which improves their discoverability by the framework.

aura:event
An event is represented by the `aura:event` tag, which has the following attributes.

aura:interface
Interfaces determine a component's shape by defining its attributes. Implement an interface to allow a component to be used in
different contexts, such as on a record page or in Lightning App Builder.

aura:method
Use `<aura:method>` to define a method as part of a component's API. This enables you to directly call a method in a component’s
client-side controller instead of firing and handling a component event. Using `<aura:method>` simplifies the code needed for
a parent component to call a method on a child component that it contains.

aura:set
Use `<aura:set>` in markup to set the value of an attribute inherited from a component or event.

### aura:application

An app is a special top-level component whose markup is in a `.app` resource.

The markup looks similar to HTML and can contain components as well as a set of supported HTML tags. The `.app` resource is a
standalone entry point for the app and enables you to define the overall application layout, style sheets, and global JavaScript includes.
It starts with the top-level `<aura:application>` tag, which contains optional system attributes. These system attributes tell the
framework how to configure the app.

**System Attribute** **Type** **Description**

`access` String Indicates whether the app can be extended by another app outside of a namespace.
Possible values are `public` (default), and `global` .

`controller` String The Apex controller class for the app. The format is
`namespace.myController` .

`description` String A brief description of the app.

`extends` Component The app to be extended, if applicable. For example,
`extends="namespace:yourApp"` .

`extensible` Boolean Indicates whether the app is extensible by another app. Defaults to `false` .

`implements` String A comma-separated list of interfaces that the app implements.

`template` Component

The name of the template used to bootstrap the loading of the framework and
the app. The default value is `aura:template` . You can customize the template
by creating your own component that extends the default template. For example:

```
<aura:component extends="aura:template" ... >

```


### Reference aura:dependency

**System Attribute** **Type** **Description**

`tokens` String A comma-separated list of tokens bundles for the application. For example,
`tokens="ns:myAppTokens"` . Tokens make it easy to ensure that your

design is consistent, and even easier to update it as your design evolves. Define
the token values once and reuse them throughout your application.

`useAppcache` Boolean Deprecated. Browser vendors have deprecated AppCache, so we followed their
lead. Remove the `useAppcache` attribute in the `<aura:application>`

tag of your standalone apps ( `.app` resources) to avoid cross-browser support
issues due to deprecation by browser vendors.

If you don’t currently set `useAppcache` in an `<aura:application>` tag,
you don’t have to do anything because the default value of `useAppcache` is
`false` .

`aura:application` also includes a `body` attribute defined in a `<aura:attribute>` tag. Attributes usually control the output
or behavior of a component, but not the configuration information in system attributes.

**Attribute** **Type** **Description**

`body` `Component[]` The body of the app. In markup, this is
everything in the body of the tag.

SEE ALSO:

Creating Apps

Application Access Control

### aura:dependency

The `<aura:dependency>` tag enables you to declare dependencies, which improves their discoverability by the framework.

The framework automatically tracks dependencies between definitions, such as components, defined in markup. This enables the
framework to send the definitions to the browser. However, if a component’s JavaScript code dynamically instantiates another component
or fires an event that isn’t directly referenced in the component’s markup, use `<aura:dependency>` in the component’s markup
to explicitly tell the framework about the dependency. Adding the `<aura:dependency>` tag ensures that a definition, such as a
component, and its dependencies are sent to the client, when needed.

For example, adding this tag to a component marks the `sampleNamespace:sampleComponent` component as a dependency.

```
   <aura:dependency resource="markup://sampleNamespace:sampleComponent" />

```

Add this tag to component markup to mark the event as a dependency.

```
   <aura:dependency resource="markup://force:navigateToComponent" type="EVENT"/>

```

Use the `<aura:dependency>` tag if you fire an event in JavaScript code and you’re not registering the event in component markup
using `<aura:registerEvent>` . Using an `<aura:registerEvent>` tag is the preferred approach.

The `<aura:dependency>` tag includes these system attributes.


### Reference aura:event

**System Attribute** **Description**

```
resource

type

```

SEE ALSO:

The resource that the component depends on, such as a component or event. For example,
`resource="markup://sampleNamespace:sampleComponent"` refers to the
`sampleComponent` in the `sampleNamespace` namespace.

Using an asterisk ( `*` ) for wildcard matching is deprecated. Instead, add an
`<aura:dependency>` tag for each resource that’s not directly referenced in the component’s

markup. Wildcard matching can cause save validation errors when no resources match. Wildcard
matching can also slow page load time because it sends more definitions than needed to the
client.

The type of resource that the component depends on. The default value is `COMPONENT` .

Using an asterisk ( `*` ) for wildcard matching is deprecated. Instead, add an
`<aura:dependency>` tag for each resource that’s not directly referenced in the component’s
markup. Be as selective as possible in the types of definitions that you send to the client.

The most commonly used values are:

**•** `COMPONENT`

**•** `EVENT`

**•** `INTERFACE`

**•** `APPLICATION`

**•** `MODULE` —Use this type to add a dependency for a Lightning web component

Use a comma-separated list for multiple types; for example: `COMPONENT,APPLICATION` .

Dynamically Creating Components

Fire Component Events

Fire Application Events

### aura:event An event is represented by the aura:event tag, which has the following attributes.

**Attribute** **Type** **Description**

`access` String

Indicates whether the event can be extended or used outside of its
own namespace. Possible values are `public` (default), and
`global` .

`description` String A description of the event.

`extends` Component The event to be extended. For example,
`extends="namespace:myEvent"` .


### Reference aura:interface

**Attribute** **Type** **Description**

`type` String Required. Possible values are `COMPONENT` or `APPLICATION` .

SEE ALSO:

Communicating with Events

Event Access Control

### aura:interface

Interfaces determine a component's shape by defining its attributes. Implement an interface to allow a component to be used in different
contexts, such as on a record page or in Lightning App Builder.

### The aura:interface tag has the following optional attributes.

**Attribute** **Type** **Description**

`access` String

Indicates whether the interface can be extended or used outside of
its own namespace. Possible values are `public` (default), and
`global` .

`description` String A description of the interface.

`extends` Component The comma-separated list of interfaces to be extended. For example,
`extends="namespace:intfB"` .

SEE ALSO:

Interfaces

Interface Access Control

### aura:method

Use `<aura:method>` to define a method as part of a component's API. This enables you to directly call a method in a component’s
client-side controller instead of firing and handling a component event. Using `<aura:method>` simplifies the code needed for a
parent component to call a method on a child component that it contains.

The `<aura:method>` tag has these system attributes.

**Attribute** **Type** **Description**

```
name String

action Expression

```

The method name. Use the method name to call the method in
JavaScript code. For example:

```
  cmp.sampleMethod(param1);

```

The client-side controller action to execute. For example:

```
  action="{!c.sampleAction}"

```


Reference aura:method

**Attribute** **Type** **Description**

`sampleAction` is an action in the client-side controller. If you
don’t specify an `action` value, the controller action defaults to
the value of the method `name` .

`access` `String` The access control for the method. Valid values are:

**•** **public** —Any component in the same namespace can call the
method. This is the default access level.

**•** **global** —Any component in any namespace can call the
method.

`description` `String` The method description.

Declaring Parameters

An `<aura:method>` can optionally include parameters. Use an `<aura:attribute>` tag within an `<aura:method>` to
declare a parameter for the method. For example:

```
   <aura:method name="sampleMethod" action="{!c.doAction}"

     description="Sample method with parameters">

      <aura:attribute name="param1" type="String" default="parameter 1"/>

      <aura:attribute name="param2" type="Object" />

   </aura:method>

```

For more information, see the **Returning a Value** section below.

Note: You don’t need an `access` system attribute in the `<aura:attribute>` tag for a parameter.

Creating a Handler Action

This handler action shows how to access the arguments passed to the method.

```
   ({

      doAction : function(cmp, event) {

        var params = event.getParam('arguments');

        if (params) {

           var param1 = params.param1;

           // add your code here

        }

      }

   })

```

Retrieve the arguments using `event.getParam('arguments')` . It returns an object if there are arguments or an empty array
if there are no arguments.

Returning a Value

`aura:method` executes synchronously.

**•** A synchronous method finishes executing before it returns. Use the `return` statement to return a value from synchronous JavaScript
code. See Return Result for Synchronous Code.


### Reference aura:set

**•** An asynchronous method may continue to execute after it returns. Use a callback to return a value from asynchronous JavaScript
code. See Return Result for Asynchronous Code.

SEE ALSO:

Calling Component Methods

Component Events

### aura:set

Use `<aura:set>` in markup to set the value of an attribute inherited from a component or event.

IN THIS SECTION:

#### Setting Attributes Inherited from a Super Component

Setting Attributes on a Component Reference

Setting Attributes Inherited from an Interface

#### Setting Attributes Inherited from a Super Component

Use `<aura:set>` in the markup of a sub component to set the value of an inherited attribute.

Let's look at an example. Here is the `c:setTagSuper` component.

```
   <!--c:setTagSuper-->

   <aura:component extensible="true">

      <aura:attribute name="address1" type="String" />

      setTagSuper address1: {!v.address1}<br/>

   </aura:component>

```

`c:setTagSuper` outputs:

```
   setTagSuper address1:

```

The `address1` attribute doesn't output any value yet as it hasn't been set.

Here is the `c:setTagSub` component that extends `c:setTagSuper` .

```
   <!--c:setTagSub-->

   <aura:component extends="c:setTagSuper">

      <aura:set attribute="address1" value="808 State St" />

   </aura:component>

```

`c:setTagSub` outputs:

```
   setTagSuper address1: 808 State St

```

`sampleSetTagExc:setTagSub` sets a value for the `address1` attribute inherited from the super component,
`c:setTagSuper` .

Warning: This usage of `<aura:set>` works for components and abstract components, but it doesn’t work for interfaces. For
more information, see Setting Attributes Inherited from an Interface on page 474.


Reference aura:set

If you’re using a component by making a reference to it in your component, you can set the attribute value directly in the markup. For
example, `c:setTagSuperRef` makes a reference to `c:setTagSuper` and sets the `address1` attribute directly without using
`aura:set` .

```
   <!--c:setTagSuperRef-->

   <aura:component>

      <c:setTagSuper address1="1 Sesame St" />

   </aura:component>

```

`c:setTagSuperRef` outputs:

```
   setTagSuper address1: 1 Sesame St

```

SEE ALSO:

Component Body

Inherited Component Attributes

#### Setting Attributes on a Component Reference Setting Attributes on a Component Reference

When you include another component, such as `<lightning:button>`, in a component, we call that a component reference to
`<lightning:button>` . You can use `<aura:set>` to set an attribute on the component reference. For example, if your component
includes a reference to `<lightning:button>` :

```
   <lightning:button label="Save">

      <aura:set attribute="variant" value="brand"/>

   </lightning:button>

```

This is equivalent to:

```
   <lightning:button label="Save" variant="brand" />

```

The latter syntax without `aura:set` makes more sense in this simple example. You can also use this simpler syntax in component
references to set values for attributes that are inherited from parent components.

`aura:set` is more useful when you want to set markup as the attribute value. For example, this sample specifies the markup for the
`else` attribute in the `aura:if` tag.

```
   <aura:component>

      <aura:attribute name="display" type="Boolean" default="true"/>

      <aura:if isTrue="{!v.display}">

        Show this if condition is true

        <aura:set attribute="else">

          <lightning:button label="Save" onclick="{!c.saveRecord}" />

        </aura:set>

      </aura:if>

   </aura:component>

```

SEE ALSO:

Setting Attributes Inherited from a Super Component


## Reference JavaScript API

#### Setting Attributes Inherited from an Interface

To set the value of an attribute inherited from an interface, redefine the attribute in the component and set its default value. Let’s look
at an example with the `c:myIntf` interface.

```
   <!--c:myIntf-->

   <aura:interface>

      <aura:attribute name="myBoolean" type="Boolean" default="true" />

   </aura:interface>

```

This component implements the interface and sets `myBoolean` to `false` .

```
   <!--c:myIntfImpl-->

   <aura:component implements="c:myIntf">

      <aura:attribute name="myBoolean" type="Boolean" default="false" />

      <p>myBoolean: {!v.myBoolean}</p>

   </aura:component>

## JavaScript API

```

The JavaScript API lists the publicly accessible methods for each object that you can use in JavaScript code, such as a controller or helper.
### The $A namespace is the entry point for using the framework in JavaScript code.

IN THIS SECTION:

### $A namespace The $A namespace is the entry point for using the framework in JavaScript code.

Action

`Action` contains methods to work with JavaScript actions that you can use to communicate with Apex classes.

AuraLocalizationService

`AuraLocalizationService` provides methods for formatting and localizing dates. Use `$A.localizationService`
to use the methods in `AuraLocalizationService` .

Component

`Component` contains methods to work with components.

Event

`Event` contains methods to work with events. Use an event to communicate between components.

Util

`Util` contains utility methods.

### $A namespace The $A namespace is the entry point for using the framework in JavaScript code.


Reference $A namespace

Methods

IN THIS SECTION:

createComponent()
Create a component from a type and a set of attributes. This method accepts the name of a type of component, a map of attributes,
and a callback to notify the caller.

createComponents()
Create an array of components from a list of types and attributes. This method accepts a list of component names and attribute
maps, and a callback to notify the caller.

enqueueAction()
Queue a call to an Apex action . The framework queues up actions before sending them to the server. This mechanism is largely
transparent to you when you’re writing code but it enables the framework to minimize network traffic by batching multiple actions
into one request (XHR).

error()
Deprecated. For a serious error that has no recovery path, throw a standard JavaScript error instead by using `throw new`

`Error(msg)` .

get()
Returns a value from the specified global value provider using property syntax.

getCallback()
Use `$A.getCallback()` to wrap any code that modifies a component outside the normal rerendering lifecycle, such as in a
`setTimeout()` call. The `$A.getCallback()` call ensures that the framework rerenders the modified component and
processes any enqueued actions.

getComponent()
Gets an instance of a component from either a global ID or a DOM element that was created by a rendered component.

getReference()
Returns a live reference to the global value requested using property syntax.

getRoot()
Gets the root component or application. For example, `$A.getRoot().get("v.attrName")` returns the value of the
`attrName` attribute from the root component.

getToken()
Returns an application configuration token referenced by name. A tokens file is configured with the `tokens` attribute in the
`<aura:application>` tag.

log()
Deprecated. Logs to the browser's JavaScript console, if it is available. This method doesn't log in production or debug modes so it’s
only useful for internal usage by the framework.

reportError()
Report an error to the server after handling it. Note that the method should be used only if the try-catch mechanism of error handling
is not desired or not functional, such as in nested promises.

run()
Deprecated. Use `getCallback()` instead.

set()
Sets a value on the specified global value provider using property syntax.


Reference $A namespace

warning()
Deprecated. Logs a warning to the browser's JavaScript console, if it is available.

#### createComponent()

Create a component from a type and a set of attributes. This method accepts the name of a type of component, a map of attributes,
and a callback to notify the caller.

Signature

```
   createComponent(String type, Object attributes, function callback)

```

Parameters

```
   type
```

Type: `String`

The type of component to create. For example, `"lightning:button"` .

```
   attributes
```

Type: `Object`

A map of attributes to send to the component. These attributes take the same form as in the markup, including events
`{"press":component.getReference("c.handlePress")}`, and id `{"aura:id":"myComponentId"}` .

```
   callback(cmp, status, errorMessage)
```

Type: `function`

The callback to invoke after the component is created. The callback has three parameters.

**1.** `cmp` —The component that was created. This parameter enables you to do something with the new component, such as add
it to the body of the component that creates it. If there’s an error, `cmp` is `null` .

**2.** `status` —The status of the call. The possible values are `SUCCESS`, `INCOMPLETE`, or `ERROR` . Always check that the status
is `SUCCESS` before you try to use the component.

**3.** `errorMessage` —The error message if the status is `ERROR` .

SEE ALSO:

Dynamically Creating Components

#### createComponents()

Create an array of components from a list of types and attributes. This method accepts a list of component names and attribute maps,
and a callback to notify the caller.

Signature

```
   createComponents(Array components, function callback)

```

Parameters

```
   components
```

Type: `Array`


Reference $A namespace

The list of components to create. For example, `["lightning:button",`

```
    {"onclick":component.getReference("c.handlePress")}]

   callback(components, status, errorMessage)
```

Type: `function`

The callback to invoke after the components are created. The callback has three parameters.

**1.** `components` —The components that were created. This parameter enables you to do something with the new components,
such as add them to the body of the component that created them. If there’s an error, `components` is `null` .

**2.** `status` —The status of the call. The possible values are `SUCCESS`, `INCOMPLETE`, or `ERROR` . Always check that the status
is `SUCCESS` before you try to use the components.

**3.** `errorMessage` —The error message if the status is `ERROR` .

SEE ALSO:

Dynamically Creating Components

#### enqueueAction()

Queue a call to an Apex action . The framework queues up actions before sending them to the server. This mechanism is largely transparent
to you when you’re writing code but it enables the framework to minimize network traffic by batching multiple actions into one request
(XHR).

The batching of actions is also known as boxcar’ing, similar to a train that couples boxcars together.

The framework uses a stack to keep track of the actions to send to the server. When the browser finishes processing events and JavaScript
on the client, the enqueued actions on the stack are sent to the server in a batch.

Signature

```
   enqueueAction (Action action, Boolean background)

```

Parameters

```
   action
```

Type: `Action`

The action to enqueue.

```
   background
```

Type: `Boolean`

Deprecated. Do not use.

SEE ALSO:

Queuing of Server-Side Actions

Calling a Server-Side Action

#### error()

Deprecated. For a serious error that has no recovery path, throw a standard JavaScript error instead by using `throw new Error(msg)` .


Reference $A namespace

Signature

```
   error (String msg, Error e)

```

Parameters

```
   msg
```

Type: `String`

The error message to display to the user.

```
   e
```

Type: `Error`

The error message to display to the user.

#### get()

Returns a value from the specified global value provider using property syntax.

Signature

```
   get (String key, function callback)

```

Parameters

```
   key
```

Type: `String`

The data key to look up. For example, `"$Label.c.labelName"` for a custom label.

```
   callback
```

Type: `function`

The method to call with the result if a server trip occurs.

Returns

**Type:** **`String`**
The requested value.

SEE ALSO:

set()

#### getCallback()

Use `$A.getCallback()` to wrap any code that modifies a component outside the normal rerendering lifecycle, such as in a
`setTimeout()` call. The `$A.getCallback()` call ensures that the framework rerenders the modified component and processes
any enqueued actions.

Don't use `$A.getCallback()` if your code is executed as part of the framework's call stack. For example, your code is handling an
event or in the callback for an Apex controller action.


Reference $A namespace

Run async operations with a `$A.getCallback()` wrapper. For example, use `setTimeout()` and `setInterval()` with
`$A.getCallback()` . Use Promise resolve or reject handlers with `$A.getCallback()` .

When using `$A.getCallback(function callback)` with a Promise, the function runs after the Promise resolves. For example:

```
   ({

      getUser : function(component, event, helper) {

        // Call helper to get the Promise object

        var userPromise = helper.fetchUserData();

        // Set the Promise object into an attribute (v.userPromise)

        component.set("v.userPromise", userPromise);

        // Use .then() with the Promise that's retrieved via component.get()

        // The Promise resolves and its result is passed to the function

        component.get("v.userPromise").then(

           $A.getCallback(function(result) {

             // 'result' is returned object from the helper

             var userName = result.name;

             var userId = result.id;

             // Use the data to update a component attribute

             component.set("v.userName", userName);

           })

        ).catch($A.getCallback(function(error) {

           // Handle any potential errors during the promise resolution

           component.set("v.userName", "Error fetching data.");

           console.error("Promise rejected:", error);

        }));

      }

   })

```

Signature

```
   getCallback (function callback)

```

Parameters

```
   callback
```

Type: `function`

The method to call after establishing an Aura context.

Sample Code

Use `$A.getCallback()` with component validity check.

```
   window.setTimeout(

      $A.getCallback(function() {

        if(cmp.isValid())

        cmp.set("v.value", data);

```


Reference $A namespace

```
      }), 5000

   );

```

Use Promise handling with Aura lifecycle management.

```
   promise.then($A.getCallback(function(result) {

      if(cmp.isValid())

      helper.process(result);

      }

   ));

```

SEE ALSO:

Modifying Components Outside the Framework Lifecycle

#### getComponent()

Gets an instance of a component from either a global ID or a DOM element that was created by a rendered component.

Signature

```
   getComponent (Object identifier)

```

Parameters

```
   identifier
```

Type: `Object`

A globalId or an element.

#### getReference()

Returns a live reference to the global value requested using property syntax.

Signature

```
   getReference (String key)

```

Parameters

```
   key
```

Type: `String`

The data key for which to return a reference.

Returns

**Type:** **`PropertyReferenceValue`**
The reference to the global value requested.


Reference $A namespace

#### getRoot()

Gets the root component or application. For example, `$A.getRoot().get("v.attrName")` returns the value of the `attrName`
attribute from the root component.

Signature

#### `getRoot()` getToken()

Returns an application configuration token referenced by name. A tokens file is configured with the `tokens` attribute in the
`<aura:application>` tag.

Signature

```
   getToken (String token)

```

Parameters

```
   token
```

Type: `String`

The name of the application configuration token to retrieve.

Returns

**Type:** **`String`**
application configuration token.

#### log()

Deprecated. Logs to the browser's JavaScript console, if it is available. This method doesn't log in production or debug modes so it’s
only useful for internal usage by the framework.

Signature

```
   log (Object value, Object error)

```

Parameters

```
   value
```

Type: `Object`

The object to log.

```
   error
```

Type: `Object`

The error message to log in the stack trace.


Reference $A namespace

Returns

**Type:** **`String`**
The requested value.

#### reportError()

Report an error to the server after handling it. Note that the method should be used only if the try-catch mechanism of error handling
is not desired or not functional, such as in nested promises.

Signature

```
   reportError (String message, Error error)

```

Parameters

```
   message
```

Type: `String`

The error message.

```
   error
```

Type: `Error`

An error object to be included in handling and reporting.

#### run()

Deprecated. Use `getCallback()` instead.

Signature

```
   run (function func, String name)

```

Parameters

```
   func
```

Type: `function`

The function to run.

```
   name
```

Type: `String`

An optional name for the stack.

#### set()

Sets a value on the specified global value provider using property syntax.

Signature

```
   set (String key, Object value)

```


### Reference Action

Parameters

```
   key
```

Type: `String`

The data key to change on the global value provider.

```
   value
```

Type: `Object`

The value to set for the key. If the global value provider doesn’t implement `set()`, this method throws an exception.

#### warning()

Deprecated. Logs a warning to the browser's JavaScript console, if it is available.

Signature

```
   warning (String w, Error e)

```

Parameters

#### _`w`_

Type: `String`

The message to log.

```
   error
```

Type: `Object`

The error message to log in the stack trace.

Returns

**Type:** **`String`**
The requested value.

### Action Action contains methods to work with JavaScript actions that you can use to communicate with Apex classes.

Methods

IN THIS SECTION:

getError()
Returns an array of error objects for server-side actions only. Each error object has a message field. In any mode except `PROD` mode,
each object also has a stack field, which is a list describing the execution stack when the error occurred.

getName()
Returns the name of an action.

getParam()
Returns an action parameter value for a parameter name.


Reference Action

getParams()
Returns the collection of parameters for an action.

getReturnValue()
Gets the return value of an Apex action. An Apex action can return any object containing serializable JSON data.

getState()
Returns the current state of an action. Check the state of the action in the callback after an Apex action completes.

isBackground()
Returns `true` if the action is enqueued in the background, `false` if it’s enqueued in the foreground.

setAbortable()
Sets an action as abortable. If the component is not valid, abortable actions are not sent to the server. A component is automatically
destroyed and marked invalid by the framework when it is unrendered. Actions not marked abortable are always sent to the server
regardless of the validity of the component.

setBackground()
Sets the action to run as a background action. This cannot be unset. Background actions are usually long running and lower priority
actions. A background action is useful when you want your app to remain responsive to a user while it executes a low priority,
long-running action. A rough guideline is to use a background action if it takes more than five seconds for the response to return
from the server.

setCallback()
Sets the callback function that is executed after an Apex action returns.

setParam()
Sets a single parameter for an action. Use parameters to pass data to an Apex action.

setParams()
Sets parameters for an action. Use parameters to pass data to an Apex action.

setStorable()
Marks an Apex action as storable to have its response stored in the framework’s client-side cache . Enhance your component’s
performance by marking actions as storable (cacheable) to quickly show cached data from client-side storage without waiting for
a server trip. If the cached data is stale, the framework retrieves the latest data from the server. Caching is especially beneficial for
users on high latency, slow, or unreliable connections such as 3G networks.

#### getError()

Returns an array of error objects for server-side actions only. Each error object has a message field. In any mode except `PROD` mode,
each object also has a stack field, which is a list describing the execution stack when the error occurred.

Signature

#### `getError()`

Returns

**Type:** **`Object[]`**
An array of error objects. Each error object has a message field.


Reference Action

#### getName()

Returns the name of an action.

Signature

#### `getName()`

Returns

**Type:** **`String`**
The action name.

#### getParam()

Returns an action parameter value for a parameter name.

Signature

```
   getParam (String name)

```

Parameters

```
   name
```

Type: `String`

The parameter name.

Returns

**Type:** **`Object`**
The parameter value.

#### getParams()

Returns the collection of parameters for an action.

Signature

#### `getParams`

Returns

**Type:** **`Object`**
The key-value pairs for the action parameters.

#### getReturnValue()

Gets the return value of an Apex action. An Apex action can return any object containing serializable JSON data.


Reference Action

Signature

```
   getReturnValue()

```

Returns

**Type:** **`Object`**
The return value of an Apex action.

SEE ALSO:

Calling a Server-Side Action

#### getState()

Returns the current state of an action. Check the state of the action in the callback after an Apex action completes.

Signature

#### `getState()`

Returns

**Type:** **`String`**
The action state.

SEE ALSO:

Action States

#### isBackground()

Returns `true` if the action is enqueued in the background, `false` if it’s enqueued in the foreground.

Signature

#### `isBackground()`

Returns

**Type:** **`Boolean`**
Returns `true` if the action is enqueued in the background.

#### setAbortable()

Sets an action as abortable. If the component is not valid, abortable actions are not sent to the server. A component is automatically
destroyed and marked invalid by the framework when it is unrendered. Actions not marked abortable are always sent to the server
regardless of the validity of the component.

For example, a save or edit action should not be set as abortable to ensure that it’s always sent to the server even if the component is
deleted. Setting an action as abortable can’t be undone.


Reference Action

Signature

```
   setAbortable()

```

SEE ALSO:

Abortable Actions

#### setBackground()

Sets the action to run as a background action. This cannot be unset. Background actions are usually long running and lower priority
actions. A background action is useful when you want your app to remain responsive to a user while it executes a low priority, long-running
action. A rough guideline is to use a background action if it takes more than five seconds for the response to return from the server.

Signature

#### `setBackground()` setCallback()

Sets the callback function that is executed after an Apex action returns.

Signature

```
   setCallback (Object scope, function callback, String name)

```

Parameters

```
   scope
```

Type: `Object`

The scope in which the function is executed. Always set this parameter to the keyword `this` .

```
   callback
```

Type: `function`

The callback to invoke after the Apex action returns.

```
   name
```

Type: `String`

Defaults to "ALL" which registers callbacks for the "SUCCESS", "ERROR", and "INCOMPLETE" states.

SEE ALSO:

Calling a Server-Side Action

Action States

#### setParam()

Sets a single parameter for an action. Use parameters to pass data to an Apex action.


Reference Action

Signature

```
   setParam (String key, Object value)

```

Parameters

```
   key
```

Type: `String`

The parameter name.

```
   value
```

Type: `Object`

The parameter value.

SEE ALSO:

Calling a Server-Side Action

#### setParams()

Sets parameters for an action. Use parameters to pass data to an Apex action.

Signature

```
   setParams (Object config)

```

Parameters

```
   config
```

Type: `Object`

The key-value pairs for action parameters. For example `{ "record":` _**`id`**_ `, "name":` _**`name`**_ `}.`

SEE ALSO:

Calling a Server-Side Action

#### setStorable()

Marks an Apex action as storable to have its response stored in the framework’s client-side cache . Enhance your component’s performance
by marking actions as storable (cacheable) to quickly show cached data from client-side storage without waiting for a server trip. If the
cached data is stale, the framework retrieves the latest data from the server. Caching is especially beneficial for users on high latency,
slow, or unreliable connections such as 3G networks.

Note: Client-side storage is automatically configured in Lightning Experience and the Salesforce mobile app. A component
shouldn’t assume a cache duration because it may change as we optimize the platform.

Signature

```
   setStorable (Object config)

```


### Reference AuraLocalizationService

Parameters

```
   config
```

Type: `Object`

An optional configuration map of key-value pairs representing the storage options and values to set. You can only set the
`ignoreExisting` property. Set `ignoreExisting` to `true` to bypass the cache. The default value is `false` .

This property is useful when you know that any cached data is invalid, such as after a record modification. This property should be
used rarely because it explicitly defeats caching.

SEE ALSO:

Storable Actions

### AuraLocalizationService AuraLocalizationService provides methods for formatting and localizing dates. Use $A.localizationService to use the methods in AuraLocalizationService .

Methods

IN THIS SECTION:

UTCToWallTime()
Converts a datetime from UTC to a specified timezone.

WallTimeToUTC
Converts a datetime from a specified timezone to UTC.

displayDuration()
Displays a length of time.

displayDurationInDays()
Displays a length of time in days.

displayDurationInHours()
Displays a length of time in hours.

displayDurationInMilliseconds()
Displays a length of time in milliseconds.

displayDurationInMinutes()
Displays a length of time in minutes.

displayDurationInMonths()
Displays a length of time in months.

displayDurationInSeconds()
Displays a length of time in seconds.

duration()
Returns an object representing a length of time.

endOf()
Returns a date that is the end of a unit of time for the given date.


Reference AuraLocalizationService

formatCurrency()
Returns a currency number based on the default currency format.

formatDate()
Returns a formatted date.

formatDateTime()
Returns a formatted date time.

formatDateTimeUTC()
Returns a formatted date time in UTC.

formatDateUTC()
Returns a formatted date in UTC.

formatNumber()
Returns a formatted number with the default number format.

formatPercent()
Returns a formatted percentage number based on the default percentage format.

formatTime()
Returns a formatted time.

formatTimeUTC()
Returns a formatted time in UTC.

getDateStringBasedOnTimezone
Gets a date string based on a time zone.

getDaysInDuration()
Returns the number of days in a duration.

getDefaultCurrencyFormat()
Returns the default currency format.

getDefaultNumberFormat()
Returns the default `NumberFormat` object.

getDefaultPercentFormat()
Returns the default percentage format.

getHoursInDuration()
Returns a length of time in hours.

getLocalizedDateTimeLabels()
Deprecated. Do not use. Returns date time labels, such as month name, weekday name.

getMillisecondsInDuration()
Returns the number of milliseconds in a duration.

getMinutesInDuration()
Returns the number of minutes in a duration.

getMonthsInDuration()
Returns the number of months in a duration.

getNumberFormat()
Returns a `NumberFormat` object.


Reference AuraLocalizationService

getSecondsInDuration()
Returns the number of seconds in a duration.

getToday
Gets today’s date based on a time zone.

getYearsInDuration()
Returns the number of years in a duration.

isAfter()
Checks if `date1` is after `date2` .

isBefore()
Checks if `date1` is before `date2` .

isBetween()
Checks if `date` is between `fromDate` and `toDate`, where the match is inclusive.

isPeriodTimeView()
Deprecated. Do not use. Checks if a datetime pattern string uses a 24-hour or 12-hour time view.

isSame()
Checks if `date1` is the same as `date2` .

parseDateTime()
Parses a string and returns a JavaScript Date.

parseDateTimeISO8601()
Parses a date time string in an ISO-8601 format and returns a JavaScript Date.

parseDateTimeUTC()
Parses a string and returns a JavaScript Date.

startOf()
Returns a date that is the start of a unit of time for the given date.

toISOString()
Deprecated. Use `Date.toISOString()` instead.

translateFromLocalizedDigits()
Translate the localized digit string to a string with Arabic digits, if there is any.

translateFromOtherCalendar()
Translates the input date from another calendar system (for example, the Buddhist calendar) to the Gregorian calendar based on
the locale.

translateToLocalizedDigits()
Translate the input string to a string with localized digits, if there is any.

translateToOtherCalendar()
Translates the input date to a date in another calendar system (for example, the Buddhist calendar) based on the locale.

SEE ALSO:

Formatting Dates in JavaScript


Reference AuraLocalizationService

#### UTCToWallTime()

Converts a datetime from UTC to a specified timezone.

Signature

```
   UTCToWallTime (Date date, String timezone, function callback)

```

Parameters

```
   date
```

Type: `Date`

A JavaScript `Date` object.

```
   timezone
```

Type: `String`

A time zone ID based on the class, for example, `"America/Los_Angeles"` .

```
   callback
```

Type: `function`

A function to call after the conversion is done. Access the converted value in the first parameter of the callback.

Sample Code

```
   var format = $A.get("$Locale.timeFormat");

   format = format.replace(":ss", "");

   var langLocale = $A.get("$Locale.langLocale");

   var timezone = $A.get("$Locale.timezone");

   var date = new Date();

   $A.localizationService.UTCToWallTime(date, timezone, function(walltime) {

      // Returns the local time without the seconds, for example, 9:00 PM

     displayValue = $A.localizationService.formatDateTimeUTC(walltime, format, langLocale);

   })

#### WallTimeToUTC

```

Converts a datetime from a specified timezone to UTC.

Signature

#### `WallTimeToUTC (Date date, string timezone, function callback)`

Parameters

```
   date
```

Type: `Date`

A JavaScript `Date` object.

```
   timezone
```

Type: `String`


Reference AuraLocalizationService

A time zone ID based on the class, for example, `"America/Los_Angeles"` .

```
   callback
```

Type: `function`

A function to call after the conversion is done. Access the converted value in the first parameter of the callback.

#### displayDuration()

Displays a length of time.

Signature

```
   displayDuration (Duration duration, boolean withSuffix)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

```
   withSuffix
```

Type: `boolean`

If `true`, returns value with a suffix matching the unit of the _`duration`_ parameter.

Returns

**Type:** **`String`**
The length of time.

Sample Code

```
   var dur = $A.localizationService.duration(1, 'day');

   // Returns "a day"

   var length = $A.localizationService.displayDuration(dur);

```

SEE ALSO:

duration()

#### displayDurationInDays()

Displays a length of time in days.

Signature

```
   displayDurationInDays (Duration duration)

```


Reference AuraLocalizationService

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The length of time in days.

Sample Code

```
   var dur = $A.localizationService.duration(24, 'hour');

   // Returns 1

   var length = $A.localizationService.displayDurationInDays(dur);

```

SEE ALSO:

duration()

#### displayDurationInHours()

Displays a length of time in hours.

Signature

```
   displayDurationInHours (Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The length of time in hours.

Sample Code

```
   var dur = $A.localizationService.duration(2, 'day');

   // Returns 48

   var length = $A.localizationService.displayDurationInHours(dur);

```

SEE ALSO:

duration()


Reference AuraLocalizationService

#### displayDurationInMilliseconds()

Displays a length of time in milliseconds.

Signature

```
   displayDurationInMilliseconds (Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The length of time in milliseconds.

Sample Code

```
   var dur = $A.localizationService.duration(1, 'hour');

   // Returns 3600000

   var length = $A.localizationService.displayDurationInMilliseconds(dur);

```

SEE ALSO:

duration()

#### displayDurationInMinutes()

Displays a length of time in minutes.

Signature

```
   displayDurationInMinutes (Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The length of time in minutes.


Reference AuraLocalizationService

Sample Code

```
   var dur = $A.localizationService.duration(1, 'hour');

   // Returns 60

   var length = $A.localizationService.displayDurationInMinutes(dur);

```

SEE ALSO:

duration()

#### displayDurationInMonths()

Displays a length of time in months.

Signature

```
   displayDurationInMonths (Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The length of time in months.

Sample Code

```
   var dur = $A.localizationService.duration(60, 'day');

   // Returns 1.971293

   var length = $A.localizationService.displayDurationInMonths(dur);

```

SEE ALSO:

duration()

#### displayDurationInSeconds()

Displays a length of time in seconds.

Signature

```
   displayDurationInSeconds (Duration duration)

```


Reference AuraLocalizationService

Parameters

#### _`duration`_

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The length of time in seconds.

Sample Code

```
   var dur = $A.localizationService.duration(60, 'minutes');

   // Returns 3600

   var length = $A.localizationService.displayDurationInSeconds(dur);

```

SEE ALSO:

#### duration() duration()

Returns an object representing a length of time.

Signature

```
   duration (number num, String unit)

```

Parameters

```
   num
```

Type: `number`

The length of time in a given unit.

```
   unit
```

Type: `String`

A datetime unit. The default is 'milliseconds'. The options are 'years, 'months', 'weeks', 'days', 'hour', 'minutes', 'seconds', 'milliseconds'.

Returns

**Type:** **`Object`**
A duration object.

Sample Code

```
   var dur = $A.localizationService.duration(2, 'days');

```


Reference AuraLocalizationService

#### endOf()

Returns a date that is the end of a unit of time for the given date.

Signature

```
   endOf(string | number | Date date, string unit)

```

Parameters

```
   date
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.

```
   unit
```

Type: `string`

A datetime unit. Options are 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'.

Returns

**Type:** **`Date`**
A JavaScript `Date` object. If a unit is not provided, returns a parsed date.

Sample Code

```
   var date = new Date();

   // Returns the time at the end of the day

   // in the format "Fri Oct 09 2015 23:59:59 GMT-0700 (PDT)"

   var day = $A.localizationService.endOf(date, 'day');

#### formatCurrency()

```

Returns a currency number based on the default currency format.

Signature

```
   formatCurrency (number number)

```

Parameters

```
   number
```

Type: `number`

The currency number to format.

Returns

**Type:** **`number`**
The formatted currency.


Reference AuraLocalizationService

Sample Code

```
   var curr = 123.45;

   // Returns $123.45

   $A.localizationService.formatCurrency(curr);

#### formatDate()

```

Returns a formatted date.

Signature

```
   formatDate (string | number | Date date, string formatString, string locale)

```

Parameters

```
   date
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object. If you provide a String value, use ISO 8601
format to avoid parsing warnings. If no timezone is specified, defaults to the browser timezone offset.

```
   formatString
```

Type: `string`

Optional. A string containing tokens to format the given date. For example, `"yyyy-MM-dd"` formats 15th January, 2017 as
"2017-01-15". The default format string comes from the `$Locale` value provider. For details on available tokens, see Formatting
Dates in JavaScript.

```
   locale
```

Type: `string`

Optional. A locale to format the given date. The default value is `$Locale.langLocale` . We strongly recommended that you
use the locale value from `$Locale` . We fall back to the value in `$Locale.langLocale` if you use an unavailable locale.

Returns

**Type:** **`string`**
A formatted and localized date string.

Sample Code

```
   var date = new Date();

   // Returns date in the format "Oct 9, 2015"

   $A.localizationService.formatDate(date);

#### formatDateTime()

```

Returns a formatted date time.

Signature

```
   formatDateTime (string | number | Date date, string formatString, string locale)

```


Reference AuraLocalizationService

Parameters

```
   date
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object. If you provide a String value, use ISO 8601
format to avoid parsing warnings. If no timezone is specified, defaults to the browser timezone offset.

```
   formatString
```

Type: `string`

Optional. A string containing tokens to format the given date. For example, `"yyyy-MM-dd"` formats 15th January, 2017 as
"2017-01-15". The default format string comes from the `$Locale` value provider. For details on available tokens, see Formatting
Dates in JavaScript.

```
   locale
```

Type: `string`

Optional. A locale to format the given date. The default value is `$Locale.langLocale` . We strongly recommended that you
use the locale value from `$Locale` . We fall back to the value in `$Locale.langLocale` if you use an unavailable locale.

Returns

**Type:** **`string`**
A formatted and localized date time string.

Sample Code

```
   var date = new Date();

   // Returns datetime in the format "Oct 9, 2015 9:00:00 AM"

   $A.localizationService.formatDateTime(date);

#### formatDateTimeUTC()

```

Returns a formatted date time in UTC.

Signature

```
   formatDateTimeUTC (string | number | Date date, string formatString, string locale)

```

Parameters

```
   date
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object. If you provide a String value, use ISO 8601
format to avoid parsing warnings. If no timezone is specified, defaults to the browser timezone offset.

```
   formatString
```

Type: `string`

Optional. A string containing tokens to format the given date. For example, `"yyyy-MM-dd"` formats 15th January, 2017 as
"2017-01-15". The default format string comes from the `$Locale` value provider. For details on available tokens, see Formatting
Dates in JavaScript.


Reference AuraLocalizationService

```
   locale
```

Type: `string`

Optional. A locale to format the given date. The default value is `$Locale.langLocale` . We strongly recommended that you
use the locale value from `$Locale` . We fall back to the value in `$Locale.langLocale` if you use an unavailable locale.

Returns

**Type:** **`string`**
A formatted and localized date time string.

Sample Code

```
   var date = new Date();

   // Returns datetime in UTC in the format "Oct 9, 2015 4:00:00 PM"

   $A.localizationService.formatDateTimeUTC(date);

#### formatDateUTC()

```

Returns a formatted date in UTC.

Signature

```
   formatDateUTC (string | number | Date date, string formatString, string locale)

```

Parameters

```
   date
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object. If you provide a String value, use ISO 8601
format to avoid parsing warnings. If no timezone is specified, defaults to the browser timezone offset.

```
   formatString
```

Type: `string`

Optional. A string containing tokens to format the given date. For example, `"yyyy-MM-dd"` formats 15th January, 2017 as
"2017-01-15". The default format string comes from the `$Locale` value provider. For details on available tokens, see Formatting
Dates in JavaScript.

```
   locale
```

Type: `string`

Optional. A locale to format the given date. The default value is `$Locale.langLocale` . We strongly recommended that you
use the locale value from `$Locale` . We fall back to the value in `$Locale.langLocale` if you use an unavailable locale.

Returns

**Type:** **`string`**
A formatted and localized date string.


Reference AuraLocalizationService

Sample Code

```
   var date = new Date();

   // Returns date in UTC in the format "Oct 9, 2015"

   $A.localizationService.formatDateUTC(date);

#### formatNumber()

```

Returns a formatted number with the default number format.

Signature

```
   formatNumber (number number)

```

Parameters

```
   number
```

Type: `number`

The number to format.

Returns

**Type:** **`number`**
The formatted number.

Sample Code

```
   var num = 10000;

   // Returns 10,000

   var formatted = $A.localizationService.formatNumber(num);

#### formatPercent()

```

Returns a formatted percentage number based on the default percentage format.

Signature

```
   formatPercent (number number)

```

Parameters

```
   number
```

Type: `number`

The number to format.

Returns

**Type:** **`number`**
The formatted percentage.


Reference AuraLocalizationService

Sample Code

```
   var num = 0.54;

   // Returns 54%

   var formatted = $A.localizationService.formatPercent(num);

#### formatTime()

```

Returns a formatted time.

Signature

```
   formatTime (string | number | Date date, string formatString, string locale)

```

Parameters

```
   date
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object. If you provide a String value, use ISO 8601
format to avoid parsing warnings. If no timezone is specified, defaults to the browser timezone offset.

```
   formatString
```

Type: `string`

Optional. A string containing tokens to format the given date. For example, `"yyyy-MM-dd"` formats 15th January, 2017 as
"2017-01-15". The default format string comes from the `$Locale` value provider. For details on available tokens, see Formatting
Dates in JavaScript.

```
   locale
```

Type: `string`

Optional. A locale to format the given date. The default value is `$Locale.langLocale` . We strongly recommended that you
use the locale value from `$Locale` . We fall back to the value in `$Locale.langLocale` if you use an unavailable locale.

Returns

**Type:** **`string`**
A formatted and localized time string.

Sample Code

```
   var date = new Date();

   // Returns a date in the format "9:00:00 AM"

   var now = $A.localizationService.formatTime(date);

#### formatTimeUTC()

```

Returns a formatted time in UTC.

Signature

```
   formatTime (string | number | Date date, string formatString, string locale)

```


Reference AuraLocalizationService

Parameters

```
   date
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object. If you provide a String value, use ISO 8601
format to avoid parsing warnings. If no timezone is specified, defaults to the browser timezone offset.

```
   formatString
```

Type: `string`

Optional. A string containing tokens to format the given date. For example, `"yyyy-MM-dd"` formats 15th January, 2017 as
"2017-01-15". The default format string comes from the `$Locale` value provider. For details on available tokens, see Formatting
Dates in JavaScript.

```
   locale
```

Type: `string`

Optional. A locale to format the given date. The default value is `$Locale.langLocale` . We strongly recommended that you
use the locale value from `$Locale` . We fall back to the value in `$Locale.langLocale` if you use an unavailable locale.

Returns

**Type:** **`string`**
A formatted and localized time string.

Sample Code

```
   var date = new Date();

   // Returns time in UTC in the format "4:00:00 PM"

   $A.localizationService.formatTimeUTC(date);

#### getDateStringBasedOnTimezone

```

Gets a date string based on a time zone.

Signature

#### `getDateStringBasedOnTimezone (string timeZone, Date date, function callback)`

Parameters

```
   timezone
```

Type: `String`

A time zone ID based on the class, for example, `"America/Los_Angeles"` .

```
   date
```

Type: `Date`

A JavaScript `Date` object.

```
   callback
```

Type: `function`

A function to call after the date string is returned. Access the date string in the first parameter of the callback.


Reference AuraLocalizationService

Sample Code

```
   var timezone = $A.get("$Locale.timezone");

   var date = new Date();

   // Returns the date string in the format "2015-10-9"

   $A.localizationService.getDateStringBasedOnTimezone(timezone, date, function(today){

      console.log(today);

   });

#### getDaysInDuration()

```

Returns the number of days in a duration.

Signature

```
   getDaysInDuration(Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The number of days in the duration.

Sample Code

```
   var dur = $A.localizationService.duration(48, 'hour');

   // Returns 2, the number of days for the given duration

   $A.localizationService.getDaysInDuration(dur);

```

SEE ALSO:

duration()

#### getDefaultCurrencyFormat()

Returns the default currency format.

Signature

#### `getDefaultCurrencyFormat()`

Returns

**Type:** **`NumberFormat`**
The currency format returned by `$Locale.currencyFormat` .


Reference AuraLocalizationService

Sample Code

```
   // Returns $20,000.00

   $A.localizationService.getDefaultCurrencyFormat().format(20000);

```

SEE ALSO:

$Locale

#### getDefaultNumberFormat()

Returns the default `NumberFormat` object.

Signature

#### `getDefaultNumberFormat()`

Returns

**Type:** **`NumberFormat`**
The number format returned by `$Locale.numberFormat` .

Sample Code

```
   // Returns 20,000.123

   $A.localizationService.getDefaultNumberFormat().format(20000.123);

```

SEE ALSO:

$Locale

#### getDefaultPercentFormat()

Returns the default percentage format.

Signature

#### `getDefaultPercentFormat()`

Returns

**Type:** **`NumberFormat`**
The percentage format returned by `$Locale.percentFormat` .


Reference AuraLocalizationService

Sample Code

```
   // Returns 20%

   $A.localizationService.getDefaultPercentFormat().format(0.20);

```

SEE ALSO:

$Locale

#### getHoursInDuration()

Returns a length of time in hours.

Signature

```
   getHoursInDuration(Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The number of hours in the duration.

Sample Code

```
   var dur = $A.localizationService.duration(60, 'minute');

   // Returns 1, the number of hours in the given duration

   $A.localizationService.getHoursInDuration(dur);

```

SEE ALSO:

duration()

#### getLocalizedDateTimeLabels()

Deprecated. Do not use. Returns date time labels, such as month name, weekday name.

Signature

#### `getLocalizedDateTimeLabels()`

Returns

**Type:** **`Object`**
The localized set of labels.


Reference AuraLocalizationService

#### getMillisecondsInDuration()

Returns the number of milliseconds in a duration.

Signature

```
   getMillisecondsInDuration(Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The number of milliseconds in the duration.

SEE ALSO:

duration()

#### getMinutesInDuration()

Returns the number of minutes in a duration.

Signature

```
   getMinutesInDuration(Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The number of minutes in the duration.


Reference AuraLocalizationService

Sample Code

```
   var dur = $A.localizationService.duration(60, 'second');

   // Returns 1, the number of minutes in the given duration

   $A.localizationService.getMinutesInDuration(dur);

```

SEE ALSO:

duration()

#### getMonthsInDuration()

Returns the number of months in a duration.

Signature

```
   getMonthsInDuration(Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The number of months in the duration.

Sample Code

```
   var dur = $A.localizationService.duration(70, 'day');

   // Returns 2, the number of months in the given duration

   $A.localizationService.getMonthsInDuration(dur);

```

SEE ALSO:

duration()

#### getNumberFormat()

Returns a `NumberFormat` object.

Signature

```
   getNumberFormat(string format, string symbols)

```


Reference AuraLocalizationService

Parameters

```
   format
```

Type: `string`

The number format. For example, `format=".00"` displays the number followed by two decimal places.

```
   symbols
```

Type: `string`

An optional map of localized symbols. Otherwise, the current locale’s symbols are used.

Returns

**Type:** **`NumberFormat`**
The number format returned by `$Locale.numberFormat` .

Sample Code

```
   var f = $A.get("$Locale.numberFormat");

   var num = 10000

   var nf = $A.localizationService.getNumberFormat(f);

   var formatted = nf.format(num);

   // Returns 10,000

   var formatted = $A.localizationService.formatNumber(num);

#### getSecondsInDuration()

```

Returns the number of seconds in a duration.

Signature

```
   getSecondsInDuration(Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .

Returns

**Type:** **`number`**
The number of seconds in the duration.


Reference AuraLocalizationService

Sample Code

```
   var dur = $A.localizationService.duration(3000, 'millisecond');

   // Returns 3

   $A.localizationService.getSecondsInDuration(dur);

```

SEE ALSO:

duration()

#### getToday

Gets today’s date based on a time zone.

Signature

#### `getToday(string timezone, function callback)`

Parameters

```
   timezone
```

Type: `String`

A time zone ID based on the class, for example, `"America/Los_Angeles"` .

```
   callback
```

Type: `function`

A function to call after the date is returned. Access the date in the first parameter of the callback.

Sample Code

```
   var timezone = $A.get("$Locale.timezone");

   // Returns the date string in the format "2015-11-25"

   $A.localizationService.getToday(timezone, function(today){

      console.log(today);

   });

#### getYearsInDuration()

```

Returns the number of years in a duration.

Signature

```
   getYearsInDuration(Duration duration)

```

Parameters

```
   duration
```

Type: `Duration`

The duration object returned by `$A.localizationService.duration` .


Reference AuraLocalizationService

Returns

**Type:** **`number`**
The number of years in the duration.

Sample Code

```
   var dur = $A.localizationService.duration(24, 'month');

   // Returns 2

   $A.localizationService.getYearsInDuration(dur);

```

SEE ALSO:

duration()

#### isAfter()

Checks if `date1` is after `date2` .

Signature

```
   isAfter(string | number | Date date1, string | number | Date date2, string unit)

```

Parameters

```
   date1
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.

```
   date2
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.

```
   unit
```

Type: `string`

A datetime unit. Options are 'year', 'month', 'week', 'day', 'hour', 'minute', 'second', or 'millisecond'.

Returns

**Type:** **`boolean`**

Returns `true` if `date1` is after `date2`, or `false` otherwise.

Sample Code

```
   var date = new Date();

   var day = $A.localizationService.endOf(date, 'day');

   // Returns false, since date is before day

   $A.localizationService.isAfter(date, day);

```


Reference AuraLocalizationService

#### isBefore()

Checks if `date1` is before `date2` .

Signature

```
   isBefore(string | number | Date date1, string | number | Date date2, string unit)

```

Parameters

```
   date1
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.

```
   date2
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.

```
   unit
```

Type: `string`

A datetime unit. Options are 'year', 'month', 'week', 'day', 'hour', 'minute', 'second', or 'millisecond'.

Returns

**Type:** **`boolean`**

Returns `true` if `date1` is before `date2`, or `false` otherwise.

Sample Code

```
   var date = new Date();

   var day = $A.localizationService.endOf(date, 'day');

   // Returns true, since date is before day

   $A.localizationService.isBefore(date, day);

#### isBetween()

```

Checks if `date` is between `fromDate` and `toDate`, where the match is inclusive.

Signature

```
   isBetween(string | number | Date date, string | number | Date fromDate, string | number

   | Date toDate, string unit)

```

Parameters

```
   date
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.


Reference AuraLocalizationService

```
   fromDate
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.

```
   toDate
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.

```
   unit
```

Type: `string`

A datetime unit. Options are 'year', 'month', 'week', 'day', 'hour', 'minute', 'second', or 'millisecond'.

Returns

**Type:** **`boolean`**

Returns `true` if `date` is between `fromDate` and `toDate`, or `false` otherwise.

Sample Code

```
   // Returns true

   $A.localizationService.isBetween("2017-03-07","March 7, 2017", "12/1/2017");

   // Returns false

   $A.localizationService.isBetween("2017-03-07 12:00", "March 7, 2017 15:00", "12/1/2017");

   // Returns true because the unit is "day"

   $A.localizationService.isBetween("2017-03-07 12:00", "March 7, 2017 15:00", "12/1/2017",

   "day");

#### isPeriodTimeView()

```

Deprecated. Do not use. Checks if a datetime pattern string uses a 24-hour or 12-hour time view.

Signature

```
   isPeriodTimeView(string pattern)

```

Parameters

```
   pattern
```

Type: `string`

A datetime pattern.

Returns

**Type:** **`boolean`**

Returns `true` if the pattern uses a 12-hour period time view.

#### isSame()

Checks if `date1` is the same as `date2` .


Reference AuraLocalizationService

Signature

```
   isSame(string | number | Date date1, string | number | Date date2, string unit)

```

Parameters

```
   date1
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.

```
   date2
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.

```
   unit
```

Type: `string`

A datetime unit. Options are 'year', 'month', 'week', 'day', 'hour', 'minute', 'second', or 'millisecond'.

Returns

**Type:** **`boolean`**

Returns `true` if `date1` is the same as `date2`, or `false` otherwise.

Sample Code

```
   var date = new Date();

   var day = $A.localizationService.endOf(date, 'day');

   // Returns false

   $A.localizationService.isSame(date, day, 'hour');

   // Returns true

   $A.localizationService.isSame(date, day, 'day');

#### parseDateTime()

```

Parses a string and returns a JavaScript Date.

Signature

```
   parseDateTime(string dateTimeString, string parseFormat, string | boolean locale,

   boolean strictParsing)

```

Parameters

```
   dateTimeString
```

Type: `string`

A datetime string.

```
   parseFormat
```

Type: `string`

An optional Java format string used to parse the datetime. The default is from the `$Locale` global value provider.


Reference AuraLocalizationService

```
   locale
```

Type: `string | boolean`

This parameter is deprecated.

```
   strictParsing
```

Type: `string`

Set this optional parameter to `true` to turn off forgiving parsing and use strict validation.

Returns

**Type:** **`Date`**
Returns a JavaScript `Date` object, or `null` if `dateTimeString` is invalid.

#### parseDateTimeISO8601()

Parses a date time string in an ISO-8601 format and returns a JavaScript Date.

Signature

```
   parseDateTimeISO8601(string dateTimeString)

```

Parameters

```
   dateTimeString
```

Type: `string`

A datetime string in ISO8601 format.

Returns

**Type:** **`Date`**
Returns a JavaScript `Date` object, or `null` if `dateTimeString` is invalid.

#### parseDateTimeUTC()

Parses a string and returns a JavaScript Date.

Signature

```
   parseDateTime(string dateTimeString, string parseFormat, string | boolean locale,

   boolean strictParsing)

```

Parameters

```
   dateTimeString
```

Type: `string`

A datetime string.

```
   parseFormat
```

Type: `string`


Reference AuraLocalizationService

An optional Java format string used to parse the datetime. The default is from the `$Locale` global value provider.

```
   locale
```

Type: `string | boolean`

This parameter is deprecated.

```
   strictParsing
```

Type: `string`

Set this optional parameter to `true` to turn off forgiving parsing and use strict validation.

Returns

**Type:** **`Date`**
Returns a JavaScript `Date` object, or `null` if `dateTimeString` is invalid.

Sample Code

```
   var date = "2015-10-9";

   // Returns "Thu Oct 08 2015 17:00:00 GMT-0700 (PDT)"

   $A.localizationService.parseDateTimeUTC(date);

#### startOf()

```

Returns a date that is the start of a unit of time for the given date.

Signature

```
   startOf(string | number | Date date, string unit)

```

Parameters

```
   date
```

Type: `string | number | Date`

A datetime string in ISO8601 format, or a timestamp in milliseconds, or a `Date` object.

```
   unit
```

Type: `string`

A datetime unit. Options are 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'.

Returns

**Type:** **`Date`**
A JavaScript `Date` object. If a unit is not provided, returns a parsed date.

Sample Code

```
   var date = "2015-10-9";

   // Returns "Thu Oct 01 2015 00:00:00 GMT-0700 (PDT)"

   $A.localizationService.startOf(date, 'month');

```


Reference AuraLocalizationService

#### toISOString()

Deprecated. Use `Date.toISOString()` instead.

Signature

```
   toISOString(Date | T date)

```

Parameters

```
   date
```

Type: `Date | T`

A `Date` object.

```
   unit
```

Type: `string`

A datetime unit. Options are 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'.

Returns

**Type:** **`Date`**
An ISO8601 string.

#### translateFromLocalizedDigits()

Translate the localized digit string to a string with Arabic digits, if there is any.

Signature

```
   translateFromLocalizedDigits(string input)

```

Parameters

```
   input
```

Type: `string`

A string with localized digits.

Returns

**Type:** **`string`**
A string with Arabic digits.

#### translateFromOtherCalendar()

Translates the input date from another calendar system (for example, the Buddhist calendar) to the Gregorian calendar based on the
locale.


Reference AuraLocalizationService

Signature

```
   translateFromOtherCalendar(Date date)

```

Parameters

```
   date
```

Type: `Date`

A `Date` object.

Returns

**Type:** **`Date`**
Returns a translated `Date` object.

#### translateToLocalizedDigits()

Translate the input string to a string with localized digits, if there is any.

Signature

```
   translateToLocalizedDigits(string input)

```

Parameters

```
   input
```

Type: `string`

A string with Arabic digits.

Returns

**Type:** **`string`**
A string with localized digits.

#### translateToOtherCalendar()

Translates the input date to a date in another calendar system (for example, the Buddhist calendar) based on the locale.

Signature

```
   translateToOtherCalendar(Date date)

```

Parameters

```
   date
```

Type: `Date`

A `Date` object.


### Reference Component

Returns

**Type:** **`Date`**
Returns a translated `Date` object.

### Component Component contains methods to work with components.

Methods

IN THIS SECTION:

addEventHandler()
Dynamically adds an event handler for a component or application event.

addHandler()
Deprecated. Use `addEventHandler()` instead.

addValueHandler()
Adds handlers to values owned by the component.

addValueProvider()
Adds custom value providers to a component.

autoDestroy()
Sets a flag to tell the rendering service whether or not to destroy this component when it is removed from its rendering facet.

clearReference()
Clears a live reference for the value passed in using property syntax. For example, if you use `aura:set` to set a value and later
want to reset the value using `component.set()`, clear the reference before resetting the value.

destroy()
Destroys the component and cleans up memory. After a component that is declared in markup is no longer in use, the framework
automatically destroys it and frees up its memory. If you create a component dynamically in JavaScript and that component isn't
added to a facet ( `v.body` or another attribute of type `Aura.Component[]` ), you have to destroy it manually using `destroy()`
to avoid memory leaks.

find()
Locates a component using its local ID ( `aura:id` ).

get()
Returns the value referenced using property syntax. For example, `cmp.get("v.attr")` returns the value of the `attr` attribute.

getConcreteComponent()
Gets the concrete implementation of a component. If the component is concrete, the method returns the component itself. For
example, call this method to get the concrete component of a super component.

getElement()
If the component renders only a single element, return it. Otherwise, use `getElements()` .

getElements()
Returns a map of the elements rendered by the component.


Reference Component

getEvent()
Returns a new event instance of the named component event.

getGlobalId()
Gets the global ID, which is the generated globally unique id of the component. It can be used to locate the instance later, but will
change across page loads.

getLocalId()
Gets the ID set using the `aura:id` attribute. Pass the local ID into `find()` on the parent component to locate this child
component.

getName()
Returns the component’s code-compatible camel case name, such as `'lightningButton'` .

getReference()
Returns a live reference to the value indicated using property syntax. This method is useful when you dynamically create a component.

getSuper()
Returns the super component.

getType()
Returns the component’s canonical type; for example, `'lightning:button'` .

getVersion()
Returns the component’s version number.

isConcrete()
Returns `true` if the component is concrete, or `false` otherwise. A concrete component is a sub-component in an inheritance
chain.

isInstanceOf()
Checks whether a component is an instance of the given component or interface name.

isValid()
Returns `true` if the component has not been destroyed.

removeEventHandler()
Dynamically removes a component event handler for the specified event.

set()
Sets the value referenced using property syntax.

#### addEventHandler()

Dynamically adds an event handler for a component or application event.

Signature

```
   addEventHandler(String event, function handler, String phase, Boolean includeFacets)

```

Parameters

```
   event
```

Type: `String`


Reference Component

The name of the event to handle. For a component event, set this argument to match the name attribute of the
`aura:registerEvent` tag. For an application event, set this argument to match the event descriptor,
`namespace:eventName` .

```
   handler
```

Type: `function`

The handler for the event. There are two format options for this argument.

**•** To use a controller action, use the format: `cmp.getReference("c.` _**`actionName`**_ `")` .

**•** To use an anonymous function, use the format: `function(auraEvent) { // handling logic here }`

```
   phase
```

Type: `String`

Optional. The event bubbling phase for which to add the handler. The default value is `"bubble"` .

```
   includeFacets
```

Type: `Boolean`

If `true`, attempts to catch events generated by components transcluded by facets; for example `v.body` .

Sample Code

```
   // For component event, first param matches name attribute in <aura:registerEvent> tag

   cmp.addEventHandler("compEvent", cmp.getReference("c.handleEvent"));

   // For application event, first param is event descriptor, "c:appEvent"

   cmp.addEventHandler("c:appEvent", cmp.getReference("c.handleAppEvent"));

   // Anonymous function handler for component event

   cmp.addEventHandler("compEvent", function(auraEvent) {

      // add handler logic here

      console.log("Handled the component event in anonymous function");

   });

```

SEE ALSO:

Dynamically Adding Event Handlers To a Component

removeEventHandler()

#### addHandler()

Deprecated. Use `addEventHandler()` instead.

Signature

```
   addHandler(String eventName, Object valueProvider, Object actionExpression, Boolean

   insert, String phase, Boolean includeFacets)

```

Parameters

```
   eventName
```

Type: `String`


Reference Component

The name of the event to handle. For a component event, set this argument to match the name attribute of the
`aura:registerEvent` tag. For an application event, set this argument to match the event descriptor,
`namespace:eventName` .

```
   valueProvider
```

Type: `Object`

The value provider to use for resolving the `actionExpression` .

```
   actionExpression
```

Type: `Object`

The expression to use for resolving the handler action against the given `valueProvider` .

```
   insert
```

Type: `Boolean`

If `true`, put the handler at the beginning instead of the end of the handler array.

```
   phase
```

Type: `String`

Optional. The event bubbling phase for which to add the handler. The default value is `"bubble"` .

```
   includeFacets
```

Type: `Boolean`

If `true`, attempts to catch events generated by components transcluded by facets; for example `v.body` .

SEE ALSO:

addEventHandler()

#### addValueHandler()

Adds handlers to values owned by the component.

Signature

```
   addValueHandler(Object config)

```

Parameters

```
   config
```

Type: `Object`

The value event, such as `"change"`, and the action, such as `"c.myAction"` .

#### addValueProvider()

Adds custom value providers to a component.

Signature

```
   addValueProvider(String key, Object valueProvider)

```


Reference Component

Parameters

```
   key
```

Type: `String`

Key to identify the value provider. Used in expressions in markup.

```
   valueProvider
```

Type: `Object`

The object to request data from. Must implement `get(expression)`, can implement `set(key,value)` .

SEE ALSO:

Value Providers

#### autoDestroy()

Sets a flag to tell the rendering service whether or not to destroy this component when it is removed from its rendering facet.

Signature

```
   autoDestroy(Boolean destroy)

```

Parameters

```
   destroy
```

Type: `Boolean`

Default is `true`, which marks the component to be destroyed when it’s orphaned. Set to `false` to keep a reference to a component
after it has been unrendered or removed from a parent facet. We don't recommend setting the value to `false` . If you do, be careful
to avoid memory leaks.

#### clearReference()

Clears a live reference for the value passed in using property syntax. For example, if you use `aura:set` to set a value and later want
to reset the value using `component.set()`, clear the reference before resetting the value.

Signature

```
   clearReference(String key)

```

Parameters

```
   key
```

Type: `String`

The data key for which to clear the reference. For example, `"v.attributeName"` .


Reference Component

#### destroy()

Destroys the component and cleans up memory. After a component that is declared in markup is no longer in use, the framework
automatically destroys it and frees up its memory. If you create a component dynamically in JavaScript and that component isn't added
#### to a facet ( v.body or another attribute of type Aura.Component[] ), you have to destroy it manually using destroy() to

avoid memory leaks.

Signature

#### `destroy()` find()

Locates a component using its local ID ( `aura:id` ).

Returns different types depending on the result.

**1.** If the local ID is unique, returns the component.

**2.** If there are multiple components with the same local ID, returns an array of the components.

**3.** If there is no matching local ID, returns `undefined` .

Signature

```
   find(String | Object name)

```

Parameters

```
   name
```

Type: `String | Object`

If name is an object, return instances of it. Otherwise, finds a component using its `aura:id` .

SEE ALSO:

Finding Components by ID

#### get()

Returns the value referenced using property syntax. For example, `cmp.get("v.attr")` returns the value of the `attr` attribute.

Signature

```
   get(String key)

```

Parameters

```
   key
```

Type: `String`

The data key to look up on the component.


Reference Component

#### getConcreteComponent()

Gets the concrete implementation of a component. If the component is concrete, the method returns the component itself. For example,
call this method to get the concrete component of a super component.

Signature

#### `getConcreteComponent()`

SEE ALSO:

Favor Composition Over Inheritance

#### getElement() If the component renders only a single element, return it. Otherwise, use getElements() .

Signature

#### `getElement()` getElements()

Returns a map of the elements rendered by the component.

Signature

#### `getElements()` getEvent()

Returns a new event instance of the named component event.

Signature

```
   getEvent(String name)

```

Parameters

```
   name
```

Type: `String`

The name of the event.

Sample Code

```
   // evtName matches the name attribute in aura:registerEvent

   cmp.getEvent("evtName");

```


Reference Component

#### getGlobalId()

Gets the global ID, which is the generated globally unique id of the component. It can be used to locate the instance later, but will
change across page loads.

Signature

#### `getGlobalId()`

SEE ALSO:

Component IDs

#### getLocalId()

Gets the ID set using the `aura:id` attribute. Pass the local ID into `find()` on the parent component to locate this child component.

Signature

#### `getLocalId()`

SEE ALSO:

find()

#### getName()

Returns the component’s code-compatible camel case name, such as `'lightningButton'` .

Signature

#### `getName()`

Returns

**Type:** **`String`**
The component name.

#### getReference()

Returns a live reference to the value indicated using property syntax. This method is useful when you dynamically create a component.

Signature

```
   getReference(String key)

```

Parameters

```
   key
```

Type: `String`


Reference Component

The data key for which to return a reference.

Returns

**Type:** **`PropertyReferenceValue`**
A property reference value.

#### getSuper()

Returns the super component.

Signature

#### `getSuper()`

Returns

**Type:** **`Component`**
The super component.

#### getType()

Returns the component’s canonical type; for example, `'lightning:button'` .

Signature

#### `getType()`

Returns

**Type:** **`String`**
The component’s type.

#### getVersion()

Returns the component’s version number.

Signature

#### `getVersion()`

Returns

**Type:** **`String`**
The component name.

#### isConcrete()

Returns `true` if the component is concrete, or `false` otherwise. A concrete component is a sub-component in an inheritance chain.


Reference Component

Signature

```
   isConcrete()

```

Returns

**Type:** **`Boolean`**
Returns `true` if the component is concrete, or `false` otherwise.

SEE ALSO:

getConcreteComponent()

Favor Composition Over Inheritance

#### isInstanceOf()

Checks whether a component is an instance of the given component or interface name.

Signature

```
   isInstanceOf(String name)

```

Parameters

```
   name
```

Type: `String`

The name of the component or interface, with a format of `namespace:componentName` .

Returns

**Type:** **`Boolean`**
Returns `true` if the component is an instance, or `false` otherwise.

#### isValid()

Returns `true` if the component has not been destroyed.

Signature

#### `isValid()`

Returns

**Type:** **`Boolean`**
Returns `true` if the component has not been destroyed, or `false` otherwise.

#### removeEventHandler()

Dynamically removes a component event handler for the specified event.


### Reference Event

Signature

```
   removeEventHandler(String event, function handler, String phase)

```

Parameters

```
   event
```

Type: `String`

The name of the event to remove; for example, `'c:myEvent'` .

```
   handler
```

Type: `function`

A reference to the function or action to remove; for example., `'cmp.getReference("c.handleMyEvent");'` .

```
   phase
```

Type: `String`

Optional. The event bubbling phase for which to remove the handler. The default value is `"default"` .

SEE ALSO:

addEventHandler()

#### set()

Sets the value referenced using property syntax.

Signature

```
   set(String key, Object value)

```

Parameters

```
   key
```

Type: `String`

The data key to set on the component; for example, `cmp.set("v.key","value")` .

```
   value
```

Type: `Object`

The value to set.

SEE ALSO:

get()

### Event Event contains methods to work with events. Use an event to communicate between components.


Reference Event

Methods

IN THIS SECTION:

fire()
Fires an event.

getEventType()
Returns the type of the event. Possible values are `'COMPONENT'` or `'APPLICATION'` .

getName()
Returns an event’s name.

getParam()
Returns the value of an event’s parameter.

getParams()
Returns the value of all an event’s parameters.

getPhase()
Returns the current phase of an event. Returns `undefined` if the event hasn’t been fired yet. Possible return values for application
and component events are `"capture"`, `"bubble"`, and `"default"` once fired. A value event returns `"default"` once
it’s fired.

getSource()
Returns the source component that fired an event.

getSourceEvent()
Returns the source event that fired this event, if it was fired by an event binding, such as `{!e.myEvent}` .

getType()
Returns the type of the event’s definition, such as `'c:myEvent'` .

pause()
Pauses an event. Event handlers aren’t processed until `Event.resume()` is called. The handling process pauses in the current
position of the event handler processing sequence. If the event is already paused, this method does nothing. This method throws
an error if it’s called in the `"default"` phase.

preventDefault()
Prevents the default phase execution for this event. This method throws an error if it’s called in the `"default"` phase.

resume()
Resumes event handling for this event from the same position in the event handler processing sequence from which it was previously
paused. If the event isn’t paused, this method does nothing. This method throws an error if it’s called in the `"default"` phase.
Any remaining event handlers might execute in the current call stack or might be deferred and executed in a new call stack. Therefore,
the exact timing behavior is not predictable.

setParam()
Sets a parameter for an event. This method doesn’t modify an event that has already been fired.

setParams()
Sets parameters for an event. This method doesn’t modify an event that has already been fired.

stopPropagation()
Sets whether the event can bubble or not. This method throws an error if called in the `"default"` phase.


Reference Event

#### fire()

Fires an event.

Signature

```
   fire(Object params)

```

Parameters

```
   params
```

Type: `Object`

An optional set of parameters for the event. Any previous parameters of the same name are overwritten.

#### getEventType()

Returns the type of the event. Possible values are `'COMPONENT'` or `'APPLICATION'` .

Signature

#### `getEventType()`

Returns

**Type:** **`String`**
The event type.

#### getName()

Returns an event’s name.

Signature

#### `getName()`

Returns

**Type:** **`String`**
The event name.

#### getParam()

Returns the value of an event’s parameter.

Signature

```
   getParam(String name)

```


Reference Event

Parameters

```
   name
```

Type: `String`

The parameter name. For example, `event.getParam("button")` returns the value of the pressed mouse button (0, 1, or
2).

Returns

**Type:** **`Object`**
The parameter value.

#### getParams()

Returns the value of all an event’s parameters.

Signature

#### `getParams()`

Returns

**Type:** **`Object`**
The collection of parameters.

#### getPhase()

Returns the current phase of an event. Returns `undefined` if the event hasn’t been fired yet. Possible return values for application
and component events are `"capture"`, `"bubble"`, and `"default"` once fired. A value event returns `"default"` once it’s
fired.

Signature

#### `getPhase()`

Returns

**Type:** **`String`**
The current phase of the event.

#### getSource()

Returns the source component that fired an event.

Signature

#### `getSource()`


Reference Event

Returns

**Type:** **`Object`**
The source component that fired the event.

#### getSourceEvent()

Returns the source event that fired this event, if it was fired by an event binding, such as `{!e.myEvent}` .

Signature

#### `getSourceEvent()`

Returns

**Type:** **`Object`**
The source event that fired the event.

#### getType()

Returns the type of the event’s definition, such as `'c:myEvent'` .

Signature

#### `getType()`

Returns

**Type:** **`String`**
The event definition type.

#### pause()

Pauses an event. Event handlers aren’t processed until `Event.resume()` is called. The handling process pauses in the current
position of the event handler processing sequence. If the event is already paused, this method does nothing. This method throws an
error if it’s called in the `"default"` phase.

Signature

#### `pause()` preventDefault()

Prevents the default phase execution for this event. This method throws an error if it’s called in the `"default"` phase.

Signature

#### `preventDefault()`


Reference Event

#### resume()

Resumes event handling for this event from the same position in the event handler processing sequence from which it was previously
paused. If the event isn’t paused, this method does nothing. This method throws an error if it’s called in the `"default"` phase. Any
remaining event handlers might execute in the current call stack or might be deferred and executed in a new call stack. Therefore, the
exact timing behavior is not predictable.

Signature

#### `resume()` setParam()

Sets a parameter for an event. This method doesn’t modify an event that has already been fired.

Signature

```
   setParam(String key, Object value)

```

Parameters

```
   key
```

Type: `String`

The name of the parameter.

```
   value
```

Type: `Object`

The value of the parameter.

#### setParams()

Sets parameters for an event. This method doesn’t modify an event that has already been fired.

Signature

```
   setParams(Object config)

```

Parameters

```
   config
```

Type: `Object`

The event’s parameter.

#### stopPropagation()

Sets whether the event can bubble or not. This method throws an error if called in the `"default"` phase.


### Reference Util

Signature

```
   stopPropagation()

### Util Util contains utility methods.

```

Methods

IN THIS SECTION:

#### addClass()

Adds a CSS class to a component.

getBooleanValue()
Coerces truthy and falsy values into a native boolean.

hasClass()
Checks whether the component has the specified CSS class.

isArray()
Checks whether the specified object is an array.

isEmpty()
Checks if the object is empty. An empty object’s value is `undefined`, `null`, an empty array, or an empty string. An object with
no native properties is not considered empty.

isObject()
Checks whether the specified object is a valid object. A valid object is not a DOM element, is not a native browser class
( `XMLHttpRequest` ) is not falsey, and is not an array, error, function string or a number.

isUndefined()
Checks if the object is `undefined` .

isUndefinedOrNull()
Checks if the object is `undefined` or `null` .

removeClass()
Removes a CSS class from a component.

toggleClass()
Toggles (adds or removes) a CSS class from a component.

#### addClass()

Adds a CSS class to a component.

Signature

```
   addClass(Object element, String newClass)

```


Reference Util

Parameters

```
   element
```

Type: `Object`

The component to apply the class on.

```
   newClass
```

Type: `String`

The CSS class to be applied.

Sample Code

```
   // find a component with aura:id="myCmp" in markup

   var myCmp = component.find("myCmp");

   $A.util.addClass(myCmp, "myClass");

#### getBooleanValue()

```

Coerces truthy and falsy values into a native boolean.

Signature

```
   getBooleanValue(Object val)

```

Parameters

```
   val
```

Type: `Object`

The object to check.

Returns

**Type:** **`String`**
Returns `true` if the object is truthy, or `false` otherwise.

#### hasClass()

Checks whether the component has the specified CSS class.

Signature

```
   hasClass(Object element, String className)

```

Parameters

```
   element
```

Type: `Object`

The component to check.


Reference Util

```
   className
```

Type: `String`

The CSS class name to check for.

Returns

**Type:** **`Boolean`**
Returns `true` if the specified class is found for the component, or `false` otherwise.

Sample Code

```
   // find a component with aura:id="myCmp" in markup

   var myCmp = component.find("myCmp");

   $A.util.hasClass(myCmp, "myClass");

#### isArray()

```

Checks whether the specified object is an array.

Signature

```
   isArray(Object obj)

```

Parameters

```
   obj
```

Type: `Object`

The object to check.

Returns

**Type:** **`Boolean`**
Returns `true` if the object is an array, or `false` otherwise.

#### isEmpty()

Checks if the object is empty. An empty object’s value is `undefined`, `null`, an empty array, or an empty string. An object with no
native properties is not considered empty.

Signature

```
   isEmpty(Object obj)

```

Parameters

```
   obj
```

Type: `Object`

The object to check.


Reference Util

Returns

**Type:** **`Boolean`**
Returns `true` if the object is empty, or `false` otherwise.

#### isObject()

Checks whether the specified object is a valid object. A valid object is not a DOM element, is not a native browser class
( `XMLHttpRequest` ) is not falsey, and is not an array, error, function string or a number.

Signature

```
   isObject(Object obj)

```

Parameters

```
   obj
```

Type: `Object`

The object to check.

Returns

**Type:** **`Boolean`**
Returns `true` if the object is a valid object, or `false` otherwise.

#### isUndefined()

Checks if the object is `undefined` .

Signature

```
   isUndefined(Object obj)

```

Parameters

```
   obj
```

Type: `Object`

The object to check.

Returns

**Type:** **`Boolean`**
Returns `true` if the object is undefined, or `false` otherwise.

#### isUndefinedOrNull()

Checks if the object is `undefined` or `null` .


Reference Util

Signature

```
   isUndefinedOrNull(Object obj)

```

Parameters

```
   obj
```

Type: `Object`

The object to check.

Returns

**Type:** **`Boolean`**
Returns `true` if the object is `undefined` or `null`, or `false` otherwise.

#### removeClass()

Removes a CSS class from a component.

Signature

```
   removeClass(Object element, String newClass)

```

Parameters

```
   element
```

Type: `Object`

The component to remove the class from.

```
   newClass
```

Type: `String`

The CSS class to be removed.

Sample Code

```
   //find a component with aura:id="myCmp" in markup

   var myCmp = component.find("myCmp");

   $A.util.removeClass(myCmp, "myClass");

#### toggleClass()

```

Toggles (adds or removes) a CSS class from a component.

Signature

```
   toggleClass(Object element, String className)

```


Reference Util

Parameters

```
   element
```

Type: `Object`

The component to add or remove the class from.

```
   className
```

Type: `String`

The CSS class to be added or removed.

Sample Code

```
   // find a component with aura:id="toggleMe" in markup

   var toggleText = component.find("toggleMe");

   $A.util.toggleClass(toggleText, "toggle");

```


INDEX

A

Apex
custom objects 420
Lightning components 453
records 420
saving records 415
standard objects 420
application, creating 7
Aura components
action override 155–156, 158
Lightning Experience 155–156
packaging 158
Salesforce 155–156

C

change handling 400
Component bundles
configuring design resources for Lightning Pages 191
configuring for Lightning App Builder 182, 199
configuring for Lightning Experience Record Home pages

configuring for Lightning Experience record pages 182
configuring for Lightning pages 182, 199
create dynamic picklists for components on Lightning Pages

tips for configuring for Lightning App Builder 199
Components
action override 155–156, 158
actions 144, 146, 148
custom app integration 241
flow, finish behavior 232
flow, resume 233
packaging 158
tabs 144–145
using 140, 144–146, 148, 155, 210, 454
Custom Actions
components 146, 148
Custom Lightning page template component
best practices 196
Custom Tabs
components 145

D

data access 382, 401, 407, 414
deleteRecord 398

Developer Edition organization, sign up 7

E

error handling 401
errors 252, 255, 257, 401
Events
Salesforce mobile and Lightning Experience demo 7
Salesforce mobile demo 10, 14
example 407

G

getNewRecord 392

L

Lightning App Builder
configuring custom components 182, 199
configuring design resources 191
create dynamic picklists for components 191
creating a custom page template 196
creating a width-aware component 197
Lightning components
custom app integration 241
Lightning Experience 144–146, 148
overview 180
Salesforce 144–146, 148
Lightning Container
javascript 248
messaging 250, 254
Lightning Data Service
create record 392
delete record 398
force:recordData 381
form display density 403
handling record changes 400
lightning:recordEditForm 381
lightning:recordForm 381
lightning:recordViewForm 381
load record 383
saveRecord 387
Lightning Out 246, 248
lightning:flexipageRegionInfo 197
lightning:formattedUrl 160
lightning:hasPageReference 159
lightning:isUrlAddressable 159, 165
lightning:navigation 159–160, 164–165


**Index**

N

Navigation
Default Field Values 161
Page Definitions 166
Node.js 248

P

Packaging
action override 158
Performance
caching 458
settings 458
Prerequisites 7

R

Rich Publisher Apps 241

S

SaveRecordResult 414
SharePoint 248
Standard Actions
Lightning components 155–156, 158
override 155–156, 158
packaging 158
standard controller 382, 401, 407, 414

T

troubleshooting 252, 255, 257

V

Visualforce 246

W

Width-aware Aura component 197

