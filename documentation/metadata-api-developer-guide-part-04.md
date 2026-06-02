Represents how records open in a Salesforce console app. Required if isServiceCloudConsole `is true` . Available for Salesforce Classic
console apps in API version 25.0 and later. Available for Lightning console apps in API version 41.0 and later. In API version 42.0, this type
was renamed from WorkspaceMappings to AppWorkspaceConfig.

**Field Name** **Field Type** **Description**

`mappings` WorkspaceMappingSingle[] `Represents how records for a specific tab open`

```
                        in a Salesforce console app. Required for each

                        tab specified in the
```

`CustomApplication.workspaceMapping` to `mappings` .

WorkspaceMapping

Represents how records for a specific tab open in a Salesforce console app. Required for each tab specified in the CustomApplication.
Available in API version 25.0 and later for Salesforce Classic console apps. Available in API version 41.0 and later for Lightning console
apps.

**Field Name** **Field Type** **Description**

`fieldName` string The name of the field that specifies the primary tab in which to display
`tab` as a subtab. If not specified, `tab` opens as a primary tab.

`tab` string Required. Name of the tab.


Metadata Types CustomApplication

CustomShortcut

Represents custom keyboard shortcuts assigned to a Salesforce console app in Salesforce Classic. Before you can create custom shortcuts,
a developer must define the shortcut’s action with the `addEventListener()` method in the Salesforce Console Integration Toolkit.
You can’t create keyboard shortcuts for actions performed outside of the console. Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`action` string Required. The action performed in the console when a user presses the
keyboard shortcut.

`active` boolean Required. Indicates whether the keyboard shortcut is active ( `true` ) or
not ( `false` ).

`keyCommand` string Required. The combination of keys a user presses to trigger the keyboard
shortcut. Keyboard shortcuts aren’t case-sensitive, but they display as

uppercase on setup pages in the Salesforce user interface so that they’re
easier to read.

Each key command can include up to four modifier keys followed by one
non-modifier key. Modifier and non-modifier keys are separated by the
`+` key. Modifier keys can occur in any order, but you must place
non-modifier keys at the end of the key command sequence. For example,
`SHIFT+CTRL+ALT+META +A` .

Valid modifier keys are:

**•** `SHIFT`

**•** `CTRL`

**•** `ALT`

**•** `META` (represents the COMMAND key on Macs)

Valid non-modifier keys are letters A through Z and numbers 0 through
9. Other valid keys are:

**•** `TAB`

**•** `ENTER`

**•** `PAUSE/BREAK`

**•** `CAPS LOCK`

**•** `ESC`

**•** `SPACE`

**•** `PAGE UP`

**•** `PAGE DOWN`

**•** `END`

**•** `HOME`

**•** `LEFT ARROW`

**•** `UP ARROW`

**•** `RIGHT ARROW`

**•** `DOWN ARROW`


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

**•** `PRINT SCREEN`

**•** `INSERT`

**•** `DELETE`

**•** `RIGHT WINDOW`

**•** `NUMPAD 0`

**•** `NUMPAD 1`

**•** `NUMPAD 2`

**•** `NUMPAD 3`

**•** `NUMPAD 4`

**•** `NUMPAD 5`

**•** `NUMPAD 6`

**•** `NUMPAD 7`

**•** `NUMPAD 8`

**•** `NUMPAD 9`

**•** `MULTIPLY`

**•** `ADD`

**•** `SUBTRACT`

**•** `DECIMAL POINT`

**•** `DIVIDE`

**•** `F1`

**•** `F2`

**•** `F3`

**•** `F4`

**•** `F5`

**•** `F6`

**•** `F7`

**•** `F8`

**•** `F9`

**•** `F10`

**•** `F11`

**•** `F12`

**•** `NUM LOCK`

**•** `SCROLL LOCK`

**•** `;`

**•** `=`

**•** `,`

**•** `—`

**•** `.`


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

**•** `/`

**•** `‘`

**•** `[`

**•** `]`

**•** `\`

**•** `'`

`description` string The optional description text for the keyboard shortcut.

`eventName` string Required. Code available to developers who want to add custom shortcut
functions to the console via the Salesforce Console Integration Toolkit.

DefaultShortcut

Represents default keyboard shortcuts assigned to a Salesforce console app. After you enable keyboard shortcuts for a console, several
default shortcuts are available for customization. These include opening and closing tabs, moving between tabs, and saving records.
Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`action` string Required. The action performed in the console when a user presses the
keyboard shortcut. Valid values are:

**•** `FOCUS_CONSOLE`

**•** `FOCUS_NAVIGATOR_TAB`

**•** `FOCUS_DETAIL_VIEW`

**•** `FOCUS_PRIMARY_TAB_PANEL`

**•** `FOCUS_SUBTAB_PANEL`

**•** `FOCUS_LIST_VIEW`

**•** `FOCUS_FIRST_LIST_VIEW`

**•** `FOCUS_SEARCH_INPUT`

**•** `MOVE_LEFT`

**•** `MOVE_RIGHT`

**•** `UP_ARROW`

**•** `DOWN_ARROW`

**•** `OPEN_TAB_SCROLLER_MENU`

**•** `OPEN_TAB`

**•** `CLOSE_TAB`

**•** `ENTER`

**•** `EDIT`

**•** `SAVE`


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`active` boolean Required. Indicates whether the keyboard shortcut is active ( `true` ) or
not ( `false` ).

`keyCommand` string

KeyboardShortcuts

Each key command can include up to four modifier keys followed by one
non-modifier key. Modifier and non-modifier keys are separated by the

`+` key. Modifier keys can occur in any order, but you must place
non-modifier keys at the end of the key command sequence. For example,
`SHIFT+CTRL+ALT+META +A` .

Represents keyboard shortcuts assigned to a Salesforce console app. Required if `isServiceCloudConsole` is `true` . Available
in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`customShortcuts` CustomShortcut[]

`addEventListener()` method in the Salesforce Console Integration
Toolkit. You can’t create keyboard shortcuts for actions performed outside
of the console.

Represents custom keyboard shortcuts assigned to a Salesforce console
app in Salesforce Classic. Before you can create custom shortcuts, a

developer must define the shortcut’s action with the In API version 42.0,
this field was renamed from `customShortcut` to
`customShortcuts` .

`defaultShortcuts` DefaultShortcut[] Represents default keyboard shortcuts assigned to a Salesforce console
app. After you enable keyboard shortcuts for a console, several default

shortcuts are available for customization. These include opening and
closing tabs, moving between tabs, and saving records.In API version
42.0, this field was renamed from `defaultShortcut` to
`defaultShortcuts` .

ListPlacement

Represents how lists display in a Salesforce console app. Required if `isServiceCloudConsole` is `true` . Available in API version
25.0 and later.

**Field Name** **Field Type** **Description**

`height` int Height of the list in pixels or percentage. Required if `location` is top.

`location` string Required. Location of the list on the screen. Valid values are:

**•** full

**•** top

**•** left


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`units` string Required. Represents if `height` or `width` is in pixels or percentage.

`width` int Width of the list in pixels or percentage. Required if `location` is left.

LiveAgentConfig

Represents your organization's settings for using Chat in the Salesforce Console.

**Field Name** **Field Type** **Description**

`enableLiveChat` boolean Specifies whether Chat is enabled in your organization ( `true` ) or not
( `false` ).

`openNewAccountSubtab` boolean

Specifies whether to open a new Account subtab in a Salesforce console
app automatically ( `true` ) or not ( `false` ) when an agent accepts a
chat.

`openNewCaseSubtab` boolean Specifies whether to open a new Case subtab in a Salesforce console app
automatically ( `true` ) or not ( `false` ) when an agent accepts a chat.

`openNewContactSubtab` boolean

`openNewLeadSubtab` boolean

`openNewVFPageSubtab` boolean

`pageNamesToOpen` string [array of strings]

Specifies whether to open a new Contact subtab in a Salesforce console
app automatically ( `true` ) or not ( `false` ) when an agent accepts a
chat.

Specifies whether to open a new Lead subtab in a Salesforce console
app automatically ( `true` ) or not ( `false` ) when an agent accepts a
chat.

Specifies whether to open a new Visualforce page as a subtab in a
Salesforce console app automatically ( `true` ) or not ( `false` ) when an
agent accepts a chat.

Specifies the Visualforce pages to open in subtabs when an agent accepts
a chat in a Salesforce console app.

This field is available in API version 42.0 and later.

`showKnowledgeArticles` boolean Specifies whether to display the Knowledge component while using
Chat in a Salesforce console app ( `true` ) or not ( `false` ).

PushNotification

Represents a set of push notifications, which are visual indicators on lists and detail pages that show when a record or field has changed
during a user’s session. Available for use if `isServiceCloudConsole` is `true` . Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`fieldNames` string] The name of the field or fields that trigger push notifications for the
selected object.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`objectName` string Required. Name of the object that triggers push notifications.

ServiceCloudConsoleConfig

Represents configuration settings for a Salesforce console app. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`componentList` AppComponentList Represents custom console components (Visualforce pages) assigned to
a Salesforce console app.

`detailPageRefreshMethod` string Determines how detail pages refresh in a Salesforce console app. Required
if `isServiceCloudConsole` is `true` . The valid values are:

**•** `none`

**•** `autoRefresh`

**•** `flag`

`footerColor` string Determines the footer color in a Salesforce console app.Specify the color
with a hexadecimal code, such as #0000FF for blue.

`headerColor` string Specify the color with a hexadecimal code, such as #0000FF for
blue.Determines the header color in a Salesforce console app.

`keyboardShortcuts` KeyboardShortcuts

Represents the keyboard shortcuts for a Salesforce console app. Keyboard
shortcuts let users perform actions by pressing a combination of keys
instead of having to use a mouse.

`listPlacement` ListPlacement Represents how lists display in a Salesforce console app. Required if
`isServiceCloudConsole` is `true` .

`listRefreshMethod` string Determines how lists refresh in a Salesforce console app. Required if
`isServiceCloudConsole` is `true` . The valid values are:

**•** `none`

**•** `refreshList`

**•** `refreshListRows`

`liveAgentConfig` LiveAgentConfig Represents the configurations for using Chat in the Salesforce Console.

`primaryTabColor` string Determines the primary tab color in a Salesforce console app.Specify the
color with a hexadecimal code, such as #0000FF for blue.

`pushNotifications` PushNotification[] Represents push notifications for a Salesforce console app. Push
notifications are visual indicators on lists and detail pages that show when

a record or field has changed during a user’s session. For example, assume
that two support agents are working on the same case. If one agent
changes the `Priority`, a push notification displays to the other agent
so the agent notices the change and doesn’t duplicate the effort.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`tabLimitConfig` TabLimitConfig

Represents the maximum number of primary tabs and subtabs allowed
in one Salesforce console session. Required if `enableTabLimits` is
`true` .

`whiteListedDomains` string[] Any external domains that users can access from within a Salesforce
console app. For example, `www.yourdomain.com` .

TabLimitConfig

Represents the maximum number of primary tabs and subtabs allowed in one Salesforce console session. Required if
`enableTabLimits` is `true` .

**Field Name** **Field Type** **Description**

`maxNumberOfPrimaryTabs` string The maximum number of primary tabs allowed in one console session.
Valid values are:

**•** 5

**•** 10

**•** 20

**•** 30

`maxNumberOfSubTabs` string The maximum number of subtabs allowed in one console session. Valid
values are:

**•** 5

**•** 10

**•** 15

Usage

You can't delete custom app ProfileActionOverrides by deploying with `destructiveChange.xml` . To delete a ProfileActionOverride,
retrieve the app. In the app definition file, find the `<profileActionOverrides>` section, and remove the `<content>` row.
Then, change the `<type>` value in that same section to `default` instead of `flexipage` . Do this for every override you want to
reset. After making the changes, rezip the folder and deploy.

You can remove one override at a time each with its own deploy, or you can remove multiple overrides in a single deploy. However, we
recommend that you do a fresh retrieve every time you want to delete a new override. Don’t use a previously retrieved file.

Retrieving Apps

To retrieve apps in your organization, use the CustomApplication type name in the `package.xml` manifest file. You can either retrieve
all apps or specify which apps to retrieve in the types section of `package.xml` .


Metadata Types CustomApplication

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

        <actionName>View</actionName>

        <comment>Action override created by Lightning App Builder during

   activation.</comment>

        <content>Custom_Mobile_Oppty_Page</content>

        <formFactor>Large</formFactor>

```


Metadata Types CustomApplication

```
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

      <label>Collaboration</label>

      <tabs>standard-Chatter</tabs>

      <tabs>standard-UserProfile</tabs>

      <tabs>standard-OtherUserProfile</tabs>

      <tabs>standard-CollaborationGroup</tabs>

```


Metadata Types CustomApplication

```
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

             <action>FOCUS_LIST_VIEW</action>

             <active>true</active>

             <keyCommand>N</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

```


Metadata Types CustomApplication

```
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

           <defaultShortcuts>

             <action>EDIT</action>

             <active>true</active>

             <keyCommand>E</keyCommand>

           </defaultShortcuts>

```


Metadata Types CustomApplication

```
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

           <tab>standard-Contact</tab>

        </mappings>

        <mappings>

           <tab>standard-Contract</tab>

        </mappings>

```


### Metadata Types CustomApplicationComponent

```
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

`isHidden` boolean Required. Indicates whether the custom console component is hidden
from users ( `true` ) or not ( `false` ).

`isWidthFixed` boolean Required. Indicates whether users can change the component width
( `false` ) or not ( `true` ).


### Metadata Types CustomFeedFilter

**Field Name** **Field Type** **Description**

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

Version

### CustomFeedFilter components are available in API version 35.0 and later.


Metadata Types CustomFeedFilter

Fields

**Field Name** **Field Type** **Description**

`criteria` FeedFilterCriterion The criterion that defines which feed items are shown when the filter is
on page 729 [] applied. The feed filter displays all feed items that satisfy the criteria.

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

`feedItemVisibility` FeedItemVisibility (enumeration of
type string)


The visibility of feed items that the filter shows. For
example, you can show only poll posts that are visible
internally.

Valid values are:

**•** AllUsers

Metadata Types CustomFeedFilter

**Field Name** **Field Type** **Description**

**•** InternalUsers

`relatedSObjectType` string

Declarative Metadata Sample Definition

The following is an example of a CustomFeedFilter on page 728 component.

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

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types CustomFieldDisplay CustomFieldDisplay

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

 <displayType>Pill</displayType>

 <isProtected>false</isProtected>

</CustomFieldDisplay>

```


### Metadata Types CustomHelpMenuSection

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

CustomHelpMenuItems

Items included in the custom section. Specify up to 15 items.

Required. Name of the custom section. Only one custom section
can be added to the Lightning Experience help menu. Specify up
to 80 characters.


### Metadata Types CustomIndex

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

File Suffix and Directory Location

### CustomIndex components have the suffix .indx-meta and are stored in the customindex folder.


### Metadata Types CustomLabels

Version

CustomIndex is available in API versions 50.0 and later.

Special Access Rules

[To use this metadata and create a custom index, review Indexes in](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_large_data_volumes_bp.meta/salesforce_large_data_volumes_bp/ldv_deployments_infrastructure_indexes.htm) _Best Practices for Deployments with Large Data Volumes_, and then
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

Declarative Metadata File Suffix and Directory Location

### Master custom label values are stored in the CustomLabels.labels file. Translations for custom labels can be retrieved through

Translations in Metadata API. Translations are stored in files under the `translations` folder with the name format of


Metadata Types CustomLabels

_`localeCode`_ `.translation`, where _`localeCode`_ is the locale code of the translation language. The supported locale codes
are listed in Language on page 2426.

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

`value` string Required. The translated custom label. Maximum of 1000
characters.


Metadata Types CustomLabels

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

       <name>CustomLabel</name>

      </types>

      <version>66.0</version>

   </Package>

```


### Metadata Types Custom Metadata Types (CustomObject)

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

Note: Audit fields ( `CreatedDate`, `CreatedBy`, `LastModifiedDate`, `LastModifiedBy`, `SystemModStamp` )
remain uneditable.

Fields

Custom metadata types can contain the following CustomObject fields.


Metadata Types Custom Metadata Types (CustomObject)

To make the fields on your custom metadata types unique and indexable, mark your fields as `Unique` and `ExternalId` .

Declarative Metadata Sample Definition

In this example, Picklists R Us creates its Reusable Picklist custom metadata type by deploying a file in the objects folder, named
`ReusablePicklistOption__mdt.object`, with these contents.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

  <fields>

```


#### Metadata Types CustomMetadata

```
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

#### 1. CustomMetadata

Represents a record of a custom metadata type.

#### CustomMetadata

Represents a record of a custom metadata type.


Metadata Types CustomMetadata

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

CustomMetadata components have the suffix `.md` and are stored in the `customMetadata` folder. Unlike custom metadata types,
custom metadata records don’t have a double-underscore suffix. Custom metadata record names are prepended with their custom
metadata type name, excluding the `__mdt` suffix but including the namespace of any types in an installed managed package.

Version

CustomMetadata components are available in API version 31.0 and later.

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

**•** Code that the subscriber creates and code that’s in
an unmanaged package can’t read the protected
records.

**•** The developer can modify protected records with a
package upgrade or by using the Metadata Apex
classes (if the Apex code is in the same namespace
as either the records or their type). The subscriber
can’t read or modify protected records. The developer


Metadata Types CustomMetadata

**Field Name** **Field Type** **Description**

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

```


Metadata Types CustomMetadata

```
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

```


Metadata Types CustomMetadata

```
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

       <members>

         picklist1234__PicklistUsage.DestinationPlanetPL

       </members>

       <members>picklist1234__PicklistUsage.PlanetVisitedPl</members>

       <name>CustomMetadata</name>

     </types>

   …

   </package>

```


Metadata Types CustomMetadata

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

`xsi:type="xsd:string"` Text

`xsi:type="xsd:string"` Phone

`xsi:type="xsd:string"` TextArea

`xsi:type="xsd:string"` URL

`xsi:type="xsd:string"` Email


### Metadata Types CustomNotificationType

**Custom metadata value** **Custom field definition**

`xsi:type="xsd:int"` Number/Percent, with scale equal to 0

`xsi:type="xsd:double"` Number/Percent, with scale not equal to 0

You can also omit the `xsi:type` attribute. For example, `<value>true</value>` .

Although this attribute must be specified for any CustomMetadataValue, you can use an element with the `xsi:nil` attribute set to
`true` to explicitly set the field’s value to `null` . For example, `<value` `xsi:nil="true"/>` .

Using `null` field values differs from leaving out the for a particular field entirely. If you leave out the, the value of the field doesn’t
change. The field’s value is `null` for newly deployed custom metadata records and left at its previous value for updated custom
metadata records.

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

Version

### CustomNotificationType components are available in API version 46.0 and later.


Metadata Types CustomNotificationType

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

**Description**

Required.

Unique name of the mobile action group.


Metadata Types CustomNotificationType

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

**•** `Share` : Client-side action where the app shares notification content to any
channel.

Declarative Metadata Sample Definition

The following is a definition of a custom notification type that is enabled for desktop and mobile.

```
<CustomNotificationType xmlns="http://soap.sforce.com/2006/04/metadata">

   <customNotifTypeName>Custom Notification</customNotifTypeName>

```


### Metadata Types CustomObject

```
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
[on Standard Objects in Sample package.xml Manifest Files in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/manifest_samples.htm) _Metadata API Developer Guide_

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

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Version

Custom objects are available in API version 10.0 and later. External objects are available in API version 32.0 and later.

Fields

Unless otherwise noted, all fields are creatable, filterable, and nillable.


Metadata Types CustomObject

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

`customSettingsVisibility` CustomSettingsVisibility
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

This field is available in API version 17.0 and later.

When this field is present, this component isn’t a custom
object, but a custom setting. This field returns the visibility of
the custom setting. The following string values are valid:

**•** `Public` —if the custom setting is packaged, it’s
accessible to all subscribing orgs.

**•** `Protected` —if the custom setting is in a managed
package, it’s accessible only to the developer org.
Subscribing orgs can’t access it. This value is the default.

Metadata Types CustomObject

**Field Name** **Field Type** **Description**

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
or not ( `false` [). See Division in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_division.htm) _Salesforce Object Reference_ .
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
For more information about enhanced lookups, see “Enable
Enhanced Lookups” in Salesforce Help.

`enableFeeds` boolean

Indicates whether the object is enabled for feed tracking
( `true` ) or not ( `false` ). For more information, see “Customize
Chatter Feed Tracking” in Salesforce Help.

This field is available in API version 18.0 and later.

`enableHistory` boolean Indicates whether the object is enabled for history tracking
( `true` ) or not ( `false` ). Also available for standard objects


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

in API version 29.0 and later. History tracking on the Account
object includes person account history tracking.

`enableLicensing` boolean

`enableReports` boolean

`enableSearch` boolean

`enableSharing` boolean

`enableStreamingApi` boolean

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


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

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


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

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

`pluralLabel` string

Required for custom objects. On external objects, the name
field can instead be specified by setting `isNameField` to
`true` in the CustomField component.

The field that this object's name is stored in. Every custom
object must have a name, usually a string or autonumber.

Identifier for the custom object record. This name appears in
page layouts, related lists, lookup dialogs, search results, and
key lists on tab home pages. By default, this field is added to
the custom object page layout as a required field.

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


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

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


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

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


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

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

MktDataLakeAttributes

Represents how Data 360 receives the data. MktDataLakeAttributes is a Data 360 subtype of CustomObject. Its components are available
in API version 50.0 and later.

Special Access Rules

You need an org with a Data Cloud license to access this object.

**Field Name** **Description**

```
creationType

```

**Field Type**
DefinitionCreationType enumeration of type string

**Description**
Indicates how this object is added.


Metadata Types CustomObject

**Field Name** **Description**

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

```
isEnabled

objectCategory

```

**Field Type**
boolean

**Description**
Indicates whether the Landing Object is enabled.

**Field Type**
string

**Description**
Reference to the Object Category. For landing object, these would be Profile, Behavioral,
Other.


Metadata Types CustomObject

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

```


Metadata Types CustomObject

```
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

```


Metadata Types CustomObject

```
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

```


Metadata Types CustomObject

```
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


Metadata Types CustomObject

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
[Represents an index defined within a custom big object. Use this metadata type to define the composite primary key (index) for a](https://developer.salesforce.com/docs/atlas.en-us.262.0.bigobjects.meta/bigobjects/big_object.htm)
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


#### Metadata Types ActionOverride

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

Fields

Unless otherwise noted, all fields are creatable, filterable, and nillable.

**Field Name** **Field Type** **Description**

`actionName` string Required. The possible values are the same as the actions you can override:

**•** `accept`

**•** `clone`

**•** `delete`


Metadata Types ActionOverride

**Field Name** **Field Type** **Description**

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

**•** In API version 43.0 and later, a Lightning component override for
Lightning Experience returns the `Large` value and a Lightning
component override for mobile returns the `Small` value, as
expected.

`skipRecordTypeSelect` boolean Set this field to `true` if you prefer that any new records created by this
action override aren’t forwarded to the record type selection page. This

field is only valid if the `actionName` is a “create” type (like `new` ), and


Metadata Types ActionOverride

**Field Name** **Field Type** **Description**

`type` is set to `visualforce` . This field is available in API version 21.0
and later.

`type` ActionOverrideType Required. Represents the type of action override. Valid values are described
(enumeration of type string) in ActionOverrideType.

ActionOverrideType

ActionOverrideType on page 765 is an enumeration of type string that defines which kind of action override to use. The valid values are:

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

        <actionName>edit</actionName>

        <type>visualforce</type>

        <content>myEditVFPage</content>

        <comment>This edit action is a lot safer.</comment>

      </actionOverrides>

   </CustomObject

```

This example includes no value for FormFactor. Using no value is the same as using the `null` value, which represents Salesforce Classic.


Metadata Types ActionOverride

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

        <actionName>View</actionName>

        <content>myLightningPage</content>

        <formFactor>Large</formFactor>

        <type>flexipage</type>

      </actionOverrides>

   </CustomObject>

```


#### Metadata Types BusinessProcess

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

#### BusinessProcess on page 767 components are available in API version 17.0 and later.

Special Access Rules

Access to this object requires the View Setup and Configuration permission.

Fields

**Field** **Field Type** **Description**

`description` string Description for the business process.

`fullName` string Required. The name used as a unique identifier for API access.
This field is inherited from the Metadata component, but the

string it contains is created differently than the `fullName`
strings for other types. For a `fullName` string BusinessProcess
on page 767, the `fullName` is created combining the Entity
Name and Business Process Name. For example, for a business
process called “Bulk Orders” for opportunities, the `fullName`
would be `Opportunity.Bulk Orders` .


Metadata Types BusinessProcess

**Field** **Field Type** **Description**

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
802 is specified. For information about using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

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
field. Each value is defined as a CustomValue on page 847. If this

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

Fields use additional data types. For more information, see Metadata Field Types on page 815.

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

[Represents an index defined within a custom big object. Use this metadata type to define the composite primary key (index) for a custom](https://developer.salesforce.com/docs/atlas.en-us.262.0.bigobjects.meta/bigobjects/big_object.htm)
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

```

Records in the territory of the user seeing the list view. This option is available if territory
management is enabled for your organization. Opportunities can’t be filtered by
`MyTerritory` . This option is available in API version 17.0 and later.

`MyTeamTerritory` Records in the territory of the team of the user seeing the list view. `This option is`

```
               available if territory management is enabled for your
```

`organization.MyTeamTerritory` . This option is available in API version 17.0 and
later.

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

```


#### Metadata Types NamedFilter

```
        <columns>NAME</columns>

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

In API version 38.0 and later, Picklist is replaced by ValueSet on page 818 on the CustomField type.

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

The following sample uses a picklist. For a complete sample of using a picklist with record types and profiles, see Profile on page 1757.

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
See BusinessProcess on page 767.

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

The following sample uses two record types. For the complete sample that includes profiles and picklists, see Profile on page 1757.

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

fullName string

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
field in the CustomFieldTranslation on page 821 subtype.

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

Represents a permission that grants access to a custom feature. This type extends the Metadata metadata type and inherits its `fullName`
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
[sites, see Network.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_network.htm)

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
page 861[]

`dashboardDynamicValues` DashboardDynamicValue on page
862[]

`dashboardFilterColumns` DashboardFilterColumn on page 862[]

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
page 875

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
page 875

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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based.htm)

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

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### DgtAssetMgmtPrvdLghtCpnt

Represents the Lightning web component configurations for external content providers, such as digital asset management (DAM)
systems. This metadata type enables the integration of external content systems with Salesforce CMS using custom Lightning web
components.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

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
DgtAssetMgmtProvider on page 905 type, that this Lightning web component
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
LightningComponentBundle on page 1508 type, that implements the user interface for
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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

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
LWR sites, use the ExperienceBundle (recommended) or the SiteDotCom on page 2354 metadata types. Packaging is unsupported for
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

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.


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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### DisclosureDefinitionVersion

Represents the version information about the disclosure definition.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### DisclosureType

Represents the types of disclosures that are done by an individual or an organization and the associated metadata.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

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

