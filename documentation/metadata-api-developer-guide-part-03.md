Then, change the `<type>` value in that same section to `default` instead of `flexipage` . Do this for every override you want to
reset. After making the changes, rezip the folder and deploy.

You can remove one override at a time each with its own deploy, or you can remove multiple overrides in a single deploy. However, we
recommend that you do a fresh retrieve every time you want to delete a new override. Don’t use a previously retrieved file.


Metadata Types CustomApplication

Retrieving Apps

To retrieve apps in your organization, use the CustomApplication type name in the `package.xml` manifest file. You can either retrieve
all apps or specify which apps to retrieve in the types section of `package.xml` .

To retrieve all apps in your organization—custom and standard apps, specify the wildcard character ( `*` ), as follows.

```
   <types>

      <members>*</members>

      <name>CustomApplication</name>

   </types>

```

Note: In API version 29.0 and earlier, use of the wildcard returns only all custom applications but not standard applications.

To retrieve a custom app, specify the app name.

```
   <types>

      <members>MyCustomApp</members>

      <name>CustomApplication</name>

   </types>

```

To retrieve a standard app, add the `standard__` prefix to the app name. For example, to retrieve the Chatter standard app, specify
`standard__Chatter` .

```
   <types>

      <members>standard__Chatter</members>

      <name>CustomApplication</name>

   </types>

```

To retrieve an app that is part of an installed package, add the package namespace prefix followed by two underscores and the app
name. For example, if the package namespace is `myInstalledPackageNS` and the app name is `PackageApp`, specify
`myInstalledPackageNS__PackageApp`, as follows.

```
   <types>

      <members>myInstalledPackageNS__PackageApp</members>

      <name>CustomApplication</name>

   </types>

```

Declarative Metadata Sample Definition

Here’s the definition of a custom Lightning Experience app:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomApplication xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>View</actionName>

        <comment>Action override created by Lightning App Builder during

   activation.</comment>

        <content>Custom_Mobile_Oppty_Page</content>

        <formFactor>Small</formFactor>

        <skipRecordTypeSelect>false</skipRecordTypeSelect>

        <type>Flexipage</type>

        <pageOrSobjectType>Opportunity</pageOrSobjectType>

      </actionOverrides>

      <actionOverrides>

```


Metadata Types CustomApplication

```
        <actionName>View</actionName>

        <comment>Action override created by Lightning App Builder during

   activation.</comment>

        <content>Custom_Mobile_Oppty_Page</content>

        <formFactor>Large</formFactor>

        <skipRecordTypeSelect>false</skipRecordTypeSelect>

        <type>Flexipage</type>

        <pageOrSobjectType>Opportunity</pageOrSobjectType>

      </actionOverrides>

      <brand>

        <headerColor>#EE1518</headerColor>

        <shouldOverrideOrgTheme>true</shouldOverrideOrgTheme>

      </brand>

      <description>Manage inventory and deliveries for our warehouses.</description>

      <formFactors>Small</formFactors>

      <formFactors>Large</formFactors>

      <isNavAutoTempTabsDisabled>false</isNavAutoTempTabsDisabled>

      <isNavPersonalizationDisabled>false</isNavPersonalizationDisabled>

      <label>Warehouse Lightning</label>

      <navType>Standard</navType>

      <profileActionOverrides>

        <actionName>View</actionName>

        <content>Warehouse_test_page</content>

        <formFactor>Large</formFactor>

        <pageOrSobjectType>Warehouse__c</pageOrSobjectType>

        <type>Flexipage</type>

        <profile>Admin</profile>

      </profileActionOverrides>

      <profileActionOverrides>

        <actionName>View</actionName>

        <content>Warehouse_test_page</content>

        <formFactor>Small</formFactor>

        <pageOrSobjectType>Warehouse__c</pageOrSobjectType>

        <type>Flexipage</type>

        <profile>Admin</profile>

      </profileActionOverrides>

      <setupExperience>all</setupExperience>

      <tabs>standard-Feed</tabs>

      <tabs>standard-File</tabs>

      <tabs>standard-Account</tabs>

      <tabs>standard-Case</tabs>

      <tabs>Merchandise__c</tabs>

      <tabs>Invoice__c</tabs>

      <tabs>Warehouse__c</tabs>

      <tabs>Delivery__c</tabs>

      <tabs>standard-report</tabs>

      <tabs>standard-Dashboard</tabs>

      <uiType>Lightning</uiType>

   </CustomApplication>

```

The following is a definition of a standard app (Chatter):

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomApplication xmlns="http://soap.sforce.com/2006/04/metadata">

      <defaultLandingTab>standard-home</defaultLandingTab>

```


Metadata Types CustomApplication

```
      <label>Collaboration</label>

      <tabs>standard-Chatter</tabs>

      <tabs>standard-UserProfile</tabs>

      <tabs>standard-OtherUserProfile</tabs>

      <tabs>standard-CollaborationGroup</tabs>

      <tabs>standard-File</tabs>

   </CustomApplication>

```

Declarative Metadata Sample Definition—Salesforce Console

The following is the definition of a custom app where `isServiceCloudConsole` is `true` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomApplication xmlns="http://soap.sforce.com/2006/04/metadata">

      <consoleConfig>

        <componentList>

           <alignment>left</alignment>

           <components>MyComponent</components>

        </componentList>

        <detailPageRefreshMethod>autoRefresh</detailPageRefreshMethod>

        <keyboardShortcuts>

           <customShortcuts>

             <action>MyCustomShortcutAction</action>

             <active>true</active>

             <keyCommand>X</keyCommand>

             <description>Custom Shortcut example</description>

             <eventName>myCustomShortcutExample</eventName>

           </customShortcuts>

           <defaultShortcuts>

             <action>FOCUS_CONSOLE</action>

             <active>true</active>

             <keyCommand>ESC</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_NAVIGATOR_TAB</action>

             <active>true</active>

             <keyCommand>V</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_DETAIL_VIEW</action>

             <active>true</active>

             <keyCommand>SHIFT+S</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_PRIMARY_TAB_PANEL</action>

             <active>true</active>

             <keyCommand>P</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_SUBTAB_PANEL</action>

             <active>true</active>

             <keyCommand>S</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

```


Metadata Types CustomApplication

```
             <action>FOCUS_LIST_VIEW</action>

             <active>true</active>

             <keyCommand>N</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_FIRST_LIST_VIEW</action>

             <active>true</active>

             <keyCommand>SHIFT+F</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_SEARCH_INPUT</action>

             <active>true</active>

             <keyCommand>R</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>MOVE_LEFT</action>

             <active>true</active>

             <keyCommand>LEFT ARROW</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>MOVE_RIGHT</action>

             <active>true</active>

             <keyCommand>RIGHT ARROW</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>UP_ARROW</action>

             <active>true</active>

             <keyCommand>UP ARROW</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>DOWN_ARROW</action>

             <active>true</active>

             <keyCommand>DOWN ARROW</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>OPEN_TAB_SCROLLER_MENU</action>

             <active>true</active>

             <keyCommand>D</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>OPEN_TAB</action>

             <active>true</active>

             <keyCommand>T</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>CLOSE_TAB</action>

             <active>true</active>

             <keyCommand>C</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>ENTER</action>

             <active>true</active>

             <keyCommand>ENTER</keyCommand>

           </defaultShortcuts>

```


Metadata Types CustomApplication

```
           <defaultShortcuts>

             <action>EDIT</action>

             <active>true</active>

             <keyCommand>E</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>SAVE</action>

             <active>true</active>

             <keyCommand>CTRL+S</keyCommand>

           </defaultShortcuts>

        </keyboardShortcuts>

        <listPlacement>

           <location>left</location>

           <units>percent</units>

           <width>20</width>

        </listPlacement>

        <listRefreshMethod>refreshList</listRefreshMethod>

        <pushNotifications>

           <fieldNames>CreatedBy</fieldNames>

           <objectName>Campaign</objectName>

        </pushNotifications>

        <pushNotifications>

           <fieldNames>CustomField1__c</fieldNames>

           <objectName>CustomObject1__c</objectName>

        </pushNotifications>

      </consoleConfig>

      <defaultLandingTab>standard-home</defaultLandingTab>

      <isServiceCloudConsole>true</isServiceCloudConsole>

      <label>MyConsole</label>

      <preferences>

        <enableCustomizeMyTabs>false</enableCustomizeMyTabs>

        <enableKeyboardShortcuts>true</enableKeyboardShortcuts>

        <enableListViewHover>true</enableListViewHover>

        <enableListViewReskin>true</enableListViewReskin>

        <enableMultiMonitorComponents>true</enableMultiMonitorComponents>

        <enablePinTabs>true</enablePinTabs>

        <enableTabHover>false</enableTabHover>

        <enableTabLimits>false</enableTabLimits>

        <saveUserSessions>false</saveUserSessions>

      </preferences>

      <tabs>standard-Case</tabs>

      <tabs>standard-Account</tabs>

      <tabs>standard-Contact</tabs>

      <tabs>standard-Contract</tabs>

      <workspaceConfig>

        <mappings>

           <tab>standard-Case</tab>

        </mappings>

        <mappings>

           <fieldName>ParentId</fieldName>

           <tab>standard-Account</tab>

        </mappings>

        <mappings>

           <fieldName>AccountId</fieldName>

```


### Metadata Types CustomApplicationComponent

```
           <tab>standard-Contact</tab>

        </mappings>

        <mappings>

           <tab>standard-Contract</tab>

        </mappings>

      </workspaceConfig>

   </CustomApplication>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomTab

### CustomApplicationComponent

Represents a custom console component (Visualforce page) assigned to a CustomApplication that is marked as a Salesforce console.
Custom console components extend the capabilities of Salesforce console apps. See Customize a Console with Custom Components
in Salesforce Classic in Salesforce Help.

File Suffix and Directory Location

Custom application components have the suffix `.customApplicationComponent` and are stored in the
`customApplicationComponents` folder.

Version

Custom applications are available in API version 25.0 and later.

Fields

**Field Name** **Field Type** **Description**

`buttonIconUrl` string The address of a page that hosts an icon for the button.

`buttonStyle` string The inline style used to define how the button looks.

`buttonText` string The label on the button used to launch the custom console component.

`buttonWidth` int The pixel width of the button displayed in the Salesforce console.

`height` int The pixel height of the window used to display the custom console
component.

`isHeightFixed` boolean Required. Indicates whether users can change the custom console
component height ( `false` ) or not ( `true` ).


### Metadata Types CustomFeedFilter

**Field Name** **Field Type** **Description**

`isHidden` boolean Required. Indicates whether the custom console component is hidden
from users ( `true` ) or not ( `false` ).

`isWidthFixed` boolean Required. Indicates whether users can change the component width
( `false` ) or not ( `true` ).

`visualforcePage` string Required. Name of the Visualforce page that represents the custom
console component.

`width` int The pixel width of the window used to display the custom console
component.

Declarative Metadata Sample Definition

The following is the definition of a custom application component:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomApplicationComponent xmlns="http://soap.sforce.com/2006/04/metadata">

      <buttonIconUrl>https://salesforce.com</buttonIconUrl>

      <buttonStyle>buttonStyleCSS</buttonStyle>

      <buttonText>buttonText</buttonText>

      <buttonWidth>200</buttonWidth>

      <height>200</height>

      <isHeightFixed>false</isHeightFixed>

      <isHidden>false</isHidden>

      <isWidthFixed>false</isWidthFixed>

      <visualforcePage>MyVisualforcePage</visualforcePage>

      <width>50</width>

   </CustomApplicationComponent>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomFeedFilter

Represents a custom feed filter that limits the feed view to feeds from the Cases object. The custom feed filter shows only feed items
that satisfy the criteria specified in the CustomFeedFilter definition. This type extends the Metadata metadata type and inherits its
`fullName` field.

File Suffix and Directory Location

### CustomFeedFilter components have the suffix .feedFilter and are stored in the feedFilters folder.


Metadata Types CustomFeedFilter

Version

CustomFeedFilter components are available in API version 35.0 and later.

Fields

**Field Name** **Field Type** **Description**

`criteria` FeedFilterCriterion The criterion that defines which feed items are shown when the filter is
on page 720 [] applied. The feed filter displays all feed items that satisfy the criteria.

`description` string The description of the custom feed filter. For example, specify what feed
items that filter shows.

`label` string Required. The API label of the custom feed filter.

`isProtected` boolean An auto-generated value. It currently has no impact.

FeedFilterCriterion

Represents the conditions that a feed item must satisfy to be displayed when a feed filter is applied.

**Field Name** **Field Type** **Description**

`feedItemType` FeedItemType (enumeration of type
Required. The type of feed items that the filter shows.
string)

The feed item type can be one of the following values:

**•** AttachArticleEvent

**•** CallLogPost

**•** CanvasPost

**•** CaseCommentPost

**•** ChangeStatusPost

**•** ChatTranscriptPost

**•** ContentPost

**•** CreateRecordEvent

**•** EmailMessageEvent

**•** LinkPost

**•** MilestoneEvent

**•** QuestionPost

**•** PollPost

**•** ReplyPost

**•** SocialPost

**•** TextPost


Metadata Types CustomFeedFilter

**Field Name** **Field Type** **Description**

`feedItemVisibility` FeedItemVisibility (enumeration of
type string)

`relatedSObjectType` string

Declarative Metadata Sample Definition

The following is an example of a CustomFeedFilter on page 719 component.

The visibility of feed items that the filter shows. For
example, you can show only poll posts that are visible
internally.

Valid values are:

**•** AllUsers

**•** InternalUsers

The API name of the object that the feed item refers to.
This field is typically used with the CreateRecordEvent
feed item type.

For example, a feed filter can show CreateRecordEvent
feed items for the Cases object.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomFeedFilter xmlns="http://soap.sforce.com/2006/04/metadata">

   <criteria>

     <feedItemType>CreateRecordEvent</feedItemType>

     <relatedSObjectType>MyCO01__c</relatedSObjectType>

   </criteria>

   <criteria>

     <feedItemType>CreateRecordEvent</feedItemType>

     <relatedSObjectType>Case</relatedSObjectType>

   </criteria>

   <criteria>

     <feedItemType>PollPost</feedItemType>

     <feedItemVisibility>InternalUsers</feedItemVisibility>

   </criteria>

   <label>Sample Custom Feed Filter</label>

</CustomFeedFilter>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>myCaseFeedFilter</members>

     <name>CustomFeedFilter</name>

   </types>

   <version>66.0</version>

</Package>

```


### Metadata Types CustomFieldDisplay

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomFieldDisplay

Represents the view type assigned to product attribute custom fields. This type extends the Metadata metadata type and inherits its
`fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CustomFieldDisplay components have the suffix .customFieldDisplay .

Version

### CustomFieldDisplay components are available in API version 63.0 and later.

Fields

**Field Name** **Field Type** **Description**

Required. The view type of the product attribute custom fields. Values
are:

**•** `ColorSwatch`

**•** `Dropdown`

**•** `Pill`

```
displayType

```

### CustomFieldDisplayType

(enumeration of
type string)

`fieldApiName` string Required. The unique name of the product attribute, for example, color_c.

`isProtected` boolean Optional. An auto-generated value that doesn’t impact the behavior of
the metadata type. The default value is `false` .

`masterLabel` string Required. The primary label for this object.

Declarative Metadata Sample Definition

The following is an example of a CustomFieldDisplay component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomFieldDisplay xmlns="http://soap.sforce.com/2006/04/metadata">

 <masterLabel>cfd1</masterLabel>

 <fieldApiName>Color__c</fieldApiName>

```


### Metadata Types CustomHelpMenuSection

```
    <displayType>Pill</displayType>

    <isProtected>false</isProtected>

   </CustomFieldDisplay>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

    <members>*</members>

    <name>CustomFieldDisplay</name>

    </types>

    <version>63.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomHelpMenuSection

Represents the section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources for
the org. The custom section contains help resources added by the admin. This type extends the Metadata metadata type and inherits
its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CustomHelpMenuSection components have the suffix .customHelpMenuSection and are stored in the

`customHelpMenuSections` folder.

Version

### CustomHelpMenuSection components are available in API version 45.0 and later.

Fields

**Field Name** **Field Type** **Description**

`customHelpMenuItems` CustomHelpMenuItems[] Items included in the custom section. Specify up to 15 items.

`masterLabel` string

Required. Name of the custom section. Only one custom section
can be added to the Lightning Experience help menu. Specify up
to 80 characters.


### Metadata Types CustomIndex

CustomHelpMenuItems

Items included in the custom section. Specify up to 15 items.

**Field Name** **Field Type** **Description**

`linkURL` string Required. The URL for the resource.

`masterLabel` string Required. The name of the resource. Specify up to 100 characters.

`sortOrder` int Required. The order of the item within the custom section. Valid values are `1`
through `15` .

Declarative Metadata Sample Definition

The following is an example of a CustomHelpMenuSection component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomHelpMenuSection xmlns="http://soap.sforce.com/2006/04/metadata">

      <masterLabel>MyOrgCustomHelp</masterLabel>

      <customHelpMenuItems>

        <linkUrl>https://www.yourcompanyhelp.com/gettingstarted</linkUrl>

        <masterLabel>Getting Started</masterLabel>

        <sortOrder>1</sortOrder>

      </customHelpMenuItems>

      <customHelpMenuItems>

        <linkUrl>https://www.yourcompanyhelp.com/features</linkUrl>

        <masterLabel>Feature to Start Using Right Away</masterLabel>

        <sortOrder>2</sortOrder>

      </customHelpMenuItems>

      <customHelpMenuItems>

        <linkUrl>https://www.yourcompanyhelp.com/salestips</linkUrl>

        <masterLabel>Tips for Sales Team Members</masterLabel>

        <sortOrder>3</sortOrder>

      </customHelpMenuItems>

   </CustomHelpMenuSection>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyOrgCustomHelp</members>

        <name>CustomHelpMenuSection</name>

      </types>

      <version>45.0</version>

   </Package>

### CustomIndex

```

Represents an index used to increase the speed of queries.This type extends the Metadata metadata type and inherits its `fullName`
field.


### Metadata Types CustomLabels

File Suffix and Directory Location

CustomIndex components have the suffix .indx-meta and are stored in the `customindex` folder.

Version

CustomIndex is available in API versions 50.0 and later.

Special Access Rules

[To use this metadata and create a custom index, review Indexes in](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_large_data_volumes_bp.meta/salesforce_large_data_volumes_bp/ldv_deployments_infrastructure_indexes.htm) _Best Practices for Deployments with Large Data Volumes_, and then
contact Salesforce Customer Support.

Fields

**Field Name** **Field Type** **Description**

`allowNullValues` boolean Indicates whether null values are allowed in the index ( `true` ) or not
( `false` ). The default value is `false` .

`booleanIndexedValue` boolean Indicates whether boolean fields are indexed (true) or not (false).
Available in API version 61.0 and later.

Declarative Metadata Sample Definition

The following is an example of a CustomIndex component.

```
   <?xml version="1.0" encoding="UTF-8" ?>

   <CustomIndex xmlns="http://soap.sforce.com/2006/04/metadata">

      <allowNullValues>false</allowNullValues>

      <booleanIndexedValue>true</booleanIndexedValue>

   </CustomIndex>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomLabels

The CustomLabels metadata type allows you to create custom labels that can be localized for use in different languages, countries, and
currencies.

This type extends the Metadata metadata type and inherits its `fullName` field. Custom labels are custom text values, up to 1,000
characters in length that can be accessed from Apex classes or Visualforce pages. For more information, see “Custom Labels” in Salesforce
Help.


Metadata Types CustomLabels

Declarative Metadata File Suffix and Directory Location

Master custom label values are stored in the `CustomLabels.labels` file. Translations for custom labels can be retrieved through
Translations in Metadata API. Translations are stored in files under the `translations` folder with the name format of
_`localeCode`_ `.translation`, where _`localeCode`_ is the locale code of the translation language. The supported locale codes
are listed in Language on page 2390.

Version

CustomLabels components are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`fullName` string

Required. The name of the custom label bundle.

Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating, updating,

or deleting. See `createMetadata()` to see an example of
this field specified for a call.

`labels` CustomLabel[] A list of custom labels.

CustomLabel

This metadata type represents a custom label. This type extends the Metadata metadata type and inherits its `fullName` field.

**Field** **Field Type** **Description**

`categories` string

`fullName` string

A comma-separated list of categories for the label. This field can
be used in filter criteria when creating custom label list views.
Maximum of 255 characters.

Required. The name of the custom label.

Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating, updating,

or deleting. See `createMetadata()` to see an example of
this field specified for a call.

`language` string Required. The language of the translated custom label.

`protected` boolean

Required. Indicates whether this component is protected ( `true` )
or not ( `false` ). Protected components can’t be linked to or
referenced by components created in the installing organization.

`shortDescription` string Required. An easily recognizable term to identify this custom
label. This description is used in merge fields.


Metadata Types CustomLabels

**Field** **Field Type** **Description**

`value` string Required. The translated custom label. Maximum of 1000
characters.

Usage

Use CustomLabels with the wildcard character (*) for members in the `package.xml` manifest file to retrieve all custom labels that
are defined in your organization. CustomLabels doesn’t support retrieving one or more custom labels by name. To retrieve specific labels
by name, use CustomLabel and specify the label names as members.

Declarative Metadata Sample Definition

This is a sample XML definition of a custom label component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomLabels xmlns="http://soap.sforce.com/2006/04/metadata">

      <labels>

        <fullName>quoteManual</fullName>

        <value>This is a manual quote.</value>

        <language>en_US</language>

        <protected>false</protected>

        <shortDescription>Manual Quote</shortDescription>

      </labels>

      <labels>

        <fullName>quoteAuto</fullName>

        <value>This is an automatically generated quote.</value>

        <language>en_US</language>

        <protected>false</protected>

        <shortDescription>Automatic Quote</shortDescription>

      </labels>

   </CustomLabels>

```

This is a sample manifest file for retrieving all custom labels in the organization by using the CustomLabels type.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>MyPkg</fullName>

      <types>

       <members>*</members>

       <name>CustomLabels</name>

      </types>

      <version>66.0</version>

   </Package>

```

This is a sample manifest file for retrieving two custom labels by name. Notice it uses the CustomLabel singular type.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>MyPkg</fullName>

      <types>

       <members>quoteManual</members>

       <members>quoteAuto</members>

```


### Metadata Types Custom Metadata Types (CustomObject)

```
       <name>CustomLabel</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

CustomLabels Limitation

Before you use the CustomLabels metadata type, understand the limitations of this feature. You can’t retrieve the CustomLabels metadata
type with a namespace.

SEE ALSO:

Translations

### Custom Metadata Types (CustomObject)

Represents the metadata associated with a custom metadata type.

[For more information, see Custom Metadata Types.](https://help.salesforce.com/s/articleView?id=platform.custommetadatatypes_overview.htm&language=en_US)

File Suffix and Directory Location

A custom metadata type is defined as a custom object and is stored in the objects folder. Custom metadata types have a suffix of `__mdt`
(instead of `__c` for custom objects). Custom metadata type field names have a suffix of `__c`, like other custom fields. Custom metadata
type field names must be dot-qualified with the name of the custom metadata type to which they belong.

Names of custom metadata types must be unique within their namespace. All custom metadata types belong to the `CustomMetadata`
namespace and can optionally belong to a second namespace. In your organization, you can use custom metadata types with your
namespace and also other organizations’ namespaces.

Version

Custom metadata type components are available in API version 31.0 and later.

Special Access Rules

To create custom metadata types, you must have the “Author Apex” permission. Apex code can create, read, and update (but not delete)
custom metadata records, as long as the metadata is subscriber-controlled and visible from within the code's namespace. You can edit
records in memory but not upsert or delete them. Apex code can deploy custom metadata records, but not via a DML operation.
Moreover, DML operations aren’t allowed on custom metadata in the Partner or Enterprise APIs. Customers who install a managed
custom metadata type can’t add new custom fields to it. With unpackaged metadata, both developer-controlled and subscriber-controlled
[access behave the same: like subscriber-controlled access. Refer to Trust, but Verify: Apex Metadata API and Security to learn more.](https://developer.salesforce.com/blogs/engineering/2017/06/apex-metadata-api-security.html)


Metadata Types Custom Metadata Types (CustomObject)

Note: Audit fields ( `CreatedDate`, `CreatedBy`, `LastModifiedDate`, `LastModifiedBy`, `SystemModStamp` )
remain uneditable.

Fields

Custom metadata types can contain the following CustomObject fields.

To make the fields on your custom metadata types unique and indexable, mark your fields as `Unique` and `ExternalId` .


Metadata Types Custom Metadata Types (CustomObject)

Declarative Metadata Sample Definition

In this example, Picklists R Us creates its Reusable Picklist custom metadata type by deploying a file in the objects folder, named
`ReusablePicklistOption__mdt.object`, with these contents.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

     <fields>

       <fullName>AlphaSort__c</fullName>

       <defaultValue>false</defaultValue>

       <externalId>false</externalId>

       <label>Sorted Alphabetically</label>

       <type>Checkbox</type>

     </fields>

     <label>Reusable Picklist</label>

     <pluralLabel>Reusable Picklist</pluralLabel>

     <visibility>Public</visibility>

   </CustomObject>

```

This excerpt from a `package.xml` file shows the use of dot notation and the `__mdt` suffix. If you’re using a namespace, for example
`picklist1234`, the full name of `ReusablePicklistOption__mdt` would be `picklist1234`
`__ReusablePicklistOption__mdt` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

   ...

     <types>

       <members>PicklistTest__c.PicklistTestField__c</members>

       <members>ReusablePicklistOption__mdt.Picklist__c</members>

       <members>ReusablePicklistOption__mdt.SortOrder__c</members>

       <members>PicklistUsage__mdt.Field__c</members>

       <members>PicklistUsage__mdt.Picklist__c</members>

       <members>PicklistUsage__mdt.SObjectType__c</members>

       <members>ReusablePicklist__mdt.AlphaSort__c</members>

       <name>CustomField</name>

     </types>

   ...

     <types>

       <members>PicklistTest__c</members>

       <members>ReusablePicklistOption__mdt</members>

       <members>PicklistUsage__mdt</members>

       <members>ReusablePicklist__mdt</members>

       <name>CustomObject</name>

     </types>

   ...

     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types CustomMetadata 1. CustomMetadata

Represents a record of a custom metadata type.

#### CustomMetadata

Represents a record of a custom metadata type.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### CustomMetadata components have the suffix .md and are stored in the customMetadata folder. Unlike custom metadata types,

custom metadata records don’t have a double-underscore suffix. Custom metadata record names are prepended with their custom
metadata type name, excluding the `__mdt` suffix but including the namespace of any types in an installed managed package.

Version

#### CustomMetadata components are available in API version 31.0 and later.

Special Access Rules

To create custom metadata records, you must have the “Customize Application” permission.

Fields

**Field Name** **Field Type** **Description**

`description` string A description of the custom metadata record. This field
can contain a maximum of 1,000 characters.

`label` string A label that represents the object throughout the
Salesforce Setup user interface. Custom metadata records

are currently visible only through the packaging user
interface.

`protected` boolean

Boolean. Indicates whether the record is protected (true)
or not (false). When a custom metadata type is released
in a managed package, access is limited in specific ways.

**•** Code that’s in the same managed package as custom
metadata records can read the records.

**•** Code that’s in the same managed package as custom
metadata types can read the records that belong to
that type.

**•** Code that’s in a managed package that doesn’t
contain either the type or the protected record can’t
read the protected records.


Metadata Types CustomMetadata

**Field Name** **Field Type** **Description**

**•** Code that the subscriber creates and code that’s in
an unmanaged package can’t read the protected
records.

**•** The developer can modify protected records with a
package upgrade or by using the Metadata Apex
classes (if the Apex code is in the same namespace
as either the records or their type). The subscriber
can’t read or modify protected records. The developer
name of a protected record can’t be changed after
release.

**•** The subscriber can’t create records of a protected
type.

Records that are hidden by these access rules are also
unavailable to REST, SOAP, SOQL, and Setup.

`values` CustomMetadataValue[] Represents one or more values for custom fields on the
custom metadata record.

CustomMetadataValue

Represents a value for a custom field on the custom metadata record.

**Field Name** **Field Type** **Description**

`field` string Required. The non-object-qualified name of a custom
field in the custom metadata type. This value corresponds

to the name of a field on the custom metadata record’s
custom metadata type. Include the namespace (if the
type is from a managed package) and the `__c` suffix.
The name of the custom metadata type isn’t required.
For example, `picklist1234__AlphaSort__c` .

`value` Any type The value on a custom metadata record. Where fields are
EntityDefinition and FieldDefinition, the qualified API

names of the entity and the field it points to. This value
can be null.

Declarative Metadata Sample Definitions

The following is an example of a CustomMetadata component. In this example, the sample app TravelApp deploys a Planets picklist,
specifies its sort order, and adds picklist items to it.


Metadata Types CustomMetadata

Assuming Picklists R Us’s namespace is `picklist1234`, to define the `Planets` picklist, TravelApp deploys a file in the
`customMetadata` folder, named `picklist1234__ReusablePicklist.Planets.md`, with these contents. The
`xsi:type` attribute specifies the type for the value of the `AlphaSort__c` checkbox field.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata"

               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

               xmlns:xsd="http://www.w3.org/2001/XMLSchema">

      <description>All the planets in the solar system. Does not

              include asteroids.</description>

      <label>Planets</label>

      <values>

        <field>picklist1234__AlphaSort__c</field>

        <value xsi:type="xsd:boolean">false</value>

      </values>

   </CustomMetadata>

```

Picklists R Us creates its Reusable Picklist Option custom metadata type by deploying a file in the objects folder, named
`ReusablePicklist__mdt.object`, with these contents.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <fields>

        <fullName>Picklist__c</fullName>

        <externalId>false</externalId>

        <label>Picklist</label>

        <length>40</length>

        <required>true</required>

        <type>Text</type>

        <unique>false</unique>

      </fields>

      <fields>

        <fullName>SortOrder__c</fullName>

        <externalId>false</externalId>

        <label>Non-Alphabetical Sort Order</label>

        <precision>3</precision>

        <scale>0</scale>

        <required>false</required>

        <type>Number</type>

        <unique>false</unique>

      </fields>

      <label>Reusable Picklist Option</label>

      <pluralLabel>Reusable Picklist Options</pluralLabel>

   </CustomObject>

```

To define the `Mars` picklist item, TravelApp deploys a file, named `picklist1234__ReusablePicklistOption.Mars.md`,
with these contents. This component file specifies types that apply to the `ReusablePicklistOption__mdt` custom fields.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata"

     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

     xmlns:xsd="http://www.w3.org/2001/XMLSchema">

      <label>Mars</label>

      <values>

        <field>picklist1234__Picklist__c</field>

```


Metadata Types CustomMetadata

```
        <value xsi:type="xsd:string">Planets</value>

      </values>

      <values>

        <field>picklist1234__SortOrder__c</field>

        <value xsi:type="xsd:int">4</value>

      </values>

   </CustomMetadata>

```

To define the `Motel6` picklist item, TravelApp deploys a file, named
`picklist1234__ReusablePicklistOption.Motel6.md`, with these contents.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata"

     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

     xmlns:xsd="http://www.w3.org/2001/XMLSchema">

      <label>Motel 6</label>

      <values>

        <field>picklist1234__Picklist__c</field>

        <value xsi:type="xsd:string">Hotels</value>

      </values>

   </CustomMetadata>

```

Because the `SortOrder__c` field isn’t required, this file doesn’t require a value for `SortOrder__c` . Alternatively, the file could
have explicitly specified a value with `xsi:nil` to ensure that `SortOrder__c` was cleared of any previous value.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

   xmlns:xsd="http://www.w3.org/2001/XMLSchema">

      <label>Motel 6</label>

      <values>

        <field>picklist1234__Picklist__c</field>

        <value xsi:type="xsd:string">Hotels</value>

      </values>

      <values>

        <field>picklist1234__SortOrder__c</field>

        <value xsi:nil="true" />

      </values>

   </CustomMetadata>

```

This excerpt from a `package.xml` file illustrates the inclusion of custom metadata types and their namespaces in custom metadata
records’ names. Assume that Picklists R Us’s namespace is `picklist1234` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <package xmlns="http://soap.sforce.com/2006/04/metadata">

   …

     <types>

       <members>picklist1234__ReusablePicklist.Hotels</members>

       <members>picklist1234__ReusablePicklist.Planets</members>

       <members>picklist1234__ReusablePicklistOption.Bellagio</members>

       <members>picklist1234__ReusablePicklistOption.Motel6</members>

       <members>picklist1234__ReusablePicklistOption.Mercury</members>

       <members>picklist1234__ReusablePicklistOption.Venus</members>

       <members>picklist1234__ReusablePicklistOption.Earth</members>

       <members>picklist1234__PicklistUsage.BookedHotel</members>

```


Metadata Types CustomMetadata

```
       <members>

         picklist1234__PicklistUsage.DestinationPlanetPL

       </members>

       <members>picklist1234__PicklistUsage.PlanetVisitedPl</members>

       <name>CustomMetadata</name>

     </types>

   …

   </package>

```

TravelApp, Inc.’s `package.xml` file uses a wildcard to install custom metadata, as is shown in this excerpt from their `package.xml`
file. Unless you want to deploy or retrieve specific records, using a wildcard is easier than listing all of your custom metadata records in
your `package.xml` file.

```
   <types>

     <members>*</members>

     <name>CustomMetadata</name>

   </types>

```

If the custom metadata is from a managed package, the name after the dot in the `package.xml` file—between the two dots in the
file name—is qualified by the managed package’s namespace. For example, assuming TravelApp uses the namespace `travelApp1234`,
the first member element in the TravelApp `package.xml` file appears to Galactic Tours as:

```
   <members>picklist1234__ReusablePicklist.travelApp1234__Hotels</members>

```

Here’s another example. In this case, we have an instance of custom metadata record, whose EntityDefinition field points to a custom
object named `SalesAgreement__c` . The FieldDefinition field points to the custom field `CustomerReference__c` on
`SalesAgreement__c` . You can deploy new custom metadata records and retrieve existing ones with EntityDefinition and
FieldDefinition fields using qualified API names of custom and standard entities and their fields.

```
   <?xml version="1.0" encoding="UTF-8"?><values>

   <field>EntityDefintionField__c</field>

   <value xsi:type="xsd:string">v1__SalesAgreement__c</value>

   </values>

   <values>

   <field>FieldDefinitionField__c</field>

   <value xsi:type="xsd:string">v1__CustomerReference__c</value>

   </values>

```

Usage

When specifying the `value` field in the CustomMetadataValue subtype, specify an appropriately typed object that’s based on your
field type definition. In declarative metadata definitions for CustomMetadataValue, use the `xsi:type` attribute of the value element.
For example, to specify a boolean value: `<value` `xsi:type="xsd:boolean">true</value>` . Valid `xsi:type` attributes
are:

**Custom metadata value** **Custom field definition**

`xsi:type="xsd:boolean"` Checkbox

`xsi:type="xsd:date"` Date

`xsi:type="xsd:dateTime"` Date/Time

`xsi:type="xsd:picklist"` Picklist


### Metadata Types CustomNotificationType

**Custom metadata value** **Custom field definition**

`xsi:type="xsd:string"` Text

`xsi:type="xsd:string"` Phone

`xsi:type="xsd:string"` TextArea

`xsi:type="xsd:string"` URL

`xsi:type="xsd:string"` Email

`xsi:type="xsd:int"` Number/Percent, with scale equal to 0

`xsi:type="xsd:double"` Number/Percent, with scale not equal to 0

You can also omit the `xsi:type` attribute. For example, `<value>true</value>` .

Although this attribute must be specified for any CustomMetadataValue, you can use an element with the `xsi:nil` attribute set to
`true` to explicitly set the field’s value to `null` . For example, `<value` `xsi:nil="true"/>` .

Using `null` field values differs from leaving out the CustomMetadataValue for a particular field entirely. If you leave out the
CustomMetadataValue, the value of the field doesn’t change. The field’s value is `null` for newly deployed custom metadata records
and left at its previous value for updated custom metadata records.

When you retrieve CustomMetadataValue objects, the `value` field of the returned object holds a value of the correct type, specified
by `xsi:type` in the case of declarative metadata definitions.

Custom number fields are stored as double values. When you retrieve a value from a Number type field with a scale 0, you will see a
decimal number. For example, if the value in UI is 1234567, a query through the API returns 1234567.0.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomNotificationType

Represents the metadata associated with a custom notification type.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

For more information about custom notifications, see Custom Notification Actions. This type extends the Metadata metadata type and
inherits its `fullName` field.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.notiftype` for the notification type definition. Notification types are stored in the `notificationtypes`
directory of the corresponding package directory.


Metadata Types CustomNotificationType

Version

CustomNotificationType components are available in API version 46.0 and later.

Fields

**Field Name** **Field Type** **Description**

`actionGroups` CustomNotificationActionGroup[]

```
(Beta)

```

Optional. Indicates whether mobile action groups are enabled, allowing
users to take actions directly from mobile notifications.

`actionGroups` is a pilot or beta service that is subject to the Beta
[Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)

[Agreement if executed by Customer, and applicable terms in the Product](https://ptd.salesforce.com/)
[Terms Directory. Use of this pilot or beta service is at the Customer's sole](https://ptd.salesforce.com/)
discretion.

`customNotifTypeName` string Required. Specifies a notification type name. Maximum number of
characters: 80.

`description` string Specifies a general description of the notification type, which is displayed
with the notification type name. Maximum number of characters: 255.

`desktop` boolean Required. Indicates whether the desktop delivery channel is enabled
( `true` ) or not ( `false` ).

`masterLabel` string Required. Specifies the label for the notification type.

`mobile` boolean Required. Indicates whether the mobile delivery channel is enabled
( `true` ) or not ( `false` ).

`slack` boolean Reserved for future use.

CustomNotificationActionGroup (Beta)

CustomNotificationActionGroup represents the action group.

`CustomNotificationActionGroup` [is a pilot or beta service that is subject to the Beta Services Terms at Agreements -](https://www.salesforce.com/company/legal/agreements/)
[Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use](https://www.salesforce.com/company/legal/agreements/)
of this pilot or beta service is at the Customer's sole discretion.

**Field Name** **Description**

```
actions

groupName

```

**Field Type**

CustomNotificationActionDefinition[]

**Description**
Represents the actions within a mobile action group.

**Field Type**
string


Metadata Types CustomNotificationType

**Field Name** **Description**

**Description**

Required.

Unique name of the mobile action group.

CustomNotificationActionDefinition

CustomNotificationActionDefinition represents the metadata that define an actionable notification.

`CustomNotificationActionDefinition` [is a pilot or beta service that is subject to the Beta Services Terms at Agreements](https://www.salesforce.com/company/legal/agreements/)

[- Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory.](https://www.salesforce.com/company/legal/agreements/)
Use of this pilot or beta service is at the Customer's sole discretion.

**Field Name** **Description**

```
actionLabel

actionName

actionTarget

actionType

```

**Field Type**
string

**Description**

Required.

The name of the action seen in the push notification.

**Field Type**
string

**Description**

Required.

Unique identifier of the action in an action group.

**Field Type**
string

**Description**
The name of the Apex class where the action is implemented.

**Field Type**
NotificationActionType (enumeration of type string)

**Description**

Type of action.

Required.

Values are:

**•** `NotificationApiAction` : Server-side action where client needs to make
action API call.


### Metadata Types CustomObject

**Field Name** **Description**

**•** `Share` : Client-side action where the app shares notification content to any
channel.

Declarative Metadata Sample Definition

The following is a definition of a custom notification type that is enabled for desktop and mobile.

```
   <CustomNotificationType xmlns="http://soap.sforce.com/2006/04/metadata">

      <customNotifTypeName>Custom Notification</customNotifTypeName>

      <desktop>true</desktop>

      <masterLabel>Custom Notification</masterLabel>

      <mobile>true</mobile>

   </CustomNotificationType>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomObject

Represents a custom object that stores data unique to your org or an external object that maps to data stored outside your org.

This type extends the Metadata metadata type and inherits its `fullName` field.

Specify all relevant fields when you create or update a custom object. You can’t update a single field on the object. For more information
[about custom objects, see Store Information That’s Unique to Your Organization in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.dev_object_def.htm&type=5&language=en_US)

You can also use this metadata type to work with customizations of standard objects, such as accounts. For an example, see the section
[on Standard Objects in Sample package.xml Manifest Files in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/manifest_samples.htm) _Metadata API Developer Guide_

All metadata components have a `fullName` field, which must be fully specified for any custom object.

For example, the following are fully specified names for a standard object and a custom object respectively:

```
   Account

   MyCustomObject__c

```

And the following is a fully specified name for an external object:

```
   MyExternalObject__x

```

For sample Java code that creates a custom object, see Step 3: Walk Through the Java Sample Code on page 16.

Declarative Metadata File Suffix and Directory Location

Custom object names are automatically appended with __c. The file suffix is `.object` for the custom object or standard object file.

External object names are automatically appended with __x. The file suffix is `.object` for the external object file.

Custom, standard, and external objects are stored in the `objects` folder in the corresponding package directory.


Metadata Types CustomObject

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Version

Custom objects are available in API version 10.0 and later. External objects are available in API version 32.0 and later.

Fields

Unless otherwise noted, all fields are creatable, filterable, and nillable.

**Field Name** **Field Type** **Description**

`actionOverrides` ActionOverride[]

`allowInChatterGroups` boolean

`businessProcesses` BusinessProcess[]

`compactLayoutAssignment` string

`compactLayouts` CompactLayout[]

`customHelp` string

`customHelpPage` string

`customSettingsType` CustomSettingsType
(enumeration of type string)


A list of action overrides on the object.

This field is available in API version 18.0 and later.

Indicates whether records of this custom object type can be
added to Chatter groups.

This field is available in API version 34.0 and later.

A list of business processes associated with the object.

This field is available in API version 17.0 and later.

The compact layout assigned to the object.

This field is available in API version 29.0 and later. This field is
available for external objects in API version 42.0 and later.

A list of compact layouts associated with the object.

This field is available in API version 29.0 and later. This field is
available for external objects in API version 42.0 and later.

The s-control that contains the help content if the object has
customized help content. This field is available in API version
14.0 and later.

The Visualforce page that contains the help content if the
object has customized help content. This field is available in
API version 16.0 and later.

When this field is present, this component isn’t a custom
object, but a custom setting. This field returns the type of
custom setting. The following string values are valid:

**•** `List` —static data stored in cache, accessed as part of
your application, and available org-wide.

**•** `Hierarchy` —static data stored in cache, accessed as
part of your application, and available based on a hierarchy
of user, profile, or org. This value is the default.

Metadata Types CustomObject

**Field Name** **Field Type** **Description**

This field is available in API version 17.0 and later.

`customSettingsVisibility` CustomSettingsVisibility
(enumeration of type string)

When this field is present, this component isn’t a custom
object, but a custom setting. This field returns the visibility of
the custom setting. The following string values are valid:

**•** `Public` —if the custom setting is packaged, it’s
accessible to all subscribing orgs.

**•** `Protected` —if the custom setting is in a managed
package, it’s accessible only to the developer org.
Subscribing orgs can’t access it. This value is the default.

This field is available in API versions 17.0 through 33.0. In
versions 34.0 and later, use the `visibility` field instead
of this field.

`dataStewardGroup` string Removed in API version 47.0.

`dataStewardUser` string Removed in API version 47.0.

`deploymentStatus` DeploymentStatus Indicates the deployment status of the object.
(enumeration of type string)

`deprecated` boolean Reserved for future use.

`description` string A description of the object. Maximum of 1000 characters.

`enableActivities` boolean

`enableBulkApi` boolean

`enableDivisions` boolean

Indicates whether the object is enabled for activities ( `true` )
or not ( `false` ).

Not available for external objects.

When enabled, the object is classified as an Enterprise
Application object for usage tracking.

When enabled, `enableSharing` and
`enableStreamingApi` must also be enabled.

This field is available in API version 31.0 and later.

Indicates whether the object is enabled for divisions ( `true` )
or not ( `false` [). See Division in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_division.htm) _Salesforce Object Reference_ .
.

`enableEnhancedLookup` boolean Indicates whether the object is enabled for enhanced lookups
( `true` ) or not ( `false` ). The custom object must be

searchable for `enableEnhancedLookup` to work. Set
`enableSearch` as `true` before setting
`enableEnhancedLookup` as `true` . In API version 28.0
and later, this field can also be used for the Account, Contact,
and User objects. Enhanced lookups provide an updated
lookup dialog interface that lets users filter, sort, and page
through search results and customize search result columns.


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

For more information about enhanced lookups, see “Enable
Enhanced Lookups” in Salesforce Help.

`enableFeeds` boolean

Indicates whether the object is enabled for feed tracking
( `true` ) or not ( `false` ). For more information, see “Customize
Chatter Feed Tracking” in Salesforce Help.

This field is available in API version 18.0 and later.

`enableHistory` boolean Indicates whether the object is enabled for history tracking
( `true` ) or not ( `false` ). Also available for standard objects

in API version 29.0 and later. History tracking on the Account
object includes person account history tracking.

`enableLicensing` boolean

`enableReports` boolean

`enableSearch` boolean

`enableSharing` boolean

Indicates whether this object is licensed by Salesforce and
users require a permission set license for it ( `true` ) or not
( `false` ). This field is available in API version 45.0 and later.

Indicates whether the object is enabled for reports ( `true` )
or not ( `false` ). Support for external objects is available in
API version 38.0 and later.

Indicates whether the object’s records can be found via SOSL
and Salesforce searches. Corresponds to `Allow Search`
in the user interface.

By default, search is disabled for new custom objects. This
field is available for custom objects in API version 35.0 and
later.

To enhance Einstein Search performance, searchability is
disabled for custom objects that haven't been searched for
more than 120 days. To enable object and field searchability,
contact your admin.

By default, search is disabled for new external objects.
However, you can validate and sync an external data source
to automatically create external objects. Syncing always
enables search on the external object when search is enabled
on the external data source, and vice versa.This field is
available for external objects in API version 37.0 and later.

When enabled, the object is classified as an Enterprise
Application object for usage tracking.

When enabled, `enableBulkApi` and
`enableStreamingApi` must also be enabled.

This field is available in API version 31.0 and later.


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

`enableStreamingApi` boolean

When enabled, the object is classified as an Enterprise
Application object for usage tracking.

When enabled, `enableBulkApi` and `enableSharing`
must also be enabled.

This field is available in API version 31.0 and later.

`eventType` PlatformEventType This field applies only to platform events. Indicates the event
(enumeration of type string) type. The values are:

**•** `HighVolume` —For a high-volume platform event.

**•** `StandardVolume` —Deprecated. Creating a platform
event with this event type is supported and returns an
error.

This field is available in API version 41.0 and later.

`externalDataSource` string Required and available for external objects only. The name of
the external data source that stores the data for the external

object. The data source is represented by the
ExternalDataSource component.

This field is available in API version 32.0 and later.

`externalName` string

`externalRepository` string

`externalSharingModel` SharingModel (enumeration
of type string)

Required and available for external objects only. The name of
the table in the external data source that contains the data
for the external object.

This field is available in API version 32.0 and later.

Available for Salesforce Connect external objects only.
Corresponds to `Display URL Reference Field`
in the user interface.

The external object’s `Display URL` standard field values
are automatically generated from the external system. For

example, with the OData 2.0 adapter for Salesforce Connect,
the value is based on the `link href` that’s defined on the
OData producer. You can override the default values with the
values of a custom field on the same external object. Select
the field name, and make sure that the custom field’s values
are valid URLs.

This field is available in API version 32.0 and later.

Indicates the external org-wide defaults for the object, which
determines the access level for external users.

This field is available in API version 31.0 and later.

`fields` CustomField[] Represents one or more fields in the object.


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

`fieldSets` FieldSet Defines the field set that exists on this object.

`fullName` string Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see an
example of this field specified for a call.

This value can't be `null` .

`gender` Gender

Indicates the gender of the noun that represents the object.
This is used for languages where words need different
treatment depending on their gender.

`household` boolean This field supports relationship groups, a feature available only
with Salesforce for Wealth Management. For more

information, see “Salesforce for Wealth Management” in
Salesforce Help.

`historyRetentionPolicy` HistoryRetentionPolicy Reserved for future use.

`indexes` Index[] Defines the index for a custom big object.

`label` string

Label that represents the object throughout the Salesforce
user interface.

We recommend that you make object labels unique across
all standard, custom, and external objects in the org.

`listViews` ListView[] Represents one or more _list views_ associated with the object.

`namedFilter` NamedFilter[] Represents the metadata associated with a lookup filter. This
metadata type is used to create, update, or delete lookup filter

definitions. This component has been removed as of API
version 30.0 and is only available in previous API versions. The
metadata associated with a lookup filter is now represented
by the lookupFilter field in the CustomField component.

This field is available in API version 17.0 and later.

This field has been removed as of API version 30.0 and is only
available in prior versions. The metadata associated with a
lookup filter is now represented by the lookupFilter field in
the CustomField component.

`nameField` CustomField

Required for custom objects. On external objects, the name
field can instead be specified by setting `isNameField` to
`true` in the CustomField component.

The field that this object's name is stored in. Every custom
object must have a name, usually a string or autonumber.

Identifier for the custom object record. This name appears in
page layouts, related lists, lookup dialogs, search results, and


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

key lists on tab home pages. By default, this field is added to
the custom object page layout as a required field.

`pluralLabel` string

Plural version of the label value.

Custom objects require a plural version of the label to ensure
that object names are localizable.

`profileSearchLayouts` ProfileSearchLayouts Represents a user profile’s search results layouts for an object.
With profile-specific layouts, each user profile can have a

different search results layout for an object. Available in API
version 47.0 and later.

`publishBehavior` PlatformEventPublishBehavior This field applies only to platform events. Indicates when
(enumeration of type string) platform event messages are published in a Lightning Platform

transaction. This field applies to event messages published
through the Lightning Platform, such as Apex, Process Builder,
and Flow Builder, but not through Salesforce APIs. Valid values
are:

**•** `PublishAfterCommit` —The event message is
published only after a transaction commits successfully.
If the transaction fails, the event message isn't published.

**•** `PublishImmediately` —The event message is
published when the publish call executes, regardless of
whether the transaction succeeds.

If you don’t specify this field, the default value used is
`PublishImmediately` .

This field is available in API version 46.0 and later.

`recordTypes` RecordType[] An array of one or more record types defined for this object.

`recordTypeTrackFeedHistory` boolean Indicates whether the record type is enabled for feed tracking
( `true` ) or not ( `false` ). To set this field to `true`, the

`enableFeeds` field on the associated CustomObject must
also be `true` . For more information, see “Customize Chatter
Feed Tracking” in Salesforce Help.

This field is available in API version 19.0 and later.

`recordTypeTrackHistory` boolean Indicates whether history tracking is enabled for this record
type ( `true` ) or not ( `false` ). To set

`recordTypeTrackHistory` to true, the
`enableHistory` field on the associated custom object
must also be `true` .

This field is available in API version 19.0 and later.

`searchLayouts` SearchLayouts The _Search Layouts_ related list information for the object.


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

`sharingModel` SharingModel(enumeration Indicates the org-wide defaults for the object.
of type string)

Note: Using API version 29.0 and earlier, this field is
read-only and can’t be set using the Metadata API; you
must use the Salesforce user interface. Using API
version 30.0 and later, you can set this field for internal
users using the API and the Salesforce user interface.

`sharingReasons` SharingReason[] The reasons why the object is being shared.

`sharingRecalculations` SharingRecalculation[] A list of custom sharing recalculations associated with the
object.

`startsWith` StartsWith (enumeration of Indicates whether the noun starts with a vowel, consonant,
type string) or is a special character. This is used for languages where

words need different treatment depending on the first
character. Valid values are listed in StartsWith.

`validationRules` ValidationRule[] An array of one or more validation rules on the object.

`visibility` SetupObjectVisibility
(enumeration of type string)

This field returns the visibility of the custom object, custom
setting, or custom metadata type. The following values are
valid.

**•** `Public` —If the custom object, custom setting, or
custom metadata type is packaged, it’s accessible to all
subscribing orgs.

**•** `Protected` —If the custom object, custom setting, or
custom metadata type is in a managed package, it’s
accessible only to the developer org. Subscribing orgs
can’t access it.

**•** `PackageProtected` - (Custom metadata type only)
If the custom metadata type is `PackageProtected`,
it’s only accessible by the custom Apex code in the
package. Use this value to secure secrets such as API
access keys and security tokens. Available in API version
47.0 and later.

The default value is `Public` .

This field is available in API version 34.0 and later. For custom
settings, this field replaces the
`customSettingsVisibility` field.

`webLinks` WebLink[] An array of one or more weblinks defined for the object.

MktDataModelAttributes

This type is a Data 360 subtype of CustomObject.


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

`creationType` DefinitionCreationType
enumeration

Indicates how this object is added.

Valid values availble in API version 62.0 and later are:

**•** `Activation_Audience`

**•** `Ad_Audience_Insights`

**•** `ADG`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Directory_Table`

**•** `External`

**•** `Problem_Records`

**•** `Segment_Membership`

**•** `Semantic`

**•** `Transform`

**•** `Vector_Embedding`

`dataModelTaxonomy` string When the model is a Standard Data 360 model, a Reference to the Data Model
from which this Object was started. Currently only supports the following

strings: if the creationType is Standard, it must be Reference, if creationType is
Custom, it must be View.

`description` string A description of the object. This field can contain a maximum of 521 characters.
This field is available in API version 55.0 and later.

`isEnabled` boolean True indicates that the Data Model Object is enabled.

`isSegmentable` boolean True indicates that the Data Model Object can be used as a target for
segmentation.

`isUsedForMetrics` boolean Indicates whether the Data Model Object is used for metrics ( `true` ) or not
( `false` ). This field is used to include additional attributes on the objects that

are not present in the Data Model Object POJO. This field is available in API
version 55.0 and later.

`objectCategory` string Reference to the Object Category. For modeling, the value is Profile,
Engagement, or Other.

`referenceEntityGroup` string When this is a Standard Object, the Entity Group of the Object from the
Reference Model.

`referenceEntityName` string When this is a Standard Object, the Name of the Object from the Reference
Model.

`referenceEntitySubjectArea` string When this is a Standard Object, the Subject Area of the Object from the
Reference Model.


Metadata Types CustomObject

MktDataLakeAttributes

Represents how Data 360 receives the data. MktDataLakeAttributes is a Data 360 subtype of CustomObject. Its components are available
in API version 50.0 and later.

Special Access Rules

You need an org with a Data Cloud license to access this object.

**Field Name** **Description**

```
creationType

isEnabled

```

**Field Type**
DefinitionCreationType enumeration of type string

**Description**
Indicates how this object is added.

Values are:

**•** `Activation_Audience`

**•** `Bridge`

**•** `Curated`

**•** `Custom`

**•** `Derived`

**•** `Ml_Prediction`

**•** `Segment_Membership`

**•** `Standard`

**•** `System`

Valid values availble in API version 62.0 and later are:

**•** `Activation_Audience`

**•** `Ad_Audience_Insights`

**•** `ADG`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Directory_Table`

**•** `External`

**•** `Problem_Records`

**•** `Segment_Membership`

**•** `Semantic`

**•** `Transform`

**•** `Vector_Embedding`

**Field Type**
boolean


Metadata Types CustomObject

**Field Name** **Description**

**Description**
Indicates whether the Landing Object is enabled.

```
objectCategory

```

**Field Type**
string

**Description**
Reference to the Object Category. For landing object, these would be Profile, Behavioral,
Other.

Declarative Metadata Additional Components

CustomObject definitions can include additional components defined in the custom object for declarative metadata. The following
components are defined in the CustomObject:

**•** ActionOverride

**•** BusinessProcess

**•** CompactLayout

**•** CustomField

**•** FieldSet

**•** HistoryRetentionPolicy

**•** ListView

**•** RecordType

**•** SearchLayouts

**•** SharingReason

**•** SharingRecalculation

**•** ValidationRule

**•** WebLink

Declarative Metadata Sample Definition

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   <deploymentStatus>Deployed</deploymentStatus>

   <description>test object with one field for eclipse ide testing</description>

   <fields>

     <fullName>Comments__c</fullName>

     <description>add your comments about this object here</description>

    <inlineHelpText>This field contains comments made about this object</inlineHelpText>

     <label>Comments</label>

     <length>32000</length>

     <type>LongTextArea</type>

     <visibleLines>30</visibleLines>

   </fields>

```


Metadata Types CustomObject

```
      <label>MyFirstObject</label>

      <nameField>

        <label>MyFirstObject Name</label>

        <type>Text</type>

      </nameField>

      <pluralLabel>MyFirstObjects</pluralLabel>

      <sharingModel>ReadWrite</sharingModel>

   </CustomObject>

```

The following is the metadata definition of an external object for Salesforce Connect.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>CancelEdit</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Delete</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Edit</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Follow</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>List</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>New</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>SaveEdit</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Tab</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>View</actionName>

        <type>Default</type>

      </actionOverrides>

      <deploymentStatus>InDevelopment</deploymentStatus>

      <description>Products</description>

      <enableFeeds>false</enableFeeds>

      <externalDataSource>OData</externalDataSource>

      <externalIndexAvailable>false</externalIndexAvailable>

      <externalName>Products</externalName>

```


Metadata Types CustomObject

```
      <fields>

        <fullName>DiscontinuedDate__c</fullName>

        <description>DiscontinuedDate</description>

        <externalDeveloperName>DiscontinuedDate</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>DiscontinuedDate</label>

        <required>false</required>

        <type>DateTime</type>

      </fields>

      <fields>

        <fullName>ID__c</fullName>

        <description>ID</description>

        <externalDeveloperName>ID</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>ID</label>

        <precision>18</precision>

        <required>false</required>

        <scale>0</scale>

        <type>Number</type>

        <unique>false</unique>

      </fields>

      <fields>

        <fullName>Name__c</fullName>

        <description>Name</description>

        <externalDeveloperName>Name</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>Name</label>

        <length>128</length>

        <required>false</required>

        <type>Text</type>

        <unique>false</unique>

      </fields>

      <fields>

        <fullName>Price__c</fullName>

        <description>Price</description>

        <externalDeveloperName>Price</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>Price</label>

        <precision>16</precision>

        <required>false</required>

        <scale>2</scale>

        <type>Number</type>

```


Metadata Types CustomObject

```
        <unique>false</unique>

      </fields>

      <fields>

        <fullName>Products__c</fullName>

        <externalDeveloperName>Products</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>Products</label>

        <length>20</length>

        <referenceTo>Products__x</referenceTo>

        <relationshipLabel>Products</relationshipLabel>

        <relationshipName>Products</relationshipName>

        <type>ExternalLookup</type>

      </fields>

      <fields>

        <fullName>Rating__c</fullName>

        <description>Rating</description>

        <externalDeveloperName>Rating</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>Rating</label>

        <precision>18</precision>

        <required>false</required>

        <scale>0</scale>

        <type>Number</type>

        <unique>false</unique>

      </fields>

      <fields>

        <fullName>ReleaseDate__c</fullName>

        <description>ReleaseDate</description>

        <externalDeveloperName>ReleaseDate</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>ReleaseDate</label>

        <required>false</required>

        <type>DateTime</type>

      </fields>

      <label>Products</label>

      <pluralLabel>Products</pluralLabel>

      <searchLayouts>

        <customTabListAdditionalFields>ExternalId</customTabListAdditionalFields>

        <lookupDialogsAdditionalFields>ExternalId</lookupDialogsAdditionalFields>

       <lookupPhoneDialogsAdditionalFields>ExternalId</lookupPhoneDialogsAdditionalFields>

        <searchResultsAdditionalFields>ExternalId</searchResultsAdditionalFields>

        <searchResultsAdditionalFields>DisplayUrl</searchResultsAdditionalFields>

        <searchResultsAdditionalFields>ID__c</searchResultsAdditionalFields>

```


Metadata Types CustomObject

```
      </searchLayouts>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file for Field Sets and Record Types
but not for other components. For information about using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

1. ActionOverride
Represents an action override on a standard or custom object. Use it to create, update, edit, or delete action overrides.You can access
ActionOverride only by accessing its encompassing CustomObject.

2. BusinessProcess
The BusinessProcess metadata type enables you to display different picklist values for users based on their profile.

3. CompactLayout
Represents the metadata associated with a compact layout. This type extends the Metadata metadata type and inherits its `fullName`
field.

4. CustomField
Represents the metadata associated with a field. Use this metadata type to create, update, or delete custom field definitions on
standard, custom, and external objects or standard field definitions on standard objects.

5. FieldSet
Represents a field set. A field set is a grouping of fields. For example, you could have a field set that contains fields describing a user's
first name, middle name, last name, and business title.

6. HistoryRetentionPolicy
Represents the policy for archiving field history data. When you set a policy, you specify the number of months that you want to
keep field history in Salesforce before archiving it. By default, when Field Audit Trail is enabled, all field history is retained.

7. Index
[Represents an index defined within a custom big object. Use this metadata type to define the composite primary key (index) for a](https://developer.salesforce.com/docs/atlas.en-us.260.0.bigobjects.meta/bigobjects/big_object.htm)
custom big object. This type extends the Metadata metadata type and inherits its `fullName` field.

8. ListView
ListView allows you to see a filtered list of records, such as contacts, accounts, or custom objects.

9. NamedFilter
Represents the metadata associated with a lookup filter. This metadata type is used to create, update, or delete lookup filter definitions.
This component has been removed as of API version 30.0 and is only available in previous API versions. The metadata associated
with a lookup filter is now represented by the lookupFilter field in the CustomField component.

10. Picklist (Including Dependent Picklist)

Deprecated. Represents a picklist (or dependent picklist) definition for a custom field in a custom object or a custom or standard
field in a standard object, such as an account.

11. ProfileSearchLayouts

Represents a user profile’s search results layouts for an object. `ProfileSearchLayouts` are similar to `SearchLayouts` .
However, with profile-specific layouts, each user profile can have a different search results layout for an object.

12. RecordType

Represents the metadata associated with a record type. Record types let you offer different business processes, picklist values, and
page layouts to different users. Use this metadata type to create, update, or delete record type definitions for a custom object.


#### Metadata Types ActionOverride

13. SearchLayouts

Represents the metadata associated with the search layouts for an object. You can customize which fields to display for users in
search results, search filter fields, lookup dialogs, and recent record lists on tab home pages. You can access SearchLayouts only by
accessing its encompassing CustomObject.

14. SharingReason

Represents an Apex sharing reason, which is used to indicate why sharing was implemented for a custom object. Apex managed
sharing allows developers to use Apex to programmatically share custom objects. When you use Apex managed sharing to share a
custom object, only users with the “Modify All Data” permission can add or change the sharing on the custom object's record, and
the sharing access is maintained across record owner changes.

15. SharingRecalculation

Represents Apex classes that recalculate the Apex managed sharing for a specific custom object.

16. ValidationRule

Represents a validation rule, which is used to verify that the data a user enters in a record is valid and can be saved. A validation rule
contains a formula or expression that evaluates the data in one or more fields and returns a value of `true` or `false` . Validation
rules also include an error message that your client application can display to the user when the rule returns a value of `true` due
to invalid data.

17. WebLink

Represents a custom button or link defined in a custom object.

18. Metadata Field Types

These field types extend the field types described in the _Salesforce Object Reference_ .

SEE ALSO:

CustomField

Metadata

Picklist (Including Dependent Picklist)

SearchLayouts

WebLink

CustomObjectTranslation

ListView

CompactLayout

#### ActionOverride

Represents an action override on a standard or custom object. Use it to create, update, edit, or delete action overrides. You can access
#### ActionOverride only by accessing its encompassing CustomObject.

Declarative Metadata File Suffix and Directory Location

Action overrides are defined as part of a standard or custom object.

Version

Action overrides are available in API version 18.0 and later. As of Summer ’13, action overrides can be applied to both standard and
custom objects. Previously, action overrides only applied to custom objects.


Metadata Types ActionOverride

Fields

Unless otherwise noted, all fields are creatable, filterable, and nillable.

**Field Name** **Field Type** **Description**

`actionName` string Required. The possible values are the same as the actions you can override:

**•** `accept`

**•** `clone`

**•** `delete`

**•** `edit`

**•** `list`

**•** `new`

**•** `tab`

**•** `view`

`comment` string Any comments you want associated with the override.

`content` string Set this field if `type` is set to `flexipage`, `lightningcomponent`,
`scontrol`, or `visualforce` . It refers to the name of the Lightning

page, Lightning component, s-control, or Visualforce page to use as the
override. To reference installed components, use this format:
_**`Component_namespace`**_ `__` _**`Component_name`**_ .

`formFactor` FormFactor (enumeration of
type string)

The size of the page being overridden.

If the `type` field is set to `flexipage`, set this field to `Large` to
override the View action with a Lightning page in Lightning Experience.

The `Large` value represents the Lightning Experience desktop
environment and is valid only for the `flexipage` and
`lightningcomponent` types. The `Small` value represents the
Salesforce mobile app on a phone or tablet. The `Medium` value is
reserved for future use. The `null` value (which is the same as specifying
no value) represents Salesforce Classic.

This field is available in API version 37.0 and later and is part of the feature
for creating and editing record pages in Lightning Experience.

Lightning component overrides return different `FormFactor` values
depending on the API version used.

**•** In API version 41.0 and earlier, Lightning component overrides return
only the `null` value (no value), representing the Salesforce Classic
environment.

**•** In API version 42.0, if you specify different Lightning component
overrides for Lightning Experience and mobile, one component is
selected randomly for both overrides and its `FormFactor` value
is returned. If there’s a conflict between Lightning components, and
a Visualforce page override is also specified for Salesforce Classic, the
Visualforce page takes precedence.


Metadata Types ActionOverride

**Field Name** **Field Type** **Description**

**•** In API version 43.0 and later, a Lightning component override for
Lightning Experience returns the `Large` value and a Lightning
component override for mobile returns the `Small` value, as
expected.

`skipRecordTypeSelect` boolean Set this field to `true` if you prefer that any new records created by this
action override aren’t forwarded to the record type selection page. This

field is only valid if the `actionName` is a “create” type (like `new` ), and
`type` is set to `visualforce` . This field is available in API version 21.0
and later.

`type` ActionOverrideType Required. Represents the type of action override. Valid values are described
(enumeration of type string) in ActionOverrideType.

ActionOverrideType

ActionOverrideType on page 756 is an enumeration of type string that defines which kind of action override to use. The valid values are:

**•** `default` —The override uses a custom override provided by an installed package. If there isn’t one available, the standard Salesforce
behavior is used.

**•** `flexipage` —The override uses behavior from a Lightning page, and is only valid for the View action in Lightning Experience.

**•** `lightningcomponent` —The override uses behavior from a Lightning component.

**•** `scontrol` —The override uses behavior from an s-control.

**•** `standard` —The override uses regular Salesforce behavior.

**•** `visualforce` —The override uses behavior from a Visualforce page.

Note: Existing s-controls can be used as overrides for Salesforce Classic under certain conditions. However, s-controls have been
deprecated since the Spring ’09 release. We recommend using Visualforce pages instead.

Usage

You can't delete ActionOverrides by deploying with `destructiveChange.xml` . To delete an ActionOverride, retrieve the
CustomObject. In the definition file, find the `<ActionOverrides>` section, and remove the `<content>` row. Then, change the
`<type>` value in that same section to `Default` . Do this for every override you want to reset. After making the changes, rezip the
folder and deploy.

You can remove one override at a time each with its own deploy, or you can remove multiple overrides in a single deploy. However, we
recommend that you do a fresh retrieve every time you want to delete a new override. Don’t use a previously retrieved file.

Org default flexipage override assignment metadata can’t be retrieved from a managed package.

Declarative Metadata Sample Definitions

You can define action overrides, as in these examples for the Edit action.

A Visualforce page override for Salesforce Classic:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

```


Metadata Types ActionOverride

```
        <actionName>edit</actionName>

        <type>visualforce</type>

        <content>myEditVFPage</content>

        <comment>This edit action is a lot safer.</comment>

      </actionOverrides>

   </CustomObject

```

This example includes no value for FormFactor. Using no value is the same as using the `null` value, which represents Salesforce Classic.

A Lightning component override for Lightning Experience:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>edit</actionName>

        <type>lightningcomponent</type>

        <content>myEditLightningComponent</content>

        <formFactor>Large</formFactor>

        <comment>This edit action is a lot safer.</comment>

      </actionOverrides>

   </CustomObject>

```

A Lightning component override for the Salesforce mobile app:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>edit</actionName>

        <type>lightningcomponent</type>

        <content>myEditLightningComponent</content>

        <formFactor>Small</formFactor>

        <comment>This edit action is a lot safer.</comment>

      </actionOverrides>

   </CustomObject>

```

When overrides are included in a managed package, the overrides are represented as `default` type in the metadata. Calling retrieve()
presents the following:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>edit</actionName>

        <type>default</type>

      </actionOverrides>

   </CustomObject>

```

If you subscribe to a managed package with default overrides, you can replace the default override behavior by editing the XML. For
example, to replace the Visualforce page override with the Salesforce standard page for Salesforce Classic, use:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>edit</actionName>

        <type>standard</type>

      </actionOverrides>

   </CustomObject>

```

To set a Lightning page action override on the View standard button in Lightning Experience, use:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

```


#### Metadata Types BusinessProcess

```
        <actionName>View</actionName>

        <content>myLightningPage</content>

        <formFactor>Large</formFactor>

        <type>flexipage</type>

      </actionOverrides>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

#### BusinessProcess

The BusinessProcess metadata type enables you to display different picklist values for users based on their profile.

Multiple business processes allow you to track separate sales, support, and lead lifecycles. A sales, support, lead, or solution process is
assigned to a record type. The record type determines the user profiles that are associated with the business process.

Important: Don’t use business processes as an access control mechanism. Profile assignment governs create and edit access for
business process but doesn’t govern read access. For example, a user assigned to a profile that isn't enabled for a particular business
process can't create or edit it, but they can read the business process record.

Users with access to a business process can read all information it stores. Don’t store sensitive information in the business process
description, name, or picklist values. Instead, store sensitive information in a separate object or fields to which you’ve applied
appropriate access controls.

Declarative Metadata File Suffix and Directory Location

Business processes are defined as part of the custom object or standard object definition. See CustomObject for more information.

Version

#### BusinessProcess on page 758 components are available in API version 17.0 and later.

Special Access Rules

Access to this object requires the View Setup and Configuration permission.

Fields

**Field** **Field Type** **Description**

`description` string Description for the business process.


Metadata Types BusinessProcess

**Field** **Field Type** **Description**

`fullName` string Required. The name used as a unique identifier for API access.
This field is inherited from the Metadata component, but the

string it contains is created differently than the `fullName`
strings for other types. For a `fullName` string BusinessProcess
on page 758, the `fullName` is created combining the Entity
Name and Business Process Name. For example, for a business
process called “Bulk Orders” for opportunities, the `fullName`
would be `Opportunity.Bulk Orders` .

`isActive` boolean Indicates if the business process is active ( `true` ) or not
( `false` ).

`namespacePrefix` string The namespace of the developer organization where the
package was created.

`values` PicklistValue[] A list of picklist values associated with this business process.

Declarative Metadata Sample Definition

The following is a sample XML definition of a lead business process.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   ....

      <businessProcesses>

        <fullName>HardwareLeadProcess</fullName>

        <description>Lead Process for hardware division</description>

        <isActive>true</isActive>

        <values>

           <fullName>Closed - Converted</fullName>

           <default>false</default>

        </values>

        <values>

           <fullName>CustomLeadStep1</fullName>

           <default>false</default>

        </values>

        <values>

           <fullName>CustomLeadStep2</fullName>

           <default>false</default>

        </values>

        <values>

           <fullName>Open - Not Contacted</fullName>

           <default>false</default>

        </values>

        <values>

           <fullName>Working - Contacted</fullName>

           <default>true</default>

        </values>

      </businessProcesses>

   ....

   </CustomObject>

```


#### Metadata Types CompactLayout

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file only when a RecordType on page
793 is specified. For information about using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm#mdc_business_process_group)_ : BusinessProcessGroup

CustomObject

#### CompactLayout

Represents the metadata associated with a compact layout. This type extends the Metadata metadata type and inherits its `fullName`
field.

A compact layout displays a record’s key fields at a glance in the Salesforce mobile app, Lightning Experience, and in the Outlook and
Gmail integrations.

Compact layouts support all field types except:

**•** text area

**•** long text area

**•** rich text area

**•** multi-select picklist

[For more information on compact layouts, see Compact Layouts in the Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.compact_layout_overview.htm&type=5&language=en_US)

File Suffix and Directory Location

Compact layouts are defined as part of the custom object, standard object, or external object definition. See CustomObject for more
information.

Version

#### CompactLayout components are available in API version 29.0 and later. CompactLayout components are available for external objects

in API version 42.0 and later.

Fields

**Field Name** **Field Type** **Description**

`fields` string The fields assigned to the compact layout. Their order represents the
prioritization given to them when defining the compact layout.

`label` string Label that represents the object throughout the Salesforce user interface.


Metadata Types CompactLayout

Declarative Metadata Sample Definition

The following is an example of a CompactLayout component:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>Accept</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Clone</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Delete</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Edit</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>List</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>New</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Tab</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>View</actionName>

        <type>Default</type>

      </actionOverrides>

      <compactLayouts>

        <fullName>testCompactLayout</fullName>

        <fields>textfield__c</fields>

        <label>testCompactLayoutLabel</label>

      </compactLayouts>

      <compactLayoutAssignment>SYSTEM</compactLayoutAssignment>

      <deploymentStatus>Deployed</deploymentStatus>

      <enableActivities>false</enableActivities>

      <enableFeeds>false</enableFeeds>

      <enableHistory>false</enableHistory>

      <enableReports>false</enableReports>

      <fields>

        <fullName>textfield__c</fullName>

        <externalId>false</externalId>

        <label>textfield</label>

        <length>255</length>

        <required>false</required>

        <type>Text</type>

```


#### Metadata Types CustomField

```
        <unique>false</unique>

      </fields>

      <label>customObj</label>

      <nameField>

        <label>customObj Name</label>

        <type>Text</type>

      </nameField>

      <pluralLabel>customObjs</pluralLabel>

      <recordTypes>

        <fullName>RT1</fullName>

        <active>true</active>

        <label>RT1</label>

        <compactLayoutAssignment>testCompactLayout</compactLayoutAssignment>

      </recordTypes>

      <recordTypes>

        <fullName>RT2</fullName>

        <active>true</active>

        <label>RT2</label>

      </recordTypes>

      <searchLayouts/>

      <sharingModel>ReadWrite</sharingModel>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### CustomField

Represents the metadata associated with a field. Use this metadata type to create, update, or delete custom field definitions on standard,
custom, and external objects or standard field definitions on standard objects.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Only standard fields that you can customize are supported, that is, standard fields to which you can add help text or enable history
tracking or Chatter feed tracking. Other standard fields aren't supported, including system fields (such as `CreatedById` or
`LastModifiedDate` ) and autonumber fields. Some standard picklist fields aren’t supported. See Unsupported Metadata Types. By
default, a custom object doesn’t have any standard fields that are customizable.

Specify the full name whenever you create or update a field. For example, a custom field on a custom object:

```
   MyCustomObject__c.MyCustomField__c

```

An example of a custom field on a standard object:

```
   Account.MyAcctCustomField__c

```

An example of a standard field on a standard object:

```
   Account.Phone

```


Metadata Types CustomField

An example of a custom field on an external object:

```
   MyExternalObject__x.MyCustomField__c

```

Note: In Metadata API, external objects are represented by the CustomObject metadata type.

These custom field types aren’t available for external objects.

**•** Auto-number (available only with the cross-org adapter for Salesforce Connect)

**•** Currency (available only with the cross-org adapter for Salesforce Connect)

**•** Formula

**•** Location

**•** Master-detail relationship

**•** Picklist and multi-select picklist (available only with the cross-org adapter for Salesforce Connect)

**•** Roll-up summary

**•** Text (encrypted)

**•** Text Area (rich)

Declarative Metadata File Suffix and Directory Location

Custom fields are user-defined fields and are part of the custom object or standard object definition. See CustomObject for more
information. Standard fields are predefined on standard objects.

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Retrieving Fields on Custom or Standard Objects

When you retrieve a custom or standard object, you return everything associated with the object, except for standard fields that aren't
customizable. You can also retrieve only specific fields for an object by explicitly naming the object and fields in `package.xml` . The
following definition in `package.xml` creates the files `objects/MyCustomObject__c.object` and
`objects/Account.object`, each containing the requested field definitions.

```
   <types>

     <members>MyCustomObject__c.MyCustomField__c</members>

     <members>Account.MyCustomAccountField__c</members>

     <members>Account.Phone</members>

     <name>CustomField</name>

   </types>

```

Retrieving or Deploying Fields on Data 360 Objects

When you retrieve a Data 360 object, such as a DLO or DMO, not all of the custom field properties are returned. The properties returned
depend on the data type of the custom field.

When you deploy a Data 360 object via Metadata API, in API version 60.0 or later, the call succeeds only if the properties are supported
by the custom field's data type. If you include a property that isn't supported by the field's data type, the API returns an error.

Data 360 objects support these data types.

**•** Boolean/Checkbox


Metadata Types CustomField

**•** Date

**•** DateTime

**•** Email

**•** Lookup (DMOs only)

**•** Number

**•** Percent

**•** Phone

**•** Text

**•** Url

Version

Custom and standard fields are available in API version 10.0 and later.

Fields

Unless otherwise noted, all fields are creatable, filterable, and nillable.

**Field Name** **Field Type** **Description**

`businessOwnerGroup` reference Indicates the group associated with this field. The business owner
group understands the importance of the field’s data to your

company, and can be responsible for determining the minimum
security classification. This field is available in API version 45.0 and
later.

`businessOwnerUser` reference Indicates the person associated with this field. The business owner
understands the importance of the field’s data to your company,

and can be responsible for determining the minimum security
classification. This field is available in API version 45.0 and later.

`businessStatus` picklist Indicates whether the field is in use. Valid values include:

**•** `Active`

**•** `DeprecateCandidate`

**•** `Hidden`

This field is available in API version 45.0 and later

`caseSensitive` boolean

Indicates whether the field is case-sensitive ( `true` ) or not
( `false` ).

For indirect lookup relationship fields on external objects, this
attribute affects how this custom field’s values are matched against
the values of the `referenceTargetField` .

`complianceGroup` multipicklist Indicates the compliance acts, definitions, or regulations related
to the field’s data. Valid values include:

**•** `CCPA`

**•** `COPPA`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

**•** `GDPR`

**•** `HIPAA`

**•** `PCI`

**•** `PII`

This field is available in API version 47.0 and later.

`customDataType` string Deprecated in the Spring ‘19 (API version 45.0) release.

`defaultValue` string If specified, represents the default value of the field.

`deleteConstraint` DeleteConstraint (enumeration Provides deletion options for lookup relationships. Valid values are:
of type string)

**•** `Cascade` —Deletes the lookup record as well as associated
lookup fields.

**•** `Restrict` —Prevents the record from being deleted if it's
in a lookup relationship.

**•** `SetNull` —This value is the default. If the lookup record is
deleted, the lookup field is cleared.

For more information on lookup relationships, see "Object
Relationships" in Salesforce Help.

`deprecated` boolean Reserved for future use.

`description` string Description of the field.

`displayFormat` string The display format.

`displayLocationInDecimal` boolean Indicates how the geolocation values of a custom Location field
appear in the user interface. If `true`, the geolocation values appear

in decimal notation. If `false`, the geolocation values appear as
degrees, minutes, and seconds.

`elementType` ElementType (enumeration of Reserved for future use.
type string)

`encrypted` boolean

`encryptionScheme` EncryptionScheme
(enumeration of type string)

This entry is about Shield Platform Encryption, not Classic
Encryption.

Indicates whether this field is encrypted ( `true` ) or not ( `false` ).
This field is available in API version 34.0 through 43.0.

This entry is about Shield Platform Encryption, not Classic
Encryption.

For encrypted fields, determines which encryption scheme a field
takes. Valid values are

**•** `CaseInsensitiveDeterministicEncryption`

**•** `CaseSensitiveDeterministicEncryption`

**•** `None`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

**•** `ProbabilisticEncryption`

This field is available in API version 44.0 and later.

`externalDeveloperName` string Available only for external objects. Name of the table column on
the external data source that maps to this custom field in Salesforce.

Corresponds to `External Column Name` in the user
interface. This field is available in API version 32.0 and later.

`externalId` boolean

Indicates whether the field is an external ID field ( `true` ) or not
( `false` ). This property is returned only if the custom field data
type is AutoNumber, Email, Number, or Text.

`fieldManageability` FieldManageability Determines who can update the field after it’s released in a
(enumeration of type string) managed package. Valid values:

**•** `Locked` —The field can’t be updated.

**•** `DeveloperControlled` —The creator of the record can
update the field with a package upgrade.

**•** `SubscriberControlled` —Anyone with proper
permissions can update the field. The field can’t be updated
with a package upgrade.

Available only for fields on custom metadata types. If the field type
is `MetadataRelationship`, and the manageability of the
entity definition field is:

**•** Subscriber-controlled, then the Field Definition field must be
subscriber-controlled.

**•** Upgradeable, then the Field Definition field must be either
upgradeable or subscriber-controlled.

`formula` string If specified, represents a formula on the field.

`formulaTreatBlanksAs` TreatBlanksAs (enumeration of Indicates how to treat blanks in a formula. Valid values are:
type string) `BlankAsBlank` and `BlankAsZero` .

`fullName` string Inherited from Metadata, this field is defined in the WSDL for this
metadata type. It must be specified when creating, updating, or

deleting. See `createMetadata()` to see an example of this
field specified for a call.

This value can't be `null` .

`globalPicklist` string. (This field is available in API version 37.0 only and removed from
later versions.) If this custom field is a picklist that’s based on a

global picklist, `globalPicklist` is the name of the global
picklist whose value set this picklist inherits. A custom picklist that’s
based on a global picklist is restricted. You can only add or remove
values by editing the global picklist.


Metadata Types CustomField

**Field Name** **Field Type** **Description**

`indexed` boolean Indicates if the field is indexed. If this field is unique or the
`externalId` is set true, the `isIndexed` value is set to true.

This field has been deprecated as of API version 14.0 and is only
provided for backward compatibility.

`inlineHelpText` string Represents the content of field-level help. For more information,
see "Define Field-Level Help" in Salesforce Help.

`isAIPredictionField` boolean Available for Number type custom fields when you use Einstein
Prediction Builder. Denotes whether the field can store and display

Einstein prediction data on an object. Use Einstein Prediction Builder
to determine the data for the target field. This field is available in
API version 43.0 and later.

`isFilteringDisabled` boolean

Available only for external objects. Indicates whether the custom
field is available in filters. This field is available in API version 32.0
and later.

`isNameField` boolean Available only for external object fields of type text. For each
external object, you can specify one field as the name field. If you

set this value to `true`, make sure that the external table column
identified by the `externalDeveloperName` attribute
contains name values. This field is available in API version 32.0 and
later.

`isSortingDisabled` boolean Available only for external objects. Indicates whether the custom
field is sortable. This field is available in API version 32.0 and later.

`label` string Label for the field. You can't update the label for standard picklist
fields, such as the `Industry` field for accounts.

`length` int Length of the field.

`lookupFilter` LookupFilter Represents the metadata associated with a lookup filter. This
metadata type is used to create, update, or delete lookup filter

definitions. This component has been removed as of API version
30.0 and is only available in previous API versions. The metadata
associated with a lookup filter is now represented by the
`lookupFilter` field in the CustomField component.

This field is available in API version 30.0 and later.

LookupFilter isn't supported on the article type object.

`maskChar` EncryptedFieldMaskChar
(enumeration of type string)

This page is about Classic Encryption, not Shield Platform
Encryption.

For encrypted fields, specifies the character to be used as a mask.
Valid values are:

**•** `asterisk`

**•** `X`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

For more information on encrypted fields, see Classic Encryption
for Custom Fields in Salesforce Help.

`maskType` EncryptedFieldMaskType
(enumeration of type string)

This page is about Classic Encryption, not Shield Platform
Encryption.

For encrypted text fields, specifies the format of the masked and
unmasked characters in the field. Valid values are:

**•** `all` —All characters in the field are hidden. This option is
equivalent to the `Mask All Characters` option in
Salesforce.

**•** `creditCard` —The first 12 characters are hidden and the
last four display. This option is equivalent to the `Credit`
`Card Number` option in Salesforce.

**•** `lastFour` —All characters are hidden but the last four
display. This option is equivalent to the `Last Four`
`Characters Clear` option in Salesforce.

**•** `nino` —All characters are hidden. Salesforce automatically
inserts spaces after each pair of characters if the field contains
nine characters. This option is equivalent to the `National`
`Insurance Number` option in Salesforce.

**•** `sin` —All characters are hidden but the last four display. This
option is equivalent to the `Social Insurance Number`
option in Salesforce.

**•** `ssn` —The first five characters are hidden and the last four
display. This option is equivalent to the `Social Security`
`Number` option in Salesforce.

For more information on encrypted fields, see "Classic Encryption
for Custom Fields" in Salesforce Help.

`metadataRelationshipControllingField` string In custom metadata relationships, represents the controlling field
that specifies the standard or custom object in an entity definition

metadata relationship. Required when creating a field definition
or entity particle metadata relationship on a custom metadata
type. The object specified in the controlling field determines the
values available in its dependent field definition or entity particle.
For example, specifying the Account object filters the available
fields in the field definition to Account fields only. This field is
available in API version 39.0 and later.

`picklist` Picklist

( **Deprecated.** Use this field in API version 37.0 and earlier only. In
later versions, use `valueSet` instead.) If specified, the field is a
picklist, and this field enumerates the picklist values and labels.

`populateExistingRows` boolean Indicates whether existing rows are going to be populated ( `true` )
or not ( `false` ).


Metadata Types CustomField

**Field Name** **Field Type** **Description**

`precision` int

The precision for number values. Precision is the number of digits
in a number. For example, the number 256.99 has a precision value
of 5.

`referenceTargetField` string Available only for indirect lookup relationship fields on external
objects. Specifies the custom field on the parent object to match

against this indirect lookup relationship field, whose values come
from an external data source. The specified custom field on the
parent object must have both `externalId` and `unique` set
to `true` . This field is available in API version 32.0 and later.

`referenceTo` string If specified, indicates a reference this field has to another object.

`relationshipLabel` string Label for the relationship.

`relationshipName` string

If specified, indicates the value for one-to-many relationships. For
example, in the object MyObject that had a relationship to
YourObject, the relationship name can be YourObjects.

`relationshipOrder` int This field is valid for all master-detail relationships, but the value is
only non-zero for junction objects. A junction object has two

master-detail relationships, and is analogous to an association table
in a many-to-many relationship. Junction objects must define one
parent object as primary (0), the other as secondary (1). The
definition of primary or secondary affects delete behavior and
inheritance of look and feel, and record ownership for junction
objects. For more information, see Salesforce Help.

0 or 1 are the only valid values, and 0 is always the value for objects
that aren't junction objects.

`reparentableMasterDetail` boolean

Indicates whether the child records in a master-detail relationship
on a custom object can be reparented to different parent records.
The default value is `false` .

This field is available in API version 25.0 and later.

`required` boolean Indicates whether the field requires a value on creation ( `true` ) or
not ( `false` ).

`scale` int

The scale for the field. Scale is the number of digits to the right of
the decimal point in a number. For example, the number 256.99
has a scale of 2.

`securityClassification` picklist Indicates the sensitivity of the data contained in the field. Valid
values include:

**•** `Public`

**•** `Internal`

**•** `Confidential`

**•** `Restricted`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

**•** `MissionCritical`

This field is available in API version 45.0 and later.

`startingNumber` int If specified, indicates the starting number for the field. When you
create records, `Starting Number` ’s value increments to store

the number that will be assigned to the next auto-number field
created.

**•** You can’t retrieve the starting number of an auto-number field
through Metadata API. To specify a `Starting Number`
while deploying, add a `startingNumber` tag for your field
to your `package.xml` file. For example:

```
                              <startingNumber>42</startingNumber>

```

**•** If you deploy without specifying a `Starting Number`
value in your `package.xml` file, the default starting number
for standard fields is `0` . The default starting number for custom
fields is `1` .

`stripMarkup` boolean Set to `true` to remove markup, or `false` to preserve markup.
Used when converting a rich text area to a long text area.

`summarizedField` string

`summaryFilterItems` FilterItem[]

Represents the field on the detail row that’s being summarized.
This field can't be null unless the `summaryOperation` value
is `count` .

Represents the set of filter conditions for this field if it's a summary
field. This field is summed on the child if the filter conditions are
met.

`summaryForeignKey` string Represents the master-detail field on the child that defines the
relationship between the parent and the child.

`summaryOperation` SummaryOperations Represents the type of sum operation to be performed. Valid values
(enumeration of type string) are:

**•** `Count`

**•** `Min`

**•** `Max`

**•** `Sum`

`trackFeedHistory` boolean Indicates whether the field is enabled for feed tracking ( `true` ) or
not ( `false` ). To set this field to `true`, the `enableFeeds` field

on the associated CustomObject must also be `true` . For more
information, see "Customize Chatter Feed Tracking" in Salesforce
Help.

This field is available in API version 18.0 and later.


Metadata Types CustomField

**Field Name** **Field Type** **Description**

`trackHistory` boolean

Indicates whether history tracking is enabled for the field ( `true` )
or not ( `false` ). Also available for standard object fields (picklist
and lookup fields only) in API version 30.0 and later.

To set `trackHistory` to `true`, the `enableHistory` field
on the associated standard or custom object must also be `true` .

For more information, see "Field History Tracking" in Salesforce
Help.

Field history tracking isn’t available for external objects.

`trackTrending` boolean Indicates whether historical trending data is captured for the field
( `true` ) or not ( `false` ).An object is enabled for historical trending

if this attribute is `true` for at least one field. Available in API
version 29.0 and later.

For more information, see "Report on Historical Changes" in
Salesforce Help.

`trueValueIndexed` boolean

`type` FieldType (enumeration of type
string)

Only relevant for a checkbox field. If set, `true` values are built
into the index. This field has been deprecated as of API version 14.0
and is only provided for backward compatibility.

Indicates the field type for the field. Valid values are enumerated
in FieldType.

For standard fields on standard objects, the `type` field is optional.
This field is included for some standard field types, such as Picklist

or Lookup, but not for others. The `type` field is included for
custom fields.

`unique` boolean Indicates whether the field is unique ( `true` ) or not ( `false` ).

`valueSet` ValueSet Represents the set of values that make up a picklist on a custom
field. Each value is defined as a CustomValue on page 838. If this

custom field is a picklist that uses a global value set, `valueSet`
is the name of the global value set whose values this picklist
inherits. A custom picklist that uses a global value set is restricted.
You can only add or remove values by editing the global value set.

A ValueSet component has either a `valueSetDefinition`
or a `valueName` specified, but never both.

This field is available in API version 38.0 and later.

`visibleLines` int Indicates the number of lines displayed for the field.


Metadata Types CustomField

**Field Name** **Field Type** **Description**

`writeRequiresMasterRead` boolean

Sets the minimum sharing access level required on the primary
record to create, edit, or delete child records. This field applies only
to master-detail or junction object custom field types.

**•** `true` —Allows users with Read access to the primary record
permission to create, edit, or delete child records. This setting
makes sharing less restrictive.

**•** `false` —Allows users with Read/Write access to the primary
record permission to create, edit, or delete child records. This
setting is more restrictive than `true`, and is the default value.

For junction objects, the most restrictive access from the two
parents is enforced. For example, if you set to `true` on both
master-detail fields, but users have Read access to one primary
record and Read/Write access to the other primary record, users
aren't able to create, edit, or delete child records.

Fields use additional data types. For more information, see Metadata Field Types on page 806.

MktDataModelFieldAttributes

This is a subtype of CustomField.

**Field Name** **Field Type** **Description**

`definitionCreationType` DefinitionCreationType Indicates how this object was added. Valid values are:
enumeration

**•** `Bridge`

**•** `Custom`

**•** `Derived`

**•** `Standard`

**•** `System`

Valid values availble in API version 62.0 and later are:

**•** `Activation_Audience`

**•** `Ad_Audience_Insights`

**•** `ADG`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Directory_Table`

**•** `External`

**•** `Problem_Records`

**•** `Segment_Membership`

**•** `Semantic`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

**•** `Transform`

**•** `Vector_Embedding`

If this field is used for merging data, indicates what the system should do when
an invalid merge occurs.

Valid values are:

**•** `Drop`

**•** `Keep`

**•** `Override`

```
invalidMergeActionType

```

InvalidMergeActionType
(enumeration of type
string)

`isDynamicLookup` boolean When true, the existing data is queried for a unique set of values for this field.

`primaryIndexOrder` int If supplied, indicates that this field is part of the primary key. The number value
(starting at 1) indicates the order of attributes if it’s a compound primary key.

`refAttrDeveloperName` string When this is a Standard Field, it’s the Name of the field from the Reference
Model.

`mktDatalakeSrcKeyQualifier` string String storing the developer name of MktDataLakeSrcKeyQualifier configured
on the field

MktDataLakeFieldAttributes

This is a subtype of CustomField. MktDataLakeFieldAttributes is available in API version 50.0 or later.

**Field Name** **Field Type** **Description**

```
definitionCreationType

```

DefinitionCreationType Indicates how this object is added. Valid values are:
(enumeration of type

**•** `Bridge`

string)

**•** `Custom`

**•** `Derived`

**•** `Standard`

**•** `System`

Valid values available in API version 62.0 and later are:

**•** `ADG`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Directory_Table`

**•** `External`

**•** `Semantic`

**•** `Vector_Embedding`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

`dateFormat` string

Optional: The Date format of date, time, date/time fields in this Lake field.

**This field is deprecated in API version 55.0 and later.**

`externalName` string The external name of this field.

`isEventDate` boolean When true, this field contains the event date for behavioral model area objects
that are used to partition data.

`primaryIndexOrder` int If supplied, indicates that this field is part of the primary key. The number value
(starting at 1) indicates the order of attributes if it’s a compound primary key.

`isInternalOrganization` boolean

When true, this field contains the value for internal organization. In this case,
the value of the field is the name of the internal organization. Landing Objects
don't have access to the Salesforce ID and thus are using the developer name.

`isRecordModified` boolean Indicates the record modified field used to calibrate latest record version.

`mktDatalakeSrcKeyQualifier` string String storing the developer name of MktDataLakeSrcKeyQualifier configured
on the field. Available in API version 55.0 and later.

`keyQualifierName` string Contains the developer name of key qualifier field. Available in API version 55.0
and later.

LookupFilter

Represents the metadata associated with a lookup filter. Replaces the NamedFilter component, which was removed as of API version
30.0. LookupFilter is available in API version 30.0 and later.

**Field** **Field Type** **Description**

`active` boolean Required. Indicates whether the lookup filter is active ( `true` ) or not
( `false` ).

`booleanFilter` string Specifies advanced filter conditions.

`description` string A description of what this filter does.

`errorMessage` string The error message that appears if the lookup filter fails.

`filterItems` FilterItem[] Required. The set of filter conditions. You can have up to 10 FilterItems
per lookup filter.

`infoMessage` string

The information message displayed on the page. Use to describe
things the user possibly doesn't understand, such as why certain items
are excluded in the lookup filter.

`isOptional` boolean Required. Indicates whether the lookup filter is optional ( `true` ) or
not ( `false` ).

Lookup filters use additional data types. For more information, see Metadata Field Types.


Metadata Types CustomField

FilterItem

Represents one entry in a set of filter criteria.

**Field** **Field Type** **Description**

`field` string Represents the field specified in the filter.

```
operation

```

FilterOperation Represents the filter operation for this filter item. Valid values are:
(enumeration of

**•** `equals`

type string)

**•** `equals`

**•** `notEqual`

`value` string

`valueField` string

Declarative Metadata Sample Definition

**•** `lessThan`

**•** `greaterThan`

**•** `lessOrEqual`

**•** `greaterOrEqual`

**•** `contains`

**•** `notContain`

**•** `startsWith`

**•** `includes`

**•** `excludes`

**•** `within` ( `DISTANCE` criteria only)

Represents the value of the filter item being operated upon, for
example, if the filter is `my_number_field__c > 1`, the value
of `value` is `1` .

Specifies if the final column in the filter contains a field or a field value.

Approval processes don’t support `valueField` entries in filter
criteria.

The following example shows a field definition for a custom field that’s named `Comments__c` .

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

....

<fields>

     <fullName>Comments__c</fullName>

     <description>Add your comments about this object here</description>

     <inlineHelpText>This field contains help text for this object</inlineHelpText>

     <label>Comments</label>

     <length>32000</length>

     <type>LongTextArea</type>

     <visibleLines>30</visibleLines>

</fields>

....

</CustomObject>

```


#### Metadata Types FieldSet

This XML is the definition for two fields on the Account standard object—a custom field ( `MyCustomAccountField__c` ), and a
standard field ( `Phone` ) that has history tracking enabled.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <fields>

        <fullName>MyCustomAccountField__c</fullName>

        <description>A custom field on the Account standard object.</description>

        <externalId>false</externalId>

        <inlineHelpText>Some help text.</inlineHelpText>

        <label>MyCustomAccountField</label>

        <length>100</length>

        <required>false</required>

        <trackFeedHistory>false</trackFeedHistory>

        <trackHistory>false</trackHistory>

        <type>Text</type>

        <unique>false</unique>

      </fields>

      <fields>

        <fullName>Phone</fullName>

        <trackFeedHistory>false</trackFeedHistory>

        <trackHistory>true</trackHistory>

      </fields>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

Picklist (Including Dependent Picklist)

Metadata

NamedFilter

#### FieldSet

Represents a field set. A field set is a grouping of fields. For example, you could have a field set that contains fields describing a user's
first name, middle name, last name, and business title.

Field sets can be referenced on Visualforce pages dynamically. If the page is added to a managed package, administrators can add,
remove, or reorder fields in a field set to modify the fields presented on the Visualforce page without modifying any code.

Version

#### FieldSet components are available in API version 21.0 and later.


Metadata Types FieldSet

Fields

**Field** **Field Type** **Description**

`availableFields` FieldSetItem[] An array containing all the possible fields in the field set.

`description` string Required. A description provided by the developer that describes
the field set. This is required.

`displayedFields` FieldSetItem[]

An array containing all the fields that are presented on the
Visualforce page. The order in which a field is listed determines
the order of appearance on the page.

`label` string Required. The label used to reference the field set.

FieldSetItem

FieldSetItem represents an individual field in a field set.

**Field** **Field Type** **Description**

`field` string Required. The name of a field in a standard or custom object.

`isFieldManaged` boolean Read-only. Denotes whether the field was added to the field set
via a managed or unmanaged package.

`isRequired` boolean Read-only. Indicates whether the field is universally required
( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

A sample XML definition of a FieldSet component is shown below.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   <fieldSets>

     <fullName>FieldSetNames</fullName>

     <availableFields>

        <field>MiddleName__c</field>

     </availableFields>

     <availableFields>

        <field>Title__c</field>

     </availableFields>

     <description>FieldSet containing how to properly address someone</description>

     <displayedFields>

        <field>FirstName__c</field>

     </displayedFields>

     <displayedFields>

        <field>LastName__c</field>

     </displayedFields>

     <label>FieldSet Names</label>

```


#### Metadata Types HistoryRetentionPolicy

```
      </fieldSets>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### HistoryRetentionPolicy

Represents the policy for archiving field history data. When you set a policy, you specify the number of months that you want to keep
field history in Salesforce before archiving it. By default, when Field Audit Trail is enabled, all field history is retained.

This component is only available to users with the RetainFieldHistory permission.

Declarative Metadata File Suffix and Directory Location

Field history retention policies are defined as part of a standard or custom object. You can set field history retention policies for objects
individually. See CustomObject for more information.

Version

Available in API version 31.0 and later.

Fields

**Field Name** **Field Type** **Description**

`archiveAfterMonths` int Required. The number of months that you want to keep field history data
in Salesforce before archiving. You can set a minimum of 1 month and a

maximum of 18 months. If you don't set a number, the default is 18
months. (That is, Salesforce maintains data for 18 months before
archiving.)

`archiveRetentionYears` int

The number of years until you manually delete data from the archive. Use
this field as a reminder for manually deleting data. By default, field history
data isn’t automatically deleted when Field Audit Trail is enabled.

`description` string A text description for the history retention.

`gracePeriodDays` int The number of days of extra time after the `archiveAfterMonths`
period before the data is archived. The `gracePeriodDays` interval

applies only to the first time that the data is archived; because all the data
is copied the first time, the operation can take longer than subsequent
times when only the data that changed since the last archival operation
is copied. The `gracePeriodDays` provides extra time for the
administrator to prepare the organization before the initial archive
operation. You can set a minimum of zero days and a maximum of 10
days. If no number is set, the default is 1 day.


#### Metadata Types Index

Declarative Metadata Sample Definition

This sample shows the definition of a history retention policy for a custom object.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

     <historyRetentionPolicy>

        <archiveAfterMonths>6</archiveAfterMonths>

        <archiveRetentionYears>5</archiveRetentionYears>

        <description>My field history retention</description>

     </historyRetentionPolicy>

   ...

   </CustomObject>

#### Index

```

[Represents an index defined within a custom big object. Use this metadata type to define the composite primary key (index) for a custom](https://developer.salesforce.com/docs/atlas.en-us.260.0.bigobjects.meta/bigobjects/big_object.htm)
big object. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### Indexes are user-defined and are part of the custom object definition for big objects. See CustomObject for more information.

Version

The Index type is available in API version 41.0 and later.

Fields

**Field Name** **Field Type** **Description**

#### fields IndexField[] The definition of the fields in the index.

`label` string Required. This name is used to refer to the big object in the user interface.
Available in API version 41.0 and later.

#### IndexField

Defines which fields make up the index, their order, and sort direction. The order in which the fields are defined determines the order
fields are listed in the index.


Metadata Types Index

**Field Name** **Field Type** **Description**

`name` string

Required. The API name for the field that’s part of the index. This value must
match the `fullName` value for the corresponding field in the fields section
and be marked as required.

Warning: When querying a big object record via SOQL and passing
the results as arguments to the delete API, if any index field name has
a leading or trailing white space, you can't delete the big object record.

`sortDirection` string Required. The sort direction of the field in the index. Valid values are `ASC` for
ascending order and `DESC` for descending order.

Declarative Metadata Sample Definition

The following is an example of an index contained within the definition of a custom big object,
`Customer_Interactions__b.object` .

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   <deploymentStatus>Deployed</deploymentStatus>

// Define the fields within the big object

   <fields>

     <fullName>Purchase__c</fullName>

     <label>Purchase</label>

     <length>16</length>

     <required>false</required>

     <type>Text</type>

     <unique>false</unique>

   </fields>

   <fields>

     <fullName>Order_Number__c</fullName>

     <label>Order Number</label>

     <length>16</length>

     <required>false</required>

     <type>Text</type>

     <unique>true</unique>

   </fields>

   <fields>

     <fullName>Platform__c</fullName>

     <label>Platform</label>

     <length>16</length>

     <required>true</required>

     <type>Text</type>

     <unique>false</unique>

   </fields>

   <fields>

     <fullName>Account__c</fullName>

```


#### Metadata Types ListView

```
        <label>User Account</label>

        <referenceTo>Account</referenceTo>

        <relationshipName>User_Account</relationshipName>

        <required>true</required>

        <type>Lookup</type>

      </fields>

      <fields>

        <fullName>Order_Date__c</fullName>

        <label>Order Date</label>

        <required>true</required>

        <type>DateTime</type>

      </fields>

   // Define the index

      <indexes>

        <fullName>CustomerInteractionsIndex</fullName>

        <label>Customer Interactions Index</label>

        <fields>

           <name>Account__c</name>

           <sortDirection>DESC</sortDirection>

        </fields>

        <fields>

           <name>Platform__c</name>

           <sortDirection>ASC</sortDirection>

        </fields>

        <fields>

           <name>Order_Date__c</name>

           <sortDirection>DESC</sortDirection>

        </fields>

      </indexes>

      <label>Customer Interaction</label>

      <pluralLabel>Customer Interactions</pluralLabel>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

Metadata

#### ListView ListView allows you to see a filtered list of records, such as contacts, accounts, or custom objects.

This type extends the Metadata metadata type and inherits its `fullName` field. See “Create a Custom List View in Salesforce Classic”
in Salesforce Help.


Metadata Types ListView

Note: List views with the Visible only to me `Restrict Visibility` option aren’t accessible in Metadata API. Each of these
list views is associated with a particular user.

Declarative Metadata File Suffix and Directory Location

List views are stored within a CustomObject component. The component can represent a custom object or a standard object, such as
an account.

Version

ListView components for custom objects are available in API version 14.0 and later. ListView components for standard objects, such as
accounts, are available in API version 17.0 and later.

Fields

**Field** **Field Type** **Description**

`booleanFilter` string This field represents an Advanced Option for a filter. Advanced
Options in filters allow you to build up filtering conditions that

use a mixture of AND and OR boolean operators across multiple
filter line items. For example, `(1 AND 2) OR 3` finds records
that match both the first two filter line items or the third.

`columns` string[]

The list of fields in the list view. The field name relative to the
object name, for example MyCustomField__c, is specified for
each custom field.

Field names in the ListView columns don’t always match their
API name counterparts. If person accounts are enabled in your

organization, standard fields merged from a contact into an
account start with the `PC_` prefix, while the corresponding API
name starts with the `Person` prefix. For example, the ListView
column name is `PC_Email` for a corresponding API field name
of `PersonEmail` .

`division` string If your organization uses divisions to segment data and you’ve
got the “Affected by Divisions” permission, records in the list

view must match this division. This field is only available if you’re
searching all records.

This field is available in API version 17.0 and later.

`filterScope` FilterScope (enumeration of Required. This field indicates whether you’re filtering by owner
type string) or viewing all records.

`filters` ListViewFilter[] The list of filter line items.

`fullName` string Required. Inherited from Metadata Metadata, this field is defined
in the WSDL for this metadata type. It must be specified when

creating, updating, or deleting. See `createMetadata()` to
see an example of this field specified for a call.


Metadata Types ListView

**Field** **Field Type** **Description**

`label` string Required. The list view name.

`language` Language The language used for filtering if your organization uses the
Translation Workbench and you’re using the `startsWith`

or `contains` operator. The values entered as search terms
must be in the same language as the filter language.

For a list of valid language values, see Language.

This field is available in API version 17.0 and later.

`queue` string The name of a queue. Objects are sometimes assigned to a
queue so that the users who have access to the queue can

monitor and manage them. When you create a queue, a
corresponding list view is automatically created. See “Create
Queues” in Salesforce Help.

`sharedTo` SharedTo

ListViewFilter

ListViewFilter represents a filter line item.

Sharing access for the list view.

This field is available in API version 17.0 and later.

**Field** **Field Type** **Description**

`filter` string Required. Represents the field specified in the filter.

`operation` FilterOperation (enumeration of Required. The operation used by the filter, such as `equals` .
type string) The valid values are:

**•** `equals`

**•** `notEqual`

**•** `lessThan`

**•** `greaterThan`

**•** `lessOrEqual`

**•** `greaterOrEqual`

**•** `contains`

**•** `notContain`

**•** `startsWith`

**•** `includes`

**•** `excludes`

**•** `within` ( `DISTANCE` criteria only)

`value` string

Represents the value of the filter item being operated upon, for
example, if the filter is `my_number_field__c > 1`, the
value of `value` is `1` .


Metadata Types ListView

FilterScope

The FilterScope is an enumeration of type string that represents the filtering criteria for the records. The valid values are listed in the
table:

**Enumeration Value** **Description**

`Everything` All records, for example All Opportunities.

`Mine` Records owned by the user running the list view, for example My Opportunities.

`MineAndMyGroups` Records owned by the user running the list view, and records assigned to the user’s queues.

```
AssignedToMe

```

Records assigned to the user running the list view.

The `AssignedToMe` scope is supported for the ServiceAppointment object only.

`Queue` Records assigned to a queue.

`Delegated` Records delegated to another user for action: for example, a delegated task. This option is
available in API version 17.0 and later.

```
MyTerritory

MyTeamTerritory

```

Records in the territory of the user seeing the list view. This option is available if territory
management is enabled for your organization. Opportunities can’t be filtered by
`MyTerritory` . This option is available in API version 17.0 and later.

Records in the territory of the team of the user seeing the list view. This option is available if
territory management is enabled for your organization. Opportunities can’t be filtered by
`MyTeamTerritory` . This option is available in API version 17.0 and later.

`Team` Records assigned to a team. In the Lightning Experience UI, the corresponding list view filter is
**My team’s opportunities** . This option is available in API version 17.0 and later.

`SalesTeam` Opportunities assigned to an opportunity team. In the Lightning Experience UI, the corresponding
list view filter is **My opportunity teams** . This option is available in API version 49.0 and later.

`ScopingRule` Records that meet a scoping rule's record criteria. In Lightning Experience, scoping rules are
applied to list views only if the user selects **Filter by scope** .

Declarative Metadata Sample Definition

A sample XML definition of a list view in a custom object is shown.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

. . .

   <listViews>

     <fullName>All_Mileages</fullName>

     <filterScope>everything</filterScope>

     <label>All Mileages</label>

   </listViews>

   <listViews>

     <fullName>My_Mileages</fullName>

     <booleanFilter>1 AND 2</booleanFilter>

     <columns>NAME</columns>

```


#### Metadata Types NamedFilter

```
        <columns>CREATED_DATE</columns>

        <filterScope>mine</filterScope>

        <filters>

           <field>NAME</field>

           <operation>equals</operation>

           <value>Eric Bristow</value>

        </filters>

        <filters>

           <field>City__c</field>

           <operation>equals</operation>

           <value>Paris</value>

        </filters>

        <label>My Mileages</label>

      </listViews>

   . . .

   </CustomObject>

```

Usage

In general, avoid including unedited default list views in managed packages. We discourage including a modified default list view in a
[managed package, as it can result in duplicated list views in the target org. See Incorrect List View Loads Due to Possibility of Existing](https://help.salesforce.com/s/articleView?id=000386164&type=1&language=en_US)
[Duplicate List Views.](https://help.salesforce.com/s/articleView?id=000386164&type=1&language=en_US)

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

Sample package.xml Manifest Files

#### NamedFilter

Represents the metadata associated with a lookup filter. This metadata type is used to create, update, or delete lookup filter definitions.
This component has been removed as of API version 30.0 and is only available in previous API versions. The metadata associated with
a lookup filter is now represented by the lookupFilter field in the CustomField component.

This type extends the Metadata metadata type and inherits its `fullName` field. You can also use this metadata type to work with
customizations of lookup filters on standard fields.

Note: The namedFilter appears as a child of the target object of the associated lookup field.

Declarative Metadata File Suffix and Directory Location

Lookup filters are defined as part of the custom object or standard object definition. See CustomObject for more information.

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.


Metadata Types NamedFilter

Version

Lookup filters are available in API version 17.0 and later. However, the NamedFilter type was removed in API version 30.0. The metadata
associated with a lookup filter is now represented by the lookupFilter field in the CustomField type.

Fields

Unless otherwise noted, all fields are creatable, filterable, and nillable.

**Field Name** **Field Type** **Description**

`active` boolean Required. Indicates whether the lookup filter is active.

`booleanFilter` string Specifies advanced filter conditions.

`description` string A description of what this filter does.

`errorMessage` string The error message that appears if the lookup filter fails.

`field` string

Required. The `fullName` of the custom or standard field
associated with the lookup filter. You can associate one
relationship field with each lookup filter, and vice versa.

Note: You can’t update a field associated with a lookup
filter.

`filterItems` FilterItems[] Required. The set of filter conditions.

`infoMessage` string

The information message displayed on the page. Use to
describe things the user might not understand, such as why
certain items are excluded in the lookup filter.

`fullName` string Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see an
example of this field specified for a call.

This value can’t be `null` .

`isOptional` boolean Required. Indicates whether the lookup filter is optional.

`name` string Required. The name of the lookup filter. If you create this field
in the user interface, a name is automatically assigned. If you

create this field through Metadata API, you must include the
`name` field.

`sourceObject` string

The object that contains the lookup field that uses this lookup
filter. Set this field if the lookup filter references fields on the
source object.

Lookup filters use additional data types. For more information, see Metadata Field Types.


Metadata Types NamedFilter

FilterItems

FilterItems contains the following properties:

**Field** **Field Type** **Description**

`field` string Represents the field specified in the filter.

```
operation

```

FilterOperation Represents the filter operation for this filter item. Valid values are
(enumeration of enumerated in FilterOperation.
type string)

`value` string

FilterOperation

Represents the value of the filter item being operated upon, for
example, if the filter is `my_number_field__c > 1`, the value
of `value` is `1` .

Here’s an enumeration of type string that lists different filter operations. Valid values are:

**•** `equals`

**•** `notEqual`

**•** `lessThan`

**•** `greaterThan`

**•** `lessOrEqual`

**•** `greaterOrEqual`

**•** `contains`

**•** `notContain`

**•** `startsWith`

**•** `includes`

**•** `excludes`

Declarative Metadata Sample Definition

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

....

   <namedfilters>

     <fullName>nf_Acc</fullName>

     <active>true</active>

     <booleanFilter>1 OR 2</booleanFilter>

     <field>Account.lk__c</field>

     <filterItems>

        <field>Account.Phone</field>

        <operation>notEqual</operation>

        <value>x</value>

     </filterItems>

     <filterItems>

        <field>Account.Fax</field>

```


#### Metadata Types Picklist (Including Dependent Picklist)

```
           <operation>notEqual</operation>

           <value>y</value>

        </filterItems>

        <name>Acc</name>

        <sourceObject>Account</sourceObject>

      </namedfilters>

   ....

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

#### Picklist (Including Dependent Picklist)

Metadata

CustomField

#### Picklist (Including Dependent Picklist)

Deprecated. Represents a picklist (or dependent picklist) definition for a custom field in a custom object or a custom or standard field
in a standard object, such as an account.

Version

Use this type in API version 37.0 and earlier only. Picklists for custom fields in custom objects are available in API version 12.0 and later.
Picklists for custom or standard fields in standard objects, such as accounts, are available in API version 16.0 and later.

In API version 38.0 and later, Picklist is replaced by ValueSet on page 809 on the CustomField type.

Declarative Metadata File Suffix and Directory Location

Picklist definitions are included in the custom object and field with which they’re associated.

Fields

Picklist contains the following fields:

**Field Name** **Field Type** **Description**

`controllingField` string The `fullName` of the controlling field if `controllingField` is
a dependent picklist. A dependent picklist works in conjunction with a

controlling picklist or checkbox to filter the available options. The value
chosen in the controlling field affects the values available in the
dependent field. This field is available in API version 14.0 and later.


Metadata Types Picklist (Including Dependent Picklist)

**Field Name** **Field Type** **Description**

`picklistValues` PicklistValue[]
Required. Represents a set of values for a picklist.

`restrictedPicklist` boolean

`sorted` boolean

Java Sample

Indicates whether the picklist’s value list is restricted. With a restricted
picklist, only an admin can add or change values; users can’t load or
remove values through the API. By default this value is `false` .

This field is available in API version 37.0 and later.

Indicates whether values are sorted ( `true` ), or not ( `false` ). By default
this value is `false` .

The following sample uses a picklist. For a complete sample of using a picklist with record types and profiles, see Profile on page 1726.

```
public void setPicklistValues() {

  // Create a picklist

  Picklist expenseStatus = new Picklist();

  PicklistValue unsubmitted = new PicklistValue();

  unsubmitted.setFullName("Unsubmitted");

  PicklistValue submitted = new PicklistValue();

  submitted.setFullName("Submitted");

  PicklistValue approved = new PicklistValue();

  approved.setFullName("Approved");

  PicklistValue rejected = new PicklistValue();

  rejected.setFullName("Rejected");

  expenseStatus.setPicklistValues(new PicklistValue[]

    {unsubmitted, submitted, approved, rejected});

  CustomField expenseStatusField = new CustomField();

  expenseStatusField.setFullName(

    "ExpenseReport__c.ExpenseStatus__c");

  expenseStatusField.setLabel("Expense Report Status");

  expenseStatusField.setType(FieldType.Picklist);

  expenseStatusField.setPicklist(expenseStatus);

  try {

   AsyncResult[] ars =

   metadataConnection.create(new Metadata[] {expenseStatusField});

  } catch (ConnectionException ce) {

   ce.printStackTrace();

  }

}

```


Metadata Types Picklist (Including Dependent Picklist)

Declarative Metadata Sample Definition

The following sample shows usage for picklists, including dependent picklists, in a custom object. The `isAmerican__c` checkbox
controls the list of manufacturers shown in the `manufacturer__c` picklist. The `manufacturer__c` checkbox in turn controls
the list of models shown in the `model__c` picklist.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <deploymentStatus>Deployed</deploymentStatus>

      <enableActivities>true</enableActivities>

      <fields>

        <fullName>isAmerican__c</fullName>

        <defaultValue>false</defaultValue>

        <label>American Only</label>

        <type>Checkbox</type>

      </fields>

      <fields>

        <fullName>manufacturer__c</fullName>

        <label>Manufacturer</label>

        <picklist>

           <controllingField>isAmerican__c</controllingField>

           <picklistValues>

             <fullName>Chrysler</fullName>

             <controllingFieldValues>checked</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Ford</fullName>

             <controllingFieldValues>checked</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Honda</fullName>

             <controllingFieldValues>unchecked</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Toyota</fullName>

             <controllingFieldValues>unchecked</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <sorted>false</sorted>

        </picklist>

        <type>Picklist</type>

      </fields>

      <fields>

        <fullName>model__c</fullName>

        <label>Model</label>

        <picklist>

           <controllingField>manufacturer__c</controllingField>

           <picklistValues>

             <fullName>Mustang</fullName>

             <controllingFieldValues>Ford</controllingFieldValues>

             <default>false</default>

           </picklistValues>

```


Metadata Types Picklist (Including Dependent Picklist)

```
           <picklistValues>

             <fullName>Taurus</fullName>

             <controllingFieldValues>Ford</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>PT Cruiser</fullName>

             <controllingFieldValues>Chrysler</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Pacifica</fullName>

             <controllingFieldValues>Chrysler</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Accord</fullName>

             <controllingFieldValues>Honda</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Civic</fullName>

             <controllingFieldValues>Honda</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Prius</fullName>

             <controllingFieldValues>Toyota</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Camry</fullName>

             <controllingFieldValues>Toyota</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <sorted>false</sorted>

        </picklist>

        <type>Picklist</type>

      </fields>

   ....

   </CustomObject>

```

The following sample shows usage for the standard `Stage` field in opportunities.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <fields>

        <fullName>StageName</fullName>

        <picklist>

           <picklistValues>

             <fullName>Prospecting</fullName>

             <default>false</default>

             <forecastCategory>Pipeline</forecastCategory>

             <probability>10</probability>

           </picklistValues>

```


#### Metadata Types ProfileSearchLayouts

```
           <picklistValues>

             <fullName>Qualification</fullName>

             <default>false</default>

             <forecastCategory>Pipeline</forecastCategory>

             <probability>10</probability>

           </picklistValues>

           <picklistValues>

             <fullName>Needs Analysis</fullName>

             <default>false</default>

             <forecastCategory>Pipeline</forecastCategory>

             <probability>20</probability>

           </picklistValues>

           ...

        </picklist>

      </fields>

   <CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ProfileSearchLayouts Represents a user profile’s search results layouts for an object. ProfileSearchLayouts are similar to SearchLayouts .

However, with profile-specific layouts, each user profile can have a different search results layout for an object.

File Suffix and Directory Location

Profile search layouts are defined as part of a standard or custom object. `SearchLayout` is the default search results layout used
when no layout is specified for a user profile. For more information, see CustomObject.

Version

Profile search layouts for custom objects are available in API version 48.0 and later.

Fields

**Field** **Field Type** **Description**

`profileName` string[]

The name of the profile associated with a customized search
results layout. The profile name can be a standard Salesforce
profile or custom profile defined in your org.

`fields` string[] The list of fields displayed in search results for the object and
for the users that have the profile _`Profile Name`_ . The

`name` field is required and is always displayed as the first
column header, so it isn’t included in this list. All additional
fields are included. The field name relative to the object


#### Metadata Types RecordType

**Field** **Field Type** **Description**

name, for _`exampleMyCustomField__c`_, is specified
for each custom field.

Declarative Metadata Sample Definition

The following shows a sample definition of profile-specific search layouts in an object.

Note: To deploy a profile-specific search results layout, the profile must be defined in the destination org and if it's for a custom
object, you must enable search for that custom object. If the profile-specific search results layout is for a custom object, the custom
object's tab must exist in the destination org or must be included with the deployment.

```
   <?xml version="1.0" encoding="UTF-8"?>

             <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

             . . .

             <profileSearchLayouts>

             <fields>ACCOUNT.NAME</fields>

             <fields>ACCOUNT.SITE</fields>

             <fields>ACCOUNT.PHONE1</fields>

             <fields>CORE.USERS.ALIAS</fields>

             <fields>ACCOUNT.ADDRESS2_CITY</fields>

             <profileName>System Administrator</profileName>

             </profileSearchLayouts>

             <profileSearchLayouts>

             <fields>ACCOUNT.NAME</fields>

             <fields>ACCOUNT.SITE</fields>

             <profileName>WDC Only User</profileName>

             </profileSearchLayouts>

             . . .

             </CustomObject>

```

SEE ALSO:

SearchLayouts

#### RecordType

Represents the metadata associated with a record type. Record types let you offer different business processes, picklist values, and page
layouts to different users. Use this metadata type to create, update, or delete record type definitions for a custom object.

For more information, see _Tailor Busines Processes to Different Record Types Users_ in Salesforce Help. This type extends the Metadata
metadata type and inherits its `fullName` field.

Important: Don’t use record types as an access control mechanism. Profile assignment governs create and edit access for an
object but doesn’t govern read access. For example, a user assigned to a profile that isn't enabled for a particular record type can't
create records with that record type, but can access records associated with that record type.

Users with access to an object can read all record type information for that object. We strongly recommend against storing sensitive
information in the record type description, name, or label. Instead, store sensitive information in a separate object or fields to which
you’ve applied appropriate access controls.


Metadata Types RecordType

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Note: Metadata API doesn’t retrieve custom picklist values on person account record types, if the picklist exists on a contact. In
this case, Metadata API retrieves standard picklist values only.

Note: Metadata API doesn't retrieve specific picklist fields that are associated with a record type.

Version

Record types are available in API version 12.0 and later.

Fields

**Field** **Field Type** **Description**

`active` boolean Required. Indicates whether the record type is active.

`businessProcess` string The `fullName` of the business process associated with
the record type. This field is required in record types for lead,

opportunity, solution, and case, and not allowed otherwise.
See BusinessProcess on page 758.

This field is available in API version 17.0 and later.

`compactLayoutAssignment` string

Represents the compact layout that is assigned to the record
type.

This field is available in API version 29.0 and later.

`description` string Record type description. Maximum of 255 characters.

`fullName` string Record type name. The `fullName` can contain only
underscores and alphanumeric characters. It must be unique,

begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores.
If this field contained characters before version 14.0 that are
no longer allowed, the characters were stripped out of this
field, and the previous value of the field was saved in the
`label` field.

Inherited from the Metadata component, this field isn’t
defined in the WSDL for this component. It must be specified
when creating, updating, or deleting. See create() to see an
example of this field specified for a call.

This value can't be `null` .

`label` string Required. Descriptive label for the record type. The list of
characters allowed in the `fullName` field has been reduced

for versions 14.0 and later. This field contains the value
contained in the `fullName` field before version 14.0.


Metadata Types RecordType

**Field** **Field Type** **Description**

`picklistValues` RecordTypePicklistValue[] Represents a set of values for a picklist.

RecordTypePicklistValue

RecordTypePicklistValue represents the combination of picklists and valid values that define a record type:

**Field Name** **Field Type** **Description**

`picklist` string Required. The name of the picklist.

`values` PicklistValue One or more of the picklist values in the picklist. Each value defined is
available in the record type that contains this component.

Java Sample

The following sample uses two record types. For the complete sample that includes profiles and picklists, see Profile on page 1726.

```
   public void recordTypeSample() {

     try {

      // Employees and managers have different access

      // to the state of the expense sheet

      RecordType edit = new RecordType();

      edit.setFullName("ExpenseReport__c.Edit");

      edit.setLabel("ExpenseReport__c.Label");

      PicklistValue unsubmitted = new PicklistValue();

      unsubmitted.setFullName("Unsubmitted");

      PicklistValue submitted = new PicklistValue();

      submitted.setFullName("Submitted");

      RecordTypePicklistValue editStatuses =

        new RecordTypePicklistValue();

      editStatuses.setPicklist("ExpenseStatus__c");

      editStatuses.setValues(

        new PicklistValue[] {unsubmitted, submitted});

      edit.setPicklistValues(

        new RecordTypePicklistValue[] {editStatuses});

      AsyncResult[] arsEdit =

        metadataConnection.create(new Metadata[] {edit});

      RecordType approve = new RecordType();

      approve.setFullName("ExpenseReport__c.Approve");

      PicklistValue approved = new PicklistValue();

      approved.setFullName("Approved");

      PicklistValue rejected = new PicklistValue();

      rejected.setFullName("Rejected");

      RecordTypePicklistValue approveStatuses =

        new RecordTypePicklistValue();

      approveStatuses.setPicklist("ExpenseStatus__c");

      approveStatuses.setValues(

        new PicklistValue[] {approved, rejected});

      approve.setPicklistValues(

```


#### Metadata Types SearchLayouts

```
        new RecordTypePicklistValue[] {approveStatuses});

      AsyncResult[] arsApprove =

       metadataConnection.create(new Metadata[] {approve});

     } catch (ConnectionException ce) {

      ce.printStackTrace();

     }

   }

```

Declarative Metadata Sample Definition

The definition of a record type in a custom object is shown in this code block.

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   . . .

     <recordTypes>

        <fullName>My First Recordtype</fullName>

      </recordTypes>

    . . .

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SearchLayouts

Represents the metadata associated with the search layouts for an object. You can customize which fields to display for users in search
results, search filter fields, lookup dialogs, and recent record lists on tab home pages. You can access SearchLayouts only by accessing
its encompassing CustomObject.

[For more information, see Customize Layouts for Search Results and Customize Search Layouts for Custom Objects in Salesforce Help.](https://help.salesforce.com/articleView?id=ai.customizing_search_layouts.htm&type=5&language=en_US)

Version

Search layouts for custom objects are available in API version 14.0 and later. The ability to modify search layouts for standard objects
(except events and tasks) is available in API version 27.0 and later.

Fields

When defining metadata for search layouts:

**•** Any Name field defined as a text type is mandatory; it’s always displayed as the first column in the search results page. When you
query for a list of fields; the name field isn’t returned but all other fields are. If you define the Name field as an autonumber type, it’s
not mandatory and you can remove it from the list, but when you import the search layout with Metadata API, it will always add the
Name field back. These rules apply to `customTabListAdditionalFields`, `lookupDialogsAdditionalFields`,
`lookupPhoneDialogsAdditionalFields`, and `searchResultsAdditionalFields`

**•** For custom objects, the search layout uses the API name, for example, MyCustomField__c instead of the field name My Custom
Field.


Metadata Types SearchLayouts

**Field** **Field Type** **Description**

`customTabListAdditionalFields` string[] The list of fields displayed in the Recent _`Object Name`_
list view for an object.

`excludedStandardButtons` string[] The list of standard buttons excluded from the search layout.

`listViewButtons` string[]

`lookupDialogsAdditionalFields` string[]

`lookupFilterFields` string[]

`lookupPhoneDialogsAdditionalFields` string[]

`massQuickActions` string[]

The list of buttons available in list views for an object.

This field is equivalent to the Buttons Displayed value in the
_`Object Name`_ `List View` in the related list of the
object detail page in the UI.

The list of fields displayed in a lookup dialog for the object.

Salesforce objects often include one or more _lookup fields_
that allow users to associate two records together in a

relationship. For example, a contact record includes an
`Account` lookup field that represents the relationship
between the contact and the organization with which the
contact is associated. A lookup search dialog helps you search
for the record associated with the one being edited. Lookup
filter fields allow you to filter your lookup search by a
customized list of fields in the object.

This field is equivalent to the `Lookup Dialogs` related
list on the object detail page in the UI.

The list of fields that can be used to filter enhanced lookups
for an object. Enhanced lookups are optionally enabled by
your administrator.

This field is equivalent to the `Lookup Filter Fields`
related list on the object detail page in the application user
interface.

The list of phone-related fields displayed in a lookup dialog
for the object.

This list enables integration of the fields with a softphone
dial pad.

This field is equivalent to the `Lookup Phone Dialogs`
related list on the object detail page in the application user
interface.

The list of actions that you can use to perform mass quick
action on records. Use this field to add an existing create or
update action.

You can perform mass quick actions on custom objects and
all standard objects that support quick actions and have a

search layout in Lightning Experience. This includes but isn’t
limited to cases, leads, accounts, campaigns, contacts,
opportunities, and work orders.


Metadata Types SearchLayouts

**Field** **Field Type** **Description**

`searchFilterFields` string[]

`searchResultsAdditionalFields` string[]

`searchResultsCustomButtons` string[]

Declarative Metadata Sample Definition

A sample definition of object’s search layout is shown..

```
<?xml version="1.0" encoding="UTF-8"?>

```

The list of fields that can be used to filter a search for the
object.

This field is equivalent to the `Search Filter Fields`
related list on the object detail page in the application user
interface.

The list of fields displayed in a search result for the object.

This field is equivalent to the `Search Results` related
list on the object detail page in the application user interface.

The list of custom buttons available in a search result for the
object. The actions associated with the buttons can be
applied to any of the records returned in the search result.

```
          <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

          . . .

          <searchLayouts>

          <listViewButtons>New</listViewButtons>

          <listViewButtons>Accept</listViewButtons>

          <listViewButtons>ChangeOwner</listViewButtons>

         <lookupDialogsAdditionalFields>firstQuote__c</lookupDialogsAdditionalFields>

         <lookupDialogsAdditionalFields>finalQuote__c</lookupDialogsAdditionalFields>

          <massQuickActions>Create_MQA_Contact</massQuickActions>

         <searchResultsAdditionalFields>CREATEDBY_USER</searchResultsAdditionalFields>

          </searchLayouts>

          . . .

          </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

ProfileSearchLayouts


#### Metadata Types SharingReason SharingReason

Represents an Apex sharing reason, which is used to indicate why sharing was implemented for a custom object. Apex managed sharing
allows developers to use Apex to programmatically share custom objects. When you use Apex managed sharing to share a custom
object, only users with the “Modify All Data” permission can add or change the sharing on the custom object's record, and the sharing
access is maintained across record owner changes.

Use SharingReason to create, update, or delete sharing reason definitions for a custom object. This type extends the Metadata metadata
type and inherits its `fullName` field.

Version

Sharing reasons are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`fullName` string

Required. Sharing reason name. The __c suffix is appended to custom
sharing reasons.

Inherited from Metadata, this field is defined in the WSDL for this
metadata type. It must be specified when creating, updating, or deleting.

See `createMetadata()` to see an example of this field specified for
a call.

`label` string Required. Descriptive label for the sharing reason. Maximum of 40
characters.

Declarative Metadata Sample Definition

The definition of a sharing reason in a custom object:

```
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

. . .

   <sharingReasons>

     <fullName>recruiter__c</fullName>

     <label>Recruiter</label>

   </sharingReasons>

 . . .

</CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types SharingRecalculation SharingRecalculation

Represents Apex classes that recalculate the Apex managed sharing for a specific custom object.

Version

Sharing recalculations are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`className` string

Required. The Apex class that recalculates the Apex sharing for a custom
object. This class must implement the `Database.Batchable`
interface.

Declarative Metadata Sample Definition

The definition of a sharing recalculation in a custom object:

```
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

. . .

   <sharingRecalculations>

     <className>RecruiterRecalculation</className>

   </sharingRecalculations>

 . . .

</CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ValidationRule

Represents a validation rule, which is used to verify that the data a user enters in a record is valid and can be saved. A validation rule
contains a formula or expression that evaluates the data in one or more fields and returns a value of `true` or `false` . Validation rules
also include an error message that your client application can display to the user when the rule returns a value of `true` due to invalid
data.

This type extends the Metadata metadata type and inherits its `fullName` field.

As of API version 20.0, validation rules can't have compound fields. Examples of compound fields include addresses, first and last names,
dependent picklists, and dependent lookups.

As of API version 40.0, you can use validation rules with custom metadata types.


Metadata Types ValidationRule

Version

Validation rules are available in API version 12.0 and later.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Required. Indicates whether this validation rule is active, ( `true` ), or not
active ( `false` ).

`description` string A description of the validation rule.

`errorConditionFormula` string Required. The formula defined in the validation rule. If the formula returns
a value of `true`, an error message is displayed.

`errorDisplayField` string The fully specified name of a field in the application. If a value is supplied,
the error message appears next to the specified field. If you do not specify

a value or the field isn’t visible on the page layout, the value changes
automatically to `Top of Page` .

`errorMessage` string Required. The message that appears if the validation rule fails. The
message must be 255 characters or less.

`fullName` string The internal name of the object. White spaces and special characters are
escaped for validity. The name must:

**•** Contain characters, letters, or the underscore (_) character

**•** Must start with a letter

**•** Can’t end with an underscore

**•** Can't contain two consecutive underscore characters.

Inherited from the Metadata component, this field isn’t defined in the
WSDL for this component. It must be specified when creating, updating,
or deleting. See create() to see an example of this field specified for a call.

Declarative Metadata Sample Definition

A sample XML definition of a validation rule in a custom object is shown in this code block.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <deploymentStatus>Deployed</deploymentStatus>

      <fields>

        <fullName>Mommy_Cat__c</fullName>

        <label>Mommy Cat</label>

        <referenceTo>Cat__c</referenceTo>

        <relationshipName>Cats</relationshipName>

        <type>Lookup</type>

      </fields>

      <label>Cat</label>

      <nameField>

```


#### Metadata Types WebLink

```
        <label>Cat Name</label>

        <type>Text</type>

      </nameField>

      <pluralLabel>Cats</pluralLabel>

      <sharingModel>ReadWrite</sharingModel>

      <validationRules>

        <fullName>CatsRule</fullName>

        <active>true</active>

        <errorConditionFormula>OR(Name = &apos;Milo&apos;,Name =

   &apos;Moop&apos;)</errorConditionFormula>

        <validationMessage>Name must be that of one of my cats</validationMessage>

      </validationRules>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### WebLink

Represents a custom button or link defined in a custom object.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

Version

#### WebLinks are available in API version 12.0 and later.

Fields

**Field Name** **Field Type** **Description**

#### availability WebLinkAvailability Required. Indicates whether the button or link is only available online

(enumeration of type string) ( `online`, or if it is also available offline ( `offline` ).

`description` string A description of the button or link.

#### displayType WebLinkDisplayType Represents how the button or link is rendered. Valid values are:

(enumeration of type string)

**•** `link` for a hyperlink

**•** `button` for a button

**•** `massActionButton` for a button attached to a related list

`encodingKey` Encoding

Required. The default encoding setting is Unicode: `UTF-8` . Change it
if your template requires data in a different format. This is available if
your content source is URL.

Valid values include:


Metadata Types WebLink

**Field Name** **Field Type** **Description**

**•** `UTF-8` —Unicode (UTF-8)

**•** `ISO-8859-1` —General US & Western Europe (ISO-8859–1,
ISO-LATIN-1)

**•** `Shift_JIS` —Japanese (Shift-JIS)

**•** `ISO-2022-JP` —Japanese (JIS)

**•** `EUC-JP` —Japanese (EUC-JP)

**•** `x-SJIS_0213` —Japanese (Shift-JIS_2004)

**•** `ks_c_5601-1987` —Korean (ks_c_5601-1987)

**•** `Big5` —Traditional Chinese (Big5)

**•** `GB2312` —Simplified Chinese (GB2312)

**•** `Big5-HKSCS` —Traditional Chinese Hong Kong (Big5–HKSCS)

`fullName` string The name of the custom button or link with white spaces and special
characters escaped for validity. The name can only contain characters,

letters, and the underscore (_) character. The name must start with a
letter, and can’t end with an underscore or contain two consecutive
underscore characters.

Inherited from the Metadata component, this field isn’t defined in the
WSDL for this component. It must be specified when creating, updating,
or deleting. See create() to see an example of this field specified for a
call.

`hasMenubar` boolean

`hasScrollbars` boolean

`hasToolbar` boolean

`height` int

`isResizable` boolean

`linkType` WebLinkType (enumeration of
type string)

If the `openType` is `newWindow`, this field indicates whether to show
the browser menu bar for the window ( `true` ) or not ( `false` ).
Otherwise, leave this field empty.

If the `openType` is `newWindow`, this field indicates whether to show
the scroll bars for the window ( `true` ) or not ( `false` ). Otherwise, leave
this field empty.

If the `openType` is `newWindow`, this field indicates whether to show
the browser toolbar for the window ( `true` ) or not ( `false` ). Otherwise,
leave this field empty.

Height in pixels of the window opened by the custom button or link.
Required if the `openType` is `newWindow` . Otherwise, leave this field
empty.

If the `openType` is `newWindow`, this field indicates whether to allow
resizing of the window ( `true` ) or not ( `false` ). Otherwise, leave this
field empty.

Required. Represents whether the content of the button or link is
specified by a URL, an sControl, a JavaScript code block, or a Visualforce
page.

**•** `url`


Metadata Types WebLink

**Field Name** **Field Type** **Description**

**•** `sControl`

**•** `javascript`

**•** `page`

**•** `flow` —Reserved for future use.

`masterLabel` string Master label for this object. This display value is the internal label that is
not translated.

`openType` WebLinkWindowType Required. When the button or link is clicked, specifies the window style
(enumeration of type string) that will be used to display the content. Valid values:

**•** `newWindow`

**•** `sidebar`

**•** `noSidebar`

**•** `replace`

**•** `onClickJavaScript`

`page` string If the value of `linkType` is `page`, this field represents the Visualforce
page. Otherwise, leave this field empty.

`position` WebLinkPosition (enumeration
of type string)

If the value of `OpenType` is `newWindow`, this field indicates how
the new window should be displayed. Otherwise, don’t specify a value.
Valid values are:

**•** `fullScreen`

**•** `none`

**•** `topLeft`

`protected` boolean Required. Indicates whether this subcomponent is protected ( `true` )
or not ( `false` ). Protected subcomponents can’t be linked to or

referenced by components or subcomponents created in the installing
organization.

`requireRowSelection` boolean

If the `displayType` is `massActionButton`, this field indicates
whether to require individual row selection to execute the action for
this button ( `true` ) or not ( `false` ). Otherwise, leave this field empty.

`scontrol` string If the value of `linkType` is `sControl`, this field represents the name
of the sControl. Otherwise, leave this field empty.

`showsLocation` boolean

If the `openType` is `newWindow`, this field indicates whether to show
the browser location bar for the window ( `true` ) or not ( `false` ).
Otherwise, leave this field empty.

`showsStatus` boolean If the `openType` is `newWindow`, this field indicates whether to show
the browser status bar for the window. Otherwise, leave this field empty.


Metadata Types WebLink

**Field Name** **Field Type** **Description**

`url` string

`width` int

Java Sample

If the value of `linkType` is `url`, this is the URL value. If the value of
`linkType` is `javascript`, this is the JavaScript content. If the value
is neither of these options, leave this field empty.

Content must be escaped in a manner consistent with XML parsing
rules.

Width in pixels of the window opened by the button or link.

Required if the `openType` is `newWindow` . Otherwise, leave this field
empty.

The following Java sample shows sample values for WebLink fields:

```
public void WebLinkSample(String name) throws Exception {

   WebLink WebLink = new WebLink();

   // name variable represents the full name of the object

   // on which to create the WebLink, for example, customObject__c

   WebLink.setFullName(name + ".googleButton");

   WebLink.setUrl("http://www.google.com");

   WebLink.setAvailability(WebLinkAvailability.online);

   WebLink.setLinkType(WebLinkType.url);

   WebLink.setEncodingKey(Encoding.fromString("UTF-8"));

   WebLink.setOpenType(WebLinkWindowType.newWindow);

   WebLink.setHeight(600);

   WebLink.setWidth(600);

   WebLink.setShowsLocation(false);

   WebLink.setHasScrollbars(true);

   WebLink.setHasToolbar(false);

   WebLink.setHasMenubar(false);

   WebLink.setShowsStatus(false);

   WebLink.setIsResizable(true);

   WebLink.setPosition(WebLinkPosition.none);

   WebLink.setMasterLabel("google");

   WebLink.setDisplayType(WebLinkDisplayType.link);

   AsyncResult[] asyncResults = metadataConnection.create(new WebLink[]{WebLink});

   // After the create() call completes, we must poll the results of checkStatus()

   //

}

```


#### Metadata Types Metadata Field Types

Declarative Metadata Sample Definition

The following is the definition of a WebLink in a custom object. For related samples, see Declarative Metadata Sample Definition and
Declarative Metadata Sample Definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   ....

      <WebLinks>

        <fullName>googleButton</fullName>

        <availability>online</availability>

        <displayType>link</displayType>

        <encodingKey>UTF-8</encodingKey>

        <hasMenubar>false</hasMenubar>

        <hasScrollbars>true</hasScrollbars>

        <hasToolbar>false</hasToolbar>

        <height>600</height>

        <isResizable>true</isResizable>

        <linkType>url</linkType>

        <masterLabel>google</masterLabel>

        <openType>newWindow</openType>

        <position>none</position>

        <protected>false</protected>

        <showsLocation>false</showsLocation>

        <showsStatus>false</showsStatus>

        <url>http://www.google.com</url>

        <width>600</width>

      </WebLinks>

   ....

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

HomePageComponent

HomePageLayout

CustomPageWebLink

#### Metadata Field Types

These field types extend the field types described in the _Salesforce Object Reference_ .

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types Metadata Field Types

**Field Type** **Objects** **What the Field Contains**

CustomField

Custom object Represents a custom field.

Custom field

DeleteConstraint Custom field A string that represents deletion options for lookup relationships. Valid values
are:

**•** `SetNull`

**•** `Restrict`

**•** `Cascade`

DeploymentStatus

Custom object

Custom field

A string that represents the deployment status of a custom object or field. Valid
values are:

**•** `InDevelopment`

**•** `Deployed`

FieldType Custom field Indicates the type of a custom field. Valid values are:

**•** `Address`

**•** `AutoNumber`

**•** `Lookup`

**•** `MasterDetail`

**•** `MetadataRelationship`

**•** `Checkbox`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Email`

**•** `EncryptedText`

Note: This page is about Classic Encryption, not Shield Platform
[Encryption. What's the difference?](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_vs_classic_encryption.htm&type=5&language=en_US)

**•** `ExternalLookup`

**•** `IndirectLookup`

**•** `Number` [1]

**•** `Percent`

**•** `Phone`

**•** `Picklist`

**•** `MultiselectPicklist`

**•** `Summary`

**•** `Text`

**•** `TextArea`

**•** `LongTextArea`


Metadata Types Metadata Field Types

**Field Type** **Objects** **What the Field Contains**

**•** `Url`

**•** `Hierarchy`

**•** `File`

**•** `Html`

**•** `Location` (use for geolocation fields)

**•** `Time`

**•** `Array`

**•** `Integer`

**•** `Long`

A `Number` custom field, internally represented as a field of type double. Setting
the scale of the `Number` field to 0 gives you a double that behaves like an int.

Gender Custom object

Picklist (Including Dependent Custom field
Picklist)

Indicates the gender of the noun that represents the object. Used for languages
where words need different treatment depending on their gender. Valid values
are:

**•** `Masculine`

**•** `Feminine`

**•** `Neuter`

**•** `AnimateMasculine` (Slavic languages—currently Czech, Polish, Russian,
Slovak, Slovenian, and Ukrainian)

**•** `ClassI`, `ClassIII`, `ClassV`, `ClassVII`, `ClassIX`, `ClassXI`,
`ClassXIV`, `ClassXV`, `ClassXVI`, `ClassXVII`, `ClassXVIII`
(African languages—currently Afrikaans, Xhosa, and Zulu)

Note: The following genders appear on the Rename Tabs and Labels
page in Setup but are stored internally as “Feminine”. When setting them
through the Metadata API, use “Feminine”.

**•** `Euter (Swedish)`

**•** `Common (Dutch)`

(This field type isn’t used in Metadata API. CustomField includes this field type for
Tooling API support). Represents a picklist, a set of labels and values that can be
selected from a picklist.

SharingModel Custom object Represents the sharing model for the custom object. Depending on the object,
valid values are:

**•** `Private`

**•** `Read`

**•** `ReadWrite`

**•** `ReadWriteTransfer`

**•** `FullAccess`

**•** `ControlledByParent`


Metadata Types Metadata Field Types

**Field Type** **Objects** **What the Field Contains**

**•** `ControlledByCampaign`

**•** `ControlledByLeadOrContact`

For example, the User object supports `Private` and `Read` values. Accounts,
opportunities, and custom objects support `Private`, `Read` and `ReadWrite`
values. Campaign members support `ControlledByCampaign` and
`ControlledByLeadOrContact` .

StartsWith

Custom object

Custom field

Indicates whether the noun starts with a vowel, consonant, or is a special character.
This is used for languages where words need different treatment depending on
the first character. Valid values are:

**•** `Consonant`

**•** `Vowel`

**•** `Special (for nouns starting with z, or s plus`

```
  consonants)

```

TreatBlanksAs Custom field Indicates how blanks should be treated. Valid values are:

**•** `BlankAsBlank`

**•** `BlankAsZero`

ValueSet Custom field Represents a set of values that can be selected from a custom picklist field. Defines
the valueSet of a custom picklist field.

ValueSet

Represents a set of values that can be selected from a custom picklist field. Defines the valueSet of a custom picklist field.

**Field Type** **Field Type** **Description**

`controllingField` string

The `fullname` of the controlling field if this is a dependent picklist. A
controlling field can be a checkbox or picklist field, but in this case it’s a picklist.
The controlling picklist filters the available values in the dependent picklist.

`restricted` boolean Whether the picklist’s values are limited to only the values defined by a
Salesforce admin. Values are `true` or `false` .

`valueSetDefinition` ValueSetValuesDefinition Defines value-specific settings for a custom dependent picklist. Indicates
whether the value set of the custom picklist field is sorted alphabetically.

`valueSetName` string The `masterLabel` of the global value set to be used for this picklist field.

`valueSettings` ValueSettings Used for the settings that describe a value in a custom picklist field. The picklist
can have its own unique value set, or inherit the values from a global value

set. You can add field dependency values via the Metadata API but not remove
them.


### Metadata Types CustomObjectTranslation

ValueSetValuesDefinition

**Field Name** **Field Type** **Description**

`sorted` boolean Whether the picklist’s value set is displayed in alphabetical order in the user
interface.

`value` CustomValue Required. The list of values for this local, custom picklist.

ValueSettings

**Field Name** **Field Type** **Description**

`controllingFieldValue` stringstring[]

Applies only to dependent custom picklists. A list of values in the controlling
or parent picklist (that the custom picklist values depend on). You can add field
dependency values via the Metadata API but not remove them.

`valueName` string Defines the values in the custom dependent picklist.

### CustomObjectTranslation

This metadata type allows you to translate custom objects for a variety of languages.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field. The ability to translate component labels is part of the
Translation Workbench.

Declarative Metadata File Suffix and Directory Location

Local translations are stored in a file with a format of _`customObjectName__c`_ `-` _`lang`_ `.objectTranslation`, where
_`customObjectName__c`_ is the custom object name, and _`lang`_ is the translation language. A sample file name for German
translations is `myCustomObject__c-de.objectTranslation` .

Similarly, packaged translations are stored in a file with a format of
_`customObjectName-pkgNamespace__c`_ `-` _`lang`_ `.objectTranslation`, where
_`customObjectName-pkgNamespace__c`_ is the custom object and package namespace, and _`lang`_ is the translation language.
A sample file name for German translations in a package with the namespace of Acme is
`myCustomObject-Acme__c-de.objectTranslation` . Custom object translations are stored in the objectTranslations
folder in the corresponding package directory.

Custom object translations are stored in the `objectTranslations` folder in the corresponding package directory.

Version

### CustomObjectTranslation components are available in API version 14.0 and later.


Metadata Types CustomObjectTranslation

Fields

**Field** **Field Type** **Description**

`caseValues` ObjectNameCaseValue[] Different combinations of the custom object with regard to
article, plural, possessive, and case.

`fields` CustomFieldTranslation[] A list of translations for the custom fields associated with the
custom object.

`fieldSets` FieldSetTranslation[] A list of field set translations. Available in API version 41.0 and
later.

`fullName` string The name of the custom object and the translation language
with a format of _`customObjectName`_                                         - _`lang`_, where

_`customObjectName`_ is the custom object name, and _`lang`_
is the translation language.

Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating, updating,
or deleting. See `createMetadata()` to see an example of
this field specified for a call.

`gender` Gender

Indicates the gender of the noun that represents the object.
Used for languages where words need different treatment
depending on their gender.

`layouts` LayoutTranslation[] A list of page layout translations.

`nameFieldLabel` string The label for the name field. Maximum of 80 characters.

`namedFilters` NamedFilterTranslation[]

A list of translations for lookup filter error messages associated
with the custom object.

This field has been removed as of API version 30.0 and is only
available in prior versions. The translation metadata associated

with a lookup filter is now represented by the `lookupFilter`
field in the CustomFieldTranslation on page 812 subtype.

`quickActions` QuickActionTranslation[] A list of translations for actions.

`recordTypes` RecordTypeTranslation[] A list of record type translations.

`sharingReasons` SharingReasonTranslation[] A list of sharing reason translations.

`startsWith` StartsWith (enumeration of type
string)

Indicates whether the noun starts with a vowel, consonant, or
is a special character. This is used for languages where words
need different treatment depending on the first character.

`validationRules` ValidationRuleTranslation[] A list of validation rule translations.

`webLinks` WebLinkTranslation[] A list of web link translations.

`workflowTasks` WorkflowTaskTranslation[] A list of workflow task translations.


Metadata Types CustomObjectTranslation

Note: When you retrieve or deploy translations from a package, the translations from the package might override existing
translations. The overridden translations appear in the Rename Tabs and Labels UI until you click **Reset** to restore the translations
installed by the latest package.

CustomFieldTranslation

CustomFieldTranslation contains details for a custom field translation. In API versions 37.0 and earlier standard picklist values could be
translated with CustomFieldTranslation. In API version 38.0, use StandardValueSetTranslation instead. For more details, see CustomField.

Note: Not every language supports all the possible values for the fields in CustomFieldTranslation. For language-specific supported
values, see the fully supported languages and end-user languages appendices.

**Field** **Field Type** **Description**

`caseValues` ObjectNameCaseValue[]

Different combinations of the custom object with regard to
article, plural, possessive, and case. Available in API version 29.0
and later.

`description` string Translation for the custom field description.

`gender` Gender Available in API version 29.0 and later.

`help` string Translation for the text that displays in the field-level help hover
text for this field.

`label` string Translation for the label. Maximum of 40 characters.

`lookupFilter` LookupFilterTranslation

Represents the translation metadata associated with a lookup
filter.

This field is available in API version 30.0 and later.

LookupFilter isn’t supported on the article type object.

`name` string Required. The name of the field relative to the custom object;
for example, `MyField__c` .

`picklistValues` PicklistValueTranslation[]

List of translations for picklist values. See PicklistValue.

Note: “Subject” on the Task object is a text field, not a picklist
value. It can’t be retrieved via Metadata API. Translations can be
provided via the Translation Workbench.

`relationshipLabel` string Translation for a lookup relationship label. A lookup relationship
allows a field to be associated with another field. The relationship

field allows users to select an option from a list of values defined
by the other field. Maximum of 80 characters.

`startsWith` StartsWith (enumeration of type Indicates whether the noun starts with a vowel, consonant, or
string) is a special character. Used for languages where words need

different treatment depending on the first character. Available
in API version 29.0 and later.


Metadata Types CustomObjectTranslation

FieldSetTranslation

FieldSetTranslation contains details for a field set translation. For more details, see FieldSet. Available in API 41.0 and later.

**Field** **Field Type** **Description**

`label` string Required. Translation for the field set label. Maximum of 80
characters.

`name` string Required. The field set name.

LayoutTranslation

LayoutTranslation contains details for a page layout translation. For more details, see Fields.

**Field** **Field Type** **Description**

`layout` string Required. The layout name.

`layoutType` string

`sections` LayoutSectionTranslation[] An array of layout section translations.

LayoutSectionTranslation

LayoutSectionTranslation contains details for a page layout section translation. For more details, see LayoutSection.

**Field** **Field Type** **Description**

`label` string Required. Translation for the label. Maximum of 765 characters.

`section` string Required. The section name.

LookupFilterTranslation

LookupFilterTranslation shows a translation for a lookup filter error message associated with the custom object. Replaces
NamedFilterTranslation.

LookupFilterTranslation is available in API version 30.0 and later.

**Field** **Field Type** **Description**

`errorMessage` string The error message that appears if the lookup filter fails.

`informationalMessage` string

The information message displayed on the page. Use to describe
things some users don't understand, such as why certain items
are excluded in the lookup filter.


Metadata Types CustomObjectTranslation

NamedFilterTranslation

NamedFilterTranslation has been removed as of API version 30.0 and is only available in previous API versions.

NamedFilterTranslation shows a list of translations for lookup filter error messages associated with the custom object. See NamedFilter
for more information.

**Field** **Field Type** **Description**

`errorMessage` string The error message that appears if the lookup filter fails.

`informationalMessage` string

The information message displayed on the page. Use to describe
things the user doesn’t understand, such as why certain items
are excluded in the lookup filter.

`name` string Required. The name of the lookup filter. If you create this field
in the user interface, a name is automatically assigned. If you

create this field through Metadata API, you must include the
`name` field.

ObjectNameCaseValue

ObjectNameCaseValue supports multiple cases and definitions of the custom object name to allow usage in various grammatical contexts.

Note: Not every language supports all the possible values for the fields in ObjectNameCaseValue. For language-specific supported
values, see the fully supported languages and end-user languages appendices.

**Field** **Field Type** **Description**

`article` Article (enumeration of type English has two types of articles: definite ( _`the`_ ) and indefinite
string) ( _`a`_, _`an`_ ). The usage of these articles depends mainly on whether

you're referring to any member of a group, or to a specific
member of a group. The valid values are:

**•** `Definite`

**•** `Indefinite`

**•** `None`

`caseType` CaseType (enumeration of type The case of the custom object name. The valid values are:
string)

**•** `Ablative`

**•** `Accusative`

**•** `Adessive`

**•** `Allative`

**•** `Causalfinal`

**•** `Dative`

**•** `Delative`

**•** `Distributive`

**•** `Elative`

**•** `Essive`


Metadata Types CustomObjectTranslation

**Field** **Field Type** **Description**

**•** `Essiveformal`

**•** `Genitive`

**•** `Illative`

**•** `Inessive`

**•** `Instrumental`

**•** `Lative`

**•** `Locative`

**•** `Nominative`

**•** `Objective`

**•** `Partitive`

**•** `Prepositional`

**•** `Subjective`

**•** `Sublative`

**•** `Superessive`

**•** `Termanative`

**•** `Translative`

**•** `Vocative`

`plural` boolean Indicates whether the `value` field is plural ( `true` ) or singular
( `false` ).

`possessive` Possessive (enumeration of type The possessive case of a language is a grammatical case used
string) to indicate a relationship of possession. The valid values are:

**•** `First`

**•** `None`

**•** `Second`

`value` string Required. The value or label in this grammatical context.

PicklistValueTranslation

PicklistValueTranslation contains details for translation of a picklist value from a local, custom picklist field. For more details, see Picklist
(Including Dependent Picklist).

**Field** **Field Type** **Description**

`masterLabel` string Required. The picklist value defined on the setup page in the
application. Displayed wherever a translated label isn't available.

`translation` string Required. Translation for the value.


Metadata Types CustomObjectTranslation

QuickActionTranslation

QuickActionTranslation contains details for an action label in the user interface. For more information, see QuickAction.

**Field** **Field Type** **Description**

`aspect` string Identifies which quick action label the translated text belongs
to. Use this field only when you want to use different strings for

the quick action's field label and informational message. Valid
values are `Master` and `InfoMessage` . Available in API
version 53.0 and later.

`label` string Required. Translation for the label. Maximum of 765 characters.

`name` string Required. The quick action name.

RecordTypeTranslation

RecordTypeTranslation contains details for a record type name translation. For more details, see RecordType.

**Field** **Field Type** **Description**

`label` string Required. Translation for the label. Maximum of 765 characters.

`name` string Required. The record type name.

`description` string Translation for the record type description. Available in API
version 42.0 and later.

SharingReasonTranslation

SharingReasonTranslation contains details for a sharing reason translation. For more details, see SharingReason.

**Field** **Field Type** **Description**

`label` string Required. Translation for the sharing reason.

`name` string Required. The sharing reason name.

ValidationRuleTranslation

ValidationRuleTranslation contains details for a validation rule translation. For more details, see ValidationRule.

**Field** **Field Type** **Description**

`errorMessage` string Required. Translation for the error message associated with the
validation rule failure.

`name` string Required. The validation rule name.


Metadata Types CustomObjectTranslation

WebLinkTranslation

WebLinkTranslation contains details for a web link translation. For more details, see WebLink.

**Field** **Field Type** **Description**

`label` string Required. Translation for the web link label. Maximum of 765
characters.

`name` string Required. The web link name.

WorkflowTaskTranslation

WorkflowTaskTranslation contains details for a workflow task translation. For more details, see Workflow.

**Field** **Field Type** **Description**

`description` string Translation for the workflow task description.

`name` string Required. The workflow task name.

`subject` string Translation for the workflow task subject.

Declarative Metadata Sample Definitions

This sample XML definition shows a CustomObjectTranslation for the Description__c object in German, with one custom field, Summary__c.
The name and location of the file containing this definition would be
`objectTranslations/Description__c-de.objectTranslation` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObjectTranslation xmlns="http://soap.sforce.com/2006/04/metadata">

      <caseValues>

        <caseType>Nominative</caseType>

        <plural>false</plural>

        <value>Beschreibung</value>

      </caseValues>

      <caseValues>

        <caseType>Nominative</caseType>

        <plural>true</plural>

        <value>Beschreibungen</value>

      </caseValues>

      <caseValues>

        <caseType>Accusative</caseType>

        <plural>false</plural>

        <value>Beschreibung</value>

      </caseValues>

      <caseValues>

        <caseType>Accusative</caseType>

        <plural>true</plural>

        <value>Beschreibungen</value>

      </caseValues>

      <caseValues>

```


Metadata Types CustomObjectTranslation

```
        <caseType>Genitive</caseType>

        <plural>false</plural>

        <value>Beschreibung</value>

      </caseValues>

      <caseValues>

        <caseType>Genitive</caseType>

        <plural>true</plural>

        <value>Beschreibungen</value>

      </caseValues>

      <caseValues>

        <caseType>Dative</caseType>

        <plural>false</plural>

        <value>Beschreibung</value>

      </caseValues>

      <caseValues>

        <caseType>Dative</caseType>

        <plural>true</plural>

        <value>Beschreibungen</value>

      </caseValues>

      <fields>

        <label>Zusammenfassung</label>

        <name>Summary__c</name>

      </fields>

      <gender>Feminine</gender>

      <nameFieldLabel>Beschreibungen</nameFieldLabel>

   </CustomObjectTranslation>

```

This sample XML definition shows a CustomObjectTranslation for the Account object, renaming Account to Client (Kunde) in German.
The Account object has one standard field, account_number, and one custom field, Account_Code__c. The name and location of the
file containing this definition would be `objectTranslations/Account-de.objectTranslation` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObjectTranslation xmlns="http://soap.sforce.com/2006/04/metadata">

      <caseValues>

        <caseType>Nominative</caseType>

        <plural>false</plural>

        <value>Kunde</value>

      </caseValues>

      <caseValues>

        <caseType>Nominative</caseType>

        <plural>true</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Accusative</caseType>

        <plural>false</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Accusative</caseType>

        <plural>true</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Genitive</caseType>

```


Metadata Types CustomObjectTranslation

```
        <plural>false</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Genitive</caseType>

        <plural>true</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Dative</caseType>

        <plural>false</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Dative</caseType>

        <plural>true</plural>

        <value>Kunden</value>

      </caseValues>

      <fields>

        <caseValues>

           <caseType>Nominative</caseType>

           <plural>false</plural>

           <value>Kundennummer</value>

        </caseValues>

        <caseValues>

           <caseType>Nominative</caseType>

           <plural>true</plural>

           <value>Kundennummern</value>

        </caseValues>

        <gender>Feminine</gender>

        <name>account_number</name>

      </fields>

      <fields>

        <label>Kunden-Code</label>

        <name>Account_Code__c</name>

      </fields>

      <gender>Masculine</gender>

   </CustomObjectTranslation>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

Translations


### Metadata Types CustomPageWebLink CustomPageWebLink

Represents a custom link defined in a home page component.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

All other custom links are stored as a WebLink in a CustomObject.

Declarative Metadata File Suffix and Directory Location

There is one file per custom link definition, stored in the `weblinks` folder in the corresponding package directory. The file suffix is
`.weblink` .

Version

### CustomPageWebLinks are available in API version 13.0 and later.

Fields

**Field Name** **Field Type** **Description**

`availability` WebLinkAvailability Required. Indicates whether the link is only available online ( `online`,
(enumeration of type string) or if it is also available offline ( `offline` ).

`description` string A description of the link.

`displayType` WebLinkDisplayType
(enumeration of type string)

`encodingKey` Encoding (enumeration of type
string)

Represents how this link is rendered.

Valid values:

**•** `link` for a hyperlink

**•** `button` for a button

**•** `massActionButton` for a button attached to a related list

Required. The default encoding setting is Unicode: `UTF-8` . Change it if
your template requires data in a different format. This is available if your
content source is URL. Valid values include:

**•** `UTF-8` —Unicode (UTF-8)

**•** `ISO-8859-1` —General US & Western Europe (ISO-8859–1,
ISO-LATIN-1)

**•** `Shift_JIS` —Japanese (Shift-JIS)

**•** `ISO-2022-JP` —Japanese (JIS)

**•** `EUC-JP` —Japanese (EUC-JP)

**•** `x-SJIS_0213` —Japanese (Shift-JIS_2004)

**•** `ks_c_5601-1987` —Korean (ks_c_5601-1987)

**•** `Big5` —Traditional Chinese (Big5)


Metadata Types CustomPageWebLink

**Field Name** **Field Type** **Description**

**•** `GB2312` —Simplified Chinese (GB2312)

**•** `Big5-HKSCS` —Traditional Chinese Hong Kong (Big5–HKSCS)

`fullName` string The name used as a unique identifier for API access. The `fullName`
can contain only underscores and alphanumeric characters. It must be

unique, begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores.

`hasMenubar` boolean

`hasScrollbars` boolean

`hasToolbar` boolean

If the `openType` is `newWindow`, this field indicates whether to show
the browser menu bar for the window ( `true` or not ( `false` ). Otherwise,
leave this field empty.

If the `openType` is `newWindow`, this field indicates whether to show
the scroll bars for the window ( `true` ) or not ( `false` ). Otherwise, leave
this field empty.

If the `openType` is `newWindow`, this field indicates whether to show
the browser toolbar for the window ( `true` ) or not ( `false` ). Otherwise,
leave this field empty.

`height` int Height in pixels of the window opened by the link. Required if the
`openType` is `newWindow` . Otherwise, leave this field empty.

`isResizable` boolean

If the `openType` is `newWindow`, this field indicates whether to allow
resizing of the window ( `true` ) or not ( `false` ). Otherwise, leave this
field empty.

`linkType` WebLinkType (enumeration of Required. Represents whether the content of the button or link is specified
type string) by a URL, an sControl, a JavaScript code block, or a Visualforce page.

**•** `url`

**•** `sControl`

**•** `javascript`

**•** `page`

**•** `flow` —Reserved for future use.

`masterLabel` string The label for the link.

`openType` WebLinkWindowType
(enumeration of type string)

Required. When the link is clicked, this field specifies the window style
used to display the content.

Valid values are:

**•** `newWindow`

**•** `sidebar`

**•** `noSidebar`

**•** `replace`

**•** `onClickJavaScript`


Metadata Types CustomPageWebLink

**Field Name** **Field Type** **Description**

`page` string If the value of `linkType` is `page`, this field represents the Visualforce
page. Otherwise, leave this field empty.

`position` WebLinkPosition (enumeration
of type string)

`protected` boolean

`requireRowSelection` boolean

If the `openType` is `newWindow`, this field indicates how the new
window should be displayed. Otherwise, leave this field empty.

Valid values are:

**•** `fullScreen`

**•** `none`

**•** `topLeft`

Required. Indicates whether this component is protected ( `true` ) or not
( `false` ). Protected components cannot be linked to or referenced by
components created in the installing organization.

If the `openType` is `massAction`, this field indicates whether to
require individual row selection to execute the action for this button
( `true` ) or not ( `false` ). Otherwise, leave this field empty.

`scontrol` string If the value of `linkType` is `sControl`, this field represents the name
of the sControl. Otherwise, leave this field empty.

`showsLocation` boolean

`showsStatus` boolean

`url` string

`width` int

If the `openType` is `newWindow`, this field indicates whether or not
to show the browser location bar for the window. Otherwise, leave this
field empty.

If the `openType` is `newWindow`, this field indicates whether or not
to show the browser status bar for the window. Otherwise, leave this field
empty.

If the value of `linkType` is `url`, this field represents the URL value. If
the value of `linkType` is `javascript`, this field represents the
JavaScript content. If the value is neither of these, leave this field empty.

Content must be escaped in a manner consistent with XML parsing rules.

Width in pixels of the window opened by the link.

Required if the `openType` is `newWindow` . Otherwise, leave this field
empty.

Declarative Metadata Sample Definition

The following is the definition of a Weblink. For related samples, see HomePageComponent and HomePageLayout.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomPageWebLink xmlns="http://soap.sforce.com/2006/04/metadata">

   <availability>online</availability>

   <displayType>button</displayType>

   <encodingKey>UTF-8</encodingKey

```


### Metadata Types CustomPermission

```
      <hasMenubar>false</hasMenubar>

      <hasScrollbars>true</hasScrollbars>

      <hasToolbar>false</hasToolbar>

      <height>600</height>

      <isResizable>true</isResizable>

      <linkType>url</linkType>

      <masterLabel>detailPageButon</masterLabel>

      <openType>newWindow</openType>

      <position>none</position>

      <protected>false</protected>

      <showsLocation>false</showsLocation>

      <showsStatus>false</showsStatus>

      <url>http://google.com</url>

   </CustomPageWebLink>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

HomePageComponent

HomePageLayout

WebLink

### CustomPermission

Represents a permission that grants access to a custom feature.This type extends the Metadata metadata type and inherits its `fullName`
field.

File Suffix and Directory Location

### CustomPermission components have the suffix .customPermission and are stored in the customPermissions folder.

Version

### CustomPermission components are available in API version 31.0 and later.

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets


Metadata Types CustomPermission

Fields

**Field Name** **Field Type** **Description**

`connectedApp` string

The name of the connected app that’s
associated with this permission. Limit: 80
characters.

`description` string The custom permission description. Limit:
255 characters.

`isLicensed` boolean Required. Read-only. Indicates whether the
appropriate Salesforce license is required

before accessing the permission ( `true` ) or
not ( `false` ).

`label` string Required. The custom permission label.
Limit: 80 characters.

`requiredPermission` CustomPermissionDependencyRequired[] Indicates which custom permissions are
required by the parent custom permission.

This field is available in API version 32.0 and
later.

CustomPermissionDependencyRequired

CustomPermissionDependencyRequired determines whether a custom permission is required by the parent custom permission. A
required custom permission must be enabled when its parent is enabled.

**Field Name** **Field Type** **Description**

`customPermission` string Required. The custom permission name.

`dependency` boolean Required. Indicates whether this custom permission is required by the
parent custom permission ( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of a CustomPermission component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomPermission xmlns="http://soap.sforce.com/2006/04/metadata">

  <connectedApp>Acme</connectedApp>

  <description>Read and edit access for Acme accounts.</description>

  <label>Acme Account Full Access</label>

  <requiredPermission>

    <customPermission>Acme_Account_Read</customPermission>

    <dependency>true</dependency>

  </requiredPermission>

</CustomPermission>

```


### Metadata Types CustomSite

The following is an example `package.xml` that references the previous definition, as well as other custom permissions that are
associated with a connected app.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>Acme</members>

       <name>ConnectedApp</name>

     </types>

     <types>

       <members>Acme_Account_Email_Read</members>

       <members>Acme_Account_Phone_Edit</members>

       <members>Acme_Account_Full_Access</members>

       <members>Acme_Account_Read</members>

       <name>CustomPermission</name>

     </types>

     <types>

       <members>Acme_Account_Email_Read</members>

       <members>Acme_Account_Phone_Edit</members>

       <members>Acme_Account_Full_Access</members>

       <members>Acme_Account_Read</members>

       <name>PermissionSet</name>

     </types>

     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomSite

Represents a Salesforce site. Create public websites and applications that are directly integrated with your Salesforce organization, but
don't require users to log in with a username and password.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

[This Metadata API Type applies only to Salesforce sites and Visualforce sites. For Digital Experiences, also known as Experience Cloud](https://help.salesforce.com/s/articleView?id=experience.exp_cloud_basics_glossary.htm&type=5&language=en_US)
[sites, see Network.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_network.htm)

[For more information, see Salesforce Sites in Salesforce Help. This type extends the Metadata metadata type and inherits its](https://help.salesforce.com/s/articleView?id=platform.sites_overview.htm&type=5&language=en_US) `fullName`
field.

Note: CustomSite doesn’t currently support syndication feeds.

Declarative Metadata File Suffix and Directory Location

Lightning Platform CustomSite components are stored in the `sites` directory of the corresponding package directory. The file name
matches the site name, and the extension is `.site` .


Metadata Types CustomSite

Version

Lightning Platform CustomSite components are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`active` boolean Required. Determines whether the site is active.

`allowHomePage` boolean

`allowStandardAnswersPages` boolean

`allowStandardIdeasPages` boolean

`allowStandardLookups` boolean

Required. Determines whether the standard home
page is visible to public users. This field is available in
API version 15.0 and later.

Determines whether the standard answer pages are
visible to public users. This field is available in API
version 19.0 and later.

Required. Determines whether the standard Ideas
pages are visible to public users. This field is available
in API version 15.0 and later.

Required. Determines whether the standard lookup
pages are visible to public users. This field is available
in API version 15.0 and later.

`allowStandardPortalPages` boolean Required. When enabled, authenticated users in this
site can access standard Salesforce pages as allowed

by their access controls. When disabled, authenticated
users in this site can't access standard Salesforce
pages, even if their access controls allow it. If your site
serves only Visualforce pages, disabling this setting
helps add a layer of access protection to your site. This
field is available in API version 39.0 and later.

`allowStandardSearch` boolean

Required. Determines whether the standard search
pages are visible to public users. This field is available
in API version 15.0 and later.

`analyticsTrackingCode` string The tracking code associated with your site. Services
such as Google Analytics can use this code to track

page request data for your site. This field is available
in API version 17.0 and later.

`authorizationRequiredPage` string

The name of the Visualforce page to display when the
guest user tries to access a page for which they aren’t
authorized.

`bandwidthExceededPage` string The name of the Visualforce page to display when the
site has exceeded its bandwidth quota.

`browserXssProtection` boolean Required. Determines whether protection against
reflected cross-site scripting attacks is enabled. If a


Metadata Types CustomSite

**Field** **Field Type** **Description**

reflected cross-site scripting attack is detected, the
browser shows a blank page with no content.
Available in API version 41.0 and later.

`cachePublicVisualforcePagesInProxyServers` boolean Indicates whether proxy servers cache this site’s
publicly available pages only for unauthenticated

guest users ( `true` ) or not ( `false` ). When this field
is `false`, this site’s cache-enabled Visualforce pages
are cached in the web browser for both authenticated
and unauthenticated users. The default is `true` . See
[Configure Site Caching in Salesforce Help for more](https://help.salesforce.com/articleView?id=platform.sites_caching.htm&type=5&language=en_US)
information.

This field is available in API version 52.0 and later.

`changePasswordPage` string

The name of the Visualforce page to display when the
portal user attempts to change their password for
either the portal or for Chatter Answers, when enabled.

`chatterAnswersForgotPasswordConfirmPage` string The name of the Visualforce page that informs the
user that an email has been sent to them with a

temporary password. This field is available if Chatter
Answers is enabled for your organization. This field is
available in API version 27.0 and later.

`chatterAnswersForgotPasswordPage` string The name of the Visualforce page to display when a
user clicks the link to retrieve a forgotten password.

This field is available if Chatter Answers is enabled for
your organization. This field is available in API version
27.0 and later.

`chatterAnswersHelpPage` string The name of the Visualforce page to display when the
user clicks the help link. This field is available if Chatter

Answers is enabled for your organization. This field is
available in API version 27.0 and later.

`chatterAnswersLoginPage` string The name of the Visualforce page to display where
users can log in to the portal. This field is available if

Chatter Answers is enabled for your organization. This
field is available in API version 27.0 and later.

`chatterAnswersRegistrationPage` string

The name of the Visualforce page to display where
users can register themselves and access the portal.
This field is available in API version 27.0 and later.

```
clickjackProtectionLevel

```

SiteClickjackProtectionLevel Required. Sets the clickjack protection level. The
(enumeration of type options are:
string)

**•** `AllowAllFraming`           - Allow framing by any
page (no protection)


Metadata Types CustomSite

**Field** **Field Type** **Description**

**•** `External`                                 - Allow framing of site or
Experience Cloud site pages on external domains
(good protection)

**•** `SameOriginOnly`                                 - Allow framing by the
same origin only (recommended)

**•** `NoFraming`                                 - Don’t allow framing by any
page (most protection)

This field is available in API version 30.0 and later.

`contentSniffingProtection` boolean Required. Determines whether the browser is
prevented from inferring the MIME type from the

document content. If enabled, it also prevents the
browser from executing some malicious files
(JavaScript, Stylesheet) as dynamic content. This field
is available in API version 41.0 and later.

`cspUpgradeInsecureRequests` boolean

This field is removed in API version 52.0 and later. In
API version 51.0 and earlier, the value in the field is
ignored.

`customWebAddresses` SiteWebAddress[] The root custom URLs associated with the site. Saving
or deploying a CustomSite replaces all root custom

URLs in the site with the root custom URLs in this list.
Custom URLs that use a non-root path prefix aren’t
included in this list and aren’t affected when saving
or deploying a CustomSite. This field is available in API
version 21.0 and later.

`description` string The site description.

`enableAuraRequests` boolean Determines whether guest users can view features
available only in Lightning ( `true` ). If set to `false`,

Lightning features don’t load. This field is available in
API version 46.0 and later.

`favoriteIcon` string

The name of the static resource, without the extension,
for the icon that appears in next to the site’s name in
browser tabs, bookmarks, and search results.

To update a site’s favorite icon, create a 16px by 16px
ICO file. Then store that images a static resource at

the base path for the site. For example, if the icon file
name is favico.ico,

```
https:// myDomainName .my.site.com/store/favicon.ico
```

is the required path for a site with the URL
`https://` _**`myDomainName`**_ `.my.site.com/store` .
To use that icon, set `favoriteIcon` to `favicon` .


Metadata Types CustomSite

**Field** **Field Type** **Description**

If the specified the ICO file doesn’t exist in the required
location, a 404 error is returned. Otherwise, if the file
isn’t present, no favorite icon is used.

`fileNotFoundPage` string The name of the Visualforce page to display when the
guest user tries to access a non-existent page.

`forgotPasswordPage` string The name of the Visualforce page to display when a
user clicks the Forgot Password link on the site’s login

page. This field is only applicable for Experience Cloud
sites.

`genericErrorPage` string The name of the Visualforce page to display for errors
not otherwise specified.

`guestProfile` string Read only. The name of the profile associated with
the guest user.

`inMaintenancePage` string The name of the Visualforce page to display when the
site is down for maintenance.

`inactiveIndexPage` string The name of the Visualforce page set as the inactive
site home page.

`indexPage` string Required. The name of the Visualforce page set as the
active site home page.

`masterLabel` string Required. The name of the site label in the Salesforce
user interface.

`myProfilePage` string The name of the Visualforce page to display as the
site user’s profile page, where users can update their

contact information. This field is available in API
version 20.0 and later.

`portal` string The name of the portal associated with this site for
login access.

`redirectToCustomDomain` boolean Indicates whether requests for this site’s
system-managed URLs are redirected to the HTTPS

custom domain serving this site ( `true` ) or not
( `false` ). System-managed site URLs end in
`*.my.salesforce-sites.com` or
`*.my.site.com` . In Experience Cloud sites, the
default is `false` . In Salesforce Sites, the default is
`true` .

If multiple custom domains serve this site and this
field is set to `true`, requests are routed to the site’s
primary custom URL only if it’s an HTTPS custom
domain. Otherwise, requests are redirected to the first
HTTPS custom domain associated with this site, in


Metadata Types CustomSite

**Field** **Field Type** **Description**

alphanumeric order. If no HTTPS custom domain
serves this site, this option has no effect.

This field is available in API version 52.0 and later.

`referrerPolicyOriginWhenCrossOrigin` boolean Required. Determines whether the referrer header
shows only Salesforce.com rather than the entire URL

when loading a page. This feature eliminates the
potential for a referrer header to reveal sensitive
information that could be present in a full URL, such
as an org ID. This field is available in API version 41.0
and later.

`requireHttps` boolean

This field is removed in API version 52.0 and later. In
API version 51.0 and earlier, the value in the field is
ignored.

`requireInsecurePortalAccess` boolean Determines whether to override your organization's
security settings and exclusively use HTTP when

logging in to the associated portal from your site.
Removed in API version 50.0 and later.

`robotsTxtPage` string The name of the Visualforce page to display for the
`robots.txt` file used by web crawlers.

`selfRegPage` string Visualforce page used for self-registration.

`serverIsDown` string The name of the static resource to be displayed from
the cache server when Salesforce servers are down.

The static resource must be a public zip file 1 MB or
smaller and must contain a page named
`maintenance.html` at the root level of the zip
file. Other resources in the zip file, such as images or
CSS files, can follow any directory structure. This field
is available in API version 17.0 and later.

`siteAdmin` string The username of the site administrator.

`siteGuestRecordDefaultOwner` string

`siteIframeWhiteListUrls` SiteIframeWhiteListUrl[]

The username of the user who owns all new records
that unauthenticated guest users create. This field is
available in API version 51.0 and later.

The list of external domains that you allow to frame
your Salesforce site. This field is available in API 49.0
and later.

`siteRedirectMappings` SiteRedirectMapping[] An array of all URL redirect rules set for your site. This
field is available in API version 20.0 and later.

`siteTemplate` string The name of the Visualforce page to be used as the
site template.


Metadata Types CustomSite

**Field** **Field Type** **Description**

`siteType` siteType Required. Identifies whether the site is a Visualforce
(Salesforce Sites), Site.com site, or ChatterNetwork

(Salesforce Sites).This field is available in API version
27.0 and later.

`subdomain` string Read only. The previous custom subdomain prefix for
the site. For example, if your site URL is

`mycompany.force.com/partners`,
`mycompany` is the `subdomain` .

This field is applicable and required only when the
`myDomainSuffix` MyDomainSettings field is set
to `MySalesforceLimited`,
`CloudforceLimited`, or
`DatabaseLimited` .

If you enabled Salesforce Sites or Digital Experiences
when the `myDomainSuffix` MyDomainSettings
field was set to one of those values, this field returns
this site’s previous subdomain. Otherwise, this field
returns a null value.

`urlPathPrefix` string The first part of the path on the site's URL that
distinguishes this site from other sites. For example,

if your site URL is
_`MyDomainName`_ `.my.salesforce-sites.com/partners`,
`partners` is the `urlPathPrefix` .

SiteIframeWhiteListUrl

Represents the external domains that you allow to frame your site or experience pages.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.

**Field** **Field Type** **Description**

`url` string Required. The trusted domain that you allow
to frame your site or Experience Cloud site

pages. Accepts these formats: `example`,
`example.com`, `*example.com`, and
`https://example.com` .

SiteRedirectMapping

SiteRedirectMapping represents a URL redirect rule on your Salesforce site.” in Salesforce Help.


Metadata Types CustomSite

**Field** **Field Type** **Description**

`action` SiteRedirect (enumeration of type string) Required. The type of the redirect. Available
string values are:

**•** `Permanent`

**•** `Temporary`

`isActive` boolean The status of the redirect: active or inactive.

`source` string Required. The URL that you want to redirect.
It must be a relative URL, but can have any

valid extension type, such as `.html` or
`.php` .

`target` string Required. The new URL you want users to
visit. It can be a relative URL or a

fully-qualified URL with an `http://` or
`https://` prefix.

SiteWebAddress

Represents the web address of a Salesforce site.

**Field** **Field Type** **Description**

`certificate` string Identifies the certificate associated with the
custom domain. If the custom domain is set

up for Salesforce to serve HTTPS, this field
indicates which certificate to use.

`domainName` string Required. The domain of the website, in the
form of `www.acme.com` .

`primary` boolean

Declarative Metadata Sample Definition

Here is a sample XML definition of a site.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomSite xmlns="http://soap.sforce.com/2006/04/metadata">

```

Required. Indicates whether this is the
primary domain ( `true` ). If `false`, this is
not the primary domain.

```
<active>true</active>

<allowHomePage>true</allowHomePage>

<allowStandardAnswersPages>true</allowStandardAnswersPages>

<allowStandardIdeasPages>true</allowStandardIdeasPages>

<allowStandardLookups>true</allowStandardLookups>

<allowStandardPortalPages>true</allowStandardPortalPages>

<allowStandardSearch>true</allowStandardSearch>

```


Metadata Types CustomSite

```
      <analyticsTrackingCode>UA-000000-2</analyticsTrackingCode>

      <authorizationRequiredPage>Unauthorized</authorizationRequiredPage>

      <bandwidthExceededPage>BandwidthExceeded</bandwidthExceededPage>

      <browserXssProtection>true</browserXssProtection>

   <cachePublicVisualforcePagesInProxyServers>false</cachePublicVisualforcePagesInProxyServers>

      <changePasswordPage>ChangePassword</changePasswordPage>

   <chatterAnswersForgotPasswordConfirmPage>ChatterAnswersForgotPasswordConfirm</chatterAnswersForgotPasswordConfirmPage>

   <chatterAnswersForgotPasswordPage>ChatterAnswersForgotPassword</chatterAnswersForgotPasswordPage>

      <chatterAnswersHelpPage>ChatterAnswersHelp</chatterAnswersHelpPage>

      <chatterAnswersLoginPage>ChatterAnswersLogin</chatterAnswersLoginPage>

   <chatterAnswersRegistrationPage>ChatterAnswersRegistration</chatterAnswersRegistrationPage>

      <clickjackProtectionLevel>SameOriginOnly</clickjackProtectionLevel>

      <contentSniffingProtection>true</contentSniffingProtection>

      <customWebAddresses>

       <domainName>www.testing123.com</domainName>

       <primary>true</primary>

      </customWebAddresses>

      <description>Partners portal for My Company</description>

      <enableAuraRequests>true</enableAuraRequests>

      <favoriteIcon>favicon</favoriteIcon>

      <fileNotFoundPage>FileNotFound</fileNotFoundPage>

      <forgotPasswordPage>ForgotPassword</forgotPasswordPage>

      <genericErrorPage>Exception</genericErrorPage>

      <guestProfile>Guest</guestProfile>

      <inMaintenancePage>InMaintenance</inMaintenancePage>

      <inactiveIndexPage>Inactive</inactiveIndexPage>

      <indexPage>UnderConstruction</indexPage>

      <masterLabel>customSite</masterLabel>

      <myProfilePage>UserProfile</myProfilePage>

      <portal>Customer Portal</portal>

      <redirectToCustomDomain>true</redirectToCustomDomain>

      <referrerPolicyOriginWhenCrossOrigin>true</referrerPolicyOriginWhenCrossOrigin>

      <robotsTxtPage>RobotsTxt</robotsTxtPage>

      <selfRegPage>SelfReg</selfRegPage>

      <serverIsDown>MyServerDownResource</serverIsDown>

      <siteAdmin>admin@myco.org</siteAdmin>

      <siteGuestRecordDefaultOwner>admin@myco.org</siteGuestRecordDefaultOwner>

      <siteIframeWhiteListUrl>

       <url>example.com</url>

      </siteIframeWhiteListUrl>

      <siteTemplate>SiteTemplate</siteTemplate>

      <siteType>Siteforce</siteType>

      <subdomain>myco</subdomain>

      <urlPathPrefix>partners</urlPathPrefix>

   </CustomSite>

```


### Metadata Types CustomTab

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Portal

### CustomTab

Represents a custom tab. Custom tabs let you display custom object data or other web content in Salesforce. When you add a custom
tab to an app in Salesforce Classic, it appears as a tab. When you add a custom tab to an app in Lightning Experience, it appears as an
item in the app’s navigation bar and in the App Launcher. When a tab displays a custom object, the tab name is the same as the custom
object name. For page, s-control, or URL tabs, the name is arbitrary.

For more information, see _Custom Tabs_ in Salesforce Help. This type extends the Metadata metadata type and inherits its `fullName`
field.

File Suffix and Directory Location

The file suffix is `.tab` . There’s one file for each tab, stored in the `tabs` folder in the corresponding package directory.

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Version

Tabs are available in API version 10.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`actionOverrides` ActionOverride[]

`auraComponent` string

A list of the action overrides that are assigned to the tab. Only one
override is allowed per `formFactor` for a given tab.

This field is available in API version 37.0 and later.

The name of the Aura component to display in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`


Metadata Types CustomTab

**Field Name** **Field Type** **Description**

**•** `scontrol`

**•** `url`

`customObject` boolean

Indicates whether this tab is for a custom object ( `true` ) or not ( `false` ).
If set to `true`, the name of the tab matches the name of the custom
object.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`

`description` string The optional description text for the tab.

`flexiPage` string

The name of the Lightning page to display in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`

`frameHeight` int The height, in pixels of the tab frame. Required for s-control and page
tabs.

`fullName` string The name of the tab. The value of this field depends on the type of tab,
and the API version.

**•** For custom object tabs, the `fullName` is the developer-assigned
name of the custom object (MyCustomObject__c, for example). For
custom object tabs, this name must be the same as the custom
object name, and `customObject` must be set to `true` .

**•** For web tabs, the `fullName` is the developer-assigned name of
the tab (MyWebTab, for example).

The `fullName` can contain only underscores and alphanumeric
characters. It must be unique, begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive
underscores. This field is inherited from the Metadata component.


Metadata Types CustomTab

**Field Name** **Field Type** **Description**

`hasSidebar` boolean Indicates if the tab displays the sidebar panel.

`icon` string

The optional reference to the image document for the tab if the tab isn’t
using one of the standard tab styles. This field is available in API version
14.0.

`label` string The label of the tab, for web tabs only.

`lwcComponent` string

`motif` string

The name of the Lightning web component to display in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`

Required. The tab style for the color scheme and icon for the custom
tab.

For example, “'Custom70: Handsaw,” is the handsaw icon.

Valid Values for this field are: Custom1:Heart, Custom2:Fan, Custom3:Sun,
Custom4:Hexagon, Custom5:Leaf, Custom6:Triangle, Custom7:Square,
Custom8:Diamond, Custom9:Lightning, Custom10:Moon, Custom11:Star,
Custom12:Circle, Custom13:Box, Custom14:Hands, Custom15:People,
Custom16:Bank, Custom17:Sack, Custom18:Form, Custom19:Wrench,
Custom20:Airplane, Custom21:Computer, Custom22:Telephone,
Custom23:Envelope, Custom24:Building, Custom25:Alarmclock,
Custom26:Flag, Custom27:Laptop, Custom28:Cellphone, Custom29:PDA,
Custom30:Radardish, Custom31:Car, Custom32:Factory, Custom33:Desk,
Custom34:Insect, Custom35:Microphone, Custom36:Train,
Custom37:Bridge, Custom38:Camera, Custom39:Telescope,
Custom40:Creditcard, Custom41:Cash, Custom42:Treasurechest,
Custom43:Jewel, Custom44:Hammer, Custom45:Ticket, Custom46:Stamp,
Custom47:Knight, Custom48:Trophy, Custom49:CD/DVD,
Custom50:Bigtop, Custom51:Apple, Custom52:Balls, Custom53:Bell,
Custom54:Boat, Custom55:Books, Custom56:Bottle,
Custom57:BuildingBlock, Custom58:Caduceus, Custom59:Can,
Custom60:Umbrella, Custom61:Castle, Custom62:Chalkboard,
Custom63:Chip, Custom64:Compass, Custom65:Cup, Custom66:Dice,
Custom67:Gears, Custom68:Globe, Custom69:Guitar, Custom70:Handsaw,
Custom71:Headset, Custom72:Helicopter, Custom73:HighwaySign,
Custom74:HotAirBalloon, Custom75:IPPhone, Custom76:Keys,
Custom77:Locked, Custom78:Map, Custom79:MeasuringTape,
Custom80:Motorcycle, Custom81:MusicalNote, Custom82:Whistle,
Custom83:Pencil, Custom84:Presenter, Custom85:RealEstateSign,


Metadata Types CustomTab

**Field Name** **Field Type** **Description**

Custom86:RedCross, Custom87:Safe, Custom88:Sailboat,
Custom89:Saxophone, Custom90:Scales, Custom91:Shield,
Custom92:Ship, Custom93:ShoppingCart, Custom94:Stethoscope,
Custom95:Stopwatch, Custom96:StreetSign, Custom97:Thermometer,
Custom98:Truck, Custom99:TVCRT, Custom100:TVWidescreen.

`page` string

`scontrol` string

The name of the Visualforce page to display in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`

The name of the s-control to display in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`

`splashPageLink` string The custom link used as the introductory splash page when users click
the tab. References a HomePageComponent.

`url` string

The URL for the external web-page to embed in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`


### Metadata Types CustomValue

**Field Name** **Field Type** **Description**

The default encoding setting is Unicode: `UTF-8` . Change it if you’re
passing information to a URL that requires data in a different format. This
option is available when the value `URL` is selected in the tab type.

```
urlEncodingKey

```

Encoding
(enumeration of
type string)

Declarative Metadata Sample Definition

The following is the definition of a tab:

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomTab xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Myriad Publishing</description>

   <frameHeight>600</frameHeight>

   <motif>Custom53: Bell</motif>

   <url>https://www.example.com</url>

   <urlEncodingKey>UTF-8</urlEncodingKey>

</CustomTab>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomApplication

### CustomValue

Represents the definition of a value used in a global value set or local custom picklist. Custom picklist fields can be local and unique, or
can inherit their values from a global picklist (called a _global value set_ in API version 38.0). This type extends the Metadata metadata type
and inherits its `fullName` field.

To deactivate a global picklist value, you can invoke an `update()` call on GlobalPicklist (API version 37.0) or GlobalValueSet (API
version 38.0 and later) with the value omitted, or with the value’s `isActive` field set to `false` . Or, you can invoke an `update()`
call directly on GlobalPicklistValue (API version 37.0) or CustomValue (API version 38.0 and later) with the `isActive` field set to `false` .

Note: If picklist values are missing from a component definition, they get deactivated when deployed. Deactivation occurs for
picklist values of both standard and custom fields.

### CustomValue doesn’t support file-based operations and only supports CRUD-based calls. CustomValue is retrieved or deployed together

with a GlobalValueSet or CustomObject component.

File Suffix and Directory Location

### CustomValue components have the suffix .customValue . A CustomValue component is returned with either a GlobalValueSet or

CustomObject component.


Metadata Types CustomValue

Version

CustomValue components are available in API version 38.0 and later. CustomValue replaces GlobalPicklistValue from API version 37.0.

Fields

**Field Name** **Field Type** **Description**

`color` string The color assigned to the picklist value when it’s used in charts on reports
and dashboards. The color is in hexadecimal format; for example,

#FF6600. If a color isn’t specified, it’s assigned dynamically upon chart
generation.

`default` boolean

`description` string

Required. Indicates whether this value is the default selection for the
global picklist and the custom picklists that share its picklist value set.
This field is set to _`true`_ by default.

A picklist value’s description. It’s useful to include a description for a
picklist value so the reason for creating it can be tracked. Limit: 255
characters.

`isActive` boolean Indicates whether this value is active or inactive. The default value is
_`true`_ . Users can select only active values from a picklist. An API retrieve

operation for global picklist values returns all active and inactive values
in the picklist. But retrieving the values of a non-global, unrestricted
picklist returns only the active values.

`label` string The value’s display label. If you don’t specify the label when creating a
value it defaults to the API name. Available in API version 39.0 and later.

StandardValue

This metadata type defines a value in a value set for a standard picklist and specifies whether this value is the default value. This type
extends the CustomValue metadata type and inherits all its fields.

When you deploy changes to standard picklist fields, picklist values are added as needed.

**Field Name** **Field Type** **Description**

`allowEmail` boolean

Indicates whether this value lets users email a quote PDF ( `true` ), or not
( `false` ). This field is only relevant for the `Status` field in quotes.This
field is available in API version 18.0 and later.

`closed` boolean Indicates whether this value is associated with a closed status ( `true` ),
or not ( `false` ). This field is only relevant for the standard `Status`

field in cases and tasks. This field is available in API version 16.0 and up
to version 36.0. In version 37.0, this field is in GlobalPicklistValue.

`converted` boolean Indicates whether this value is associated with a converted status ( `true` ),
or not ( `false` ). This field is relevant for only the standard `Lead`

`Status` field in leads. Your organization can set its own guidelines for


Metadata Types CustomValue

**Field Name** **Field Type** **Description**

determining when a lead is qualified, but typically, you want to convert
a lead as soon as it becomes a real opportunity that you want to forecast.
For more information, see Convert Qualified Leads in Salesforce Help.
This field is available in API version 16.0 and later.

`cssExposed` boolean

Indicates whether this value is available in your Self-Service Portal ( `true` ),
or not ( `false` ). This field is only relevant for the standard `Case`
`Reason` field in cases.

Self-Service provides an online support channel for your customers allowing them to resolve their inquiries without contacting a customer

service representative. For more information about Self-Service, see
Setting Up Your Self-Service Portal in Salesforce Help.

Note: Starting with Spring ’12, the Self-Service portal isn’t
available for new Salesforce orgs. Existing orgs continue to have
access to the Self-Service portal.

This field is available in API version 16.0 and later.

Indicates whether this value is associated with a forecast category
( `true` ), or not ( `false` ). This field is only relevant for the standard
`Stage` field in opportunities.

**•** Omitted

**•** Pipeline

**•** BestCase

**•** Forecast

**•** Closed

This field is available in API version 16.0 and later.

```
forecastCategory

```

ForecastCategories
(enumeration of
type string)

`highPriority` boolean Indicates whether this value is a high priority item ( `true` ), or not
( `false` ). This field is only relevant for the standard `Priority` field

in tasks. For more information about tasks, see Start Using Tasks in
Salesforce Help. This field is available in API version 16.0 and later.

`probability` int

Indicates whether this value is a probability percentage ( `true` ), or not
( `false` ). This field is only relevant for the standard `Stage` field in
opportunities. This field is available in API version 16.0 and later.

`reverseRole` string A picklist value corresponding to a reverse role name for a partner. If the
role is subcontractor, then the reverse role might be general contractor.

Assigning a partner role to an account in Salesforce creates a reverse
partner relationship so that both accounts list the other as a partner. This
field is only relevant for partner roles.

For more information, see Partner Fields in Salesforce Help.

This field is available in API version 18.0 and later.


### Metadata Types Dashboard

**Field Name** **Field Type** **Description**

`reviewed` boolean Indicates whether this value is associated with a reviewed status ( `true` ),
or not ( `false` ). This field is only relevant for the standard `Status`

field in solutions. For more information about opportunities, see Creating
Solutions in Salesforce Help. This field is available in API version 16.0 and
later.

`won` boolean Indicates whether this value is associated with a closed or won status
( `true` ), or not ( `false` ). This field is only relevant for the standard

`Stage` field in opportunities. This field is available in API version 16.0
and later.

Declarative Metadata Sample Definition

For an example of CustomValue components within a GlobalValueSet component that’s referenced by a `package.xml`, see
GlobalValueSet.

### Dashboard

Represents a dashboard. Dashboards are visual representations of data that allow you to see key metrics and performance at a glance.

This type extends the Metadata metadata type and inherits its `fullName` field. For more information, see “Edit Dashboards in
Accessibility Mode in Salesforce Classic” in the Salesforce online help.

Declarative Metadata File Suffix and Directory Location

### Dashboards are stored in the dashboards directory of the corresponding package directory. The file name matches the dashboard

title and the extension is `.dashboard` .

Retrieving Dashboards

You can’t use the wildcard (*) symbol with dashboards in `package.xml` . To retrieve the list of dashboards for populating
### package.xml with explicit names, call listMetadata() and pass in DashboardFolder as the type. Note that DashboardFolder is not returned as a type in describeMetadata() . Dashboard is returned from describeMetadata()

with an associated attribute of `inFolder` set to true. If that attribute is set to true, you can construct the type by using the component
name with the word Folder, such as DashboardFolder.

The following example shows folders in `package.xml` . The names used in `package.xml` must be developer names, not dashboard
titles.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyDBFolder/MyDBName</members>

        <name>Dashboard</name>

      </types>

      <types>

        <members>MyDocumentFolder/MyDocumentName</members>

```


Metadata Types Dashboard

```
        <name>Document</name>

      </types>

      <types>

        <members>unfiled$public/MarketingProductInquiryResponse</members>

        <members>unfiled$public/SalesNewCustomerEmail</members>

        <name>EmailTemplate</name>

      </types>

      <types>

        <members>MyReportFolder/MyReportName</members>

        <name>Report</name>

      </types>

      <version>66.0</version>

   </Package>

```

Version

Dashboard components are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`backgroundEndColor` string Required. A dashboard can have a gradient color change on its
charts. This field defines the second color for the gradient and

`backgroundStartColor` defines the first color. If you
prefer your background to be all one color or do not want a
gradient color change, select the same color for this field and
`backgroundStartColor` . The color is in hexadecimal
format; for example #FF6600.

`backgroundFadeDirection` ChartBackgroundDirection
(enumeration of type string)

Required. The direction of the gradient color change, defined
by the `backgroundStartColor` and
`backgroundEndColor` fields. The valid values are:

**•** `Diagonal`

**•** `LeftToRight`

**•** `TopToBottom`

`backgroundStartColor` string Required. The starting color for the gradient color change on
the dashboard's charts. See `backgroundEndColor` for

more information. The color is in hexadecimal format; for
example #FF6600.

`chartTheme` ChartTheme (enumeration of Determines the default theme for all dashboard charts. Replaces
type string) `dashboardChartTheme` for API v42.0 and later.

**•** `light` —Light-colored theme.

**•** `dark` —Dark-colored theme.

This field is available in API version 42.0 and later.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`colorPalette` ChartColorPalettes Determines the default palette for all dashboard charts. Replaces
(enumeration of type string) `dashboardColorPalette` for API v42.0 and later.

**•** `accessible`

**•** `bluegrass`

**•** `colorSafe`

**•** `Default`

**•** `dusk`

**•** `earth`

**•** `fire`

**•** `gray`

**•** `heat`

**•** `justice`

**•** `nightfall`

**•** `pond`

**•** `sunrise`

**•** `tropic`

**•** `unity`

**•** `water`

**•** `watermelon`

This field is available in API version 42.0 and later.

`dashboardChartTheme` ChartTheme (enumeration of Determines the default theme for all dashboard charts.
type string)

**•** `light` —Light-colored theme.

**•** `dark` —Dark-colored theme.

This field is available to maintain backward compatibility with
versions prior to API version 42.0.

`dashboardColorPalette` ChartColorPalettes Determines the default palette for all dashboard charts.
(enumeration of type string)

**•** `accessible`

**•** `bluegrass`

**•** `colorSafe`

**•** `Default`

**•** `dusk`

**•** `earth`

**•** `fire`

**•** `gray`

**•** `heat`

**•** `justice`

**•** `nightfall`


Metadata Types Dashboard

**Field** **Field Type** **Description**

**•** `pond`

**•** `sunrise`

**•** `tropic`

**•** `unity`

**•** `water`

**•** `watermelon`

This field is available to maintain backward compatibility with
versions prior to API version 42.0.

`dashboardFilters` DashboardFilter[]

`dashboardGridLayout` DashboardGridLayout

The list of filters in a dashboard.

This field is available in API version 23.0 and later.

Lists the included DashboardGridComponent objects, specifies
the number of dashboard columns, and sets each dashboard
row’s height in pixels.

This field is available in API version 35.0 and later.

`dashboardType` DashboardType (enumeration Determines the way visibility settings are set for a dashboard.
of type string) The valid values are:

**•** `SpecifiedUser` —All users see data at the access level
of one specific running user, specified in the
`runningUser` field, regardless of their own security
settings.

**•** `LoggedInUser` —Each logged-in user sees data
according to his or her own access level.

**•** `MyTeamUser` —Managers can choose to view the
dashboard from the point of view of their subordinates in
the role hierarchy. This value is available in API version 20.0
and later.

This field is available in API version 19.0 and later.

`description` string Description for the dashboard. Maximum of 255 characters.

`folderName` string

Name of the folder that houses the dashboard.

This field is available in API version 35.0 and later.

`fullName` string Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating, updating,

or deleting. See `createMetadata()` to see an example of
this field specified for a call.

This field specifies the folder and dashboard title; for example
`folderSales/California` .


Metadata Types Dashboard

**Field** **Field Type** **Description**

`isGridLayout` boolean

Specifies whether a dashboard uses the Lightning Experience
layout ( `true` ) or not ( `false` ).

Lightning Experience allows dashboards with more than three
columns with components that span multiple columns and
multiple rows in size.

This field is available in API version 35.0 and later.

`dashboardResultRefreshedDate` string Required. Date that the dashboard was last refreshed.

`dashboardResultRunningUser` string Required. User currently accessing the dashboard.

`leftSection` DashboardComponentSection Required. The left section or column of the dashboard.

`middleSection` DashboardComponentSection The middle section or column of the dashboard.

`numSubscriptions` int Number of subscriptions reported on the dashboard. This field
is available in API version 42.0 and later.

`owner` string The creator of the dashboard.

`rightSection` DashboardComponentSection Required. The right section or column of the dashboard.

`runningUser` string

The username of the user whose role and sharing settings are
used to determine the data shown in the dashboard.

When you deploy a dashboard and the value in this field is not
defined or does not correspond to a valid user, the field is

populated with the username of the user performing the
deployment.

Regardless of their security settings, all users viewing a
dashboard see exactly the same data, because dashboards are
always run using the security settings of a particular user.

Tip: To avoid inappropriate exposure of sensitive data,
save the dashboard to a folder that is visible only to
appropriate users.

`textColor` string Required. Color of the text on each chart in the dashboard. The
color is in hexadecimal format; for example #FF6600.

`title` string Required. The dashboard title.

`titleColor` string Required. Color of the titles on each dashboard component. The
color is in hexadecimal format; for example #FF6600.

`titleSize` int Required. Size of characters in title text. For example, a value of
12 indicates 12pt text.

DashboardFilter

DashboardFilter represents a filter in a dashboard.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`dashboardFilterOptions` DashboardFilterOption[] The list of items you can select in the **Filter Options** section of
the Add Filter dialog.

`name` string Required. The filter label.

DashboardFilterOption

DashboardFilterOption represents a filter option in a dashboard.

**Field** **Field Type** **Description**

```
operator

```

DashboardFilterOperation Required. Represents the filter operation for this filter item. Valid
values are:

(enumeration of type string)

**•** `equals`

**•** `notEqual`

**•** `lessThan`

**•** `greaterThan`

**•** `lessOrEqual`

**•** `greaterOrEqual`

**•** `contains`

**•** `notContain`

**•** `startsWith`

**•** `includes`

**•** `excludes`

**•** `between`

Note: The “between” operator takes two operands
(for example, “between MinimumValue,
MaximumValue”). Note also that the minimum value
is inclusive, while the maximum value is exclusive.
All other dashboard filter operations take a single
operand only.

This field is available in API version 24.0 and later.

With API version 23.0, valid values are enumerated in
CustomField.

`values` string[]

Required. One or more values in the **Filter Options** area of the
Add Filter dialog. This field is available in API version 24.0 and
later.


Metadata Types Dashboard

DashboardGridLayout

Lightning Experience features dashboards with more than three columns and components that span multiple columns and multiple
rows in size. DashboardGridLayout lists the included dashboard components, specifies the number of dashboard columns, and sets each
dashboard row’s height in pixels.

**Field** **Field Type** **Description**

`dashboardGridComponents` DashboardGridComponent[] List of DashboardGridComponent objects in the dashboard.

`numberOfColumns` int Required. Total number of columns in the dashboard.

`rowHeight` int Required. Height of each row in pixels.

DashboardGridComponent

Lightning Experience features dashboards with more than three columns and components that span multiple columns and multiple
rows in size. DashboardGridComponent specifies location and size of a given dashboard component.

**Field** **Field Type** **Description**

`colSpan` int

Required. The width of the dashboard component in columns.

For example, if `colSpan` is 5, then the dashboard component
spans five columns.

`columnIndex` int Required. The left-most column that is occupied by the
dashboard component.

`dashboardComponent` DashboardComponent Required. The dashboard component that is being sized and
placed.

`rowIndex` int Required. The top-most row that is occupied by the dashboard
component.

`rowSpan` int Required. The height of the dashboard component in rows.

DashboardComponent

A dashboard consists of a group of different components or elements that display data. Each component can use a custom report or a
custom s-control as their data source to display corporate metrics or key performance indicators. You can create several dashboard
components and display them all in one dashboard aligned in up to three columns.

**Field** **Field Type** **Description**

`chartAxisRange` ChartRangeType (enumeration of type A manual or automatic axis range for bar or line charts.
string) The valid values are:

**•** `auto`

**•** `manual`


Metadata Types Dashboard

**Field** **Field Type** **Description**

`chartAxisRangeMax` double

`chartAxisRangeMin` double

`chartSummary` ChartSummary

The maximum axis range to be displayed. This only applies
to bar and line charts in which the `manual` axis range
is selected for the `chartAxisRange` field.

The minimum axis range to be displayed. This only applies
to bar and line charts in which the `manual` axis range
is selected for the `chartAxisRange` field.

Specifies the summary field for the chart data. Required
if `isAutoSelectFromReport` is set to `false` .

This field is available in API version 25.0 and later.

`componentType` DashboardComponentType Required. Dashboard component type. The valid values
(enumeration of type string) are:

**•** `Bar`

**•** `BarGrouped`

**•** `BarStacked`

**•** `BarStacked100`

**•** `Column`

**•** `ColumnGrouped`

**•** `ColumnLine`

**•** `ColumnLineGrouped`

**•** `ColumnLineStacked`

**•** `ColumnLineStacked100`

**•** `ColumnStacked`

**•** `ColumnStacked100`

**•** `Donut`

**•** `FlexTable`

**•** `Funnel`

**•** `Gauge`

**•** `Image`

**•** `LightningWebComponent`

**•** `Line`

**•** `LineCumulative`

**•** `LineGrouped`

**•** `LineGroupedCumulative`

**•** `Metric`

**•** `Pie`

**•** `PulseMetricCard`

**•** `RichText`

**•** `Scatter`


Metadata Types Dashboard

**Field** **Field Type** **Description**

**•** `ScatterGrouped`

**•** `SControl`

**•** `Table`

**•** `VisualforcePage`

`dashboardComponentContents` DashboardComponentContent on
page 852[]

`dashboardDynamicValues` DashboardDynamicValue on page
853[]

`dashboardFilterColumns` DashboardFilterColumn on page 853[]

A list of dashboard component contents.

This field is available in API version 58.0 and later.

A list of dashboard dynamic values.

This field is available in API version 36.0 and later.

A list of dashboard filter columns. Each report-based
component must have a dashboard filter column that
defines the column that the filter applies to.

This field is available in API version 23.0 and later.

`dashboardTableColumn` DashboardTableColumn[] Represents a list of columns on a customized dashboard
table component.

`displayUnits` ChartUnits (enumeration of type Chart Units. The valid values are:
string)

**•** `Auto`

**•** `Integer`

**•** `Hundreds`

**•** `Thousands`

**•** `Millions`

**•** `Billions`

**•** `Trillions`

`drillDownUrl` string For charts, specifies a URL that users go to when they click
the dashboard component. Use this option to send users

to another dashboard, report, record detail page, or other
system that uses a Web interface. This field overrides the
`drillEnabled` and `drillToDetailEnabled`
fields.

`drillEnabled` boolean Specifies whether to take users to the full or filtered source
report when they click the dashboard component. Set to

`false` to drill to the full source report; set to `true` to
drill to the source report filtered by what they clicked. If
set to `true`, users can click individual groups, axis values,
or legend entries.

This overrides the `drillToDetailEnabled` field.
This field is available in API version 17.0 and later.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`drillToDetailEnabled` boolean When enabled, users are taken to the record detail page
when they click a record name, record owner, or feed post

in a table or chart. When set to `true` users can click axis
and legend values, chart elements, and table entries. The
`drillDownUrl` and `drillEnabled` fields override
this field. This field is available in API version 20.0 and later.

`enableHover` boolean Specifies whether to display values, labels, and
percentages when hovering over charts. Hover details

depend on chart type. Percentages apply to pie, donut,
and funnel charts only. This field is available in API version
17.0 and later.

`expandOthers` boolean Specifies whether to combine all groups less than or equal
to 3% of the total into a single 'Others' wedge or segment.

This only applies to pie, donut, and funnel charts. Set to
`true` to show all values individually on the chart; set to
`false` to combine small groups into 'Others.' This field
is available in API version 17.0 and later.

`flexComponentProperties` DashboardFlexTableComponentProperties

Defines metadata for Lightning Experience table columns
and sorting. This field is available in API version 41.0 and
later.

`footer` string Footer displayed at the bottom of the dashboard
component. Maximum of 255 characters.

`gaugeMax` double

The maximum value on a gauge. A gauge is used to see
how far you are from reaching a goal. It looks like a
speedometer in a car.

`gaugeMin` double The minimum value on a gauge.

`groupingColumn` string

Specifies the field by which to group data. This data is
displayed on the X-axis for vertical column charts and on
the Y-axis for horizontal bar charts.

This field is available in API version 25.0 and later.

`GroupingSortProperties` DashboardComponentGroupingSortProperties This field captures sort properties of the dashboard
component. If the component has one or more groupings,

sort information is stored here; otherwise, it is stored in
the `sortBy` field. This field is available in API version
46.0 and later.

`header` string Header displayed at the top of the dashboard component.
Maximum of 80 characters.

`indicatorBreakpoint1` double

The value that separates the `indicatorLowColor`
from the `indicatorMiddleColor` on the
dashboard.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`indicatorBreakpoint2` double

The value that separates the
`indicatorMiddleColor` from the
`indicatorHighColor` on the dashboard.

`indicatorHighColor` string The color representing a high number range on the
gauge.

`indicatorLowColor` string The color representing a low number range on the gauge.

`indicatorMiddleColor` string The color representing a medium number range on the
gauge.

`legendPosition` ChartLegendPosition (enumeration of
type string)

The location of the legend with respect to the chart. The
valid values are:

**•** `Bottom`

**•** `OnChart`

**•** `Right`

`maxValuesDisplayed` int The maximum number of elements to include in the
top-level grouping of the horizontal axis of a horizontal

chart, vertical axis of a vertical chart, or selected axis of a
stacked bar chart. For example, if you want to list only
your top five salespeople, create an opportunity report
that lists total opportunity amounts by owner and enter
`5` in this field.

`metricLabel` string Descriptive label for the metric. This is relevant if `metric`
is the value of the `componentType` field.

`page` string Visualforce page associated with the component.

`pageHeightInPixels` int Display height of the Visualforce page in pixels.

`report` string Name of the report associated with the component.

`scontrol` string S-control associated with component if `scontrol` is
the value of the `componentType` field. For more

information, see “Defining Custom S-Controls” in the
Salesforce online help.

`scontrolHeightInPixels` int Display height of the s-control in pixels.

`showPercentage` boolean

Indicates if percentages are displayed for regions of
gauges and wedges and segments of pie, donut, and
funnel charts ( `true` ), or not ( `false` ).

`showPicturesOnCharts` boolean Display Chatter photos for up to 20 records in a horizontal
bar chart component whose source report is grouped by

a user or group name field. If there are more than 20
records with photos, record names are shown instead of
photos. Set `Grouping Display` to _`None`_ to show


Metadata Types Dashboard

**Field** **Field Type** **Description**

photos. Set the `Drill Down to` option to _`Record`_
_`Detail Page`_ to take users directly to user profile or
group pages when they click photos. Chatter must be
enabled for photos to be displayed. Depending on your
organization's setup, you may not see photos on tables
and charts.

`showPicturesOnTables` boolean Display Chatter photos for up to 20 records in a horizontal
bar chart component whose source report is grouped by

a user or group name field. If there are more than 20
records with photos, record names are shown instead of
photos. Set `Grouping Display` to _`None`_ to show
photos. Set the `Drill Down to` option to _`Record`_
_`Detail Page`_ to take users directly to user profile or
group pages when they click photos. Chatter must be
enabled for photos to be displayed. Depending on your
organization's setup, you may not see photos on tables
and charts.

`showTotal` boolean Indicates if the total of all wedges is displayed for gauges
and donut charts ( `true` ), or not ( `false` ).

`showValues` boolean Indicates if the values of individual records or groups are
displayed for charts ( `true` ), or not ( `false` ).

`sortBy` DashboardComponentFilter The sort option for the dashboard component.
(enumeration of type string)

`sortLegendValues` boolean Specifies whether to sort the legend values for the
dashboard component.

`title` string The title of the dashboard component. Maximum of 40
characters.

`useReportChart` boolean Specifies whether to use the chart defined in the source
report on this dashboard component. The chart settings

in the source report determine how the chart displays in
the dashboard, and any chart settings you define for the
dashboard are overridden. If you defined a combination
chart in the source report, use this option to use that
combination chart on this dashboard.

DashboardComponentContent

dashboardComponentContent represents the content of a dashboard’s components.

**Field** **Field Type** **Description**

`additionalInfo` string Any additional metadata the user wants to include for the
component contents.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`altText` string The component’s alternative text.

`fileName` string The name of the component file.

`fit` Fit (enumeration of type string) The image alignment type. Valid values are:

**•** `FitHeight`

**•** `FitWidth`

**•** `Original`

**•** `Stretch`

**•** `Tile`

`horizontalAlignment` HorizontalAlignment The horizontal alignment type. Valid values are:
(enumeration of type string)

**•** `Left`

**•** `Center`

**•** `Right`

`componentParameters` string The parameters for the component.

`richTextContent` string The rich text content for the component.

`tooltip` string The dashboard component’s tooltip.

`verticalAlignment` VerticalAlignment (enumeration The vertical alignment type. Valid values are:
of type string)

**•** `Bottom`

**•** `Center`

**•** `Top`

DashboardDynamicValue

DashboardDynamicValue represents a dynamic value in a dashboard.

**Field** **Field Type** **Description**

`additionalInfo` string Any additional metadata the user wants to include for the
dynamic value.

`fieldName` string Required. The name of the field for the dynamic value.

`isDynamicUser` boolean Indicates whether the value should be retrieved as the user
running the dashboard ( `true` ) or not ( `false` ).

DashboardFilterColumn

DashboardFilterColumn represents a filter column in a dashboard.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`column` string Required. The report column code for the filter.

DashboardTableColumn

DashboardTableColumn represents a column in a customized table component in a dashboard.

**Field** **Field Type** **Description**

`aggregateType` ReportSummaryType[] Specifies the aggregation type for the table column.
(enumeration of type string)

`column` string Required. The label of the column to use in the table.

`showTotal` boolean

Displays the totals for each summarizable column in the
dashboard table. This field is available in API version 19.0 and
later.

`sortBy` DashboardComponentSection(enumeration The sort option for the dashboard table component. Sort on just
of type string) one column per table.

DashboardFlexTableComponentProperties

DashboardFlexTableComponentProperties represents a column in a customized table component in a dashboard.

**Field** **Field Type** **Description**

`flexTableColumn` DashboardComponentColumn Represents a column in a Lightning Experience table component.
This field is available in API version 41.0 and later.

`flexTableSortInfo` DashboardComponentSortInfo

`hideChatterPhotos` boolean

Represents sorting column and order in a Lightning Experience
table component. This field is available in API version 41.0 and
later.

If `true`, hides any photos from Chatter feeds.

This field is available in API version 41.0 and later.

`decimalPrecision` integer For columns with numeric values, indicates the number of
significant digits.

`useReportTableSetting` boolean

If `true`, users can import report table settings to this
component.

This field is available in API version 65.0 and later.

DashboardComponentGroupingSortProperties

DashboardComponentGroupingSortProperties is composed of multiple elements of the type DashboardComponentGroupingSort.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`groupingSorts` DashboardComponentGroupingSort

DashboardComponentGroupingSort

This field stores sort information for a dashboard at each
grouping level of granularity. This field is available in API version
46.0 and later.

DashboardComponentGroupingSort specifies properties for sorting on a dashboard component group.

**Field** **Field Type** **Description**

`groupingLevel` String Grouping at which this sort configuration is applied.

`inheritedReportGroupingSort` String `true` if the sort order is picked up from an underlying report
for this grouping level.

`sortColumn` String

If grouping is sorted by an aggregate, this value is the aggregate
value (such as `sortColumn` ). If the grouping is sorted by its
own value, this field is null.

`sortOrder` String `Ascending` or `Descending` to reflect the sort order.

DashboardComponentColumn

DashboardComponentColumn represents a component column in a dashboard. Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`breakPoint1` double The value that separates the `lowRangeColor` from the
`midRangeColor` on the dashboard.

`breakPoint2` double The value that separates the `midRangeColor` from the
`highRangeColor` on the dashboard.

`breakPointOrder` double Conditional highlighting can be applied to multiple columns.
This field stores the order of conditional highlights.

`highRangeColor` int The color representing a high number range on the column.

`lowRangeColor` int The color representing a low number range on the column.

`midRangeColor` int The color representing a mid number range on the column.

`reportColumn` string Required. The report column code for the filter.

`showTotal` boolean If `true`, the column total is displayed.

`type` DashboardComponentColumnType Represents the type of Lightning Experience table column:
(enumeration of type string)

**•** `Details`

**•** `Aggregates`

**•** `Grouping`


Metadata Types Dashboard

**Field** **Field Type** **Description**

This field is available in API version 41.0 and later.

DashboardComponentSortInfo

DashboardFilterColumns represents a filter column in a dashboard.

**Field** **Field Type** **Description**

`ComponentSortColumn` string Indicates the column on which the table is sorted. This field is
available in API version 41.0 and later.

`sortOrder` string Indicates whether column sorting is ascending or descending.
This field is available in API version 41.0 and later.

DashboardComponentSection

DashboardComponentSection represents one of the sections or columns in a dashboard.

**Field** **Field Type** **Description**

`columnSize` DashboardComponentSize Required. The size of the column in the dashboard:
(enumeration of type string)

**•** `Medium`

**•** `Narrow`

**•** `Wide`

`components` DashboardComponent[] The list of DashboardComponent objects in the dashboard
column.

DashboardComponentFilter

DashboardComponentFilter is an enumeration of type string that lists the sort values for dashboard components. The valid values are:

**Enumeration Value** **Description**

`RowLabelAscending` Sorts in alphabetical order by the label.

`RowLabelDescending` Sorts in reverse alphabetical order by the label.

`RowValueAscending` Sorts lowest to highest by the value.

`RowValueDescending` Sorts highest to lowest by the value.


Metadata Types Dashboard

Declarative Metadata Sample Definition — Filtered Dashboard

A sample XML definition of a filtered dashboard is shown below. Note that this example is supported in API version 24.0 and later. The
file name matches the dashboard title and the extension is `.dashboard` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Dashboard xmlns="http://soap.sforce.com/2006/04/metadata">

      <backgroundEndColor>#FFFFFF</backgroundEndColor>

      <backgroundFadeDirection>Diagonal</backgroundFadeDirection>

      <backgroundStartColor>#FFFFFF</backgroundStartColor>

      <dashboardFilters>

        <dashboardFilterOptions>

           <operator>equals</operator>

           <values>Media</values>

        </dashboardFilterOptions>

        <dashboardFilterOptions>

           <operator>lessThan</operator>

           <values>Working</values>

        </dashboardFilterOptions>

        <dashboardFilterOptions>

           <operator>between</operator>

           <values>ABC</values>

           <values>XYZ</values>

        </dashboardFilterOptions>

        <name>Industry</name>

      </dashboardFilters>

      <dashboardFilters>

        <dashboardFilterOptions>

           <operator>equals</operator>

           <values>Analyst,Partner</values>

        </dashboardFilterOptions>

        <dashboardFilterOptions>

           <operator>startsWith</operator>

           <values>Integrator</values>

        </dashboardFilterOptions>

        <name>Account Type</name>

      </dashboardFilters>

      <dashboardType>SpecifiedUser</dashboardType>

      <leftSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Bar</componentType>

           <dashboardFilterColumns>

             <column>INDUSTRY</column>

           </dashboardFilterColumns>

           <dashboardFilterColumns>

             <column>TYPE</column>

           </dashboardFilterColumns>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>false</drillEnabled>

           <drillToDetailEnabled>false</drillToDetailEnabled>

           <enableHover>false</enableHover>

           <expandOthers>false</expandOthers>

           <legendPosition>Bottom</legendPosition>

```


Metadata Types Dashboard

```
           <report>unfiled$public/SampleReportofAccounts</report>

           <showPercentage>false</showPercentage>

           <showPicturesOnCharts>false</showPicturesOnCharts>

           <showValues>false</showValues>

           <sortBy>RowLabelAscending</sortBy>

           <useReportChart>false</useReportChart>

        </components>

      </leftSection>

      <middleSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Funnel</componentType>

           <dashboardFilterColumns>

             <column>ACCOUNT_INDUSTRY</column>

           </dashboardFilterColumns>

           <dashboardFilterColumns>

             <column>ACCOUNT.TYPE</column>

           </dashboardFilterColumns>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>false</drillEnabled>

           <drillToDetailEnabled>false</drillToDetailEnabled>

           <enableHover>false</enableHover>

           <expandOthers>false</expandOthers>

           <legendPosition>Bottom</legendPosition>

           <report>unfiled$public/SampleReportofCases</report>

           <showPercentage>false</showPercentage>

           <showValues>true</showValues>

           <sortBy>RowLabelAscending</sortBy>

           <useReportChart>false</useReportChart>

        </components>

      </middleSection>

      <rightSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Column</componentType>

           <dashboardFilterColumns>

             <column>INDUSTRY</column>

           </dashboardFilterColumns>

           <dashboardFilterColumns>

             <column>ACCOUNT_TYPE</column>

           </dashboardFilterColumns>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>false</drillEnabled>

           <drillToDetailEnabled>false</drillToDetailEnabled>

           <enableHover>false</enableHover>

           <expandOthers>false</expandOthers>

           <legendPosition>Bottom</legendPosition>

           <report>unfiled$public/SampleReportofOpportunities</report>

           <showPercentage>false</showPercentage>

           <showValues>false</showValues>

           <sortBy>RowLabelAscending</sortBy>

           <useReportChart>false</useReportChart>

```


Metadata Types Dashboard

```
        </components>

      </rightSection>

      <runningUser>admin@TESTORGNUM</runningUser>

      <textColor>#000000</textColor>

      <title>My Dashboard</title>

      <titleColor>#000000</titleColor>

      <titleSize>12</titleSize>

   </Dashboard>

```

Declarative Metadata Sample Definition — Unfiltered Dashboard

A sample XML definition of a dashboard is shown below. The file name matches the dashboard title and the extension is `.dashboard` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Dashboard xmlns="http://soap.sforce.com/2006/04/metadata">

      <backgroundEndColor>#FFFFFF</backgroundEndColor>

      <backgroundFadeDirection>LeftToRight</backgroundFadeDirection>

      <backgroundStartColor>#FFFFFF</backgroundStartColor>

      <description>Dashboard with all possible chart types</description>

      <leftSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>BarStacked100</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <componentType>Table</componentType>

           <dashboardTableColumn>

             <column>CLOSE_DATE</column>

             <sortBy>RowLabelAscending</sortBy>

           </dashboardTableColumn>

           <dashboardTableColumn>

             <aggregateType>Sum</aggregateType>

             <column>AMOUNT</column>

             <showTotal>true</showTotal>

           </dashboardTableColumn>

           <dashboardTableColumn>

             <column>STAGE_NAME</column>

           </dashboardTableColumn>

           <dashboardTableColumn>

             <column>PROBABILITY</column>

             <aggregateType>Maximum</aggregateType>

           </dashboardTableColumn>

           <displayUnits>Integer</displayUnits>

           <header>Opportunities Table</header>

           <indicatorHighColor>#54C254</indicatorHighColor>

           <indicatorLowColor>#C25454</indicatorLowColor>

           <indicatorMiddleColor>#C2C254</indicatorMiddleColor>

           <maxValuesDisplayed>10</maxValuesDisplayed>

```


Metadata Types Dashboard

```
           <report>testFolder/sourceRep</report>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Bar</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Column</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <legendPosition>Bottom</legendPosition>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

           <useReportChart>true</useReportChart>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Funnel</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <expandOthers>true</expandOthers>

           <legendPosition>Bottom</legendPosition>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

      </leftSection>

      <middleSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>ColumnStacked100</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>ColumnStacked</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

```


Metadata Types Dashboard

```
           <chartAxisRange>Auto</chartAxisRange>

           <componentType>ColumnStacked</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>ColumnGrouped</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Column</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

      </middleSection>

      <rightSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Bar</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Pie</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <expandOthers>true</expandOthers>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>LineGroupedCumulative</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

```


Metadata Types Dashboard

```
           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>LineGrouped</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>LineCumulative</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Donut</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <expandOthers>true</expandOthers>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

      </rightSection>

      <runningUser>admin@TESTORGNUM</runningUser>

      <textColor>#000000</textColor>

      <title>Db Title</title>

      <titleColor>#000000</titleColor>

      <titleSize>12</titleSize>

   </Dashboard>

```

Declarative Metadata Sample Definition — Lightning Experience Dashboard
with **`isGridLayout`** Equals **`true`**

A sample XML definition of a Lightning Experience dashboard with `isGridLayout` equals `true` is shown below. Note that this
example is supported in API version 35.0 and later. The file name matches the dashboard title and the extension is `.dashboard` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Dashboard xmlns="http://soap.sforce.com/2006/04/metadata">

      <backgroundEndColor>#FFFFFF</backgroundEndColor>

      <backgroundFadeDirection>Diagonal</backgroundFadeDirection>

      <backgroundStartColor>#FFFFFF</backgroundStartColor>

      <dashboardType>SpecifiedUser</dashboardType>

      <gridLayout>

        <dashboardGridComponents>

```


Metadata Types Dashboard

```
           <colSpan>3</colSpan>

           <columnIndex>0</columnIndex>

           <dashboardComponent>

             <autoselectColumnsFromReport>false</autoselectColumnsFromReport>

             <chartAxisRange>Auto</chartAxisRange>

             <chartSummary>

               <axisBinding>y</axisBinding>

               <column>RowCount</column>

             </chartSummary>

             <componentType>Donut</componentType>

             <drillEnabled>false</drillEnabled>

             <drillToDetailEnabled>false</drillToDetailEnabled>

             <enableHover>false</enableHover>

             <expandOthers>false</expandOthers>

             <groupingColumn>TITLE</groupingColumn>

             <legendPosition>Bottom</legendPosition>

             <report>unfiled$public/lead_rpt</report>

             <showPercentage>false</showPercentage>

             <showTotal>false</showTotal>

             <showValues>true</showValues>

             <sortBy>RowLabelAscending</sortBy>

             <useReportChart>false</useReportChart>

           </dashboardComponent>

           <rowIndex>0</rowIndex>

           <rowSpan>3</rowSpan>

        </dashboardGridComponents>

        <dashboardGridComponents>

           <colSpan>3</colSpan>

           <columnIndex>0</columnIndex>

           <dashboardComponent>

             <autoselectColumnsFromReport>false</autoselectColumnsFromReport>

             <chartAxisRange>Auto</chartAxisRange>

             <chartSummary>

               <axisBinding>y</axisBinding>

               <column>RowCount</column>

             </chartSummary>

             <componentType>Pie</componentType>

             <drillEnabled>false</drillEnabled>

             <drillToDetailEnabled>false</drillToDetailEnabled>

             <enableHover>false</enableHover>

             <expandOthers>false</expandOthers>

             <groupingColumn>TITLE</groupingColumn>

             <legendPosition>Bottom</legendPosition>

             <report>unfiled$public/lead_rpt</report>

             <showPercentage>false</showPercentage>

             <showValues>true</showValues>

             <sortBy>RowLabelAscending</sortBy>

             <useReportChart>false</useReportChart>

           </dashboardComponent>

           <rowIndex>3</rowIndex>

           <rowSpan>3</rowSpan>

        </dashboardGridComponents>

        <dashboardGridComponents>

           <colSpan>3</colSpan>

```


### Metadata Types DataCategoryGroup

```
           <columnIndex>0</columnIndex>

           <dashboardComponent>

             <autoselectColumnsFromReport>false</autoselectColumnsFromReport>

             <chartAxisRange>Auto</chartAxisRange>

             <chartSummary>

               <axisBinding>y</axisBinding>

               <column>RowCount</column>

             </chartSummary>

             <componentType>Column</componentType>

             <drillEnabled>false</drillEnabled>

             <drillToDetailEnabled>false</drillToDetailEnabled>

             <enableHover>false</enableHover>

             <expandOthers>false</expandOthers>

             <groupingColumn>TITLE</groupingColumn>

             <legendPosition>Bottom</legendPosition>

             <report>unfiled$public/lead_rpt</report>

             <showPercentage>false</showPercentage>

             <showValues>false</showValues>

             <sortBy>RowLabelAscending</sortBy>

             <useReportChart>false</useReportChart>

           </dashboardComponent>

           <rowIndex>9</rowIndex>

           <rowSpan>3</rowSpan>

        </dashboardGridComponents>

        <numberOfColumns>9</numberOfColumns>

        <rowHeight>90</rowHeight>

      </gridLayout>

      <isGridLayout>true</isGridLayout>

      <runningUser>admin@s1.com</runningUser>

      <textColor>#000000</textColor>

      <title>sfx</title>

      <titleColor>#000000</titleColor>

      <titleSize>12</titleSize>

   </Dashboard>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Folder

Report

### DataCategoryGroup

Represents a data category group.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types DataCategoryGroup

Warning: Using Metadata API to deploy category changes from one organization to another permanently removes categories
and record categorizations that are not specified in your XML file. Salesforce recommends that you manually create data categories
and record associations in an organization from Setup by entering _`Data Categories`_ in the `Quick Find` box, then
selecting **Data Categories** rather than deploying changes from a sandbox to a production organization. For more information,
see Usage.

Data category groups are provided to:

**•** Classify and filter data.

**•** Share data among users.

Every data category group contains items or data categories that can be organized hierarchically.

The example below shows the `Geography` data category group and its data categories.

```
   Geography

      Worldwide

        North America

           United States of America

           Canada

           Mexico

        Europe

        Asia

```

Note: See "Work with Data Categories" in the Salesforce online help for more information on data category groups, data categories,
parent and sub categories.

File Suffix and Directory Location

The file suffix is `.datacategorygroup` . There is one file for each data category group stored in the `datacategorygroups`
folder in the corresponding package directory.

Version

Data category groups are available in API version 18.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`active` boolean Required. The status of the category group. Indicates whether this
category group is active, ( `true` ), or not active ( `false` ).

`dataCategory` DataCategory on Required. The top-level category within the data category group.
page 866

`description` string The description of the data category group.

`fullName` string Required. The unique name of the data category group. When creating
a data category group, the `fullName` field and the file name (without

its suffix) must match.The `fullName` can contain only underscores


Metadata Types DataCategoryGroup

**Field Name** **Field Type** **Description**

and alphanumeric characters. It must be unique, begin with a letter, not
include spaces, not end with an underscore, and not contain two
consecutive underscores. This field is inherited from the Metadata
component.

`label` string Required. Label that represents the object in Salesforce.

`objectUsage` ObjectUsage on The objects that are associated with the data category group.
page 866

DataCategory

Represents an item (or data category) in the data category group. A data category can recursively contain a list of other data categories.

**Field Name** **Field Type** **Description**

`dataCategory` DataCategory[]

A recursive list of sub data categories. For example, a list of countries
within a continent. You can create up to 100 categories in a data category
group and have up to 5 levels in a data category group hierarchy.

`label` string Required. Label for the data category throughout the Salesforce user
interface.

`name` string Required. The developer name of the data category used as a unique
identifier for API access. The name can only contain characters, letters,

and the underscore (_) character, must start with a letter, and cannot
end with an underscore or contain two consecutive underscore
characters.

Important: The value for this field is defined once and cannot
be changed later.

Warning: If you deploy a category group that already exists in
an organization, any category that is not defined in the XML file
is permanently removed from your organization. For more
information see Usage.

ObjectUsage

Represents the objects that can be associated with the data category group. This association allows the object to be classified and filtered
using the data categories.

**Field Name** **Field Type** **Description**

`object` string[] A list of the object names that can be associated with the data category
group. Valid values are:

**•** `KnowledgeArticleVersion` —to associate articles. See
"Modify Default Category Group Assignments for Articles" in the


Metadata Types DataCategoryGroup

**Field Name** **Field Type** **Description**

Salesforce online help for more information on data category groups
association to articles.

**•** `Question` —to associate questions. You can associate the
`Question` object with at most one category group.

Warning: If you deploy a category group that already exists in
an organization, any object association that is not defined in the
XML file is permanently removed from your organization. Ensure
that your XML file specifies all the records associated with your
category group in the organization. For more information see
Usage.

Declarative Metadata Sample Definition

This sample is the definition of the `Geography` data category group and its data categories:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DataCategoryGroup xmlns="http://soap.sforce.com/2006/04/metadata">

     <label>Geography</label>

     <description>Geography structure of service center locations</description>

     <fullName>geo</fullName>

     <dataCategory> <name>WW</name> <label>Worldwide</label>

       <dataCategory> <name>AMER</name> <label>North America</label>

         <dataCategory>

           <name>USA</name>

           <label>United States of America</label>

         </dataCategory>

         <dataCategory>

           <name>CAN</name>

           <label>Canada</label>

         </dataCategory>

         <dataCategory>

           <name>MEX</name>

           <label>Mexico</label>

         </dataCategory>

       </dataCategory>

       <dataCategory> <name>EMEA</name> <label>Europe, Middle East, Africa</label>

         <dataCategory>

           <name>FR</name>

           <label>France</label>

         </dataCategory>

         <dataCategory>

           <name>SP</name>

           <label>Spain</label>

        </dataCategory>

         <dataCategory>

           <name>UK</name>

           <label>United-Kingdom</label>

         </dataCategory>

```


Metadata Types DataCategoryGroup

```
       </dataCategory>

       <dataCategory>

         <name>APAC</name>

         <label>Asia</label>

       </dataCategory>

     </dataCategory>

     <objectUsage>

       <object>KnowledgeArticleVersion </object>

     <objectUsage>

   </DataCategoryGroup>

```

Usage

When you deploy a category group XML file, Metadata API checks whether the category group exists in the target organization. If the
category group does not exist, it is created. If the category group already exists, then Metadata API:

**•** Adds any new category or object defined in the XML file.

**•** Deletes any category that is not defined in the XML file. Records associated with the deleted categories are re-associated with the
parent category.

**•** Deletes any object association that is not defined in the XML file.

**•** Moves any category if its hierarchical position differs from the position specified in the XML file.

Note: When a category moves to a new parent category, users that have no visibility on the new parent category lose their
visibility to the repositioned category.

Note: For more information about category deletion, category repositioning and its impact on record categorization and visibility
see "Delete a Data Category" and "Modify and Arrange Data Categories" in the Salesforce online help.

Using Metadata API to deploy category changes from one organization to another permanently removes categories and record
categorizations that are not specified in your XML file. Salesforce recommends that you manually create data categories and record
associations in an organization from Setup by entering _`Data Categories`_ in the `Quick Find` box, then selecting **Data**
**Categories** rather than deploying changes from a sandbox to a production organization.

The following example illustrates what happens if you deploy an XML representation of a `Geography` data category group hierarchy
to an organization that already has this data category group defined. Note that the organization contains a `US` category, while the XML
file includes a `USA` category in the same hierarchical position. The Metadata API deployment process deletes the `US` category from
the organization and moves associations for any records from `US` to the parent `AMER` category. It also adds the `USA` category under
`AMER` . Note that all records that were previously categorized with `US` are now associated with the `AMER` category.


Metadata Types DataCategoryGroup

The next example illustrates what can happen when you delete or move a category in a data category group and deploy its XML
representation from a sandbox to a production organization that already has this data category group defined. Hierarchy 1 shows the
initial data category group in the sandbox organization. In hierarchy 2, we add an `EU` category under `EMEA` and move `FR`, `SP` and
`UK` below `EU` . In hierarchy 3, we delete `FR` and associate its records with its new parent, `EU` . Finally, we deploy the changes from the
sandbox to the production organization.


### Metadata Types DataObjectSearchIndexConf

Metadata API has no concept of the order of the changes made to the sandbox organization. It just deploys the changes from one
organization to another. During the deployment, it first notices the deletion of the `FR` category and removes it from the production
organization. Consequently, it moves associations for any records from `FR` to its parent on the production organization, `EMEA` . Metadata
API then adds the `EU` category and moves `SP` and `UK` below it. Although the category group hierarchy looks the same in both
organizations, record categorization in production is different from the sandbox organization. The records that were originally associated
with `FR` in hierarchy 1 are associated with `EU` in the sandbox organization, but are associated with `EMEA` in the production organization.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DataObjectSearchIndexConf

Represents the source Data 360 data model object (DMO) for Search Answers and holds the search index that Search Answers uses
when searching DMO records.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DataObjectSearchIndexConf components have the suffix .dataObjectSearchIndexConf and are stored in the

`dataObjectSearchIndexConfs` folder.


Metadata Types DataObjectSearchIndexConf

Version

DataObjectSearchIndexConf components are available in API version 63.0 and later.

Special Access Rules

To access this metadata type, you must have the Customize Application user permission. The Salesforce org must have a Data 360 license.

Fields

**Field Name** **Description**

```
application

channel

masterLabel

nameFieldReference

objectReference

retriever

```

**Field Type**
string

**Description**
Required.

The name of the app that the Search Answers index is associated with.

**Field Type**
string

**Description**
The search channel that the Search Answers configuration applies to.

**Field Type**
string

**Description**
Required.

The name of the Search Answers configuration.

**Field Type**
string

**Description**
Required.

The name field of the DMO selected as a source for Search Answers.

**Field Type**
string

**Description**
Required.

The DMO that the Search Answers configuration applies to.

**Field Type**
string


### Metadata Types DataWeaveResource

**Field Name** **Description**

**Description**
The retriever that accesses the Search Answers indexed data.

```
searchIndex

```

**Field Type**
string

**Description**
Required.

The name of the search index mapped to the DMO.

Declarative Metadata Sample Definition

The following is an example of a DataObjectSearchIndexConf component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DataObjectSearchIndexConf xmlns="http://soap.sforce.com/2006/04/metadata">

 <application>SearchAnswers</application>

 <channel>SharedIndex</channel>

 <masterLabel>SearchAnswers</masterLabel>

 <nameFieldReference>Name__c</nameFieldReference>

 <objectReference>Account__dlm</objectReference>

 <searchIndex>searchAnswersIndex</searchIndex>

</DataObjectSearchIndexConf>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

  <types>

     <members>*</members>

     <name>DataObjectSearchIndexConf</name>

  </types>

  <version>63.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DataWeaveResource

Represents the `DataWeaveScriptResource` class that is generated for all DataWeave scripts. DataWeave scripts can be directly
invoked from Apex.


Metadata Types DataWeaveResource

Parent Type

This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

File Suffix and Directory Location

DataWeaveResource components have the suffix `.dwl` and are stored in the `dw` folder.

Version

DataWeaveResource components are available in API version 58.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
apiVersion

isGlobal

isProtected

```

**Field Type**
double

**Description**
Required.

The API version for this component.

**Field Type**
boolean

**Description**
When set to `true`, the generated `DataWeaveScriptResource` class is global.

**Field Type**
boolean

**Description**
Not used.

Declarative Metadata Sample Definition

The following is an example of a DataWeaveResource component.

```
csvToContacts.dwl

%dw 2.0

input records application/csv

output application/apex

```


### Metadata Types DecisionTable

```
   --
   records map(record) -> {

    FirstName: record.first_name,

    LastName: record.last_name,

    Email: record.email

   } as Object {class: "Contact"}

   csvToContacts.dwl-meta.xml

   <?xml version="1.0" encoding="UTF-8"?>

   <DataWeaveResource xmlns="http://soap.sforce.com/2006/04/metadata">

      <apiVersion>58.0</apiVersion>

      <isGlobal>true</isGlobal>

   </DataWeaveResource>

```

The following is an example `package.xml` that references the csvToContacts definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

       xmlns="http://soap.sforce.com/2006/04/metadata">

       <types>

           <members>csvToContacts</members>

           <name>DataWeaveResource</name>

       </types>

       <version>58.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DecisionTable

Represents the information about a decision table.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DecisionTable components have the suffix .decisionTable and are stored in the decisionTables folder.

Version

### DecisionTable components are available in API version 51.0 and later.


Metadata Types DecisionTable

Special Access Rules

To use this metadata type, your Salesforce org must have the Loyalty Management or the Rebate Management license.

Fields

**Field Name** **Description**

```
collectOperator

conditionCriteria

conditionType

dataSourceType

```

**Field Type**
DecisionTableCollectOperator (enumeration of type string)

**Description**
Specifies the operator that's used when the result is filtered by the Collect operator.

Valid values are:

**•** `Count`

**•** `Maximum`

**•** `Minimum`

**•** `None`

**•** `Sum`

**Field Type**
string

**Description**
Logic that's used to decide how the input fields are processed.

**Field Type**
DecisionTableConditionType (enumeration of type string)

**Description**
Condition logic that's used for input fields.

Valid values are:

**•** `All`

**•** `Any`

**•** `Custom`

**Field Type**
DecisionTableDataSourceType (enumeration of type string)

**Description**
Specifies the type of data source that's used to create a decision table.

Valid values are:

**•** `ContextDefinition`

**•** `CsvUpload`

**•** `MultipleSobjects`

**•** `SingleSobject`


Metadata Types DecisionTable

**Field Name** **Description**

```
decisionTableParameters

decisionTable

SourceCriterias

description

doesConsiderNullValue

downloadStatus

executionType

```

**Field Type**

DecisionTableParameter[]

**Description**
Parameters that you specify in a decision table.

**Field Type**

DecisionTableSourceCriteria[]

**Description**
The fields and values from a data source that are used to define the condition logic of
the data that's used in a decision table.

**Field Type**
string

**Description**
Description of the decision table.

**Field Type**
boolean

**Description**
Indicates whether a column that has a null value is considered for lookup ( `true` ) or
not ( `false` ). The default value is false.

**Field Type**
DecisionTableDownloadStatus (enumeration of type string)

**Description**
Specifies the progress status of a CSV download from a CSV-based lookup table.
Available in API version 64.0 and later.

Valid values are:

**•** `Completed`

**•** `DownloadInProgress`

**•** `Failed`

**Field Type**
DecisionTableExecutionType (enumeration of type string)

**Description**
Indicates the backing storage for the Decision Table.

Valid values are:

**•** `Dmo`

**•** `Hbase`

**•** `Hbpo`

**•** `Solr`


Metadata Types DecisionTable

**Field Name** **Description**

**•** `Soql`

Execution type of `Hbase` must be passed in all caps ( `HBASE` ) in POST and PATCH
calls.

```
filterResultBy

hasIncrementalSyncFailed

isIncrementalSyncEnabled

lastIncrementalSyncDate

lastSyncDate

refreshFailureReason

```

**Field Type**
DecisionTableHitPolicy (enumeration of type string)

**Description**
Specifies how the results of a decision table are filtered if a set of inputs returns multiple
matching outputs.

Valid values are:

**•** `AnyValue`

**•** `CollectOperator`

**•** `FirstMatch`

**•** `OutputOrder`

**•** `Priority`

**•** `RuleOrder`

**•** `UniqueValues`

**Field Type**
boolean

**Description**
Indicates if the last incremental refresh failed.

**Field Type**
boolean

**Description**
Indicates if incremental refresh is enabled for the Decision Table.

**Field Type**
string

**Description**
The date and time on which the last incremental refresh occured for the decision table.

**Field Type**
string

**Description**
Latest date on which the decision table was refreshed.

**Field Type**
string


Metadata Types DecisionTable

**Field Name** **Description**

**Description**
Reason why the refresh of the decision table data failed.

```
refreshStatus

setupName

sourceConditionLogic

sourceObject

status

```

**Field Type**
DecisionTableRefreshStatus (enumeration of type string)

**Description**
Specifies the refresh status of the cached data in the decision table.

Valid values are:

**•** `Completed`

**•** `Failed`

**•** `InProgress`

**•** `Initiated`

**Field Type**
string

**Description**

Required. Name of the decision table, which appears in Salesforce Setup.

**Field Type**
string

**Description**
The condition logic that's used to define the decision table from the source data.

**Field Type**
string

**Description**

Required. Object that contains the rules based on which the decision table must
provide outcomes.

**Field Type**
DecisionTableStatus (enumeration of type string)

**Description**

Required. Status of the decision table.

Valid values are:

**•** `ActivationInProgress`

**•** `Active`

**•** `Draft`

**•** `Inactive`


Metadata Types DecisionTable

**Field Name** **Description**

```
type

uploadStatus

usageType

```

**Field Type**
DecisionTableType (enumeration of type string)

**Description**
Stores the type of decision table.

Valid values are:

**•** `Advanced`

**•** `HighScaleExecution`

**•** `HighVolume`

**•** `LowVolume`

**•** `MediumVolume`

**•** `RealTime`

**Field Type**
DecisionTableUploadStatus (enumeration of type string)

**Description**
Specifies the progress status of the CSV upload for a CSV based Lookup table.

Valid values are:

**•** `Completed`

**•** `CompletedWithErrors`

**•** `Failed`

**•** `UploadInProgress`

**Field Type**
ExpsSetProcessType (enumeration of type string)

**Description**
Type of industry or the application within the industry that's using a decision table.

Valid values are:

**•** `Bre`

**•** `ComplianceControl`

**•** `DecompositionEnrichmentMapping`

**•** `DefaultPricing`

**•** `DefaultRating`

**•** `EventOrchestration`

**•** `FinancialServicesCloud`

**•** `FulfillmentCondition`

**•** `GpaCalculation`

**•** `InsuranceClaimProcessing` —Available in API version 65.0 and later.

**•** `ItServiceManagement` —Available in API version 65.0 and later.

**•** `PlanCostCalculation`


Metadata Types DecisionTable

**Field Name** **Description**

**•** `PriceProtection`

**•** `PricingDiscovery`

**•** `ProductCategoryQualification`

**•** `ProductQualification`

**•** `RatingDiscovery`

**•** `RecordAlert`

**•** `ShipAndDebit`

**•** `StudentInformationSystem` —Available in API version 65.0 and later.

**•** `StudentSuccess`

**•** `TestProcess`

**•** `WarrantyClaim`

When Business Rules Engine is enabled for a Salesforce instance, the default value is
' `Bre` ’. Other usage types are available to you depending on your industry solution
and permission sets.

DecisionTableParameter

Represents an input or output field of a decision table.

**Field Name** **Description**

```
dataType

decimalScale

```

**Field Type**
DTParameterDataType (enumeration of type string)

**Description**
The data type of the field used in a decision table.

Valid values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Number`

**•** `Percent`

**•** `String`

**Field Type**
int

**Description**
The number of digits to the right of the decimal point.


Metadata Types DecisionTable

**Field Name** **Description**

```
domainObject

fieldName

fieldPath

isGroupByField

isPriorityField

isRequired

length

operator

```

**Field Type**
string

**Description**
For polymorhpic fields, indicates the domain object in the field hierarchy.

**Field Type**
string

**Description**

Required. API name of the fields that selected as an input or output for the decision
table.

**Field Type**
string

**Description**
The path of the field used in a decision table in relation to the object that the field
belongs to.

**Field Type**
boolean

**Description**
Indicates whether an input field is used to group the business rules of the decision
table.

**Field Type**
boolean

**Description**
Indicates whether a field is given priority.

**Field Type**
boolean

**Description**
Indicates whether a field is required to be used for lookups.

**Field Type**
int

**Description**
The maximum number of characters supported for a field that's used in a decision
table.

**Field Type**
DecisionTableOperator (enumeration of type string)


Metadata Types DecisionTable

**Field Name** **Description**

**Description**
Operator used for the input field.

Valid values are:

**•** `Contains`

**•** `DoesNotExistIn`

**•** `DoesNotMatch`

**•** `Equals`

**•** `ExistsIn`

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `IsNotNull`

**•** `IsNull`

**•** `LessOrEqual`

**•** `LessThan`

**•** `Matches`

**•** `NotEquals`

```
sequence

sortType

usage

```

**Field Type**
int

**Description**
The sequence in which input fields are processed. This field is available in API version
52.0 and later.

**Field Type**
DecisionTableSortType (enumeration of type string)

**Description**
Sort outputs of a decision table based on the values of the input or output parameter
field. This field is available in API version 56.0 and later.

Valid values are:

**•** `AscNullFirst`

**•** `AscNullLast`

**•** `DescNullFirst`

**•** `DescNullLast`

**•** `None`

**Field Type**
DecisionTableParameterType (enumeration of type string)

**Description**

Required. Usage type of a field.


Metadata Types DecisionTable

**Field Name** **Description**

Valid values are:

**•** `INPUT`

**•** `OUTPUT`

**•** `ROWCRITERIA`

DecisionTableSourceCriteria

Represents the fields and values from a data source that are used to define the condition logic of the data that's used in a decision table.

**Field Name** **Description**

```
operator

sequenceNumber

sourceFieldName

```

**Field Type**
DTSourceCriteriaOperator (enumeration of type string)

**Description**

Required. The operator that’s applied to an associated decision table’s field to filter
the data.

Valid values are:

**•** `Contains`

**•** `DoesNotExistIn`

**•** `DoesNotMatch`

**•** `Equals`

**•** `ExistsIn`

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `IsNotNull`

**•** `IsNull`

**•** `LessOrEqual`

**•** `LessThan`

**•** `Matches`

**•** `NotEquals`

**Field Type**
int

**Description**

Required. The sequence number used in the associated decision table's source condition
logic.

**Field Type**
string


Metadata Types DecisionTable

**Field Name** **Description**

**Description**

Required. The name of the field that's used in the decision table.

```
value

valueType

```

**Field Type**
string

**Description**
The value that’s expected in the source field used in the decision table.

**Field Type**
DTSourceCriteriaValueType (enumeration of type string)

**Description**

Required. The type of the value that’s used to filter the source data.

Valid values are:

**•** `Formula`

**•** `Literal`

**•** `Lookup`

**•** `Parameter`

**•** `Picklist`

Declarative Metadata Sample Definition

The following is an example of a DecisionTable component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DecisionTable xmlns="http://soap.sforce.com/2006/04/metadata">

   <collectOperator>None</collectOperator>

   <conditionCriteria>1 and 2 and 3 and 4</conditionCriteria>

   <conditionType>All</conditionType>

   <dataSourceType>SingleSobject</dataSourceType>

   <decisionTableParameters>

     <fieldName>IsDeleted</fieldName>

     <operator>Equals</operator>

     <usage>INPUT</usage>

     <sequence>1</sequence>

     <isGroupByField>true</isGroupByField>

     <sortType>AscNullFirst</sortType>

     <dataType>Number</dataType>

     <fieldPath>AccountFeed.CommentsCount</fieldPath>

     <domainObject>AccountFeed</domainObject>

     <isPriorityField>false</isPriorityField>

     <decimalScale>2</decimalScale>

     <length>14</length>

     <isRequired>false</isRequired>

   </decisionTableParameters>

   <decisionTableParameters>

```


Metadata Types DecisionTable

```
        <fieldName>IsActive</fieldName>

        <usage>OUTPUT</usage>

      </decisionTableParameters>

      <decisionTableParameters>

        <fieldName>LimitNumber</fieldName>

        <operator>Equals</operator>

        <usage>INPUT</usage>

        <sequence>2</sequence>

        <isGroupByField>false</isGroupByField>

      </decisionTableParameters>

      <decisionTableParameters>

        <fieldName>LimitStartDate</fieldName>

        <usage>OUTPUT</usage>

      </decisionTableParameters>

      <decisionTableParameters>

        <fieldName>GivenBadgeCount</fieldName>

        <operator>Equals</operator>

        <usage>INPUT</usage>

        <sequence>3</sequence>

        <isGroupByField>false</isGroupByField>

      </decisionTableParameters>

      <decisionTableParameters>

        <fieldName>Name</fieldName>

        <operator>Equals</operator>

        <usage>INPUT</usage>

        <sequence>4</sequence>

        <isGroupByField>false</isGroupByField>

      </decisionTableParameters>

      <decisionTableSourceCriterias>

        <sourceFieldName>IsDeleted</sourceFieldName>

        <operator>Equals</operator>

        <value>false</value>

        <sequenceNumber>1</sequenceNumber>

        <valueType>Literal</valueType>

      </decisionTableSourceCriterias>

      <description>Sample DT created for md-common tests</description>

      <filterResultBy>UniqueValues</filterResultBy>

      <setupName>Sample DT</setupName>

      <sourceObject>WorkBadgeDefinition</sourceObject>

      <sourceConditionLogic>1</sourceConditionLogic>

      <status>Draft</status>

      <type>LowVolume</type>

      <usageType>Bre</usageType>

      <doesConsiderNullValue>false</doesConsiderNullValue>

      <refreshStatus>Failed</refreshStatus>

      <refreshFailureReason>Failed due to limit violation.</refreshFailureReason>

      <executionType>Hbpo</executionType>

      <lastIncrementalSyncDate>""</lastIncrementalSyncDate>

      <uploadStatus>Completed</uploadStatus>

      <isIncrementalSyncEnabled>false</isIncrementalSyncEnabled>

      <hasIncrementalSyncFailed>false</hasIncrementalSyncFailed>

   </DecisionTable>

```


### Metadata Types DecisionTableDatasetLink

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <fullName>Sample DT Package</fullName>

     <description>Package created for md-common tests</description>

     <types>

       <members>Sample_DT</members>

       <name>DecisionTable</name>

     </types>

     <types>

       <members>DSL_Sample</members>

       <members>Sample_DT_Default</members>

       <name>DecisionTableDatasetLink</name>

     </types>

     <version></version>

   </Package>

### DecisionTableDatasetLink

```

Represents the information about a dataset link associated with a decision table. In a dataset link, select an object for whose records,
the decision table must provide an outcome. This type extends the Metadata metadata type and inherits its `fullName` field.

Note: Dataset links are supported only for Standard decision tables.

File Suffix and Directory Location

### DecisionTableDatasetLink components have the suffix .decisionTableDatasetLink and are stored in the

`decisionTableDatasetLinks` folder.

Version

### DecisionTableDatasetLink components are available in API version 51.0 and later.

Special Access Rules

To use this metadata type, your Salesforce org must have the Loyalty Management or the Rebate Management license.

Fields

**Field Name** **Field Type** **Description**

`decisionTableName` string Required. The name of the associated decision table.

`decisionTblDatasetParameters` DecisionTblDatasetParameters Mapping between a decision table parameter and a field of the object
selected in the dataset link.

`description` string The description of the dataset link.


Metadata Types DecisionTableDatasetLink

**Field Name** **Field Type** **Description**

`isDefault` boolean Indicates whether a dataset link is the default dataset link for a decision
table.

`setupName` string Required. The name of the decision table dataset link, which appears in
Setup.

`sourceObject` string Required. The name of the object being evaluated.

DecisionTblDatasetParameters

Represents the mapping between a decision table parameter and a field of the object selected in the dataset link.

The mapping allows the decision table to know which object fields must be compared to the input-output fields of the decision table.

Fields

**Field Name** **Field Type** **Description**

`datasetFieldName` string Required. Name of the dataset field whose value must be compared against
an Input type decision table parameter when providing the outcome.

`fieldName` string Required. The API name of the decision table field that is selected as an input
or output for the decision table dataset link.

Declarative Metadata Sample Definition

The following is an example of a DecisionTableDatasetLink component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DecisionTableDatasetLink xmlns="http://soap.sforce.com/2006/04/metadata">

     <decisionTableName>Sample_DT</decisionTableName>

     <decisionTblDatasetParameters>

       <fieldName>IsDeleted</fieldName>

       <datasetFieldName>IsDeleted</datasetFieldName>

     </decisionTblDatasetParameters>

     <decisionTblDatasetParameters>

       <fieldName>LimitNumber</fieldName>

       <datasetFieldName>CallDurationInSeconds</datasetFieldName>

     </decisionTblDatasetParameters>

     <decisionTblDatasetParameters>

       <fieldName>Name</fieldName>

       <datasetFieldName>Subject</datasetFieldName>

     </decisionTblDatasetParameters>

     <description>DSL created for md-common tests</description>

     <isDefault>false</isDefault>

     <sourceObject>Task</sourceObject>

     <setupName>DSL Sample</setupName>

   </DecisionTableDatasetLink>

```


### Metadata Types DecisionMatrixDefinition

The following is an example of a default DecisionTableDatasetLink component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DecisionTableDatasetLink xmlns="http://soap.sforce.com/2006/04/metadata">

     <decisionTableName>Sample_DT</decisionTableName>

     <isDefault>true</isDefault>

     <sourceObject>WorkBadgeDefinition</sourceObject>

     <setupName>Default DSL Sample</setupName>

   </DecisionTableDatasetLink>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <fullName>Sample DT Package</fullName>

     <description>Package created for md-common tests</description>

     <types>

       <members>Sample_DT</members>

       <name>DecisionTable</name>

     </types>

     <types>

       <members>DSL_Sample</members>

       <members>Sample_DT_Default</members>

       <name>DecisionTableDatasetLink</name>

     </types>

     <version>51.0</version>

   </Package>

### DecisionMatrixDefinition

```

Represents a definition of a decision matrix.

[Note: Before deploying a decision matrix or a decision matrix version to a target org, review these decision matrix migration](https://help.salesforce.com/s/articleView?id=ind.decision_matrix_migration_considerations.htm&type=5&language=en_US)
[considerations.](https://help.salesforce.com/s/articleView?id=ind.decision_matrix_migration_considerations.htm&type=5&language=en_US)

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DecisionMatrixDefinition components have the suffix .decisionMatrixDefinition and are stored in the

`decisionMatrixDefinition` folder.

Version

### DecisionMatrixDefinition components are available in API version 55.0 and later.


Metadata Types DecisionMatrixDefinition

Fields

**Field Name** **Description**

```
description

groupKey

label

processType

subGroupKey

```

**Field Type**
string

**Description**
Describes a decision matrix definition.

**Field Type**
string

**Description**
A key for grouping matrix rows in different versions, such as a geographic region or a
product code.

**Field Type**
string

**Description**

Required.

The UI label of a decision matrix definition.

**Field Type**
ExpsSetProcessType (enumeration of type string)

**Description**
The process type that uses the expression set rule.

Valid values are:

**•** `Bre`

**•** `GpaCalculation`

**•** `InsuranceClaimProcessing` —Available in API version 65.0 and later.

**•** `ItServiceManagement` —Available in API version 65.0 and later.

**•** `PlanCostCalculation`

**•** `RatingDiscovery`

**•** `StudentInformationSystem` —Available in API version 65.0 and later.

**•** `StudentSuccess`

Note: When Business Rules Engine is enabled for a Salesforce instance, the
default value is ' `Bre` ’. Other usage types may be available to you depending
on your industry solution and permission sets.

Available in API version 59.0 and later.

**Field Type**
string


Metadata Types DecisionMatrixDefinition

**Field Name** **Description**

**Description**
A subgroup key for grouping matrix rows in different versions, such as a geographic
region or a product code. For example, if the `groupKey` is `Country`, the
`subGroupKey` can be `State` or `Province` .

```
type

versions

```

**Field Type**
DecisionMatrixType (enumeration of type string)

**Description**
The type of a decision matrix.

Valid values are:

**•** `Grouped`

**•** `Standard`

**Field Type**

DecisionMatrixDefinitionVersion[]

**Description**
Represents an array of decision matrix version definitions in a decision matrix. This
array must contain at least one version.

DecisionMatrixDefinitionVersion

Represents a definition of a decision matrix version.

**Field Name** **Description**

```
columns

decisionMatrixDefinition

endDate

groupKeyValue

```

**Field Type**

DecisionMatrixDefinitionVersionColumn[]

**Description**
Represents an array of columns in a decision matrix definition version.

**Field Type**
string

**Description**
The full name of a decision matrix version.

**Field Type**
dateTime

**Description**
The date until which a decision matrix definition version is available for use.

**Field Type**
string


Metadata Types DecisionMatrixDefinition

**Field Name** **Description**

**Description**
The value of the `groupKey` for a decision matrix definition version. For example, if the
`groupKey` is `Country`, the `groupKeyValue` can be `United States` .

```
label

rank

startDate

status

subGroupKeyValue

```

**Field Type**
string

**Description**

Required.

The UI label of a decision matrix definition version.

**Field Type**
int

**Description**
The rank of the `Decision Matrix Definition Version` . When more than
one enabled version matches a decision matrix call, and the start date time to end date
time spans overlap, the version with the highest rank is chosen. Available in API version
64.0 and later.

**Field Type**
dateTime

**Description**

Required.

The date from when a decision matrix definition version is available for use.

**Field Type**
DecisionMatrixDefStatus (enumeration of type string)

**Description**

Required.

Specifies the status of a decision matrix definition version.

Valid values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**•** `InvalidDraft`

**•** `Obsolete`

**Field Type**
string


Metadata Types DecisionMatrixDefinition

**Field Name** **Description**

**Description**
The value of the subgroup key for a decision matrix definition version. For example, if the
`subGroupKey` is `State` or `Province`, the `subGroupKeyValue` can be
`California` .

```
versionNumber

```

**Field Type**
int

**Description**

Required.

The version number of a decision matrix definition.

DecisionMatrixDefinitionVersionColumn

Represents a definition of a column in a decision matrix definition version.

**Field Name** **Description**

```
columnType

dataType

```

**Field Type**
DecisionMatrixColumnType (enumeration of type string)

**Description**

Required.

Specifies whether a column is for an input or output.

Valid values are:

**•** `Input`

**•** `Output`

**Field Type**
DecisionMatrixDataType (enumeration of type string)

**Description**
Required.

The type of data that’s stored in a column.

Valid values are:

**•** `Boolean`

**•** `Currency`

**•** `Number`

**•** `NumberRange`

**•** `Percent`

**•** `Text`

**•** `TextRange`


Metadata Types DecisionMatrixDefinition

**Field Name** **Description**

```
displaySequence

isWildcardColumn

name

rangeValue

wildcardValue

```

**Field Type**
int

**Description**
Required.

Represents the position of a column in the column order.

**Field Type**
boolean

**Description**
Required.

Specifies whether a column stores a wildcard value ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**
Required.

The full name of a decision matrix definition version column.

**Field Type**
string

**Description**
A list of values that define range boundaries.

**Field Type**
string

**Description**
The wildcard value such as `ALL` .

Declarative Metadata Sample Definition

The following is an example of a DecisionMatrixDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DecisionMatrixDefinition

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <label>HealthCloudUM_ValidRegions</label>

 <type>Standard</type>

 <versions>

  <fullName>HealthCloudUM_ValidRegions_V1</fullName>

  <columns>

  <columnType>Input</columnType>

  <dataType>Text</dataType>

```


### Metadata Types DelegateGroup

```
     <displaySequence>2</displaySequence>

     <isWildcardColumn>false</isWildcardColumn>

     <name>State</name>

     </columns>

     <columns>

     <columnType>Input</columnType>

     <dataType>Text</dataType>

     <displaySequence>1</displaySequence>

     <isWildcardColumn>false</isWildcardColumn>

     <name>City</name>

     </columns>

     <columns>

     <columnType>Output</columnType>

     <dataType>Boolean</dataType>

     <displaySequence>3</displaySequence>

     <isWildcardColumn>false</isWildcardColumn>

     <name>IsValid</name>

     </columns>

     <decisionMatrixDefinition>HealthCloudUM_ValidRegions</decisionMatrixDefinition>

     <label>HealthCloudUM_ValidRegions V1</label>

     <startDate>2022-05-02T13:04:06.000Z</startDate>

     <status>Draft</status>

     <versionNumber>1</versionNumber>

    </versions>

   </DecisionMatrixDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>*</members>

     <name>DecisionMatrixDefinition</name>

    </types>

    <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based.htm)

### DelegateGroup

Represents a group of users who have the same administrative privileges. These groups are different from public groups used for sharing.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types DelegateGroup

File Suffix and Directory Location

DelegateGroup components have the suffix `.delegateGroup` and are stored in the `delegateGroups` folder. The file prefix
must match the developer name of the delegate group. For example, a delegate group with a developer name of MyDelegateGroup
would have a file name of `MyDelegateGroup.delegateGroup` .

Version

DelegateGroup components are available in API version 36.0 and later.

Special Access Rules

Only users with the “View Setup and Configuration” permission can be delegated administrators. As of Spring ’20 and later, only users
with “View Setup” or “Configuration” permission can access this object.

Fields

**Field Name** **Field Type** **Description**

`customObjects` string[] The custom objects associated with the group. Delegated administrators
can customize nearly every aspect of each of those custom objects,

including creating a custom tab. However, they can’t create or modify
relationships on the objects or set organization-wide sharing defaults.
Delegated administrators must have access to custom objects to access
the merge fields on those objects from formulas.

`groups` string[] The groups with users assigned by delegated administrators.

`label` string Required. The delegated group’s non-API name.

`loginAccess` boolean Required. Allows users in this group to log in as users in the role hierarchy
that they administer ( `true` ) or not ( `false` ). Depending on your

organization settings, individual users must grant login access to allow
their administrators to log in as them.

`permissionSetGroups` string[] The permission set groups that can be assigned to users in specified
roles and all subordinate roles by delegated administrators.

`permissionSets` string[] The permission sets that can be assigned to users in specified roles and
all subordinate roles by delegated administrators.

`profiles` string[] The profiles that can be assigned to users by delegated administrators.

`roles` string[] The roles and subordinates for which delegated administrators of the
group can create and edit users.


### Metadata Types DgtAssetMgmtProvider

Declarative Metadata Sample Definition

The following is an example of a DelegateGroup component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DelegateGroup xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>MyDelegateGroup</label>

      <loginAccess>true</loginAccess>

      <name>MyDelegateGroup</name>

      <profiles>Chatter Free User</profiles>

      <profiles>Chatter Moderator User</profiles>

      <profiles>Marketing User</profiles>

      <permissionSetGroups>My Permission Set Group</permissionSetGroups>

      <permissionSets>My Permset</permissionSets>

      <roles>LesserBossMan</roles>

   </DelegateGroup>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>DelegateGroup</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DgtAssetMgmtProvider

Represents external content providers, such as digital asset management (DAM) systems, that integrate with Salesforce CMS. When
combined with the DgtAssetMgmtPrvdLghtCpnt type, this metadata type enables organizations to configure external content systems
as content providers within the Salesforce platform.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### DgtAssetMgmtProvider components have the suffix .dgtAssetMgmtProvider and are stored in the

`dgtAssetMgmtProviders` folder.


Metadata Types DgtAssetMgmtProvider

Version

DgtAssetMgmtProvider components are available in API version 65.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
icon

label

masterLabel

```

**Field Type**
string

**Description**
Stores a reference to the icon resource (typically a Lightning icon or custom image)
that visually represents the external content provider in the user interface.

**Field Type**
string

**Description**
Required. Specifies the display label for the external content provider that users see
when they select or view the provider.

**Field Type**
string

**Description**
Required. Specifies the primary identifier for the provider in metadata contexts and
localization.

Declarative Metadata Sample Definition

The following is an example of a DgtAssetMgmtProvider component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DgtAssetMgmtProvider xmlns="http://soap.sforce.com/2006/04/metadata">

   <icon>My icon</icon>

   <label>My text</label>

   <masterLabel>My text</masterLabel>

</DgtAssetMgmtProvider>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

```


### Metadata Types DgtAssetMgmtPrvdLghtCpnt

```
        <name>DgtAssetMgmtProvider</name>

      </types>

      <version>65.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### DgtAssetMgmtPrvdLghtCpnt

Represents the Lightning web component configurations for external content providers, such as digital asset management (DAM)
systems. This metadata type enables the integration of external content systems with Salesforce CMS using custom Lightning web
components.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### DgtAssetMgmtPrvdLghtCpnt components have the suffix .dgtAssetMgmtPrvdLghtCpnt and are stored in the

`dgtAssetMgmtPrvdLghtCpnts` folder.

Version

### DgtAssetMgmtPrvdLghtCpnt components are available in API version 65.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
dgtAssetMgmtProvider

```

**Field Type**
string

**Description**
Required. References the external content provider, represented by the
DgtAssetMgmtProvider on page 896 type, that this Lightning web component
configuration supports.


Metadata Types DgtAssetMgmtPrvdLghtCpnt

**Field Name** **Description**

```
lightningComponentBundle

masterLabel

type

```

**Field Type**
string

**Description**
References the Lightning web component, represented by the
LightningComponentBundle on page 1491 type, that implements the user interface for
the external content provider in Salesforce CMS.

The LightningComponentBundle must be deployed and available before you reference
it.

**Field Type**
string

**Description**
Required. Specifies the display name of the Lightning web component configuration
as it appears in the UI.

**Field Type**
DgtAssetMgmtPrvdLghtCpntType (enumeration of type string)

**Description**
Required. Specifies the type of external content provider Lightning web component
that’s being configured. Possible values are:

**•** DIGITAL_ASSET_MANAGER: Represents a component that provides full
management capabilities for external content providers, including browsing,
searching, and selecting.

**•** NONE: Represents an undefined or default provider type. Indicates that no specific
provider type is assigned.

Declarative Metadata Sample Definition

The following is an example of a DgtAssetMgmtPrvdLghtCpnt component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DgtAssetMgmtPrvdLghtCpnt xmlns="http://soap.sforce.com/2006/04/metadata">

   <dgtAssetMgmtProvider>External Content Provider</dgtAssetMgmtProvider>

   <lightningComponentBundle>myLightningComponentBundle</lightningComponentBundle>

   <masterLabel>myComponent</masterLabel>

   <type>DIGITAL_ASSET_MANAGER</type>

</DgtAssetMgmtPrvdLghtCpnt>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>DgtAssetMgmtPrvdLghtCpnt</name>

   </types>

```


### Metadata Types DigitalExperienceBundle

```
      <version>65.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### DigitalExperienceBundle

Represents a text-based code structure of your organization’s workspaces, organized by workspace type, and each workspace’s content
items.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DigitalExperienceBundle components have the suffix .digitalExperience and are stored in the digitalExperiences

folder.

### DigitalExperienceBundle uses workspaces and content types to organize your data in a content-focused structure.

**•** Workspace: For enhanced Lightning Web Runtime (LWR) sites, a collection of related content items that form the site when combined
with data from the DigitalExperienceConfig metadata type.

For Salesforce CMS, a collection of related content items contained in a general workspace.

For Marketing Cloud, a collection of related content items contained in a marketing or general workspace.

Note: The maximum length for a workspace name is 80 characters.

**•** Workspace type: A way to categorize different kinds of workspaces. For example, the workspace type for enhanced LWR sites is
`site`, and the workspace type for marketing workspaces in Marketing Cloud is `marketing` . The workspace type determines
which content types are available in the workspace. In the DigitalExperienceBundle folder structure, all workspaces of a given type
are under that workspace type. `site`, `marketing`, and `general` are the supported workspace types.

**•** Content types: A way to categorize different kinds of content in a workspace. For example, all routes in an enhanced LWR site are
stored under a content type folder called `sfdc_cms__route` . Similarly, forms for a marketing workspace are stored under a
content type folder called `sfdc_cms__form` .

**•** Content items: For enhanced LWR sites, the individual settings and site components that make up an enhanced LWR site. For example,
each of the routes in an enhanced LWR site is a single content item.

For marketing workspaces, the content items used in marketing campaigns. For example, each form in a workspace is a single content
item.

Here’s an example of the DigitalExperienceBundle structure.


Metadata Types DigitalExperienceBundle

When retrieved, DigitalExperienceBundle contains workspace type folders (1) under the digitalExperiences folder.

The marketing folder contains one or more workspace folders (2), each representing a marketing workspace in Marketing Cloud. The
site folder contains one or more workspace folders (3), each representing the workspace for an individual enhanced LWR site. Each
workspace folder contains an `XML` file with information about the workspace, such as the label. For enhanced LWR sites, be sure to
keep the label value in sync with the site’s network name.

Each workspace folder also contains several content type folders that represent each of the different content types (4) used in that
workspace. For example, marketing workspaces support landing pages, forms, emails, and referenced images and branding.

Finally, each content type folder can contain one or more content subfolders. Each content subfolder can contain additional subfolders
and several files that, when combined, represent an individual content item, such as a specific view (5).

**•** A `_meta.json` file that contains the metadata for the content item. Use the `_meta.json` file to learn the location of a content
item within the workspace, or to move the content item to another location, including creating a new location for the content item.
You can also use the `_meta.json` file to view a content item’s parent-child relationships, to move the content item from one
parent to another, or to remove a parent-child relationship entirely.

**•** A `content.json` file that contains the primary version of the content item. Each `content.json` file includes values for the
content item’s type, title, and content body. Use this file to edit the content’s properties on your local machine or scratch org and
then deploy.

**•** If applicable, additional `JSON` files that represent variants of the content item, such as language translations.

Note: Before you deploy the DigitalExperienceBundle in a target org, make sure that any translated variants of content in the
target org are also in the source org. If the target org contains a `JSON` file for a translated variant that isn’t in the source org,
deploying the DigitalExperienceBundle fails.

The `_meta.json` file contains several properties:


Metadata Types DigitalExperienceBundle

Version

DigitalExperienceBundle components are available in API version 56.0 and later.


Metadata Types DigitalExperienceBundle

Special Access Rules

In Experience Cloud, you can use DigitalExperienceBundle for enhanced LWR sites created in Winter ’23 or later. For Aura sites and other
LWR sites, use the ExperienceBundle (recommended) or the SiteDotCom on page 2321 metadata types. Packaging is unsupported for
enhanced LWR sites.

In Salesforce CMS and in Marketing Cloud, you must have a contributor role in a workspace to retrieve it. For Marketing Cloud, you can
package the content of general and marketing workspaces, including landing pages, forms, and emails (and their associated images
and branding).

Fields

**Field Name** **Description**

```
description

digitalExperienceFolderShares

label

spaceResources

```

DigitalExperience

**Field Type**
string

**Description**
Contains the description of the workspace.

For site workspaces, this value is empty.

**Field Type**

DigitalExperienceFolderShare[]

**Description**
The list of folders in the source marketing workspace that are shared with target
marketing workspaces.

Available in API version 61.0 and later.

**Field Type**
string

**Description**
Required.

A user-friendly name for DigitalExperienceBundle, which is defined when the
DigitalExperienceBundle is created.

**Field Type**

DigitalExperience[]

**Description**
The list of resources in this DigitalExperienceBundle. Each resource represents a content
type, such as views, routes, themes, and languageSettings.

Represents content in the bundle. When retrieved as part of DigitalExperienceBundle, DigitalExperience represents all content for the
requested workspace or workspaces. When retrieved on its own, DigitalExperience represents only the content types you specify.


Metadata Types DigitalExperienceBundle

This subtype extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

When you retrieve DigitalExperience, the folder structure matches that of DigitalExperienceBundle, with only the specified content
returned.

**Field Name** **Description**

```
fileName

filePath

format

```

**Field Type**
string

**Description**
Required.

Name of the resource file.

**Field Type**
string

**Description**
Path to the file within the artifact folder.

**Field Type**
string

**Description**
Required.

Only `JSON` is allowed.

DigitalExperienceFolderShare

Represents a folder in a source marketing workspace that’s shared with other target marketing workspaces. Available in API version 61.0
and later.

**Field Name** **Description**

```
folderPath

sharedWith

```

SharedWith

**Field Type**
string

**Description**
The root folder of the shared workspace. The allowed value is `_root` .

**Field Type**

SharedWith[]

**Description**
The list of target workspaces that the source workspace is shared with.

Represents a target marketing workspace that the source marketing workspace is shared with. Available in API version 61.0 and later.


Metadata Types DigitalExperienceBundle

**Field Name** **Description**

```
fullyQualifiedName

```

**Field Type**
string

**Description**
The target workspace that the source workspace is shared with. It uses the format
_`workspace_type`_ / _`target_workspace_name`_ . For example,
`marketing/Workspace2` .

Declarative Metadata Sample Definition

The following is an example of a DigitalExperienceBundle component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DigitalExperienceBundle xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>content</description>

   <label>isv1</label>

</DigitalExperienceBundle>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>site/isv1</members>

     <name>DigitalExperienceBundle</name>

   </types>

   <version>56.0</version>

</Package>

```

Usage

Tip: Before you update the `JSON` files of an Experience Builder site, we recommend making a copy of the site’s folder as a backup.

To retrieve and deploy DigitalExperienceBundle, use legacy sfdx commands.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

DigitalExperienceBundle: Marketing Workspace Bundle and Folders
DigitalExperienceBundle uses the `marketing` workspace type to organize content items used in marketing campaigns in a
content-focused, text-based code structure.

DigitalExperienceBundle: Site Workspace Bundle and Folders
DigitalExperienceBundle uses the `site` workspace type to organize data for enhanced LWR sites in a content-focused, text-based
code structure.


#### Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and

Folders

#### DigitalExperienceBundle: Marketing Workspace Bundle and Folders

DigitalExperienceBundle uses the `marketing` workspace type to organize content items used in marketing campaigns in a
content-focused, text-based code structure.

For Marketing Cloud, the `marketing` folder contains one or more workspace folders, each representing an individual marketing
workspace. Each workspace folder contains a collection of related content items, such as landing pages, forms, and emails, and their
associated images and branding.

The folder for each marketing workspace includes content type folders, content item subfolders, and associated data that's contained
in `content.json` and `_meta.json` files.

The following content type folders represent the content types that are supported in a marketing workspace. For example, forms for a
marketing workspace are stored under a content type folder called `sfdc_cms__form` .

**•** sfdc_cms__brand Folder

**•** sfdc_cms__brandSettings Folder

**•** sfdc_cms__email Folder

**•** sfdc_cms__form Folder

**•** sfdc_cms__image Folder

**•** sfdc_cms__landingPage Folder

**•** sfdc_cms__languageSettings Folder

sfdc_cms__brand Folder

This content type folder contains one content subfolder per brand. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__brand",

     "title" : "brand 1",

     "contentBody" : {

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
      "baseFontFamily" : "{!$brand.fontFamily.arial}",

      "baseFontSize" : {

       "unit" : "px",

       "value" : 16.0

      },

      "borderRadius" : {

       "round" : {

        "unit" : "rem",

        "value" : 0.25

       },

       "square" : {

        "unit" : "rem",

        "value" : 0.0

       }

      },

      "borderWeight" : {

       "medium" : {

        "unit" : "rem",

        "value" : 0.125

       },

       "none" : {

        "unit" : "rem",

        "value" : 0.0

       },

       ...

      },

      "buttonStyleGroup" : {

       "primary" : {

        "lightning:borderRadius" : "{!$brand.borderRadius.round}",

        "lightning:borderWidth" : "{!$brand.borderWeight.thin}",

        "lightning:buttonColorGroup" : {

         "backgroundColor" : "{!$brand.colorScheme.primaryAccent}",

         "backgroundHoverColor" : "{!$brand.colorScheme.primaryAccentDerived}",

         "borderColor" : "{!$brand.colorScheme.primaryAccent}",

         "borderHoverColor" : "{!$brand.colorScheme.primaryAccentDerived}",

         "textColor" : "{!$brand.colorScheme.primaryAccentContrast}",

         "textHoverColor" : "{!$brand.colorScheme.primaryAccentContrastDerived}"

        },

        "lightning:padding" : {

         "bottom" : {

           "unit" : "rem",

           "value" : 0.5

         },

         ...

        },

        "lightning:typography" : "{!$brand.typography.button.button1}"

       },

       "secondary" : {...},

       "tertiary" : {...}

      },

      "colorScheme" : {

       "contrast" : "#000000",

       "neutral" : "#747474",

       "primaryAccent" : "#99F077",

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
       "primaryAccentContrast" : "#ffffff",

       "primaryAccentContrastDerived" : "#000000",

       "primaryAccentDerived" : "#7fd65f",

       "root" : "#ffffff"

      },

      "fontFamily" : {

       "arial" : {

        "category" : "sans-serif",

        "fallbacks" : [ "Helvetica" ],

        "name" : "Arial"

       },

       "arialBlack" : {

        "category" : "sans-serif",

        "fallbacks" : [ "Gadget" ],

        "name" : "Arial Black"

       },

       ...

      },

      "fontSize" : {

       "large" : {

        "unit" : "rem",

        "value" : 1.125

       },

       "medium" : {

        "unit" : "rem",

        "value" : 1.0

       },

       ...

      },

      "spacing" : {

       "large" : {

        "bottom" : {

         "unit" : "rem",

         "value" : 1.5

        },

        "left" : {

         "unit" : "rem",

         "value" : 1.5

        },

        "right" : {

         "unit" : "rem",

         "value" : 1.5

        },

        "top" : {

         "unit" : "rem",

         "value" : 1.5

        }

       },

       ...

      },

      "typography" : {

       "button" : {

        "button1" : {

         "fontFamily" : "{!$brand.baseFontFamily}",

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
         "fontSize" : "{!$brand.fontSize.medium}",

         "fontWeight" : "{!$brand.fontWeight.normal}",

         "letterSpacing" : "normal",

         "lineHeight" : 1.5,

         "textTransform" : "none"

        }

       },

       ...

      },

      ...

      "lightning:dataProviders" : [ ],

      "sfdc_cms:einsteinBrandProperties" : {

       "personality" : {

        "defaultPersonality" : "professional"

       }

      },

      "sfdc_cms:variants" : [ ]

     },

     "urlName" : "brand-1",

     "sfdc_cms:title" : "brand 1",

   }

```

sfdc_cms__brandSettings Folder

This content type folder contains one content subfolder called brandSettings. The brandSettings content subfolder contains two or
more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__brandSettings",

     "title" : "Brand Settings",

     "contentBody" : {

      "defaultBrand" : "brand3"

     },

     "urlName" : "brand-settings"

   }

```

sfdc_cms__email Folder

This content type folder contains one content subfolder per email. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

Note: In marketing workspaces, the default data graph, personalization recommenders, personalization points, and decisions
aren't included in the bundle. If the workspace includes emails with personalized content that’s based on these objects, then:

**•** Any merge field or repeater that uses the default data graph or a personalization recommender from the source org is broken
in the target org.

**•** Any dynamic content variations of email components are removed and only the default variations appear in the email.

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__email",

     "title" : "Email_marketingSpaceA",

     "contentBody" : {

      "backgroundColor" : "#f3f3f3",

      "lightning:brandSource" : {

       "defaultBrandOption" : "sfdcBrand"

      },

      "lightning:colorScheme" : "{!$brand.colorScheme}",

      "lightning:dataProviders" : [ {

       "attributes" : {

        "objectApiName" : "UnifiedIndividual__dlm"

       },

       "definition" : "sfdc_cms__unifiedIndividualDataProvider",

       "sfdcExpressionKey" : "unifiedIndividual"

      } ],

      "lightning:padding" : "{!$brand.spacing.none}",

      "messagePurpose" : "promotional",

      "sfdc_cms:block" : {

       "definition" : "sfdc_cms/rootContentBlock",

       "id" : "6458e24b-c1a8-4f7d-b6f0-3659c092f1c3",

       "type" : "block",

       "children" : [ {

        "attributes" : {

         "lightning:borderRadius" : "{!$brand.borderRadius.square}",

         "lightning:borderWidth" : "{!$brand.borderWeight.none}",

         "lightning:colorScheme" : "{!$brand.colorScheme}",

         "lightning:margin" : "{!$brand.spacing.none}",

         "lightning:padding" : "{!$brand.spacing.xSmall}",

         "stackOnMobile" : true,

         "lightning:backgroundImage" : {

           "repeat" : "no-repeat",

           "position" : "center center",

           "size" : "cover"

         }

        },

        "definition" : "lightning/section",

        "id" : "b61c4d08-7985-41f2-a38c-7f8338e56e00",

        "type" : "block",

        "children" : [ {

         "attributes" : {

           "columnWidth" : 12.0,

           "lightning:borderRadius" : "{!$brand.borderRadius.square}",

           "lightning:borderWidth" : "{!$brand.borderWeight.none}",

           "lightning:colorScheme" : "{!$brand.colorScheme}",

           "lightning:margin" : "{!$brand.spacing.none}",

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
           "lightning:padding" : "{!$brand.spacing.xSmall}",

           "lightning:verticalAlignment" : "top",

           "lightning:backgroundImage" : {

            "repeat" : "no-repeat",

            "position" : "center center",

            "size" : "cover"

           }

         },

         "definition" : "lightning/column",

         "id" : "778d9976-82ec-49aa-a3de-ac6485332434",

         "type" : "block",

         "children" : [ ]

        } ]

       } ]

      },

      "sfdc_cms:title" : "Email_marketingSpaceA",

      "subjectLine" : "Email_marketingSpaceA subject{!$organization.Address}",

      "lightning:expressions" : [ ],

      "lightning:backgroundImage" : {

       "repeat" : "no-repeat",

       "position" : "center center",

       "size" : "cover"

      },

      "sfdc_cms:variants" : [ ]

     },

     "urlName" : "email-mk1"

   }

```

sfdc_cms__form Folder

This content type folder contains one content subfolder per form. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__form",

     "title" : "Form1_mk1",

     "contentBody" : {

      "lightning:brandSource" : {

       "defaultBrandOption" : "sfdcBrand"

      },

      "lightning:dataProviders" : [ {

       "attributes" : {

        "objectApiName" : "Account",

        "recordTypeId" : "012000000000000AAA"

       },

       "definition" : "sfdc_cms__recordDataProvider",

       "sfdcExpressionKey" : "Flow1"

      } ],

      "sfdc_cms:block" : {

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
       "definition" : "sfdc_cms/rootContentBlock",

       "id" : "fef7b2b0-5ddf-4f0e-b0d5-cdbc77a897e9",

       "type" : "block",

       "children" : [ {

        "attributes" : {

         "lightning:borderRadius" : "{!$brand.borderRadius.square}",

         "lightning:borderWidth" : "{!$brand.borderWeight.none}",

         "lightning:colorScheme" : "{!$brand.colorScheme}",

         "lightning:margin" : "{!$brand.spacing.none}",

         "lightning:padding" : "{!$brand.spacing.xSmall}",

         "stackOnMobile" : true,

         "lightning:backgroundImage" : {

           "repeat" : "no-repeat",

           "position" : "center center",

           "size" : "cover"

         }

        },

        "definition" : "lightning/section",

        "id" : "43dc4273-47e2-43ad-9e64-f0862eb0fcdf",

        "type" : "block",

        "children" : [ {

         "attributes" : {

           "columnWidth" : 12.0,

           "lightning:borderRadius" : "{!$brand.borderRadius.square}",

           "lightning:borderWidth" : "{!$brand.borderWeight.none}",

           "lightning:colorScheme" : "{!$brand.colorScheme}",

           "lightning:margin" : "{!$brand.spacing.none}",

           "lightning:padding" : "{!$brand.spacing.xSmall}",

           "lightning:verticalAlignment" : "top",

           "lightning:backgroundImage" : {

            "repeat" : "no-repeat",

            "position" : "center center",

            "size" : "cover"

           }

         },

         "definition" : "lightning/column",

         "id" : "95fc1b5c-481d-4d32-bd03-fec0a4d7aaa0",

         "type" : "block",

         "children" : [ {

           "attributes" : {

            "lightning:borderRadius" : "{!$brand.borderRadius.square}",

            "lightning:borderWidth" : "{!$brand.borderWeight.none}",

            "lightning:formInputColorGroup" : {

             "backgroundColor" : "{!$brand.colorScheme.root}",

             "borderColor" : "{!$brand.colorScheme.neutral}",

             "textColor" : "{!$brand.colorScheme.contrast}"

            },

            "lightning:horizontalAlignment" : "left",

            "lightning:inputTypography" : "{!$brand.typography.input.input1}",

            "lightning:labelTypography" : "{!$brand.typography.label.label1}",

            "lightning:margin" : "{!$brand.spacing.none}",

            "lightning:padding" : "{!$brand.spacing.none}",

            "maxLength" : 255.0,

            "sfdc_cms:fieldReference" : "{!Flow1.Name}",

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
            "sfdc_cms:formInputLabelProperty" : "Account Name",

            "sfdc_cms:formInputNameProperty" : "Name",

            "sfdc_cms:formInputRequiredProperty" : true,

            "width" : "auto"

           },

           "definition" : "lightning/inputText",

           "id" : "6aac0596-26c6-457a-9a9a-cc43ba622739",

           "type" : "block"

         } ]

        } ]

       }, {

        "attributes" : {

         "lightning:borderRadius" : "{!$brand.borderRadius.square}",

         "lightning:borderWidth" : "{!$brand.borderWeight.none}",

         "lightning:colorScheme" : "{!$brand.colorScheme}",

         "lightning:margin" : "{!$brand.spacing.none}",

         "lightning:padding" : "{!$brand.spacing.xSmall}",

         "stackOnMobile" : true,

         "lightning:backgroundImage" : {

           "repeat" : "no-repeat",

           "position" : "center center",

           "size" : "cover"

         }

        },

        "definition" : "lightning/section",

        "id" : "7fe6298e-8c83-4dac-9596-02c629fdc519",

        "type" : "block",

        "children" : [ {

         "attributes" : {

           "columnWidth" : 12.0,

           "lightning:borderRadius" : "{!$brand.borderRadius.square}",

           "lightning:borderWidth" : "{!$brand.borderWeight.none}",

           "lightning:colorScheme" : "{!$brand.colorScheme}",

           "lightning:margin" : "{!$brand.spacing.none}",

           "lightning:padding" : "{!$brand.spacing.xSmall}",

           "lightning:verticalAlignment" : "top",

           "lightning:backgroundImage" : {

            "repeat" : "no-repeat",

            "position" : "center center",

            "size" : "cover"

           }

         },

         "definition" : "lightning/column",

         "id" : "976bff41-3fa9-4d04-aaf8-3590cb87909f",

         "type" : "block",

         "children" : [ {

           "attributes" : {

            "lightning:borderRadius" :

   "{!$brand.buttonStyleGroup.primary.lightning:borderRadius}",

            "lightning:borderWidth" :

   "{!$brand.buttonStyleGroup.primary.lightning:borderWidth}",

            "lightning:buttonColorGroup" :

   "{!$brand.buttonStyleGroup.primary.lightning:buttonColorGroup}",

            "lightning:horizontalAlignment" : "center",

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
            "lightning:margin" : "{!$brand.spacing.none}",

           "lightning:padding" : "{!$brand.buttonStyleGroup.primary.lightning:padding}",

            "lightning:typography" :

   "{!$brand.buttonStyleGroup.primary.lightning:typography}",

            "sfdc_cms:styleGroup" : "{!$brand.buttonStyleGroup.primary}",

            "text" : "Submit",

            "width" : "auto",

            "lightning:click" : {

             "actions" : [ {

              "definition" : "sfdc_cms/customEventAction",

              "attributes" : {

               "type" : "formsubmit",

               "options" : {

                 "bubbles" : true

               }

              }

             } ]

            }

           },

           "definition" : "lightning/actionButton",

           "id" : "84c67ba2-fffc-46d1-80af-35e66ae85ef3",

           "type" : "block"

         } ]

        } ]

       } ]

      },

      "sfdc_cms:title" : "Form1_mk1",

      "formsubmission" : {

       "actions" : [ {

        "definition" : "sfdc_cms/umaFormSubmissionAction",

        "attributes" : {

         "formId" : "{!$form.id}",

         "pageReferenceId" : "{!$page.id}",

         "formData" : "{!$form.fields}"

        }

       }, {

        "definition" : "sfdc_cms/showThankYouAction",

        "attributes" : {

         "message" : "Thank you for your submission."

        }

       } ]

      }

     },

     "urlName" : "form1-mk1"

   }

```

sfdc_cms__image Folder

This content type folder contains one content subfolder per image. Each content subfolder contains two or more `JSON` files and a
`_media` subfolder that contains the image file.

**•** `_meta.json`

**•** `content.json`


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__image",

     "title" : "Img1_mk1",

     "contentBody" : {

      "sfdc_cms:media" : {

       "source" : {

        "mimeType" : "image/png",

        "ref" : "0sNSB000001rKsr2AE",

        "type" : "file",

        "size" : 538158

       }

      }

     },

     "urlName" : "img1-mk1"

   }

```

sfdc_cms__landingPage Folder

This content type folder contains one content subfolder per landing page. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__landingPage",

     "title" : "LandingPageA_marketingSpaceA",

     "contentBody" : {

      "lightning:brandSource" : {

       "defaultBrandOption" : "sfdcBrand"

      },

      "sfdc_cms:block" : {

       "definition" : "sfdc_cms/rootContentBlock",

       "id" : "ac065643-646a-4b1e-b5ed-7eeeed90d0d3",

       "type" : "block",

       "children" : [ {

        "attributes" : {

         "lightning:borderRadius" : "{!$brand.borderRadius.square}",

         "lightning:borderWidth" : "{!$brand.borderWeight.none}",

         "lightning:colorScheme" : "{!$brand.colorScheme}",

         "lightning:margin" : "{!$brand.spacing.none}",

         "lightning:padding" : "{!$brand.spacing.xSmall}",

         "stackOnMobile" : true,

         "lightning:backgroundImage" : {

           "repeat" : "no-repeat",

           "position" : "center center",

           "size" : "cover"

         }

        },

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
        "definition" : "lightning/section",

        "id" : "f6371eda-aafc-4164-a18f-284e49071b76",

        "type" : "block",

        "children" : [ {

         "attributes" : {

           "columnWidth" : 12.0,

           "lightning:borderRadius" : "{!$brand.borderRadius.square}",

           "lightning:borderWidth" : "{!$brand.borderWeight.none}",

           "lightning:colorScheme" : "{!$brand.colorScheme}",

           "lightning:margin" : "{!$brand.spacing.none}",

           "lightning:padding" : "{!$brand.spacing.xSmall}",

           "lightning:verticalAlignment" : "top",

           "lightning:backgroundImage" : {

            "repeat" : "no-repeat",

            "position" : "center center",

            "size" : "cover"

           }

         },

         "definition" : "lightning/column",

         "id" : "db82b936-f2d8-4d47-b373-71dff7fc1f1d",

         "type" : "block",

         "children" : [ {

           "attributes" : {

            "imageFitConfig" : {

             "width" : {

              "unit" : "%",

              "value" : 100.0

             }

            },

            "imageInfo" : {

             "altText" : "",

             "overrideAltText" : false,

             "source" : {

              "ref" : "Img1_mk1",

              "type" : "imageReference"

             },

             "url" : "/cms/media/MCWJDAQWY2HREBRENINOZIKNNVNM"

            },

            "lightning:borderRadius" : "{!$brand.borderRadius.square}",

            "lightning:borderWidth" : "{!$brand.borderWeight.none}",

            "lightning:colorGroup" : {

             "backgroundColor" : "{!$brand.colorScheme.root}",

             "borderColor" : "{!$brand.colorScheme.neutral}",

             "linkColor" : "{!$brand.colorScheme.primaryAccent}",

             "textColor" : "{!$brand.colorScheme.contrast}"

            },

            "lightning:horizontalAlignment" : "center",

            "lightning:margin" : "{!$brand.spacing.none}",

            "lightning:padding" : "{!$brand.spacing.none}",

            "lightning:typography" : "{!$brand.typography.paragraph.paragraph1}"

           },

           "definition" : "lightning/image",

           "id" : "6775db07-8343-420c-918a-0d91c193902d",

           "type" : "block"

```


#### Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
         } ]

        } ]

       } ]

      },

      "sfdc_cms:seoProperties" : {

       "isIndexed" : false,

       "title" : "LandingPageA_marketingSpaceA"

      },

      "sfdc_cms:title" : "LandingPageA_marketingSpaceA",

      "lightning:dataProviders" : [ ],

      "lightning:backgroundImage" : {

       "repeat" : "no-repeat",

       "position" : "center center",

       "size" : "cover"

      }

     },

     "urlName" : "lp1-mk1"

   }

```

sfdc_cms__languageSettings Folder

This content type folder contains one content subfolder called languages. The languages content subfolder contains two or more `JSON`
files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__languageSettings",

     "title" : "LanguageContent",

     "contentBody" : {

      "languages" : [ {

       "locale" : "en_US",

       "label" : "English (US)",

       "isActive" : true,

       "isAuthoringOnly" : false

      } ],

      "defaultLocale" : "en_US"

     },

     "urlName" : "languagecontent"

   }

#### DigitalExperienceBundle: Site Workspace Bundle and Folders

```

DigitalExperienceBundle uses the `site` workspace type to organize data for enhanced LWR sites in a content-focused, text-based code
structure.

The `site` folder contains one or more workspace folders, each representing the workspace for an individual enhanced LWR site. Each
workspace folder contains a collection of related content items, such as settings and site components, that form the site when combined
with data from the DigitalExperienceConfig metadata type.


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

The workspace folder for each site includes content type folders, content item subfolders, and associated data that's contained in
`content.json` and `_meta.json` files.

The following content type folders represent the content types that are supported in an enhanced LWR site. For example, all routes in
an enhanced LWR site are stored under the `sfdc_cms__route` content type folder.

**•** sfdc_cms__appPage Folder

**•** sfdc_cms__brandingSet Folder

**•** sfdc_cms__languageSettings Folder

**•** sfdc_cms__route Folder

**•** sfdc_cms__site Folder

**•** sfdc_cms__theme Folder

**•** sfdc_cms__themeLayout Folder

**•** sfdc_cms__view Folder

sfdc_cms__appPage Folder

This content type folder exists at the root level and contains one content subfolder that represents the site’s single-page application.
Only one `sfdc_cms__appPage` content item is allowed per site.

The content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
{

  "type" : "sfdc_cms__appPage",

  "title" : "main",

  "contentBody" : {

   "currentThemeId" : "Build_Your_Own_LWR",

   "headMarkup" : "<meta charset=\"UTF-8\" />\n<meta name=\"viewport\"

content=\"width=device-width, initial-scale=1\" />\n<title>Welcome to LWC

Communities!</title>\n\n<link rel=\"stylesheet\" href=\"{ basePath

}/assets/styles/styles.css?{ versionKey }\" />\n\n\n<!-- webruntime-branding-shared

stylesheets -->\n<link rel=\"stylesheet\" href=\"{ basePath

}/assets/styles/salesforce-lightning-design-system.min.css?{ versionKey }\" />\n<link

rel=\"stylesheet\" href=\"{ basePath }/assets/styles/dxp-site-spacing-styling-hooks.min.css?{

 versionKey }\" />\n<link rel=\"stylesheet\" href=\"{ basePath

}/assets/styles/dxp-styling-hooks.min.css?{ versionKey }\" />\n<link rel=\"stylesheet\"

href=\"{ basePath }/assets/styles/dxp-slds-extensions.min.css?{ versionKey }\" />\n\n\n<!-
 webruntime-branding-shared stylesheets -->",

   "isLockerServiceEnabled" : true,

   "isRelaxedCSPLevel" : false,

   "templateName" : "talon-template-byo"

  }

}

```

sfdc_cms__brandingSet Folder

This content type folder contains one content subfolder per branding set. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
<apiName> /content.json

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
   {

     "type" : "sfdc_cms__brandingSet",

     "title" : "Build Your Own (LWR)",

     "contentBody" : {

      "brandingSetType" : "APP",

      "definitionName" : "talon-template-byo:branding",

      "values" : {

       "BackgroundColor" : "#ffffff",

       "BaseFontSize" : "1rem",

       "BodyFont" : "Salesforce Sans",

       "BodyFontSize" : "1rem",

       "BodyFontStyle" : "normal",

       "BodyFontWeight" : "400",

       "BodyLetterSpacing" : "0em",

       "BodyLineHeight" : "1.5",

       "BodySmallFont" : "Salesforce Sans",

       "BodySmallFontSize" : "0.75rem",

       "BodySmallFontStyle" : "normal",

       "BodySmallFontWeight" : "400",

       "BodySmallLetterSpacing" : "0em",

       "BodySmallLineHeight" : "1.25",

       "BodySmallTextColor" : "var(--dxp-g-root-contrast)",

       "BodySmallTextDecoration" : "none",

       "BodySmallTextTransform" : "none",

       "BodyTextColor" : "var(--dxp-g-root-contrast)",

       "BodyTextDecoration" : "none",

       "BodyTextTransform" : "none",

       "ButtonActiveColor" : "var(--dxp-s-button-color-1)",

       "ButtonBorderRadius" : "4px",

       "ButtonColor" : "var(--dxp-g-brand)",

       "ButtonFocusColor" : "var(--dxp-s-button-color-1)",

       "ButtonFont" : "Salesforce Sans",

       "ButtonFontSize" : "1rem",

       "ButtonFontStyle" : "normal",

       "ButtonFontWeight" : "400",

       "ButtonHoverColor" : "var(--dxp-s-button-color-1)",

       "ButtonLargeBorderRadius" : "4px",

       "ButtonLargeFontSize" : "1.25rem",

       "ButtonLargePadding" : "1.25rem",

       "ButtonLetterSpacing" : "0em",

       "ButtonLineHeight" : "2",

       "ButtonPadding" : "1rem",

       "ButtonSmallBorderRadius" : "4px",

       "ButtonSmallFontSize" : "0.75rem",

       "ButtonSmallPadding" : "0.75rem",

       "ButtonTextTransform" : "none",

       "ColumnSpacerSizeDesktop" : "1rem",

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
       "ColumnSpacerSizeMobile" : "0.75rem",

       "ComponentSpacerSizeDesktop" : "1.5rem",

       "ComponentSpacerSizeMobile" : "1.5rem",

       "DropdownBackgroundColor" : "var(--dxp-g-root)",

       "DropdownBackgroundHoverColor" : "var(--dxp-g-neutral)",

       "DropdownBorderColor" : "var(--dxp-g-neutral)",

       "DropdownTextColor" : "var(--dxp-g-root-contrast)",

       "DropdownTextHoverColor" : "var(--dxp-g-neutral-contrast)",

       "FormElementBackgroundColor" : "var(--dxp-g-root)",

       "FormElementBorderColor" : "var(--dxp-g-neutral-3)",

       "FormElementBorderRadius" : "4px",

       "FormElementBorderWidth" : "1px",

       "FormElementLabelColor" : "var(--dxp-g-root-contrast)",

       "FormElementTextColor" : "var(--dxp-g-root-contrast)",

       "HeadingExtraLargeColor" : "var(--dxp-g-root-contrast)",

       "HeadingExtraLargeFont" : "Salesforce Sans",

       "HeadingExtraLargeFontSize" : "2.5rem",

       "HeadingExtraLargeFontStyle" : "normal",

       "HeadingExtraLargeFontWeight" : "300",

       "HeadingExtraLargeLetterSpacing" : "0em",

       "HeadingExtraLargeLineHeight" : "1.25",

       "HeadingExtraLargeTextDecoration" : "none",

       "HeadingExtraLargeTextTransform" : "none",

       "HeadingLargeColor" : "var(--dxp-g-root-contrast)",

       "HeadingLargeFont" : "Salesforce Sans",

       "HeadingLargeFontSize" : "1.75rem",

       "HeadingLargeFontStyle" : "normal",

       "HeadingLargeFontWeight" : "300",

       "HeadingLargeLetterSpacing" : "0em",

       "HeadingLargeLineHeight" : "1.25",

       "HeadingLargeTextDecoration" : "none",

       "HeadingLargeTextTransform" : "none",

       "HeadingMediumColor" : "var(--dxp-g-root-contrast)",

       "HeadingMediumFont" : "Salesforce Sans",

       "HeadingMediumFontSize" : "1.25rem",

       "HeadingMediumFontStyle" : "normal",

       "HeadingMediumFontWeight" : "300",

       "HeadingMediumLetterSpacing" : "0em",

       "HeadingMediumLineHeight" : "1.25",

       "HeadingMediumTextDecoration" : "none",

       "HeadingMediumTextTransform" : "none",

       "HeadingSmallColor" : "var(--dxp-g-root-contrast)",

       "HeadingSmallFont" : "Salesforce Sans",

       "HeadingSmallFontSize" : "1.125rem",

       "HeadingSmallFontStyle" : "normal",

       "HeadingSmallFontWeight" : "300",

       "HeadingSmallLetterSpacing" : "0em",

       "HeadingSmallLineHeight" : "1.25",

       "HeadingSmallTextDecoration" : "none",

       "HeadingSmallTextTransform" : "none",

       "HorizontalRowPaddingDesktop" : "1rem",

       "HorizontalRowPaddingMobile" : "0.75rem",

       "LinkColor" : "var(--dxp-g-brand)",

       "LinkHoverColor" : "var(--dxp-s-link-text-color-1)",

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
       "LinkTextDecoration" : "none",

       "LinkTextDecorationFocus" : "underline",

       "LinkTextDecorationHover" : "underline",

       "MaxContentWidthDesktop" : "1800px",

       "MaxContentWidthMobile" : "none",

       "MobileBaseFontSize" : "1rem",

       "PrimaryAccentColor" : "#005fb2",

       "PrimaryAccentForegroundColor" : "#ffffff",

       "SiteLogo" : "",

       "TextColor" : "#1a1b1e",

       "VerticalRowPaddingDesktop" : "1rem",

       "VerticalRowPaddingMobile" : "0.75rem",

       "_BackgroundColor1" : "#ebebeb",

       "_BackgroundColor2" : "#c2c2c2",

       "_BackgroundColor3" : "#858585",

       "_ButtonActiveColorContrast" : "var(--dxp-g-brand-contrast-1)",

       "_ButtonColor1" : "var(--dxp-g-brand-1)",

       "_ButtonColorContrast" : "var(--dxp-g-brand-contrast)",

       "_ButtonFocusColorContrast" : "var(--dxp-g-brand-contrast-1)",

       "_ButtonHoverColorContrast" : "var(--dxp-g-brand-contrast-1)",

       "_DestructiveColor" : "#c23934",

       "_DestructiveColor1" : "#a2302b",

       "_DestructiveColor2" : "#611d1a",

       "_DestructiveColor3" : "#010000",

       "_DestructiveForegroundColor" : "#ffffff",

       "_DestructiveForegroundColor1" : "#ffffff",

       "_DestructiveForegroundColor2" : "#ffffff",

       "_DestructiveForegroundColor3" : "#ffffff",

       "_InfoColor" : "#16325c",

       "_InfoColor1" : "#0e203b",

       "_InfoColor2" : "#000000",

       "_InfoColor3" : "#000000",

       "_InfoForegroundColor" : "#ffffff",

       "_InfoForegroundColor1" : "#ffffff",

       "_InfoForegroundColor2" : "#ffffff",

       "_InfoForegroundColor3" : "#ffffff",

       "_LinkColor1" : "var(--dxp-g-brand-1)",

       "_NeutralColor" : "#ecebea",

       "_NeutralColor1" : "#d9d7d5",

       "_NeutralColor2" : "#b2aeaa",

       "_NeutralColor3" : "#76716b",

       "_NeutralForegroundColor" : "#000000",

       "_NeutralForegroundColor1" : "#000000",

       "_NeutralForegroundColor2" : "#000000",

       "_NeutralForegroundColor3" : "#ffffff",

       "_OfflineColor" : "#444444",

       "_OfflineColor1" : "#303030",

       "_OfflineColor2" : "#070707",

       "_OfflineColor3" : "#000000",

       "_OfflineForegroundColor" : "#ffffff",

       "_OfflineForegroundColor1" : "#ffffff",

       "_OfflineForegroundColor2" : "#ffffff",

       "_OfflineForegroundColor3" : "#ffffff",

       "_PrimaryAccentColor1" : "#004989",

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
       "_PrimaryAccentColor2" : "#001e38",

       "_PrimaryAccentColor3" : "#000000",

       "_PrimaryAccentForegroundColor1" : "#ffffff",

       "_PrimaryAccentForegroundColor2" : "#ffffff",

       "_PrimaryAccentForegroundColor3" : "#ffffff",

       "_SiteLogoUrl" : "",

       "_SuccessColor" : "#4bca81",

       "_SuccessColor1" : "#36b66c",

       "_SuccessColor2" : "#237747",

       "_SuccessColor3" : "#07190f",

       "_SuccessForegroundColor" : "#000000",

       "_SuccessForegroundColor1" : "#000000",

       "_SuccessForegroundColor2" : "#ffffff",

       "_SuccessForegroundColor3" : "#ffffff",

       "_TextColor1" : "#000000",

       "_TextColor2" : "#000000",

       "_TextColor3" : "#000000",

       "_WarningColor" : "#ffb75d",

       "_WarningColor1" : "#ffa534",

       "_WarningColor2" : "#e27d00",

       "_WarningColor3" : "#673900",

       "_WarningForegroundColor" : "#000000",

       "_WarningForegroundColor1" : "#000000",

       "_WarningForegroundColor2" : "#000000",

       "_WarningForegroundColor3" : "#ffffff"

      }

     }

   }

```

sfdc_cms__languageSettings Folder

This content type folder contains one content subfolder called languages. The languages content subfolder contains two or more `JSON`
files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
   {

     "type" : "sfdc_cms__languageSettings",

     "title" : "LanguageContent",

     "contentBody" : {

      "languages" : [ {

       "locale" : "en_US",

       "label" : "English (US)",

       "isActive" : true,

       "isAuthoringOnly" : false

      } ],

      "defaultLocale" : "en_US"

     }

   }

```

sfdc_cms__route Folder

This content type folder contains one content subfolder for each of the site’s routes. Each route content subfolder contains two or more
`JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
   {

     "type" : "sfdc_cms__route",

     "title" : "Error",

     "contentBody" : {

      "activeViewId" : "error",

      "configurationTags" : [ ],

      "pageAccess" : "UseParent",

      "routeType" : "error",

      "urlPrefix" : "error"

     }

   }

```

sfdc_cms__site Folder

This content type folder exists at the root level and contains one content subfolder. The content subfolder contains two or more `JSON`
files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
{

  "type" : "sfdc_cms__site",

  "title" : "Capricorn_Coffee",

  "contentBody" : {

   "authenticationType" : "AUTHENTICATED"

  }

}

```

sfdc_cms__theme Folder

This content type folder contains one content subfolder, representing the site’s theme. The content subfolder contains two or more
`JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
<apiName> /content.json

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
   {

     "type" : "sfdc_cms__theme",

     "title" : "Build Your Own (LWR)",

     "contentBody" : {

      "activeBrandingSetId" : "Build_Your_Own_LWR",

      "definitionName" : "byo",

      "layouts" : [ {

       "layoutId" : "snaThemeLayout",

       "layoutType" : "ServiceNotAvailable"

      }, {

       "layoutId" : "scopedHeaderAndFooter",

       "layoutType" : "Inner"

      } ]

     }

   }

```

sfdc_cms__themeLayout Folder

This content type folder contains one content subfolder for each theme layout in the site. Each content subfolder contains two or more
`JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

Note: We recommend that you don’t add, reorder, or delete a component within a locked region using the DigitalExperienceBundle.
To find out which regions are locked, in Experience Builder, view the Page Structure tab for the page that you’re working on. If the
region that you’re modifying has a lock icon next to it, it’s a locked region.

```
   <apiName> /content.json

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
{

 "type" : "sfdc_cms__themeLayout",

 "title" : "Service Not Available Theme Layout",

 "contentBody" : {

  "component" : {

    "id" : "50458146-12d8-4dd7-a37b-62f71615c1a0",

    "type" : "component",

    "children" : [ {

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
        "title": "Theme Header",

         "id": "8fc2497b-fae7-4570-bc69-63a7a229e6fc",

         "type": "region",

         "name": "header",

         "children": [

           {

            "id": "05224a3a-8044-9h2h-9187-b3f43155344d",

            "type": "component",

            "definition": "community_builder:htmlEditor",

            "attributes": {

             "richTextValue": "<div style=\"display: flex; justify-content: center;

   align-items: center; margin: 50px 0; flex-direction: column; text-align: center;\"><div

   style=\"background-image: url(assets/img/desert.svg); background-size: cover;

   background-position: center; height: 300px; width: 100%; max-width: 600px; min-width:

   300px;\"></div><h1 class=\"slds-text-heading_medium slds-p-bottom_x-small\">Start Building

    Your Page</h1> <div>Drag and drop a component into the content slots.</div></div>"

            },

            "variations": [

             {

              "id": "5d700461-4c2a-4930-98e5-366ec2a4d41e",

              "title": "Variation Country USA",

              "type": "mutationComponent",

              "definition": "community_builder:htmlEditor",

              "attributes": {

               "richTextValue": "<div style=\"display: flex; justify-content: center;

    align-items: center; margin: 50px 0; flex-direction: column; text-align: center;\"><div

   style=\"background-image: url(assets/img/desert.svg); background-size: cover;

   background-position: center; height: 300px; width: 100%; max-width: 600px; min-width:

   300px;\"></div><h1 class=\"slds-text-heading_medium slds-p-bottom_x-small\">Start Building

    Your Page</h1> <div>Drag and drop a component into the content slots.</div></div>"

              }

             }

            ]

           }

         ]

        },

        {

        "title" : "Theme Footer",

        "id" : "05224a3a-8044-9h2h-9187-b3f43155344d",

        "type" : "region",

        "name" : "footer"

       } ],

       "definition" : "community_layout:simpleThemeLayout",

       "attributes": {}

      }, "contentOperations": {

       "operations": [

        {

         "targetId": "05224a3a-8044-9h2h-9187-b3f43155344d",

         "isHiddenOnOperationSuccess": false,

         "isActive": true,

         "rule": {

           "name": "708b6ff0-d50c-4cea-a492-kkjk4b174e86",

           "description": "",

           "criteriaType": "AllCriteriaMatch",

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
           "expressionCriteria": [

            {

             "resource": "User.Record.FirstName",

             "operator": "Equal",

             "value": "Clark"

            }

           ]

         }

        },

        {

         "targetId": "05224a3a-8044-9h2h-9187-b3f43155344d",

         "ruleToVariationList": [

           {

            "variationId": "5d700461-4c2a-4930-98e5-366ec2a4d41e",

            "rule": {

             "name": "6e1ea488-13d8-477a-a9d7-93f442cc7936",

             "description": "",

             "criteriaType": "CustomLogicMatches",

             "customFormula": "(1 && 3) || 2",

             "expressionCriteria": [

              {

               "resource": "User.Record.Country",

               "operator": "Equal",

               "value": "USA",

               "criterionNumber": 1

              },

              {

               "resource": "User.Record.City",

               "operator": "Equal",

               "value": "Chicago",

               "criterionNumber": 2

              },

              {

               "resource": "User.Record.PostalCode",

               "operator": "Equal",

               "value": "60131",

               "criterionNumber": 3

              }

             ]

            }

           }

         ]

        }

       ]

      }

     }

   }

```

sfdc_cms__view Folder

This content type folder contains one content subfolder per view. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

**•** If applicable, additional `JSON` files that represent variations of the content item

Each Experience Builder site is built from single-page applications, which are web apps that load a single HTML page. Single-page
applications consist of multiple views that update the page dynamically as the user interacts with it. A view is made up of regions that
contain other regions or components in the rendered page for the user. Single-page applications in your site are defined in the
`sfdc_cms__appPage` folder.

Each `content.json` file in the sfdc_cms__view folder contains a hidden region named `sfdcHiddenRegion` . The hidden
region contains a component with a definition of `community_builder:seoAssistant` that represents the SEO assistant
component. This component corresponds to the SEO page properties that you can configure in Experience Builder and isn't visible on
your pages. To improve search engine results, use the SEO assistant component to set the `customHeadTags`, `description`, and
`pageTitle` properties for your public and custom site pages. You can’t edit the other properties associated with the SEO assistant
component. To learn more about what the title, description, and custom head tags properties represent and which head tags are allowed,
[see SEO Page Properties in Experience Builder.](https://help.salesforce.com/s/articleView?id=experience.networks_seo_tags.htm&type=5&language=en_US)

Note: We recommend that you don’t add, reorder, or delete a component within a locked region using the DigitalExperienceBundle.
To find out which regions are locked, in Experience Builder, view the Page Structure tab for the page that you’re working on. If the
region that you’re modifying has a lock icon next to it, it’s a locked region.

Note: If there are specific style overrides for mobile or tablet views in the target org, make sure that these overrides are also
present in the source org. If the target org contains mobile or tablet `JSON` files within the mobile or tablet folders that aren’t
present in the source org, deploying the DigitalExperienceBundle fails.

```
   <apiName> /content.json

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
{

 "type" : "sfdc_cms__view",

 "title" : "Home",

 "contentBody" : {

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
      "themeLayoutType" : "Inner",

      "viewType" : "home",

      "component" : {

       "id" : "40c14c97-1846-4872-8e9e-cdf3d11beb34",

       "type" : "component",

       "children" : [ {

        "title" : "Content",

        "id" : "c507f23d-6e2a-457a-9656-2377846dd639",

        "type" : "region",

        "children" : [ {

         "id" : "21f99012-3a2f-488e-bf48-f782dc7b4300",

         "type" : "component",

         "children" : [ {

           "title" : "Column 1",

           "id": "05224a3a-8044-4bfb-9187-b3f43155344d",

           "type" : "region",

           "children" : [ {

            "id" : "05224a3a-8044-4bfb-9187-b3f43155344d",

            "type" : "component",

            "definition" : "community_builder:htmlEditor",

            "attributes" : {

             "dxpStyle" : {

              "isVisible" : false,

              "margin" : {

               "bottom" : "20px",

               "left" : "20px",

               "right" : "20px",

               "top" : "20px"

              },

              "padding" : {

               "bottom" : "20px",

               "left" : "20px",

               "right" : "20px",

               "top" : "20px"

              }

             },

             "richTextValue" : "<div style=\"display: flex; justify-content: center;

   align-items: center; margin: 50px 0; flex-direction: column; text-align: center;\"><div

   style=\"background-image: url(assets/img/desert.svg); background-size: cover;

   background-position: center; height: 300px; width: 100%; max-width: 600px; min-width:

   300px;\"></div><h1 class=\"slds-text-heading_medium slds-p-bottom_x-small\">Start Building

    Your Page</h1> <div>Drag and drop a component into the content slots.</div></div>"

            },

            "variations": [

                  {

                   "id": "5d700461-4c2a-4930-98e5-366ec2a4d41e",

                   "title": "Variation Country USA",

                   "type": "mutationComponent",

                   "definition": "community_builder:htmlEditor",

                   "attributes": {

                    "richTextValue": "<div style=\"display: flex; justify-content:

    center; align-items: center; margin: 50px 0; flex-direction: column; text-align:

   center;\"><div style=\"background-image: url(assets/img/desert.svg); background-size:

   cover; background-position: center; height: 300px; width: 100%; max-width: 600px; min-width:

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
    300px;\"></div><h1 class=\"slds-text-heading_medium slds-p-bottom_x-small\">Start Building

    Your Page</h1> <div>Drag and drop a component into the content slots.</div></div>"

                   }

                  }

                 ]

            "customCssClasses": "myClass"

           } ],

           "name" : "col1"

         } ],

         "definition" : "community_layout:section",

         "attributes" : {

           "backgroundImageConfig" : "",

           "backgroundImageOverlay" : "rgba(0,0,0,0)",

           "sectionConfig" :

   "{\"UUID\":\"21f99012-3a2f-488e-bf48-f782dc7b4300\",\"columns\":[{\"UUID\":\"5019aeeb-6437-4194-8369-22c19aa45dc9\",\"columnName\":\"Column

    1\",\"columnKey\":\"col1\",\"columnWidth\":\"12\",\"seedComponents\":null}]}"

         }

        } ],

        "name" : "content"

       }, {

        "title" : "sfdcHiddenRegion",

        "id" : "8157e041-9c41-460a-b596-c45babbbd53b",

        "type" : "region",

        "children" : [ {

         "id" : "2d536aae-a859-4264-ba9e-9a569daf7213",

         "type" : "component",

         "definition" : "community_builder:seoAssistant",

         "attributes" : {

           "customHeadTags" : "",

           "description" : "",

           "pageTitle" : "Home",

           "recordId" : "{!recordId}"

         }

        } ],

        "name" : "sfdcHiddenRegion"

       } ],

       "definition": "community_layout:sldsFlexibleLayout"

      },

      "contentOperations": {

       "operations": [

        {

         "targetId": "05224a3a-8044-4bfb-9187-b3f43155344d",

         "isHiddenOnOperationSuccess": false,

         "isActive": true,

         "rule": {

           "name": "a53bb452-003f-4015-a751-0403c70731a1",

           "description": "",

           "criteriaType": "AllCriteriaMatch",

           "expressionCriteria": [

            {

             "resource": "User.isGuest",

             "operator": "Equal",

             "value": false

            }

```


### Metadata Types DigitalExperienceConfig

```
           ]

         }

        },

        {

         "targetId": "05224a3a-8044-9h2h-9187-b3f43155344d",

         "ruleToVariationList": [

           {

            "variationId": "5d700461-4c2a-4930-98e5-366ec2a4d41e",

            "rule": {

             "name": "6e1ea488-13d8-477a-a9d7-93f442cc7936",

             "description": "",

             "criteriaType": "CustomLogicMatches",

             "customFormula": "(1 && 3) || 2",

             "expressionCriteria": [

              {

               "resource": "User.Record.Country",

               "operator": "Equal",

               "value": "USA",

               "criterionNumber": 1

              },

              {

               "resource": "User.Record.City",

               "operator": "Equal",

               "value": "Chicago",

               "criterionNumber": 2

              },

              {

               "resource": "User.Record.PostalCode",

               "operator": "Equal",

               "value": "60131",

               "criterionNumber": 3

              }

             ]

            }

           }

         ]

        }

       ]

      }

     }

   }

### DigitalExperienceConfig

```

Represents details for your organization’s workspaces, such as the site label, site URL path prefix, and workspace type.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types DigitalExperienceConfig

File Suffix and Directory Location

DigitalExperienceConfig components have the suffix `.digitalExperienceConfig` and are stored in the
`digitalExperienceConfigs` folder.

Version

DigitalExperienceConfig components are available in API version 56.0 and later.

Special Access Rules

You can use DigitalExperienceConfig for enhanced LWR sites created after the Winter ’23 release.

Fields

**Field Name** **Description**

```
label

site

space

```

Site

**Field Type**
string

**Description**
Required.

The name of the site.

**Field Type**

Site

**Description**
Required.

Contains site-related settings, such as the site’s URL path prefix.

**Field Type**
string

**Description**
Required.

References the workspace that contains the site’s content items such as brandingSets,
themes, views, and routes.

Represents site-related information, such as the URL path prefix.

**Field Name** **Description**

```
urlPathPrefix

```

**Field Type**
string


### Metadata Types DisclosureDefinition

**Field Name** **Description**

**Description**
The first part of the path on the site's URL that distinguishes this site from other sites.
For example, if your site URL is _`MyDomainName`_ .my.site.com/partners, then partners
is the `urlPathPrefix` .

Declarative Metadata Sample Definition

The following is an example of a DigitalExperienceConfig component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DigitalExperienceConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>Capricorn_Coffee</label>

      <site>

        <urlPathPrefix>CapricornCoffee</urlPathPrefix>

      </site>

      <space>site/Capricorn_Coffee1</space>

   </DigitalExperienceConfig>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Capricorn_Coffee1</members>

        <name>DigitalExperienceConfig</name>

      </types>

      <version>56.0</version>

   </Package>

```

Usage

To retrieve and deploy DigitalExperienceConfig, use legacy sfdx commands.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DisclosureDefinition

Represents information that defines a disclosure type, such as details of the publisher or vendor who created or implemented the report.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.


Metadata Types DisclosureDefinition

File Suffix and Directory Location

DisclosureDefinition components have the suffix `.disclosureDefinition` and are stored in the `disclosureDefinitions`
folder.

Version

DisclosureDefinition components are available in API version 57.0 and later.

Special Access Rules

The DisclosureAndComplianceHubAddOn license is required to access this object along with user access for the Disclosure Compliance
Hub permission set license.

Fields

**Field Name** **Description**

```
description

disclosureType

isProtected

masterLabel

```

**Field Type**
string

**Description**
The description about the disclosure definition.

**Field Type**
string

**Description**

Required.

The API name of the disclosure type associated with this definition.

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default is `false` .

**Field Type**
string

**Description**

Required.

A user-friendly name for DisclosureDefinition, which is defined when the
DisclosureDefinition is created.


### Metadata Types DisclosureDefinitionVersion

Declarative Metadata Sample Definition

The following is an example of a DisclosureDefinition component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DisclosureDefinition

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <description>This is GRI Disclosure Definition</description>

    <disclosureType>disclstype10</disclosureType>

    <isProtected>false</isProtected>

    <masterLabel>GRI</masterLabel>

   </DisclosureDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <fullName>Pkg</fullName>

    <types>

     <members>GRI</members>

     <name>DisclosureDefinition</name>

    </types>

    <types>

     <members>dt12</members>

     <name>DisclosureType</name>

    </types>

    <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### DisclosureDefinitionVersion

Represents the version information about the disclosure definition.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### DisclosureDefinitionVersion components have the suffix .disclosureDefinitionVersion and are stored in the

`disclosureDefinitionVersions` folder.


Metadata Types DisclosureDefinitionVersion

Version

DisclosureDefinitionVersion components are available in API version 57.0 and later.

Special Access Rules

The DisclosureAndComplianceHubAddOn and OmniStudioDesignerAddon licenses are required to access this object along with user
access for the Disclosure Compliance Hub and OmniStudio Admin permission set licenses.

Fields

**Field Name** **Description**

```
authoringMode

description

disclosureDefCurrVer

disclosureDefinition

documentTemplateGlobalKey

```

**Field Type**
AuthoringMode (enumeration of type string)

**Description**
Specifies the authoring mode used to launch the disclosure authoring experience.

Possible values are:

**•** `Microsoft 365 Word`

**•** `Omniscript and Microsoft 365 Word`

**•** `Omniscript Form`

**Field Type**
string

**Description**
The description about the disclosure definition version.

**Field Type**
string

**Description**
For internal use only.

**Field Type**
string

**Description**

Required.

The API name of the disclosure definition associated with this version.

**Field Type**
string

**Description**
The document template global key associated with the DOCX template for the
disclosure definition version.


Metadata Types DisclosureDefinitionVersion

**Field Name** **Description**

```
isActive

isCurrentVersion

isProtected

masterLabel

omniScriptCnfgApiName

omniScriptConfiguration

```

**Field Type**
boolean

**Description**
Indicates whether the disclosure definition version is an active version ( `true` ) or not
( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether this is the current version of the disclosure definition specified in
the `disclosureDefinition` field ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default is `false` .

**Field Type**
string

**Description**

Required.

A user-friendly name for DisclosureDefinitionVersion, which is defined when the
DisclosureDefinitionVersion is created.

**Field Type**
string

**Description**
The API name of the Omniscript configuration that's associated with the disclosure
definition version. This field is required only when `authoringMode` isn’t
`Microsoft 365 Word` .

**Field Type**
string

**Description**
The ID of the Omniscript configuration record.

Note: The value of this field is automatically populated using the API name of
the OmniScript configuration specified in the `omniScriptCnfgApiName`
field.


Metadata Types DisclosureDefinitionVersion

**Field Name** **Description**

```
versionNumber

```

**Field Type**
string

**Description**

Required.

The version of the disclosure definition published by the author.

Declarative Metadata Sample Definition

The following is an example of a DisclosureDefinitionVersion component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DisclosureDefinitionVersion xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>This is GRI Disclosure Definition Version</description>

   <versionNumber>disclosure definition version number</versionNumber>

   <isActive>false</isActive>

   <disclosureDefinition>df10</disclosureDefinition>

   <omniScriptConfiguration>omni script configuration</omniScriptConfiguration>

   <omniScriptCnfgApiName>omni script config api name</omniScriptCnfgApiName>

   <isCurrentVersion>true</isCurrentVersion>

   <disclosureDefCurrVer>df10.Id</disclosureDefCurrVer>

   <documentTemplateGlobalKey>document template global key</documentTemplateGlobalKey>

   <authoringMode>OmniScriptForm</authoringMode>

   <masterLabel>GRI</masterLabel>

   <isProtected>false</isProtected>

</DisclosureDefinitionVersion>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <fullName>Pkg</fullName>

 <types>

  <members>GRI</members>

  <name>DisclosureDefinitionVersion</name>

 </types>

 <types>

  <members>df10</members>

  <name>DisclosureDefinition</name>

 </types>

 <types>

  <members>dt10</members>

  <name>DisclosureType</name>

 </types>

 <version>60.0</version>

</Package>

```


### Metadata Types DisclosureType

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### DisclosureType

Represents the types of disclosures that are done by an individual or an organization and the associated metadata.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### DisclosureType components have the suffix .disclosureType and are stored in the disclosureTypes folder.

Version

### DisclosureType components are available in API version 57.0 and later.

Special Access Rules

The DisclosureAndComplianceHubAddOn license is required to access this object along with user access for the Disclosure Compliance
Hub permission set license.

Fields

**Field Name** **Description**

```
description

disclosureBodyLogo

disclosureBodyUrl

```

**Field Type**
string

**Description**
The description about the disclosure type.

**Field Type**
string

**Description**
The logo ID of the standard body to which an individual or a company is making a
disclosure.

**Field Type**
string


Metadata Types DisclosureType

**Field Name** **Description**

**Description**
The URL of the disclosure standard body.

```
disclosureCategory

isProtected

masterLabel

```

**Field Type**
string

**Description**

Required.

The name of the clause category that's used for disclosure.

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default is `false` .

**Field Type**
string

**Description**

Required.

A user-friendly name for DisclosureType, which is defined when the DisclosureType
is created.

Declarative Metadata Sample Definition

The following is an example of a DisclosureType component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DisclosureType

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <description>This is ESG Disclosure Type</description>

 <disclosureBodyLogo>asdf</disclosureBodyLogo>

 <disclosureCategory>EnvSocGvnc</disclosureCategory>

 <disclosureBodyUrl>disclosure body url</disclosureBodyUrl>

 <isProtected>false</isProtected>

 <masterLabel>ESG</masterLabel>

</DisclosureType>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <fullName>Pkg</fullName>

```


### Metadata Types DiscoveryAIModel

```
    <types>

     <members>ESG</members>

     <name>DisclosureType</name>

    </types>

    <types>

     <name>StaticResource</name>

     <members>asdf</members>

    </types>

    <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### DiscoveryAIModel

Represents the metadata associated with a model used in Einstein Discovery.

A model is a sophisticated, custom algorithm that Einstein Discovery generates based on a comprehensive, statistical understanding of
past outcomes. Einstein Discovery uses models to predict future outcomes. A model accepts the values of one or more predictor variables
as input and produces a predicted outcome as output, along with (optionally) top factors and improvements. In Package Manager, this
type is listed as "Discovery Model".

You can also build models using a third-party modeling tool, and then import them into Salesforce using Model Manager in Analytics
Studio.

Note: Write operations for DiscoveryAIModel objects are generally not supported.

Declarative Metadata File Suffix and Directory Location

A DiscoveryAIModel is stored in the `discovery` folder. DiscoveryAIModels have two files:

**•** file with `.model` suffix contains the model's actual data

**•** file named _`ModelName`_ `.model-meta.xml` suffix contains the model's metadata

Here is a sample `package.xml` file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Maximize_Sales</members>

        <name>DiscoveryAIModel</name>

      </types>

      <version>53.0</version>

   </Package>

```

Version

### DiscoveryAIModels are available in API version 51.0 and later.


Metadata Types DiscoveryAIModel

Fields

**Field Name** **Field Type** **Description**

`algorithmType` DiscoveryAlgorithmType Algorithm that Einstein Discovery used to create the model
associated with this story.

`classificationThreshold` double Threshold value. Applies only to binary classification models. For
regression models, this is null.

`description` string Model description.

`label` string Model label. If you package a model, this label appears in Package
Manager.

`modelFields` DiscoveryModelField[] One or more model fields (variables).

`modelRuntimeType` DiscoveryModelRuntimeType Model run-time type.

`predictedField` string Name of the field that is predicted.

`predictionType` DiscoveryPredictionType Type of prediction. One of the following strings:

**•** `Regression`

**•** `Classification`

**•** `Unknown`

`sourceType` DiscoveryModelSourceType Source type.

`status` DiscoveryAIModelStatus Model status (enabled or disabled).

`trainingMetrics` string JSON object that represents metrics about the model when it was
trained.

`transformations` DiscoveryModelTransform One or more model transformations.

DiscoveryAlgorithmType

Represents the algorithm that Einstein Discovery used to create the model.

**Field Name** **Field Type** **Description**

`Best` string

Tournament Model. Genetic algorithm used to generate
high-quality solutions to optimization and search problems, like
optimizing decision trees for better performance.

`Glm` string Generalized Linear Model. Regression-based algorithm.

`Gbm` string Gradient Boost Machine. Decision tree-based ensemble machine
learning algorithm.

`Xgboost` string XGBoost. Decision tree-based ensemble machine learning
algorithm.


Metadata Types DiscoveryAIModel

**Field Name** **Field Type** **Description**

`Drf` string Random Forest. Supervised learning algorithm that uses multiple
decision trees, randomization, and other optimization techniques.

DiscoveryModelField

Represents a field (variable) in the model.

**Field Name** **Field Type** **Description**

`isDisparateImpact` boolean Indicates whether the field is disparate impact ( `true` ) or not
( `false` ).

`isSensitive` boolean Indicates whether the field is sensitive ( `true` ) or not ( `false` ).

`label` string Field label displayed in the UI.

`name` string Field name.

`type` DiscoveryModelFieldType Field type. Enumerated.

`values` string[] A list of field values.

DiscoveryModelTransform

Represents a transformation in the model.

**Field Name** **Field Type** **Description**

`config` string The configuration for the transformation.

`sourceFieldNames` string[] A list of the source field names.

`targetFieldNames` string[] A list of the target field names.

`type` DiscoveryAIModelTransformationType Type of transformation.

DiscoveryAIModelTransformationType

Represents the type of transformation to apply before making a prediction.

**Field Name** **Field Type** **Description**

`TypographicClustering` string Typographic clustering transformation.

`SentimentAnalysis` string Sentiment analysis transformation.

`FreeTextClustering` string Free text clustering transformation.

`NumericalImputation` string Numerical imputation transformation.

`CatagoricalImputation` string Catagorical imputation transformation.


Metadata Types DiscoveryAIModel

**Field Name** **Field Type** **Description**

`TimeSeriesForecast` string Time series forecast transformation.

`ExtractMonthOfYear` string Extract month of year transformation.

`ExtractDayOfWeek` string Extract day of week transformation.

`ZipCodeAnalysis` string Zip code analysis transformation.

DiscoveryModelFieldType

Represents the data type of a model field.

**Field Name** **Field Type** **Description**

`Text` string Text data type.

`Number` string Number data type.

`Date` string Date data type.

DiscoveryModelRuntimeType

Represents the model run-type.

**Field Name** **Field Type** **Description**

`Discovery` string The model run-type is Einstein Discovery.

`H2O` string The model run-type is H20.

`T` string The model run-type is Tensorflow v2.4.4.

`Tf27` string The model run-type is Tensorflow v2.7.0.

`SC102` string The model run-type is Scikit Learn v1.0.2.

DiscoveryModelSourceType

Represents the source tool used to build the model: Discovery or an external tool (the model was uploaded into Salesforce).

**Field Name** **Field Type** **Description**

`Discovery` string Einstein Discovery built the model.

`UserUpload` string An external tool built the model. The model was then uploaded
into Salesforce.

Note: This source type is not supported in the Metadata
API.


Metadata Types DiscoveryAIModel

DiscoveryAIModelStatus

Represents the status of the model (Enabled or Disabled).

**Field Name** **Field Type** **Description**

`Disabled` string The model is disabled (inactive).

`Uploading` string The model is uploading.

`UploadFailed` string The model failed to upload.

`UploadCompleted` string The model upload is complete.

`Validating` string The model is validating.

`ValidationFailed` string The model validation failed.

`ValidationCompleted` string The model validation is complete.

`Enabled` string The model is enabled (active).

Declarative Metadata Sample Definitions

Here is a sample DiscoveryAIModel:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DiscoveryAIModel xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

     <content xsi:nil="true"/>

     <algorithmType>Glm</algorithmType>

     <classificationThreshold>0.7383</classificationThreshold>

     <label>Maximize Tenure</label>

     <modelFields>

       <label>Field</label>

       <name>Field</name>

       <type>Text</type>

     </modelFields>

     <modelFields>

       <label>PTO</label>

       <name>PTO</name>

       <type>Number</type>

     </modelFields>

     <modelFields>

       <label>Level</label>

       <name>Level</name>

       <type>Text</type>

     </modelFields>

     <modelFields>

       <label>Salary</label>

       <name>Salary</name>

       <type>Number</type>

     </modelFields>

     <modelFields>

       <label>Tenure</label>

```


### Metadata Types DiscoveryGoal

```
       <name>Tenure</name>

       <type>Number</type>

     </modelFields>

     <modelRuntimeType>Discovery</modelRuntimeType>

     <predictedField>Tenure</predictedField>

     <predictionType>Classification</predictionType>

     <sourceType>Discovery</sourceType>

     <status>Enabled</status>

   </DiscoveryAIModel>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DiscoveryGoal

Represents the metadata associated with an Einstein Discovery prediction definition.

A prediction definition is a container object in Einstein Discovery that is associated with one or more deployed models. If a prediction
definition contains multiple models, then each model produces predictions for a different segment of the data. A prediction definition
can contain up to ten active models. In Package Manager, this type is listed as "Discovery Prediction".

Declarative Metadata File Suffix and Directory Location

A DiscoveryGoal is stored in the `discovery` folder. DiscoveryGoals have a `.goal` file suffix. Here is a sample `package.xml` file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>employees_Tenure</members>

        <name>DiscoveryGoal</name>

      </types>

      <version>53.0</version>

   </Package>

```

Version

### DiscoveryGoals are available in API version 51.0 and later.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the prediction definition is active (True) or not
(False).

`deployedModels` DiscoveryDeployedModel[] One or more deployed models associated with this prediction
definition.


Metadata Types DiscoveryGoal

**Field Name** **Field Type** **Description**

`label` string Name of the prediction definition.

`modelCards` DiscoveryModelCard[] Model card for this prediction definition.

`outcome` DiscoveryGoalOutcome Outcome variable of this prediction definition.

`predictionType` DiscoveryPredictionType Type of prediction: `Regression`, `Classification`, or
`Unknown` .

`pushbackField` string Automated writeback field for predictions. A custom field on the
Salesforce object specified in `subscribedEntity` .

Note: Removing a pushback field from the goal metadata
causes the field to be deleted from the Salesforce object as
well.

`pushbackType` DiscoveryPushbackType Type of writeback field for predictions.

`subscribedEntity` string Salesforce object associated with this model.

`terminalStateFilters` DiscoveryFilter[] If specified, one or more filter expressions that define the conditions
under which an observation has attained its terminal state (the

actual outcome has been reached). For performance monitoring,
Einstein Discovery determines model accuracy by comparing a
model’s predicted outcomes with actual (observed) outcomes.

DiscoveryDeployedModel

Represents a model deployed in Salesforce.

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the deployed model is active (True) or inactive
(False).

`aiModel` string Full name of the DiscoveryAIModel being deployed.

`classificationThreshold` double

Threshold value. Applies only to binary classification models. For
regression models, this is null.

`fieldMappings` DiscoveryFieldMap[] One or more mappings between model variables and either fields
(in Salesforce objects) or columns (in CRM Analytics datasets).

`filters` DiscoveryFilter[] If specified, one or more segmentation filters for the deployed
model. When making a prediction, the first model that has filters

matching a specific input row will be used to make the prediction.
No filters indicates that the model matches all input rows.

`label` string Label for the deployed model. Appears in Model Manager.

`name` string Name of the deployed model.


Metadata Types DiscoveryGoal

**Field Name** **Field Type** **Description**

`prescribableFields` DiscoveryPrescribableField[] Actionable fields associated with improvements.

DiscoveryFieldMap

Represents a mapping between model variables and field values.

**Field Name** **Field Type** **Description**

`mappedField` string Field in a Salesforce object or column in a CRM Analytics dataset.

`modelField` string Model variable.

`sobjectFieldJoinKey` string Join key for a Salesforce object. Null if `sourceType` is
`AnalyticsDatasetField` .

`source` string If the mapping is to a CRM Analytics dataset, this is the name of
the dataset. Otherwise, null.

`sourceFieldJoinKey` string If the mapping is to a CRM Analytics dataset, this is the lookup
column on that dataset used to perform the join. Otherwise, null.

`sourceType` DiscoveryFieldMapSourceType Data source type for field mapping.

DiscoveryFieldMapSourceType

Represents the data source type for field mapping: `SalesforceField` or `AnalyticsDatasetField` .

**Field Name** **Field Type** **Description**

`SalesforceField` string Field in a Salesforce object.

`AnalyticsDatasetField` string Column in a CRM Analytics dataset.

DiscoveryFilter

Represents a field filter.

**Field Name** **Field Type** **Description**

`field` string Name of the field to filter.

`operator` DiscoveryFilterOperator Operator used to calculate the filter.

`type` DiscoveryFilterFieldType Type of filter value.

`values` DiscoveryFilterValue[] One or more values selected for the filter.


Metadata Types DiscoveryGoal

DiscoveryFilterOperator

Represents a filter operator.

**Field Name** **Field Type** **Description**

`Equal` string Equal to operator (=).

`NotEqual` string Not equal to operator (<>).

`GreaterThan` string Greater than operator (>).

`GreaterThanOrEqual` string Greater than or equal to operator (>=).

`LessThan` string Less than operator (<).

`LessThanOrEqual` string Less than or equal to operator (<=).

`Between` string Between operator.

`NotBetween` string Not between operator.

`InSet` string In set operator.

`NotIn` string Not in operator.

`Contains` string Contains operator.

`StartsWith` string Starts with operator.

`EndsWith` string Ends with operator.

`IsNull` string Is null operator.

`IsNotNull` string Is not null operator.

DiscoveryFilterFieldType

Represents the data type of the filter field.

**Field Name** **Field Type** **Description**

`Text` string Text field type.

`Number` string Number field type.

`Date` string Date field type.

`DateTime` string Datetime field type.

`Boolean` string Boolean field type.

DiscoveryFilterValue

Represents a filter value.


Metadata Types DiscoveryGoal

**Field Name** **Field Type** **Description**

`type` DiscoveryFilterValueType Type of filter value.

`value` DiscoveryFilterValue Value.

DiscoveryFilterValueType

Represents the type of filter value.

**Field Name** **Field Type** **Description**

`Constant` string Filter value is a constant.

`PlaceHolder` string Filter value is a placeholder.

DiscoveryPrescribableField

Represents custom improvement text.

**Field Name** **Field Type** **Description**

`customDefinitions` DiscoveryCustomPrescribableFieldDefinition[] One or more strings for custom improvement text. Uses the default
improvement text if none are specified.

`name` string Name of the model field that is actionable.

DiscoveryCustomPrescribableFieldDefinition

Represents a field definition in custom improvement text.

**Field Name** **Field Type** **Description**

`filters` DiscoveryFilter[] Represents one or more filters associated with custom
improvement text.

`template` string

DiscoveryModelCard

If specified, represents the user-provided template from which the
custom text is computed. If not specified, then the default text is
used.

Represents a model card associated with an Einstein Discovery prediction definition.

**Field Name** **Field Type** **Description**

`contactEmail` string Contact email for this model card.

`contactName` string Contact name for this model card.


Metadata Types DiscoveryGoal

**Field Name** **Field Type** **Description**

`label` string Title for this model card.

`sections` string Sections in the model card.

DiscoveryGoalOutcome

Represents the outcome variable of the model.

**Field Name** **Field Type** **Description**

`field` string Name of the outcome variable.

`fieldLabel` string Label for the outcome variable.

`goal` DiscoveryOutcomeGoal Goal for the outcome variable.

`mappedField` string Mapped field.

DiscoveryOutcomeGoal

Represents the goal for an outcome.

**Field Name** **Field Type** **Description**

`Minimize` string Maximize the outcome.

`Maximize` string Minimize the outcome.

`None` string Reserved for future use.

DiscoveryPredictionType

Represents the prediction type for a model.

**Field Name** **Field Type** **Description**

`Unknown` string Unknown prediction type.

`Regression` string Regression prediction (numeric use case).

`Classification` string Binary classification prediction.

`MulticlassClassification` string Multiclass classification prediction.

DiscoveryPushbackType

Represents the type of writeback field. Must be set to `AiRecordInsight` .


Metadata Types DiscoveryGoal

**Field Name** **Field Type** **Description**

`AiRecordInsight` string Automatic writeback type. Required.

`Direct` string Currently not supported. Reserved for future use.

Declarative Metadata Sample Definitions

Here is a sample DiscoveryGoal:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DiscoveryGoal xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

     <active>true</active>

     <deployedModels>

       <active>true</active>

       <aiModel>Maximize_Tenure</aiModel>

       <fieldMappings>

         <mappedField>Opportunity.Amount</mappedField>

         <modelField>PTO</modelField>

         <sourceType>SalesforceField</sourceType>

       </fieldMappings>

       <fieldMappings>

         <mappedField>Opportunity.ExpectedRevenue</mappedField>

         <modelField>Salary</modelField>

         <sourceType>SalesforceField</sourceType>

       </fieldMappings>

       <fieldMappings>

         <mappedField>Level</mappedField>

         <modelField>Level</modelField>

         <sobjectFieldJoinKey>Opportunity.Name</sobjectFieldJoinKey>

         <source>employees</source>

         <sourceFieldJoinKey>Name</sourceFieldJoinKey>

         <sourceType>AnalyticsDatasetField</sourceType>

       </fieldMappings>

       <fieldMappings>

         <mappedField>Opportunity.StageName</mappedField>

         <modelField>Field</modelField>

         <sourceType>SalesforceField</sourceType>

       </fieldMappings>

       <filters>

         <field>Opportunity.StageName</field>

         <operator>Equal</operator>

         <values>

           <type>Constant</type>

           <value>Qualification</value>

         </values>

       </filters>

       <label>employees</label>

       <name>employees</name>

       <prescribableFields>

         <customDefinitions>

```


Metadata Types DiscoveryGoal

```
          <filters>

            <field>Salary</field>

            <operator>LessThan</operator>

            <type>Number</type>

            <values>

              <type>PlaceHolder</type>

              <value>[value_low]</value>

            </values>

          </filters>

          <template>Increase [field_name] by [diff]</template>

         </customDefinitions>

         <customDefinitions>

           <filters>

            <field>Salary</field>

            <operator>GreaterThan</operator>

            <type>Number</type>

            <values>

               <type>PlaceHolder</type>

               <value>[value_low]</value>

             </values>

           </filters>

           <template xsi:nil="true"/>

         </customDefinitions>

         <name>Salary</name>

       </prescribableFields>

       <prescribableFields>

         <customDefinitions>

           <filters>

             <field>Level</field>

             <operator>LessThan</operator>

             <type>Number</type>

             <values>

               <type>PlaceHolder</type>

               <value>[value_low]</value>

             </values>

           </filters>

           <template xsi:nil="true"/>

         </customDefinitions>

         <customDefinitions>

           <filters>

             <field>Level</field>

             <operator>GreaterThan</operator>

             <type>Number</type>

             <values>

               <type>PlaceHolder</type>

               <value>[value_low]</value>

              </values>

            </filters>

            <template xsi:nil="true"/>

         </customDefinitions>

         <name>Level</name>

       </prescribableFields>

       <prescribableFields>

         <name>Field</name>

```


### Metadata Types DiscoveryStory

```
       </prescribableFields>

     </deployedModels>

     <label>employees_Tenure</label>

     <outcome>

       <field>Tenure</field>

       <fieldLabel>Tenure</fieldLabel>

       <goal>Maximize</goal>

       <mappedField>Opportunity.Amount</mappedField>

     </outcome>

     <predictionType>Regression</predictionType>

     <pushbackField>My_Pushback_Field__c</pushbackField>

     <subscribedEntity>Opportunity</subscribedEntity>

     <terminalStateFilters>

       <field>Opportunity.Amount</field>

       <operator>GreaterThan</operator>

       <values>

         <type>Constant</type>

         <value>5</value>

       </values>

     </terminalStateFilters>

     <terminalStateFilters>

       <field>Opportunity.Amount</field>

       <operator>LessThan</operator>

       <values>

         <type>Constant</type>

         <value>10</value>

       </values>

     </terminalStateFilters>

   </DiscoveryGoal>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DiscoveryStory

Represents the metadata associated with a story used in Einstein Discovery.

A story defines the data and analytical settings that Einstein Discovery uses to generate insights and build predictive models. Story
settings include the outcome variable, whether to maximize or minimize the outcome variable, the data to analyze in a CRM Analytics
dataset, and other preferences. Story settings tell Einstein Discovery how to conduct the analysis and communicate its results. In Package
Manager, this type is listed as "Discovery Story".

Note: Write operations for DiscoveryStory objects are generally not supported.

Declarative Metadata File Suffix and Directory Location

A DiscoveryStory is stored in the `discovery` folder. DiscoveryStory have two files:

**•** file with `.story` suffix contains the story’s actual data


Metadata Types DiscoveryStory

**•** file named _`ModelName`_ `.story-meta.xml` suffix contains the story’s metadata

Here is a sample `package.xml` file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Subscriber_Changes</members>

        <name>DiscoveryStory</name>

      </types>

      <version>55.0</version>

   </Package>

```

Version

DiscoveryStorys are available in API version 54.0 and later.

Fields

**Field Name** **Field Type** **Description**

`application` string Required. The CRM Analytics app the story is associated with.

`autopilot` DiscoveryStoryAutopilotStatus Optional. The autopilot status for the story. One of the following
strings:

**•** `Enabled`

**•** `Disabled`

`classificationThreshold` double Optional. The threshold for classification predictions for the story.

`label` string Required. The story label. If you package a story, this label appears
in Package Manager.

`outcome` DiscoveryStoryOutcome Required. The selected outcome of the story.

`sourceContainer` string Required. The source ID for the story.

`sourceType` DiscoveryStorySourceType Required. The source type of the story. One of the following strings:

**•** `AnalyticsDataset`

**•** `LiveDataset`

**•** `Report`

`validationContainder` string Optional. The validation ID for the story.

DiscoveryStoryOutcome

Represents the selected outcome of the generated story.


Metadata Types DiscoveryStory

**Field Name** **Field Type** **Description**

`failureValue` string Optional. The value if the story failed.

`field` string Required. The field configuration for the story.

`goal` DiscoveryStoryOutcomeGoal Required. The story outcome goal. One of the following strings:

**•** `Maximize`

**•** `Minimize`

**•** `None`

`label` string Required. The story outcome label.

`successValue` string Optional. The value if the story succeeded.

`type` DiscoveryStoryOutcomeType Required. The story outcome type. One of the following strings:

**•** `Categorical`

**•** `Count`

**•** `Number`

**•** `Text`

Declarative Metadata Sample Definitions

Here is a sample DiscoveryStory:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DiscoverStory xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <application>MyStoryApp</application>

      <autopilot>Enabled</autopilot>

      <classificationThreshold>0.7383</classificationThreshold>

      <label>SubscriberChanges</label>

      <outcome>

        <field>Subscriber</field>

        <goal>Minimize</goal>

        <label>SubscriberChangeOutcome</label>

        <successValue>Success</successValue>

        <type>Numerical</type>

      </outcome>

      <sourceContainer>01X00000000xxxx1AB</sourceContainer>

      <sourceType>AnalyticsDataset</sourceType>

   </DiscoveryStory>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types Document Document

Represents a Document. All documents must be in a document folder, such as `sampleFolder/TestDocument` .

This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Retrieving Documents

You can’t use the wildcard (*) symbol with documents in `package.xml` . To retrieve the list of documents for populating
### package.xml with explicit names, call listMetadata() and pass in DocumentFolder as the type. Note that DocumentFolder

is not returned as a type in `describeMetadata()` . Document is returned from `describeMetadata()` with an associated
attribute of `inFolder` set to true. If that attribute is set to true, you can construct the type by using the component name with the
word Folder, such as DocumentFolder.

The following example shows folders in `package.xml` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyDBFolder/MyDBName</members>

        <name>Dashboard</name>

      </types>

      <types>

        <members>MyDocumentFolder/MyDocumentName</members>

        <name>Document</name>

      </types>

      <types>

        <members>unfiled$public/MarketingProductInquiryResponse</members>

        <members>unfiled$public/SalesNewCustomerEmail</members>

        <name>EmailTemplate</name>

      </types>

      <types>

        <members>MyReportFolder/MyReportName</members>

        <name>Report</name>

      </types>

      <version>66.0</version>

   </Package>

### For each document an accompanying metadata file named DocumentFilename -meta.xml is created in the document folder.
```

For example, for a document `TestDocument.png` in the sampleFolder folder, there’s a `TestDocument.png-meta.xml` in
the `documents/sampleFolder` of the package.

Version

### Documents are available in API version 10.0 and later.

In API version 17.0 and later, you can delete a folder containing documents moved to the Recycle Bin. When you delete the folder, any
related documents in the Recycle Bin are permanently deleted.

In API version 18.0 and later, documents do not need an extension.


Metadata Types Document

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`content` base64 Content of the document. Base 64-encoded binary data. Prior to making
an API call, client applications must encode the binary attachment data

as base64. Upon receiving a response, client applications must decode
the base64 data to binary. This conversion is usually handled for you by
a SOAP client. This field is inherited from the MetadataWithContent
component.

`description` string A description of the document. Enter a description to distinguish this
document from others.

`fullName` string The name of the document, including the folder name. In version 17.0
and earlier, the `fullName` included the document extension. In version

18.0 and later, the `fullName` does not include the file extension. The
`fullName` can contain only underscores and alphanumeric characters.
It must be unique, begin with a letter, not include spaces, not end with
an underscore, and not contain two consecutive underscores. If this field
contained characters before version 14.0 that are no longer allowed, the
characters were stripped out of this field, and the previous value of the
field was saved in the `name` field. This field is inherited from the
Metadata component.

`internalUseOnly` boolean

Required. Indicates whether the document is confidential ( `true` ) or not
( `false` ). This field and `public` are mutually exclusive; you cannot
set both to `true` .

`keywords` string Contains one or more words that describe the document. A check for
matches to words in this field is performed when doing a search.

`name` string The list of characters allowed in the `fullName` field has been reduced
for versions 14.0 and later. This field contains the value contained in the

`fullName` field before version 14.0. This field is only populated if the
value of the `fullName` field contained characters that are no longer
accepted in that field.

`public` boolean Required. Indicates whether the document is an image available for
HTML email templates and does not require a Salesforce username and

password to view in an email ( `true` ) or not ( `false` ). If the images will
be used as a custom app logo or custom tab icon, both of which require
a Salesforce username and password to view, set this field to `false` .
This field and `internalUseOnly` are mutually exclusive; you cannot
set both to `true` .


### Metadata Types DocumentCategory

Declarative Metadata Sample Definition

The following is the definition of a document:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Document xmlns="http://soap.sforce.com/2006/04/metadata">

      <internalUseOnly>false</internalUseOnly>

      <name>Q2 Campaign Analysis</name>

      <public>false</public>

      <description>Analyze Q2 campaign effectiveness</description>

   </Document>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Folder

### DocumentCategory

Represents a document category.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DocumentCategory components have the suffix .documentCategory and are stored in the documentCategory folder.

Version

### DocumentCategory components are available in API version 59.0 and later.

Special Access Rules

Fields

**Field Name** **Description**

```
description

```

**Field Type**
string


### Metadata Types DocumentCategoryDocumentType

**Field Name** **Description**

**Description**
A description of the DocumentCategory.

```
isProtected

masterLabel

```

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default value is `false` .

**Field Type**
string

**Description**

Required.

The master label of the DocumentCategory. This internal label doesn’t get translated.

Declarative Metadata Sample Definition

The following is an example of a DocumentCategory component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DocumentCategory xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>Address_Proof</masterLabel>

</DocumentCategory>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>DocumentCategory</name>

   </types>

   <version>59.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DocumentCategoryDocumentType

Represents the junction between a DocumentCategory and a DocumentType. Puts a DocumentType in a DocumentCategory.


Metadata Types DocumentCategoryDocumentType

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

DocumentCategoryDocumentType components have the suffix `.documentCategoryDocumentType` and are stored in the
`documentCategoryDocumentTypes` folder.

Version

DocumentCategoryDocumentType components are available in API version 59.0 and later.

Special Access Rules

Fields

**Field Name** **Description**

```
documentCategory

documentType

isProtected

masterLabel

```

**Field Type**
string

**Description**

Required.

The master label of the related DocumentCategory.

**Field Type**
string

**Description**

Required.

The master label of the related DocumentType.

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default value is `false` .

**Field Type**
string

**Description**

Required.


### Metadata Types DocumentChecklistSettings

**Field Name** **Description**

The master label of the DocumentCategoryDocumentType. This internal label doesn’t
get translated.

Declarative Metadata Sample Definition

The following is an example of a DocumentCategoryDocumentType component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DocumentCategoryDocumentType xmlns="http://soap.sforce.com/2006/04/metadata">

      <documentCategory>Address_Proof</documentCategory>

      <documentType>Utility_Bill</documentType>

      <masterLabel>junction1</masterLabel>

   </DocumentCategoryDocumentType>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8" standalone="yes"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>DocumentCategory</name>

      </types>

      <types>

        <members>*</members>

        <name>DocumentCategoryDocumentType</name>

      </types>

      <types>

        <members>*</members>

        <name>DocumentType</name>

      </types>

      <version>59.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DocumentChecklistSettings

Represents an org’s DocumentChecklistItem settings.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for more details.


Metadata Types DocumentChecklistSettings

File Suffix and Directory Location

DocumentChecklistSettings components are stored in the `DocumentChecklist.settings` file in the `settings` folder. The
`.settings` files are different from other named components because there’s only one settings file for each settings component.

Version

DocumentChecklistSettings components are available in API versions 55.0 and later.

Fields

**Field Name** **Field Type** **Description**

`dciCustomSharing` boolean

Indicates whether the custom sharing rule for document checklist items
is enabled for your org ( `true` ) or not ( `false` ). The default value is
`false` .

`deleteDCIWithFiles` boolean Indicates whether deletion of document checklist items is enabled for
your org ( `true` ) or not ( `false` ). The default value is `false` .

Declarative Metadata Sample Definition

The following is an example of a DocumentChecklistSettings.settings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DocumentChecklistSettings

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <dciCustomSharing>true</dciCustomSharing>

 <deleteDCIWithFiles>true</deleteDCIWithFiles>

</DocumentChecklistSettings>

```

Example Package Manifest

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <types>

  <members>DocumentChecklist</members>

  <name>Settings</name>

 </types>

 <version>55.0</version>

</Package>

```


### Metadata Types DocumentType

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DocumentType

Represents a document type.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DocumentType components have the suffix .documentType and are stored in the documentTypes folder.

Version

### DocumentType components are available in API version 59.0 and later.

Special Access Rules

Fields

**Field Name** **Description**

```
description

isActive

masterLabel

```

**Field Type**
string

**Description**
A description of the DocumentType.

**Field Type**
boolean

**Description**

Required.

Specifies whether the DocumentType is active.

**Field Type**
string

**Description**

Required.


### Metadata Types DuplicateRule

**Field Name** **Description**

The master label of the DocumentType. This internal label doesn’t get translated.

Declarative Metadata Sample Definition

The following is an example of a DocumentType component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DocumentType xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>Utility_Bill</description>

      <isActive>true</isActive>

      <masterLabel>Utility_Bill</masterLabel>

   </DocumentType>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8" standalone="yes"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>DocumentType</name>

      </types>

      <version>59.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DuplicateRule

Represents a rule that specifies how duplicate records in an object are detected. This type extends the Metadata metadata type and
inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### DuplicateRule components have the .duplicateRule  suffix and are stored in the duplicateRules/  directory. The name

of the component file is based on the name of the object associated with the rule. For example, the component file name
`duplicateRules/Account.Standard_Account_Duplicate_Rule.duplicateRule` describes a duplicate rule
component associated with the Account object.

Version

### DuplicateRule components are available in API version 66.0 and later.


Metadata Types DuplicateRule

Fields

**Field Name** **Field Type** **Description**

Required. Determines what the duplicate rule does when users or the
DuplicateRule API try to insert a record that is a duplicate. Valid values
are:

```
Allow
```

For users, if `operationsOnInsert` is set to `alert`, the UI
displays the value of `alertText` in a dialog. The dialog prompts

users to continue or cancel. If the user chooses to continue, the
insertion proceeds. If the user chooses to cancel, the record isn’t
inserted.

The DuplicateRule API returns an error code and a message. To
complete the insertion, the code must set the `allowSave` field
in DuplicateRuleHeader to `true` and reissue the request.

If `operationsOnInsert` isn’t set to `alert`, the UI inserts the
record without issuing an alert. The API inserts the record and doesn’t
return an error code.

```
Block
```

For users, the UI displays an error message and prevents them from
inserting the new record. The DuplicateRule API returns an error and
doesn’t insert the record.

Required. Determines what the duplicate rule does when users or the
DuplicateRule API try to update a record, and the result is a duplicate.
Valid values are:

```
Allow
```

For users, if `operationsOnUpdate` is set to `alert`, the UI
displays the value of `alertText` in a dialog. The dialog prompts

users to continue or cancel. If the user chooses to continue, the
update proceeds. If the user chooses to cancel, the record isn’t
updated.

The DuplicateRule API returns a message. To complete the update,
the code must set the `allowSave` field in DuplicateRuleHeader
to `true` and reissue the request.

If `operationsOnUpdate` isn’t set to `alert`, the UI updates
the record without issuing an alert. The API updates the record and
doesn’t return an error code.

```
Block
```

For users, the UI displays an error message and prevents them from
continuing. The DuplicateRule API returns an error.


```
actionOnInsert

actionOnUpdate

```

DupeActionType
(enumeration of
type string)

DupeActionType
(enumeration of
type string)

Metadata Types DuplicateRule

**Field Name** **Field Type** **Description**

`alertText` string

Text that’s sent when the duplicate rule is triggered. The text is only sent
if `isActive` is `true` . In the UI, the text displays as a message. The
DuplicateRule API returns the message in its response.

You can set a value for `alertText` only when you have
`actionOnInsert` or `actionOnUpdate` (or both) set to `Allow` .

Otherwise, you receive a validation error when you add or update this
component.

`description` string Required. Text that describes the duplicate rule. The value is
customer-supplied, but isn’t visible in the UI.

`duplicateRuleFilter` DuplicateRuleFilter

Required. Criteria that define how to find records to consider when
looking for duplicates. For example, use `duplicateRuleFilter`
to exclude records from the match when looking for duplicates.

`duplicateRuleMatchRules` DuplicateRuleMatchRule[] Required. One or more MatchingRule components for the DuplicateRule.
A `MatchingRule` controls what constitutes a match between records.

`isActive` boolean Required. If `true`, the DuplicateRule detects duplicate records.
Otherwise, the rule has no effect.

`masterLabel` string Required. Label for this DuplicateRule. This value is the internal label for
the rule.

`operationsOnInsert` string[]

`operationsOnUpdate` string[]

Required. Controls the action to take when `actionOnInsert` is set
to `Allow` and the duplicate rule is triggered. Either one or both of
these values can be set in the array:

```
alert
```

If set, the action specified in `actionOnInsert` occurs; otherwise,
the insert proceeds.

```
report
```

If set, the insert operation is added to the report of duplicates.

Required. Controls the action to take when `actionOnUpdate` is set
to `Allow` and the duplicate rule is triggered. Either one or both of
these values can be set in the array:

```
alert
```

If set, the action specified in `actionOnUpdate` occurs; otherwise,
the update proceeds.

```
report
```

If set, the update operation is added to the report of duplicates.

Required. Determines how record sharing rules affect duplicate
management. Valid values are:

```
EnforceSharingRules
```

Sharing rules affect duplicate management. If a duplicate rule is
triggered because an insert or update duplicates an existing record,


```
securityOption

```

DupeSecurityOptionType
(enumeration of
type string)

Metadata Types DuplicateRule

**Field Name** **Field Type** **Description**

but the running user doesn’t have sharing access to that record, the
insert or update proceeds. The sharing rule doesn’t prevent the user
from creating or updating the record because the record is hidden
from the user. No message is issued.

```
                           BypassSharingRules
```

Sharing rules don’t affect duplicate management. If a duplicate rule
is triggered because an insert or update duplicates an existing record,
sharing rules are ignored, but other access restrictions apply.

`sortOrder` int Required. Determines the order in which duplicate rules are applied.

DuplicateRuleMatchRule

Describes the MatchingRule associated with the `DuplicateRule` . The `MatchingRule` identifies duplicate records.

**Field Name** **Field Type** **Description**

`matchRuleSObjectType` string Required. The name of the target object of the matching rule. For
example, if you define a duplicate rule for Contact records, and you want

to match with Lead records, the value of `matchRuleSObjectType`
is Lead.

`matchingRule` string Required. Value that corresponds to the value of `developerName`
in the MatchingRule for this duplicate rule.

`objectMapping` ObjectMapping

DuplicateRuleFilter

Required. Foreign key to an ObjectMapping that maps fields from the
duplicate rule’s object to fields in the target object specified by
`matchRuleSObjectType` .

Specifies filter criteria for a DuplicateRule. Salesforce only applies the DuplicateRule if the record matches the criteria.

**Field Name** **Field Type** **Description**

`booleanFilter` string Required. A string of boolean operators that establishes the filter logic
for the filter items specified in `duplicateRuleFilterItems` .

`duplicateRuleFilterItems` DuplicateRuleFilterItem[] Required. A list of DuplicateRuleFilterItem components.

DuplicateRuleFilterItem

This type extends the FilterItem type and inherits all its fields.

**Field Name** **Field Type** **Description**

`sortOrder` int Required. The order of this item in the duplicate rule filter.


Metadata Types DuplicateRule

**Field Name** **Field Type** **Description**

`table` string

ObjectMapping

Required. The object that has the field specified in the `field` field of
DuplicateRuleFilterItem. See the documentation for FilterItem for the
definition of `field` .

Represents a map of fields in the input object of the DuplicateRule to fields in the output object of DuplicateRule. The input object is
the object associated with the DuplicateRule. The output object can be the same object or a different object with similar fields.

For example, you can have a DuplicateRule that looks for duplicates between the Contact object and the Lead object. In this case, the
input object is Contact, and the output object is Lead.

**Field Name** **Field Type** **Description**

`inputObject` string Required. The input object for the duplicate rule. The DuplicateRule is
associated with this object. For example, if you define a duplicate rule

for Contact records, and you want to match with Lead records, the value
of `inputObject` is Contact.

`mappingFields` ObjectMappingField[] Required. The mapping of source object fields to target object fields for
the duplicate rule.

`outputObject` string Required. The output object for the duplicate rule. This value is the same
as the value of the `matchRuleSObjectType` field in

DuplicateRuleMatchRule. Any duplicate rules that this object has are
ignored when the DuplicateRule API uses the ObjectMapping.

ObjectMappingField

A field name in the input object of the DuplicateRule, and the corresponding field name in the output object.

**Field Name** **Field Type** **Description**

`inputField` string Required. Field in the object specified by the `inputObject` field in
ObjectMapping. This field is mapped to the field in `outputField`,

which is assumed to be a field in the object specified by the
`outputObject` field in ObjectMapping.

`outputField` string Required. Field in the object specified by the `outputObject` field
in ObjectMapping. The field is mapped to the field name in

`inputField`, which is assumed to be a field in the object specified
by the `inputObject` in ObjectMapping.


Metadata Types DuplicateRule

Declarative Metadata Sample Definition

The following is an example of a DuplicateRule component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DuplicateRule xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <actionOnInsert>Allow</actionOnInsert>

      <actionOnUpdate>Allow</actionOnUpdate>

      <alertText>You are creating a duplicate record. Use an existing record

   instead.</alertText>

      <description>Detects a contact that duplicates a Lead</description>

      <duplicateRuleFilter>

        <booleanFilter xsi:nil="true"/>

        <duplicateRuleFilterItems>

           <field>Username</field>

           <operation>equals</operation>

           <value>user@example.com</value>

           <sortOrder>1</sortOrder>

           <table>User</table>

        </duplicateRuleFilterItems>

      </duplicateRuleFilter>

      <duplicateRuleMatchRules>

        <matchRuleSObjectType>Lead</matchRuleSObjectType>

        <matchingRule>ContactToLeadDuplicate_matching_rule</matchingRule>

        <objectMapping>

           <inputObject>Contact</inputObject>

           <mappingFields>

             <inputField>FirstName</inputField>

             <outputField>FirstName</outputField>

           </mappingFields>

           <mappingFields>

             <inputField>LastName</inputField>

             <outputField>LastName</outputField>

           </mappingFields>

           <outputObject>Lead</outputObject>

        </objectMapping>

      </duplicateRuleMatchRules>

      <isActive>true</isActive>

      <masterLabel>ContactToLeadDuplicate</masterLabel>

      <operationsOnInsert>Alert</operationsOnInsert>

      <operationsOnInsert>Report</operationsOnInsert>

      <operationsOnUpdate>Alert</operationsOnUpdate>

      <operationsOnUpdate>Report</operationsOnUpdate>

      <securityOption>EnforceSharingRules</securityOption>

      <sortOrder>1</sortOrder>

   </DuplicateRule>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>ContactToLeadDuplicate</members>

        <name>DuplicateRule</name>

```


### Metadata Types EclairGeoData

```
      </types>

      <version>38.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EclairGeoData

Represents an Analytics custom map chart. Custom maps are user-defined maps that are uploaded to Analytics and are used just as
standard maps are. Custom maps are accessed in Analytics from the list of maps available with the map chart type.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### EclairGeoData components have the suffix geodata and are stored in the eclair folder.

Version

### EclairGeoData components are available in API version 39.0 and later.

Fields

**Field Name** **Field Type** **Description**

`maps` EclairMap[] A list of EclairMap objects. Each EclairMap object specifies the bounding
box (if any) and the map name that appears in the user interface.

`masterLabel` string Required. Label for this object. This display value is the internal label that
is not translated.

EclairMap

**Field Name** **Field Type** **Description**

`boundingBoxBottom` double When bounding-box coordinates are used, this contains the bottom coordinate.

`boundingBoxLeft` double When bounding-box coordinates are used, this contains the left side coordinate.

`boundingBoxRight` double When bounding-box coordinates are used, this contains the right side
coordinate.

`boundingBoxTop` double When bounding-box coordinates are used, this contains the top coordinate.


Metadata Types EclairGeoData

**Field Name** **Field Type** **Description**

`mapLabel` string Required. The user-interface name of the map. This name appears in the maps
list for the map chart in Analytics.

`mapName` string Required. Label for this object. This display value is the internal label that is not
translated.

`projection` string Required. The type of map projection used to create the map. Valid values are:

**•** Equirectangular

**•** Mercator

**•** AlbersUSA

Declarative Metadata Sample Definition

The following is an example of an EclairGeoData component:

```
         <EclairGeoData xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

           <content xsi:nil="true"/>

           <maps>

            <boundingBoxBottom>0.0</boundingBoxBottom>

            <boundingBoxLeft>100.0</boundingBoxLeft>

            <boundingBoxRight>100.0</boundingBoxRight>

            <boundingBoxTop>0.0</boundingBoxTop>

            <mapLabel>WorldMap0 Label</mapLabel>

            <mapName>WorldMap0</mapName>

            <projection>Equirectangular</projection>

           </maps>

           <maps>

            <boundingBoxBottom>1.0</boundingBoxBottom>

            <boundingBoxLeft>101.0</boundingBoxLeft>

            <boundingBoxRight>101.0</boundingBoxRight>

            <boundingBoxTop>1.0</boundingBoxTop>

            <mapLabel>WorldMap1 Label</mapLabel>

            <mapName>WorldMap1</mapName>

            <projection>Mercator</projection>

           </maps>

           <masterLabel>WorldMapGeoDataToCreate Label</masterLabel>

         </EclairGeoData>

```

The following is an example `package.xml` that references the previous definition.

```
        <?xml version="1.0" encoding="UTF-8"?>

        <Package xmlns="http://soap.sforce.com/2006/04/metadata">

         <types>

           <members>*</members>

           <name>EclairGeoData</name>

         </types>

```


### Metadata Types EmailServicesFunction

```
         <version>39.0</version>

        </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EmailServicesFunction

Represents an email service. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### EmailServicesFunction components have the suffix .xml and are stored in the emailservices folder.

Version

### EmailServicesFunction components are available in API version 42.0 and later.

Fields

**Field Name** **Field Type** **Description**

`apexClass` string Required. The name of the Apex class that the email service uses to
process inbound messages.

```
attachmentOption

```

EmailServicesAttOptions Required. Indicates the types of attachments the email service accepts.
(enumeration of One of the following values:
type string)

**•** `None` —The email service accepts the message but discards any
attachment.

**•** `NoContent` —The attachment metadata (filename, MIME type,
and so on) is provided to the Apex class, but the body is set to `null` .

**•** `TextOnly` —The email service only accepts the following types
of attachments:

**–** Attachments with a Multipurpose Internet Mail Extension (MIME)
type of text.

**–** Attachments with a MIME type of application/octet-stream and
a file name that ends with either a .vcf or .vcs extension. These
are saved as text/x-vcard and text/calendar MIME types,
respectively.

**•** `BinaryOnly` —The email service only accepts binary attachments,
such as image, audio, application, and video files.

**•** `All` —The email service accepts any type of attachment.


Metadata Types EmailServicesFunction

**Field Name** **Field Type** **Description**

Required. Indicates what the email service does with messages that fail
or do not support any of the authentication protocols if the
`isAuthenticationRequired` field is true.

One of the following values:

**•** `UseSystemDefault` —The system default is used.

**•** `Bounce` —The email service returns the message to the sender
with a notification that explains why the message was rejected.

**•** `Discard` —The email service deletes the message without
notifying the sender.

**•** `Requeue` —The email service queues the message for processing
in the next 24 hours. If the message is not processed within 24 hours,
the email service returns the message to the sender with a
notification that explains why the message was rejected.

Required. Indicates what the email service does with messages received
from senders who are not listed in the `authorizedSenders` field
on either the email service or email service address.

One of the following values:

**•** `UseSystemDefault` —The system default is used.

**•** `Bounce` —The email service returns the message to the sender
with a notification that explains why the message was rejected.

**•** `Discard` —The email service deletes the message without
notifying the sender.

**•** `Requeue` —The email service queues the message for processing
in the next 24 hours. If the message is not processed within 24 hours,
the email service returns the message to the sender with a
notification that explains why the message was rejected.

```
authenticationFailureAction

authorizationFailureAction

```

EmailServicesErrorAction
(enumeration of
type string)

EmailServicesErrorAction
(enumeration of
type string)

`authorizedSenders` string Configures the email service to only accept messages from the email
addresses or domains listed in this field. If the email service receives a

message from an unlisted email address or domain, the email service
performs the action specified in the
`authorizationFailureAction` field. Leave this field blank if
you want the email service to receive email from any email address.

`emailServicesAddresses` EmailServicesAddress[] A list of EmailServiceAddress records.

`errorRoutingAddress` email The destination email address for error notification email messages when
`isErrorRoutingEnabled` is `true` .

Required. Indicates what the email service does with messages it receives
when the email service itself is inactive.

One of the following values:

**•** `UseSystemDefault` —The system default is used.


```
functionInactiveAction

```

EmailServicesErrorAction
(enumeration of
type string)

Metadata Types EmailServicesFunction

**Field Name** **Field Type** **Description**

**•** `Bounce` —The email service returns the message to the sender
with a notification that explains why the message was rejected.

**•** `Discard` —The email service deletes the message without
notifying the sender.

**•** `Requeue` —The email service queues the message for processing
in the next 24 hours. If the message is not processed within 24 hours,
the email service returns the message to the sender with a
notification that explains why the message was rejected.

`functionName` string Required. The name of the email service in the API. This name can contain
only underscores and alphanumeric characters and must be unique in

your org. The value in this 64-character field must begin with a letter,
not include spaces, not end with an underscore, and not contain two
consecutive underscores.

In managed packages, this field prevents naming conflicts on package
installations. This field is automatically generated, but you can supply
your own value if you create the record using the API. With this field, a
developer can change the object’s name in a managed package and
the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`functionName` for each record. If no `functionName` is
specified, performance may slow while Salesforce generates one
for each record.

`isActive` boolean Indicates whether this object is active ( `true` ) or not ( `false` ).

`isAuthenticationRequired` boolean Configures the email service to verify the legitimacy of the sending server
before processing a message. The email service uses the SPF, SenderId,

and DomainKeys protocols to verify the sender's legitimacy: If the sending
server passes at least one of these protocols and does not fail any, the
email service accepts the email. If the server fails a protocol or does not
support any of the protocols, the email service performs the action
specified in the `authenticationFailureAction` field.

`isErrorRoutingEnabled` boolean

When incoming email messages can’t be processed, indicates whether
error notification email messages are routed to a chosen address or to
the senders.

`isTextAttachmentsAsBinary` boolean If `true`, text attachments are supplied to the Apex code as a
`Messaging.BinaryAttachment` instead of as a

`Messaging.TextAttachment` . This means that the body is
supplied as an Apex Blob instead of as an Apex String.

`isTlsRequired` boolean Not currently in use.


Metadata Types EmailServicesFunction

**Field Name** **Field Type** **Description**

Required. Indicates what the email service does with messages if the
total number of messages processed by all email services combined has
reached the daily limit for your organization.

One of the following values:

**•** `UseSystemDefault` —The system default is used.

**•** `Bounce` —The email service returns the message to the sender
with a notification that explains why the message was rejected.

**•** `Discard` —The email service deletes the message without
notifying the sender.

**•** `Requeue` —The email service queues the message for processing
in the next 24 hours. If the message is not processed within 24 hours,
the email service returns the message to the sender with a
notification that explains why the message was rejected.

The system calculates the limit by multiplying the number of user licenses
by 1,000.

```
overLimitAction

```

EmailServicesAddress

EmailServicesErrorAction
(enumeration of
type string)

Each email service has one or more email addresses to which users can send messages for processing. An email service only processes
messages it receives at one of its addresses.

**Field Name** **Field Type** **Description**

`authorizedSenders` string Configures the email service address to only accept messages from the email
addresses or domains listed in this field. If the email service address receives a

message from an unlisted email address or domain, the email service performs
the action specified in the `authorizationFailureAction` field of
its associated email service. Leave this field blank if you want the email service
address to receive email from any email address.

`developerName` string Required. The name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your org. It

must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. This 25-character field must be
unique among other EmailServicesAddress records under the same
EmailServiceFunction parent.

In managed packages, this field prevents naming conflicts on package
installations. This field is automatically generated, but you can supply your own
value if you create the record using the API. With this field, a developer can
change the object’s name in a managed package and the changes are reflected
in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`developerName` for each record. If no `developerName` is


### Metadata Types EmailTemplate

**Field Name** **Field Type** **Description**

specified, performance might be slow while Salesforce generates one
for each record.

`isActive` boolean Indicates whether this object is active ( `true` ) or not ( `false` ).

`localPart` string

Required. The local-part of the email service address, which is the string that
comes before the @ symbol. For the local-part of a Salesforce email address,
all alphanumeric characters are valid, plus the following special characters:

```
! # $ % & amp; ' * / = ? ^ _ + - ` { | } ~,

```

The dot character (.) is also valid as long as it's not the first or last character.
Email addresses aren’t case sensitive.

`runAsUser` string Required. The username of the user whose permissions the email service
assumes when processing messages sent to this address.

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EmailTemplate

Represents a template for an email, mass email, list email, or Sales Engagement email. Supported in first-generation managed packages
only.

This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Note: First-generation packaging only is supported for Lightning email templates.

File Suffix and Directory Location

### The file suffix is .email for the template file. The accompanying metadata file is named EmailTemplateName -meta.xml . EmailTemplate components are stored in the email folder in the corresponding package directory. For example, for an email template

named SampleTemplate in the sampleFolder folder, there’s a `SampleTemplate-meta.xml` in the `email/sampleFolder`
of the package.

Retrieving Email Templates

You can’t use the wildcard (*) symbol with email templates in `package.xml` . To retrieve the list of email templates for populating
### package.xml with explicit names, call listMetadata() and pass in EmailTemplate as the type.

The following example shows folders in `package.xml` :

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

```


Metadata Types EmailTemplate

```
        <members>MyDBFolder/MyDBName</members>

        <name>Dashboard</name>

      </types>

      <types>

        <members>MyDocumentFolder/MyDocumentName</members>

        <name>Document</name>

      </types>

      <types>

        <members>unfiled$public/MarketingProductInquiryResponse</members>

        <members>unfiled$public/SalesNewCustomerEmail</members>

        <name>EmailTemplate</name>

      </types>

      <types>

        <members>MyReportFolder/MyReportName</members>

        <name>Report</name>

      </types>

      <version>66.0</version>

   </Package>

```

Version

Email templates are available in API version 12.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`apiVersion` double

`attachedDocuments` string[]

The API version if it's a Visualforce email template. Every Visualforce email
template has an API version specified at creation. This field is available in API
version 16.0 and later.

A list of references to documents in your organization. These documents are
included as attachments in the email template. Each document is referenced
by its path, for example `MyFolder/MyDocument.txt` .

`attachments` Attachment[] A list of attachments for the email template.

`available` boolean Required. Indicates whether this template is offered to users when sending an
email ( `true` ) or not ( `false` ).

`content` base64Binary Content of the email template. Base 64-encoded binary data. Before making an
API call, client applications must encode the binary attachment data as base64.

Upon receiving a response, client applications must decode the base64 data to
binary. This conversion is handled for you by a SOAP client. This field contains:

**•** Binary content of the email body if `type` is set to `text`

**•** HTML email content if `type` is set to `html`

**•** HTML body if `type` is set to `custom`

**•** Visualforce body if `type` is set to `visualforce`


Metadata Types EmailTemplate

**Field Name** **Field Type** **Description**

This field is inherited from the MetadataWithContent component.

`description` string The email template description describes the reason for creating the template.

`encodingKey` Encoding (enumeration
of type string)

Required for Classic email templates. The default encoding setting is Unicode:
`UTF-8` . Change it if your template requires data in a different format.

Valid values include:

**•** `UTF-8` —Unicode (UTF-8)

**•** `ISO-8859-1` —General US & Western Europe (ISO-8859–1, ISO-LATIN-1)

**•** `Shift_JIS` —Japanese (Shift-JIS)

**•** `ISO-2022-JP` —Japanese (JIS)

**•** `EUC-JP` —Japanese (EUC-JP)

**•** `x-SJIS_0213` —Japanese (Shift-JIS_2004)

**•** `ks_c_5601-1987` —Korean (ks_c_5601-1987)

**•** `Big5` —Traditional Chinese (Big5)

**•** `GB2312` —Simplified Chinese (GB2312)

**•** `Big5-HKSCS` —Traditional Chinese Hong Kong (Big5–HKSCS)

Lightning email templates don’t use this field. Instead, the encoding values are
taken directly from the user’s encoding settings.

`fullName` string The email template developer name used as a unique identifier for API access.
The `fullName` can contain only underscores and alphanumeric characters.

It must be unique, begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. If this field contained
characters before version 14.0 that are no longer allowed, the characters were
stripped out of this field, and the previous value of the field was saved in the
`name` field. This field is inherited from the Metadata component.

`letterhead` string The letterhead name associated with this email template. Only available when
`type` is set to `html` .

`name` string

`packageVersions` PackageVersion[]

Required. Email template name. The list of characters allowed in the `fullName`
field has been reduced for versions 14.0 and later. This field contains the value
contained in the `fullName` field before version 14.0.

The list of package versions for any managed packages containing components
that are referenced by this email template. This field is only relevant for Visualforce
email templates.

[For more information about managed packages, see Second-Generation](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm)
[Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm) _Salesforce DX Developer Guide_ . This field is available in
API version 16.0 and later.

```
relatedEntityType

```

Object Name Reserved for future use with Lightning Experience.
(enumeration of type
string)


Metadata Types EmailTemplate

**Field Name** **Field Type** **Description**

Required. The style of the template. This field is only available when `type` is set
to `html` .

Valid style values include:

**•** `none`

**•** `freeForm`

**•** `formalLetter`

**•** `promotionRight`

**•** `promotionLeft`

**•** `newsletter`

**•** `products`

The email subject.

The limit is 1,000 characters for Lightning email templates and 230 characters
for Classic email templates.

```
style

```

EmailTemplateStyle
(enumeration of type
string)

`subject` string

`textOnly` string The text of the email body if `type` is set to `html` or `custom` .

Required. The email template type.

The valid values are:

**•** `text` - all users can create or change text email templates.

**•** `html` - administrators and users with the “Edit HTML Templates” permission
can create HTML email templates based on a letterhead.

**•** `custom` - administrators and users with the “Edit HTML Templates”
permission can create custom HTML email templates without using a
letterhead. You must either know HTML or obtain the HTML code to insert
in your email template.

**•** `visualforce` - administrators and users with the Customize Application
permission can create email templates using Visualforce.

```
type

UiType

```

Example:

EmailTemplateType
(enumeration of type
string)

EmailTemplateUiType Indicates the user interface where this template is usable. Valid values are:
(enumeration of type

**•** `Aloha` (Salesforce Classic)

string)

**•** `Aloha` (Salesforce Classic)

**•** `SFX` (Lightning Experience)

```
<EmailTemplate>

  <available>true</available>

```

**•** `SFX_Sample` (Lightning Experience Sample)

If `UiType` is `SFX`, the `type` must be `custom` .

Packaging is supported for Salesforce Classic email templates only.


Metadata Types EmailTemplate

```
        <description>Notification that user has been added to a community.</description>

        <encodingKey>UTF-8</encodingKey>

        <name>Communities: New Member Welcome Email</name>

        <style>none</style>

        <subject>Welcome to {!Community_Name}</subject>

        <type>custom</type>

        <uiType>Aloha</uiType>

      </EmailTemplate>

```

Attachment

Attachment represents an email attachment.

**Field** **Field Type** **Description**

`content` base64Binary Required. The attachment content. Base 64-encoded binary
data. Before making an API call, client applications must encode

the binary attachment data as base64. Upon receiving a
response, client applications must decode the base64 data to
binary. This conversion is handled for you by a SOAP client.

`name` string Required. The attachment file name.

Declarative Metadata Sample Definition

Here's a sample XML definition of an email template.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EmailTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

      <available>true</available>

      <description>Sample Email Template</description>

      <encodingKey>ISO-8859-1</encodingKey>

      <name>Sample Email Template</name>

      <style>none</style>

      <subject>Sample email subject</subject>

      <textOnly>Your case has been resolved.</textOnly>

      <type>custom</type>

   </EmailTemplate>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Letterhead


### Metadata Types EmbeddedServiceBranding EmbeddedServiceBranding

Represents the branding for each Embedded Service deployment. This type extends the Metadata metadata type and inherits its
`fullName` field.

This object works only with the legacy chat products. For Messaging for In-app and Web, use the BrandingSet object.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### EmbeddedServiceBranding components are stored in the developer_name .EmbeddedServiceBranding file in the EmbeddedServiceBranding folder.

Version

### EmbeddedServiceBranding is available in API version 39.0 and later.

Fields

**Field Name** **Field Type** **Description**

`contrastInvertedColor` string

Accent branding color used in the embedded component, displayed as
a hexadecimal value. Changes made to this field in the API aren’t reflected
in the embedded component.

`contrastPrimaryColor` string Accent branding color used in the embedded component, displayed as
a hexadecimal value.

`embeddedServiceConfig` string Required. The Embedded Service configuration that this branding applies
to.

`font` string Font used in the text of the embedded component.

`height` int Height of the embedded component. Available in API version 43.0 and
later.

`masterLabel` string Required. The name of the Embedded Service configuration node.

`navBarColor` string Color used for the header in the embedded component, displayed as a
hexadecimal value.

`navBarTextColor` string

Color used for the text and icons in the header in the embedded
component, displayed as a hexadecimal value. Available in API version
49.0 and later.

`primaryColor` string Primary branding color used in the embedded component, displayed
as a hexadecimal value.

`secondaryColor` string Secondary branding color used in the embedded component, displayed
as a hexadecimal value.


### Metadata Types EmbeddedServiceConfig

**Field Name** **Field Type** **Description**

`secondaryNavBarColor` string Secondary branding color used for the header in the embedded
component, displayed as a hexadecimal value. It applies to the header

in the chat feature when it's trying to reconnect because of lost internet
connection. Available in API version 49.0 and later.

`width` int Width of the embedded component. Available in API version 43.0 and
later.

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceBranding file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EmbeddedServiceBranding xmlns="http://soap.sforce.com/2006/04/metadata">

      <contrastInvertedColor>#ffffff</contrastInvertedColor>

      <contrastPrimaryColor>#333333</contrastPrimaryColor>

      <embeddedServiceConfig>EswConfig001</embeddedServiceConfig>

      <font>Salesforce Sans</font>

      <height>498</height>

      <masterLabel>EmbeddedServiceBranding_Parent04IRM000000002a_16033cd2c16</masterLabel>

      <navBarColor>#222222</navBarColor>

      <primaryColor>#222222</primaryColor>

      <secondaryColor>#005290</secondaryColor>

      <width>320</width>

   </EmbeddedServiceBranding>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EmbeddedServiceConfig

Represents a setup node for creating an Embedded Service for Web deployment. This type extends the Metadata metadata type and
inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### EmbeddedServiceConfig components have the suffix .EmbeddedServiceConfig and are stored in the EmbeddedServiceConfig folder.


Metadata Types EmbeddedServiceConfig

Version

EmbeddedServiceConfig is available in API version 37.0 and later.

Fields

**Field Name** **Field Type** **Description**

`areGuestUsersAllowed` boolean Specifies whether a user must be logged in to access an embedded
component. Available in API version 45.0 and later.

```
authMethod

```

EmbeddedServiceAuthMethod Type of login method selected for this Embedded Service deployment.
(enumeration of Valid values are:
type string)

**•** `CommunitiesLogin` –Customers log in using Communities.

**•** `CustomLogin` –Customers log in using your own custom
authentication.

Available in API version 43.0 and later.

`branding` string The branding set that has all of the branding configurations for this
Embedded Service configuration. Available in API version 52.0 and later.

`customMinimizedComponent` string The custom Lightning component that’s used in this Embedded Service
deployment in its minimized state. Available in API version 43.0 to 45.0.

`deploymentFeature` EmbeddedServiceDeploymentFeature(enumeration The conversation type of this Embedded Service deployment. Valid
of type string) values are:

**•** `EmbeddedMessaging` —Messaging for In-App and Messaging
for Web deployments

**•** `Flows`

**•** `FieldService`

**•** `LiveAgent`

**•** `None`

Available in API version 52.0 and later.

```
deploymentType

```

EmbeddedServiceDeploymentType The platform this Embedded Service is deployed to. Valid values are:
(enumeration of

**•** `Mobile` —For future use

type string)

**•** `Mobile` —For future use

**•** `Web`

`embeddedServiceAppointmentSettings` EmbeddedServiceAppointmentSe **t** ings[]

**•** `API`

Available in API version 51.0 and later.

The settings of the Embedded Service deployment whose
`deploymentFeature` is `FieldService` . Available in API version
46.0 and later.

`embeddedServiceCustomComponents` EmbeddedServiceCustomComponent The custom components used in this Embedded Service deployment.
on page 1006[] Available in API version 44.0 and later.


Metadata Types EmbeddedServiceConfig

**Field Name** **Field Type** **Description**

`embeddedServiceCustomLabels` EmbeddedServiceCustomLabel The custom labels used in this Embedded Service deployment. Available
on page 1007[] in API version 44.0 and later.

`embeddedServiceCustomizations` EmbeddedServiceCustomization
on page 1008[]

The customizations used in this Embedded Service deployment. Each
customization is associated with a static resource. Available in API version
50.0 and later.

`embeddedServiceFlowConfig` EmbeddedServiceFlowConfig Represents a setup node for creating an embedded flow. Available in
on page 1012[] API version 45.0 and later.

`embeddedServiceFlows` EmbeddedServiceFlow All of the flows used by this Embedded Service deployment. Available
on page 1011[] in API version 45.0 and later.

`embeddedServiceLayouts` EmbeddedServiceLayout[] The layout of an Appointment Management deployment of an
Embedded Service. Available in API version 44.0 and later.

`isEnabled` boolean Indicates if this Embedded Service deployment is enabled (true).

`isTermsAndConditionsEnabled` boolean Indicates whether Terms and Conditions is displayed. Displaying Terms
and Conditions is supported if the `deploymentFeature` is either

`EmbeddedMesssaging` or `LiveAgent` . The default is `false` .
Available in API version 59.0 and later.

`isTermsAndConditionsRequired` boolean Indicates whether acceptance of the Terms and Conditions is required
before starting a chat. Displaying Terms and Conditions is supported if

the `deploymentFeature` is either `EmbeddedMesssaging`
or `LiveAgent` . The default is `false` . Available in API version 59.0
and later.

`masterLabel` string Required. The name of the Embedded Service configuration node.
Available in API version 37.0 and later.

`shouldHideAuthDialog` boolean Specifies whether the prompt that the customer log in again during a
flow is hidden ( `true` ) or not ( `false` ). When it’s hidden, the customer

is taken directly to your login page. This field is set to `false` by default.
Available in API version 43.0 and later.

`site` string Required. The name of the Experience site or website connected to this
Embedded Service deployment. Available in API version 37.0 and later.

EmbeddedServiceAppointmentSettings

Returns the settings of an Embedded Service deployment whose `deploymentFeature` is `FieldService` . Available in API
version 46.0 and later.

**Field Name** **Description**

```
appointmentConfirmImg

```

**Field Type**
string


Metadata Types EmbeddedServiceConfig

**Field Name** **Description**

**Description**
The URL of the image to display when an appointment is confirmed.

```
enabled

homeImg

logoImg

shouldShowExistingAppointment

shouldShowNewAppointment

```

**Field Type**
boolean

**Description**

Required.

Indicates whether this deployment is enabled. The default is `false` .

**Field Type**
string

**Description**
The URL of the image to display on the appointment management widget home
screen.

**Field Type**
string

**Description**
The URL of the logo to display in the appointment management widget.

**Field Type**
boolean

**Description**
Indicates whether existing appointments are displayed in the appointment
management widget. The default is `false` .

**Field Type**
boolean

**Description**
Indicates whether new appointments are displayed in the appointment management
widget. The default is `false` .

EmbeddedServiceCustomComponent

Returns a custom component that’s associated with an EmbeddedServiceConfig setup.


Metadata Types EmbeddedServiceConfig

EmbeddedServiceCustomLabel

Returns a custom label that’s associated with an EmbeddedServiceConfig setup.


Metadata Types EmbeddedServiceConfig

EmbeddedServiceCustomization

Returns the customization associated with the Embedded Service feature. Available in API version 50.0 and later.

EmbeddedServiceForm

Returns the form that’s used for pre-chat. Available in API version 62 and later.


Metadata Types EmbeddedServiceConfig

EmbeddedServiceFormField

Represents an individual field in a prechat form. Available in API version 62 or higher.


Metadata Types EmbeddedServiceConfig

embeddedServiceMessagingChannel

Returns the settings of an Embedded Service deployment whose

```
deploymentFeature

```

is EmbeddedMessaging. Available in API version 62 or higher.


Metadata Types EmbeddedServiceConfig

EmbeddedServiceResource

Returns the static resource associated with the Embedded Service Chat feature customization. Available in API version 50.0 and later.

EmbeddedServiceFlow

Returns an embedded flow that’s associated with an EmbeddedServiceConfig setup.


Metadata Types EmbeddedServiceConfig

EmbeddedServiceFlowConfig

Returns the EmbeddedServiceFlowConfig type.

EmbeddedServiceLayout

Returns the layout of an Embedded Service deployment whose `deploymentFeature` is `FieldService` . Available in API version
44.0 and later.

**Field Name** **FieldDescription**
**Type**

`embeddedServiceLayoutRules` []tRledSrviceLayo **u** Embe **de** The appointment statuses that the layout of the Embedded Service deployment is valid
for.

`layout` string The FlexiPage that represents the layout of this Embedded Service deployment.

```
layoutType

```

SrviceLayoutTypeEmb **ed**
(enumeration
f 

The type of layout applied to the Embedded Service deployment.

Values are:

**•** `FS_AppointmentHome`
type
string)

EmbeddedServiceLayoutRule

Returns an appointment status for which the Embedded Service layout is valid for. This subtype is for Embedded Service deployments
whose `deploymentFeature` is `FieldService` . Available in API version 44.0 and later.

**Field Name** **Field Type** **Description**

`appointmentStatus` string The service appointment status that the EmbeddedServiceLayout subtype
is valid for.


Metadata Types EmbeddedServiceConfig

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceConfig file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EmbeddedServiceConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <areGuestUsersAllowed>false</areGuestUsersAllowed>

      <deploymentType>Mobile</deploymentType>

      <deploymentFeature>EmbeddedMessaging</deploymentFeature>

      <masterLabel>ESWOne</masterLabel>

      <shouldHideAuthDialog>false</shouldHideAuthDialog>

      <embeddedServiceMessagingChannel>

        <isEnabled>true</isEnabled>

        <shouldShowTypingIndicators>false</shouldShowTypingIndicators>

        <shouldShowReadReceipts>false</shouldShowReadReceipts>

        <shouldShowDeliveryReceipts>false</shouldShowDeliveryReceipts>

        <shouldShowEmojiSelection>false</shouldShowEmojiSelection>

        <shouldStartNewLineOnEnter>false</shouldStartNewLineOnEnter>

        <messagingChannel>EM1</messagingChannel>

      </embeddedServiceMessagingChannel>

      <embeddedServiceForms>

        <isActive>true</isActive>

        <displayContext>Session</displayContext>

        <embeddedServiceFormFields>

           <displayOrder>0</displayOrder>

           <formField>_FirstName</formField>

           <messagingChannelParameterType>Standard</messagingChannelParameterType>

           <formFieldType>Text</formFieldType>

           <isHidden>false</isHidden>

           <isRequired>true</isRequired>

           <embeddedServiceCustomLabels>

   <customLabel>EM_PreChat_Base_PrechatCustomFieldLabel_133xx0000004GG2_5523048</customLabel>

             <labelKey>EM_PreChat_Base_PrechatCustomFieldLabel</labelKey>

             <feature>EmbeddedMessaging</feature>

           </embeddedServiceCustomLabels>

        </embeddedServiceFormFields>

        <embeddedServiceFormFields>

           <displayOrder>1</displayOrder>

           <formField>_LastName</formField>

           <messagingChannelParameterType>Standard</messagingChannelParameterType>

           <formFieldType>Text</formFieldType>

           <isHidden>false</isHidden>

           <isRequired>true</isRequired>

           <embeddedServiceCustomLabels>

   <customLabel>EM_PreChat_Base_PrechatCustomFieldLabel_133xx0000004GG2_5523058</customLabel>

             <labelKey>EM_PreChat_Base_PrechatCustomFieldLabel</labelKey>

             <feature>EmbeddedMessaging</feature>

           </embeddedServiceCustomLabels>

```


### Metadata Types EmbeddedServiceFieldService

```
        </embeddedServiceFormFields>

        <embeddedServiceFormFields>

           <displayOrder>2</displayOrder>

           <formField>FavoriteFood_name</formField>

           <messagingChannelParameterType>Custom</messagingChannelParameterType>

           <formFieldType>ChoiceList</formFieldType>

           <isHidden>false</isHidden>

           <isRequired>true</isRequired>

           <choiceList>Food</choiceList>

        </embeddedServiceFormFields>

      </embeddedServiceForms>

   </EmbeddedServiceConfig>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EmbeddedServiceFieldService

Represents a setup node for creating an embedded Appointment Management deployment. This type extends the Metadata metadata
type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### EmbeddedServiceFieldService components are stored in a developer_name .EmbeddedServiceFieldService file in the EmbeddedServiceFieldService folder.

Version

### EmbeddedServiceFieldService is available in API version 43.0 and later.

Fields

**Field Name** **Field Type** **Description**

`appointmentBookingFlowName` string Name of the appointment booking flow for this embedded Appointment
Management (beta) deployment.

`cancelApptBookingFlowName` string Name of the appointment cancellation flow for this embedded
Appointment Management (beta) deployment.

`embeddedServiceConfig` string Required. The name of the Embedded Service configuration node.

`enabled` boolean Required. Indicates whether this embedded Appointment Management
deployment is enabled ( `true` ).


Metadata Types EmbeddedServiceFieldService

**Field Name** **Field Type** **Description**

`fieldServiceConfirmCardImg` string URL of the image used for the confirmation card in embedded
Appointment Management (beta).

`fieldServiceHomeImg` string URL of the image used for the home screen in embedded Appointment
Management (beta).

`fieldServiceLogoImg` string URL of the logo used for the home screen in embedded Appointment
Management (beta).

`masterLabel` string Required. Name of the embedded Appointment Management (beta)
deployment.

`modifyApptBookingFlowName` string Name of the appointment modification flow for this embedded
Appointment Management (beta) deployment.

`shouldShowExistingAppointment` boolean

`shouldShowNewAppointment` boolean

Specifies whether to display a button on the home screen for customers
to access their existing appointments ( `true` ) or not ( `false` ). This field
is `false` by default.

Specifies whether to display a button on the home screen for customers
to create a new appointment ( `true` ) or not ( `false` ). This field is
`false` by default.

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceFieldService file.

```
<?xml version="1.0" encoding="UTF-8"?>

<EmbeddedServiceFieldService xmlns="http://soap.sforce.com/2006/04/metadata">

   <appointmentBookingFlowName>ESW_FS_BookAppt_Main_Flow</appointmentBookingFlowName>

   <cancelApptBookingFlowName>ESW_FS_CancelAppt_Flow</cancelApptBookingFlowName>

   <embeddedServiceConfig>EswFS</embeddedServiceConfig>

   <enabled>true</enabled>

<fieldServiceConfirmCardImg>https://google.com/AppointmentConfirmationImg.png</fieldServiceConfirmCardImg>

   <fieldServiceHomeImg>https://google.com/HeroImg.png</fieldServiceHomeImg>

   <fieldServiceLogoImg>https://google.com/logo.png</fieldServiceLogoImg>

<masterLabel>EmbeddedServiceFieldService_Parent04IRM000000007p2AA_162d4270834</masterLabel>

   <modifyApptBookingFlowName>ESW_FS_ModifyAppt_Main_Flow</modifyApptBookingFlowName>

   <shouldShowExistingAppointment>true</shouldShowExistingAppointment>

   <shouldShowNewAppointment>true</shouldShowNewAppointment>

</EmbeddedServiceFieldService>

```

Usage

Note: Any changes you make to the image fields override what you’ve entered in Setup. We recommend setting your image
URLs in Setup.


### Metadata Types EmbeddedServiceFlowConfig EmbeddedServiceFlowConfig

Represents a setup node for creating an embedded flow. This type extends the Metadata metadata type and inherits its `fullName`
field.

File Suffix and Directory Location

### EmbeddedServiceFlowConfig components are stored in the developer_name .EmbeddedServiceFlowConfig file in the EmbeddedServiceFlowConfig folder.

Version

### EmbeddedServiceFlowConfig is available in API version 45.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enabled` boolean Indicates whether the embedded flow is enabled ( `true` ) or not
( `false` ). Defaults to `false` .

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceFlowConfig file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EmbeddedServiceFlowConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <enabled>true</enabled>

   </EmbeddedServiceFlowConfig>

### EmbeddedServiceLiveAgent

```

Represents a setup node for creating an embedded chat deployment. This type extends the Metadata metadata type and inherits its
`fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### EmbeddedServiceLiveAgent components are stored in the developer_name .EmbeddedServiceLiveAgent file in the EmbeddedServiceLiveAgent folder.

Version

### EmbeddedServiceLiveAgent is available in API version 38.0 and later.


Metadata Types EmbeddedServiceLiveAgent

Fields

**Field Name** **Field Type** **Description**

`avatarImg` string Avatar image for this embedded chat deployment.

`customPrechatComponent` string The custom Lightning Component that’s used for the pre-chat page in
this embedded chat deployment.

`embeddedServiceConfig` string Required. The name of the embedded service configuration node.

`embeddedServiceQuickActions` EmbeddedServiceQuickAction The quick action used by the pre-chat form.

`enabled` boolean Required. Indicates whether this embedded chat deployment is enabled
( `true` ).

```
fontSize

```

EmbeddedServiceFontSize Required. The font size for the text in the embedded chat window. One
(enumeration of of the following values:
type string)

**•** `Small`

**•** `Medium`

**•** `Large`

`headerBackgroundImg` string Header background image for this embedded chat window. Removed
in API version 49.0.

`isOfflineCaseEnabled` boolean Indicates whether offline support is enabled for this embedded chat
deployment. Available in API version 43.0 and later.

`isQueuePositionEnabled` boolean

Indicates whether queue position (displaying the chat visitor’s place in
line while they wait for an agent) is enabled for this embedded chat
deployment. Available in API version 43.0 and later.

`liveAgentChatUrl` string The rest endpoint for chats.

`liveAgentContentUrl` string The rest endpoint for cChat content.

`liveChatButton` string Required. Reference to a chat button created in Chat setup.

`liveChatDeployment` string Required. Reference to a deployment created in Chat setup.

`masterLabel` string Required. Name of the embedded chat deployment.

`offlineCaseBackgroundImg` string Offline support case form background image for this embedded chat
window. Available in API version 43.0 and later.

`prechatBackgroundImg` string Pre-chat background image for this embedded chat window.

`prechatEnabled` string Required. Indicates whether the embedded chat pre-chat form is enabled
for this deployment.

`prechatJson` string JSON object of all the fields of the selected pre-chat form in Chat setup.

```
scenario

```

EmbeddedServiceScenario Required. The scenario for the embedded chat window that determines
(enumeration of which objects to relate to the chat. One of the following values:
type string)

**•** `Sales`


Metadata Types EmbeddedServiceLiveAgent

**Field Name** **Field Type** **Description**

**•** `Service`

**•** `Basic`

`smallCompanyLogoImg` string Company logo image for this embedded chat window.

`waitingStateBackgroundImg` string Chat waiting image for this embedded chat window.

EmbeddedServiceQuickAction

Returns a quick action that’s associated with an EmbeddedServiceLiveAgent setup. The quick action includes the pre-chat form fields
that the embedded chat window displays and shows the order in which the fields are displayed.

**Field Name** **Field Type** **Description**

`embeddedServiceLiveAgent` string Reference to the embedded chat deployment.

`order` int Order in which this quick action appears in the embedded chat pre-chat form.

`quickActionDefinition` string Reference to a quick action.

```
quickActionType

```

EmbeddedServiceQuickActionType Quick action type. One of the following values:
(enumeration of type

**•** `Prechat` –Pre-chat

string)

**•** `Prechat` –Pre-chat

**•** `OfflineCase` –Offline support (Cases)

Available in API version 43.0 and later.

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceLiveAgent file.

```
<?xml version="1.0" encoding="UTF-8"?>

<EmbeddedServiceLiveAgent xmlns="http://soap.sforce.com/2006/04/metadata">

   <avatarImg>https://google.com/avatar.png</avatarImg>

   <customPrechatComponent>auraCustomPrechat</customPrechatComponent>

   <embeddedServiceConfig>EswConfig001</embeddedServiceConfig>

   <embeddedServiceQuickActions>

<embeddedServiceLiveAgent>EmbeddedServiceLiveAgent_Parent04Ixx0000000001EAA_15ec5bd2971</embeddedServiceLiveAgent>

     <order>1</order>

<quickActionDefinition>Snapins_Contact_QuickAction_08hRM000000001h</quickActionDefinition>

   </embeddedServiceQuickActions>

   <embeddedServiceQuickActions>

<embeddedServiceLiveAgent>EmbeddedServiceLiveAgent_Parent04Ixx0000000001EAA_15ec5bd2971</embeddedServiceLiveAgent>

     <order>1</order>

```


Metadata Types EmbeddedServiceLiveAgent

```
   <quickActionDefinition>Snapins_Case_OfflineCaseQuickAction_08hRM000000001h</quickActionDefinition>

        <quickActionType>OfflineCase</quickActionType>

      </embeddedServiceQuickActions>

      <embeddedServiceQuickActions>

   <embeddedServiceLiveAgent>EmbeddedServiceLiveAgent_Parent04Ixx0000000001EAA_15ec5bd2971</embeddedServiceLiveAgent>

        <order>2</order>

   <quickActionDefinition>Snapins_Case_QuickAction_08hRM000000001h</quickActionDefinition>

      </embeddedServiceQuickActions>

      <enabled>true</enabled>

      <fontSize>Medium</fontSize>

      <headerBackgroundImg>https://google.com/headerBackgroundImg.png</headerBackgroundIm>

      <isOfflineCaseEnabled>true</isOfflineCaseEnabled>

      <isQueuePositionEnabled>true</isQueuePositionEnabled>

      <liveChatButton>chatButton01</liveChatButton>

      <liveChatDeployment>liveAgentDeployment01</liveChatDeployment>

     <masterLabel>EmbeddedServiceLiveAgent_Parent04Ixx0000000001EAA_15ec5bd2971</masterLabel>

   <offlineCaseBackgroundImg>https://google.com/offlineCaseBackgroundImg.png</offlineCaseBackgroundImg>

     <prechatBackgroundImg>https://google.com/prechatBackgroundImg.png</prechatBackgroundImg>

      <prechatEnabled>true</prechatEnabled>

      <scenario>Service</scenario>

      <smallCompanyLogoImg>https://google.com/smallCompanyLogoImg.png</smallCompanyLogoImg>

   <waitingStateBackgroundImg>https://google.com/waitingImage.png</waitingStateBackgroundImg>

   </EmbeddedServiceLiveAgent>

```

Usage

EmbeddedServiceLiveAgent represents a Chat configuration that is added to your web page. The EmbeddedServiceLiveAgent record
contains a unique combination of a chat button and the Chat deployment that the administrator selects during setup.

To create an EmbeddedServiceLiveAgent record:

**1.** Create a Chat Deployment record.

**2.** Create a Chat Button record.

**3.** Create an EmbeddedServiceConfig record.

**4.** Set the fields for the Chat Deployment record, Chat Button record, and EmbeddedServiceConfig record as references on the
EmbeddedServiceLiveAgent record.

Any changes you make to the image fields override what you’ve entered in Setup. We recommend setting your image URLs in Setup.


### Metadata Types EmbeddedServiceMenuSettings

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EmbeddedServiceMenuSettings

Represents a setup node for creating a channel menu deployment. Channel menus list the ways in which customers can contact your
business. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### EmbeddedServiceMenuSettings components are stored in the developer_name.EmbeddedServiceMenuSettings folder.

Version

### EmbeddedServiceMenuSettings components are available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`branding` string The developer name of the associated BrandingSet.

`embeddedServiceCustomLabels` EmbeddedServiceCustomLabel[]

Represents a customized label that appears in the
embedded component for a particular channel menu
deployment.

`embeddedServiceCustomizations` EmbeddedServiceCustomization The customizations used in this Embedded Service
on page 1021[] deployment. Each customization is associated with

a static resource. Available in API version 50.0 and
later.

`embeddedServiceMenuItems` EmbeddedServiceMenuItem[] Represents a channel menu item that lists a way in
which customers can contact your business.

`isEnabled` boolean If `true` (default), the deployment is enabled. If
`false`, the deployment is disabled.

`masterLabel` string Required. The name of the channel menu
deployment.

`site` string Required. The name of the Experience site or website
connected to this channel menu deployment.


Metadata Types EmbeddedServiceMenuSettings

EmbeddedServiceCustomLabel

Represents the custom labels used in your channel menu deployment.

**Field Name** **Field Type** **Description**

`customLabel` string The customized label that appears in the channel menu.

`feature` EmbeddedServiceFeature The feature using the custom label. For channel menu
(enumeration of type string) deployments, the value is `ChannelMenu` .

`labelKey` EmbeddedServiceLabelKey
(enumeration of type string)

EmbeddedServiceCustomization

The type of label for this embedded component. The value
corresponds to the label within a label group (substate of chat
state or page type).

Returns the customization associated with the Embedded Service feature. Available in API version 50.0 and later.

EmbeddedServiceResource

Returns the static resource associated with the Embedded Service Chat feature customization. Available in API version 50.0 and later.


Metadata Types EmbeddedServiceMenuSettings

EmbeddedServiceMenuItem

Represents an item in a channel menu.

**Field Name** **Field Type** **Description**

`channel` string The ID of the channel type. If `channelType` is
`Phone` or `CustomURL`, this field is `null` .

`channelType` EmbeddedServiceChannelType The type of communication channel. Values are:
(enumeration of type string)

**•** `EmbeddedMessaging`

**•** `EmbeddedServiceConfig`

**•** `MessagingChannel`

**•** `Phone`

**•** `CustomURL`

`customUrl` string

A custom URL that appears in the menu. The
`shouldOpenUrlInSameTab` field determines
where the URL opens.

`displayOrder` int The item’s order in the menu, such as 1 or 2.

`embeddedServiceCustomLabels` EmbeddedServiceCustomLabel[] Represents the custom labels used in your channel
menu item.

`iconUrl` string

The icon URL for the menu item. Icons can be used
only for phone, SMS, custom URL, and chat menu
items.

`isDisplayedOnPageLoad` boolean If `true`, the menu item is displayed on page load.
Available in API version 49.0 and later.

`itemName` string A unique custom name for the menu item, which is
visible in the user interface.

`osOptionsHideInIOS` boolean If `true`, the menu item is hidden in iOS.

`osOptionsHideInLinuxOS` boolean If `true`, the menu item is hidden in Linux operating
system.

`osOptionsHideInMacOS` boolean If `true`, the menu item is hidden in Mac operating
system.

`osOptionsHideInOtherOS` boolean If `true`, the menu item is hidden in any operating
system other than iOS, Linux, Mac, and Windows.

`osOptionsHideInWindowsOS` boolean If `true`, the menu item is hidden in Windows
operating system.

`phoneNumber` string The phone number for menu items whose
`channelType` is `Phone` .


Metadata Types EmbeddedServiceMenuSettings

**Field Name** **Field Type** **Description**

`shouldOpenUrlInSameTab` boolean

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceMenuSettings component.

If the menu item’s `channelType` is `CustomURL`,
this field indicates whether the link opens in the same
tab ( `true` ) or a new tab ( `false` ).

```
<?xml version="1.0" encoding="UTF-8"?>

<EmbeddedServiceMenuSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <embeddedServiceCustomLabels>

<customLabel>CM_Container_Header_Primary_Greeting_3MsRM0000004CB5_6181150</customLabel>

     <labelKey>CM_Container_Header_Primary_Greeting</labelKey>

   </embeddedServiceCustomLabels>

   <embeddedServiceCustomLabels>

<customLabel>CM_Container_Header_Secondary_Greeting_3MsRM0000004CB5_4637097</customLabel>

     <labelKey>CM_Container_Header_Secondary_Greeting</labelKey>

   </embeddedServiceCustomLabels>

   <embeddedServiceMenuItems>

     <channel>Chat</channel>

     <channelType>EmbeddedServiceConfig</channelType>

     <displayOrder>1</displayOrder>

     <embeddedServiceCustomLabels>

<customLabel>CM_Container_MenuItems_WebChatUnavailable_3miRM0000004CuZ_8003848</customLabel>

        <labelKey>CM_Container_MenuItems_WebChatUnavailable</labelKey>

     </embeddedServiceCustomLabels>

     <embeddedServiceCustomLabels>

<customLabel>CM_Container_MenuItems_WebChatAvailable_3miRM0000004CuZ_5823055</customLabel>

        <labelKey>CM_Container_MenuItems_WebChatAvailable</labelKey>

     </embeddedServiceCustomLabels>

     <itemName>Chat1</itemName>

     <osOptionsHideInIOS>false</osOptionsHideInIOS>

     <osOptionsHideInLinuxOS>true</osOptionsHideInLinuxOS>

     <osOptionsHideInMacOS>false</osOptionsHideInMacOS>

     <osOptionsHideInOtherOS>false</osOptionsHideInOtherOS>

     <osOptionsHideInWindowsOS>true</osOptionsHideInWindowsOS>

     <shouldOpenUrlInSameTab>false</shouldOpenUrlInSameTab>

   </embeddedServiceMenuItems>

   <embeddedServiceMenuItems>

     <channelType>Phone</channelType>

     <displayOrder>2</displayOrder>

     <itemName>Phone1</itemName>

     <osOptionsHideInIOS>true</osOptionsHideInIOS>

     <osOptionsHideInLinuxOS>false</osOptionsHideInLinuxOS>

```


### Metadata Types EnablementMeasureDefinition

```
        <osOptionsHideInMacOS>true</osOptionsHideInMacOS>

        <osOptionsHideInOtherOS>false</osOptionsHideInOtherOS>

        <osOptionsHideInWindowsOS>false</osOptionsHideInWindowsOS>

        <phoneNumber>1234567890</phoneNumber>

        <shouldOpenUrlInSameTab>false</shouldOpenUrlInSameTab>

      </embeddedServiceMenuItems>

      <embeddedServiceMenuItems>

        <channelType>CustomURL</channelType>

        <customUrl>https://google.com</customUrl>

        <displayOrder>3</displayOrder>

        <itemName>url1</itemName>

        <osOptionsHideInIOS>false</osOptionsHideInIOS>

        <osOptionsHideInLinuxOS>false</osOptionsHideInLinuxOS>

        <osOptionsHideInMacOS>false</osOptionsHideInMacOS>

        <osOptionsHideInOtherOS>false</osOptionsHideInOtherOS>

        <osOptionsHideInWindowsOS>false</osOptionsHideInWindowsOS>

        <shouldOpenUrlInSameTab>false</shouldOpenUrlInSameTab>

      </embeddedServiceMenuItems>

      <isEnabled>true</isEnabled>

      <masterLabel>ChannelMenuSettings</masterLabel>

      <site>SnapInCommunity</site>

   </EmbeddedServiceMenuSettings>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EnablementMeasureDefinition

Represents an Enablement measure, which specifies the job-related activity that a user performs to complete a milestone or outcome
in an Enablement program. A measure identifies a source object and optional related objects, with optional field filters and filter logic,
for tracking the activity. To avoid deployment errors, deploy measures before you deploy programs.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### EnablementMeasureDefinition components have the suffix .enablementMeasureDefinition and are stored in the

`enablementMeasureDefinitions` folder.

Version

### EnablementMeasureDefinition components are available in API version 61.0 and later.


Metadata Types EnablementMeasureDefinition

Special Access Rules

To access Enablement measures, the Design and Deliver Enablement Programs permission is required. This permission is available with
the Enablement add-on license.

Fields

**Field Name** **Description**

```
description

developerName

masterLabel

sourceMeasureObject

status

```

**Field Type**
string

**Description**
An internal description for the measure to help Enablement admins understand the
activity that’s tracked.

**Field Type**
string

**Description**

Required. The unique programmatic name for the measure record.

**Field Type**
string

**Description**

Required. A user-friendly name for the measure, which is defined when the measure
is created.

**Field Type**

EnablementMeasureSourceObjectDefinition

**Description**

Required. The source object that tracks the activity you're measuring.

**Field Type**
EnblProgramMeasureStatus (enumeration of type string)

**Description**

Required. Indicates whether the measure is published for use in Enablement programs.

Values are:

**•** `Draft` —The measure is saved, but not activated for use in programs.

**•** `Published` —The measure is activated for use in programs. In Lightning
Experience, this value is Active.


Metadata Types EnablementMeasureDefinition

EnablementMeasureSourceObjectDefinition

Defines the source object, fields, field values, and calculation method for the job-related activity you’re measuring.

**Field Name** **Description**

```
aggregateFieldApiName

aggregateFunction

dateFieldApiName

displayFieldApiName

```

**Field Type**
string

**Description**
The unique programmatic name for the field that the `aggregateFunction` uses
for calculating.

For example, if you’re measuring how much revenue a sales rep has won, the value
of `aggregateFunction` is `Sum` and the value of `aggregateFieldApiName`
is `Amount`, which is the programmatic name of the Amount field on the Opportunity
object.

**Field Type**
EnablementAggregationType (enumeration of type string)

**Description**

Required. The method for calculating progress towards the milestone or outcome
from records that qualify for the measure’s criteria.

Values are:

**•** `Average`

**•** `Count`

**•** `Sum`

For example, if you’re measuring the number of deals won, the function is `Count` .

If the function is `Average` or `Sum`, `aggregateFieldApiName` is required.

**Field Type**
string

**Description**

Required. The unique programmatic name for the field that defines when users get
credit for the activity you’re measuring. For example, if you’re measuring the number
of deals won, this value can be `ClosedDate`, the programmatic name of the Close
Date field on the Opportunity object.

**Field Type**
string

**Description**

Required. The unique programmatic name for the field that primarily identifies records
that qualify for the activity you’re measuring. For example, if you’re measuring the
number of deals won, you’re tracking the Opportunity object, and maybe you want
to identify opportunities by their name. In this case, this field can be `Name`, the
programmatic name of the Opportunity Name field on the Opportunity object.


Metadata Types EnablementMeasureDefinition

**Field Name** **Description**

```
filterLogic

filters

objectApiName

relatedMeasureObjects

userFieldApiName

```

**Field Type**
string

**Description**
An expression that determines how to evaluate the optional field filters for the object.

**Field Type**

EnablementMeasureFilterDefinition[]

**Description**
The fields on the object and corresponding field values that further specify criteria for
the activity you’re measuring.

**Field Type**
string

**Description**

Required. The unique programmatic name for the source object that tracks the activity
you’re measuring. For example, if you’re measuring the number of deals won, this
value is `Opportunity`, the programmatic name of the Opportunity object.

**Field Type**

EnablementMeasureRelatedObjectDefinition[]

**Description**
The optional related objects that further specify criteria for the activity you’re measuring.
Related objects can also specify additional filters.

**Field Type**
string

**Description**

Required. The unique programmatic name for the field that defines who gets credit
for the activity you’re measuring. For example, if you’re measuring the number of deals
won by a sales rep, this value can be `OwnerId`, the developer name of the
Opportunity Owner field on the Opportunity object.

EnablementMeasureFilterDefinition

Represents the fields on the source object or related objects and the corresponding field values that further specify criteria for the activity
you’re measuring.

**Field Name** **Description**

```
fieldApiName

```

**Field Type**
string


Metadata Types EnablementMeasureDefinition

**Field Name** **Description**

**Description**

Required. The unique programmatic name for the field that you’re filtering by. For
example, if you’re tracking activity on the Opportunity object and want to filter by the
Stage field, this value can be `StageName` .

```
fieldValue

operator

sequenceNumber

```

**Field Type**
string

**Description**

Required. The field value to filter by. For example, if you’re tracking activity on the
Opportunity object and want to filter by the Stage field, this value can be `Closed`

```
  Won.

```

**Field Type**
EnablementFilterOperator (enumeration of type string)

**Description**

Required. The logic for evaluating the specified field and field value.

Values are:

**•** `Contains`

**•** `DoesNotContain`

**•** `DoesNotEqual`

**•** `EndsWith`

**•** `Equals`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `In`

**•** `IsNull`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `NotIn`

**•** `StartsWith`

**Field Type**
int

**Description**

Required. A number that specifies the order of the filter, relative to other filters, starting
at 1.


Metadata Types EnablementMeasureDefinition

EnablementMeasureRelatedObjectDefinition

Represents objects related to the source object. Related objects can further specify criteria for the activity you’re measuring. Related
objects can also have additional filters. For example, maybe you’re measuring deals won for a specific product line. In this case, the source
object is Opportunity, the related object is Opportunity Product, and the related object can have a filter for the specific product name.

**Field Name** **Description**

```
filterLogic

filters

idFieldApiName

objectApiName

```

**Field Type**
string

**Description**
An expression that determines how to evaluate the optional field filters for the object.

**Field Type**

EnablementMeasureFilterDefinition[]

**Description**
The fields on the related object and the corresponding field values that further specify
criteria for the activity you’re measuring.

**Field Type**
string

**Description**

Required. The programmatic name of the field that links the related object to the
primary object. For example, if the primary object is Opportunity and the related object
is Opportunity Product, this value is `OpportunityId`, the developer name of the
Opportunity field on the Opportunity Product object.

**Field Type**
string

**Description**

Required. The unique programmatic name for the related object. For example, if the
related object is Opportunity Product, this value is `OpportunityLineItem` .

Declarative Metadata Sample Definition

The following is an example of an EnablementMeasureDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<EnablementMeasureDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Total amount in pipeline measure</description>

   <developerName>TotalAmountInPipeline</developerName>

   <masterLabel>Total Amount in Pipeline</masterLabel>

   <status>Draft</status>

   <sourceMeasureObject>

     <aggregateFieldApiName>Amount</aggregateFieldApiName>

     <aggregateFunction>Sum</aggregateFunction>

```


### Metadata Types EnablementProgramDefinition

```
        <dateFieldApiName>CreatedDate</dateFieldApiName>

        <displayFieldApiName>Name</displayFieldApiName>

        <objectApiName>Opportunity</objectApiName>

        <userFieldApiName>OwnerId</userFieldApiName>

        <filters>

           <fieldApiName>StageName</fieldApiName>

           <fieldValue>Closed Won</fieldValue>

           <operator>Equals</operator>

           <sequenceNumber>1</sequenceNumber>

        </filters>

        <relatedMeasureObjects>

           <objectApiName>OpportunityLineItem</objectApiName>

           <idFieldApiName>OpportunityId</idFieldApiName>

           <filterLogic>1 OR 2</filterLogic>

           <filters>

             <fieldApiName>UnitPrice</fieldApiName>

             <fieldValue>10000</fieldValue>

             <operator>GreaterThan</operator>

             <sequenceNumber>1</sequenceNumber>

           </filters>

           <filters>

             <fieldApiName>TotalPrice</fieldApiName>

             <fieldValue>10000</fieldValue>

             <operator>GreaterThan</operator>

             <sequenceNumber>2</sequenceNumber>

           </filters>

        </relatedMeasureObjects>

      </sourceMeasureObject>

   </EnablementMeasureDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>TotalAmountInPipeline</members>

        <name>EnablementMeasureDefinition</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EnablementProgramDefinition

Represents an Enablement program, which includes exercises and measurable milestones to help users such as sales reps achieve specific
outcomes related to your company’s revenue goals.


Metadata Types EnablementProgramDefinition

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

EnablementProgramDefinition components have the suffix `.enablementProgramDefinition` and are stored in the
`enablementProgramDefinitions` folder.

Version

EnablementProgramDefinition components are available in API version 61.0 and later.

Special Access Rules

To access Enablement programs, the Design and Deliver Enablement Programs permission is required. This permission is available with
the Enablement add-on license.

[For partner programs in supported Experience Cloud sites, a supported Partner Relationship Management (PRM) add-on license is also](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)
required.

Fields

**Field Name** **Description**

```
description

developerName

doesAllowSelfEnrollment

```

**Field Type**
string

**Description**

Required. A summary of the program’s goals and content that’s visible to users.

**Field Type**
string

**Description**

Required. The unique programmatic name for the program record.

**Field Type**
boolean

**Description**
Indicates whether users can self-enroll in programs that are shared with them ( `true` )
or take only assigned programs ( `false` ). The default value is `false` .


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

```
masterLabel

name

network

sections

tasks

type

```

**Field Type**
string

**Description**

Required. A user-friendly name for the program, which is defined when the program
is created.

**Field Type**
string

**Description**

Required. The name of the program that’s visible to users.

**Field Type**
string

**Description**
The Experience Cloud site where a program is published for partner users.

**Field Type**

EnablementProgramSection[]

**Description**
Groups of milestones and exercises within a program.

**Field Type**

EnablementProgramTask[]

**Description**
The outcome, milestones, and exercises in the program.

**Field Type**
string

**Description**

Required. Indicates whether the program is for sales users in Lightning Experience
( `Enablement` ) or partner users in supported Experience Cloud sites
( `PtnrEnablement` ).

EnablementProgramSection

Represents a logical, trackable group of milestones and exercises within an Enablement program. When users take programs, they can
expand or collapse sections.


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

```
developerName

name

sequenceNumber

tasks

```

**Field Type**
string

**Description**

Required. The unique programmatic name for the section.

**Field Type**
string

**Description**
Required. The title of the section that’s visible to users when they take the program.

**Field Type**
int

**Description**

Required. A number that specifies the order of the section, relative to other sections,
starting at 0.

**Field Type**

EnablementProgramTask[]

**Description**
The milestones and exercises in the section.

EnablementProgramTask

Represents an outcome, milestone, or exercise in an Enablement program. A program task is also known as a program item.

**Field Name** **Description**

```
customSubCategoryName

day

```

**Field Type**
string

**Description**

The API name of custom exercise task subcategory. This value determines the type of
the custom exercise and its associated content. Available in API version 63.0 and later.

**Field Type**
int

**Description**

Required. The day of the program when the item is due, relative to the program's start
date. For example, if a user is expected to complete an exercise where they watch a
product demo by day 2, this field’s value is 2. For an outcome, this field specifies the
number of days the full program takes. For example, if your program lasts 60 days, the


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

value of this field is 60 for the outcome. This field’s value contributes to the program’s
due date that users see when they take the program.

```
description

developerName

exercise

milestone

name

sequenceNumber

```

**Field Type**
string

**Description**

Required. A summary of the outcome, milestone, or exercise that’s visible to users
when they take the program.

**Field Type**
string

**Description**

Required. The unique programmatic name for the outcome, milestone, or exercise.

**Field Type**

EnablementProgramTaskExercise

**Description**
The content used with an exercise.

If `taskSubCategory` is `ActionItem`, this field isn’t included when retrieving
metadata.

**Field Type**

EnablementProgramTaskMilestone

**Description**
The definition of an outcome or milestone, including the Enablement measures used
and the criteria for completing the goal.

**Field Type**
string

**Description**

Required. The title of the outcome, milestone, or exercise that’s visible to users when
they take the program.

**Field Type**
int

**Description**

Required. A number that specifies the order of the milestone or exercise, relative to
other milestones or exercises that have the same due date in the program or in the
same section, starting at 0. This number determines the order of items that users see
for that day in the program.


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

```
taskCategory

taskSubCategory

```

**Field Type**
ProgramTaskDefCategory (enumeration of type string)

**Description**

Required. The type of the program item.

Values are:

**•** `Exercise`

**•** `Milestone`

`Milestone` is used for both the program’s outcome and incremental milestones.

**Field Type**
string

**Description**

Required. The type of exercise. This value determines the content associated with the
exercise. For example, if the field value is `Video`, the exercise must reference video
content from the Enablement workspace in the Digital Experiences app. Possible values
are:

**•** `ActionItem`

**•** `AudioRecording`

**•** `CustomExercise` —Available in API version 62.0 and later.

**•** `Document`

**•** `FeedbackRequest`

**•** `Other`

**•** `OtherExercise`

**•** `ScheduledEvent`

**•** `TextLesson`

**•** `Trailhead`

**•** `Video`

When `taskCategory` is `Milestone`, the value of `taskSubCategory` must
be `Other` .

EnablementProgramTaskExercise

Represents the content used with an exercise in an Enablement program.

**Field Name** **Description**

```
cmsContent

```

**Field Type**

EnablementProgramTaskCmsContent


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

**Description**

The definition of content managed in the Enablement workspace in the Digital
Experiences app when `taskSubCategory` on EnablementProgramTask is
`AudioRecording`, `Document`, `OtherExercise`, `ScheduledEvent`,
`TextLesson`, or `Video` .

```
customContent

externalContent

feedbackContent

```

**Field Type**

EnablementProgramTaskCustomContent

**Description**

The definition of content used with a custom exercise type when
`taskSubCategory` on EnablementProgramTask is `CustomExercise` .

**Field Type**

EnablementProgramTaskExternalContent

**Description**
The definition of Trailhead content when `taskSubCategory` on
EnablementProgramTask is `Trailhead` .

**Field Type**

EnablementProgramTaskFeedbackContent

**Description**
The definition of an assessment survey or Einstein prompt template when
`taskSubCategory` on EnablementProgramTask is `FeedbackRequest` .

EnablementProgramTaskCmsContent

Defines content managed in the Enablement workspace in the Digital Experiences app for the Audio Recording, Document, Other,
Scheduled Event, Text Lesson, or Video exercise types.

**Field Name** **Description**

```
apiName

```

**Field Type**
string

**Description**

Required in API version 62.0. The unique programmatic ID of the Digital Experiences
content for the exercise. This string’s format is
_**`workspaceType`**_ `/` _**`workspaceApiName`**_ `.` _**`contentFQN`**_ `/` _**`contentApiName`**_,
which matches the `fullName` field value on the corresponding DigitalExperience
metadata type.

For example, a Link content record from the Enablement workspace has this API name:
`enablement/sfdcEnablement_EnablementWorkspace.sfdc_enablement__link/link_API_name` .


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

```
contentKey

```

**Field Type**
string

**Description**

Required in API version 61.0 only.

EnablementProgramTaskCustomContent

Defines content used with a custom exercise type.

**Field Name** **Description**

```
content

```

**Field Type**
string

**Description**

A serialized string returned by the Apex class that’s specified in the corresponding
LearningItemType metadata type’s `apexSerializerDeserializer` field. This
string identifies the content used with the custom exercise type so the custom exercise
can be recreated in the destination org. This string:

**•** Can’t exceed 250 characters

**•** Must contain only alphanumeric characters

[For details, see Implement Custom Exercise Types for Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
_Sales Programs and Partner Tracks with Enablement Developer Guide_ .

EnablementProgramTaskExternalContent

Defines Trailhead content for the Trailhead exercise type.

**Field Name** **Description**

```
externalId

providerType

```

**Field Type**
string

**Description**

Required. The API name of the Trailhead module used with the exercise.

**Field Type**
ProgramExtContentDefProvider (enumeration of type string)

**Description**

Required. The supported external content platform or system.

Values are:

**•** `Trailhead`


Metadata Types EnablementProgramDefinition

EnablementProgramTaskFeedbackContent

Defines the assessment survey or Einstein prompt template for the Feedback Request exercise type.

**Field Name** **Description**

```
inviteeCount

promptTemplate

surveyDeveloperName

type

```

**Field Type**
int

**Description**
The number of peers or managers that the user is required to invite for giving feedback
when `type` is `PeerFeedback` . Each peer or manager receives an invitation to the
assessment survey associated with the Feedback Request exercise.

When `type` is `AIFeedback`, this value is always `1` .

**Field Type**
string

**Description**
The prompt template to use with this exercise when `type` is `AIFeedback` .

**Field Type**
string

**Description**
The unique programmatic name for the assessment survey that’s sent to peers and
managers when `type` is `PeerFeedback` .

**Field Type**
string

**Description**

Required. The type of feedback used with the exercise.

Values are:

**•** `AIFeedback` —Users submit a video call, and Einstein generates feedback from
the call’s transcription. With this type, `promptTemplate` is required.

**•** `PeerFeedback` —Users submit a URL to a sample of their work, and select
peers and managers to review their work. Selected peers and managers complete
an assessment survey. With this type, `surveyId` is required.

EnablementProgramTaskMilestone

Defines the requirements for an outcome or milestone, including the Enablement measures used for tracking activity and the criteria
for completing the outcome or milestone.


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

```
compositeMilestoneType

isMilestoneAnOutcome

milestoneMeasures

milestoneTarget

minimumSampleSize

```

**Field Type**
EnblCompositeMilestoneType (enumeration of type string)

**Description**
The type of logic to use for evaluating the activity from two Enablement measures in
a composite milestone.

Values are:

**•** `Addition`

**•** `Division`

**•** `Percentage`

**Field Type**
boolean

**Description**

Required. Indicates whether the program item is the program’s outcome ( `true` ) or
an incremental milestone ( `false` ).

**Field Type**

EnablementProgramTaskMilestoneMeasure[]

**Description**
The Enablement measures used with the outcome or milestone.

**Field Type**
double

**Description**
The target value for a user to achieve to get credit for completing the outcome or
milestone. The unit depends on the specific measure used with the outcome or
milestone. For example, if the measure is the dollar amount of all closed opportunities,
then the field value is measured in dollars.

**Field Type**
int

**Description**
The number of records to evaluate when calculating progress for an outcome or
milestone that uses an average-based measure. Use this field with
`milestoneTarget` . For example, if you want users to achieve an average deal
size of $50,000 after closing 4 deals, then this field’s value is `4` and
`milestoneTarget` is `50000` .

EnablementProgramTaskMilestoneMeasure

Defines the Enablement measure used with an outcome or milestone.


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

```
measureDefinitionDeveloperName

sequenceNumber

```

**Field Type**
string

**Description**
The unique programmatic name of the Enablement measure used with the outcome
or milestone.

**Field Type**
int

**Description**
A number that specifies the order of the Enablement measure when multiple measures
are used with one outcome or milestone, starting at 0. For example, in a composite
milestone that uses the Percentage function, the measure that provides the numerator
value is sequence 0 and the measure that provides the denominator value is sequence
1.

Declarative Metadata Sample Definition

The following is an example of an EnablementProgramDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<EnablementProgramDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Get started with sales at Cloud Kicks and close your first

deal!</description>

   <developerName>Get_Started_Close_First_Deal_Program</developerName>

   <doesAllowSelfEnrollment>false</doesAllowSelfEnrollment>

   <masterLabel>Welcome to Sales at Cloud Kicks</masterLabel>

   <name>Welcome to Sales at Cloud Kicks</name>

   <sections>

     <developerName>section_0</developerName>

     <name>Learn the Ropes in Your First Week</name>

     <sequenceNumber>0</sequenceNumber>

     <tasks>

        <day>1</day>

        <description>Learn the basics of sales at Cloud Kicks.</description>

        <developerName>task_0</developerName>

        <exercise>

          <externalContent>

            <externalId>sales-rep-training</externalId>

            <providerType>Trailhead</providerType>

          </externalContent>

        </exercise>

        <name>Sales Rep Training</name>

        <sequenceNumber>0</sequenceNumber>

        <taskCategory>Exercise</taskCategory>

        <taskSubCategory>Trailhead</taskSubCategory>

     </tasks>

     <tasks>

        <day>2</day>

```


Metadata Types EnablementProgramDefinition

```
           <description>Watch our CEO explain the company vision.</description>

           <developerName>task_1</developerName>

           <exercise>

             <cmsContent>

   <apiName>enablement/sfdcEnablement_EnablementWorkspace.sfdc_enablement__link/company_vision_video</apiName>

             </cmsContent>

           </exercise>

           <name>See Our Company Vision</name>

           <sequenceNumber>1</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>Video</taskSubCategory>

        </tasks>

        <tasks>

           <day>3</day>

           <description>Action Item</description>

           <developerName>task_2</developerName>

           <name>Action Item</name>

           <sequenceNumber>2</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>ActionItem</taskSubCategory>

        </tasks>

        <tasks>

           <day>4</day>

           <description>Try out your first sales patch at Cloud Kicks and get feedback

   from our in-house experts.</description>

           <developerName>task_3</developerName>

           <exercise>

             <feedbackContent>

             <inviteeCount>1</inviteeCount>

             <surveyDeveloperName>discovery_call_assessment</surveyDeveloperName>

           </feedbackContent>

           </exercise>

           <name>Feedback from Peers and Managers</name>

           <sequenceNumber>3</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>FeedbackRequest</taskSubCategory>

        </tasks>

        <tasks>

           <day>5</day>

           <description>Complete a discovery calls by day 5.</description>

           <developerName>task_4</developerName>

           <isMilestoneAnOutcome>false</isMilestoneAnOutcome>

           <milestone>

             <milestoneMeasures>

   <measureDefinitionDeveloperName>salesforceTemplate_CallsEmails</measureDefinitionDeveloperName>

             </milestoneMeasures>

             <milestoneTarget>1.0</milestoneTarget>

           </milestone>

           <name>Log a Discovery Call by Day 5</name>

           <sequenceNumber>4</sequenceNumber>

```


Metadata Types EnablementProgramDefinition

```
           <taskCategory>Milestone</taskCategory>

           <taskSubCategory>Other</taskSubCategory>

        </tasks>

        <tasks>

           <day>6</day>

           <description>Browse our sales leaders blog for more insights.</description>

           <developerName>task_5</developerName>

           <exercise>

             <cmsContent>

   <apiName>enablement/sfdcEnablement_EnablementWorkspace.sfdc_enablement__link/sales_blog</apiName>

             </cmsContent>

           </exercise>

           <name>Review Tips from Sales Leaders</name>

           <sequenceNumber>5</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>OtherExercise</taskSubCategory>

        </tasks>

        <tasks>

           <day>7</day>

          <description>Follow a screen flow for onboarding to the sales team.</description>

           <developerName>task_6</developerName>

           <exercise>

             <customContent>

               <content>flowDeveloperName=OnboardingFlow</content>

             </customContent>

           </exercise>

           <name>Onboarding Flow</name>

           <sequenceNumber>6</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>CustomExercise</taskSubCategory>

           <customSubCategoryName>ScreenFlowTaskSubCategory</customSubCategoryName>

        </tasks>

      </sections>

      <tasks>

        <day>30</day>

        <description>Close your first opportunity. To make sure it's counted, set the

   opportunity Stage field to Closed Won.</description>

        <developerName>task_enablementProgramOutcomeCard</developerName>

        <isMilestoneAnOutcome>true</isMilestoneAnOutcome>

        <milestone>

           <milestoneMeasures>

   <measureDefinitionDeveloperName>measure_CloseFirstDeal</measureDefinitionDeveloperName>

           </milestoneMeasures>

           <milestoneTarget>1.0</milestoneTarget>

        </milestone>

        <name>outcome</name>

        <sequenceNumber>0</sequenceNumber>

        <taskCategory>Milestone</taskCategory>

        <taskSubCategory>Other</taskSubCategory>

      </tasks>

```


### Metadata Types EnblProgramTaskSubCategory

```
      <type>Enablement</type>

   </EnablementProgramDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Get_Started_Close_First_Deal_Program</members>

        <name>EnablementProgramDefinition</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EnblProgramTaskSubCategory

Represents a custom exercise type that an Enablement admin adds to an Enablement program in Program Builder. A custom exercise
type also requires a corresponding EnblProgramTaskDefinition record for Program Builder and corresponding LearningItem and
LearningItemType records for when users take the exercise in the Guidance Center.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### EnblProgramTaskSubCategory components have the suffix .enblProgramTaskSubCategory and are stored in the

`enblProgramTaskSubCategories` folder.

Version

### EnblProgramTaskSubCategory components are available in API version 62.0 and later.

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.


Metadata Types EnblProgramTaskSubCategory

Important: Custom exercises aren’t compatible with Partner Enablement programs.

Fields

**Field Name** **Description**

```
developerName

icon

learningItemType

masterLabel

```

**Field Type**
string

**Description**

Required. The unique programmatic name for the EnblProgramTaskSubCategory
record.

**Field Type**
string

**Description**
Required. The icon to use for the custom exercise type in Program Builder.

Use the format _**`iconType`**_ `:` _**`iconName`**_, where the values correspond to icon
[categories and names from the Salesforce Lightning Design System.](https://www.lightningdesignsystem.com/icons/)

**•** _**`iconType`**_ is the type of icon, such as `standard` or `doctype` .

**•** _**`iconName`**_ is the icon name, such as `flow` or `slide` .

For example, to use the Standard type Flow icon, this value is `standard:flow` .
[For details, see Implement Custom Exercise Types for Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
_Sales Programs and Partner Tracks with Enablement Developer Guide_ .

**Field Type**
string

**Description**

[Required. The programmatic name of the LearningItemType record that represents](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_learningitemtype.htm)
this custom exercise type in the Guidance Center when users take a program.

**Field Type**
string

**Description**

Required. A user-friendly name for the EnblProgramTaskSubCategory, which is defined
when it’s created.

Declarative Metadata Sample Definition

The following is an example of an EnblProgramTaskSubCategory component for a custom exercise type that shows a screen flow.

```
<?xml version="1.0" encoding="UTF-8"?>

<EnblProgramTaskSubCategory xmlns="http://soap.sforce.com/2006/04/metadata">

```


### Metadata Types EntitlementProcess

```
      <developerName>ScreenFlowTaskSubCategory</developerName>

      <icon>standard:flow</icon>

      <learningItemType>ScreenFlowLearningItemType</learningItemType>

      <masterLabel>Screen Flow Exercise</masterLabel>

   </EnblProgramTaskSubCategory>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>ScreenFlowTaskSubCategory</members>

        <name>EnblProgramTaskSubCategory</name>

      </types>

      <version>62.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EntitlementProcess

Represents the settings for an entitlement process.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

Entitlement process values are stored in files in the `entitlementProcesses` directory. Each file has the name of a process and
the suffix `.entitlementProcess` . Each file contains one entitlement process or, if entitlement versioning is enabled, one version
of an entitlement process.

The name of the file is the name of the entitlement process with the version appended to the end, if applicable (for example, an entitlement
process named “gold_support” can have the file name “gold_support_v2.entitlementProcess”). This file name corresponds to the
`slaProcess.NameNorm` field exposed through SOAP API. This file name is distinct from the `name` field, which represents what
displays in the user interface and, if versioning is enabled, can be shared among multiple versions of the same entitlement process. The
`slaProcess.NameNorm` field contains the lowercase version of the `name` field shown in the user interface.

Version

Entitlement processes are available in API version 27.0 and later.


Metadata Types EntitlementProcess

Fields

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the entitlement process is active
( `true` ) or not ( `false` ).

`businessHours` string

The business hours that apply to the entitlement process.

This field is available in API version 30.0 and later.

`description` string The description of the entitlement process.

`entryStartDateField` string

`exitCriteriaBooleanFilter` string

For milestone processes on which a case enters the
process based on a custom date/time field on the case,
specifies which date and time are used. Valid values are:

**•** SlaStartDate (entitlement process start date)

**•** CreatedDate (date case was opened)

**•** ClosedDate (date case was closed)

**•** LastModifiedDate (date case was last modified)

**•** StopStartDate (date case was stopped)

For milestone processes on which a case exits the process
when custom criteria are met, and for which filter logic
is added, specifies that logic.

`exitCriteriaFilterItems` FilterItem[] For milestone processes on which a case exits the process
when custom criteria are met, specifies those criteria.

`exitCriteriaFormula` string

`isVersionDefault` boolean

For milestone processes on which a case exits the process
when a custom formula evaluates to true, specifies that
formula.

Indicates whether the entitlement process is the default
version ( `true` ) or not ( `false` ).

This field is available in API version 28.0 and later.

`milestones` EntitlementProcessMilestoneItem[] Represents a milestone on the entitlement process.

`name` string The name of the entitlement process as it displays in the
user interface.

`SObjectType` string Indicates the type of record that the entitlement process
can run on.

`versionMaster` string Identifies the sequence of versions to which this
entitlement process belongs. This field’s contents can be

any value as long as it’s identical among all versions of
the entitlement process.

This field is available in API version 28.0 and later.


Metadata Types EntitlementProcess

**Field Name** **Field Type** **Description**

`versionNotes` string

`versionNumber` int

EntitlementProcessMilestoneItem

Represents a milestone item on an entitlement process.

Fields

The description of the entitlement process version.

This field is available in API version 28.0 and later.

The version number of the entitlement process. Must be
1 or greater.

This field is available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`businessHours` string

The business hours that apply to the milestone.

This field is available in API version 30.0 and later.

`criteriaBooleanFilter` string For milestones that apply only when criteria are met
and for which filter logic is added, specifies that logic.

`milestoneCompletionCriteria` string

The criteria to be met for the milestone to be marked
complete.

`milestoneCriteriaFilterItems` FilterItem[] For milestones that apply only when criteria are met,
specifies those criteria.

`milestoneCriteriaFormula` string For milestones that apply only when a formula
evaluates to true, specifies that formula.

`milestoneName` string The name of the milestone.

`minutesCustomClass` string

The name of the Apex class that is used to calculate
the trigger time. This field is available in API version
30.0 and later.

`minutesToComplete` int The number of minutes from when the case enters the
entitlement process that the milestone occurs.

`successActions` WorkflowActionReference[] The actions triggered when the milestone is completed.

`timeTriggers` EntitlementProcessMilestoneTimeTrigger[] The time triggers on an entitlement process milestone.

`useCriteriaStartTime` boolean

When the milestone starts: when the milestone criteria
are met (true) or when the case enters the entitlement
process (false).


Metadata Types EntitlementProcess

EntitlementProcessMilestoneTimeTrigger

Represents the time trigger on an entitlement process milestone.

Fields

**Field Name** **Field Type** **Description**

`actions` WorkflowActionReference[] The actions to take when the time trigger is reached, if, at that time,
the milestone isn’t completed.

`timeLength` int The length of time between the time trigger activation and the
milestone target completion date. This length of time can be a

negative or positive value. Negative values indicate that the target
completion date hasn’t yet arrived and correspond to warning time
triggers. Positive values indicate that the target completion date has
passed and correspond to violation time triggers.

```
workflowTimeTriggerUnit

```

MilestoneTimeUnits Specifies the type of unit used to determine when a workflow is
(enumeration of type triggered. Valid values are:
string)

**•** `Minutes`

**•** `Hours`

**•** `Days`

Declarative Metadata Sample Definition

Here’s a sample entitlement process.

```
<?xml version="1.0" encoding="UTF-8"?>

<EntitlementProcess xmlns="http://soap.sforce.com/2006/04/metadata">

   <active>true</active>

   <description>eppersone</description>

   <entryStartDateField>SlaStartDate</entryStartDateField>

   <exitCriteriaBooleanFilter>1 OR 2</exitCriteriaBooleanFilter>

   <exitCriteriaFilterItems>

     <field>Case.IsClosed</field>

     <operation>equals</operation>

     <value>true</value>

   </exitCriteriaFilterItems>

   <exitCriteriaFilterItems>

     <field>Case.Description</field>

     <operation>startsWith</operation>

     <value>foo</value>

   </exitCriteriaFilterItems>

   <milestones>

     <milestoneName>m1</milestoneName>

     <minutesToComplete>1</minutesToComplete>

     <successActions>

        <name>emailBob</name>

        <type>Alert</type>

```


### Metadata Types EntitlementTemplate

```
        </successActions>

        <timeTriggers>

           <actions>

             <name>emailAlice</name>

             <type>Alert</type>

           </actions>

           <actions>

             <name>setEscalateToTrue</name>

             <type>FieldUpdate</type>

           </actions>

           <timeLength>1</timeLength>

           <workflowTimeTriggerUnit>Minutes</workflowTimeTriggerUnit>

        </timeTriggers>

        <timeTriggers>

           <actions>

             <name>setStopToTrue</name>

             <type>FieldUpdate</type>

           </actions>

           <timeLength>2</timeLength>

           <workflowTimeTriggerUnit>Minutes</workflowTimeTriggerUnit>

        </timeTriggers>

        <useCriteriaStartTime>false</useCriteriaStartTime>

      </milestones>

      <milestones>

        <milestoneCriteriaFilterItems>

           <field>Case.Priority</field>

           <operation>equals</operation>

           <value>High</value>

        </milestoneCriteriaFilterItems>

        <milestoneName>m2</milestoneName>

        <minutesToComplete>120</minutesToComplete>

        <useCriteriaStartTime>true</useCriteriaStartTime>

        <successActions>

           <name>emailBob</name>

           <type>Alert</type>

        </successActions>

      </milestones>

   </EntitlementProcess>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EntitlementTemplate

Represents an entitlement template. Entitlement templates are predefined terms of customer support that you can quickly add to
products. For example, you can create entitlement templates for Web or phone support so that users can easily add entitlements to
products offered to customers.

### EntitlementTemplate extends the Metadata metadata type and inherits its fullName field.


Metadata Types EntitlementTemplate

Declarative Metadata File Suffix and Directory Location

EntitlementTemplate components are stored in the `entitlementTemplates` directory of the corresponding package directory.
The file name matches the unique name of the entitlement template, and the extension is `.entitlementTemplate` .

Version

Lightning Platform EntitlementTemplate components are available in API version 18.0 and higher.

Fields

**Field** **Field Type** **Description**

`businessHours` string The entitlement's supported business hours.

`casesPerEntitlement` int The total number of cases the entitlement supports.

`entitlementProcess` string The entitlement process associated with the entitlement.
Entitlement processes are timelines that include all the steps

(milestones) that your support team must complete to resolve
cases. Each process includes logic to determine how to enforce
the correct service level for your customers.

`isPerIncident` boolean `true` if entitlements created from this template service a
limited number of cases; `false` otherwise.

`term` int The number of days the entitlement is in effect.

`type` string The type of entitlement, such as Web or phone support.

Declarative Metadata Sample Definition

A sample XML definition of an entitlement template is shown below.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EntitlementTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

      <businessHours>AlternateBusinessHours</businessHours>

      <casesPerEntitlement>12</casesPerEntitlement>

      <entitlementProcess>Process1</entitlementProcess>

      <isPerIncident>true</isPerIncident>

      <term>33</term>

      <type>Phone Support</type>

   </EntitlementTemplate>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types EscalationRules EscalationRules

Represents case escalation rules to escalate cases automatically if they aren’t resolved within a certain time. You can access rules metadata
for all applicable objects, for a specific object, or for a specific rule on a specific object.

The `package.xml` syntax for accessing all escalation rules for all objects is:

```
      <types>

        <members>*</members>

        <name>EscalationRules</name>

      </types>

```

All rules for a specific object use a similar syntax without the wildcard. For example, all escalation rules for the Case object would use
this syntax:

```
      <types>

        <members>Case</members>

        <name>EscalationRules</name>

      </types>

```

You can also access specific escalation rules for an object. The following example only accesses the “samplerule” and “newrule” escalation
### rules on the Case object. Notice that for this example the type name syntax is EscalationRule and not EscalationRules .

```
      <types>

        <members>Case.samplerule</members>

        <members>Case.newrule</members>

        <name>EscalationRule</name>

      </types>

```

File Suffix and Directory Location

### EscalationRules for an object have the suffix .escalationRules and are stored in the escalationRules folder. For example,

all Case escalation rules are stored in the `Case.escalationRules` file.

Version

### EscalationRules components are available in API version 27.0 and later.

Fields

**Field Name** **Field Type** **Description**

`escalationRule` EscalationRule[] on
page 1052

Represents one escalation rule and specifies whether it’s active or not.
Escalation rules are processed in the order they appear in the
### EscalationRules container.


Metadata Types EscalationRules

EscalationRule

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the escalation rule is active ( `true` ) or
not ( `false` ).

`fullname` string Inherited from Metadata, this field is defined in the WSDL
for this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see
an example of this field specified for a call.

This value can't be `null` .

`ruleEntry` `RuleEntry[]` Contains the definitions of the rule entries in the escalation
rule.

RuleEntry

Represents the fields used by the rule.

**Field Name** **Field Type** **Description**

`booleanFilter` string Advanced filter conditions that were specified for the rule.

`businessHours` string The hours when escalation actions are performed. Specify
only if `businessHoursSource` is set to `Static` .

`businessHoursSource` BusinessHoursSourceType Valid values are:
(enumerations of type string)

**•** `None`

**•** `Case`

**•** `Static`

`criteriaItems` FilterItem The items in the list that define the assignment criteria.

`disableEscalationWhenModified` boolean Indicates whether the escalation is disabled when the
record is modified `true` ) or not ( `false` ).

`escalationAction` EscalationAction[] The actions to perform when the escalation criteria are met.

`escalationStartTime` EscalationStartTimeType Indicates the start time for the escalation. Valid values are:
(enumeration of type string)

**•** `CaseCreation`

**•** `CaseLastModified`

`formula` string

The validation formula.

Specify either `formula` or `criteriaItems`, but not
both fields.


Metadata Types EscalationRules

EscalationAction

Describes the action to take for an escalation rule.

**Field Name** **Field Type** **Description**

`assignedTo` string The name of the user or queue the item is assigned to.

`assignedToTemplate` string

Specifies the template to use for the email that is
automatically sent to the new owner specified by the
escalation rule.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

`assignedToType` AssignToLookupValueType Valid values are:
(enumeration of type string)

**•** `User`

**•** `Queue`

`minutesToEscalation` int The number of minutes until the escalation occurs.

`notifyCaseOwner` boolean Indicates that the owner of the case is notified when the
case is escalated `true` ) or not ( `false` ).

`notifyEmail` string Specifies the email address of the user to notify.

`notifyTo` string Specifies the user to notify.

`notifyToTemplate` string Specifies the template to user for the notification email.

Declarative Metadata Sample Definition

The following is an example EscalationRules component:

```
<EscalationRules xmlns="http://soap.sforce.com/2006/04/metadata">

   <escalationRule>

     <fullName>samplerule</fullName>

     <active>false</active>

     <ruleEntry>

        <businessHours>test</businessHours>

        <businessHoursSource>Static</businessHoursSource>

        <criteriaItems>

          <field>Case.Description</field>

          <operation>contains</operation>

          <value>test</value>

        </criteriaItems>

        <escalationAction>

          <assignedTo>someuser@org.com</assignedTo>

          <assignedToTemplate>emailtemplatename</assignedToTemplate>

          <assignedToType>User</assignedToType>

          <minutesToEscalation>1440</minutesToEscalation>

          <notifyCaseOwner>false</notifyCaseOwner>

        </escalationAction>

```


### Metadata Types EventDelivery

```
           <escalationStartTime>CaseLastModified</escalationStartTime>

        </ruleEntry>

      </escalationRule>

   </EscalationRules>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EventDelivery

Represents how an event instance maps to a target payload. Removed in API version 46.0. This type extends the Metadata metadata
type and inherits its `fullName` field.

File Suffix and Directory Location

Event delivery components have the suffix file path `.delivery`, and are stored in the `eventDeliveries` folder.

Version

Event delivery components are available in API versions 41.0 to 45.0.

Limits

Your org can have a maximum of 2500 EventDelivery object instances.

Fields

**Field Name** **Field Type** **Description**

`eventParameters` EventParameterMap[] An array of parameters to deliver in addition to the published event’s data.

`eventSubscription` string Required. The ID of the subscription to deliver the data to.

`referenceData` string User-defined non-unique identifier.

Required. Determines what action occurs when the event is delivered to the listeners on
behalf of the subscribers.

Valid values are:

**•** `StartFlow` —When the event occurs, it’s delivered to a flow of type CustomEvent.
Those flows are built through Process Builder.

**•** `ResumeFlow` —Reserved for future use.


```
type

```

### EventDeliveryType

(enumeration of type
string)

### Metadata Types EventRelayConfig

EventParameterMap

Parameters to deliver in addition to the published event’s data.

If `type` is `StartFlow`, you must include a parameter where `parameterName` is `FlowVersionName` and `parameterValue`
is the name of the flow that you want to start. The flow name must include its version number. For example, `myFlow-3` .

Each event delivery can have up to 10 parameters.

**Field Name** **Field Type** **Description**

`parameterName` string The parameter name.

`parameterValue` string The parameter value.

Declarative Metadata Sample Definition

The following is an example of an event delivery file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EventDelivery xmlns="http://soap.sforce.com/2006/04/metadata">

     <eventParameters>

       <parameterName>FlowVersionName</parameterName>

       <parameterValue>My_Event_Based_Process-1</parameterValue>

     </eventParameters>

     <eventSubscription>MySubscription</eventSubscription>

     <referenceData>My_Event_Based_Process_1</referenceData>

     <type>StartFlow</type>

   </EventDelivery>

```

The following is an example `package.xml` that deploys or retrieves all the available event delivery metadata in your org.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>EventDelivery</members>

       <name>*</name>

     </types>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EventRelayConfig

Represents the configuration of an event relay, which relays platform events and change data capture events from Salesforce to Amazon
EventBridge.


Metadata Types EventRelayConfig

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

`EventRelayConfig` components have the suffix `.eventRelay` and are stored in the `eventRelays` folder.

Version

EventRelayConfig components are available in API version 56.0 and later.

Special Access Rules

**•** You must have the Customize Application permission to deploy and retrieve this type.

**•** You can update only the `state` and `relayOption` fields and not `eventChannel` or `destinationResourceName` .

Fields

**Field Name** **Description**

```
destinationResourceName

eventChannel

label

relayOption

```

**Field Type**
string

**Description**
Required. The developer name of the named credential, which stores the AWS account
information. The `destinationResourceName` value contains the `callout:`
prefix. For example: `callout:MyRelayNamedCredential`

**Field Type**
string

**Description**
Required. The full name of the event channel used in the event relay. For example:

```
  MyRelayChannel__chn

```

**Field Type**
string

**Description**
The label for the event relay. The label is displayed in the user interface. Make sure you
use a meaningful label that describes your event relay and try to make it unique.

**Field Type**
string


Metadata Types EventRelayConfig

**Field Name** **Description**

**Description**
A JSON-encoded string that contains an option for resuming an event relay after the
system recovers from an error. This option is used if the event relay can't resume after
the last relayed event. The options available are:

**•** `{\"ReplayRecovery\":\"LATEST\"}` —(Default) Start relaying events
from new events received in the event bus. Use this option if you aren’t interested
in missed events while the relay was down.

**•** `{\"ReplayRecovery\":\"EARLIEST\"}` —Resend all events stored in
the event bus and relay new events thereafter. The event bus stores events for up
to three days. Use this option if you want to reprocess all stored events and catch
up on missed events.

```
state

usageType

```

**Field Type**
EventRelayAdminState (enumeration of type string)

**Description**
The execution state of the event relay. Possible values are:

**•** `RUN` —The event relay is running and actively relaying event messages from
Salesforce to Amazon EventBridge.

**•** `PAUSE` —An administrator paused the event relay. No events are relayed to
Amazon EventBridge during this status. All current state information is saved.

**•** `STOP` —(Default) The event relay is stopped and no events are relayed to Amazon
EventBridge. All current state information is deleted.

The event relay is created with a default state of `STOP` if you don't specify this
field. If you specify this field when creating an event relay, the only valid value you
can set is `STOP` .

**•** `DELETE` —Reserved for future use.

**Field Type**
string

**Description**
Reserved for future use.

Declarative Metadata Sample Definition

The following is an example of an EventRelayConfig component with the file name `Carbon_Comparison_Relay.eventRelay` .

```
<?xml version="1.0" encoding="UTF-8"?>

<EventRelayConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <destinationResourceName>callout:AWS_Account</destinationResourceName>

   <eventChannel>Carbon_Comparison_Channel__chn</eventChannel>

   <label>Carbon Comparison Relay</label>

   <relayOption>{\"ReplayRecovery\":\"LATEST\"}</relayOption>

```


### Metadata Types EventSubscription

```
      <state>STOP</state>

   </EventRelayConfig>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Carbon_Comparison_Relay</members>

        <name>EventRelayConfig</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EventSubscription

Represents a subscription to an event type. Removed in API version 46.0. This type extends the Metadata metadata type and inherits its
`fullName` field.

File Suffix and Directory Location

### EventSubscription components have the suffix file path .subscription, and are stored in the eventSubscriptions folder.

Version

Event subscription components are available in API versions 41.0 to 45.0.

Limits

Your org can have a maximum of:

**•** 4,000 total event subscriptions

**•** 2,000 active event subscriptions

Fields

**Field Name** **Field Type** **Description**

`active` boolean If the subscription isn’t active, it never receives any events.

`eventParameters` EventParameterMap[] An array of parameters that must be true for published events.

`eventType` string Required. The name of the platform event.


Metadata Types EventSubscription

**Field Name** **Field Type** **Description**

`referenceData` string Required. If the subscriber is a flow of type CustomEvent, `referenceData` is
_**`flowName`**_ `_` _**`versionNumber`**_ . For example, `Printer_Management_2` .

EventParameterMap

An array of parameters that must be true for published events. For example, subscribe to Vendor Response events only if `Status__c`
is `Shipped` .

Each event subscription can have up to 10 parameters.

**Field Name** **Field Type** **Description**

`parameterName` string Required. The published event’s field name.

`parameterValue` string The value that must be true.

Declarative Metadata Sample Definition

The following is an example of an active event subscription.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EventSubscription xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <eventType>Printer_Status__e</eventType>

      <referenceData>Printer_Management</referenceData>

   </EventSubscription>

```

The following is an example of an inactive event subscription that sets event parameters.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EventSubscription xmlns="http://soap.sforce.com/2006/04/metadata">

     <name>MySubscription</name>

     <active>false</active>

     <eventParameters>

       <parameterName>Ink_Status__c</parameterName>

       <parameterValue>low</parameterValue>

     </eventParameters>

     <eventParameters>

       <parameterName>Serial_Number__c</parameterName>

       <parameterValue>00123456789</parameterValue>

     </eventParameters>

     <eventType>Printer_Status__e</eventType>

     <referenceData>My_Event_Based_Process_1</referenceData>

   </EventSubscription>

```

The following is an example `package.xml` that deploys or retrieves all the available event subscription metadata in your org.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

```


### Metadata Types ExperienceBundle

```
       <name>EventSubscription</name>

     </types>

     <version>41.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ExperienceBundle

Represents a text-based code structure of the settings and site components, such as pages, branding sets, and themes that make up an
Experience Builder site. Developers can quickly update and deploy Experience Builder sites _programmatically_ using their preferred
development tools. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExperienceBundle components have the suffix .json and are stored in the experiences folder when retrieved. Each Experience

Builder site in your org has its own folder. Each of these folders contains other folders for the supported properties.

The ExperienceBundle can contain one or more site definitions under the `experiences` folder. Each site definition has resource
folders for brandingSets, config, routes, themes, variations, and views, each with additional, related configuration information in JSON
files. Here’s an example site definition, showing the resource folders.

Version

### ExperienceBundle components are available in API version 46.0 and later.


Metadata Types ExperienceBundle

Special Access Rules

To use the ExperienceBundle metadata type for Aura-based Experience Builder sites, from Setup, enter _`Digital Experiences`_
in the Quick Find box, and then select **Settings** . Select **Enable ExperienceBundle Metadata API**, and save your changes. LWR sites
use ExperienceBundle by default.

Fields

**Field Name** **Field Type** **Description**

`experienceResources` ExperienceResources[]

The list of resources in this ExperienceBundle. Each resource represents an
artifact of a site such as brandingSets, config, routes, themes, variations, and
views.

`label` string Required. Represents the name of the ExperienceBundle.

`type` SiteType (enumeration Required. Identifies the kind of site. Only Experience Builder sites are supported,
of type string) using the value `ChatterNetworkPicasso` .

`urlPathPrefix` string Specify a URL prefix for an Experience Builder site. For example, in the site URL
SitesSubdomainName.force.com/customers, customers is the UrlPathPrefix.

Note: For authenticated LWR sites created before Winter ’23 and Aura
sites, the URL path prefix ends in /s, and the part of the path without
the /s must match the Network metadata type’s URL. For
unauthenticated LWR sites and authenticated LWR sites created after
Winter ’23 through Experience Builder or Connect API, this path doesn’t
contain /s, and the path can be anything as long as there’s no conflict.

**Sample meta.xml file**

```
                       <?xml version="1.0" encoding="UTF-8"?>

                       <ExperienceBundle

                       xmlns="http://soap.sforce.com/2006/04/metadata">

                         <label>SampleStarterSite2</label>

                         <type>ChatterNetworkPicasso</type>

                       <urlPathPrefix>SampleStarterSite2/s</urlPathPrefix>

                       </ExperienceBundle>

```

ExperienceResources

Represents a list of sites in the bundle.

**Field Name** **Field Type** **Description**

`experienceResource` ExperienceResource[] The list of resources in this ExperienceBundle. Each resource represents a
property for the site, such as brandingSets, config, routes, themes, and views.


Metadata Types ExperienceBundle

ExperienceResource

Represents specific site information included in the ExperienceBundle.

Each type has a folder in the structure. Each folder contains one or more files providing information about that type and the site. Each
corresponds to a specific folder and file in the ExperienceBundle.

**Field Name** **Field Type** **Description**

`fileName` string Required. Name of resource file.

`format` string Required. Only `JSON` is allowed.

`source` base64 The `JSON` content of each file.

`type` string Required. The type of the resource. Valid values are:

**•** `brandingSets`

**•** `config`

**•** `routes`

**•** `themes`

**•** `views`

Folders and Bundled Definitions

Each ExperienceBundle includes folders and associated data that is contained in JSON files.

brandingSets Folder

This folder contains one JSON file per branding set, named _`brandingSets_name`_ `.json` . Each file has the same structure and
properties.

```
   <brandingSets_name> .json

```

**Property** **Type** **Description**

`brandingSetType` string Required in LWR sites. Not applicable for Aura sites. Represents whether the
color palette stored in the branding set is for the entire site or a specific section.

You can’t change one branding set type to another. Available in API Version
52.0 and later.

Valid values are:

**•** `APP` : The branding set applies to the entire site. There can be only one
branding set of this type.

**•** `SCOPED` : The branding set applies to a specific section.

`definitionName` string

Required. Represents the name for the branding set that is used in grouping
branding sets under a theme. Defined as _`theme`_ :branding- _`theme`_ .

For example, if the site theme is Stella, the `definitionName` would be
`stella:branding-stella` .


Metadata Types ExperienceBundle

**Property** **Type** **Description**

In addition, there are several standard templates that have unique naming:

**•** Customer Account Portal uses `cpt:branding-cpt`

**•** Customer Service uses `service:branding-service`

**•** Help Center uses `helpCenter:branding-helpCenter`

**•** Partner Central uses `prm:branding-prm`

**•** Build Your Own uses `starter:branding-starter`

Note: The combination of `definitionName` + `label` must be
unique in your org.

`id` UUID Represents the component’s GUID.

`label` string Represents the name of the branding set.

Note: The combination of `definitionName` + `label` must be
unique in your org.

`type` string Represents the component type. The only supported value is `brandingSet` .

`values` map Required. Represents a map of branding values that can be applied to a site.

```
   {

     "values" : {

      "HeaderBackgroundColor" : "#FFFFFF",

      "TextTransformStyle" : "none",

      "BorderColor" : "#D4D4D4",

      "DetailTextColor" : "#5A5A5A",

      "HeaderFonts" : "Ek Mukta",

      "CardBackgroundColor" : "rgba(255, 255, 255, 0)",

      "LoginBackgroundColor" : "#F4F4F4",

      "_ActionColorTrans" : "rgba(25, 124, 190, 0.9)",

      "LoginBackgroundImage" :

   "../../../../sfsites/picasso/core/external/salesforceIdentity/images/background.jpg?v=1",

      "PageBackgroundColor" : "#F5F7FA",

      "_HeaderTextColor" : "rgba(34,34,34,.8)",

      "_NavigationMenuHoverColor" : "rgba(255,255,255,.2)",

      "_HeaderInputBackgroundColor" : "rgba(255,255,255,.4)",

      "TextColor" : "#222222",

      "NavigationMenuTextColor" : "#222222",

      "_HeaderPlaceholderTextColor" : "rgba(85,85,85,.8)",

      "_OverlayTextColorShadow" : "#000000",

      "ActionColor" : "#0099DE",

      "CompanyLogo" : "",

      "_LinkColorDarker" : "#135F90",

      "_ActionColorDarker" : "#135F90",

      "_HoverColor" : "rgba(25, 124, 190, 0.05)",

      "ErrorFontColor" : "#ff9e9e",

      "OverlayTextColor" : "#FFFFFF",

```


Metadata Types ExperienceBundle

```
      "PrimaryFont" : "Ek Mukta",

      "LinkColor" : "#3558D6"

      },

     "definitionName" : "cpt:branding-cpt",

     "label" : "Customer Account Portal",

     "id" : "283407c3-5938-4a6b-b97f-621cda6968c8",

     "type" : "brandingSet"

    }

```

config Folder

The `config` folder contains several JSON files.

**•** _`sitename`_ `.json`

**•** `languages.json`

**•** `nativeConfig.json`

**•** _`page_name`_ `.json`

Note: One for each single-page application in the site: `loginAppPage.json` and `mainAppPage.json`

_`sitename`_ `.json` **File Properties**

**Property** **Type** **Description**

`authenticationType` string For LWR sites, indicates whether guest users have access to the site.

Note: For Aura sites, use `isAvailableToGuests` instead.

Valid values are:

**•** `AUTHENTICATED` : The site isn’t public. Only authenticated users can
access the site after logging in.

**•** `AUTHENTICATED_WITH_PUBLIC_ACCESS_ENABLED` : The site is
an authenticated site, but the **Public can access the site** checkbox is
enabled in Experience Builder in **Settings**                                   - **General** . Guest users can
access the site.

**•** `UNAUTHENTICATED` : The unauthenticated site is publicly available to
anyone on the web, and doesn’t support login or authentication. Guest
users can access the site. `UNAUTHENTICATED` isn’t supported for LWR
sites created after Winter ’23 through Experience Builder or Connect API.
To allow guest user access, we recommend using
`AUTHENTICATED_WITH_PUBLIC_ACCESS_ENABLED` .

Available in API version 51.0 and later.

`forgotPasswordRouteId` UUID Represents the ID of the route to use when a user forgets their password.

Note: Unsupported if the active Experience Builder template for the
site doesn't support login (such as Help Center).


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`isAvailableToGuests` boolean For Aura sites, indicates whether public users have access to the site ( `true` )
or not ( `false` ). The default value is `false` .

Note: For LWR sites, use `authenticationType` instead.

`isFilteredComponentsView` boolean Indicates whether the list of components is filtered based on the current page
type ( `true` ) or not ( `false` ). Some components require specific parameters

from the page and don't work unless you manually configure them. The default
value is `false` .

`isLockerServiceEnabled` boolean

Indicates whether Lightning Locker is enabled ( `true` ) or disabled ( `false` ).
The default value is `true` .

Available in API version 55.0 and later.

`isProgressiveRenderingEnabled` boolean Indicates whether the display order of page components is prioritized ( `true` )
or not ( `false` ). The default value is `false` .

`loginAppPageId` UUID Represents the ID of the login page.

Note: Unsupported if the active Experience Builder template for the
site doesn't support login (such as Help Center).

`mainAppPageId` UUID Required. Represents the ID of the main page.

`preferredDomain` string

`preferredDomainId` string

Represents the name of the domain to use for indexing a site’s pages. Improves
search engine results.

Available in API version 48.0 and later.

Represents the domain to use for indexing a site’s pages. Improves search
engine results.

Removed in API version 48.0. Use `preferredDomain` instead.

`selfRegistrationRouteId` UUID Represents the ID of the login route to use for self-registration.

Note: Unsupported if the active Experience Builder template for the
site doesn't support login (such as Help Center).

`type` string Represents the component type. The only supported value is `site` .

**trustedSitesForScript container**

When implemented, there’s one `trustedSitesForScript` container in _`sitename`_ `.json` .

**Property** **Type** **Description**

`id` UUID Represents the component's GUID.

`isActive` boolean Indicates if allowlisted item is active ( `true` ) and must be respected or inactive
( `false` ) and must not be treated as an allowlisted source. Default is `false` .


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`trustedSiteName` string Name of the allowlisted source as it appears in the UI.

`trustedSiteUrl` string The fully qualified URL of the allowlisted source.

`type` string Represents the component type. The only supported value is
`trustedSitesForScripts` .

```
   {

     "isAvailableToGuests" : false,

     "isFilteredComponentsView" : false,

     "mainAppPageId" : "df9907cb-6e68-4ca1-8bb2-51173ca5374e",

     "loginAppPageId" : "58e9939a-84b2-498d-bbc5-7a89d89087fa",

     "selfRegistrationRouteId" : "ad5c8bf1-297f-4ad3-b47c-0e35d85f10ef",

     "forgotPasswordRouteId" : "e3139f6f-44d8-4eec-be9d-3609ce063039",

     "isProgressiveRenderingEnabled" : false,

     "preferredDomain" : "none",

     "selfRegistrationRouteId" : "b8fe8ab1-f266-41e1-a63b-4791165f3c1d",

     "trustedSitesForScript" : [ {

      "id" : "92c489e2-0b7b-4a48-9c88-bef7e8fe6f1b",

      "isActive" : true,

      "trustedSiteName" : "test",

      "trustedSiteUrl" : "https://123.com",

      "type" : "trustedSitesForScripts"

     }, {

      "id" : "92c489e2-0b7b-4a48-9c88-bef7e8fe6f1c",

      "isActive" : true,

      "trustedSiteName" : "test1",

      "trustedSiteUrl" : "https://1234.com",

      "type" : "trustedSitesForScripts"

     } ],

      "type" : "site"

   }

```

`languages.json` **File Properties**

**Property** **Type** **Description**

`defaultCode` string Required. Represents the base language code plus the country code where
used.

`defaultLabel` string Required. Defines the display label for the language.

`id` UUID Represents the component's GUID.

`type` string Represents the component type. The only supported value is
`languageContainer` .

There’s one section per supported language as a container in `languages.json`

**language container**


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`countryCode` string Represents the country code of the selected language. This string can be empty.
It applies only when the selected language has variations depending on the

country, like Arabic (Algeria) and Arabic (Bahrain). In this case, use
`countryCode` to distinguish between them.

For example: `{ languageCode" : "ar", "CountryCode" :`

```
                        "DZ", "Label" : "Arabic (Algeria) (DZ)",}, { "Code"

                        : "ar", "CountryCode" : "BH", "Label" : "Arabic

                        (Bahrain) (BH)",}

```

`fallbackLanguageId` UUID Represents the language to use when no content is available for the selected
language. For example, if a site visitor chooses **Japanese** from the language

selector, but there’s no content for that page in Japanese, then content is
displayed in the fallback language.

Only one level of fallback is allowed for LWR sites. Here are examples for an
LWR site where English is the default language, and Spanish, French, and Finnish
are available site languages.

**•** Not allowed: Spanish falls back to French, and French falls back to Finnish.
This configuration includes two levels of fallback.

**•** Allowed: Spanish falls back to French, and French falls back to English. This
configuration is allowed because English is the site’s default language.

**•** Allowed: Spanish falls back to French, and French has no fallback. This
configuration includes only one level of fallback.

`id` UUID Represents the component's GUID.

`isActive` boolean Indicates whether a language is available to site visitors in the language selector
( `true` ) or not ( `false` ). The default value is `true` .

`label` string

Defines the display label for a language. The display label appears in any
language selector components that you add to your site and in the language
selector in Experience Builder.

`languageCode` string Represents the language code for the selected language.

`type` string Represents the component type. The only supported value is `language` .

```
{

  "defaultCode" : "en_US",

  "defaultLabel" : "English (US)",

  "id" : "04597c83-0b9d-4f16-9f4d-4ec28bd553b4",

  "type" : "languageContainer",

  "languages" : [ {

     "languageCode" : "af",

     "countryCode" : "",

     "isActive" : true,

     "label" : "Afrikaans",

     "fallbackLanguageId" : "c6e7fe67-55e0-47b3-ad58-bf49539249f0",

```


Metadata Types ExperienceBundle

```
        "id" : "22036d6f-11ce-4f7b-b7f0-f2c409f817ea",

        "type" : "language"

        }

      ]

    }

```

The page file represents single-page applications in the site. One file per page, named _`page_name`_ `.json` .

Note: Each Experience Builder site is actually a single-page application, which is a web app that loads a single `HTML` page.
Single-page applications use multiple views to update the page dynamically as the user interacts with it.

`nativeConfig.json` **File Properties**

**Property** **Type** **Description**

`showHamburgerMenu` boolean Required. Controls whether the hamburger menu is shown.

`mobilePublisherAppUpdateConfig` boolean

Required. Controls whether and which App Version Update message is shown.
To avoid service disruptions, users must be on the app version that supports
enhanced domains.

`id` UUID Represents the component's GUID.

`type` string Represents the component type. The only supported value is
`nativeConfig` .

```
{

 "id": "a70a0e5e-0400-4531-94dc-8f587daa5946",

 "nativeMobileNavConfig": {

  "showBackButton": true,

  "showHamburgerMenuWithBackButton": false

 },

 "mobilePublisherAppUpdateConfig": {

  "enableAppUpdate" : true,

  "forceAppUpdate" : true,

  "minVersion" : {

    "ios" : {

       "version" : "10.0"

 },

    "android" : {

         "version" : "10.1"

 }

 }

 },

 "nativeTabMenu": {

  "branding": {

   "iconTintColorUnselected": "#C9C5C5",

   "barTintColor": "#FF00FF",

   "iconTintColor": "#555321"

  },

  "menuItems": [

   {

    "iconAsset": "icon_homepng",

```


Metadata Types ExperienceBundle

```
        "targetUrl": "/"

      },

      {

        "name": "Test",

        "iconAsset": "icon_filespng",

        "targetUrl": "/files"

      }

     ]

    },

    "showNavMenu": true,

    "type": "nativeConfig"

   }

```

**nativeMobileNavConfig container**

A required container for the configuration for the Native Navigation Bar component.

**Property** **Type** **Description**

`showBackButton` boolean Controls whether the Back button is shown on iOS devices.

`showHamburgerMenuWithBackButton` boolean Controls whether the hamburger menu is shown, in addition to
the Back button, on iOS devices.

**mobilePublisherAppUpdateConfig container**

A required container for the configuration of the App Version Update message.

**Property** **Type** **Description**

`enableAppUpdate` boolean

`forceAppUpdate` boolean

`minVersion` string

Controls whether the App Version Update message is shown, to
encourage users to update by giving them a choice of whether
to do so.

Set the properties to `"enableAppUpdate" : true`, and

`"forceAppUpdate" : false` to show the message that
encourages your users to update.

If you don’t want to show an update message, for example if all
your users are on the correct version or your site uses a custom
domain, set the property to `"enableAppUpdate" :`
`false`, and don’t use the `forceAppUpdate` property.

Controls whether the App Version Update message to require
users to update is shown.

Set the properties to `"enableAppUpdate" : true`, and

`"forceAppUpdate" : true` to show the message that
requires your users to update.

Controls the iOS and Android Minimum App Versions. These
property values are currently hard coded to ensure that the app
versions supporting enhanced domains are used.


Metadata Types ExperienceBundle

**nativeTabMenu container**

A required container for the configuration of the hamburger menu and Back button behavior.

**Property** **Type** **Description**

`branding` map Settings for the Native Navigation Bar component branding. Valid keys are:

**•** iconTintColorUnselected

**•** iconTintColor

**•** barTintColor

Supply a valid 6 digit hexadecimal as the value for all properties.

`menuItems` list Items which must be displayed in the Native Navigation Bar component.

**menuItems container**

A container within the nativeTabMenu container that specifies the items displayed in the tab bar of the Native Navigation Bar component.

**Property** **Type** **Description**

`name` string Optional. The label of the tab bar menu item.

`targetUrl` string Required. The relative URL to which the tab bar menu item points.

`iconAsset` string Required. Name of the ContentAsset to use for the tab bar menu item.

_`page_name`_ `.json` **File Properties**

**Property** **Type** **Description**

`cmsSettings` map Settings for the CMS Connect header and footer. Valid values are:

**•** `headerName`

**•** `headerUrl`

**•** `headerPersonalization`

**•** `footerName`

**•** `footerUrl`

**•** `footerPersonalization`

Both source and target org must have the CMSConnect and CMSPersonalization
org perms enabled for settings to be retrieved.

`currentThemeId` UUID

`headMarkup` string

Required. Represents the UUID of the site's current theme. This field is available
for `mainAppPage.json` and `loginAppPage.json` (where
applicable).

Required. Allows the addition of custom markup to the site's main page

`<head>` tag. Similar to using **Experience Builder** - **Setting** - **Advanced** **Head Markup** [See Salesforce Help for markup guidance.](https://help.salesforce.com/articleView?id=community_builder_page_head.htm&type=5&language=en_US)

`id` UUID Required. Represents the component's GUID.


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`isRelaxedCSPLevel` boolean

Controls the ability to run scripts and script access to third-party hosts. The
default is `false` . This field is available for `mainAppPage.json` and
`loginAppPage.json` (where applicable).

`label` string Required. Represents the name of the page.

`templateName` string Required. The unique developer name of the template. Allowed values include:

**•** CPT Community Template (which represents the Customer Account Portal
template)

**•** Help Center Template (which represents the Help Center template)

**•** microsite-template-marketing (which represents the Microsite (LWR)
template

**•** PRM Community Template (which represents the Partner Central template)

**•** Service Community Template (which represents the Customer Service
template)

**•** Starter Template (which represents the Build Your Own (Aura) template)

**•** talon-template-byo (which represents the Build Your Own (LWR) template)

**•** _`Custom_template_name`_ (which is the name of a customized
template that was exported as a Bolt Solution)

Alternatively, you can retrieve a list of allowed template name values using
[Connect REST API. See Experience Builder Templates in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_communities_templates.htm) _Connect REST API_
_Developer Guide_ .

`type` string Required. Represents the component type. The only supported value is
`appPage` .

```
{

   "headMarkup" : null,

   "isRelaxedCSPLevel" : false,

   "templateName" : "Starter Template",

   "cmsSettings" : { },

   "currentThemeId" : "ff52089c-6ad9-4dd9-b5b5-251d4a117ce3",

   "label" : "main",

   "id" : "df9907cb-6e68-4ca1-8bb2-51173ca5374e",

   "type" : "appPage"

}

```

routes Folder

The `routes` folder contains one JSON file per page, named _`<page_name>`_ `.json` .

```
<page_name> .json

```


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`activeViewId` UUID

Required. Represents the default view of the route. Used when there are no
defined audiences or the user doesn’t match any audience.

Available in API version 48.0 and later.

`appPageId` UUID Required. Represents the single page application (SPA) page for the route. It
points to either `main.json` or `login.json` .

`configurationTags` string[] Required. Represents the configuration tags for the route. The only supported
value is `allow-in-static-site` . Available in API Version 51.0 and later.

Note: This is an internal property and must not be edited.

`devName` string[] Required. Represents the unique API name that’s defined when creating a new
route. Available in API version 59.0 and later.

`id` UUID Required. Represents the component GUID. Inherited from the component.

`label` string Required. Represents the name of the route. Inherited from the component.

`objectApiName` string Required. The name of the custom object API. (Not available for standard
objects.)

`pageAccess` string Required. Identifies the status of a route as public or private. When set to the
default value `UseParent`, the status of the site determines the status of the

route. Not editable from the user interface for routes that are always private.
Valid values are `UseParent`, `Public`, and `RequiresLogin` .

`routeType` string Required. Identifies the type of route. Value is unique among all routes that
share the same SPA page. The value in `viewType` must match.

`type` string Required. Represents the component type. The only supported value is `route` .

`urlPrefix` string Required. Represents the base URL for the route.

```
{

   "urlPrefix" : "",

   "appPageId" : "b5fe94e2-071f-47b2-b76d-427a624cb407",

   “configurationTags” : “allow-in-static-site”

   "routeType" : "home",

   "pageAccess" : "UseParent",

   "label" : "Home",

   "id" : "c7263124-7bc4-4147-a39a-25fe7e305b98",

   "type" : "route"

}

```

themes Folder

The `themes` folder contains one JSON file per theme named _`theme_name`_ `.json` .

```
theme_name .json

```


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`activeBrandingSetId` UUID The id of the branding set currently in use. The branding set's
`definitionName` must match the theme's `brandingSetReference` .

`customCSS` string Custom CSS for pages created in the Experience Builder template.

`developerName` string

Required. The unique developer name of the theme. Most themes derive their
names directly, for example Jepson uses `jespon` for its `developerName` .

Standard templates have unique values:

**•** `cpt` for Customer Account Portal

**•** `service` for Customer Service

**•** `helpCenter` for Help Center

**•** `prm` for Partner Central

**•** `starter` for Build Your Own

`id` UUID Required. Represents the component's GUID.

`label` string Represents the name of the theme.

`layouts` map Required. Maps `ThemeLayoutType` to UUID, and contains the definition
of the ThemeLayout. Login and Inner theme layouts are always required.

`type` string Required. Represents the component type. The only supported value is `theme` .

```
{

  "developerName" : "cpt",

  "layouts" : {

     "Login" : "12162c3e-06ac-43a9-adc7-db36ae5140b0",

     "Inner" : "c09d58be-0622-4fc4-806a-ed34174929f9"

  },

  "customCSS" : "",

  "activeBrandingSetId" : "283407c3-5938-4a6b-b97f-621cda6968c8",

  "label" : "Customer Account Portal",

  "id" : "ff52089c-6ad9-4dd9-b5b5-251d4a117ce3",

  "type" : "theme",

  "views" : [ {

     "componentName" : "salesforceIdentity:loginBody2",

     "label" : "Login",

     "id" : "12162c3e-06ac-43a9-adc7-db36ae5140b0",

     "type" : "view",

     "regions" : [ {

       "regionName" : "header",

       "id" : "f8354922-11f2-495d-9d89-0a51943af2b0",

       "type" : "region",

       "components" : [ ]

     } ]

  } ]

}

```


Metadata Types ExperienceBundle

Note: Views can be children of a theme. These children are structured the same as views in the views folder.

variations Folder

Experience variations let you change the default behavior of the Experience Builder site based on the audience. The `variations`
folder contains one JSON file per experience variation. The file is named _`experienceVariation_name`_ `.json` .

Note:

**•** Experience variations are available in API version 47.0 and later.

**•** The name of your JSON file must match the `developerName` of your variation to avoid issues when deploying a site more
than one time.

Four distinct types of variations are supported: branding sets, page variations, component visibility, and component attributes. The
different variations are indicated through the `componentVariant` container.

For example, you want the site to show a page variation for the home page when a user meets certain audience criteria. To achieve this,
create an audience and then target that audience to your experience variation using `targetId` in the `componentVariant`
container of the experience variation definition file.

```
   experienceVariation_name .json

```

**Property** **Type** **Description**

`componentVariants` list Required. A list of component variants that belong to this experience variation.

Note: Only one component variant per experience variation is allowed.

`developerName` string

Required. The unique developer name of the experience variation. This name
is used in the `targetValue` field of a Personalization API target and can’t
be updated after it’s set.

Note: For more information, see Audience.

`id` UUID Required. Represents the GUID of the component.

`type` string Required. Represents the type of the component. The only supported value is
`experienceVariation` .

When implemented, there’s one container in each _`experienceVariation_name`_ `.json` file describing the variation.

**componentVariant container**

**Property** **Type** **Description**

`id` UUID Required. Represents the GUID of the component.

`propertyOverrides` map

Required. Defines the property overrides for the given theme, route, or
component `targetId` .

For example, if the `targetId` is pointing to a theme, you can override the
`defaultBrandingSet` property of the theme to use a different branding
set for this experience variation.


Metadata Types ExperienceBundle

**Property** **Type** **Description**

Supported property overrides:

```
                        activeBrandingSetId
```

Defines which branding set to use when `targetId` is a theme. Uses the
format:

```
                            "activeBrandingSetId" : " ID_of_brandingset "

                        activeViewId
```

Defines which page variation to use when `targetId` is a route. Uses
the format:

```
                            "activeViewId" : " ID_of_view "

                        componentAttributes
```

Supported only for CMS Collection components and navigation
components, such as Navigation Menu or Tile Menu. Components can be
placed in header and footer regions, and also in the view body.

**•** Defines which navigation linkset to display when `targetId` is a
navigation component.

The value of the property is a JSON container with a single key-value
pair denoting the attribute and the value of the attribute.

`NavigationMenuEditorRefresh` is the only supported
attribute. Uses the format:

```
                             "componentAttributes" : {

                               "NavigationMenuEditorRefresh" :

                             " linkset_name "

                             }

```

**•** Defines which content collection to display when `targetId` is a
CMS Collection component.

The value of the property is a JSON container with a single key-value
pair denoting the path to the attribute and the value of the attribute.

```
                           config/dataProviderDefinition/attributes/dataProviderInfo/apiName
```

is the only supported attribute. Uses the format:

```
                             "componentAttributes" : {

                               "config/dataProviderDefinition/attributes

                             /dataProviderInfo/apiName":" collection_name "

                             }

                        isVisible
```

Defines whether a component is visible for the audience when `targetId`
is a component. Unsupported for components in header or footer regions.
Uses the format:

```
                            "isVisible": boolean

```


Metadata Types ExperienceBundle

**Property** **Type** **Description**

Note:

**•** Only one entry in the map is allowed.

**•** For a component, you can vary either its visibility or attributes but
not both together.

`targetId` UUID Required. The UUID of the item whose properties you’re overriding. Must be
the ID of a theme, route, or component.

`type` string Required. Represents the type of the component. The only supported value is
`experienceVariation` .

**Example of an experience variation for a branding set**

```
   {

     "id": "64e93604-78fa-11e9-8f9e-2a86e4085a59",

     "developerName": "BrandingVariation",

     "type": "experienceVariation",

     "componentVariants": [{

       "id": "4bf0af78-8d73-11e9-bc42-526af7764f64",

       "type": "componentVariant",

       // Theme UUID

       "targetId": "c810858e-78fa-11e9-8f9e-2a86e4085a59",

       "propertyOverrides": {

         // Brandingset UUID

         "activeBrandingSetId": "be9f4760-78fa-11e9-8f9e-2a86e4085a59"

       }

     }]

   }

```

**Example of an experience variation for a page variation**

```
   {

     "id": "64e93604-78fa-11e9-8f9e-2a86e4085a59",

     "developerName": "PageVariation",

     "type": "experienceVariation",

     "componentVariants": [{

       "id": "4bf0af78-8d73-11e9-bc42-526af7764f64",

       "type": "componentVariant",

       // Route UUID

       "targetId": "c810858e-78fa-11e9-8f9e-2a86e4085a59",

       "propertyOverrides": {

         // View UUID

         "activeViewId": "be9f4760-78fa-11e9-8f9e-2a86e4085a59"

       }

     }]

   }

```

**Example of an experience variation for component visibility**

```
   {

     "id": "64e93604-78fa-11e9-8f9e-2a86e4085a59",

```


Metadata Types ExperienceBundle

```
     "developerName": "ComponentVisibilityVariation",

     "type": "experienceVariation",

     "componentVariants": [{

       "id": "4bf0af78-8d73-11e9-bc42-526af7764f64",

       "type": "componentVariant",

       // Component UUID

       "targetId": "c810858e-78fa-11e9-8f9e-2a86e4085a59",

       "propertyOverrides": {

         "isVisible": true

       }

     }]

   }

```

**Example of a component variation for a CMS Collection component**

```
   {

     "id" : "6ce1260f-cb01-45a0-8947-f2d85602a3db"

     "developerName": "Home_CMS_Collection_Component_Properties",

     "type": "experienceVariation",

     "componentVariants": [{

       "id" : "3gh1260f-cb01-45a0-8947-f2d92037a4db"

       "type": "componentVariant",

       "targetId": "d77369e6-7230-43e7-9b59-6e91c47b3273",

       "propertyOverrides": {

         "componentAttributes": {

   "config/dataProviderDefinition/attributes/dataProviderInfo/apiName":"SilverCollection"

         }

       },

     }],

   }

```

**Example of a component variation for Navigation Menu component**

```
   {

     "id" : "8cf943b8-525d-4c13-a719-6ebc7d61a81e",

     "developerName" : "Default_Navigation_Menu_Component_Properties",

     "type" : "experienceVariation",

     "componentVariants" : [{

       "id" : "5be1260f-cb01-45a0-8947-f2d85602a4db",

       "type" : "componentVariant",

       "targetId" : "fdf9eb51-ddc5-4e79-9ea8-5b94f5ca8db4",

       "propertyOverrides" : {

         "componentAttributes" : {

           "NavigationMenuEditorRefresh" : "NavMenu1"

         }

       },

     }],

   }

```


Metadata Types ExperienceBundle

views Folder

The `views` folder contains several JSON files that each define a view. Each Experience Builder site is built from single-page applications,
which are web apps that load a single HTML page. Single-page applications consist of multiple views that update the page dynamically
as the user interacts with it.

A _view_ is made up of _regions_ that contain other regions or _components_ in the rendered page for the user. Within the `views` folder
there’s one file per view, named _`view_name`_ `.json` .

Note: Single-page applications in your site are defined in the page files of the `config` folder.

```
   view_name .json

```

**Property** **Type** **Description**

`appPageId` UUID Required. Single page application (SPA) page ID of the view. It points to either
`main.json` or `login.json` .

`componentName` string

Required. The FQN of the layout component. The component must implement
`forceCommunity:layout` or, for theme layouts,

```
forceCommunity:themeLayout

```

`id` UUID Required. Represents the GUID of the component.

`label` string Required. The name that appears in **Experience Builder** - **Settings** **Theme**                   - **Configure** .

`themeLayoutType` string Theme layout type of the view (exposed only for views).

`type` string Required. Represents the type of the component. The only supported value is
`view` .

`viewType` string Required. Matches `routeType` for the route.

There are one or more regions as a container in each _`<view_name>`_ `.json`

**region container**

**Property** **Type** **Description**

`id` UUID Required. Represents the component GUID.

`regionLabel` string Specifies region labels for tabs.

Note: This property is present only for tab regions that are children of
a component.

`regionName` string Required. Matches the design attribute in the design file of the layout
component.

`type` string Required. Represents the component type. The only supported value is
`region` .


Metadata Types ExperienceBundle

Each _`<view_name>`_ `.json` file contains a hidden region called `sfdcHiddenRegion` . The hidden region contains a component
that represents the SEO assistant component. In Aura sites, the component’s definition is `forceCommunity:seoAssistant`,
and in LWR sites, the component’s definition is `community_builder:seoAssistant` . This component corresponds to the
SEO page properties that you can configure in Experience Builder and isn’t visible on your pages. To improve search engine results, use
the SEO assistant component to set the `customHeadTags`, `description`, and `pageTitle` properties for your public and
custom site pages. You can’t edit the other properties associated with the SEO assistant component. To learn more about what the title,
[description, and custom head tags properties represent and which head tags are allowed, see SEO Page Properties in Experience Builder.](https://help.salesforce.com/s/articleView?id=experience.networks_seo_tags.htm&type=5&language=en_US)

There are one or more components as a container in the region section of each _`<view_name>`_ `.json`

**component container**

**Property** **Type** **Description**

`componentAttributes` HashMap Required. The design attribute values of the component.

`componentName` string Required. The FQN of the component. Only components that can be used in
the component panel in Experience Builder can be used in this field.

`id` UUID Required. Represents the component GUID.

Note: If you add a component to ExperienceBundle, you can enter any
value because the system automatically generates a UUID for the
component when deployed.

`renderPriority` enums.priority Sets priority value for progressive rendering of the component. Possible Values:
`HIGHEST`, `HIGH`, `NEUTRAL`

Note: Only evaluated if the site has progressive rendering turned on
in **Experience Builder**                                            - **Settings**                                            - **Advanced** .

`renditionMap` HashMap Map of different rendition keys to UUIDs of RenditionComponents.

`scopedBrandingSetID` UUID

Required for LWR sites. Not applicable for Aura sites. Represents the ID of a
branding set for a specific `community_layout:section` component.
Available in API Version 52.0 and later.

`type` string Required. Represents the component type. The only supported value is
`component` .

Each component can have a rendition container in each _`<view_name>`_ `.json`

**rendition container**

**Property** **Type** **Description**

`id` UUID Required. Represents the component GUID.

`renditionValue` map Map of different variations of a component, such as different languages of text.


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`type` string Required. Represents the component type. The only supported value is
`renditionComponent` .

```
   {

      "themeLayoutType" : "Inner",

      "viewType" : "account-management",

      "appPageId" : "df9907cb-6e68-4ca1-8bb2-51173ca5374e",

      "componentName" : "siteforce:sldsOneColLayout",

      "label" : "Account Management",

      "id" : "9ca8fa47-8e87-4915-a6f7-c2d8d37f3076",

      "type" : "view",

      "regions" : [ {

         "regionName" : "content",

         "id" : "969ada98-7d72-4e45-8a10-7db51fae247c",

         "type" : "region",

         "components" : [ {

           "componentName" : "forceCommunity:tabset",

           "componentAttributes" : {

             "tabsetConfig" :

   "{\"UUID\":\"4711850e-ffdc-4375-a45e-f716bcdbbb1c\",\"activeTab\":\"tab1\",

   \"useOverflowMenu\":false,\"tabs\":[{\"UUID\":\"bc8fb51f-4783-43d4-9376-60c07677a367\",\"tabName\":\"Members\",

   \"tabKey\":\"tab1\",\"locked\":false,\"allowGuestUser\":false,\"seedComponents\":[{\"fqn\":\"forceCommunity:relatedList\",

   \"attributes\":{\"parentRecordId\":\"{!CurrentUser.accountId}\",\"relatedListName\":\"Users\",\"customTitle\":\"Members\",

   \"showCustomTitle\":\"true\",\"showBreadCrumbs\":\"false\",\"showRowNumbers\":\"false\",\"showManualRefreshButton\":\"false\"}}]},

   {\"UUID\":\"f2793a99-b757-4be4-846f-dc98a13a8139\",\"tabName\":\"Branding\",\"tabKey\":\"tab2\",\"locked\":false,

   \"allowGuestUser\":false,\"seedComponents\":[{\"fqn\":\"forceCommunity:accountBrandRecord\",

             \"attributes\":{\"recordId\":\"{!CurrentUser.accountId}\"}}]}]}",

             "regions" : ""

           },

           "renderPriority" : "NEUTRAL",

           "renditionMap" : { },

           "id" : "4711850e-ffdc-4375-a45e-f716bcdbbb1c",

           "type" : "component",

           "renditions" : [ {

            "renditionValue" : {

              "LumenInstanceAttributes" : {

              "richTextValue" : "<p>new text</p>"

              }

            },

```


Metadata Types ExperienceBundle

```
            "id" : "9d8878df-f520-4010-861c-57b930a3daab",

            "type" : "renditionComponent"

           } ]

        } ]

      } ]

   }

```

Declarative Metadata Sample Definition

Here’s an example of an ExperienceBundle declaration. For individual folder and file examples for the bundled code, see brandingSets,
config, routes, themes, variations, and views.

```
   <xsd:complexType name="ExperienceBundle">

      <xsd:complexContent>

        <xsd:extension base="tns:Metadata">

           <xsd:sequence>

             <xsd:element name="experienceResources" minOccurs="0"

   type="tns:ExperienceResources"/>

             <xsd:element name="label" type="xsd:string"/>

             <xsd:element name="type" type="tns:SiteType"/>

           </xsd:sequence>

        </xsd:extension>

      </xsd:complexContent>

   </xsd:complexType>

      <xsd:complexType name="ExperienceResources">

        <xsd:sequence>

           <xsd:element name="experienceResource" minOccurs="0" maxOccurs="unbounded"

   type="tns:ExperienceResource"/>

        </xsd:sequence>

      </xsd:complexType>

   <xsd:complexType name="ExperienceResource">

      <xsd:sequence>

        <xsd:element name="fileName" type="xsd:string"/>

        <xsd:element name="format" type="xsd:string"/>

        <xsd:element name="source" minOccurs="0" type="xsd:base64Binary"/>

        <xsd:element name="type" type="xsd:string"/>

      </xsd:sequence>

   </xsd:complexType>

```

Usage

Tip: Before you update the .json files of an Experience Builder site, we recommend making a copy of the site’s folder as a backup.

When you add a component to ExperienceBundle, you can enter any value for the `id`, because the system automatically generates a
UUID for the component when deployed.

When deploying an Experience Builder site with ExperienceBundle, ensure that the SiteDotCom type isn’t included in the manifest file.

ExperienceBundle doesn’t support retrieving and deploying across different API versions. If you’re trying to upgrade ExperienceBundle
metadata from an earlier API version to a later one—for example, from API version 48.0 to 49.0—take the following steps:

**1.** Set the API version in the package.xml manifest file to 48.0 and deploy the package.

**2.** Then, set the API version in package.xml to 49.0.


### Metadata Types ExperiencePropertyTypeBundle (Beta)

**3.** To get the latest ExperienceBundle updates, retrieve the package.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

ExperienceBundleSettings

_Developer Guide:_ [ExperienceBundle for Experience Builder Sites](https://developer.salesforce.com/docs/atlas.en-us.260.0.communities_dev.meta/communities_dev/communities_dev_migrate_expbundle.htm)

### ExperiencePropertyTypeBundle (Beta)

Represents a property type. Replaced in Spring ’26 by the updated LightningPropertyType. When you create a custom property type for
a Lightning web component, use LightningPropertyType instead, and deploy that bundle to your org.

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
[is subject to the applicable Beta Services Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

[To create a custom property type, see LightningPropertyType.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_lightningtypebundle.htm)

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Structure and Directory Location

ExperiencePropertyTypeBundle components are stored in the experiencePropertyTypeBundles folder. Here’s an example of how the
folder is structured.

```
   +--myMetadataPackage

      +--experiencePropertyTypeBundles (1)

        +--addressProperty (2)

           +--schema.json (3)

           +--design.json (4)

```

**•** In the experiencePropertyTypeBundles folder (1) is a folder for each custom property type.

**•** Each custom property type folder is named in the format propertyTypeName. In this example (2), the name is addressProperty.

**•** Each propertyTypeName folder contains a JSON file or files that define the property type.

**–** A `schema.json` file (3), which is a JSON schema that drives the property type validation

**–** An optional `design.json` file (4), which provides the user experience and property editor information for that property type

Version

ExperiencePropertyTypeBundle components are available in API version 58.0 and later.


Metadata Types ExperiencePropertyTypeBundle (Beta)

Special Access Rules

The ExperiencePropertyTypeBundle metadata type is available only for use with Lightning web components on LWR sites.

Fields

**Field Name** **Description**

```
description

masterLabel

resources

```

**Field Type**
string

**Description**
Explanatory text about the property type.

**Field Type**
string

**Description**

Required. A user-friendly name for ExperiencePropertyTypeBundle, which is defined
when the ExperiencePropertyTypeBundle is created.

**Field Type**

ExperiencePropertyTypeBundleResource[]

**Description**
A list of source files in the experiencePropertyTypeBundles folder.

ExperiencePropertyTypeBundleResource

Represents a resource inside ExperiencePropertyTypeBundle.

**Field Name** **Description**

```
fileName

filePath

source

```

**Field Type**
string

**Description**

Required. The file name of the resource.

**Field Type**
string

**Description**

Required. The file path of the resource.

**Field Type**
base64Binary


Metadata Types ExperiencePropertyTypeBundle (Beta)

**Field Name** **Description**

**Description**

Required. The content of the resource.

Declarative Metadata Sample Definition

This `package.xml` file retrieves all the ExperiencePropertyTypeBundle components in an org.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ExperiencePropertyTypeBundle</name>

      </types>

      <version>58.0</version>

   </Package>

```

In the retrieved `.zip` file, each property type is nested under an experiencePropertyTypeBundles folder.

This example shows the directory structure in the `.zip` file of a property type named addressProperty.

```
   experiencePropertyTypeBundles

      addressProperty

        schema.json

        design.json

```

Here are the contents of the files in the addressProperty directory. The addressProperty is a complex type that includes subproperties
for firstName, lastName, address, city, state, and postal code. Each subproperty is a primitive type.

Contents of `schema.json` :

```
   {

    "title": "Simple Address Type",

    "lightning:type": "lightning__objectType",

    "properties": {

     "firstName": {

      "lightning:type": "lightning__textType",

      "title": "First Name"

     },

     "lastName": {

      "lightning:type": "lightning__textType",

      "title": "Last Name"

     },

     "address": {

      "lightning:type": "lightning__textType",

      "title": "Address Line 1"

     },

     "city": {

      "lightning:type": "lightning__textType",

      "title": "City"

     },

     "state": {

      "lightning:type": "lightning__textType",

```


Metadata Types ExperiencePropertyTypeBundle (Beta)

```
      "title": "State"

     },

     "postalCode": {

      "lightning:type": "lightning__numberType",

      "title": "Postal Code"

     }

    },

    "required": ["firstName", "lastName"]

   }

```

Contents of `design.json` (an optional file):

```
   {

    "definition": "lightning/tabsetLayout",

    "children": [

     {

      "definition": "lightning/tabLayout",

      “attributes”: {

        “label”: “First Tab”

      },

      “children”: [

        {

         "definition": "lightning/propertyLayout",

         "attributes": {

          "property": "aProperty"

         }

        },

        {

         "definition": "lightning/propertyLayout",

         "attributes": {

          "property": "bProperty"

         }

        },

      ]

     },

      {

      "definition": "lightning/tabLayout",

      “attributes”: {

        “label”: “Second Tab”

      },

      “children”: [

        {

         "definition": "lightning/propertyLayout",

         "attributes": {

          "property": "cProperty"

         }

        },

      ]

     },

    ]

   }

```


### Metadata Types ExplainabilityMsgTemplate

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

_External Link_ [: Custom Property Types and Property Editors (Beta)](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/custom_property_types_and_editors.pdf)

### ExplainabilityMsgTemplate

Represents information about the template that contains the decision explanation message for a specified expression set step type.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExplainabilityMsgTemplate components have the suffix .explainabilityMsgTemplate and are stored in the ExplainabilityMsgTemplates folder.

Version

### ExplainabilityMsgTemplate components are available in API version 56.0 and later.

Fields

**Field Name** **Description**

```
evaluationResult

expressionSetStepType

```

**Field Type**
EvaluationResult (enumeration of type string)

**Description**

Required.

The type of result for which the message template can be used. The step type for
which the result is evaluated can be a condition, conditional group, or branch.

Valid values are:

**•** `Failed`

**•** `Passed`

**•** `NoResult`

**Field Type**
ExpressionSetStepType (enumeration of type string)


Metadata Types ExplainabilityMsgTemplate

**Field Name** **Description**

**Description**

Required.

The step type in an expression set that uses the explainability message template.

Valid values are:

**•** `Aggregation`

**•** `Branch`

**•** `BusinessElement`

**•** `Calculation`

**•** `Condition`

**•** `DecisionTableLookup`

**•** `ListEnabledGroup`

**•** `ListFilter`

**•** `MatrixLookup`

**•** `ReferenceProcedure`

```
expsSetProcessType

isDefault

```

**Field Type**
ExpsSetProcessType (enumeration of type string)

**Description**

Required.

The type of industry that’s using the expression set.

Valid values are:

**•** `Bre`

**•** `GpaCalculation`

**•** `InsuranceClaimProcessing` —Available in API version 65.0 and later.

**•** `ItServiceManagement` —Available in API version 65.0 and later.

**•** `PlanCostCalculation`

**•** `RatingDiscovery`

**•** `StudentInformationSystem` —Available in API version 65.0 and later.

**•** `StudentSuccess`

When Business Rules Engine is enabled for a Salesforce instance, the default value is
' `Bre` ’. Other process types are available to you depending on your industry solution
and permission sets.

**Field Type**
boolean

**Description**
Indicates whether the decision explainer template for a specified step type is default
(true) or not (false).


Metadata Types ExplainabilityMsgTemplate

**Field Name** **Description**

```
masterLabel

message

```

**Field Type**
string

**Description**

Required.

Master label the for ExplainabilityMsgTemplate.

**Field Type**
string

**Description**

Required.

The message associated with the template for a specific expression set step type.

Declarative Metadata Sample Definition

The following is an example of an ExplainabilityMsgTemplate component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExplainabilityMsgTemplate

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <evaluationResult>Passed</evaluationResult>

 <expressionSetStepType>Condition</expressionSetStepType>

 <expsSetProcessType>ProductQualification</expsSetProcessType>

 <isDefault>false</isDefault>

 <masterLabel>ML EMT testDM</masterLabel>

 <message>EMT Testing</message>

</ExplainabilityMsgTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <types>

  <members>*</members>

  <name>ExplainabilityMsgTemplate</name>

 </types>

 <version>66.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based.htm)


### Metadata Types ExpressionSetDefinition ExpressionSetDefinition

Represents an expression set definition.

[Note: Before deploying an expression set or an expression set version to a target org, review these Expression Set Migration](https://help.salesforce.com/s/articleView?id=ind.considerations_for_migrating_expression_sets.htm&type=5&language=en_US)
[Considerations.](https://help.salesforce.com/s/articleView?id=ind.considerations_for_migrating_expression_sets.htm&type=5&language=en_US)

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExpressionSetDefinition components have the suffix .expressionSetDefinition and are stored in the

`expressionSetDefinition` folder.

Version

### ExpressionSetDefinition components are available in API version 55.0 and later.

Fields

**Field Name** **Description**

```
description

executionScale

interfaceSourceType

```

**Field Type**
string

**Description**
The description of an expression set definition.

**Field Type**
ExpsSetExecutionScale (enumeration of type string)

**Description**
Specifies the scale of the inputs that an expression set processes. The scale determines
where the expression set is executed.

Valid values are:

**•** `High`

**•** `Low`

Available in API version 61.0 and later.

**Field Type**
ExpsSetInterfaceSourceType (enumeration of type string)

**Description**
The interface source type designed by the consuming cloud that's making a customized
expression set builder available to its users.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

Valid values are:

**•** `Constraint` (Available in API version 62.0 and later).

**•** `DiscoveryProcedure` (Available in API version 61.0 and later).

**•** `EventOrchestration` (Available in API version 61.0 and later).

**•** `ItServiceManagement` (Available in API version 65.0 and later).

**•** `PricingProcedure`

**•** `QualificationProcedure`

**•** `RatingDiscoveryProcedure` (Available in API version 61.0 and later).

**•** `Sample`

Available in API version 59.0 and later.

```
label

processType

resourceInitializationType

```

**Field Type**
string

**Description**
Required.

The UI label of an expression set definition.

**Field Type**
ExpsSetProcessType (enumeration of type string)

**Description**
The process type that uses the expression set rule.

Valid values are:

**•** `Bre`

**•** `GpaCalculation`

**•** `InsuranceClaimProcessing` —Available in API version 65.0 and later.

**•** `ItServiceManagement` —Available in API version 65.0 and later.

**•** `PlanCostCalculation`

**•** `RatingDiscovery`

**•** `StudentInformationSystem` —Available in API version 65.0 and later.

**•** `StudentSuccess`

When Business Rules Engine is enabled for a Salesforce instance, the default value is
' `Bre` ’. Other process types are available to you depending on your industry solution
and permission sets.

**Field Type**
ResourceInitializationType (enumeration of type string)

**Description**
Indicates whether the initial value of expression set variables and context tags is null
or a default value.

Valid values are:


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `Default`

**•** `Off`

Available in API version 64.0 and later.

```
template

usageSubType

versions

```

**Field Type**
boolean

**Description**
Defines whether an expression set is a template or not.

**Field Type**
ExpsSetUsageSubType (enumeration of type string)

**Description**
The subtype of the industry that's using the expression set definition. If no value is
specified, the field defaults to null.

**Field Type**

ExpressionSetDefinitionVersion[]

**Description**
Represents an array of expression set version definitions in an expression set.

This array must contain at least one version.

ExpressionSetDefinitionVersion

Represents a definition of an expression set version.

**Field Name** **Description**

```
decimalScale

description

endDate

```

**Field Type**
integer

**Description**
Number of decimal places to be used in the results of calculation steps that involve context
variables.

**Field Type**
string

**Description**
Describes the version of an expression set definition.

**Field Type**
dateTime

**Description**
The date until which the expression set definition is available for use.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
expressionSetDefinition

label

rank

shouldShowExplExternally

startDate

status

```

**Field Type**
string

**Description**
The full name of an expression set definition.

**Field Type**
string

**Description**
Required.

The UI label of an expression set definition.

**Field Type**
int

**Description**
The rank of the `Expression Set Definition Version` . When more than one
enabled version matches an expression set call, and the start date time to end date time
spans overlap, the version with the highest rank is chosen. Available in API version 62.0 and
later.

**Field Type**
boolean

**Description**
Indicates whether the decision explanation is exposed to external users ( `true` ) or not
( `false` ). The default value is `false` . Available in API version 56.0 and later.

**Field Type**
dateTime

**Description**
Required.

The date from when the expression set definition is available for use.

**Field Type**
ExpsSetStatus (enumeration of type string)

**Description**
Required.

The status of an expression set definition.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**•** `InvalidDraft`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `Obsolete`

```
steps

uiTier

variables

versionNumber

```

ExpressionSetStep

**Field Type**

ExpressionSetStep[]

**Description**
Represents an array of steps created in an expression set version.

**Field Type**
boolean

**Description**
Indicates whether the API call originated from the design time builder or a package.

Note: This field is for internal use only.

**Field Type**

ExpressionSetVariable[]

**Description**
Represents an array of variables in an expression set version.

**Field Type**
int

**Description**
Required.

The version number of an expression set definition.

Represents a step in an expression set version.

**Field Name** **Description**

```
actionType

```

**Field Type**
BusinessKnowledgeModel (enumeration of type string)

**Description**
Specifies the type of action this step executes.

Valid values are:

**•** `AiAcceleratorSubscriberChurnPrediction`

**•** `ApexAction`

**•** `ApexListAction` (Available in API version 64.0 and later.)

**•** `AssetDiscovery`

**•** `AssignBadgeToMember`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `AssignParameterValues`

**•** `AssignmentElement`

**•** `AssignmentRuleCustomUser` (Available in API version 65.0 and later.)

**•** `AssignmentRuleCustomQueue` (Available in API version 65.0 and later.)

**•** `AteprlRecordCreator` (Available in API version 65.0 and later.)

**•** `BaseRate`

**•** `BindingObjectRateAdjustmentResolution` (Available in API version 64.0
and later.)

**•** `BindingObjectRateCardEntryResolution` (Available in API version 64.0
and later.)

**•** `BreAggregator`

**•** `BreAggregatorAssignment`

**•** `BreakdownLineMapping` (Available in API version 64.0 and later.)

**•** `CalculateQuantity` (Available in API version 64.0 and later.)

**•** `ChangeMemberTier`

**•** `CheckMemberBadgeAssignment`

**•** `CommercePricing` (Available in API version 62.0 and later.)

**•** `CommitmentAdjustment` (Available in API version 65.0 and later.)

**•** `ComplianceCheck`

**•** `ComplianceControlLog` (Available in API version 62.0 and later.)

**•** `Constraint` (Available in API version 64.0 and later.)

**•** `CreditPoints`

**•** `Crud`

**•** `DebitPoints`

**•** `DerivedPricing`

**•** `DiscountDistributionService`

**•** `DiscoverySettings` (Available in API version 64.0 and later.)

**•** `DynamicRulesExecutor` (Available in API version 65.0 and later.)

**•** `EvaluateCategoryDisqualification` (Available in API version 62.0 and
later.)

**•** `EvaluateCategoryQualification` (Available in API version 62.0 and later.)

**•** `FormulaBasedRating` (Available in API version 62.0 and later.)

**•** `FormulaBasedPricing`

**•** `GetCustomerPromotionAttrValue` (Available in API version 64.0 and later.)

**•** `GetMemberAttributesValues`

**•** `GetMemberPointBalance`

**•** `GetMemberPromotions`

**•** `GetMemberTier`

**•** `GetOutputsFromDecisionMatrix`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `GetOutputsFromDecisionTable`

**•** `GroupingAndAggregateRating` (Available in API version 62.0 and later.)

**•** `IncreaseUsageForCumulativePromotion`

**•** `IntegrationOrchestration`

**•** `IssueExtendedReward` (Available in API version 64.0 and later.)

**•** `IssueVoucher`

**•** `ManualRatingDiscount` (Available in API version 62.0 and later.)

**•** `MapProduct`

**•** `MinimumPrice` (Available in API version 62.0 and later.)

**•** `MultiRecipientProductQualification` (Available in API version 64.0 and
later.)

**•** `NegotiatedBaseRate` (Available in API version 64.0 and later.)

**•** `NegotiatedRateCardEntryResolution` (Available in API version 64.0 and
later.)

**•** `NegotiatedTierAdjustment` (Available in API version 64.0 and later.)

**•** `NegotiatedVolumeAdjustment` (Available in API version 64.0 and later.)

**•** `PriceGuidance` (Available in API version 64.0 and later.)

**•** `PriceRevision` (Available in API version 65.0 and later.)

**•** `PricingPropagation` (Available in API version 65.0 and later.)

**•** `PricingSettings`

**•** `PromotionsDiscount`

**•** `PromotionExecution` (Available in API version 65.0 and later.)

**•** `RateAdjustmentByAttributeResolution` (Available in API version 62.0
and later.)

**•** `RateAdjustmentByTierResolution` (Available in API version 62.0 and later.)

**•** `RateAdjustmentMatrix` (Available in API version 62.0 and later.)

**•** `RateAssignment` (Available in API version 62.0 and later.)

**•** `RateCardEntryResolution` (Available in API version 62.0 and later.)

**•** `RateCardResolution` (Available in API version 62.0 and later.)

**•** `RatingAttributeDiscount`

**•** `RatingBreakdownLineMapping` (Available in API version 65.0 and later.)

**•** `RatingRoundingValues` (Available in API version 62.0 and later.)

**•** `RatingSetting`

**•** `RatingTierDiscount`

**•** `RatingVolumeDiscount`

**•** `RecordAction`

**•** `RoundingValues`

**•** `RuleFetch`

**•** `RunFlow`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `RunProgramProcess`

**•** `SampleCustomElementWithExpressionAndListFilter`

**•** `StopPricing`

**•** `StopRating` (Available in API version 62.0 and later.)

**•** `TermGpaCalculation` (Available in API version 64.0 and later.)

**•** `TermGpaReporting` (Available in API version 64.0 and later.)

**•** `TestCustomElement`

**•** `UpdateCurrentValueForMemberAttribute`

**•** `UpdateCustomerPromotionAttrValue` (Available in API version 64.0 and
later.)

**•** `UpdatePointBalance`

**•** `UpdateUsageForCumulativePromotion`

**•** `UpsertRecord` (Available in API version 64.0 and later.)

**•** `VolumeTierDiscount`

```
advancedCondition

aggregation

assignment

conditionExpression

customElement

```

**Field Type**

ExpressionSetAdvancedCondition

**Description**
Represents an advanced condition step.

**Field Type**

ExpressionSetAggregation

**Description**
Represents an aggregation step.

**Field Type**

ExpressionSetAssignment

**Description**
Represents an assignment step.

**Field Type**

ExpressionSetConditionExpression

**Description**
Represents a condition step.

**Field Type**

ExpressionSetCustomElement

**Description**
Represents a custom element step that contains the input and output mappings. Available
in API version 56.0 and later.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
decisionTable

description

failedExplainerTemplate

failedMessageTokenMappings

label

name

noResultExplainerTemplate

```

**Field Type**

ExpressionSetDecisionTable

**Description**
Represents a decision matrix or decision table step.

**Field Type**
string

**Description**
Describes an expression set definition version step.

**Field Type**
string

**Description**

The explainability message template that’s used when the result type of a condition step
in an expression set is Failed.

**Field Type**
ExplainabilityMessageTemplateTokenMapping (enumeration of type string)

**Description**

List of the token resource mappings of the failed explainability message template. Valid
values are:

**•** `expressionSetMessageToken`

**•** `resourceReference`

Available in API version 59.0 and later.

**Field Type**
string

**Description**
Required.

The UI label of an expression set definition version step.

**Field Type**
string

**Description**
Required.

The full name of an expression set definition version step.

**Field Type**
string


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**Description**

The explainability message template that’s used when the result type of a condition step
in an expression set is No Result. Available in API version 59.0 and later.

```
noResultMessageTokenMappings

parentStep

passedExplainerTemplate

passedMessageTokenMappings

resultIncluded

```

**Field Type**
ExplainabilityMessageTemplateTokenMapping (enumeration of type string)

**Description**

List of the token resource mappings of the no result explainability message template. Valid
values are:

**•** `expressionSetMessageToken`

**•** `resourceReference`

Available in API version 59.0 and later.

**Field Type**
string

**Description**

The name of the parent step in an expression set definition version that’s associated with
a step.

**Field Type**
string

**Description**

The explainability message template that’s used when the result type of a condition step
in an expression set is Passed.

**Field Type**
ExplainabilityMessageTemplateTokenMapping (enumeration of type string)

**Description**

List of the token resource mappings of the passed explainability message template. Valid
values are:

**•** `expressionSetMessageToken`

**•** `resourceReference`

Available in API version 59.0 and later.

**Field Type**
boolean

**Description**

Indicates whether the step output must be included in the expression result (true) or not
(false).


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
sequenceNumber

shouldExposExecPathMsgOnly

shouldExposeConditionDetails

shouldShowExplExternally

stepType

subExpression

```

**Field Type**
int

**Description**
Required.

The sequence number of a step in an expression set definition version.

**Field Type**
boolean

**Description**
Indicates whether the message in the explainability message template is exposed for only
the branch path that was run.

**Field Type**
boolean

**Description**
Indicates whether the details of the condition are shown in the decision explanation.

**Field Type**
boolean

**Description**
Indicates whether the decision explanations are shown to external users.

**Field Type**
ExpsSetStepType (enumeration of type string)

**Description**
Required.

Specifies the type of step in an expression set definition version.

Valid values are:

**•** `AdvancedCondition`

**•** `Branch`

**•** `BusinessKnowledgeModel`

**•** `Condition`

**•** `DefaultPath`

**•** `SubExpression`

**Field Type**

ExpressionSetSubExpression

**Description**
Represents a sub expression step.


Metadata Types ExpressionSetDefinition

ExpressionSetAdvancedCondition

Represents an advanced condition step.

**Field Name** **Description**

```
conditionLogic

criteria

errorMessage

resultParameter

successMessage

```

**Field Type**
string

**Description**
Required.

The condition that’s defined for an advanced condition.

**Field Type**

ExpressionSetConditionCriteria []

**Description**
Represents an array of criteria defined in the advanced condition.

**Field Type**
string

**Description**
An error message for a failed advanced condition.

**Field Type**
string

**Description**
An expression set definition version variable associated with the result of a step.

**Field Type**
string

**Description**
A success message for a successful advanced condition.

ExpressionSetConditionCriteria

Represents a criterion defined in an advanced condition.

**Field Name** **Description**

```
operator

```

**Field Type**
ExpsSetConditionOperator (enumeration of type string)

**Description**
Required.

Specifies the operator for evaluating an expression.

Valid values are:


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `Contains`

**•** `DoesNotContain`

**•** `Equals`

**•** `GreaterThan`

**•** `GreaterThanOrEquals`

**•** `IsNull`

**•** `IsNotNull`

**•** `LessThan`

**•** `LessThanOrEquals`

**•** `NoEquals`

```
sequenceNumber

sourceFieldName

value

valueType

```

**Field Type**
int

**Description**
Required.

The position of the condition in a step that contains multiple conditions.

**Field Type**
string

**Description**
Required.

The expression set definition version variable associated with the result of a condition
criterion.

**Field Type**
string

**Description**
Specifies the condition of a criterion.

**Field Type**
ExpsSetValueType (enumeration of type string)

**Description**
Specifies the type of value.

Valid values are:

**•** `Formula`

**•** `Literal`

**•** `Lookup`

**•** `Parameter`

**•** `Picklist`


Metadata Types ExpressionSetDefinition

ExpressionSetAggregation

Represents an aggregation step.

**Field Name** **Description**

```
aggregatedParameter

aggregateFunction

expression

```

**Field Type**
string

**Description**
Required.

The expression set definition version variable associated with the result of a condition
criterion.

**Field Type**
ExpsSetAggregationFunction (enumeration of type string)

**Description**
Required.

Specifies the aggregation function used in a step.

Valid values are:

**•** `Avg`

**•** `Max`

**•** `Min`

**•** `Sum`

**Field Type**
string

**Description**
Required.

Specifies the expression of an aggregation.

ExpressionSetAssignment

Represents an assignment step.

**Field Name** **Description**

```
aggregatedParameter

```

**Field Type**
string

**Description**
Required.

The expression set definition version variable associated with a step detail.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
expression

```

**Field Type**
string

**Description**
Required.

The expression that’s defined for a step.

ExpressionSetConditionExpression

Represents a condition in a condition step.

**Field Name** **Description**

```
errorMessage

expression

resultParameter

successMessage

```

**Field Type**
string

**Description**
An error message for a failed condition.

**Field Type**
string

**Description**
Required.

The expression that’s defined for a step.

**Field Type**
string

**Description**
The expression set definition version variable associated with the result of a step.

**Field Type**
string

**Description**
A success message for a successful condition.

ExpressionSetCustomElement

Represents a custom element in an expression set. Available in API version 56.0 and later.

**Field Name** **Description**

```
parameters

```

**Field Type**

ExpressionSetElementParameter[]


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**Description**
Represents the list of parameters in the custom element.

ExpressionSetElementParameter

Represents a parameter within a custom element of an expression set. Available in API version 56.0 and later.

**Field Name** **Description**

```
input

name

output

type

```

**Field Type**
boolean

**Description**

Required.

Indicates whether the custom element parameter is input ( `true` ) or not ( `false` ).

The default value is `true` .

**Field Type**
string

**Description**

Required.

The name of the custom element parameter.

**Field Type**
boolean

**Description**

Required.

Indicates whether the custom element parameter is output ( `true` ) or not ( `false` ).

The default value is `true` .

**Field Type**
ExpsSetValueType (enumeration of type string)

**Description**
The type of custom element parameter.

Values are:

**•** `Formula`

**•** `Literal`

**•** `Lookup`

**•** `Parameter`

**•** `PickList`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

The default value is `Parameter` .

```
value

```

**Field Type**
string

**Description**

Required.

The name of the expression set variable.

ExpressionSetDecisionTable

Represents a decision table or decision matrix in a step.

**Field Name** **Description**

```
decisionTableName

mappings

type

```

**Field Type**
string

**Description**
Required.

The decision matrix or decision table name used in a step.

**Field Type**

ExpressionSetElementParameter[]

**Description**
The mapping information between various parameters in an ExpressionSetDecisionTable.

Available in API version 59.0 and later.

**Field Type**
string

**Description**
Required.

The type in a step. It can be a decision table or decision matrix.

ExpressionSetSubExpression

Represents a sub expression in a step.

**Field Name** **Description**

```
expressionSet

```

**Field Type**
string


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**Description**
Required.

The sub expression name used in a step.

```
mappings

```

**Field Type**

ExpressionSetElementParameter[]

**Description**
The mapping information between various parameters in an ExpressionSetDecisionTable.

Available in API version 61.0 and later.

ExpressionSetVariable

Represents a definition of an expression set variable.

**Field Name** **Description**

```
collection

dataType

```

**Field Type**
boolean

**Description**
Indicates whether a variable stores a collection of values ( `true` ) or not ( `false` ).

**Field Type**
ExpsSetDataType (enumeration of type string)

**Description**
Required.

The data type of an expression set variable.

Valid values are:

**•** `ActionOutput`

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `DecisionMatrix`

**•** `DecisionTable`

**•** `Numeric`

**•** `Percent`

**•** `Sobject`

**•** `SubExpression`

**•** `Text`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
decimalPlaces

description

fields

input

lookupName

lookupType

name

```

**Field Type**
int

**Description**
The decimal digits in the currency, number, or percent data type for an expression set
variable.

**Field Type**
string

**Description**
The description of the variable used in an expression set.

**Field Type**

ExpressionSetVariableField []

**Description**
Represents an array of fields in an object that is used as a variable in an expression set.

**Field Type**
boolean

**Description**
Indicates whether an expression set variable is used as an input ( `true` ) in an expression
or not ( `false` ).

**Field Type**
string

**Description**
The API name of a decision matrix, a decision table, or a sub expression.

**Field Type**
ExpsSetVariableLookupType (enumeration of type string)

**Description**
The type of the lookup used in an expression set definition.

Valid values are:

**•** `DecisionMatrix`

**•** `DecisionTable`

**•** `SubExpression`

**Field Type**
string

**Description**
Required.

The full name of the variable used in an expression set definition.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
objectName

output

resultStep

type

value

```

**Field Type**
string

**Description**
The name of the sObject.

**Field Type**
boolean

**Description**
Indicates whether an expression set variable is used as an output in an expression( `true` )
or not ( `false` ).

**Field Type**
string

**Description**
The step that produces the expression set variable.

**Field Type**
ExpsSetVariableType (enumeration of type string)

**Description**
Required.

The type of variable in an expression set definition.

Valid values are:

**•** `Constant`

**•** `ContextDynamicAttributeTag` (Available in API version 62.0 and later.)

**•** `ExecutableContextDefinitionTag` (Available in API version 62.0 and later.)

**•** `Formula`

**•** `Variable`

**Field Type**
string

**Description**
Represents a constant value or a formula.

Note: It stores the default value of a variable.

ExpressionSetVariableField

Represents a definition of a field in an object that is used as a variable in an expression set.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
dataType

decimalPlaces

fields

lookupName

lookupType

```

**Field Type**
ExpsSetDataType (enumeration of type string)

**Description**
Required.

Specifies the type of data stored in an expression set variable.

Valid values are:

**•** `ActionOutput`

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `DecisionMatrix`

**•** `DecisionTable`

**•** `Numeric`

**•** `Percent`

**•** `Sobject`

**•** `SubExpression`

**•** `Text`

**Field Type**
int

**Description**
The decimal digits in the currency, number, or percent data type for an expression set
variable.

**Field Type**

ExpressionSetVariableField []

**Description**
Represents an array of fields in an object that is used as a variable in an expression set.

**Field Type**
string

**Description**
The API name of a decision matrix, a decision table, or a sub expression.

**Field Type**
ExpsSetVariableLookupType (enumeration of type string)

**Description**
Required.

The type of lookup used in an expression set definition.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

Valid values are:

**•** `DecisionMatrix`

**•** `DecisionTable`

**•** `SubExpression`

```
name

objectName

```

**Field Type**
string

**Description**
Required.

The full name of the field used in an expression set variable.

**Field Type**
string

**Description**
The name of the sObject.

Declarative Metadata Sample Definition

The following is an example of an ExpressionSetDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExpressionSetDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <label>ExpSetWithAllSteps</label>

   <processType>Bre</processType>

   <template>false</template>

   <description></description>

   <interfaceSourceType>Sample</interfaceSourceType>

   <executionScale>Low</executionScale>

   <versions>

     <fullName>ExpSetWithAllSteps_V1</fullName>

     <expressionSetDefinition>ExpSetWithAllSteps</expressionSetDefinition>

     <label>ExpSetWithAllSteps V1</label>

     <shouldShowExplExternally>false</shouldShowExplExternally>

     <startDate>2022-08-09T22:04:56.000Z</startDate>

     <endDate>2023-08-09T22:04:56.000Z</endDate>

     <status>Draft</status>

     <uiTier>false</uiTier>

     <rank>1</rank>

     <description>ExpSetWithAllSteps_V1</description>

     <steps>

        <description>Aggregate</description>

        <actionType>BreAggregator</actionType>

        <aggregation>

          <aggergatedParameter>result</aggergatedParameter>

          <aggregateFunction>Avg</aggregateFunction>

          <expression>AVG ( result )</expression>

        </aggregation>

```


Metadata Types ExpressionSetDefinition

```
           <label>Aggregate</label>

           <name>Aggregate</name>

           <resultIncluded>true</resultIncluded>

           <sequenceNumber>5</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <steps>

           <label>Branch</label>

           <name>Branch</name>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>4</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>Branch</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

           <assignment>

             <assignedParameter>b</assignedParameter>

             <expression>SUM ( a, 10 )</expression>

           </assignment>

           <label>Calculation</label>

           <name>Calculation</name>

           <resultIncluded>true</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

           <assignment>

             <assignedParameter>result</assignedParameter>

             <expression>b * 100</expression>

           </assignment>

           <label>Calculation</label>

           <name>Calculation10</name>

           <parentStep>DefaultLane</parentStep>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

           <assignment>

             <assignedParameter>result</assignedParameter>

```


Metadata Types ExpressionSetDefinition

```
             <expression>b * 1</expression>

           </assignment>

           <label>Calculation</label>

           <name>Calculation3</name>

           <parentStep>Condition</parentStep>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

           <assignment>

             <assignedParameter>result</assignedParameter>

             <expression>SUM ( b, 10 )</expression>

           </assignment>

           <label>Calculation</label>

           <name>Calculation5</name>

           <parentStep>Condition4</parentStep>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

           <assignment>

