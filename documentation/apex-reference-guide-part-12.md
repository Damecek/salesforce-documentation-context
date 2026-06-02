Use this class when accessing `Metadata.Layout` metadata components. For more information, see “MiniLayout” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### MiniLayout Properties

MiniLayout Methods

#### MiniLayout Properties

### The following are properties for MiniLayout .

IN THIS SECTION:

##### fields

The fields for the mini-layout, listed in the order they appear in the UI. Fields that appear in the mini-layout must appear in the main
layout.

relatedLists
The mini related lists, listed in the order they appear in the UI. You cannot set sorting on mini related lists. Fields that appear in the
mini related lists must appear in the main layout.

##### fields

The fields for the mini-layout, listed in the order they appear in the UI. Fields that appear in the mini-layout must appear in the main
layout.

Signature

```
   public List<String> fields {get; set;}

```


### Apex Reference Guide Operations Class

Property Value

Type: List<String>

##### relatedLists

The mini related lists, listed in the order they appear in the UI. You cannot set sorting on mini related lists. Fields that appear in the mini
related lists must appear in the main layout.

Signature

```
   public List<Metadata.RelatedListItem> relatedLists {get; set;}

```

Property Value

Type: List<Metadata.RelatedListItem>

#### MiniLayout Methods The following are methods for MiniLayout .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.MiniLayout` .

##### clone()

Makes a duplicate copy of the `Metadata.MiniLayout` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### Operations Class

Represents a class to execute metadata operations, such as retrieving or deploying custom metadata.

Namespace

Metadata

Usage

Use the `Metadata.Operations` class to execute metadata operations. For more information on use cases and restrictions of
metadata operations in Apex, see Metadata.


Apex Reference Guide Operations Class

Example: Retrieve Metadata

The following example retrieves the “MyTestCustomMDType” custom metadata record from the subscriber org, and inspects the custom
fields.

```
   public class ReadMetadata {

     public void retrieveMetadata () {

      // List fullnames of components we want to retrieve

      List<String> componentNameList =

   new List<String>{'ISVNamespace__TestCustomMDType.MyTestCustomMDType'};

      // Retrieve components that are records of custom metadata types

      // based on name

      List<Metadata.Metadata> components = Metadata.Operations.retrieve(

   Metadata.MetadataType.CustomMetadata, componentNameList);

      Metadata.CustomMetadata customMetadataRecord = (Metadata.CustomMetadata)

   components.get(0);

      // Check fields of retrieved component

      List<Metadata.CustomMetadataValue> values = customMetadataRecord.values;

      for (integer i = 0; i < values.size(); i++) {

       if (values.get(i).field == 'testField__c' &&

         values.get(i).value == 'desired value') {

        // ...process accordingly...

       }

      }

     }

   }

```

Example: Deploy Metadata

The following example uses the Metadata API in Apex to update the customField custom field value of the MetadataRecordName custom
metadata record and deploy this change into the subscriber org. Because the deployment is asynchronous, you must provide a callback
class that implements the `Metadata.DeployCallback` interface, which is then used when the queued deployment completes.

```
   public class CreateMetadata{

     public void updateAndDeployMetadata() {

      // Setup custom metadata to be created in the subscriber org.

      Metadata.CustomMetadata customMetadata = new Metadata.CustomMetadata();

      customMetadata.fullName = 'ISVNamespace__MetadataTypeName.MetadataRecordName';

      Metadata.CustomMetadataValue customField = new Metadata.CustomMetadataValue();

      customField.field = 'customField__c';

      customField.value = 'New value';

      customMetadata.values.add(customField);

      Metadata.DeployContainer mdContainer = new Metadata.DeployContainer();

      mdContainer.addMetadata(customMetadata);

      // Setup deploy callback, MyDeployCallback implements

      // the Metadata.DeployCallback interface (code for

      // this class not shown in this example)

      MyDeployCallback callback = new MyDeployCallback();

```


Apex Reference Guide Operations Class

```
      // Enqueue custom metadata deployment

      Id jobId = Metadata.Operations.enqueueDeployment(mdContainer, callback);

     }

   }

```

Example: Create Two Metadata Records Synchronously

Create a metadata record along with another one that references it in the same transaction. If the parent record was installed with a
namespace, prefix the developer name with _`recordNs__`_ .

Note: No custom metadata relationship can relate records of the same type to each other.

```
   public class CreateMetadata {

      public Id doCreate(

        String parentRecDevName,

        String parentRecLabel,

        String childRecDevName,

        String childRecLabel) {

        Metadata.DeployContainer mdContainer = new Metadata.DeployContainer();

        Metadata.CustomMetadata parentRecord = new Metadata.CustomMetadata();

        parentRecord.fullName = 'ParentType.' + parentRecDevName;

        parentRecord.label = parentRecLabel;

        mdContainer.addMetadata(parentRecord);

        Metadata.CustomMetadata childRecord = new Metadata.CustomMetadata();

        childRecord.fullName = 'ChildType.' + childRecDevName;

        childRecord.label = childRecLabel;

        Metadata.CustomMetadataValue relValue = new Metadata.CustomMetadataValue();

        relValue.field = 'Parent__c';

        relValue.value = parentRecDevName;

        childRecord.values.add(relValue);

        mdContainer.addMetadata(childRecord);

        Id jobId = Metadata.Operations.enqueueDeployment(mdContainer, null);

        return jobId;

      }

   }

```

IN THIS SECTION:

#### Operations Methods Operations Methods The following are methods for Operations .


Apex Reference Guide Operations Class

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.Operations` .

##### enqueueDeployment(container, callback)

Deploys custom metadata components asynchronously.

retrieve(type, fullNames)
Retrieves a list of custom metadata components.

##### clone()

Makes a duplicate copy of the `Metadata.Operations` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### enqueueDeployment(container, callback)

Deploys custom metadata components asynchronously.

Signature

To preserve service function, we limit the number of Metadata API deployments originating from Apex that can be enqueued at a time.
See Limit on Enqueued Deployments from Apex.

```
   public static Id enqueueDeployment(Metadata.DeployContainer container,

   Metadata.DeployCallback callback)

```

Parameters

```
   container
```

Type: Metadata.DeployContainer

Container that contains the set of metadata components to deploy.

```
   callback
```

Type: Metadata.DeployCallback

A class that implements the `Metadata.DeployCallback` interface. Used by Salesforce to return information about the
deployment results.

Return Value

Type: Id

ID of deployment request.


### Apex Reference Guide PlatformActionList Class

##### retrieve(type, fullNames)

Retrieves a list of custom metadata components.

Signature

```
   public static List<Metadata.Metadata> retrieve(Metadata.MetadataType type, List<String>

   fullNames)

```

Parameters

```
   type
```

Type: Metadata.MetadataType

The metadata component type.

```
   fullNames
```

Type: List<String>

A list of component names to retrieve. For information on component name formats, see Metadata.fullName().

Return Value

Type: List<Metadata.Metadata>

### PlatformActionList Class

Represents the list of actions, and their order, that display in the Salesforce mobile action bar for the layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “PlatformActionList” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### PlatformActionList Properties

PlatformActionList Methods

#### PlatformActionList Properties

### The following are properties for PlatformActionList .

IN THIS SECTION:

actionListContext
The context of the action list.


Apex Reference Guide PlatformActionList Class

##### platformActionListItems

The actions in the platform action list.

##### relatedSourceEntity When the actionListContext property is “RelatedList” or” “RelatedListRecord”, this field represents the API name of the

related list to which the action belongs.

##### actionListContext

The context of the action list.

Signature

```
   public Metadata.PlatformActionListContextEnum actionListContext {get; set;}

```

Property Value

Type: Metadata.PlatformActionListContextEnum

##### platformActionListItems

The actions in the platform action list.

Signature

```
   public List<Metadata.PlatformActionListItem> platformActionListItems {get; set;}

```

Property Value

Type: List<Metadata.PlatformActionListItem>

##### relatedSourceEntity When the actionListContext property is “RelatedList” or” “RelatedListRecord”, this field represents the API name of the related

list to which the action belongs.

Signature

```
   public String relatedSourceEntity {get; set;}

```

Property Value

Type: String

#### PlatformActionList Methods The following are methods for PlatformActionList .


### Apex Reference Guide PlatformActionListContextEnum Enum

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionList` .

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionList` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### PlatformActionListContextEnum Enum

Describes the different contexts of action lists.

Enum Values

The following are the values of the `Metadata.PlatformActionListContextEnum` enum.

**Value** **Description**

`ActionDefinition` Action definition context.

`Assistant` Assistant context.

`BannerPhoto` Banner photo context.

`Chatter` Chatter context.

`Dockable` Dockable context.

`FeedElement` Feed element context.

`Flexipage` Flexipage context.

`Global_x` Global context.

`ListView` Listview context.

`ListViewDefinition` Listview definition context.

`ListViewRecord` Listview record context.

`Lookup` Lookup context.

`MruList` MRU list context.

`MruRow` MRU row context.

`ObjectHomeChart` Object home chart context.


### Apex Reference Guide PlatformActionListItem Class

**Value** **Description**

`Photo` Photo context

`Record` Record context.

`RecordEdit` Record edit context

`RelatedList` Related list context.

`RelatedListRecord` Related list record context.

### PlatformActionListItem Class

Represents an action in the platform action list for a layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “PlatformActionListItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### PlatformActionListItem Properties

PlatformActionListItem Methods

#### PlatformActionListItem Properties

### The following are properties for PlatformActionListItem .

IN THIS SECTION:

##### actionName

The API name for the action in the list.

actionType
The type of action.

sortOrder
The placement of the action in the list.

subtype
The subtype of the action.

##### actionName

The API name for the action in the list.


Apex Reference Guide PlatformActionListItem Class

Signature

```
   public String actionName {get; set;}

```

Property Value

Type: String

##### actionType

The type of action.

Signature

```
   public Metadata.PlatformActionTypeEnum actionType {get; set;}

```

Property Value

Type: Metadata.PlatformActionTypeEnum

##### sortOrder

The placement of the action in the list.

Signature

```
   public Integer sortOrder {get; set;}

```

Property Value

Type: Integer

##### subtype

The subtype of the action.

Signature

```
   public String subtype {get; set;}

```

Property Value

Type: String

#### PlatformActionListItem Methods The following are methods for PlatformActionListItem .


### Apex Reference Guide PlatformActionTypeEnum Enum

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionListItem` .

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionListItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### PlatformActionTypeEnum Enum

The type of action for a `PlatformActionListItem` .

Enum Values

The following are the values of the `Metadata.PlatformActionTypeEnum` enum.

**Value** **Description**

`ActionLink` An indicator on a feed element that targets an API, a web page, or a file, represented
by a button in the Salesforce Chatter feed UI.

`CustomButton` When clicked, opens a URL or a Visualforce page in a window or executes JavaScript.

`InvocableAction` An invocable action such as posting to Chatter.

`ProductivityAction` Productivity actions are predefined by Salesforce and are attached to a limited set
of objects. You can’t edit or delete productivity actions.

`QuickAction` A global or object-specific action.

`StandardButton` A predefined Salesforce button such as New, Edit, and Delete.

### PrimaryTabComponents Class

Represents custom console components on primary tabs in the Salesforce console.

Namespace

Metadata


Apex Reference Guide PrimaryTabComponents Class

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “PrimaryTabComponents” in
the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### PrimaryTabComponents Properties PrimaryTabComponents Methods PrimaryTabComponents Properties The following are properties for PrimaryTabComponents .

IN THIS SECTION:

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce
console.

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

Signature

```
   public List<Metadata.ConsoleComponent> component {get; set;}

```

Property Value

Type: List<Metadata.ConsoleComponent>

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce console.

Signature

```
   public List<Metadata.Container> containers {get; set;}

```

Property Value

Type: List<Metadata.Container>

#### PrimaryTabComponents Methods The following are methods for PrimaryTabComponents .


### Apex Reference Guide QuickActionList Class

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.PrimaryTabComponents` .

##### clone()

Makes a duplicate copy of the `Metadata.PrimaryTabComponents` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### QuickActionList Class

Represents the list of actions associated with the page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “QuickActionList” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### QuickActionList Properties

QuickActionList Methods

#### QuickActionList Properties

### The following are properties for QuickActionList .

IN THIS SECTION:

##### quickActionListItems
### List of QuickActionList objects.

##### quickActionListItems

### List of QuickActionList objects.


### Apex Reference Guide QuickActionListItem Class

Signature

```
   public List<Metadata.QuickActionListItem> quickActionListItems {get; set;}

```

Property Value

Type: List<Metadata.QuickActionListItem>

#### QuickActionList Methods The following are methods for QuickActionList .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionList` .

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionList` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### QuickActionListItem Class

#### Represents an action in the QuickActionList .

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “QuickActionListItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

QuickActionListItem Properties

QuickActionListItem Methods


### Apex Reference Guide RelatedContent Class

#### QuickActionListItem Properties The following are properties for QuickActionListItem .

IN THIS SECTION:

##### quickActionName

The API name of the action.

##### quickActionName

The API name of the action.

Signature

```
   public String quickActionName {get; set;}

```

Property Value

Type: String

#### QuickActionListItem Methods The following are methods for QuickActionListItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionListItem` .

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionListItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### RelatedContent Class

Represents the Mobile Cards section of the page layout.

Namespace

Metadata


Apex Reference Guide RelatedContent Class

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedContent” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### RelatedContent Properties RelatedContent Methods RelatedContent Properties The following are properties for RelatedContent .

IN THIS SECTION:

##### relatedContentItems

A list of layout items in the Mobile Cards section of the page layout.

##### relatedContentItems

A list of layout items in the Mobile Cards section of the page layout.

Signature

```
   public List<Metadata.RelatedContentItem> relatedContentItems {get; set;}

```

Property Value

Type: List<Metadata.RelatedContentItem>

#### RelatedContent Methods The following are methods for RelatedContent .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContent` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContent` .

Signature

```
   public Object clone()

```


### Apex Reference Guide RelatedContentItem Class

Return Value

Type: Object

### RelatedContentItem Class Represents an individual item in the RelatedContent list.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedContentItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### RelatedContentItem Properties RelatedContentItem Methods RelatedContentItem Properties

### The following are properties for RelatedContentItem .

IN THIS SECTION:

##### layoutItem

An individual layout item in the Mobile Cards section.

##### layoutItem

An individual layout item in the Mobile Cards section.

Signature

```
   public Metadata.LayoutItem layoutItem {get; set;}

```

Property Value

Type: Metadata.LayoutItem

#### RelatedContentItem Methods

### The following are methods for RelatedContentItem .


### Apex Reference Guide RelatedList Class

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContentItem` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContentItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### RelatedList Class

Represents related list custom components on the sidebars of the Salesforce console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedList” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### RelatedList Properties

RelatedList Methods

#### RelatedList Properties

### The following are properties for RelatedList .

IN THIS SECTION:

hideOnDetail
When set to true, the related list is hidden from detail pages where it appears as a component to prevent duplicate information from
showing.

name
The name of the component as it appears to console users.


### Apex Reference Guide RelatedListItem Class

##### hideOnDetail

When set to true, the related list is hidden from detail pages where it appears as a component to prevent duplicate information from
showing.

Signature

```
   public Boolean hideOnDetail {get; set;}

```

Property Value

Type: Boolean

##### name

The name of the component as it appears to console users.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

#### RelatedList Methods The following are methods for RelatedList .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedList` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedList` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### RelatedListItem Class

Represents an item in the related list in a page layout.


Apex Reference Guide RelatedListItem Class

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedListItem” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### RelatedListItem Properties

RelatedListItem Methods

#### RelatedListItem Properties The following are properties for RelatedListItem .

IN THIS SECTION:

##### customButtons

A list of custom buttons used in the related list.

excludeButtons
A list of excluded related-list buttons.

fields
A list of fields displayed in the related list. Uses aliases instead of field or API names.

quickActions
A list of quick actions used on the related list.

relatedList
The name of the related list.

sortField
The name of the field used for sorting.

sortOrder
When `sortField` is set, the `sortOrder` property determines the sort order.

##### customButtons

A list of custom buttons used in the related list.

Signature

```
   public List<String> customButtons {get; set;}

```

Property Value

Type: List<String>


Apex Reference Guide RelatedListItem Class

For more information, see “Define Custom Buttons and Links” in the Salesforce online help.

##### excludeButtons

A list of excluded related-list buttons.

Signature

```
   public List<String> excludeButtons {get; set;}

```

Property Value

Type: List<String>

##### fields

A list of fields displayed in the related list. Uses aliases instead of field or API names.

Signature

```
   public List<String> fields {get; set;}

```

Property Value

Type: List<String>

##### **`quickActions`**

A list of quick actions used on the related list.

Signature

```
   public List<String> quickActions {get; set;}

```

Property Value

Type: List<String>

##### relatedList

The name of the related list.

Signature

```
   public String relatedList {get; set;}

```

Property Value

Type: String


### Apex Reference Guide ReportChartComponentLayoutItem Class

##### sortField

The name of the field used for sorting.

Signature

```
   public String sortField {get; set;}

```

Property Value

Type: String

##### sortOrder When sortField is set, the sortOrder property determines the sort order.

Signature

```
   public Metadata.SortOrder sortOrder {get; set;}

```

Property Value

Type: Metadata.SortOrder

#### RelatedListItem Methods The following are methods for RelatedListItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedListItem` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedListItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### ReportChartComponentLayoutItem Class

Represents the settings for a report chart on a standard or custom page.


Apex Reference Guide ReportChartComponentLayoutItem Class

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see
“ReportChartComponentLayoutItem” in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### ReportChartComponentLayoutItem Properties

ReportChartComponentLayoutItem Methods

#### ReportChartComponentLayoutItem Properties The following are properties for ReportChartComponentLayoutItem .

IN THIS SECTION:

##### cacheData

Indicates whether to use cached data when displaying the chart. When the attribute is set to true, data is cached for 24 hours. When
the attribute is set to false, the report is run every time the page is refreshed.

contextFilterableField
Unique development name of the field by which a report chart is filtered to return data relevant to the page. If set, the ID field for
the parent object of the page or report type is the chart data filter. The parent object for the report type and the page must match
for a chart to return relevant data.

error
Error string that is populated only when an error occurs in the underlying report.

hideOnError
Controls whether users see a chart that has an error. When an error occurs and this attribute is not set, the chart doesn’t show any
data except the error. Set the attribute to true to hide the chart from a page on error.

includeContext
If true, filters the report chart to return data that’s relevant to the page.

reportName
Unique development name of a report that includes a chart.

showTitle
If true, applies the title from the report to the chart.

size
Size of the displayed chart. The default is medium.

##### cacheData

Indicates whether to use cached data when displaying the chart. When the attribute is set to true, data is cached for 24 hours. When
the attribute is set to false, the report is run every time the page is refreshed.


Apex Reference Guide ReportChartComponentLayoutItem Class

Signature

```
   public Boolean cacheData {get; set;}

```

Property Value

Type: Boolean

##### contextFilterableField

Unique development name of the field by which a report chart is filtered to return data relevant to the page. If set, the ID field for the
parent object of the page or report type is the chart data filter. The parent object for the report type and the page must match for a chart
to return relevant data.

Signature

```
   public String contextFilterableField {get; set;}

```

Property Value

Type: String

##### error

Error string that is populated only when an error occurs in the underlying report.

Signature

```
   public String error {get; set;}

```

Property Value

Type: String

##### hideOnError

Controls whether users see a chart that has an error. When an error occurs and this attribute is not set, the chart doesn’t show any data
except the error. Set the attribute to true to hide the chart from a page on error.

Signature

```
   public Boolean hideOnError {get; set;}

```

Property Value

Type: Boolean

##### includeContext

If true, filters the report chart to return data that’s relevant to the page.


Apex Reference Guide ReportChartComponentLayoutItem Class

Signature

```
   public Boolean includeContext {get; set;}

```

Property Value

Type: Boolean

##### reportName

Unique development name of a report that includes a chart.

Signature

```
   public String reportName {get; set;}

```

Property Value

Type: String

##### showTitle

If true, applies the title from the report to the chart.

Signature

```
   public Boolean showTitle {get; set;}

```

Property Value

Type: Boolean

##### size

Size of the displayed chart. The default is medium.

Signature

```
   public Metadata.ReportChartComponentSize size {get; set;}

```

Property Value

Type: Metadata.ReportChartComponentSize

#### ReportChartComponentLayoutItem Methods The following are methods for ReportChartComponentLayoutItem .


### Apex Reference Guide ReportChartComponentSize Enum

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.ReportChartComponentLayoutItem` .

##### clone()

Makes a duplicate copy of the `Metadata.ReportChartComponentLayoutItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### ReportChartComponentSize Enum

Describes the size of the displayed report chart component.

Enum Values

The following are the values of the `Metadata.ReportChartComponentSize` enum.

**Value** **Description**

`LARGE` Large chart size.

`MEDIUM` Medium chart size.

`SMALL` Small chart size.

### SidebarComponent Class

Represents a specific custom console component to display in a container that hosts multiple components in one of the sidebars of the
Salesforce console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SidebarComponent” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

SidebarComponent Properties


Apex Reference Guide SidebarComponent Class

SidebarComponent Methods

#### SidebarComponent Properties The following are properties for SidebarComponent .

IN THIS SECTION:

##### componentType

Specifies the component type. Valid values are “KnowledgeOne”, “Lookup”, “Milestones”, “RelatedList”, “Topics”, “Files”, and
“CaseExperts”.

createAction
If the component is a lookup field, the name of the quick action used to create a record.

enableLinking
If the component is a lookup field, lets users associate a record with this field.

height
The height of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

knowledgeOneEnable
Indicates if the component is enabled for Knowledge One.

label
The name of the component as it displays to console users. Available for components in a container with the style of tabs or accordion.

lookup
If the component is a lookup field, the name of the field.

page_x
If the component is a Visualforce page, the name of the Visualforce page.

relatedLists
If the component is a related list component, the list of related list names.

unit
The unit of measurement (pixels or percent) for the height and width of the component in the container.

updateAction
If the component is a lookup field, the name of the quick action used to update a record.

width
The width of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

##### componentType

Specifies the component type. Valid values are “KnowledgeOne”, “Lookup”, “Milestones”, “RelatedList”, “Topics”, “Files”, and “CaseExperts”.

Signature

```
   public String componentType {get; set;}

```


Apex Reference Guide SidebarComponent Class

Property Value

Type: String

##### createAction

If the component is a lookup field, the name of the quick action used to create a record.

Signature

```
   public String createAction {get; set;}

```

Property Value

Type: String

##### enableLinking

If the component is a lookup field, lets users associate a record with this field.

Signature

```
   public Boolean enableLinking {get; set;}

```

Property Value

Type: Boolean

##### height

The height of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### knowledgeOneEnable

Indicates if the component is enabled for Knowledge One.

Signature

```
   public Boolean knowledgeOneEnable {get; set;}

```

Property Value

Type: Boolean


Apex Reference Guide SidebarComponent Class

##### label

The name of the component as it displays to console users. Available for components in a container with the style of tabs or accordion.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### lookup

If the component is a lookup field, the name of the field.

Signature

```
   public String lookup {get; set;}

```

Property Value

Type: String

##### page_x

If the component is a Visualforce page, the name of the Visualforce page.

Signature

```
   public String page_x {get; set;}

```

Property Value

Type: String

##### relatedLists

If the component is a related list component, the list of related list names.

Signature

```
   public List<Metadata.RelatedList> relatedLists {get; set;}

```

Property Value

Type: List<Metadata.RelatedList>

##### unit

The unit of measurement (pixels or percent) for the height and width of the component in the container.


Apex Reference Guide SidebarComponent Class

Signature

```
   public String unit {get; set;}

```

Property Value

Type: String

##### updateAction

If the component is a lookup field, the name of the quick action used to update a record.

Signature

```
   public String updateAction {get; set;}

```

Property Value

Type: String

##### width

The width of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

Signature

```
   public Integer width {get; set;}

```

Property Value

Type: Integer

#### SidebarComponent Methods The following are methods for SidebarComponent .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SidebarComponent` .

##### clone()

Makes a duplicate copy of the `Metadata.SidebarComponent` .

Signature

```
   public Object clone()

```


### Apex Reference Guide SortOrder Enum

Return Value

Type: Object

### SortOrder Enum

Describes the sort order of a related list.

Enum Values

The following are the values of the `Metadata.SortOrder` enum.

**Value** **Description**

`Asc_x` Sort in ascending order.

`Desc_x` Sort in descending order.

### StatusCode Enum

Describes the status code for an unsuccessful component deploy.

Enum Values

The following are the values of the `Metadata.StatusCode` enum.

**Value** **Description**

`INVALID_SCS_INBOUND_USER` Log in as the RunAs user configured in your SCS setup.

`REQUIRE_CONNECTED_APP_SCS` SCS Connected App is not installed.

`REQUIRE_CONNECTED_APP_SESSION_SCS` To use the SCS connected app, the user must be authenticated.

`REQUIRE_RUNAS_USER` A RunAs user must be configured in your org.

SEE ALSO:

DeployProblemType Enum

### SubtabComponents Class

Represents custom console components on subtabs in the Salesforce console.

Namespace

Metadata


Apex Reference Guide SubtabComponents Class

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SubtabComponents” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### SubtabComponents Properties SubtabComponents Methods SubtabComponents Properties The following are properties for SubtabComponents .

IN THIS SECTION:

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce
console.

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

Signature

```
   public List<Metadata.ConsoleComponent> component {get; set;}

```

Property Value

Type: List<Metadata.ConsoleComponent>

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce console.

Signature

```
   public List<Metadata.Container> containers {get; set;}

```

Property Value

Type: List<Metadata.Container>

#### SubtabComponents Methods The following are methods for SubtabComponents .


### Apex Reference Guide SummaryLayoutStyleEnum Enum

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SubtabComponents` .

##### clone()

Makes a duplicate copy of the `Metadata.SubtabComponents` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### SummaryLayoutStyleEnum Enum Describes the highlights panel style for a SummaryLayout .

Enum Values

The following are the values of the `Metadata.SummaryLayoutStyleEnum` enum.

**Value** **Description**

`CaseInteraction` Case interaction style.

`ChildServiceReportTemplateStyle` Child service report template style.

`DefaultQuoteTemplate` Default quote template style.

`DefaultServiceReportTemplate` Default service report style

`Default_x` Default style.

`PathAssistant` Path assisstant style.

`QuickActionLayoutLeftRight` Quick action left-right layout style.

`QuickActionLayoutTopDown` Quick action top-down layout style.

`QuoteTemplate` Quote template style.

`ServiceReportTemplate` Service report style.

### SummaryLayout Class

Controls the appearance of the highlights panel, which summarizes key fields in a grid at the top of a page layout, when Case Feed is
enabled.


Apex Reference Guide SummaryLayout Class

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SummaryLayout” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### SummaryLayout Properties

SummaryLayout Methods

#### SummaryLayout Properties The following are properties for SummaryLayout .

IN THIS SECTION:

##### masterLabel

The name of the layout label.

sizeX
Number of columns in the highlights pane, between 1 and 4 (inclusive).

sizeY
Number of rows in each column, either 1 or 2.

sizeZ
If provided, the setting is not visible to users.

summaryLayoutItems
Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. At least one is required.

summaryLayoutStyle
Specifies the panel style.

##### masterLabel

The name of the layout label.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Signature

```
   public String masterLabel {get; set;}

```

Property Value

Type: String


Apex Reference Guide SummaryLayout Class

##### sizeX

Number of columns in the highlights pane, between 1 and 4 (inclusive).

Signature

```
   public Integer sizeX {get; set;}

```

Property Value

Type: Integer

##### sizeY

Number of rows in each column, either 1 or 2.

Signature

```
   public Integer sizeY {get; set;}

```

Property Value

Type: Integer

##### sizeZ

If provided, the setting is not visible to users.

Signature

```
   public Integer sizeZ {get; set;}

```

Property Value

Type: Integer

##### summaryLayoutItems

Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. At least one is required.

Signature

```
   public List<Metadata.SummaryLayoutItem> summaryLayoutItems {get; set;}

```

Property Value

Type: List<Metadata.SummaryLayoutItem>


### Apex Reference Guide SummaryLayoutItem Class

##### summaryLayoutStyle

Specifies the panel style.

Signature

```
   public Metadata.SummaryLayoutStyleEnum summaryLayoutStyle {get; set;}

```

Property Value

Type: Metadata.SummaryLayoutStyleEnum

#### SummaryLayout Methods The following are methods for SummaryLayout .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayout` .

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayout` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### SummaryLayoutItem Class

Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. You can have two fields per each grid in a highlights panel.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SummaryLayoutItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

SummaryLayoutItem Properties


Apex Reference Guide SummaryLayoutItem Class

SummaryLayoutItem Methods

#### SummaryLayoutItem Properties The following are properties for SummaryLayoutItem .

IN THIS SECTION:

##### customLink

The custom link reference.

##### field

The field name reference, relative to the page layout. Must be a standard or custom field that also exists on the detail page.

##### posX

The item's column position in the highlights panel grid. Must be within the range of `sizeX` .

posY
The item's row position in the highlights panel grid. Must be within the range of `sizeY` .

posZ
Reserved for future use. If provided, the setting is not visible to users.

##### customLink

The custom link reference.

Signature

```
   public String customLink {get; set;}

```

Property Value

Type: String

##### field

The field name reference, relative to the page layout. Must be a standard or custom field that also exists on the detail page.

Signature

```
   public String field {get; set;}

```

Property Value

Type: String

##### posX

The item's column position in the highlights panel grid. Must be within the range of `sizeX` .


Apex Reference Guide SummaryLayoutItem Class

Signature

```
   public Integer posX {get; set;}

```

Property Value

Type: Integer

##### posY

The item's row position in the highlights panel grid. Must be within the range of `sizeY` .

Signature

```
   public Integer posY {get; set;}

```

Property Value

Type: Integer

##### posZ

Reserved for future use. If provided, the setting is not visible to users.

Signature

```
   public Integer posZ {get; set;}

```

Property Value

Type: Integer

#### SummaryLayoutItem Methods The following are methods for SummaryLayoutItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayoutItem` .

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayoutItem` .

Signature

```
   public Object clone()

```


### Apex Reference Guide UiBehavior Enum

Return Value

Type: Object

### UiBehavior Enum

Describes the behavior for a layout item on a layout page.

Enum Values

The following are the values of the `Metadata.UiBehavior` enum.

**Value** **Description**

`Edit` The layout field can be edited but is not required.

`Readonly` The layout field is read-only.

`Required` The layout field can be edited and is required.

## PlaceQuote Namespace The PlaceQuote namespace provides classes and methods to create or update quotes with pricing preferences and configuration

options.

[See PlaceQuote namespace for more information about the available classes and methods.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_placequote.htm)

## Pref_center Namespace

The Pref_center namespace provides an interface, classes, and methods to create and retrieve data in forms in Preference Manager.
Preference Manager, previously called Preference Center, is a feature within the Privacy Center app.

## The following are the classes in the Pref_center namespace.

IN THIS SECTION:

LoadFormData Class
Retrieve records related to the tokenized record id, and populate the values of a preference form.

LoadParameters Class
Contains methods to retrieve record Id information for parameters passed into the load-form handler.

PreferenceCenterApexHandler Interface
Pass data between your organization and a form in Preference Manager.

SubmitFormData Class
Contains methods to retrieve information on buttons and options selected in a preference form.

SubmitParameters Class
Retrieve record ID information to use with your submit-form handler.


### Apex Reference Guide LoadFormData Class

TokenType Enum
Defines the types of values supported by the TokenUtility methods.

TokenUtility Class
Generate authentication tokens to access preference forms.

ValidationResult Class
This class is reserved for future use with Preference Manager.

### LoadFormData Class

Retrieve records related to the tokenized record id, and populate the values of a preference form.

Namespace

Pref_center

Example

### Use methods in the LoadFormData class to set available and selected values in different form components:

```
   List<System.SelectOption> picklistOptions = new List<System.SelectOption>();

   picklistOptions.add(new System.SelectOption('optIn', 'Opt In'));

   picklistOptions.add(new System.SelectOption('optOut', 'Opt Out'));

   // Set the available options for the picklist

   loadFormData.setOptions('myPicklist', picklistOptions);

   // Add an option to the existing options for the picklist

   loadFormData.addOption('myPicklist', 'optOutAll', 'Opt Out All');

   // Select the 'optIn' option in the picklist

   loadFormData.setSelectedOption('myPicklist', 'optIn');

   List<System.SelectOption> checkboxOptions = new List<System.SelectOption>();

   checkboxOptions.add(new System.SelectOption('yes', 'Yes'));

   checkboxOptions.add(new System.SelectOption('no', 'No'));

   // Set available options for the checkbox group

   loadFormData.setOptions('myCheckbox', checkboxOptions);

   // Select the 'yes' option in the checkbox group

   loadFormData.addSelectedOption('myCheckbox', 'yes');

   // Also select the 'no' option in the checkbox group

   loadFormData.addSelectedOption('myCheckbox', 'no');

   // Another way to select both the 'yes' and 'no' options in the checkbox group

   loadFormData.setSelectedOptions('myCheckbox', new List<String>{'yes', 'no'});

   // Fill the value in the text input

   loadFormData.setTextValue('myTextInput', 'admin@salesforce.com');

   // Set the hint text for the text input

   loadFormData.setTextHint('myTextInput', 'Email Address');

```


Apex Reference Guide LoadFormData Class

```
   // Set the label for the button

   loadFormData.setButtonLabel('myButton', 'Save Preferences');

```

IN THIS SECTION:

#### LoadFormData Constructors LoadFormData Methods LoadFormData Constructors The following are constructors for LoadFormData .

IN THIS SECTION:

##### LoadFormData(data)
#### Creates an instance of the LoadFormData class for running tests on any custom Apex classes you create for Preference Manager.

##### **`LoadFormData(data)`**

#### Creates an instance of the LoadFormData class for running tests on any custom Apex classes you create for Preference Manager.

Signature

```
   public LoadFormData(Map<String,pref_center.FieldProperties> data)

```

Parameters

```
   data
```

Type: Map<String,pref_center.FieldProperties>Map

Maps preference form data from the field ID to the field properties.

Usage

This constructor is available in API version 56.0 and later.

#### LoadFormData Methods The following are methods for LoadFormData .

IN THIS SECTION:

addOption(fieldId, value, label)
Add an option for a checkbox, picklist, or radio button field in a preference form using the label and value.

addOption(fieldId, option)
Add a defined, selectable option for a checkbox, picklist, or radio button field in a preference form.


Apex Reference Guide LoadFormData Class

addSelectedOption(fieldId, option)
Add a selected option for a checkbox field in a preference form. This requires the field on the form to have a defined option with a
set value.

setButtonLabel(fieldId, label)
Set the label of a button added to the preference form.

setOptions(fieldId, options)
Add a list of selectable options for a field on a preference form.

setSelectedOption(fieldId, optionValue)
For a picklist or radio button field on a preference form that has defined values, set the value entered in the optionValue field as the
selected option.

setSelectedOptions(fieldId, options)
For an existing checkbox field on a preference form that has defined values, set the values entered in the options field as the selected
options. This requires the field on the form to have defined options with a set value.

setTextHint(fieldId, hintText)
Set the hint text inside a text input field. The hint text tells the user what type of information to enter, like an email address.

setTextValue(fieldId, value)
Set the value of a text field in a preference form.

##### **`addOption(fieldId, value, label)`**

Add an option for a checkbox, picklist, or radio button field in a preference form using the label and value.

Signature

```
   public void addOption(String fieldId, String value, String label)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   value
```

Type: String

Represents the selection or text entered in a preference form field.

```
   label
```

Type: String

The label for the value of a field in a preference form.

Return Value

Type: void

##### **`addOption(fieldId, option)`**

Add a defined, selectable option for a checkbox, picklist, or radio button field in a preference form.


Apex Reference Guide LoadFormData Class

Signature

```
   public void addOption(String fieldId, System.SelectOption option)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   option
```

Type: System.SelectOption

The option selected on a field in the preference form.

Return Value

Type: void

##### **`addSelectedOption(fieldId, option)`**

Add a selected option for a checkbox field in a preference form. This requires the field on the form to have a defined option with a set
value.

Signature

```
   public void addSelectedOption(String fieldId, String option)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   option
```

Type: String

The selectable option being added.

Return Value

Type: void

##### **`setButtonLabel(fieldId, label)`**

Set the label of a button added to the preference form.

Signature

```
   public void setButtonLabel(String fieldId, String label)

```


Apex Reference Guide LoadFormData Class

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   label
```

Type: String

The label for a button added to the preference form.

Return Value

Type: void

##### **`setOptions(fieldId, options)`**

Add a list of selectable options for a field on a preference form.

Signature

```
   public void setOptions(String fieldId, List<System.SelectOption> options)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   options
```

Type: List<System.SelectOption>

The selectable options for a field in the preference form.

Return Value

Type: void

##### **`setSelectedOption(fieldId, optionValue)`**

For a picklist or radio button field on a preference form that has defined values, set the value entered in the optionValue field as the
selected option.

Signature

```
   public void setSelectedOption(String fieldId, String optionValue)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.


Apex Reference Guide LoadFormData Class

```
   optionValue
```

Type: String

The value for the selected option.

Return Value

Type: void

##### **`setSelectedOptions(fieldId, options)`**

For an existing checkbox field on a preference form that has defined values, set the values entered in the options field as the selected
options. This requires the field on the form to have defined options with a set value.

Signature

```
   public void setSelectedOptions(String fieldId, List<String> options)

```

Parameters

```
   fieldId
```

Type: String

Identifies the checkbox field in the preference form.

```
   options
```

Type: List<String>

The selected options for a field in the preference form.

Return Value

Type: void

##### **`setTextHint(fieldId, hintText)`**

Set the hint text inside a text input field. The hint text tells the user what type of information to enter, like an email address.

Signature

```
   public void setTextHint(String fieldId, String hintText)

```

Parameters

```
   fieldId
```

Type: String

The ID of the text input field in the preference form.

```
   hintText
```

Type: String

The hint text in the text input field.


### Apex Reference Guide LoadParameters Class

Return Value

Type: void

##### **`setTextValue(fieldId, value)`**

Set the value of a text field in a preference form.

Signature

```
   public void setTextValue(String fieldId, String value)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   value
```

Type: String

Represents the value entered for the text field in a preference form.

Return Value

Type: void

### LoadParameters Class

Contains methods to retrieve record Id information for parameters passed into the load-form handler.

Namespace

Pref_center

Example

```
   String userId = loadParams.getRecordId();

   User user = [select id, AboutMe from User where id=:userId];

```

IN THIS SECTION:

#### LoadParameters Methods LoadParameters Methods

### The following are methods for LoadParameters .


### Apex Reference Guide PreferenceCenterApexHandler Interface

IN THIS SECTION:

##### getRecordId()

Returns the untokenized version of the record Id.

##### **`getRecordId()`**

Returns the untokenized version of the record Id.

Signature

```
   public String getRecordId()

```

Return Value

Type: String

### PreferenceCenterApexHandler Interface

Pass data between your organization and a form in Preference Manager.

Namespace

Pref_center

IN THIS SECTION:

#### PreferenceCenterApexHandler Methods PreferenceCenterApexHandler Methods

### The following are methods for PreferenceCenterApexHandler .

IN THIS SECTION:

##### load(loadParams, formData, validationResult)

Retrieve the record IDs and initial values from a preference form before it is edited and submitted.

submit(loadParams, formData, validationResult)
Updates the changed values of fields when the preference form is submitted.

##### **`load(loadParams, formData, validationResult)`**

Retrieve the record IDs and initial values from a preference form before it is edited and submitted.

Signature

```
   public pref_center.LoadFormData load(pref_center.LoadParameters loadParams,

   pref_center.LoadFormData formData, pref_center.ValidationResult validationResult)

```


### Apex Reference Guide SubmitFormData Class

Parameters

```
   loadParams
```

Type: pref_center.LoadParameters

Retrieve the tokenized record ID.

```
   formData
```

Type: pref_center.LoadFormData

Set the initial values of fields in a form before they are edited.

```
   validationResult
```

Type: pref_center.ValidationResult

Reserved for future use.

Return Value

Type: pref_center.LoadFormData

##### **`submit(loadParams, formData, validationResult)`**

Updates the changed values of fields when the preference form is submitted.

Signature

```
   public void submit(pref_center.SubmitParameters submitParams, pref_center.SubmitFormData

   formData, pref_center.ValidationResult validationResult)

```

Parameters

```
   submitParams
```

Type: pref_center.SubmitParameters

Retrieve the tokenized record Id.

```
   formData
```

Type: pref_center.SubmitFormData

Retrieve the values of fields in a submitted form.

```
   validationResult
```

Type: pref_center.ValidationResult

Reserved for future use.

Return Value

Type: void

### SubmitFormData Class

Contains methods to retrieve information on buttons and options selected in a preference form.


Apex Reference Guide SubmitFormData Class

Namespace

Pref_center

Example

#### Use methods in the SubmitFormData class to retrieve the selected values in different form components:

```
   String buttonClickedId = formData.getButtonClicked();

   if (buttonClickedId == 'submitButton') {

   // Handle form submit

   } else if (buttonClickedId == 'cancelButton') {

   // Handle form cancel

   }

   String picklistValueOld = formData.getOldSelectedValue('myPicklist');

   String picklistValueNew = formData.getSelectedValue('myPicklist');

   if (picklistValueOld != picklistValueNew) {

   // Do something

   }

   List<String> checkboxValuesOld = formData.getOldSelectedValues('myCheckbox');

   List<String> checkboxValuesNew = formData.getSelectedValues('myCheckbox');

   if (checkboxValuesOld != null && checkboxValuesNew != null && (checkboxValuesOld.size()

   != checkboxValuesNew.size())) {

   // Do something

   }

   String textinputValueOld = formData.getOldStringValue('myTextinput');

   String textinputValueNew = formData.getStringValue('myTextinput');

   if (textinputValueOld != textinputValueNew) {

   // Do something

   }

```

IN THIS SECTION:

#### SubmitFormData Methods SubmitFormData Methods The following are methods for SubmitFormData .

IN THIS SECTION:

getButtonClicked()
Returns the field ID of the button that was clicked in the preference form. For example, use this method to determine if the clicked
#### button was Submit or Cancel .

getOldSelectedValue(fieldId)
Returns the value that was set for the specified field when the preference form was previously edited by the user. This method is
used for field types such as picklist or radio buttons.


Apex Reference Guide SubmitFormData Class

##### getOldSelectedValues(fieldId)

Returns a list of the string values that were set on a checkbox field when the preference form was previously edited by the user.

getOldStringValue(fieldId)
Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as
text, and throws a TypeException if used with a field that can return more than one value, like a checkbox field.

getSelectedValue(fieldId)
Returns the string value that is currently selected for a picklist or radio button field in the preference form.

getSelectedValues(fieldId)
Returns a list of string values that are currently selected on a checkbox field in the preference form.

getStringValue(fieldId)
Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as
text.

##### **`getButtonClicked()`**

Returns the field ID of the button that was clicked in the preference form. For example, use this method to determine if the clicked button
was **Submit** or **Cancel** .

Signature

```
   public String getButtonClicked()

```

Return Value

Type: String

##### **`getOldSelectedValue(fieldId)`**

Returns the value that was set for the specified field when the preference form was previously edited by the user. This method is used
for field types such as picklist or radio buttons.

Signature

```
   public String getOldSelectedValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

##### **`getOldSelectedValues(fieldId)`**

Returns a list of the string values that were set on a checkbox field when the preference form was previously edited by the user.


Apex Reference Guide SubmitFormData Class

Signature

```
   public List<String> getOldSelectedValues(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: List<String>

##### **`getOldStringValue(fieldId)`**

Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as text,
and throws a TypeException if used with a field that can return more than one value, like a checkbox field.

Signature

```
   public String getOldStringValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

##### **`getSelectedValue(fieldId)`**

Returns the string value that is currently selected for a picklist or radio button field in the preference form.

Signature

```
   public String getSelectedValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String


### Apex Reference Guide SubmitParameters Class

##### **`getSelectedValues(fieldId)`**

Returns a list of string values that are currently selected on a checkbox field in the preference form.

Signature

```
   public List<String> getSelectedValues(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: List<String>

##### **`getStringValue(fieldId)`**

Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as text.

Signature

```
   public String getStringValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

### SubmitParameters Class

Retrieve record ID information to use with your submit-form handler.

Namespace

Pref_center

Example

```
   String userId = submitParams.getRecordId();

   User user = [select id, AboutMe from User where id=:userId];

```


### Apex Reference Guide TokenType Enum

IN THIS SECTION:

#### SubmitParameters Methods SubmitParameters Methods The following are methods for SubmitParameters .

IN THIS SECTION:

##### getRecordId()

Returns the untokenized version of the record ID.

##### **`getRecordId()`**

Returns the untokenized version of the record ID.

Signature

```
   public String getRecordId()

```

Return Value

Type: String

### TokenType Enum

Defines the types of values supported by the TokenUtility methods.

Enum Values

The following are the values of the `pref_center.TokenType` enum.

**Value** **Description**

`EMAIL` Identifies the token as an email address.

`STANDARD` Identifies the token as a Salesforce record ID. This is the default token type.

### TokenUtility Class

Generate authentication tokens to access preference forms.

Namespace

Pref_center


Apex Reference Guide TokenUtility Class

Example

Call the `generateToken()` method to generate a single token for a specified Salesforce record ID:

```
   Individual individual = [SELECT Id FROM Individual LIMIT 1];

   String token = pref_center.TokenUtility.generateToken(individual.Id);

   // Do something with the token

   System.debug(token)

```

Call the `generateTokens()` method to generate tokens in bulk when given a list of Salesforce record IDs:

```
   List<Id> individualIds = new List<Id>();

   // Get Ids of Individuals who have not opted out of tracking

   for (Individual individual : [SELECT Id FROM Individual WHERE HasOptedOutTracking = false])

    {

      individualIds.add(individual.Id);

   }

   // Generate tokens for the list of Individual record Ids

   Map<String, String> tokens = pref_center.TokenUtility.generateTokens(individualIds);

   String firstIndividualId = individualIds[0];

   // The returned Map has the input record Id as key and the corresponding token as value

   String tokenForFirstIndividual = tokens.get(firstIndividualId);

   // Do something with the token

   System.debug(tokenForFirstIndividual);

```

IN THIS SECTION:

#### TokenUtility Methods TokenUtility Methods The following are methods for TokenUtility .

IN THIS SECTION:

##### generateToken(tokenValue, tokenType)

Returns the authentication token for the specified token value using the given token type.

generateToken(tokenValue)
Returns the authentication token for the specified token value using the default `standard` token type.

generateTokens(tokenValues, tokenType)
Returns the authentication tokens in the form of a map, where the map key is the input value to be tokenized and the map value is
the corresponding token. The given token type is used to generate the tokens.

generateTokens(tokenValues)
Returns the generated tokens in the form of a map. This method uses the default standard token type to generate the tokens.

##### **`generateToken(tokenValue, tokenType)`**

Returns the authentication token for the specified token value using the given token type.


Apex Reference Guide TokenUtility Class

Signature

```
   public static String generateToken(String tokenValue, pref_center.TokenType tokenType)

```

Parameters

```
   tokenValue
```

Type: String

The value passed to `LoadParameters.getRecordId()` and `SubmitParameters.getRecordId()` . Identifies the
entity that the preference form is acting on.

```
   tokenType
```

Type: pref_center.TokenType

Specifies the type of the value to be encrypted with authentication tokens.

Return Value

Type: String

##### **`generateToken(tokenValue)`**

Returns the authentication token for the specified token value using the default `standard` token type.

Signature

```
   public static String generateToken(String tokenValue)

```

Parameters

```
   tokenValue
```

Type: String

Identifies the entity that the preference form is acting on. The value passed to `LoadParameters.getRecordId()` and
`SubmitParameters.getRecordId()` .

Return Value

Type: String

##### **`generateTokens(tokenValues, tokenType)`**

Returns the authentication tokens in the form of a map, where the map key is the input value to be tokenized and the map value is the
corresponding token. The given token type is used to generate the tokens.

Signature

```
   public static Map<String,String> generateTokens(List<String> tokenValues,

   pref_center.TokenType tokenType)

```


### Apex Reference Guide ValidationResult Class

Parameters

```
   tokenValues
```

Type: List<String>

The values passed to `LoadParameters.getRecordId()` and `SubmitParameters.getRecordId()` . Identifies
the entity that the preference form is acting on. Contains multiple values to be encrypted with authentication tokens.

```
   tokenType
```

Type: pref_center.TokenType

Specifies the type of the value to be encrypted with authentication tokens.

Return Value

Type: Map<String,String>

##### **`generateTokens(tokenValues)`**

Returns the generated tokens in the form of a map. This method uses the default standard token type to generate the tokens.

Signature

```
   public static Map<String,String> generateTokens(List<String> tokenValues)

```

Parameters

```
   tokenValues
```

Type: List<String>

The list of string values passed to `LoadParameters.getRecordId()` and `SubmitParameters.getRecordId().`
Contains multiple values to be encrypted with authentication tokens.

Return Value

Type: Map<String,String>, where the map key is the input value to be tokenized and the map value is the corresponding token.

### ValidationResult Class

This class is reserved for future use with Preference Manager.

Namespace

Pref_center

## Process Namespace The Process namespace provides an interface and classes for passing data between your organization and a flow. The following are the interfaces and classes in the Process namespace.


### Apex Reference Guide Plugin Interface

IN THIS SECTION:

### Plugin Interface

Allows you to pass data between your organization and a specified flow.

PluginDescribeResult Class
Describes the input and output parameters for `Process.PluginResult` .

PluginDescribeResult.InputParameter Class
Describes the input parameter for `Process.PluginResult` .

PluginDescribeResult.OutputParameter Class
Describes the output parameter for `Process.PluginResult` .

PluginDescribeResult.ParameterType Enum
Specifies the data types of input and output parameters of the `Process.PluginDescribeResult` class.

PluginRequest Class
Passes input parameters from the class that implements the `Process.Plugin` interface to the flow.

PluginResult Class
Returns output parameters from the class that implements the `Process.Plugin` interface to the flow.

SEE ALSO:

_Apex Developer Guide_ [: Passing Data to a Flow Using the Process.Plugin Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_process_plugin_using.htm)

### Plugin Interface

Allows you to pass data between your organization and a specified flow.

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

IN THIS SECTION:

Plugin Methods

Plugin Example Implementation


Apex Reference Guide Plugin Interface

#### Plugin Methods The following are instance methods for Plugin .

IN THIS SECTION:

##### describe()

Returns a `Process.PluginDescribeResult` object that describes this method call.

##### invoke(request)

Primary method that the system invokes when the class that implements the interface is instantiated.

##### describe()

Returns a `Process.PluginDescribeResult` object that describes this method call.

Signature

```
   public Process.PluginDescribeResult describe()

```

Return Value

Type: Process.PluginDescribeResult

##### invoke(request)

Primary method that the system invokes when the class that implements the interface is instantiated.

Signature

```
   public Process.PluginResult invoke(Process.PluginRequest request)

```

Parameters

```
   request
```

Type: Process.PluginRequest

Return Value

Type: Process.PluginResult

#### Plugin Example Implementation

```
   global class flowChat implements Process.Plugin {

   // The main method to be implemented. The Flow calls this at run time.

   global Process.PluginResult invoke(Process.PluginRequest request) {

        // Get the subject of the Chatter post from the flow

        String subject = (String) request.inputParameters.get('subject');

        // Use the Chatter APIs to post it to the current user's feed

```


### Apex Reference Guide PluginDescribeResult Class

```
        FeedItem fItem = new FeedItem();

        fItem.ParentId = UserInfo.getUserId();

        fItem.Body = 'Flow Update: ' + subject;

        insert fItem;

        // return to Flow

        Map<String,Object> result = new Map<String,Object>();

        return new Process.PluginResult(result);

      }

      // Returns the describe information for the interface

      global Process.PluginDescribeResult describe() {

        Process.PluginDescribeResult result = new Process.PluginDescribeResult();

        result.Name = 'flowchatplugin';

        result.Tag = 'chat';

        result.inputParameters = new

          List<Process.PluginDescribeResult.InputParameter>{

            new Process.PluginDescribeResult.InputParameter('subject',

            Process.PluginDescribeResult.ParameterType.STRING, true)

           };

        result.outputParameters = new

          List<Process.PluginDescribeResult.OutputParameter>{ };

        return result;

      }

   }

```

Test Class

The following is a test class for the above class.

```
   @isTest

   private class flowChatTest {

      static testmethod void flowChatTests() {

        flowChat plugin = new flowChat();

        Map<String,Object> inputParams = new Map<String,Object>();

        string feedSubject = 'Flow is alive';

        InputParams.put('subject', feedSubject);

        Process.PluginRequest request = new Process.PluginRequest(inputParams);

        plugin.invoke(request);

      }

   }

### PluginDescribeResult Class

```

Describes the input and output parameters for `Process.PluginResult` .


Apex Reference Guide PluginDescribeResult Class

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

IN THIS SECTION:

#### PluginDescribeResult Constructors PluginDescribeResult Properties PluginDescribeResult Constructors The following are constructors for PluginDescribeResult .

IN THIS SECTION:

##### PluginDescribeResult()

Creates a new instance of the `Process.PluginDescribeResult` class.

##### PluginDescribeResult()

Creates a new instance of the `Process.PluginDescribeResult` class.

Signature

```
   public PluginDescribeResult()

#### PluginDescribeResult Properties The following are properties for PluginDescribeResult .

```

IN THIS SECTION:

description
This optional field describes the purpose of the plug-in.

inputParameters
The input parameters passed by the `Process.PluginRequest` class from a flow to the class that implements the
`Process.Plugin` interface.


Apex Reference Guide PluginDescribeResult Class

##### name

Unique name of the plug-in.

outputParameters
The output parameters passed by the `Process.PluginResult` class from the class that implements the `Process.Plugin`
interface to the flow.

##### description

This optional field describes the purpose of the plug-in.

Signature

```
   public String description {get; set;}

```

Property Value

Type: String

Usage

Size limit: 255 characters.

##### inputParameters

The input parameters passed by the `Process.PluginRequest` class from a flow to the class that implements the
`Process.Plugin` interface.

Signature

```
   public List<Process.PluginDescribeResult.InputParameter> inputParameters {get; set;}

```

Property Value

Type: List<Process.PluginDescribeResult.InputParameter>

##### name

Unique name of the plug-in.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

Usage

Size limit: 40 characters.


### Apex Reference Guide PluginDescribeResult.InputParameter Class

##### outputParameters

The output parameters passed by the `Process.PluginResult` class from the class that implements the `Process.Plugin`
interface to the flow.

Signature

```
   public List<Process.PluginDescribeResult.OutputParameter> outputParameters {get; set;}

```

Property Value

Type: List<Process.PluginDescribeResult.OutputParameter>

### PluginDescribeResult.InputParameter Class

Describes the input parameter for `Process.PluginResult` .

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

IN THIS SECTION:

#### PluginDescribeResult.InputParameter Constructors

PluginDescribeResult.InputParameter Properties

#### PluginDescribeResult.InputParameter Constructors

### The following are constructors for PluginDescribeResult.InputParameter .

IN THIS SECTION:

PluginDescribeResult.InputParameter(name, description, parameterType, required)
Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
description, parameter type, and required option.


Apex Reference Guide PluginDescribeResult.InputParameter Class

##### PluginDescribeResult.InputParameter(name, parameterType, required)

Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
parameter type, and required option.

##### PluginDescribeResult.InputParameter(name, description, parameterType, required)

Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
description, parameter type, and required option.

Signature

```
   public PluginDescribeResult.InputParameter(String name, String description,

   Process.PluginDescribeResult.ParameterType parameterType, Boolean required)

```

Parameters

```
   name
```

Type: String

Unique name of the plug-in.

```
   description
```

Type: String

Describes the purpose of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType

The data type of the input parameter.

```
   required
```

Type: Boolean

Set to `true` for required and `false` otherwise.

##### PluginDescribeResult.InputParameter(name, parameterType, required)

Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
parameter type, and required option.

Signature

```
   public PluginDescribeResult.InputParameter(String name,

   Process.PluginDescribeResult.ParameterType parameterType, Boolean required)

```

Parameters

```
   name
```

Type: String

Unique name of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType


Apex Reference Guide PluginDescribeResult.InputParameter Class

The data type of the input parameter.

```
   required
```

Type: Boolean

Set to `true` for required and `false` otherwise.

#### PluginDescribeResult.InputParameter Properties The following are properties for PluginDescribeResult.InputParameter .

IN THIS SECTION:

##### Description

This optional field describes the purpose of the plug-in.

##### Name

Unique name of the plug-in.

ParameterType
The data type of the input parameter.

Required
Set to `true` for required and `false` otherwise.

##### Description

This optional field describes the purpose of the plug-in.

Signature

```
   public String Description {get; set;}

```

Property Value

Type: String

Usage

Size limit: 255 characters.

##### Name

Unique name of the plug-in.

Signature

```
   public String Name {get; set;}

```

Property Value

Type: String


### Apex Reference Guide PluginDescribeResult.OutputParameter Class

Usage

Size limit: 40 characters.

##### **`ParameterType`**

The data type of the input parameter.

Signature

```
   public Process.PluginDescribeResult.ParameterType ParameterType {get; set;}

```

Property Value

Type: Process.PluginDescribeResult.ParameterType

##### Required

Set to `true` for required and `false` otherwise.

Signature

```
   public Boolean Required {get; set;}

```

Property Value

Type: Boolean

### PluginDescribeResult.OutputParameter Class

Describes the output parameter for `Process.PluginResult` .

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.


Apex Reference Guide PluginDescribeResult.OutputParameter Class

IN THIS SECTION:

#### PluginDescribeResult.OutputParameter Constructors

PluginDescribeResult.OutputParameter Properties

#### PluginDescribeResult.OutputParameter Constructors The following are constructors for PluginDescribeResult.OutputParameter .

IN THIS SECTION:

##### PluginDescribeResult.OutputParameter(name, description, parameterType)

Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

##### PluginDescribeResult.OutputParameter(name, parameterType)

Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

##### PluginDescribeResult.OutputParameter(name, description, parameterType)

Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

Signature

```
   public PluginDescribeResult.OutputParameter(String name, String description,

   Process.PluginDescribeResult.ParameterType parameterType)

```

Parameters

```
   name
```

Type: String

Unique name of the plug-in.

```
   description
```

Type: String

Describes the purpose of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType

The data type of the input parameter.

##### PluginDescribeResult.OutputParameter(name, parameterType)

Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.


Apex Reference Guide PluginDescribeResult.OutputParameter Class

Signature

```
   public PluginDescribeResult.OutputParameter(String name,

   Process.PluginDescribeResult.ParameterType parameterType)

```

Parameters

```
   name
```

Type: String

Unique name of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType

The data type of the input parameter.

#### PluginDescribeResult.OutputParameter Properties The following are properties for PluginDescribeResult.OutputParameter .

IN THIS SECTION:

##### Description

This optional field describes the purpose of the plug-in.

##### Name

Unique name of the plug-in.

ParameterType
The data type of the output parameter.

##### Description

This optional field describes the purpose of the plug-in.

Signature

```
   public String Description {get; set;}

```

Property Value

Type: String

Usage

Size limit: 255 characters.

##### Name

Unique name of the plug-in.


### Apex Reference Guide PluginDescribeResult.ParameterType Enum

Signature

```
   public String Name {get; set;}

```

Property Value

Type: String

Usage

Size limit: 40 characters.

##### **`ParameterType`**

The data type of the output parameter.

Signature

```
   public Process.PluginDescribeResult.ParameterType ParameterType {get; set;}

```

Property Value

Type: Process.PluginDescribeResult.ParameterType

### PluginDescribeResult.ParameterType Enum

Specifies the data types of input and output parameters of the `Process.PluginDescribeResult` class.

Enum Values

The following are the values of the `Process.PluginDescribeResult.ParameterType` enum.

**Value** **Description**

`BOOLEAN` A value that can only be assigned `true`, `false`, or `null` .

`DATE` A value that indicates a particular day.

`DATETIME` A value that indicates a particular day and time, such as a timestamp.

`DECIMAL` A number that includes a decimal point. Decimal is an arbitrary precision number.

`DOUBLE` A 64-bit number that includes a decimal point.

`FLOAT` A floating point number.

`ID` Any valid 18-character Lightning Platform record identifier.

`INTEGER` A 32-bit number that doesn’t include a decimal point.

`LONG` A 64-bit number that doesn’t include a decimal point.

`STRING` Any set of characters surrounded by single quotes.

`TIME` A value that indicates a particular time.


### Apex Reference Guide PluginRequest Class PluginRequest Class

Passes input parameters from the class that implements the `Process.Plugin` interface to the flow.

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

#### PluginRequest Properties

### The following are properties for PluginRequest .

IN THIS SECTION:

##### inputParameters

Input parameters that are passed from the class that implements the `Process.Plugin` interface to the flow.

##### inputParameters

Input parameters that are passed from the class that implements the `Process.Plugin` interface to the flow.

Signature

```
   public MAP<String,ANY> inputParameters {get; set;}

```

Property Value

Type: Map<String, Object>

### PluginResult Class

Returns output parameters from the class that implements the `Process.Plugin` interface to the flow.

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.


## Apex Reference Guide QuickAction Namespace

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

Namespace

Process

#### PluginResult Properties The following are properties for PluginResult .

IN THIS SECTION:

##### outputParameters

Output parameters returned from the class that implements the interface to the flow.

##### outputParameters

Output parameters returned from the class that implements the interface to the flow.

Signature

```
   public MAP<String, ANY> outputParameters {get; set;}

```

Property Value

Type: Map<String, Object>

## QuickAction Namespace The QuickAction namespace provides classes and methods for quick actions. The following are the classes in the QuickAction namespace.

IN THIS SECTION:

DescribeAvailableQuickActionResult Class
Contains describe metadata information for a quick action that is available for a specified parent.

DescribeLayoutComponent Class
Represents the smallest unit in a layout—a field or a separator.

DescribeLayoutItem Class
Represents an individual item in a `QuickAction.DescribeLayoutRow` .


### Apex Reference Guide DescribeAvailableQuickActionResult Class

DescribeLayoutRow Class
Represents a row in a `QuickAction.DescribeLayoutSection` .

DescribeLayoutSection Class
Represents a section of a layout and consists of one or more columns and one or more rows (an array of
`QuickAction.DescribeLayoutRow` ).

DescribeQuickActionDefaultValue Class
Returns a default value for a quick action.

DescribeQuickActionParameter Class
Represents the parameters corresponding to a quick action.

DescribeQuickActionResult Class
Contains describe metadata information for a quick action.

QuickActionDefaults Class
Represents an abstract Apex class that provides the context for running the standard Email Action on Case Feed and the container
of the Email Message fields for the action payload. You can override the target fields before the standard Email Action is rendered.

QuickActionDefaultsHandler Interface
The `QuickAction.QuickActionDefaultsHandler` interface lets you specify the default values for the standard Email
and Send Email actions in the case feed. You can use this interface to specify the From address, CC address, BCC address, subject,
and email body for the Email action in the case feed. You can use the interface to pre-populate these fields based on the context
where the action is displayed, such as the case origin (for example, country) and subject.

QuickActionRequest Class
Use the `QuickAction.QuickActionRequest` class for providing action information for quick actions to be performed by
`QuickAction` class methods. Action information includes the action name, context record ID, and record.

QuickActionResult Class
After you initiate a quick action with the `QuickAction` class, use the `QuickActionResult` class for processing action
results.

SendEmailQuickActionDefaults Class
Represents an Apex class that provides: the From address list; the original email’s email message ID, provided that the reply action
was invoked on the email message feed item; and methods to specify related settings on templates. You can override these fields
before the standard Email Action is rendered.

### DescribeAvailableQuickActionResult Class

Contains describe metadata information for a quick action that is available for a specified parent.

Namespace

QuickAction

Usage

The QuickAction `describeAvailableQuickActions` method returns an array of available quick action describe result objects
( `QuickAction.DescribeAvailableQuickActionResult` ).


Apex Reference Guide DescribeAvailableQuickActionResult Class

#### DescribeAvailableQuickActionResult Methods The following are methods for DescribeAvailableQuickActionResult . All are instance methods.

IN THIS SECTION:

##### getActionEnumOrId()

Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

##### getLabel()

The quick action label.

##### getName()

The quick action name.

getType()
The quick action type.

##### getActionEnumOrId()

Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

Signature

```
   public String getActionEnumOrId()

```

Return Value

Type: String

##### getLabel()

The quick action label.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

The quick action name.

Signature

```
   public String getName()

```


### Apex Reference Guide DescribeLayoutComponent Class

Return Value

Type: String

##### getType()

The quick action type.

Signature

```
   public String getType()

```

Return Value

Type: String

### DescribeLayoutComponent Class

Represents the smallest unit in a layout—a field or a separator.

Namespace

QuickAction

#### DescribeLayoutComponent Methods

### The following are methods for DescribeLayoutComponent . All are instance methods.

IN THIS SECTION:

##### getDisplayLines()

Returns the vertical lines displayed for a field. Applies to `textarea` and multi-select picklist fields.

getTabOrder()
Returns the tab order for the item in the row.

##### getType()

Returns the name of the `QuickAction.DescribeLayoutComponent` type for this component.

getValue()
Returns the name of the field if the type for `QuickAction.DescribeLayoutComponent` is `textarea` .

##### getDisplayLines()

Returns the vertical lines displayed for a field. Applies to `textarea` and multi-select picklist fields.

Signature

```
   public Integer getDisplayLines()

```


### Apex Reference Guide DescribeLayoutItem Class

Return Value

Type: Integer

##### getTabOrder()

Returns the tab order for the item in the row.

Signature

```
   public Integer getTabOrder()

```

Return Value

Type: Integer

##### getType()

Returns the name of the `QuickAction.DescribeLayoutComponent` type for this component.

Signature

```
   public String getType()

```

Return Value

Type: String

##### getValue()

Returns the name of the field if the type for `QuickAction.DescribeLayoutComponent` is `textarea` .

Signature

```
   public String getValue()

```

Return Value

Type: String

### DescribeLayoutItem Class

Represents an individual item in a `QuickAction.DescribeLayoutRow` .

Namespace

QuickAction


Apex Reference Guide DescribeLayoutItem Class

Usage

For most fields on a layout, there is only one component per layout item. However, in a display-only view, the
`QuickAction.DescribeLayoutItem` might be a composite of the individual fields (for example, an address can consist of
street, city, state, country, and postal code data). On the corresponding edit view, each component of the address field would be split
up into separate `QuickAction.DescribeLayoutItem` s.

#### DescribeLayoutItem Methods The following are methods for DescribeLayoutItem . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the label text for this item.

##### getLayoutComponents()

Returns a list of `QuickAction.DescribeLayoutComponents` for this item.

isEditableForNew()
Indicates whether this item can be edited for new ( `true` ) or not ( `false` ).

isEditableForUpdate()
Indicates whether this item can be edited for update( `true` ) or not ( `false` ).

isPlaceholder()
Indicates whether this item is a placeholder ( `true` ) or not ( `false` ). If `true`, then this item is blank.

isRequired()
Indicates whether this item is required ( `true` ) or not ( `false` ).

##### getLabel()

Returns the label text for this item.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getLayoutComponents()

Returns a list of `QuickAction.DescribeLayoutComponents` for this item.

Signature

```
   public List<QuickAction.DescribeLayoutComponent> getLayoutComponents()

```


Apex Reference Guide DescribeLayoutItem Class

Return Value

Type: List<QuickAction.DescribeLayoutComponent>

##### isEditableForNew()

Indicates whether this item can be edited for new ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isEditableForNew()

```

Return Value

Type: Boolean

##### isEditableForUpdate()

Indicates whether this item can be edited for update( `true` ) or not ( `false` ).

Signature

```
   public Boolean isEditableForUpdate()

```

Return Value

Type: Boolean

##### isPlaceholder()

Indicates whether this item is a placeholder ( `true` ) or not ( `false` ). If `true`, then this item is blank.

Signature

```
   public Boolean isPlaceholder()

```

Return Value

Type: Boolean

##### isRequired()

Indicates whether this item is required ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isRequired()

```

Return Value

Type: Boolean


### Apex Reference Guide DescribeLayoutRow Class

Usage

This is useful if, for example, you want to render required fields in a contrasting color.

### DescribeLayoutRow Class

Represents a row in a `QuickAction.DescribeLayoutSection` .

Namespace

QuickAction

Usage

A `QuickAction.DescribeLayoutRow` consists of one or more `QuickAction.DescribeLayoutItem` objects. For
each `QuickAction.DescribeLayoutRow`, a `QuickAction.DescribeLayoutItem` refers either to a specific field or
to an “empty” `QuickAction.DescribeLayoutItem` (one that contains no `QuickAction.DescribeLayoutComponent`
objects). An empty `QuickAction.DescribeLayoutItem` can be returned when a given
`QuickAction.DescribeLayoutRow` is sparse (for example, containing more fields on the right column than on the left column).

#### DescribeLayoutRow Methods

### The following are methods for DescribeLayoutRow . All are instance methods.

IN THIS SECTION:

##### getLayoutItems()

Returns either a specific field or an empty `QuickAction.DescribeLayoutItem` (one that contains no
`QuickAction.DescribeLayoutComponent` objects).

##### getNumItems()

Returns the number of `QuickAction.DescribeLayoutItem` .

##### getLayoutItems()

Returns either a specific field or an empty `QuickAction.DescribeLayoutItem` (one that contains no
`QuickAction.DescribeLayoutComponent` objects).

Signature

```
   public List<QuickAction.DescribeLayoutItem> getLayoutItems()

```

Return Value

Type: List<QuickAction.DescribeLayoutItem>

##### getNumItems()

Returns the number of `QuickAction.DescribeLayoutItem` .


### Apex Reference Guide DescribeLayoutSection Class

Signature

```
   public Integer getNumItems()

```

Return Value

Type: Integer

### DescribeLayoutSection Class

Represents a section of a layout and consists of one or more columns and one or more rows (an array of
`QuickAction.DescribeLayoutRow` ).

Namespace

QuickAction

#### DescribeLayoutSection Properties

### The following are properties for DescribeLayoutSection .

##### collapsed

The current view of the record details section: collapsed ( `true` ) or expanded ( `false` ).

Signature

```
   public Boolean collapsed {get; set;}

```

Property Value

Type: Boolean

##### layoutsectionid

The unique ID of the record details section in the layout.

Signature

```
   public Id layoutsectionid {get; set;}

```

Property Value

Type: Id

#### DescribeLayoutSection Methods

### The following are methods for DescribeLayoutSection .


Apex Reference Guide DescribeLayoutSection Class

IN THIS SECTION:

##### getColumns()

Returns the number of columns in the `QuickAction.DescribeLayoutSection` .

##### getHeading()

The heading text (label) for the `QuickAction.DescribeLayoutSection` .

getLayoutRows()
Returns an array of one or more `QuickAction.DescribeLayoutRow` objects.

getLayoutSectionId()
Returns the ID of the record details section in the layout.

getParentLayoutId()
Returns the ID of the layout upon which this `DescribeLayoutSection` resides.

getRows()
Returns the number of rows in the `QuickAction.DescribeLayoutSection` .

isCollapsed()
Indicates whether the record details section is collapsed ( `true` ) or expanded ( `false` ). If you build your own app, you can use this
method to see whether the current user collapsed a section, and respect that preference in your own UI.

isUseCollapsibleSection()
Indicates whether the `QuickAction.DescribeLayoutSection` is a collapsible section ( `true` ) or not ( `false` ).

isUseHeading()
Indicates whether to use the `heading` ( `true` ) or not ( `false` ).

##### getColumns()

Returns the number of columns in the `QuickAction.DescribeLayoutSection` .

Signature

```
   public Integer getColumns()

```

Return Value

Type: Integer

##### getHeading()

The heading text (label) for the `QuickAction.DescribeLayoutSection` .

Signature

```
   public String getHeading()

```

Return Value

Type: String


Apex Reference Guide DescribeLayoutSection Class

##### getLayoutRows()

Returns an array of one or more `QuickAction.DescribeLayoutRow` objects.

Signature

```
   public List<QuickAction.DescribeLayoutRow> getLayoutRows()

```

Return Value

Type: List<QuickAction.DescribeLayoutRow>

##### getLayoutSectionId()

Returns the ID of the record details section in the layout.

Signature

```
   public Id getLayoutSectionId()

```

Return Value

Type: Id

##### getParentLayoutId()

Returns the ID of the layout upon which this `DescribeLayoutSection` resides.

Signature

```
   public Id getParentLayoutId()

```

Return Value

Type: Id

##### getRows()

Returns the number of rows in the `QuickAction.DescribeLayoutSection` .

Signature

```
   public Integer getRows()

```

Return Value

Type: Integer


### Apex Reference Guide DescribeQuickActionDefaultValue Class

##### isCollapsed()

Indicates whether the record details section is collapsed ( `true` ) or expanded ( `false` ). If you build your own app, you can use this
method to see whether the current user collapsed a section, and respect that preference in your own UI.

Signature

```
   public Boolean isCollapsed()

```

Return Value

Type: Boolean

##### isUseCollapsibleSection()

Indicates whether the `QuickAction.DescribeLayoutSection` is a collapsible section ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isUseCollapsibleSection()

```

Return Value

Type: Boolean

##### isUseHeading()

Indicates whether to use the `heading` ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isUseHeading()

```

Return Value

Type: Boolean

### DescribeQuickActionDefaultValue Class

Returns a default value for a quick action.

Namespace

QuickAction

Usage

Represents the default values of fields to use in default layouts.


### Apex Reference Guide DescribeQuickActionParameter Class

#### DescribeQuickActionDefaultValue Methods The following are methods for DescribeQuickActionDefaultValue . All are instance methods.

IN THIS SECTION:

##### getDefaultValue()

Returns the default value of the quick action.

##### getField()

Returns the field name of the action.

##### getDefaultValue()

Returns the default value of the quick action.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getField()

Returns the field name of the action.

Signature

```
   public String getField()

```

Return Value

Type: String

### DescribeQuickActionParameter Class

Represents the parameters corresponding to a quick action.

Namespace

QuickAction

IN THIS SECTION:

DescribeQuickActionParameter Properties
Learn more about the available properties with the `CalculateTaxRequest` class.

DescribeQuickActionParameter Methods


Apex Reference Guide DescribeQuickActionParameter Class

#### DescribeQuickActionParameter Properties

Learn more about the available properties with the `CalculateTaxRequest` class.

#### The following are properties for DescribeQuickActionParameter .The following are properties for DescribeQuickActionParameter .

IN THIS SECTION:

##### parametername

Describes the name of the parameter that can be associated with a specific quick action type. For example, User Utterance is a
parameter that is associated with agent quick actions.

##### parametertype

Describes the type of quick action. The type can either be Input or Output.

##### parametervalue

Describes the value of the parameter associated with the quick action.

##### **`parametername`**

Describes the name of the parameter that can be associated with a specific quick action type. For example, User Utterance is a parameter
that is associated with agent quick actions.

Signature

```
   public String parametername {get; set;}

```

Property Value

Type: String

##### **`parametertype`**

Describes the type of quick action. The type can either be Input or Output.

Signature

```
   public String parametertype {get; set;}

```

Property Value

Type: String

##### **`parametervalue`**

Describes the value of the parameter associated with the quick action.

Signature

```
   public String parametervalue {get; set;}

```


Apex Reference Guide DescribeQuickActionParameter Class

Property Value

Type: String

#### DescribeQuickActionParameter Methods The following are methods for DescribeQuickActionParameter .

IN THIS SECTION:

##### getParameterName()

Returns the name of the parameter associated with the quick action.

##### getParameterType()

Returns the type of the parameter associated with the quick action. This can either be Input or Output.

##### getParameterValue()

Returns the value of the parameter associated with the quick action.

##### **`getParameterName()`**

Returns the name of the parameter associated with the quick action.

Signature

```
   public String getParameterName()

```

Return Value

Type: String

##### **`getParameterType()`**

Returns the type of the parameter associated with the quick action. This can either be Input or Output.

Signature

```
   public String getParameterType()

```

Return Value

Type: String

##### **`getParameterValue()`**

Returns the value of the parameter associated with the quick action.

Signature

```
   public String getParameterValue()

```


### Apex Reference Guide DescribeQuickActionResult Class

Return Value

Type: String

### DescribeQuickActionResult Class

Contains describe metadata information for a quick action.

Namespace

QuickAction

Usage

The QuickAction `describeQuickActions` method returns an array of quick action describe result objects
( `QuickAction.DescribeQuickActionResult` ).

IN THIS SECTION:

#### DescribeQuickActionResult Properties

DescribeQuickActionResult Methods

#### DescribeQuickActionResult Properties

### The following are properties for DescribeQuickActionResult .

IN THIS SECTION:

canvasapplicationname
The name of the Canvas application invoked by the custom action.

colors
Array of color information. Each color is associated with a theme.

contextsobjecttype
The object used for the action. Was `getsourceSobjectType()` in API version 29.0 and earlier.

defaultvalues
The action’s default values.

flowdevname
If the custom action invokes a flow, the fully qualified name of the flow.

flowrecordidvar
If the custom action invokes a flow, the input variable that the custom action passes the record’s ID to.

height
The height in pixels of the action pane.

iconname
The name of the icon used for the action. If a custom icon is not used, this value isn’t set.


Apex Reference Guide DescribeQuickActionResult Class

icons
Array of icons. Each icon is associated with a theme.

iconurl
The URL of the icon used for the action. This icon URL corresponds to the 32x32 icon used for the current Salesforce theme, introduced
in Spring ’10, or the custom icon, if there is one.

layout
The section of the layout where the action resides.

lightningcomponentbundleid
If the custom action invokes an Aura component, the ID of the Aura component bundle to which the component belongs.

lightningcomponentbundlename
If the custom action invokes an Aura component, the name of the Aura component bundle to which the component belongs.

lightningcomponentqualifiedname
The fully qualified name of the Aura component invoked by the custom action.

lightningwebcomponentbundleid
If the custom action invokes a Lightning web component, the ID of the Lightning web component bundle to which the component
belongs.

lightningwebcomponentbundlename
If the custom action invokes a Lightning web component, the name of the Lightning web component bundle to which the component
belongs.

lightningwebcomponentqualifiedname
The fully qualified name of the Lightning web component invoked by the custom action.

miniiconurl
The icon’s URL. This icon URL corresponds to the 16x16 icon used for the current Salesforce theme, introduced in Spring ’10, or the
custom icon, if there is one.

showquickactionlcheader
Indicates whether the Lightning component quick action header and footer are shown. If `false`, then both the header containing
the quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

showquickactionvfheader
Indicates whether the Visualforce quick action header and footer should be shown. If `false`, then both the header containing the
quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

targetparentfield
The parent object type of the action. Links the target object to the parent object. For example, the value is Account if the target
object is Contact and the parent object is Account.

targetrecordtypeid
The record type of the target record.

targetsobjecttype
The action’s target object type.

visualforcepagename
The name of the Visualforce page associated with the custom action.

visualforcepageurl
The URL of the Visualforce page associated with the action.


Apex Reference Guide DescribeQuickActionResult Class

width
The width in pixels of the action pane, for custom actions that call Visualforce pages, Canvas apps, or Lightning components.

##### canvasapplicationname

The name of the Canvas application invoked by the custom action.

Signature

```
   public String canvasapplicationname {get; set;}

```

Property Value

Type: String

##### colors

Array of color information. Each color is associated with a theme.

Signature

```
   public List<Schema.DescribeColorResult> colors {get; set;}

```

Property Value

Type: List<Schema.DescribeColorResult> on page 3466

##### contextsobjecttype

The object used for the action. Was `getsourceSobjectType()` in API version 29.0 and earlier.

Signature

```
   public String contextsobjecttype {get; set;}

```

Property Value

Type: String

##### defaultvalues

The action’s default values.

Signature

```
   public List<QuickAction.DescribeQuickActionDefaultValue> defaultvalues {get; set;}

```

Property Value

Type: List<QuickAction.DescribeQuickActionDefaultValue>


Apex Reference Guide DescribeQuickActionResult Class

##### flowdevname

If the custom action invokes a flow, the fully qualified name of the flow.

Signature

```
   public String flowdevname {get; set;}

```

Property Value

Type: String

##### flowrecordidvar

If the custom action invokes a flow, the input variable that the custom action passes the record’s ID to.

Signature

```
   public String flowrecordidvar {get; set;}

```

Property Value

Type: String

Valid values are _`null`_ or _`recordId`_ .

##### height

The height in pixels of the action pane.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### iconname

The name of the icon used for the action. If a custom icon is not used, this value isn’t set.

Signature

```
   public String iconname {get; set;}

```

Property Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### icons

Array of icons. Each icon is associated with a theme.

Signature

```
   public List<Schema.DescribeIconResult> icons {get; set;}

```

Property Value

Type: List<Schema.DescribeIconResult on page 3489>

If no custom icon was associated with the quick action and the quick action creates a specific object, the icons will correspond to the
##### icons used for the created object. For example, if the quick action creates an Account, the icon array will contain the icons used for

Account.

If a custom icon was associated with the quick action, the array will contain that custom icon.

##### iconurl

The URL of the icon used for the action. This icon URL corresponds to the 32x32 icon used for the current Salesforce theme, introduced
in Spring ’10, or the custom icon, if there is one.

Signature

```
   public String iconurl {get; set;}

```

Property Value

Type: String

##### layout

The section of the layout where the action resides.

Signature

```
   public QuickAction.DescribeLayoutSection layout {get; set;}

```

Property Value

Type: QuickAction.DescribeLayoutSection on page 3248

##### lightningcomponentbundleid

If the custom action invokes an Aura component, the ID of the Aura component bundle to which the component belongs.

Signature

```
   public String lightningcomponentbundleid {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: String

##### lightningcomponentbundlename

If the custom action invokes an Aura component, the name of the Aura component bundle to which the component belongs.

Signature

```
   public String lightningcomponentbundlename {get; set;}

```

Property Value

Type: String

##### lightningcomponentqualifiedname

The fully qualified name of the Aura component invoked by the custom action.

Signature

```
   public String lightningcomponentqualifiedname {get; set;}

```

Property Value

Type: String

##### **`lightningwebcomponentbundleid`**

If the custom action invokes a Lightning web component, the ID of the Lightning web component bundle to which the component
belongs.

Signature

```
   public String lightningwebcomponentbundleid {get; set;}

```

Property Value

Type: String

##### **`lightningwebcomponentbundlename`**

If the custom action invokes a Lightning web component, the name of the Lightning web component bundle to which the component
belongs.

Signature

```
   public String lightningwebcomponentbundlename {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: String

##### **`lightningwebcomponentqualifiedname`**

The fully qualified name of the Lightning web component invoked by the custom action.

Signature

```
   public String lightningwebcomponentqualifiedname {get; set;}

```

Property Value

Type: String

##### miniiconurl

The icon’s URL. This icon URL corresponds to the 16x16 icon used for the current Salesforce theme, introduced in Spring ’10, or the
custom icon, if there is one.

Signature

```
   public String miniiconurl {get; set;}

```

Property Value

Type: String

##### showquickactionlcheader

Indicates whether the Lightning component quick action header and footer are shown. If `false`, then both the header containing the
quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

Signature

```
   public Boolean showquickactionlcheader {get; set;}

```

Property Value

Type: Boolean

##### showquickactionvfheader

Indicates whether the Visualforce quick action header and footer should be shown. If `false`, then both the header containing the
quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

Signature

```
   public Boolean showquickactionvfheader {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: Boolean

##### targetparentfield

The parent object type of the action. Links the target object to the parent object. For example, the value is Account if the target object
is Contact and the parent object is Account.

Signature

```
   public String targetparentfield {get; set;}

```

Property Value

Type: String

##### targetrecordtypeid

The record type of the target record.

Signature

```
   public String targetrecordtypeid {get; set;}

```

Property Value

Type: String

##### targetsobjecttype

The action’s target object type.

Signature

```
   public String targetsobjecttype {get; set;}

```

Property Value

Type: String

##### visualforcepagename

The name of the Visualforce page associated with the custom action.

Signature

```
   public String visualforcepagename {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: String

##### visualforcepageurl

The URL of the Visualforce page associated with the action.

Signature

```
   public String visualforcepageurl {get; set;}

```

Property Value

Type: String

##### width

The width in pixels of the action pane, for custom actions that call Visualforce pages, Canvas apps, or Lightning components.

Signature

```
   public Integer width {get; set;}

```

Property Value

Type: Integer

#### DescribeQuickActionResult Methods The following are methods for DescribeQuickActionResult . All are instance methods.

IN THIS SECTION:

getActionEnumOrId()
Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

getCanvasApplicationName()
Returns the name of the Canvas application, if used.

getColors()
Returns an array of color information. Each color is associated with a theme.

getContextSobjectType()
Returns the object used for the action. Replaces `getsourceSobjectType()` in API version 30.0 and later.

getDefaultValues()
Returns the default values for a action.

getFlowDevName()
If the custom action invokes a flow, returns the fully qualified name of the flow invoked by the custom action.

getFlowRecordIdVar()
If the custom action invokes a flow, returns the input variable that the custom action passes the record’s ID to.


Apex Reference Guide DescribeQuickActionResult Class

getHeight()
Returns the height in pixels of the action pane.

getIconName()
Returns the actions’ icon name.

getIconUrl()
Returns the URL of the 32x32 icon used for the action.

getIcons()
Returns a list of `Schema.DescribeIconResult` objects that describe colors used in a tab.

getLabel()
Returns the action label.

getLayout()
Returns the layout sections that comprise an action.

getLightningComponentBundleId()
If the custom action invokes an Aura component, returns the ID of the Aura component bundle to which the component belongs.

getLightningComponentBundleName()
If the custom action invokes an Aura component, returns the name of the Aura component bundle to which the component belongs.

getLightningComponentQualifiedName()
If the custom action invokes an Aura component, returns the fully qualified name of the Aura component invoked by the custom
action.

getLightningWebComponentBundleId()
If the custom action invokes a Lightning web component, returns the ID of the Lightning web component bundle to which the
component belongs.

getLightningWebComponentBundleName()
If the custom action invokes a Lightning web component, returns the name of the Lightning web component bundle to which the
component belongs.

getLightningWebComponentQualifiedName()
If the custom action invokes a Lightning web component, returns the fully qualified name of the Lightning web component invoked
by the custom action.

getMiniIconUrl()
Returns the 16x16 icon URL.

getName()
Returns the action name.

getShowQuickActionLcHeader()
Returns an indication of whether the Lightning component quick action header and footer are shown.

getShowQuickActionVfHeader()
Returns an indication of whether the Visualforce quick action header and footer should be shown.

getSourceSobjectType()
Returns the object type used for the action.

getTargetParentField()
Returns the parent object’s type for the action.


Apex Reference Guide DescribeQuickActionResult Class

getTargetRecordTypeId()
Returns the record type of the targeted record.

getTargetSobjectType()
Returns the action’s target object type.

getType()
Returns a create or custom Visualforce action.

getVisualforcePageName()
If Visualforce is used, returns the name of the associated page for the action.

getVisualforcePageUrl()
Returns the URL of the Visualforce page associated with the action.

getWidth()
If a custom action is created, returns the width in pixels of the action pane.

##### getActionEnumOrId()

Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

Signature

```
   public String getActionEnumOrId()

```

Return Value

Type: String

##### getCanvasApplicationName()

Returns the name of the Canvas application, if used.

Syntax

```
   public String getCanvasApplicationName()

```

Return Value

Type: String

##### getColors()

Returns an array of color information. Each color is associated with a theme.

Signature

```
   public List<Schema.DescribeColorResult> getColors()

```

Return Value

Type: List <Schema.DescribeColorResult>


Apex Reference Guide DescribeQuickActionResult Class

##### getContextSobjectType()

Returns the object used for the action. Replaces `getsourceSobjectType()` in API version 30.0 and later.

Signature

```
   public String getContextSobjectType()

```

Return Value

Type: String

##### getDefaultValues()

Returns the default values for a action.

Signature

```
   public List<QuickAction.DescribeQuickActionDefaultValue> getDefaultValues()

```

Return Value

Type: List<QuickAction.DescribeQuickActionDefaultValue>

##### getFlowDevName()

If the custom action invokes a flow, returns the fully qualified name of the flow invoked by the custom action.

Signature

```
   public String getFlowDevName()

```

Return Value

Type: String

##### getFlowRecordIdVar()

If the custom action invokes a flow, returns the input variable that the custom action passes the record’s ID to.

Signature

```
   public String getFlowRecordIdVar()

```

Return Value

Type: String

##### getHeight()

Returns the height in pixels of the action pane.


Apex Reference Guide DescribeQuickActionResult Class

Signature

```
   public Integer getHeight()

```

Return Value

Type: Integer

##### getIconName()

Returns the actions’ icon name.

Signature

```
   public String getIconName()

```

Return Value

Type: String

##### getIconUrl()

Returns the URL of the 32x32 icon used for the action.

Signature

```
   public String getIconUrl()

```

Return Value

Type: String

##### getIcons()

Returns a list of `Schema.DescribeIconResult` objects that describe colors used in a tab.

Signature

```
   public List<Schema.DescribeIconResult> getIcons()

```

Return Value

Type: List<Schema.DescribeIconResult>

##### getLabel()

Returns the action label.

Signature

```
   public String getLabel()

```


Apex Reference Guide DescribeQuickActionResult Class

Return Value

Type: String

##### getLayout()

Returns the layout sections that comprise an action.

Signature

```
   public QuickAction.DescribeLayoutSection getLayout()

```

Return Value

Type: QuickAction.DescribeLayoutSection

##### getLightningComponentBundleId()

If the custom action invokes an Aura component, returns the ID of the Aura component bundle to which the component belongs.

Signature

```
   public String getLightningComponentBundleId()

```

Return Value

Type: String

##### getLightningComponentBundleName()

If the custom action invokes an Aura component, returns the name of the Aura component bundle to which the component belongs.

Signature

```
   public String getLightningComponentBundleName()

```

Return Value

Type: String

##### getLightningComponentQualifiedName()

If the custom action invokes an Aura component, returns the fully qualified name of the Aura component invoked by the custom action.

Signature

```
   public String getLightningComponentQualifiedName()

```

Return Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### **`getLightningWebComponentBundleId()`**

If the custom action invokes a Lightning web component, returns the ID of the Lightning web component bundle to which the component
belongs.

Signature

```
   public String getLightningWebComponentBundleId()

```

Return Value

Type: String

##### **`getLightningWebComponentBundleName()`**

If the custom action invokes a Lightning web component, returns the name of the Lightning web component bundle to which the
component belongs.

Signature

```
   public String getLightningWebComponentBundleName()

```

Return Value

Type: String

##### **`getLightningWebComponentQualifiedName()`**

If the custom action invokes a Lightning web component, returns the fully qualified name of the Lightning web component invoked
by the custom action.

Signature

```
   public String getLightningWebComponentQualifiedName()

```

Return Value

Type: String

##### getMiniIconUrl()

Returns the 16x16 icon URL.

Signature

```
   public String getMiniIconUrl()

```

Return Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### getName()

Returns the action name.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getShowQuickActionLcHeader()

Returns an indication of whether the Lightning component quick action header and footer are shown.

Signature

```
   public Boolean getShowQuickActionLcHeader()

```

Return Value

Type: Boolean

If `false`, then both the header containing the quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

##### getShowQuickActionVfHeader()

Returns an indication of whether the Visualforce quick action header and footer should be shown.

Signature

```
   public Boolean getShowQuickActionVfHeader()

```

Return Value

Type: Boolean

If `false`, then both the header containing the quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

##### getSourceSobjectType()

Returns the object type used for the action.

Signature

```
   public String getSourceSobjectType()

```

Return Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### getTargetParentField()

Returns the parent object’s type for the action.

Signature

```
   public String getTargetParentField()

```

Return Value

Type: String

##### getTargetRecordTypeId()

Returns the record type of the targeted record.

Signature

```
   public String getTargetRecordTypeId()

```

Return Value

Type: String

##### getTargetSobjectType()

Returns the action’s target object type.

Signature

```
   public String getTargetSobjectType()

```

Return Value

Type: String

##### getType()

Returns a create or custom Visualforce action.

Signature

```
   public String getType()

```

Return Value

Type: String

##### getVisualforcePageName()

If Visualforce is used, returns the name of the associated page for the action.


### Apex Reference Guide QuickActionDefaults Class

Signature

```
   public String getVisualforcePageName()

```

Return Value

Type: String

##### getVisualforcePageUrl()

Returns the URL of the Visualforce page associated with the action.

Signature

```
   public String getVisualforcePageUrl()

```

Return Value

Type: String

##### getWidth()

If a custom action is created, returns the width in pixels of the action pane.

Signature

```
   public Integer getWidth()

```

Return Value

Type: Integer

### QuickActionDefaults Class

Represents an abstract Apex class that provides the context for running the standard Email Action on Case Feed and the container of
the Email Message fields for the action payload. You can override the target fields before the standard Email Action is rendered.

Namespace

### QuickAction

Usage

Note: You cannot extend this abstract class. You can use the getter methods when using it in the context of
QuickAction.QuickActionDefaultsHandler. Salesforce provides a class that extends this class (See
QuickAction.SendEmailQuickActionDefaults.)

IN THIS SECTION:

QuickActionDefaults Methods


Apex Reference Guide QuickActionDefaults Class

#### QuickActionDefaults Methods The following are methods for QuickActionDefaults .

IN THIS SECTION:

##### getActionName()

Returns the name of the standard Email Action on Case Feed (Case.Email).

##### getActionType()

Returns the type of the standard Email Action on Case Feed (Email).

##### getContextId()

The ID of the context related to the standard Email Action on Case Feed (Case ID).

getTargetSObject()
The target object of the standard Email Action on Case Feed (EmailMessage).

##### getActionName()

Returns the name of the standard Email Action on Case Feed (Case.Email).

Signature

```
   public String getActionName()

```

Return Value

Type: String

##### getActionType()

Returns the type of the standard Email Action on Case Feed (Email).

Signature

```
   public String getActionType()

```

Return Value

Type: String

##### getContextId()

The ID of the context related to the standard Email Action on Case Feed (Case ID).

Signature

```
   public Id getContextId()

```


### Apex Reference Guide QuickActionDefaultsHandler Interface

Return Value

Type: Id

##### getTargetSObject()

The target object of the standard Email Action on Case Feed (EmailMessage).

Signature

```
   public SObject getTargetSObject()

```

Return Value

Type: SObject

### QuickActionDefaultsHandler Interface

The `QuickAction.QuickActionDefaultsHandler` interface lets you specify the default values for the standard Email and
Send Email actions in the case feed. You can use this interface to specify the From address, CC address, BCC address, subject, and email
body for the Email action in the case feed. You can use the interface to pre-populate these fields based on the context where the action
is displayed, such as the case origin (for example, country) and subject.

Namespace

### QuickAction

Usage

To specify default values for the standard Email action in the case feed, create a class that implements
`QuickAction.QuickActionDefaultsHandler` .

The `QuickAction.QuickActionDefaultsHandler` interface works in Salesforce Classic and Lightning Experience.

When working in Lightning Experience, keep the following things in mind:

**•** The interface overrides email values set up with predefined IDs.

**•** The interface works with the out-of-the-box Email action provided on cases. You can also use the interface with custom Email actions
for the case object.

**•** The interface in Lightning Experience doesn’t support:

**–** Email attachments

**–** Custom email fields

**–** Visualforce email templates, which are a type of email template available in Salesforce Classic

**•** The From field determines the from address picklist. While you can’t customize this picklist in Send Email action types via the
QuickActionDefaultsHandler interface, you can customize the From Address field. To customize this field, remove the From field
from the SendEmail quick action layout and add the From Address field instead. Then provide a valid and verified from address in
the QuickActionDefaultsHandler code. This address must be the current user’s address, an organization-wide email address that the
current user has access to, or an Email-to-Case routing address.

**•** If your Apex interface adds content to the email body, merge fields display as unresolved. During preview and send, the merge fields
resolve.


Apex Reference Guide QuickActionDefaultsHandler Interface

When you implement this interface, provide an empty parameterless constructor.

IN THIS SECTION:

#### QuickActionDefaultsHandler Methods QuickActionDefaultsHandler Example Implementations

These examples are implementations of the `QuickAction.QuickActionDefaultsHandler` interface.

#### QuickActionDefaultsHandler Methods The following are methods for QuickActionDefaultsHandler .

IN THIS SECTION:

##### onInitDefaults(actionDefaults)

Implement this method to provide default values for the standard Email action in the case feed.

##### onInitDefaults(actionDefaults)

Implement this method to provide default values for the standard Email action in the case feed.

Signature

```
   public void onInitDefaults(QuickAction.QuickActionDefaults[] actionDefaults)

```

Parameters

```
   actionDefaults
```

Type: QuickAction.QuickActionDefaults[]

This array contains only one item of type `QuickAction.SendEmailQuickActionDefaults` .

Return Value

Type: void

#### QuickActionDefaultsHandler Example Implementations

These examples are implementations of the `QuickAction.QuickActionDefaultsHandler` interface.

##### In this example, the onInitDefaults method checks whether the element passed in the array is for the standard Email action in

the case feed. Then, it performs a query to retrieve the case that corresponds to the context ID. Next, it sets the value of the BCC address
of the corresponding email message to a default value. The default value is based on the case reason. Finally, it sets the default values
##### of the email template properties. The onInitDefaults method determines the default values based on two criteria: first, whether

a reply action on an email message initiated the call to the method, and second, whether any previous emails attached to the case are
associated with the call.

```
   global class EmailPublisherLoader implements QuickAction.QuickActionDefaultsHandler {

      // Empty constructor

      global EmailPublisherLoader() {

      }

```


Apex Reference Guide QuickActionDefaultsHandler Interface

```
      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

        QuickAction.SendEmailQuickActionDefaults sendEmailDefaults = null;

        // Check if the quick action is the standard case feed Email action

        for (Integer j = 0; j < defaults.size(); j++) {

           if (defaults.get(j) instanceof QuickAction.SendEmailQuickActionDefaults &&

            defaults.get(j).getTargetSObject().getSObjectType() ==

               EmailMessage.sObjectType &&

            defaults.get(j).getActionName().equals('Case.Email') &&

            defaults.get(j).getActionType().equals('Email')) {

               sendEmailDefaults =

                 (QuickAction.SendEmailQuickActionDefaults)defaults.get(j);

               break;

           }

        }

        if (sendEmailDefaults != null) {

           Case c = [SELECT Status, Reason FROM Case

                 WHERE Id=:sendEmailDefaults.getContextId()];

          EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

           // Set BCC address to make sure each email goes for audit

           emailMessage.BccAddress = getBccAddress(c.Reason);

           /*

           Set Template related fields

           when the In Reply To Id field is null we know the interface

           is called on page load. Here we check if

           there are any previous emails attached to the case and load

           the 'New_Case_Created' or 'Automatic_Response' template.

           When the In Reply To Id field is not null we know that

           the interface is called on click of reply/reply all

           of an email and we load the 'Default_reply_template' template

           */

           if (sendEmailDefaults.getInReplyToId() == null) {

             Integer emailCount = [SELECT count() FROM EmailMessage

                          WHERE ParentId=:sendEmailDefaults.getContextId()];

             if (emailCount!= null && emailCount > 0) {

               sendEmailDefaults.setTemplateId(

                  getTemplateIdHelper('Automatic_Response'));

             } else {

               sendEmailDefaults.setTemplateId(

                  getTemplateIdHelper('New_Case_Created'));

             }

             sendEmailDefaults.setInsertTemplateBody(false);

             sendEmailDefaults.setIgnoreTemplateSubject(false);

           } else {

             sendEmailDefaults.setTemplateId(

               getTemplateIdHelper('Default_reply_template'));

             sendEmailDefaults.setInsertTemplateBody(false);

```


Apex Reference Guide QuickActionDefaultsHandler Interface

```
             sendEmailDefaults.setIgnoreTemplateSubject(true);

           }

        }

      }

      private Id getTemplateIdHelper(String templateApiName) {

        Id templateId = null;

        try {

           templateId = [select id, name from EmailTemplate

                   where developername = : templateApiName].id;

        } catch (Exception e) {

           system.debug('Unble to locate EmailTemplate using name: ' +

             templateApiName + ' refer to Setup | Communications Templates '

               + templateApiName);

        }

        return templateId;

      }

   private String getBccAddress(String reason) {

        if (reason != null && reason.equals('Technical'))

           { return 'support_technical@mycompany.com'; }

        else if (reason != null && reason.equals('Billing'))

           { return 'support_billing@mycompany.com'; }

        else { return 'support@mycompany.com'; }

      }

   }

```

In this example, the `onInitDefaults` method checks whether the element passed in the array is for the standard Email action in
the case feed. Then it performs a query to determine if the case Priority is set to _`High`_ . If the Priority is set to _`High`_, the email address
_`managers@acme.com`_ is appended to the BCC field.

```
   global class EmailPublisherForHighPriorityCases implements

   QuickAction.QuickActionDefaultsHandler {

      // Empty constructor

      global EmailPublisherForHighPriorityCases() {

      }

      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

        QuickAction.SendEmailQuickActionDefaults sendEmailDefaults =

   (QuickAction.SendEmailQuickActionDefaults)defaults.get(0);

        EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

        Case c = [SELECT CaseNumber, Priority FROM Case WHERE

   Id=:sendEmailDefaults.getContextId()];

        // If case severity is “High,” append “managers@acme.com” to the existing (and

   possibly blank) BCC field

        if (c.Priority != null && c.Priority.equals('High')) { // Priority is 'High'

           emailMessage.BccAddress = 'managers@acme.com';

        }

      }

   }

```


Apex Reference Guide QuickActionDefaultsHandler Interface

In this example, the `onInitDefaults` method checks whether the element passed in the array is for the standard Email action in
the case feed. Then it performs a query to determine if the case Type is set to _`Problem`_ . If the type is set to _`Problem`_, the _`First`_
_`Response`_ email template is inserted into the body of the email.

```
   global class EmailPublisherForCaseType implements QuickAction.QuickActionDefaultsHandler

   {

      // Empty constructor

      global EmailPublisherForCaseType() {

      }

      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

      QuickAction.SendEmailQuickActionDefaults sendEmailDefaults =

   (QuickAction.SendEmailQuickActionDefaults)defaults.get(0);

      EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

     Case c = [SELECT CaseNumber, Type FROM Case WHERE Id=:sendEmailDefaults.getContextId()];

      // If case type is “Problem,” insert the “First Response” email template

      if (c.CaseNumber != null && c.Type.equals('Problem')) {

        sendEmailDefaults.setTemplateId('Insert Email Template ID Here'); // Set the

   template Id corresponding to First Response

        sendEmailDefaults.setInsertTemplateBody(true);

        sendEmailDefaults.setIgnoreTemplateSubject(false);

      }

   }

```

In this example, the `onInitDefaults` method checks whether the element passed in the array is for the standard Email action in
the case feed. Then it performs a query to determine if the email is a Reply or Reply All email. If the email is a Reply or Reply All email,
the corresponding email templates for these emails are inserted into the body of the email.

```
   global class EmailPublisherForReplyAndReplyAll implements

   QuickAction.QuickActionDefaultsHandler {

      // Empty constructor

      global EmailPublisherForReplyAndReplyAll() {

      }

      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

      QuickAction.SendEmailQuickActionDefaults sendEmailDefaults =

   (QuickAction.SendEmailQuickActionDefaults)defaults.get(0);

      EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

      // If the email is a “Reply” email, insert the “Reply Email Template” to the email

   body

      if (sendEmailDefaults.getActionName().equals('EmailMessage._Reply')) {

        sendEmailDefaults.setTemplateId('Insert Reply Email Template ID Here');

        sendEmailDefaults.setInsertTemplateBody(true);

        sendEmailDefaults.setIgnoreTemplateSubject(false);

```


### Apex Reference Guide QuickActionRequest Class

```
      // If the email is a “Reply All” email, insert the “Reply All Email Template” to the

   email body

      } else if (sendEmailDefaults.getActionName().equals('EmailMessage._ReplyAll')) {

        sendEmailDefaults.setTemplateId('Insert Reply All Email Template ID Here');

        sendEmailDefaults.setInsertTemplateBody(true);

        sendEmailDefaults.setIgnoreTemplateSubject(false);

   }

### QuickActionRequest Class

```

Use the `QuickAction.QuickActionRequest` class for providing action information for quick actions to be performed by
### QuickAction class methods. Action information includes the action name, context record ID, and record.

Namespace

### QuickAction

Usage

For Apex saved using Salesforce API version 28.0, a parent ID is associated with the QuickActionRequest instead of the context ID.

The constructor of this class takes no arguments:

```
   QuickAction.QuickActionRequest qar = new QuickAction.QuickActionRequest();

```

Example

In this sample, a new quick action is created to create a contact and assign a record to it.

```
   QuickAction.QuickActionRequest req = new QuickAction.QuickActionRequest();

   // Some quick action name

   req.quickActionName = Schema.Account.QuickAction.AccountCreateContact;

   // Define a record for the quick action to create

   Contact c = new Contact();

   c.lastname = 'last name';

   req.record = c;

   // Provide the context ID (or parent ID). In this case, it is an Account record.

   req.contextid = '001xx000003DGcO';

   QuickAction.QuickActionResult res = QuickAction.performQuickAction(req);

```

IN THIS SECTION:

QuickActionRequest Constructors


Apex Reference Guide QuickActionRequest Class

#### QuickActionRequest Methods

SEE ALSO:

QuickAction Class

#### QuickActionRequest Constructors The following are constructors for QuickActionRequest .

IN THIS SECTION:

##### QuickActionRequest()

Creates a new instance of the `QuickAction.QuickActionRequest` class.

##### QuickActionRequest()

Creates a new instance of the `QuickAction.QuickActionRequest` class.

Signature

```
   public QuickActionRequest()

#### QuickActionRequest Methods The following are methods for QuickActionRequest . All are instance methods.

```

IN THIS SECTION:

##### getContextId()

Returns this QuickAction’s context record ID.

getQuickActionName()
Returns this QuickAction’s name.

getRecord()
Returns the QuickAction’s associated record.

setContextId(contextId)
##### Sets this QuickAction’s context ID. Returned by getContextId .

setQuickActionName(name)
Sets this QuickAction’s name. Returned by `getQuickActionName` .

setRecord(record)
Sets a record for this QuickAction. Returned by `getRecord` .

##### getContextId()

Returns this QuickAction’s context record ID.


Apex Reference Guide QuickActionRequest Class

Signature

```
   public Id getContextId()

```

Return Value

Type: ID

##### getQuickActionName()

Returns this QuickAction’s name.

Signature

```
   public String getQuickActionName()

```

Return Value

Type: String

##### getRecord()

Returns the QuickAction’s associated record.

Signature

```
   public SObject getRecord()

```

Return Value

Type: sObject

##### setContextId(contextId)

Sets this QuickAction’s context ID. Returned by `getContextId` .

Signature

```
   public Void setContextId(Id contextId)

```

Parameters

```
   contextId
```

Type: ID

Return Value

Type: Void

Usage

For Apex saved using Salesforce API version 28.0, sets this QuickAction’s parent ID and is returned by `getParentId` .


### Apex Reference Guide QuickActionResult Class

##### setQuickActionName(name)

Sets this QuickAction’s name. Returned by `getQuickActionName` .

Signature

```
   public Void setQuickActionName(String name)

```

Parameters

```
   name
```

Type: String

Return Value

Type: Void

##### setRecord(record)

Sets a record for this QuickAction. Returned by `getRecord` .

Signature

```
   public Void setRecord(SObject record)

```

Parameters

```
   record
```

Type: sObject

Return Value

Type: Void

### QuickActionResult Class After you initiate a quick action with the QuickAction class, use the QuickActionResult class for processing action results.

Namespace

### QuickAction

SEE ALSO:

QuickAction Class

#### QuickActionResult Methods

### The following are methods for QuickActionResult . All are instance methods.


Apex Reference Guide QuickActionResult Class

IN THIS SECTION:

##### getErrors()

If an error occurs, an array of one or more database error objects, along with error codes and descriptions, is returned.

##### getIds()

The IDs of the QuickActions being processed.

##### getSuccessMessage()

Returns the success message associated with the quick action.

isCreated()
Returns `true` if the action is created; otherwise, `false` .

isSuccess()
Returns `true` if the action completes successfully; otherwise, `false` .

##### getErrors()

If an error occurs, an array of one or more database error objects, along with error codes and descriptions, is returned.

Signature

```
   public List<Database.Error> getErrors()

```

Return Value

Type: List<Database.Error>

##### getIds()

The IDs of the QuickActions being processed.

Signature

```
   public List<Id> getIds()

```

Return Value

Type: List<Id>

##### getSuccessMessage()

Returns the success message associated with the quick action.

Signature

```
   public String getSuccessMessage()

```

Return Value

Type: String


### Apex Reference Guide SendEmailQuickActionDefaults Class

##### isCreated()

Returns `true` if the action is created; otherwise, `false` .

Signature

```
   public Boolean isCreated()

```

Return Value

Type: Boolean

##### isSuccess()

Returns `true` if the action completes successfully; otherwise, `false` .

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### SendEmailQuickActionDefaults Class

Represents an Apex class that provides: the From address list; the original email’s email message ID, provided that the reply action was
invoked on the email message feed item; and methods to specify related settings on templates. You can override these fields before
the standard Email Action is rendered.

Namespace

QuickAction

Usage

Note: You cannot instantiate this class. One can use the getters/setters when using it in the context of
`QuickAction.QuickActionDefaultsHandler` .

IN THIS SECTION:

#### SendEmailQuickActionDefaults Methods SendEmailQuickActionDefaults Methods

### The following are methods for SendEmailQuickActionDefaults .


Apex Reference Guide SendEmailQuickActionDefaults Class

IN THIS SECTION:

##### getFromAddressList()

Returns a list of email addresses that are available in the From: address drop-down menu for the standard Email Action.

##### getInReplyToId()

Returns the email message ID of the email to which the reply/reply all action has been invoked.

##### setIgnoreTemplateSubject(useOriginalSubject)

Specifies whether the template subject should be ignored (true), thus using the original subject, or whether the template subject
should replace the original subject (false).

setInsertTemplateBody(keepOriginalBodyContent)
Specifies whether the template body should be inserted above the original body content (true) or whether it should replace the
entire content with the template body (false).

setTemplateId(templateId)
Sets the email template ID to load into the email body.

##### getFromAddressList()

Returns a list of email addresses that are available in the From: address drop-down menu for the standard Email Action.

Signature

```
   public List<String> getFromAddressList()

```

Return Value

Type: List<String>

##### getInReplyToId()

Returns the email message ID of the email to which the reply/reply all action has been invoked.

Signature

```
   public Id getInReplyToId()

```

Return Value

Type: Id

##### setIgnoreTemplateSubject(useOriginalSubject)

Specifies whether the template subject should be ignored (true), thus using the original subject, or whether the template subject should
replace the original subject (false).

Signature

```
   public void setIgnoreTemplateSubject(Boolean useOriginalSubject)

```


## Apex Reference Guide renew_assets_summary Namespace

Parameters

```
   useOriginalSubject
```

Type: Boolean

Return Value

Type: void

##### setInsertTemplateBody(keepOriginalBodyContent)

Specifies whether the template body should be inserted above the original body content (true) or whether it should replace the entire
content with the template body (false).

Signature

```
   public void setInsertTemplateBody(Boolean keepOriginalBodyContent)

```

Parameters

```
   keepOriginalBodyContent
```

Type: Boolean

Return Value

Type: void

##### setTemplateId(templateId)

Sets the email template ID to load into the email body.

Signature

```
   public void setTemplateId(Id templateId)

```

Parameters

```
   templateId
```

Type: Id

The template ID.

Return Value

Type: void

## renew_assets_summary Namespace

The renew_assets_summary namespace provides classes that retrieve details about renewable assets to create renewal opportunities.

## The renew_assets_summary namespace includes these classes.


## Apex Reference Guide Reports Namespace

**•** [RenewalOpptyDetail Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_renew_assets_summary_RenewalOpptyDetail.htm)

**•** [RenewalPriceDetail Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_renew_assets_summary_RenewalPriceDetail.htm)

## Reports Namespace The Reports namespace provides classes for accessing the same data as is available in the Salesforce Reports and Dashboards REST

API.

## The following are the classes in the Reports namespace.

IN THIS SECTION:

AggregateColumn Class
Contains methods for describing summary fields such as Record Count, Sum, Average, Max, Min, and custom summary formulas.
Includes name, label, data type, and grouping context.

BucketField Class
Contains methods and constructors to work with information about a bucket field, including bucket type, name, and bucketed
values.

BucketFieldValue Class
Contains information about the report values included in a bucket field.

BucketType Enum
The types of values included in a bucket.

ColumnDataType Enum
The `Reports.ColumnDataType` enum describes the type of data in a column. It is returned by the `getDataType` method.

ColumnSortOrder Enum
The `Reports.ColumnSortOrder` enum describes the order that the grouping column uses to sort data.

CrossFilter Class
Contains methods and constructors used to work with information about a cross filter.

CsfGroupType Enum
The group level at which the custom summary format aggregate is displayed in a report.

DateGranularity Enum
The `Reports.DateGranularity` enum describes the date interval that is used for grouping.

DetailColumn Class
Contains methods for describing fields that contain detailed data. Detailed data fields are also listed in the report metadata.

Dimension Class
Contains information for each row or column grouping.

EvaluatedCondition Class
Contains the individual components of an evaluated condition for a report notification, such as the aggregate name and label, the
operator, and the value that the aggregate is compared to.

EvaluatedConditionOperator Enum
The `Reports.EvaluatedConditionOperator` enum describes the type of operator used to compare an aggregate to
a value. It is returned by the `getOperator` method.


Apex Reference Guide Reports Namespace

FilterOperator Class
Contains information about a filter operator, such as display name and API name.

FilterValue Class
Contains information about a filter value, such as the display name and API name.

FormulaType Enum
The format of the numbers in a custom summary formula.

GroupingColumn Class
Contains methods for describing fields that are used for column grouping.

GroupingInfo Class
Contains methods for describing fields that are used for grouping.

GroupingValue Class
Contains grouping values for a row or column, including the key, label, and value.

NotificationAction Interface
Implement this interface to trigger a custom Apex class when the conditions for a report notification are met.

NotificationActionContext Class
Contains information about the report instance and condition threshold for a report notification.

ReportCsf Class
Contains methods and constructors for working with information about a custom summary formula (CSF).

ReportCurrency Class
Contains information about a currency value, including the amount and currency code.

ReportDataCell Class
Contains the data for a cell in the report, including the display label and value.

ReportDescribeResult Class
Contains report, report type, and extended metadata for a tabular, summary, or matrix report.

ReportDetailRow Class
Contains data cells for a detail row of a report.

ReportDivisionInfo Class
Contains information about the divisions that can be used to filter a report.

ReportExtendedMetadata Class
Contains report extended metadata for a tabular, summary, or matrix report.

ReportFact Class
Contains the fact map for the report, which represents the report’s data values.

ReportFactWithDetails Class
Contains the detailed fact map for the report, which represents the report’s data values.

ReportFactWithSummaries Class
Contains the fact map for the report, which represents the report’s data values, and includes summarized fields.

ReportFilter Class
Contains information about a report filter, including column, operator, and value.

ReportFormat Enum
Contains the possible report format types.


Apex Reference Guide Reports Namespace

ReportFilterType Enum
The types of values included in a report filter type.

ReportInstance Class
Returns an instance of a report that was run asynchronously. Retrieves the results for that instance.

ReportManager Class
Runs a report synchronously or asynchronously and with or without details.

ReportMetadata Class
Contains report metadata for a tabular, summary, or matrix report.

ReportResults Class
Contains the results of running a report.

ReportScopeInfo Class
Contains information about possible scope values that you can choose. Scope values depend on the report type. For example, you
can set the scope for opportunity reports to `All opportunities`, `My team’s opportunities`, or `My`
`opportunities` .

ReportScopeValue Class
Contains information about a possible scope value. Scope values depend on the report type. For example, you can set the scope for
opportunity reports to `All opportunities`, `My team’s opportunities`, or `My opportunities` .

ReportType Class
Contains the unique API name and display name for the report type.

ReportTypeColumn Class
Contains detailed report type metadata about a field, including data type, display name, and filter values.

ReportTypeColumnCategory Class
Information about categories of fields in a report type.

ReportTypeMetadata Class
Contains report type metadata, which gives you information about the fields that are available in each section of the report type,
plus filter information for those fields.

SortColumn Class
Contains information about the sort column used in the report.

StandardDateFilter Class
Contains information about standard date filter available in the report—for example, the API name, start date, and end date of the
standard date filter duration as well as the API name of the date field on which the filter is placed.

StandardDateFilterDuration Class
Contains information about each standard date filter—also referred to as a relative date filter. It contains the API name and display
label of the standard date filter duration as well as the start and end dates.

StandardDateFilterDurationGroup Class
Contains information about the standard date filter groupings, such as the grouping display label and all standard date filters that
fall under the grouping. Groupings include `Calendar Year`, `Calendar Quarter`, `Calendar Month`, `Calendar`
`Week`, `Fiscal Year`, `Fiscal Quarter`, `Day`, and custom values based on user-defined date ranges.

StandardFilter Class
Contains information about the standard filter defined in the report, such as the filter field API name and filter value.

StandardFilterInfo Class
Is an abstract base class for an object that provides standard filter information.


### Apex Reference Guide AggregateColumn Class

StandardFilterInfoPicklist Class
Contains information about the standard filter picklist, such as the display name and type of the filter field, the default picklist value,
and a list of all possible picklist values.

StandardFilterType Enum
The `StandardFilterType` enum describes the type of standard filters in a report. The `getType()` method returns a
`Reports.StandardFilterType` enum value.

SummaryValue Class
Contains summary data for a cell of the report.

ThresholdInformation Class
Contains a list of evaluated conditions for a report notification.

TopRows Class
Contains methods and constructors for working with information about a row limit filter.

Reports Exceptions
The `Reports` namespace contains exception classes.

### AggregateColumn Class

Contains methods for describing summary fields such as Record Count, Sum, Average, Max, Min, and custom summary formulas. Includes
name, label, data type, and grouping context.

Namespace

Reports

#### AggregateColumn Methods

### The following are methods for AggregateColumn . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the summary field.

getLabel()
Returns the localized display name for the summarized or custom summary formula field.

getDataType()
Returns the data type of the summarized or custom summary formula field.

getAcrossGroupingContext()
Returns the column grouping in the report where the summary field is displayed.

getDownGroupingContext()
Returns the row grouping in the report where the summary field is displayed.

##### getName()

Returns the unique API name of the summary field.


Apex Reference Guide AggregateColumn Class

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name for the summarized or custom summary formula field.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getDataType()

Returns the data type of the summarized or custom summary formula field.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

##### getAcrossGroupingContext()

Returns the column grouping in the report where the summary field is displayed.

Syntax

```
   public String getAcrossGroupingContext()

```

Return Value

Type: String

##### getDownGroupingContext()

Returns the row grouping in the report where the summary field is displayed.

Syntax

```
   public String getDownGroupingContext()

```


### Apex Reference Guide BucketField Class

Return Value

Type: String

### BucketField Class

Contains methods and constructors to work with information about a bucket field, including bucket type, name, and bucketed values.

Namespace

Reports

IN THIS SECTION:

#### BucketField Constructors

BucketField Methods

#### BucketField Constructors

### The following are constructors for BucketField .

IN THIS SECTION:

##### BucketField(bucketType, devloperName, label, nullTreatedAsZero, otherBucketLabel, sourceColumnName, values)

Creates an instance of the `Reports.BucketField` class using the specified parameters.

BucketField()
Creates an instance of the `Reports.BucketField` class. You can then set values by using the class’s `set` methods.

##### BucketField(bucketType, devloperName, label, nullTreatedAsZero, otherBucketLabel,

sourceColumnName, values)

Creates an instance of the `Reports.BucketField` class using the specified parameters.

Signature

```
   public BucketField(Reports.BucketType bucketType, String devloperName, String label,

   Boolean nullTreatedAsZero, String otherBucketLabel, String sourceColumnName,

   List<Reports.BucketFieldValue> values)

```

Parameters

```
   bucketType
```

Type: Reports.BucketType

The type of bucket.

```
   devloperName
```

Type: String

API name of the bucket.


Apex Reference Guide BucketField Class

```
   label
```

Type: String

User-facing name of the bucket.

```
   nullTreatedAsZero
```

Type: Boolean

Specifies whether null values are converted to zero ( `true` ) or not ( `false` ).

```
   otherBucketLabel
```

Type: String

Name of the fields grouped as `Other` (in buckets of `BucketType PICKLIST` ).

```
   sourceColumnName
```

Type: String

Name of the bucketed field.

```
   values
```

Type: List<Reports.BucketType>

Types of the values included in the bucket.

##### BucketField()

Creates an instance of the `Reports.BucketField` class. You can then set values by using the class’s `set` methods.

Signature

```
   public BucketField()

#### BucketField Methods

##### The following are methods for BucketField .

```

IN THIS SECTION:

getBucketType()
Returns the bucket type.

getDevloperName()
Returns the bucket’s API name.

getLabel()
Returns the user-facing name of the bucket.

getNullTreatedAsZero()
Returns `true` if null values are converted to the number zero, otherwise returns `false` .

getOtherBucketLabel()
Returns the name of fields grouped as `Other` in buckets of type `PICKLIST` .

getSourceColumnName()
Returns the API name of the bucketed field.


Apex Reference Guide BucketField Class

getValues()
Returns the report values grouped by the bucket field.

setBucketType(value)
Sets the `BucketType` of the bucket.

setBucketType(bucketType)
Sets the `BucketType` of the bucket.

setDevloperName(devloperName)
Sets the API name of the bucket.

setLabel(label)
Sets the user-facing name of the bucket.

setNullTreatedAsZero(nullTreatedAsZero)
Specifies whether null values in the bucket are converted to zero ( `true` ) or not ( `false` ).

setOtherBucketLabel(otherBucketLabel)
Sets the name of the fields grouped as `Other` (in buckets of `BucketType PICKLIST` ).

setSourceColumnName(sourceColumnName)
Specifies the name of the bucketed field.

setValues(values)
Specifies which type of values are included in the bucket.

toString()
Returns a string.

##### getBucketType()

Returns the bucket type.

Signature

```
   public Reports.BucketType getBucketType()

```

Return Value

Type: Reports.BucketType

##### getDevloperName()

Returns the bucket’s API name.

Signature

```
   public String getDevloperName()

```

Return Value

Type: String


Apex Reference Guide BucketField Class

##### getLabel()

Returns the user-facing name of the bucket.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getNullTreatedAsZero()

Returns `true` if null values are converted to the number zero, otherwise returns `false` .

Signature

```
   public Boolean getNullTreatedAsZero()

```

Return Value

Type: Boolean

##### getOtherBucketLabel()

Returns the name of fields grouped as `Other` in buckets of type `PICKLIST` .

Signature

```
   public String getOtherBucketLabel()

```

Return Value

Type: String

##### getSourceColumnName()

Returns the API name of the bucketed field.

Signature

```
   public String getSourceColumnName()

```

Return Value

Type: String

##### getValues()

Returns the report values grouped by the bucket field.


Apex Reference Guide BucketField Class

Signature

```
   public List<Reports.BucketFieldValue> getValues()

```

Return Value

Type: List on page 3992<Reports.BucketFieldValue>

##### setBucketType(value)

Sets the `BucketType` of the bucket.

Signature

```
   public void setBucketType(String value)

```

Parameters

```
   value
```

Type: String

See the Reports.BucketType enum for valid values.

Return Value

Type: void

##### setBucketType(bucketType)

Sets the `BucketType` of the bucket.

Signature

```
   public void setBucketType(Reports.BucketType bucketType)

```

Parameters

```
   bucketType
```

Type: Reports.BucketType

Return Value

Type: void

##### setDevloperName(devloperName)

Sets the API name of the bucket.

Signature

```
   public void setDevloperName(String devloperName)

```


Apex Reference Guide BucketField Class

Parameters

```
   devloperName
```

Type: String

The API name to assign to the bucket.

Return Value

Type: void

##### setLabel(label)

Sets the user-facing name of the bucket.

Signature

```
   public void setLabel(String label)

```

Parameters

```
   label
```

Type: String

Return Value

Type: void

##### setNullTreatedAsZero(nullTreatedAsZero)

Specifies whether null values in the bucket are converted to zero ( `true` ) or not ( `false` ).

Signature

```
   public void setNullTreatedAsZero(Boolean nullTreatedAsZero)

```

Parameters

```
   nullTreatedAsZero
```

Type: Boolean

Return Value

Type: void

##### setOtherBucketLabel(otherBucketLabel)

Sets the name of the fields grouped as `Other` (in buckets of `BucketType PICKLIST` ).

Signature

```
   public void setOtherBucketLabel(String otherBucketLabel)

```


Apex Reference Guide BucketField Class

Parameters

```
   otherBucketLabel
```

Type: String

Return Value

Type: void

##### setSourceColumnName(sourceColumnName)

Specifies the name of the bucketed field.

Signature

```
   public void setSourceColumnName(String sourceColumnName)

```

Parameters

```
   sourceColumnName
```

Type: String

Return Value

Type: void

##### setValues(values)

Specifies which type of values are included in the bucket.

Signature

```
   public void setValues(List<Reports.BucketFieldValue> values)

```

Parameters

```
   values
```

Type: List on page 3992<Reports.BucketFieldValue>

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```


### Apex Reference Guide BucketFieldValue Class

Return Value

Type: String

### BucketFieldValue Class

Contains information about the report values included in a bucket field.

Namespace

Reports

IN THIS SECTION:

#### BucketFieldValue Constructors

BucketFieldValue Methods

#### BucketFieldValue Constructors

### The following are constructors for BucketFieldValue .

IN THIS SECTION:

##### BucketFieldValue(label, sourceDimensionValues, rangeUpperBound)

Creates an instance of the `Reports.BucketFieldValue` class using the specified parameters.

BucketFieldValue()
Creates an instance of the `Reports.BucketFieldValue` class. You can then set values by using the class’s `set` methods.

##### BucketFieldValue(label, sourceDimensionValues, rangeUpperBound)

Creates an instance of the `Reports.BucketFieldValue` class using the specified parameters.

Signature

```
   public BucketFieldValue(String label, List<String> sourceDimensionValues, Double

   rangeUpperBound)

```

Parameters

```
   label
```

Type: String

The user-facing name of the bucket.

```
   sourceDimensionValues
```

Type: List on page 3992<String>

A list of the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type `TEXT` ).

```
   rangeUpperBound
```

Type: Double


Apex Reference Guide BucketFieldValue Class

The greatest range limit under which values are included in this bucket category (in buckets of type `NUMBER` ).

##### BucketFieldValue()

Creates an instance of the `Reports.BucketFieldValue` class. You can then set values by using the class’s `set` methods.

Signature

```
   public BucketFieldValue()

#### BucketFieldValue Methods

##### The following are methods for BucketFieldValue .

```

IN THIS SECTION:

##### getLabel()

Returns the user-facing name of the bucket category.

getRangeUpperBound()
Returns the greatest range limit under which values are included in this bucket category (in buckets of type `NUMBER` ).

getSourceDimensionValues()
Returns a list of the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of
type `TEXT` ).

setLabel(label)
Set the user-facing name of the bucket category.

setRangeUpperBound(rangeUpperBound)
Sets the greatest limit of a range under which values are included in this bucket category (in buckets of type `NUMBER` ).

setSourceDimensionValues(sourceDimensionValues)
Specifies the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type
`TEXT` ).

toString()
Returns a string.

##### getLabel()

Returns the user-facing name of the bucket category.

Signature

```
   public String getLabel()

```

Return Value

Type: String


Apex Reference Guide BucketFieldValue Class

##### getRangeUpperBound()

Returns the greatest range limit under which values are included in this bucket category (in buckets of type `NUMBER` ).

Signature

```
   public Double getRangeUpperBound()

```

Return Value

Type: Double

##### getSourceDimensionValues()

Returns a list of the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type
`TEXT` ).

Signature

```
   public List<String> getSourceDimensionValues()

```

Return Value

Type: List<String>

##### setLabel(label)

Set the user-facing name of the bucket category.

Signature

```
   public void setLabel(String label)

```

Parameters

```
   label
```

Type: String

Return Value

Type: void

##### setRangeUpperBound(rangeUpperBound)

Sets the greatest limit of a range under which values are included in this bucket category (in buckets of type `NUMBER` ).

Signature

```
   public void setRangeUpperBound(Double rangeUpperBound)

```


### Apex Reference Guide BucketType Enum

Parameters

```
   rangeUpperBound
```

Type: Double

Return Value

Type: void

##### setSourceDimensionValues(sourceDimensionValues)

Specifies the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type `TEXT` ).

Signature

```
   public void setSourceDimensionValues(List<String> sourceDimensionValues)

```

Parameters

```
   sourceDimensionValues
```

Type: List<String>

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### BucketType Enum

The types of values included in a bucket.

Enum Values

The following are the values of the `Reports.BucketType` enum.

**Value** **Description**

`NUMBER` Numeric values

`PICKLIST` Picklist values


### Apex Reference Guide ColumnDataType Enum

**Value** **Description**

`TEXT` String values

### ColumnDataType Enum

The `Reports.ColumnDataType` enum describes the type of data in a column. It is returned by the `getDataType` method.

Namespace

Reports

Enum Values

The following are the values of the `Reports.ColumnDataType` enum.

**Value** **Description**

`BOOLEAN_DATA` Boolean ( `true` or `false` ) values

`COMBOBOX_DATA` Comboboxes, which provide a set of enumerated values and enable the user to
specify a value that is not in the list

`CURRENCY_DATA` Currency values

`DATETIME_DATA` DateTime values

`DATE_DATA` Date values

`DOUBLE_DATA` Double values

`EMAIL_DATA` Email addresses

`ID_DATA` An object’s Salesforce ID

`INT_DATA` Integer values

`MULTIPICKLIST_DATA` Multi-select picklists, which provide a set of enumerated values from which multiple
values can be selected

`PERCENT_DATA` Percent values

`PHONE_DATA` Phone numbers. Values can include alphabetic characters. Client applications are
responsible for phone number formatting.

`PICKLIST_DATA` Single-select picklists, which provide a set of enumerated values from which only
one value can be selected

`REFERENCE_DATA` Cross-references to another object, analogous to a foreign key field

`STRING_DATA` String values

`TEXTAREA_DATA` String values that are displayed as multiline text fields

`TIME_DATA` Time values


### Apex Reference Guide ColumnSortOrder Enum

**Value** **Description**

`URL_DATA` URL values that are displayed as hyperlinks

### ColumnSortOrder Enum

The `Reports.ColumnSortOrder` enum describes the order that the grouping column uses to sort data.

Namespace

Reports

Usage

The `GroupingInfo.getColumnSortOrder()` method returns a `Reports.ColumnSortOrder` enum value. The
`GroupingInfo.setColumnSortOrder()` method takes the enum value as an argument.

Enum Values

The following are the values of the `Reports.ColumnSortOrder` enum.

**Value** **Description**

`ASCENDING` Sort data in ascending order (A–Z)

`DESCENDING` Sort data in descending order (Z–A)

### CrossFilter Class

Contains methods and constructors used to work with information about a cross filter.

Namespace

Reports

IN THIS SECTION:

#### CrossFilter Constructors

CrossFilter Methods

#### CrossFilter Constructors

### The following are constructors for CrossFilter .

IN THIS SECTION:

CrossFilter(criteria, includesObject, primaryEntityField, relatedEntity, relatedEntityJoinField)
Creates an instance of the `Reports.CrossFilter` class using the specified parameters.


Apex Reference Guide CrossFilter Class

##### CrossFilter()

Creates an instance of the `Reports.CrossFilter` class. You can then set values by using the class’s `set` methods.

##### CrossFilter(criteria, includesObject, primaryEntityField, relatedEntity, relatedEntityJoinField)

Creates an instance of the `Reports.CrossFilter` class using the specified parameters.

Signature

```
   public CrossFilter(List<Reports.ReportFilter> criteria, Boolean includesObject, String

   primaryEntityField, String relatedEntity, String relatedEntityJoinField)

```

Parameters

```
   criteria
```

Type: List<Reports.ReportFilter>

Information about how to filter the `relatedEntity` . Relates the primary entity with a subset of the `relatedEntity` .

```
   includesObject
```

Type: Boolean

Specifies whether objects returned have a relationship with the `relatedEntity` ( `true) or not (false).`

```
   primaryEntityField
```

Type: String

The name of the object on which the cross filter is evaluated.

```
   relatedEntity
```

Type: String

The name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

```
   relatedEntityJoinField
```

Type: String

The name of the field used to join the `primaryEntityField` and `relatedEntity` .

##### CrossFilter()

Creates an instance of the `Reports.CrossFilter` class. You can then set values by using the class’s `set` methods.

Signature

```
   public CrossFilter()

#### CrossFilter Methods

##### The following are methods for CrossFilter .

```


Apex Reference Guide CrossFilter Class

IN THIS SECTION:

##### getCriteria()

Returns information about how to filter the `relatedEntity` . Describes the subset of the `relatedEntity` which the primary
entity is evaluated against.

##### getIncludesObject()

Returns `true` if primary object has a relationship with the `relatedEntity`, otherwise returns `false` .

getPrimaryEntityField()
Returns the name of the object on which the cross filter is evaluated.

getRelatedEntity()
Returns name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

getRelatedEntityJoinField()
Returns the name of the field used to join the `primaryEntityField` and `relatedEntity` .

setCriteria(criteria)
Specifis how to filter the `relatedEntity` . Relates the primary entity with a subset of the `relatedEntity` .

setIncludesObject(includesObject)
Specifies whether objects returned have a relationship with the `relatedEntity` ( `true` ) or not ( `false` ).

setPrimaryEntityField(primaryEntityField)
Specifies the name of the object on which the cross filter is evaluated.

setRelatedEntity(relatedEntity)
Specifies the name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

setRelatedEntityJoinField(relatedEntityJoinField)
Specifies the name of the field used to join the `primaryEntityField` and `relatedEntity` .

toString()
Returns a string.

##### getCriteria()

Returns information about how to filter the `relatedEntity` . Describes the subset of the `relatedEntity` which the primary
entity is evaluated against.

Signature

```
   public List<Reports.ReportFilter> getCriteria()

```

Return Value

Type: List<Reports.ReportFilter>

##### getIncludesObject()

Returns `true` if primary object has a relationship with the `relatedEntity`, otherwise returns `false` .

Signature

```
   public Boolean getIncludesObject()

```


Apex Reference Guide CrossFilter Class

Return Value

Type: Boolean

##### getPrimaryEntityField()

Returns the name of the object on which the cross filter is evaluated.

Signature

```
   public String getPrimaryEntityField()

```

Return Value

Type: String

##### getRelatedEntity()

Returns name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

Signature

```
   public String getRelatedEntity()

```

Return Value

Type: String

##### getRelatedEntityJoinField()

Returns the name of the field used to join the `primaryEntityField` and `relatedEntity` .

Signature

```
   public String getRelatedEntityJoinField()

```

Return Value

Type: String

##### setCriteria(criteria)

Specifis how to filter the `relatedEntity` . Relates the primary entity with a subset of the `relatedEntity` .

Signature

```
   public void setCriteria(List<Reports.ReportFilter> criteria)

```


Apex Reference Guide CrossFilter Class

Parameters

```
   criteria
```

Type: List<Reports.ReportFilter>

Return Value

Type: void

##### setIncludesObject(includesObject)

Specifies whether objects returned have a relationship with the `relatedEntity` ( `true` ) or not ( `false` ).

Signature

```
   public void setIncludesObject(Boolean includesObject)

```

Parameters

```
   includesObject
```

Type: Boolean

Return Value

Type: void

##### setPrimaryEntityField(primaryEntityField)

Specifies the name of the object on which the cross filter is evaluated.

Signature

```
   public void setPrimaryEntityField(String primaryEntityField)

```

Parameters

```
   primaryEntityField
```

Type: String

Return Value

Type: void

##### setRelatedEntity(relatedEntity)

Specifies the name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

Signature

```
   public void setRelatedEntity(String relatedEntity)

```


### Apex Reference Guide CsfGroupType Enum

Parameters

```
   relatedEntity
```

Type: String

Return Value

Type: void

##### setRelatedEntityJoinField(relatedEntityJoinField)

Specifies the name of the field used to join the `primaryEntityField` and `relatedEntity` .

Signature

```
   public void setRelatedEntityJoinField(String relatedEntityJoinField)

```

Parameters

```
   relatedEntityJoinField
```

Type: String

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### CsfGroupType Enum

The group level at which the custom summary format aggregate is displayed in a report.

Enum Values

The following are the values of the `Reports.CsfGroupType` enum.

**Value** **Description**

`ALL` The aggregate is displayed at the end of every summary row.

`CUSTOM` The aggregate is displayed at specified grouping levels.


### Apex Reference Guide DateGranularity Enum

**Value** **Description**

`GRAND_TOTAL` The aggregate is displayed only at the grand total level.

### DateGranularity Enum

The `Reports.DateGranularity` enum describes the date interval that is used for grouping.

Namespace

Reports

Usage

The `GroupingInfo.getDateGranularity` method returns a `Reports.DateGranularity` enum value. The
`GroupingInfo.setDateGranularity` method takes the enum value as an argument.

Enum Values

The following are the values of the `Reports.DateGranularity` enum.

**Value** **Description**

`DAY` The day of the week (Monday–Sunday)

`DAY_IN_MONTH` The day of the month (1–31)

`FISCAL_PERIOD` The fiscal period

`FISCAL_QUARTER` The fiscal quarter

`FISCAL_WEEK` The fiscal week

`FISCAL_YEAR` The fiscal year

`MONTH` The month (January–December)

`MONTH_IN_YEAR` The month number (1–12)

`NONE` No date grouping

`QUARTER` The quarter number (1–4)

`WEEK` The week number (1–52)

`YEAR` The year number (####)

### DetailColumn Class

Contains methods for describing fields that contain detailed data. Detailed data fields are also listed in the report metadata.


Apex Reference Guide DetailColumn Class

Namespace

Reports

#### DetailColumn Instance Methods The following are instance methods for DetailColumn . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the detail column field.

##### getLabel()

Returns the localized display name of a standard field, the ID of a custom field, or the API name of a bucket field that has detailed
data.

##### getDataType()

Returns the data type of a detail column field.

##### getName()

Returns the unique API name of the detail column field.

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name of a standard field, the ID of a custom field, or the API name of a bucket field that has detailed data.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getDataType()

Returns the data type of a detail column field.

Syntax

```
   public Reports.ColumnDataType getDataType()

```


### Apex Reference Guide Dimension Class

Return Value

Type: Reports.ColumnDataType

### Dimension Class

Contains information for each row or column grouping.

Namespace

Reports

#### Dimension Methods

### The following are methods for Dimension . All are instance methods.

IN THIS SECTION:

##### getGroupings()

Returns information for each row or column grouping as a list.

##### getGroupings()

Returns information for each row or column grouping as a list.

Syntax

```
   public List<Reports.GroupingValue> getGroupings()

```

Return Value

Type: List<Reports.GroupingValue>

### EvaluatedCondition Class

Contains the individual components of an evaluated condition for a report notification, such as the aggregate name and label, the
operator, and the value that the aggregate is compared to.

Namespace

Reports

IN THIS SECTION:

EvaluatedCondition Constructors

EvaluatedCondition Methods


Apex Reference Guide EvaluatedCondition Class

#### EvaluatedCondition Constructors The following are constructors for EvaluatedCondition .

IN THIS SECTION:

##### EvaluatedCondition(aggregateName, aggregateLabel, compareToValue, aggregateValue, displayCompareTo, displayValue, operator)

Creates a new instance of the `Reports.EvaluatedConditions` class using the specified parameters.

##### EvaluatedCondition(aggregateName, aggregateLabel, compareToValue, aggregateValue,

displayCompareTo, displayValue, operator)

Creates a new instance of the `Reports.EvaluatedConditions` class using the specified parameters.

Signature

```
   public EvaluatedCondition(String aggregateName, String aggregateLabel, Double

   compareToValue, Double aggregateValue, String displayCompareTo, String displayValue,

   Reports.EvaluatedConditionOperator operator)

```

Parameters

```
   aggregateName
```

Type: String

The unique API name of the aggregate.

```
   aggregateLabel
```

Type: String

The localized display name of the aggregate.

```
   compareToValue
```

Type: Double

The value that the aggregate is compared to in the condition.

```
   aggregateValue
```

Type: Double

The actual value of the aggregate when the report is run.

```
   displayCompareTo
```

Type: String

The value that the aggregate is compared to in the condition, formatted for display. For example, a display value for a currency is
$20.00 or USD20.00 instead of 20.00.

```
   displayValue
```

Type: String

The value of the aggregate when the report is run, formatted for display. For example, a display value for a currency is $20.00 or
USD20.00 instead of 20.00.

```
   operator
```

Type: Reports.EvaluatedConditionOperator

The operator used in the condition.


Apex Reference Guide EvaluatedCondition Class

#### EvaluatedCondition Methods The following are methods for EvaluatedCondition .

IN THIS SECTION:

##### getAggregateLabel()

Returns the localized display name of the aggregate.

##### getAggregateName()

Returns the unique API name of the aggregate.

getCompareTo()
Returns the value that the aggregate is compared to in the condition.

getDisplayCompareTo()
Returns the value that the aggregate is compared to in the condition, formatted for display. For example, a display value for a currency
is $20.00 or USD20.00 instead of 20.00.

getDisplayValue()
Returns the value of the aggregate when the report is run, formatted for display. For example, a display value for a currency is $20.00
or USD20.00 instead of 20.00.

getOperator()
Returns the operator used in the condition.

getValue()
Returns the actual value of the aggregate when the report is run.

##### getAggregateLabel()

Returns the localized display name of the aggregate.

Signature

```
   public String getAggregateLabel()

```

Return Value

Type: String

##### getAggregateName()

Returns the unique API name of the aggregate.

Signature

```
   public String getAggregateName()

```

Return Value

Type: String


Apex Reference Guide EvaluatedCondition Class

##### getCompareTo()

Returns the value that the aggregate is compared to in the condition.

Signature

```
   public Double getCompareTo()

```

Return Value

Type: Double

##### getDisplayCompareTo()

Returns the value that the aggregate is compared to in the condition, formatted for display. For example, a display value for a currency
is $20.00 or USD20.00 instead of 20.00.

Signature

```
   public String getDisplayCompareTo()

```

Return Value

Type: String

##### getDisplayValue()

Returns the value of the aggregate when the report is run, formatted for display. For example, a display value for a currency is $20.00 or
USD20.00 instead of 20.00.

Signature

```
   public String getDisplayValue()

```

Return Value

Type: String

##### getOperator()

Returns the operator used in the condition.

Signature

```
   public Reports.EvaluatedConditionOperator getOperator()

```

Return Value

Type: Reports.EvaluatedConditionOperator


### Apex Reference Guide EvaluatedConditionOperator Enum

##### getValue()

Returns the actual value of the aggregate when the report is run.

Signature

```
   public Double getValue()

```

Return Value

Type: Double

### EvaluatedConditionOperator Enum

The `Reports.EvaluatedConditionOperator` enum describes the type of operator used to compare an aggregate to a
value. It is returned by the `getOperator` method.

Namespace

Reports

Enum Values

The following are the values of the `Reports.EvaluatedConditionOperator` enum.

**Value** **Description**

`EQUAL` Equality operator.

`GREATER_THAN` Greater than operator.

`GREATER_THAN_EQUAL` Greater than or equal to operator.

`LESS_THAN` Less than operator.

`LESS_THAN_EQUAL` Less than or equal to operator.

`NOT_EQUAL` Inequality operator.

### FilterOperator Class

Contains information about a filter operator, such as display name and API name.

Namespace

Reports

#### FilterOperator Methods

### The following are methods for FilterOperator . All are instance methods.


### Apex Reference Guide FilterValue Class

IN THIS SECTION:

##### getLabel()

Returns the localized display name of the filter operator. Possible values for this name are restricted based on the data type of the
column being filtered.

##### getName()

Returns the unique API name of the filter operator. Possible values for this name are restricted based on the data type of the column
being filtered. For example `multipicklist` fields can use the following filter operators: “equals,” “not equal to,” “includes,” and
“excludes.” Bucket fields are considered to be of the `String` type.

##### getLabel()

Returns the localized display name of the filter operator. Possible values for this name are restricted based on the data type of the column
being filtered.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique API name of the filter operator. Possible values for this name are restricted based on the data type of the column
being filtered. For example `multipicklist` fields can use the following filter operators: “equals,” “not equal to,” “includes,” and
“excludes.” Bucket fields are considered to be of the `String` type.

Syntax

```
   public String getName()

```

Return Value

Type: String

### FilterValue Class

Contains information about a filter value, such as the display name and API name.

Namespace

Reports

#### FilterValue Methods

### The following are methods for FilterValue . All are instance methods.


### Apex Reference Guide FormulaType Enum

IN THIS SECTION:

##### getLabel()

Returns the localized display name of the filter value. Possible values for this name are restricted based on the data type of the column
being filtered.

##### getName()

Returns the unique API name of the filter value. Possible values for this name are restricted based on the data type of the column
being filtered.

##### getLabel()

Returns the localized display name of the filter value. Possible values for this name are restricted based on the data type of the column
being filtered.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique API name of the filter value. Possible values for this name are restricted based on the data type of the column being
filtered.

Syntax

```
   public String getName()

```

Return Value

Type: String

### FormulaType Enum

The format of the numbers in a custom summary formula.

Enum Values

The following are the values of the `Reports.FormulaType` enum.

**Value** **Description**

`CHECKBOX` Formatted as a checkbox (true/false).

`CURRENCY` Formatted as currency. For example, $100.00.

`DATE` Formatted as a date. For example, 01/01/2025.


### Apex Reference Guide GroupingColumn Class

**Value** **Description**

`DATE_TIME` Formatted as a date and time. For example, 01/01/2025 12:00 PM.

`NUMBER` Formatted as numbers. For example, 100.

`PERCENT` Formatted as percentages. For example, 100%.

`TEXT` Formatted as text.

`TIME` Formatted as a time. For example, 12:00 PM.

### GroupingColumn Class

Contains methods for describing fields that are used for column grouping.

Namespace

Reports

### The GroupingColumn class provides basic information about column grouping fields. The GroupingInfo class includes

additional methods for describing and updating grouping fields.

#### GroupingColumn Methods

### The following are methods for GroupingColumn . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the field or bucket field that is used for column grouping.

getLabel()
Returns the localized display name of the field that is used for column grouping.

getDataType()
Returns the data type of the field that is used for column grouping.

getGroupingLevel()
Returns the level of grouping for the column.

##### getName()

Returns the unique API name of the field or bucket field that is used for column grouping.

Syntax

```
   public String getName()

```

Return Value

Type: String


### Apex Reference Guide GroupingInfo Class

##### getLabel()

Returns the localized display name of the field that is used for column grouping.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getDataType()

Returns the data type of the field that is used for column grouping.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

##### getGroupingLevel()

Returns the level of grouping for the column.

Syntax

```
   public Integer getGroupingLevel()

```

Return Value

Type: Integer

Usage

**•** In a summary report, 0, 1, or 2 indicates grouping at the first, second, or third row level.

**•** In a matrix report, 0 or 1 indicates grouping at the first or second row or column level.

### GroupingInfo Class

Contains methods for describing fields that are used for grouping.

Namespace

Reports


Apex Reference Guide GroupingInfo Class

#### GroupingInfo Methods The following are methods for GroupingInfo . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the field or bucket field that is used for row or column grouping.

##### getSortOrder()

Returns the order that is used to sort data in a row or column grouping ( `ASCENDING` or `DESCENDING` ).

##### getDateGranularity()

Returns the date interval that is used for row or column grouping.

getSortAggregate()
Returns the summary field that is used to sort data within a grouping in a summary report. The value is null when data within a
grouping is not sorted by a summary field.

##### getName()

Returns the unique API name of the field or bucket field that is used for row or column grouping.

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getSortOrder()

Returns the order that is used to sort data in a row or column grouping ( `ASCENDING` or `DESCENDING` ).

Syntax

```
   public Reports.ColumnSortOrder getSortOrder()

```

Return Value

Type: Reports.ColumnSortOrder

##### getDateGranularity()

Returns the date interval that is used for row or column grouping.

Syntax

```
   public Reports.DateGranularity getDateGranularity()

```


### Apex Reference Guide GroupingValue Class

Return Value

Type: Reports.DateGranularity

##### getSortAggregate()

Returns the summary field that is used to sort data within a grouping in a summary report. The value is null when data within a grouping
is not sorted by a summary field.

Syntax

```
   public String getSortAggregate()

```

Return Value

Type: String

### GroupingValue Class

Contains grouping values for a row or column, including the key, label, and value.

Namespace

Reports

#### GroupingValue Methods

### The following are methods for GroupingValue . All are instance methods.

IN THIS SECTION:

##### getGroupings()

Returns a list of second- or third-level row or column groupings. If there are none, the value is an empty array.

getKey()
Returns the unique identifier for a row or column grouping. The identifier is used by the fact map to specify data values within each
grouping.

getLabel()
Returns the localized display name of a row or column grouping. For date and time fields, the label is the localized date or time.

getValue()
Returns the value of the field that is used as a row or column grouping.

##### getGroupings()

Returns a list of second- or third-level row or column groupings. If there are none, the value is an empty array.

Syntax

```
   public LIST<Reports.GroupingValue> getGroupings()

```


Apex Reference Guide GroupingValue Class

Return Value

Type: List<Reports.GroupingValue>

##### getKey()

Returns the unique identifier for a row or column grouping. The identifier is used by the fact map to specify data values within each
grouping.

Syntax

```
   public String getKey()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name of a row or column grouping. For date and time fields, the label is the localized date or time.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the value of the field that is used as a row or column grouping.

Syntax

```
   public Object getValue()

```

Return Value

Type: Object

Usage

The value depends on the field’s data type.

**•** Currency fields:

**–** `amount` : Of type currency. A data cell’s value.

**–** `currency` : Of type picklist. The ISO 4217 currency code, if available; for example, USD for US dollars or CNY for Chinese yuan.
(If the grouping is on the converted currency, this value is the currency code for the report and not for the record.)

**•** Picklist fields: API name. For example, a custom picklist field— `Type of Business` with values 1, 2, and 3 for Consulting,
Services, and Add-On Business respectively—has `1`, `2`, or `3` as the grouping value.


### Apex Reference Guide NotificationAction Interface

**•** ID fields: API name.

**•** Record type fields: API name.

**•** Date and time fields: Date or time in ISO-8601 format.

**•** Lookup fields: Unique API name. For example, for the `Opportunity Owner` lookup field, the ID of each opportunity owner’s
Chatter profile page can be a grouping value.

### NotificationAction Interface

Implement this interface to trigger a custom Apex class when the conditions for a report notification are met.

Namespace

Reports

Usage

Report notifications for reports that users have subscribed to can trigger a custom Apex class, which must implement the
##### Reports.NotificationAction interface. The execute method in this interface receives a

`NotificationActionContext` object as a parameter, which contains information about the report instance and the conditions
that must be met for a notification to be triggered.

IN THIS SECTION:

#### NotificationAction Methods

NotificationAction Example Implementation

#### NotificationAction Methods

### The following are methods for NotificationAction .

IN THIS SECTION:

##### execute(context)

Executes the custom Apex action specified in the `context` parameter of the context object, `NotificationActionContext` .
The object contains information about the report instance and the conditions that must be met for a notification to be triggered.
The method executes whenever the specified conditions are met.

##### execute(context)

Executes the custom Apex action specified in the `context` parameter of the context object, `NotificationActionContext` .
The object contains information about the report instance and the conditions that must be met for a notification to be triggered. The
method executes whenever the specified conditions are met.

Signature

```
   public void execute(Reports.NotificationActionContext context)

```


### Apex Reference Guide NotificationActionContext Class

Parameters

```
   context
```

Type: Reports.NotificationActionContext

Return Value

Type: Void

#### NotificationAction Example Implementation

This is an example implementation of the `Reports.NotificationAction` interface.

```
   public class AlertOwners implements Reports.NotificationAction {

      public void execute(Reports.NotificationActionContext context) {

        Reports.ReportResults results = context.getReportInstance().getReportResults();

        for(Reports.GroupingValue g: results.getGroupingsDown().getGroupings()) {

           FeedItem t = new FeedItem();

           t.ParentId = (Id)g.getValue();

           t.Body = 'This record needs attention. Please view the report.';

           t.Title = 'Needs Attention: '+ results.getReportMetadata().getName();

           t.LinkUrl = '/' + results.getReportMetadata().getId();

           insert t;

        }

      }

   }

### NotificationActionContext Class

```

Contains information about the report instance and condition threshold for a report notification.

Namespace

Reports

IN THIS SECTION:

#### NotificationActionContext Constructors

NotificationActionContext Methods

#### NotificationActionContext Constructors

### The following are constructors for NotificationActionContext .

IN THIS SECTION:

NotificationActionContext(reportInstance, thresholdInformation)
Creates a new instance of the `Reports.NotificationActionContext` class using the specified parameters.


Apex Reference Guide NotificationActionContext Class

##### NotificationActionContext(reportInstance, thresholdInformation)

Creates a new instance of the `Reports.NotificationActionContext` class using the specified parameters.

Signature

```
   public NotificationActionContext(Reports.ReportInstance reportInstance,

   Reports.ThresholdInformation thresholdInformation)

```

Parameters

```
   reportInstance
```

Type: Reports.ReportInstance

An instance of a report.

```
   thresholdInformation
```

Type: Reports.ThresholdInformation

The evaluated conditions for the notification.

#### NotificationActionContext Methods

##### The following are methods for NotificationActionContext .

IN THIS SECTION:

##### getReportInstance()

Returns the report instance associated with the notification.

##### getThresholdInformation()

Returns the threshold information associated with the notification.

##### getReportInstance()

Returns the report instance associated with the notification.

Signature

```
   public Reports.ReportInstance getReportInstance()

```

Return Value

Type: Reports.ReportInstance

##### getThresholdInformation()

Returns the threshold information associated with the notification.

Signature

```
   public Reports.ThresholdInformation getThresholdInformation()

```


### Apex Reference Guide ReportCsf Class

Return Value

Type: Reports.ThresholdInformation

### ReportCsf Class

Contains methods and constructors for working with information about a custom summary formula (CSF).

Namespace

Reports

IN THIS SECTION:

#### ReportCsf Constructors

ReportCsf Methods

#### ReportCsf Constructors

### The following are constructors for ReportCsf .

IN THIS SECTION:

##### ReportCsf(label, description, formulaType, decimalPlaces, downGroup, downGroupType, acrossGroup, acrossGroupType, formula)

Creates an instance of the `Reports.ReportCsf` class using the specified parameters.

ReportCsf()
Creates an instance of the `Reports.ReportCsf` class. You can then set values by using the class’s `set` methods.

##### ReportCsf(label, description, formulaType, decimalPlaces, downGroup, downGroupType,

acrossGroup, acrossGroupType, formula)

Creates an instance of the `Reports.ReportCsf` class using the specified parameters.

Signature

```
   public ReportCsf(String label, String description, Reports.FormulaType formulaType,

   Integer decimalPlaces, String downGroup, Reports.CsfGroupType downGroupType, String

   acrossGroup, Reports.CsfGroupType acrossGroupType, String formula)

```

Parameters

```
   label
```

Type: String

The user-facing name of the custom summary formula.

```
   description
```

Type: String

The user-facing description of the custom summary formula.


Apex Reference Guide ReportCsf Class

```
   formulaType
```

Type: Reports.FormulaType

The format of the numbers in the custom summary formula.

```
   decimalPlaces
```

Type: Integer

The number of decimal places to include in numbers.

```
   downGroup
```

Type: String

The name of a row grouping when the `downGroupType` is `CUSTOM` ; `null` otherwise.

```
   downGroupType
```

Type: Reports.CsfGroupType

Where to display the aggregate of the custom summary formula.

```
   acrossGroup
```

Type: String

The name of a column grouping when the `accrossGroupType` is `CUSTOM` ; `null` otherwise.

```
   acrossGroupType
```

Type: Reports.CsfGroupType

Where to display the aggregate of the custom summary formula.

```
   formula
```

Type: String

The operations performed on values in the custom summary formula.

##### ReportCsf()

Creates an instance of the `Reports.ReportCsf` class. You can then set values by using the class’s `set` methods.

Signature

```
   public ReportCsf()

#### ReportCsf Methods

##### The following are methods for ReportCsf .

```

IN THIS SECTION:

getAcrossGroup()
Returns the name of a column grouping when the `acrossGroupType` is `CUSTOM` . Otherwise, returns `null` .

getAcrossGroupType()
Returns where to display the aggregate.

getDecimalPlaces()
Returns the number of decimal places that numbers in the custom summary formula have.


Apex Reference Guide ReportCsf Class

getDescription()
Returns the user-facing description of a custom summary formula.

getDownGroup()
Returns the name of a row grouping when the `downGroupType` is `CUSTOM` . Otherwise, returns `null` .

getDownGroupType()
Returns where to display the aggregate of the custom summary formula.

getFormula()
Returns the operations performed on values in the custom summary formula.

getFormulaType()
Returns the formula type.

getLabel()
Returns the user-facing name of the custom summary formula.

setAcrossGroup(acrossGroup)
Specifies the column for the across grouping.

setAcrossGroupType(value)
Sets where to display the aggregate.

setAcrossGroupType(acrossGroupType)
Sets where to display the aggregate.

setDecimalPlaces(decimalPlaces)
Sets the number of decimal places in numbers.

setDescription(description)
Sets the user-facing description of the custom summary formula.

setDownGroup(downGroup)
Sets the name of a row grouping when the `downGroupType` is `CUSTOM` .

setDownGroupType(value)
Sets where to display the aggregate.

setDownGroupType(downGroupType)
Sets where to display the aggregate.

setFormula(formula)
Sets the operations to perform on values in the custom summary formula.

setFormulaType(value)
Sets the format of the numbers in the custom summary formula.

setFormulaType(formulaType)
Sets the format of numbers used in the custom summary formula.

setLabel(label)
Sets the user-facing name of the custom summary formula.

toString()
Returns a string.


Apex Reference Guide ReportCsf Class

##### getAcrossGroup()

Returns the name of a column grouping when the `acrossGroupType` is `CUSTOM` . Otherwise, returns `null` .

Signature

```
   public String getAcrossGroup()

```

Return Value

Type: String

##### getAcrossGroupType()

Returns where to display the aggregate.

Signature

```
   public Reports.CsfGroupType getAcrossGroupType()

```

Return Value

Type: Reports.CsfGroupType

##### getDecimalPlaces()

Returns the number of decimal places that numbers in the custom summary formula have.

Signature

```
   public Integer getDecimalPlaces()

```

Return Value

Type: Integer

##### getDescription()

Returns the user-facing description of a custom summary formula.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getDownGroup()

Returns the name of a row grouping when the `downGroupType` is `CUSTOM` . Otherwise, returns `null` .


Apex Reference Guide ReportCsf Class

Signature

```
   public String getDownGroup()

```

Return Value

Type: String

##### getDownGroupType()

Returns where to display the aggregate of the custom summary formula.

Signature

```
   public Reports.CsfGroupType getDownGroupType()

```

Return Value

Type: Reports.CsfGroupType

##### getFormula()

Returns the operations performed on values in the custom summary formula.

Signature

```
   public String getFormula()

```

Return Value

Type: String

##### getFormulaType()

Returns the formula type.

Signature

```
   public Reports.FormulaType getFormulaType()

```

Return Value

Type: Reports.FormulaType

##### getLabel()

Returns the user-facing name of the custom summary formula.

Signature

```
   public String getLabel()

```


Apex Reference Guide ReportCsf Class

Return Value

Type: String

##### setAcrossGroup(acrossGroup)

Specifies the column for the across grouping.

Signature

```
   public void setAcrossGroup(String acrossGroup)

```

Parameters

```
   acrossGroup
```

Type: String

Return Value

Type: void

##### setAcrossGroupType(value)

Sets where to display the aggregate.

Signature

```
   public void setAcrossGroupType(String value)

```

Parameters

```
   value
```

Type: String

For possible values, see Reports.CsfGroupType.

Return Value

Type: void

##### setAcrossGroupType(acrossGroupType)

Sets where to display the aggregate.

Signature

```
   public void setAcrossGroupType(Reports.CsfGroupType acrossGroupType)

```

Parameters

```
   acrossGroupType
```

Type: Reports.CsfGroupType


Apex Reference Guide ReportCsf Class

Return Value

Type: void

##### setDecimalPlaces(decimalPlaces)

Sets the number of decimal places in numbers.

Signature

```
   public void setDecimalPlaces(Integer decimalPlaces)

```

Parameters

```
   decimalPlaces
```

Type: Integer

Return Value

Type: void

##### setDescription(description)

Sets the user-facing description of the custom summary formula.

Signature

```
   public void setDescription(String description)

```

Parameters

```
   description
```

Type: String

Return Value

Type: void

##### setDownGroup(downGroup)

Sets the name of a row grouping when the `downGroupType` is `CUSTOM` .

Signature

```
   public void setDownGroup(String downGroup)

```

Parameters

```
   downGroup
```

Type: String


Apex Reference Guide ReportCsf Class

Return Value

Type: void

##### setDownGroupType(value)

Sets where to display the aggregate.

Signature

```
   public void setDownGroupType(String value)

```

Parameters

```
   value
```

Type: String

For valid values, see Reports.CsfGroupType.

Return Value

Type: void

##### setDownGroupType(downGroupType)

Sets where to display the aggregate.

Signature

```
   public void setDownGroupType(Reports.CsfGroupType downGroupType)

```

Parameters

```
   downGroupType
```

Type: Reports.CsfGroupType

Return Value

Type: void

##### setFormula(formula)

Sets the operations to perform on values in the custom summary formula.

Signature

```
   public void setFormula(String formula)

```

Parameters

```
   formula
```

Type: String


Apex Reference Guide ReportCsf Class

Return Value

Type: void

##### setFormulaType(value)

Sets the format of the numbers in the custom summary formula.

Signature

```
   public void setFormulaType(String value)

```

Parameters

```
   value
```

Type: String

For valid values, see Reports.FormulaType.

Return Value

Type: void

##### setFormulaType(formulaType)

Sets the format of numbers used in the custom summary formula.

Signature

```
   public void setFormulaType(Reports.FormulaType formulaType)

```

Parameters

```
   formulaType
```

Type: Reports.FormulaType

Return Value

Type: void

##### setLabel(label)

Sets the user-facing name of the custom summary formula.

Signature

```
   public void setLabel(String label)

```

Parameters

```
   label
```

Type: String


### Apex Reference Guide ReportCurrency Class

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### ReportCurrency Class

Contains information about a currency value, including the amount and currency code.

Namespace

Reports

#### ReportCurrency Methods

### The following are methods for ReportCurrency . All are instance methods.

IN THIS SECTION:

##### getAmount()

Returns the amount of the currency value.

getCurrencyCode()
Returns the report currency code, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null`
if the organization does not have multicurrency enabled.

##### getAmount()

Returns the amount of the currency value.

Syntax

```
   public Decimal getAmount()

```

Return Value

Type: Decimal


### Apex Reference Guide ReportDataCell Class

##### getCurrencyCode()

Returns the report currency code, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null` if
the organization does not have multicurrency enabled.

Syntax

```
   public String getCurrencyCode()

```

Return Value

Type: String

### ReportDataCell Class

Contains the data for a cell in the report, including the display label and value.

Namespace

Reports

#### ReportDataCell Methods

### The following are methods for ReportDataCell . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the localized display name of the value of a specified cell in the report.

##### getValue()

Returns the value of a specified cell of a detail row of a report.

##### getLabel()

Returns the localized display name of the value of a specified cell in the report.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the value of a specified cell of a detail row of a report.


### Apex Reference Guide ReportDescribeResult Class

Syntax

```
   public Object getValue()

```

Return Value

Type: Object

### ReportDescribeResult Class

Contains report, report type, and extended metadata for a tabular, summary, or matrix report.

Namespace

Reports

#### ReportDescribeResult Methods

### The following are methods for ReportDescribeResult . All are instance methods.

IN THIS SECTION:

##### getReportExtendedMetadata()

Returns additional information about grouping and summaries.

##### getReportMetadata()

Returns unique identifiers for groupings and summaries.

getReportTypeMetadata()
Returns the fields in each section of a report type, plus filtering information for those fields.

##### getReportExtendedMetadata()

Returns additional information about grouping and summaries.

Syntax

```
   public Reports.ReportExtendedMetadata getReportExtendedMetadata()

```

Return Value

Type: Reports.ReportExtendedMetadata

##### getReportMetadata()

Returns unique identifiers for groupings and summaries.

Syntax

```
   public Reports.ReportMetadata getReportMetadata()

```


### Apex Reference Guide ReportDetailRow Class

Return Value

Type: Reports.ReportMetadata

##### getReportTypeMetadata()

Returns the fields in each section of a report type, plus filtering information for those fields.

Syntax

```
   public Reports.ReportTypeMetadata getReportTypeMetadata()

```

Return Value

Type: Reports.ReportTypeMetadata

### ReportDetailRow Class

Contains data cells for a detail row of a report.

Namespace

Reports

#### ReportDetailRow Methods

### The following are methods for ReportDetailRow . All are instance methods.

IN THIS SECTION:

##### getDataCells()

Returns a list of data cells for a detail row.

##### getDataCells()

Returns a list of data cells for a detail row.

Syntax

```
   public LIST<Reports.ReportDataCell> getDataCells()

```

Return Value

Type: List<Reports.ReportDataCell>

### ReportDivisionInfo Class

Contains information about the divisions that can be used to filter a report.


### Apex Reference Guide ReportExtendedMetadata Class

Available only if your organization uses divisions to segment data and you have the “Affected by Divisions” permission. If you do not
have the “Affected by Divisions” permission, your reports include records in all divisions.

Namespace

Reports

Usage

Use to filter records in the report based on a division, like West Coast and East Coast.

#### ReportDivisionInfo Methods The following are methods for ReportDivisionInfo .

##### getDefaultValue()

Returns the default division for the report.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getValues()

Returns a list of all possible divisions for the report.

Signature

```
   public List<Reports.FilterValue> getValues()

```

Return Value

Type: List<Reports.FilterValue>

### ReportExtendedMetadata Class

Contains report extended metadata for a tabular, summary, or matrix report.

Namespace

Reports

Report extended metadata provides additional, detailed metadata about summary and grouping fields, including data type and label
information.


Apex Reference Guide ReportExtendedMetadata Class

#### ReportExtendedMetadata Methods The following are methods for ReportExtendedMetadata . All are instance methods.

IN THIS SECTION:

##### getAggregateColumnInfo()

Returns all report summaries such as `Record Count`, `Sum`, `Average`, `Max`, `Min`, and custom summary formulas. Contains
values for each summary that is listed in the report metadata.

##### getDetailColumnInfo()

Returns a map of two properties for each field that has detailed data identified by its unique API name. The detailed data fields are
also listed in the report metadata.

##### getGroupingColumnInfo()

Returns a map of each row or column grouping to its metadata. Contains values for each grouping that is identified in the
groupingsDown and groupingsAcross lists.

##### getAggregateColumnInfo()

Returns all report summaries such as `Record Count`, `Sum`, `Average`, `Max`, `Min`, and custom summary formulas. Contains values
for each summary that is listed in the report metadata.

Syntax

```
   public MAP<String,Reports.AggregateColumn> getAggregateColumnInfo()

```

Return Value

Type: Map<String,Reports.AggregateColumn>

##### getDetailColumnInfo()

Returns a map of two properties for each field that has detailed data identified by its unique API name. The detailed data fields are also
listed in the report metadata.

Syntax

```
   public MAP<String,Reports.DetailColumn> getDetailColumnInfo()

```

Return Value

Type: Map<String,Reports.DetailColumn>

##### getGroupingColumnInfo()

Returns a map of each row or column grouping to its metadata. Contains values for each grouping that is identified in the groupingsDown
and groupingsAcross lists.

Syntax

```
   public MAP<String,Reports.GroupingColumn> getGroupingColumnInfo()

```


### Apex Reference Guide ReportFact Class

Return Value

Type: Map<String,Reports.GroupingColumn>

### ReportFact Class

Contains the fact map for the report, which represents the report’s data values.

Namespace

Reports

Usage

### ReportFact is the parent class of ReportFactWithDetails and ReportFactWithSummaries . If includeDetails

is `true` when the report is run, the fact map is a `ReportFactWithDetails` object. If `includeDetails` is `false` when
the report is run, the fact map is a `ReportFactWithSummaries` object.

#### ReportFact Methods

### The following are methods for ReportFact . All are instance methods.

IN THIS SECTION:

##### getAggregates()

Returns summary-level data for a report, including the record count.

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each
grouping.

##### getAggregates()

Returns summary-level data for a report, including the record count.

Syntax

```
   public LIST<Reports.SummaryValue> getAggregates()

```

Return Value

Type: List<Reports.SummaryValue>

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each grouping.

Syntax

```
   public String getKey()

```


### Apex Reference Guide ReportFactWithDetails Class

Return Value

Type: String

### ReportFactWithDetails Class

Contains the detailed fact map for the report, which represents the report’s data values.

Namespace

Reports

Usage

### The ReportFactWithDetails class extends the ReportFact class. A ReportFactWithDetails object is returned if

`includeDetails` is set to `true` when the report is run. To access the detail values, you’ll need to cast the return value of the
### ReportResults.getFactMap method to a ReportFactWithDetails object.

#### ReportFactWithDetails Methods

### The following are methods for ReportFactWithDetails . All are instance methods.

IN THIS SECTION:

##### getAggregates()

Returns summary-level data for a report, including the record count.

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each
grouping.

getRows()
Returns a list of detailed report data in the order of the detail columns that are provided by the report metadata.

##### getAggregates()

Returns summary-level data for a report, including the record count.

Syntax

```
   public LIST<Reports.SummaryValue> getAggregates()

```

Return Value

Type: List<Reports.SummaryValue>

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each grouping.


### Apex Reference Guide ReportFactWithSummaries Class

Syntax

```
   public String getKey()

```

Return Value

Type: String

##### getRows()

Returns a list of detailed report data in the order of the detail columns that are provided by the report metadata.

Syntax

```
   public LIST<Reports.ReportDetailRow> getRows()

```

Return Value

Type: List<Reports.ReportDetailRow>

### ReportFactWithSummaries Class

Contains the fact map for the report, which represents the report’s data values, and includes summarized fields.

Namespace

Reports

Usage

### The ReportFactWithSummaries class extends the ReportFact class. A ReportFactWithSummaries object is

returned if `includeDetails` is set to `false` when the report is run.

#### ReportFactWithSummaries Methods

### The following are methods for ReportFactWithSummaries . All are instance methods.

IN THIS SECTION:

getAggregates()
Returns summary-level data for a report, including the record count.

getKey()
Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each
grouping.

toString()
Returns a string.


### Apex Reference Guide ReportFilter Class

##### getAggregates()

Returns summary-level data for a report, including the record count.

Syntax

```
   public LIST<Reports.SummaryValue> getAggregates()

```

Return Value

Type: List<Reports.SummaryValue>

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each grouping.

Syntax

```
   public String getKey()

```

Return Value

Type: String

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### ReportFilter Class

Contains information about a report filter, including column, operator, and value.

Namespace

Reports

IN THIS SECTION:

ReportFilter Constructors

ReportFilter Methods


Apex Reference Guide ReportFilter Class

#### ReportFilter Constructors The following are constructors for ReportFilter .

IN THIS SECTION:

##### ReportFilter()

Creates a new instance of the `Reports.ReportFilter` class. You can then set values by using the “set” methods.

##### ReportFilter(column, operator, value)

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

##### ReportFilter(column, operator, value, filterType)

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

ReportFilter(column, operator, value, filterType, entityName)
Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

##### ReportFilter()

Creates a new instance of the `Reports.ReportFilter` class. You can then set values by using the “set” methods.

Signature

```
   public ReportFilter()

##### ReportFilter(column, operator, value)

```

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

Signature

```
   public ReportFilter(String column, String operator, String value)

```

Parameters

```
   column
```

Type: String

```
   operator
```

Type: String

```
   value
```

Type: String

##### ReportFilter(column, operator, value, filterType)

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

Syntax

```
   public ReportFilterType(String column, String operator, String value,

   Reports.ReportFilterType filterType)

```


Apex Reference Guide ReportFilter Class

Parameters

```
   column
```

Type: String

```
   operator
```

Type: String

```
   value
```

Type: String

```
   filterType
```

Type: ReportFilterType Enum on page 3352

##### **`ReportFilter(column, operator, value, filterType, entityName)`**

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

Syntax

```
   public ReportFilterType(String column, String operator, String value,

   Reports.ReportFilterType filterType, String entityName)

```

Parameters

```
   column
```

Type: String

```
   operator
```

Type: String

```
   value
```

Type: String

```
   filterType
```

Type: ReportFilterType Enum on page 3352

```
   entityName
```

Type: String

#### ReportFilter Methods

##### The following are methods for ReportFilter . All are instance methods.

IN THIS SECTION:

getColumn()
Returns the unique API name for the field that’s being filtered.

getEntityName()
Returns the entity name used in the report filter. Use the entity name to handle ambiguous field names across entities, specifically
when using cross filters.

getFilterType()
Returns the type of report filter.


Apex Reference Guide ReportFilter Class

getOperator()
Returns the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions
depend on the data type of the field.

getValue()
Returns the value that the field is being filtered by. For example, the field `Age` can be filtered by a numeric value.

setColumn(column)
Sets the unique API name for the field that’s being filtered.

setEntityName(entityName)
Sets the entity name to use in the report filter. Use the entity name to handle ambiguous field names across entities, specifically
when using cross filters.

setFilterType()
Sets the type of report filter.

setOperator(operator)
Sets the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions
depend on the data type of the field.

setValue(value)
Sets the value by which a field can be filtered. For example, the field `Age` can be filtered by a numeric value.

toString(column)
Returns a string representation of the filter.

##### getColumn()

Returns the unique API name for the field that’s being filtered.

Syntax

```
   public String getColumn()

```

Return Value

Type: String

##### **`getEntityName()`**

Returns the entity name used in the report filter. Use the entity name to handle ambiguous field names across entities, specifically when
using cross filters.

Syntax

```
   public String getEntityName()

```

Return Value

Type: String


Apex Reference Guide ReportFilter Class

##### getFilterType()

Returns the type of report filter.

Syntax

```
   public String getFilterType()

```

Return Value

Type: ReportFilterType Enum on page 3352

##### getOperator()

Returns the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions
depend on the data type of the field.

Syntax

```
   public String getOperator()

```

Return Value

Type: String

##### getValue()

Returns the value that the field is being filtered by. For example, the field `Age` can be filtered by a numeric value.

Syntax

```
   public String getValue()

```

Return Value

Type: String

##### setColumn(column)

Sets the unique API name for the field that’s being filtered.

Syntax

```
   public Void setColumn(String column)

```

Parameters

```
   column
```

Type: String


Apex Reference Guide ReportFilter Class

Return Value

Type: Void

##### **`setEntityName(entityName)`**

Sets the entity name to use in the report filter. Use the entity name to handle ambiguous field names across entities, specifically when
using cross filters.

Syntax

```
   public Void setEntityName(String entityName)

```

Parameters

```
   operator
```

Type: String

Return Value

Type: Void

##### setFilterType()

Sets the type of report filter.

Syntax

```
   public Void setFilterType(String column)

```

Parameters

```
   column
```

Type: String

Return Value

Type: Void

##### setOperator(operator)

Sets the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions depend
on the data type of the field.

Syntax

```
   public Void setOperator(String operator)

```


### Apex Reference Guide ReportFormat Enum

Parameters

```
   operator
```

Type: String

Return Value

Type: Void

##### setValue(value)

Sets the value by which a field can be filtered. For example, the field `Age` can be filtered by a numeric value.

Syntax

```
   public Void setValue(String value)

```

Parameters

```
   value
```

Type: String

Return Value

Type: Void

##### toString(column)

Returns a string representation of the filter.

Signature

```
   public String toString()

```

Return Value

Type: String

### ReportFormat Enum

Contains the possible report format types.

Namespace

Reports

Enum Values

The following are the values of the `Reports.ReportFormat` enum.


### Apex Reference Guide ReportFilterType Enum

**Value** **Description**

`MATRIX` Matrix report format

`SUMMARY` Summary report format

`TABULAR` Tabular report format

### ReportFilterType Enum

The types of values included in a report filter type.

Enum Values

The following are the values of the `Reports.ReportFilterType` enum.

**Value** **Description**

`fieldToField` Field-to-field filter

`fieldValue` Field-to-value filter

### ReportInstance Class

Returns an instance of a report that was run asynchronously. Retrieves the results for that instance.

Namespace

Reports

#### ReportInstance Methods

### The following are methods for ReportInstance . All are instance methods.

IN THIS SECTION:

getCompletionDate()
Returns the date and time when the instance of the report finished running. The completion date is available only if the report
instance ran successfully or couldn’t be run because of an error. Date and time information is in ISO-8601 format.

getId()
Returns the unique ID for an instance of a report that was run asynchronously.

getOwnerId()
Returns the ID of the user who created the report instance.

getReportId()
Returns the unique ID of the report this instance is based on.


Apex Reference Guide ReportInstance Class

getReportResults()
Retrieves results for an instance of an asynchronous report. When you request your report, you can specify whether to summarize
data or include details.

getRequestDate()
Returns the date and time when an instance of the report was run. Date and time information is in ISO-8601 format.

getStatus()
Returns the status of a report.

##### getCompletionDate()

Returns the date and time when the instance of the report finished running. The completion date is available only if the report instance
ran successfully or couldn’t be run because of an error. Date and time information is in ISO-8601 format.

Syntax

```
   public Datetime getCompletionDate()

```

Return Value

Type: Datetime

##### getId()

Returns the unique ID for an instance of a report that was run asynchronously.

Syntax

```
   public Id getId()

```

Return Value

Type: Id

##### getOwnerId()

Returns the ID of the user who created the report instance.

Syntax

```
   public Id getOwnerId()

```

Return Value

Type: Id

##### getReportId()

Returns the unique ID of the report this instance is based on.


Apex Reference Guide ReportInstance Class

Syntax

```
   public Id getReportId()

```

Return Value

Type: Id

##### getReportResults()

Retrieves results for an instance of an asynchronous report. When you request your report, you can specify whether to summarize data
or include details.

Syntax

```
   public Reports.ReportResults getReportResults()

```

Return Value

Type: Reports.ReportResults

##### getRequestDate()

Returns the date and time when an instance of the report was run. Date and time information is in ISO-8601 format.

Syntax

```
   public Datetime getRequestDate()

```

Return Value

Type: Datetime

##### getStatus()

Returns the status of a report.

Syntax

```
   public String getStatus()

```

Return Value

Type: String

Usage

**•** `New` if the report run was recently triggered through a request.

**•** `Success` if the report ran.

**•** `Running` if the report is being run.


### Apex Reference Guide ReportManager Class

**•** `Error` if the report run failed. The instance of a report run can return an error if, for example, your permission to access the report
was removed after you requested the run.

### ReportManager Class

Runs a report synchronously or asynchronously and with or without details.

Namespace

Reports

Usage

Gets instances of reports and describes the metadata of Reports.

#### ReportManager Methods

### The following are methods for ReportManager . All methods are static.

IN THIS SECTION:

describeReport(reportId)
Retrieves report, report type, and extended metadata for a tabular, summary, or matrix report.

getDatatypeFilterOperatorMap()
Lists the field data types that you can use to filter the report.

getReportInstance(instanceId)
Retrieves results for an instance of a report that has been run asynchronously. The settings you use when you run your asynchronous
report determine whether you can retrieve summary data or detailed data.

getReportInstances(reportId)
Returns a list of instances for a report that was run asynchronously. Each item in the list represents a separate instance of the report,
with metadata for the time at which the report was run.

runAsyncReport(reportId, reportMetadata, includeDetails)
Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the report based
on the report metadata in _`reportMetadata`_ .

runAsyncReport(reportId, includeDetails)
Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` .

runAsyncReport(reportId, reportMetadata)
Runs a report asynchronously with the report ID. Filters the results based on the report metadata in _`reportMetadata`_ .

runAsyncReport(reportId)
Runs a report asynchronously with the report ID.

runReport(reportId, reportMetadata, includeDetails)
Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the results based on
the report metadata in _`reportMetadata`_ .

runReport(reportId, includeDetails)
Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` .


Apex Reference Guide ReportManager Class

runReport(reportId, reportMetadata)
Runs a report immediately with the report ID. Filters the results based on the report metadata in _`rmData`_ .

runReport(reportId)
Runs a report immediately with the report ID.

##### describeReport(reportId)

Retrieves report, report type, and extended metadata for a tabular, summary, or matrix report.

Syntax

```
   public static Reports.ReportDescribeResult describeReport(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: Reports.ReportDescribeResult

##### getDatatypeFilterOperatorMap()

Lists the field data types that you can use to filter the report.

Syntax

```
   public static MAP<String,LIST<Reports.FilterOperator>> getDatatypeFilterOperatorMap()

```

Return Value

Type: Map<String, List<Reports.FilterOperator>>

##### getReportInstance(instanceId)

Retrieves results for an instance of a report that has been run asynchronously. The settings you use when you run your asynchronous
report determine whether you can retrieve summary data or detailed data.

Syntax

```
   public static Reports.ReportInstance getReportInstance(Id instanceId)

```

Parameters

```
   instanceId
```

Type: Id


Apex Reference Guide ReportManager Class

Return Value

Type: Reports.ReportInstance

##### getReportInstances(reportId)

Returns a list of instances for a report that was run asynchronously. Each item in the list represents a separate instance of the report, with
metadata for the time at which the report was run.

Syntax

```
   public static LIST<Reports.ReportInstance> getReportInstances(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: List<Reports.ReportInstance>

##### runAsyncReport(reportId, reportMetadata, includeDetails)

Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the report based on
the report metadata in _`reportMetadata`_ .

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId, Reports.ReportMetadata

   reportMetadata, Boolean includeDetails)

```

Parameters

```
   reportId
```

Type: Id

```
   reportMetadata
```

Type: Reports.ReportMetadata

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportInstance

##### runAsyncReport(reportId, includeDetails)

Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` .


Apex Reference Guide ReportManager Class

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId, Boolean includeDetails)

```

Parameters

```
   reportId
```

Type: Id

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportInstance

##### runAsyncReport(reportId, reportMetadata)

Runs a report asynchronously with the report ID. Filters the results based on the report metadata in _`reportMetadata`_ .

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId, Reports.ReportMetadata

   reportMetadata)

```

Parameters

```
   reportId
```

Type: Id

```
   reportMetadata
```

Type: Reports.ReportMetadata

Return Value

Type: Reports.ReportInstance

##### runAsyncReport(reportId)

Runs a report asynchronously with the report ID.

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: Reports.ReportInstance


Apex Reference Guide ReportManager Class

##### runReport(reportId, reportMetadata, includeDetails)

Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the results based on the
report metadata in _`reportMetadata`_ .

Syntax

```
   public static Reports.ReportResults runReport(Id reportId, Reports.ReportMetadata

   reportMetadata, Boolean includeDetails)

```

Parameters

```
   reportId
```

Type: Id

```
   reportMetadata
```

Type: Reports.ReportMetadata

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportResults

##### runReport(reportId, includeDetails)

Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` .

Syntax

```
   public static Reports.ReportResults runReport(Id reportId, Boolean includeDetails)

```

Parameters

```
   reportId
```

Type: Id

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportResults

##### runReport(reportId, reportMetadata)

Runs a report immediately with the report ID. Filters the results based on the report metadata in _`rmData`_ .

Syntax

```
   public static Reports.ReportResults runReport(Id reportId, Reports.ReportMetadata

   reportMetadata)

```


### Apex Reference Guide ReportMetadata Class

Parameters

```
   reportId
```

Type: Id

```
   reportMetadata
```

Type: Reports.ReportMetadata Reports.ReportMetadata

Return Value

Type: Reports.ReportResults

##### runReport(reportId)

Runs a report immediately with the report ID.

Syntax

```
   public static Reports.ReportResults runReport(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: Reports.ReportResults

### ReportMetadata Class

Contains report metadata for a tabular, summary, or matrix report.

Namespace

Reports

Usage

Report metadata gives information about the report as a whole, such as the report type, format, summary fields, row or column groupings,
### and filters that are saved to the report. You can use the ReportMetadata class to retrieve report metadata and to set metadata

that can be used to filter a report.

#### ReportMetadata Methods

### The following are methods for ReportMetadata . All are instance methods.

IN THIS SECTION:

getAggregates()
Returns unique identifiers for summary or custom summary formula fields in the report.


Apex Reference Guide ReportMetadata Class

getBuckets()
Returns a list of bucket fields in the report.

getCrossFilters()
Returns information about cross filters applied to a report.

getCurrencyCode()
Returns report currency, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null` if the
organization does not have multicurrency enabled.

getCustomSummaryFormula()
Returns information about custom summary formulas in a report.

getDescription()
Returns the description of the report.

getDetailColumns()
Returns unique API names (column names) for the fields that contain detailed data. For example, the method might return the
following values: “OPPORTUNITY_NAME, TYPE, LEAD_SOURCE, AMOUNT.”

getDeveloperName()
Returns the report API name. For example, the method might return the following value: “Closed_Sales_This_Quarter.”

getDivision()
Returns the division specified in the report.

getGroupingsAcross()
Returns column groupings in a report.

getGroupingsDown()
Returns row groupings for a report.

getHasDetailRows()
Indicates whether the report has detail rows.

getHasRecordCount()
Indicates whether the report shows the total number of records.

getHistoricalSnapshotDates()
Returns a list of historical snapshot dates.

getId()
Returns the unique report ID.

getName()
Returns the report name.

getReportBooleanFilter()
Returns logic to parse custom field filters. The value is `null` when filter logic is not specified.

getReportFilters()
Returns a list of each custom filter in the report along with the field name, filter operator, and filter value.

getReportFormat()
Returns the format of the report.

getReportType()
Returns the unique API name and display name for the report type.


Apex Reference Guide ReportMetadata Class

getScope()
Returns the API name for the scope defined for the report. Scope values depend on the report type.

getShowGrandTotal()
Indicates whether the report shows the grand total.

getShowSubtotals()
Indicates whether the report shows subtotals, such as column or row totals.

getSortBy()
Returns the list of columns on which the report is sorted. Currently, you can sort on only one column.

getStandardDateFilter()
Returns information about the standard date filter for the report, such as the start date, end date, date range, and date field API
name.

getStandardFilters()
Returns a list of standard filters for the report.

getTopRows()
Returns information about a row limit filter, including the number of rows returned and the sort order.

setAggregates(aggregates)
Sets unique identifiers for standard or custom summary formula fields in the report.

setBuckets(buckets)
Creates bucket fields in a report.

setCrossFilters(crossFilters)
Applies cross filters to a report.

setCurrencyCode(currencyCode)
Sets the currency, such as USD, EUR, or GBP, for report summary fields in an organization that has multicurrency enabled.

setCustomSummaryFormula(customSummaryFormula)
Adds a custom summary formula to a report.

setDescription(description)
Sets the description of the report.

setDetailColumns(detailColumns)
Sets the unique API names for the fields that contain detailed data—for example, `OPPORTUNITY_NAME`, `TYPE`, `LEAD_SOURCE`,
or `AMOUNT` .

setDeveloperName(developerName)
Sets the report API name—for example, `Closed_Sales_This_Quarter` .

setDivision(division)
Sets the division of the report.

setGroupingsAcross(groupingInfo)
Sets column groupings in a report.

setGroupingsDown(groupingInfo)
Sets row groupings for a report.

setHasDetailRows(hasDetailRows)
Specifies whether the report has detail rows.


Apex Reference Guide ReportMetadata Class

setHasRecordCount(hasRecordCount)
Specifies whether the report is configured to show the total number of records.

setHistoricalSnapshotDates(historicalSnapshot)
Sets a list of historical snapshot dates.

setId(id)
Sets the unique report ID.

setName(name)
Sets the report name.

setReportBooleanFilter(reportBooleanFilter)
Sets logic to parse custom field filters.

setReportFilters(reportFilters)
Sets a list of each custom filter in the report along with the field name, filter operator, and filter value.

setReportFormat(format)
Sets the format of the report.

setReportType(reportType)
Sets the unique API name and display name for the report type.

setScope(scopeName)
Sets the API name for the scope defined for the report. Scope values depend on the report type.

setShowGrandTotal(showGrandTotal)
Specifies whether the report shows the grand total.

setShowSubtotals(showSubtotals)
Specifies whether the report shows subtotals, such as column or row totals.

setSortBy(column)
Sets the list of columns on which the report is sorted. Currently, you can only sort on one column.

setStandardDateFilter(dateFilter)
Sets the standard date filter—which includes the start date, end date, date range, and date field API name—for the report.

setStandardFilters(filters)
Sets one or more standard filters on the report.

setTopRows(topRows)
Applies a row limit filter to a report.

##### getAggregates()

Returns unique identifiers for summary or custom summary formula fields in the report.

Syntax

```
   public LIST<String> getAggregates()

```

Return Value

Type: List<String>


Apex Reference Guide ReportMetadata Class

Usage

For example:

**•** `a!Amount` represents the average for the `Amount` column.

**•** `s!Amount` represents the sum of the `Amount` column.

**•** `m!Amount` represents the minimum value of the `Amount` column.

**•** `x!Amount` represents the maximum value of the `Amount` column.

**•** `s!` _`<customfieldID>`_ represents the sum of a custom field column. For custom fields and custom report types, the identifier
is a combination of the summary type and the field ID.

##### getBuckets()

Returns a list of bucket fields in the report.

Signature

```
   public List<Reports.BucketField> getBuckets()

```

Return Value

Type: List<Reports.BucketField>

##### getCrossFilters()

Returns information about cross filters applied to a report.

Signature

```
   public Reports.CrossFilter getCrossFilters()

```

Return Value

Type: List<Reports.CrossFilter>

##### getCurrencyCode()

Returns report currency, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null` if the
organization does not have multicurrency enabled.

Syntax

```
   public String getCurrencyCode()

```

Return Value

Type: String

##### getCustomSummaryFormula()

Returns information about custom summary formulas in a report.


Apex Reference Guide ReportMetadata Class

Signature

```
   public Map<String,Reports.ReportCsf> getCustomSummaryFormula()

```

Return Value

Type: Map<String,Reports.ReportCsf>

##### getDescription()

Returns the description of the report.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getDetailColumns()

Returns unique API names (column names) for the fields that contain detailed data. For example, the method might return the following
values: “OPPORTUNITY_NAME, TYPE, LEAD_SOURCE, AMOUNT.”

Syntax

```
   public LIST<String> getDetailColumns()

```

Return Value

Type: List<String>

##### getDeveloperName()

Returns the report API name. For example, the method might return the following value: “Closed_Sales_This_Quarter.”

Syntax

```
   public String getDeveloperName()

```

Return Value

Type: String

##### getDivision()

Returns the division specified in the report.

Note: Reports that use standard filters (such as My Cases or My Team’s Accounts) show records in all divisions. These reports can’t
be further limited to a specific division.


Apex Reference Guide ReportMetadata Class

Signature

```
   public String getDivision()

```

Return Value

Type: String

##### getGroupingsAcross()

Returns column groupings in a report.

Syntax

```
   public LIST<Reports.GroupingInfo> getGroupingsAcross()

```

Return Value

Type: List<Reports.GroupingInfo>

Usage

The identifier is:

**•** An empty array for reports in summary format, because summary reports don't include column groupings

**•** `BucketField_(` _**`ID`**_ `)` for bucket fields

**•** The ID of a custom field when the custom field is used for a column grouping

##### getGroupingsDown()

Returns row groupings for a report.

Syntax

```
   public LIST<Reports.GroupingInfo> getGroupingsDown()

```

Return Value

Type: List<Reports.GroupingInfo>

Usage

The identifier is:

**•** `BucketField_(` _**`ID`**_ `)` for bucket fields

**•** The ID of a custom field when the custom field is used for grouping

##### getHasDetailRows()

Indicates whether the report has detail rows.


Apex Reference Guide ReportMetadata Class

Signature

```
   public Boolean getHasDetailRows()

```

Return Value

Type: Boolean

##### getHasRecordCount()

Indicates whether the report shows the total number of records.

Signature

```
   public Boolean getHasRecordCount()

```

Return Value

Type: Boolean

##### getHistoricalSnapshotDates()

Returns a list of historical snapshot dates.

Syntax

```
   public LIST<String> getHistoricalSnapshotDates()

```

Return Value

Type: List<String>

##### getId()

Returns the unique report ID.

Syntax

```
   public Id getId()

```

Return Value

Type: Id

##### getName()

Returns the report name.

Syntax

```
   public String getName()

```


Apex Reference Guide ReportMetadata Class

Return Value

Type: String

##### getReportBooleanFilter()

Returns logic to parse custom field filters. The value is `null` when filter logic is not specified.

Syntax

```
   public String getReportBooleanFilter()

```

Return Value

Type: String

##### getReportFilters()

Returns a list of each custom filter in the report along with the field name, filter operator, and filter value.

Syntax

```
   public LIST<Reports.ReportFilter> getReportFilters()

```

Return Value

Type: List<Reports.ReportFilter>

##### getReportFormat()

Returns the format of the report.

Syntax

```
   public Reports.ReportFormat getReportFormat()

```

Return Value

Type: Reports.ReportFormat

Usage

This value can be:

**•** `TABULAR`

**•** `SUMMARY`

**•** `MATRIX`

##### getReportType()

Returns the unique API name and display name for the report type.


Apex Reference Guide ReportMetadata Class

Syntax

```
   public Reports.ReportType getReportType()

```

Return Value

Type: Reports.ReportType

##### getScope()

Returns the API name for the scope defined for the report. Scope values depend on the report type.

Signature

```
   public String getScope()

```

Return Value

Type: String

##### getShowGrandTotal()

Indicates whether the report shows the grand total.

Signature

```
   public Boolean getShowGrandTotal()

```

Return Value

Type: Boolean

##### getShowSubtotals()

Indicates whether the report shows subtotals, such as column or row totals.

Signature

```
   public Boolean getShowSubtotals()

```

Return Value

Type: Boolean

##### getSortBy()

Returns the list of columns on which the report is sorted. Currently, you can sort on only one column.

Signature

```
   public List<Reports.SortColumn> getSortBy()

```


Apex Reference Guide ReportMetadata Class

Return Value

Type: List<Reports.SortColumn>

##### getStandardDateFilter()

Returns information about the standard date filter for the report, such as the start date, end date, date range, and date field API name.

Signature

```
   public Reports.StandardDateFilter getStandardDateFilter()

```

Return Value

Type: Reports.StandardDateFilter

##### getStandardFilters()

Returns a list of standard filters for the report.

Signature

```
   public List<Reports.StandardFilter> getStandardFilters()

```

Return Value

Type: List<Reports.StandardFilter>

##### getTopRows()

Returns information about a row limit filter, including the number of rows returned and the sort order.

Signature

```
   public Reports.TopRows getTopRows()

```

Return Value

Type: Reports.TopRows

##### setAggregates(aggregates)

Sets unique identifiers for standard or custom summary formula fields in the report.

Signature

```
   public void setAggregates(List<String> aggregates)

```


Apex Reference Guide ReportMetadata Class

Parameters

```
   aggregates
```

Type: List<String>

Return Value

Type: void

##### setBuckets(buckets)

Creates bucket fields in a report.

Signature

```
   public void setBuckets(List<Reports.BucketField> buckets)

```

Parameters

```
   buckets
```

Type: List<Reports.BucketField>

Return Value

Type: void

##### setCrossFilters(crossFilters)

Applies cross filters to a report.

Signature

```
   public void setCrossFilters(List<Reports.CrossFilter> crossFilters)

```

Parameters

```
   crossFilter
```

Type: List<Reports.CrossFilter>

Return Value

Type: void

##### setCurrencyCode(currencyCode)

Sets the currency, such as USD, EUR, or GBP, for report summary fields in an organization that has multicurrency enabled.

Signature

```
   public void setCurrencyCode(String currencyCode)

```


Apex Reference Guide ReportMetadata Class

Parameters

```
   currencyCode
```

Type: String

Return Value

Type: void

##### setCustomSummaryFormula(customSummaryFormula)

Adds a custom summary formula to a report.

Signature

```
   public void setCustomSummaryFormula(MAP<String,Reports.ReportCsf> customSummaryFormula)

```

Parameters

```
   customSummaryFormula
```

Type: Map<String, Reports.ReportCsf>

Return Value

Type: void

##### setDescription(description)

Sets the description of the report.

Signature

```
   public void setDescription(String description)

```

Parameters

```
   description
```

Type: String

Return Value

Type: void

##### setDetailColumns(detailColumns)

Sets the unique API names for the fields that contain detailed data—for example, `OPPORTUNITY_NAME`, `TYPE`, `LEAD_SOURCE`,
or `AMOUNT` .

Signature

```
   public void setDetailColumns(List<String> detailColumns)

```


Apex Reference Guide ReportMetadata Class

Parameters

```
   detailColumns
```

Type: List<String>

Return Value

Type: void

##### setDeveloperName(developerName)

Sets the report API name—for example, `Closed_Sales_This_Quarter` .

Signature

```
   public void setDeveloperName(String developerName)

```

Parameters

```
   developerName
```

Type: String

Return Value

Type: void

##### setDivision(division)

Sets the division of the report.

Note: Reports that use standard filters (such as My Cases or My Team’s Accounts) show records in all divisions. These reports can’t
be further limited to a specific division.

Signature

```
   public void setDivision(String division)

```

Parameters

```
   division
```

Type: String

Return Value

Type: void

##### setGroupingsAcross(groupingInfo)

Sets column groupings in a report.


Apex Reference Guide ReportMetadata Class

Signature

```
   public void setGroupingsAcross(List<Reports.GroupingInfo> groupingInfo)

```

Parameters

```
   groupingInfo
```

Type: List<Reports.GroupingInfo>

Return Value

Type: void

##### setGroupingsDown(groupingInfo)

Sets row groupings for a report.

Signature

```
   public void setGroupingsDown(List<Reports.GroupingInfo> groupingInfo)

```

Parameters

```
   groupingInfo
```

Type: List<Reports.GroupingInfo>

Return Value

Type: void

##### setHasDetailRows(hasDetailRows)

Specifies whether the report has detail rows.

Signature

```
   public void setHasDetailRows(Boolean hasDetailRows)

```

Parameters

```
   hasDetailRows
```

Type: Boolean

Return Value

Type: void

##### setHasRecordCount(hasRecordCount)

Specifies whether the report is configured to show the total number of records.


Apex Reference Guide ReportMetadata Class

Signature

```
   public void setHasRecordCount(Boolean hasRecordCount)

```

Parameters

```
   hasRecordCount
```

Type: Boolean

Return Value

Type: void

##### setHistoricalSnapshotDates(historicalSnapshot)

Sets a list of historical snapshot dates.

Syntax

```
   public Void setHistoricalSnapshotDates(LIST<String> historicalSnapshot)

```

Parameters

```
   historicalSnapshot
```

Type: List<String>

Return Value

Type: Void

##### setId(id)

Sets the unique report ID.

Signature

```
   public void setId(Id id)

```

Parameters

```
   id
```

Type: Id

Return Value

Type: void

##### setName(name)

Sets the report name.


Apex Reference Guide ReportMetadata Class

Signature

```
   public void setName(String name)

```

Parameters

```
   name
```

Type: String

Return Value

Type: void

##### setReportBooleanFilter(reportBooleanFilter)

Sets logic to parse custom field filters.

Syntax

```
   public Void setReportBooleanFilter(String reportBooleanFilter)

```

Parameters

```
   reportBooleanFilter
```

Type: String

Return Value

Type: Void

##### setReportFilters(reportFilters)

Sets a list of each custom filter in the report along with the field name, filter operator, and filter value.

Syntax

```
   public Void setReportFilters(LIST<Reports.ReportFilter> reportFilters)

```

Parameters

```
   reportFilters
```

Type: List<Reports.ReportFilter>

Return Value

Type: Void

##### setReportFormat(format)

Sets the format of the report.


Apex Reference Guide ReportMetadata Class

Signature

```
   public void setReportFormat(Reports.ReportFormat format)

```

Parameters

```
   format
```

Type: Reports.ReportFormat

Return Value

Type: void

##### setReportType(reportType)

Sets the unique API name and display name for the report type.

Signature

```
   public void setReportType(Reports.ReportType reportType)

```

Parameters

```
   reportType
```

Type: Reports.ReportType

Return Value

Type: void

##### setScope(scopeName)

Sets the API name for the scope defined for the report. Scope values depend on the report type.

Signature

```
   public void setScope(String scopeName)

```

Parameters

```
   scopeName
```

Type: String

Return Value

Type: void

##### setShowGrandTotal(showGrandTotal)

Specifies whether the report shows the grand total.


Apex Reference Guide ReportMetadata Class

Signature

```
   public void setShowGrandTotal(Boolean showGrandTotal)

```

Parameters

```
   showGrandTotal
```

Type: Boolean

Return Value

Type: void

##### setShowSubtotals(showSubtotals)

Specifies whether the report shows subtotals, such as column or row totals.

Signature

```
   public void setShowSubtotals(Boolean showSubtotals)

```

Parameters

```
   showSubtotals
```

Type: Boolean

Return Value

Type: void

##### setSortBy(column)

Sets the list of columns on which the report is sorted. Currently, you can only sort on one column.

Signature

```
   public void setSortBy(List<Reports.SortColumn> column)

```

Parameters

```
   column
```

Type: List<Reports.SortColumn>

Return Value

Type: void

##### setStandardDateFilter(dateFilter)

Sets the standard date filter—which includes the start date, end date, date range, and date field API name—for the report.


### Apex Reference Guide ReportResults Class

Signature

```
   public void setStandardDateFilter(Reports.StandardDateFilter dateFilter)

```

Parameters

```
   dateFilter
```

Type: Reports.StandardDateFilter

Return Value

Type: void

##### setStandardFilters(filters)

Sets one or more standard filters on the report.

Signature

```
   public void setStandardFilters(List<Reports.StandardFilter> filters)

```

Parameters

```
   filters
```

Type: List<Reports.StandardFilter>

Return Value

Type: void

##### setTopRows(topRows)

Applies a row limit filter to a report.

Signature

```
   public Reports.TopRows setTopRows(Reports.TopRows topRows)

```

Parameters

```
   topRows
```

Type: Reports.TopRows

Return Value

Type: void

### ReportResults Class

Contains the results of running a report.


Apex Reference Guide ReportResults Class

Namespace

Reports

#### ReportResults Methods The following are methods for ReportResults . All are instance methods.

IN THIS SECTION:

##### getAllData()

Returns all report data.

getFactMap()
Returns summary-level data or summary and detailed data for each row or column grouping. Detailed data is available if the
`includeDetails` parameter is set to `true` when the report is run.

getGroupingsAcross()
Returns a collection of column groupings, keys, and values.

getGroupingsDown()
Returns a collection of row groupings, keys, and values.

getHasDetailRows()
Returns information about whether the fact map has detail rows.

getReportExtendedMetadata()
Returns additional, detailed metadata about the report, including data type and label information for groupings and summaries.

getReportMetadata()
Returns metadata about the report, including grouping and summary information.

##### getAllData()

Returns all report data.

Syntax

```
   public Boolean getAllData()

```

Return Value

Type: Boolean

Usage

When `true`, indicates that all report results are returned.

When `false`, indicates that results are returned for the same number of rows as in a report run in Salesforce.

Note: For reports that contain too many records, use filters to refine results.


Apex Reference Guide ReportResults Class

##### getFactMap()

Returns summary-level data or summary and detailed data for each row or column grouping. Detailed data is available if the
`includeDetails` parameter is set to `true` when the report is run.

Syntax

```
   public MAP<String,Reports.ReportFact> getFactMap()

```

Return Value

Type: Map<String,Reports.ReportFact>

##### getGroupingsAcross()

Returns a collection of column groupings, keys, and values.

Syntax

```
   public Reports.Dimension getGroupingsAcross()

```

Return Value

Type: Reports.Dimension

##### getGroupingsDown()

Returns a collection of row groupings, keys, and values.

Syntax

```
   public Reports.Dimension getGroupingsDown()

```

Return Value

Type: Reports.Dimension

##### getHasDetailRows()

Returns information about whether the fact map has detail rows.

Syntax

```
   public Boolean getHasDetailRows()

```

Return Value

Type: Boolean


### Apex Reference Guide ReportScopeInfo Class

Usage

**•** When `true`, indicates that the fact map returns values for summary-level and record-level data.

**•** When `false`, indicates that the fact map returns summary values.

##### getReportExtendedMetadata()

Returns additional, detailed metadata about the report, including data type and label information for groupings and summaries.

Syntax

```
   public Reports.ReportExtendedMetadata getReportExtendedMetadata()

```

Return Value

Type: Reports.ReportExtendedMetadata

##### getReportMetadata()

Returns metadata about the report, including grouping and summary information.

Syntax

```
   public Reports.ReportMetadata getReportMetadata()

```

Return Value

Type: Reports.ReportMetadata

### ReportScopeInfo Class

Contains information about possible scope values that you can choose. Scope values depend on the report type. For example, you can
set the scope for opportunity reports to `All opportunities`, `My team’s opportunities`, or `My opportunities` .

Namespace

Reports

IN THIS SECTION:

#### ReportScopeInfo Methods ReportScopeInfo Methods

### The following are methods for ReportScopeInfo .

IN THIS SECTION:

getDefaultValue()
Returns the default scope of the data to display in the report.


### Apex Reference Guide ReportScopeValue Class

##### getValues()

Returns a list of scope values specified for the report.

##### getDefaultValue()

Returns the default scope of the data to display in the report.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getValues()

Returns a list of scope values specified for the report.

Signature

```
   public List<Reports.ReportScopeValue> getValues()

```

Return Value

Type: List<Reports.ReportScopeValue>

### ReportScopeValue Class

Contains information about a possible scope value. Scope values depend on the report type. For example, you can set the scope for
opportunity reports to `All opportunities`, `My team’s opportunities`, or `My opportunities` .

Namespace

Reports

IN THIS SECTION:

#### ReportScopeValue Methods ReportScopeValue Methods

### The following are methods for ReportScopeValue .

IN THIS SECTION:

getAllowsDivision()
Returns a boolean value that indicates whether you can segment the report by this scope.


### Apex Reference Guide ReportType Class

##### getLabel()

Returns the display name of the scope of the report.

##### getValue()

Returns the scope value for the report.

##### getAllowsDivision()

Returns a boolean value that indicates whether you can segment the report by this scope.

Signature

```
   public Boolean getAllowsDivision()

```

Return Value

Type: Boolean

##### getLabel()

Returns the display name of the scope of the report.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the scope value for the report.

Signature

```
   public String getValue()

```

Return Value

Type: String

### ReportType Class

Contains the unique API name and display name for the report type.

Namespace

Reports


### Apex Reference Guide ReportTypeColumn Class

#### ReportType Methods The following are methods for ReportType . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the localized display name of the report type.

##### getType()

Returns the unique identifier of the report type.

##### getLabel()

Returns the localized display name of the report type.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getType()

Returns the unique identifier of the report type.

Syntax

```
   public String getType()

```

Return Value

Type: String

### ReportTypeColumn Class

Contains detailed report type metadata about a field, including data type, display name, and filter values.

Namespace

Reports

#### ReportTypeColumn Methods

### The following are methods for ReportTypeColumn . All are instance methods.


Apex Reference Guide ReportTypeColumn Class

IN THIS SECTION:

##### getDataType()

Returns the data type of the field.

##### getFilterValues()

If the field data type is picklist, multi-select picklist, boolean, or checkbox, returns all filter values for a field. For example, checkbox
fields always have a value of `true` or `false` . For fields of other data types, the filter value is an empty array, because their values
can’t be determined.

##### getFilterable()

If the field is of a type that can’t be filtered, returns `False` . For example, fields of the type `Encrypted Text` can’t be filtered.

getLabel()
Returns the localized display name of the field.

getName()
Returns the unique API name of the field.

##### getDataType()

Returns the data type of the field.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

##### getFilterValues()

If the field data type is picklist, multi-select picklist, boolean, or checkbox, returns all filter values for a field. For example, checkbox fields
always have a value of `true` or `false` . For fields of other data types, the filter value is an empty array, because their values can’t be
determined.

Syntax

```
   public LIST<Reports.FilterValue> getFilterValues()

```

Return Value

Type: List<Reports.FilterValue>

##### getFilterable()

If the field is of a type that can’t be filtered, returns `False` . For example, fields of the type `Encrypted Text` can’t be filtered.

Syntax

```
   public Boolean getFilterable()

```


### Apex Reference Guide ReportTypeColumnCategory Class

Return Value

Type: Boolean

##### getLabel()

Returns the localized display name of the field.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique API name of the field.

Syntax

```
   public String getName()

```

Return Value

Type: String

### ReportTypeColumnCategory Class

Information about categories of fields in a report type.

Namespace

Reports

Usage

A report type column category is a set of fields that the report type grants access to. For example, an opportunity report has categories
like _Opportunity Information_ and _Primary Contact_ . The Opportunity Information category has fields like _Amount_, _Probability_, and _Close_
_Date_ .

Get category information about a report by first getting the report metadata:

```
   // Get the report ID

   List <Report> reportList = [SELECT Id,DeveloperName FROM Report where DeveloperName =

   'Q1_Opportunities2'];

   String reportId = (String)reportList.get(0).get('Id');

   // Describe the report

   Reports.ReportDescribeResult describeResults =

```


Apex Reference Guide ReportTypeColumnCategory Class

```
   Reports.ReportManager.describeReport(reportId);

   // Get report type metadata

   Reports.ReportTypeMetadata reportTypeMetadata = describeResults.getReportTypeMetadata();

   // Get report type column categories

   List<Reports.ReportTypeColumnCategory> reportTypeColumnCategories =

   reportTypeMetadata.getCategories();

   System.debug('reportTypeColumnCategories: ' + reportTypeColumnCategories);

#### ReportTypeColumnCategory Methods The following are methods for ReportTypeColumnCategory . All are instance methods.

```

IN THIS SECTION:

##### getColumns()

Returns information for all fields in the report type. The information is organized by each section’s unique API name.

##### getLabel()

Returns the localized display name of a section in the report type under which fields are organized. For example, in an Accounts
with Contacts custom report type, `Account General` is the display name of the section that contains fields on general account
information.

##### getColumns()

Returns information for all fields in the report type. The information is organized by each section’s unique API name.

Syntax

```
   public MAP<String,Reports.ReportTypeColumn> getColumns()

```

Return Value

Type: Map<String,Reports.ReportTypeColumn>

##### getLabel()

Returns the localized display name of a section in the report type under which fields are organized. For example, in an Accounts with
Contacts custom report type, `Account General` is the display name of the section that contains fields on general account information.

Syntax

```
   public String getLabel()

```

Return Value

Type: String


### Apex Reference Guide ReportTypeMetadata Class ReportTypeMetadata Class

Contains report type metadata, which gives you information about the fields that are available in each section of the report type, plus
filter information for those fields.

Namespace

Reports

IN THIS SECTION:

#### ReportTypeMetadata Methods ReportTypeMetadata Methods

### The following are methods for ReportTypeMetadata . All are instance methods.

IN THIS SECTION:

##### getCategories()

Returns all fields in the report type. The fields are organized by section.

##### getDivisionInfo()

Returns the default division and a list of all possible divisions that can be applied to this type of report.

getScopeInfo()
Returns information about the scopes that can be applied to this type of report.

getStandardDateFilterDurationGroups()
Returns information about the standard date filter groupings that can be applied to this type of report. Standard date filter groupings
include Calendar Year, Calendar Quarter, Calendar Month, Calendar Week, Fiscal Year, Fiscal Quarter, Day and a custom value based
on a user-defined date range.

getStandardFilterInfos()
Returns information about standard date filters that can be applied to this type of report.

##### getCategories()

Returns all fields in the report type. The fields are organized by section.

Syntax

```
   public LIST<Reports.ReportTypeColumnCategory> getCategories()

```

Return Value

Type: List<Reports.ReportTypeColumnCategory>

##### getDivisionInfo()

Returns the default division and a list of all possible divisions that can be applied to this type of report.


### Apex Reference Guide SortColumn Class

Signature

```
   public Reports.ReportDivisionInfo getDivisionInfo()

```

Return Value

Type: Reports.ReportDivisionInfo

##### getScopeInfo()

Returns information about the scopes that can be applied to this type of report.

Signature

```
   public Reports.ReportScopeInfo getScopeInfo()

```

Return Value

Type: Reports.ReportScopeInfo

##### getStandardDateFilterDurationGroups()

Returns information about the standard date filter groupings that can be applied to this type of report. Standard date filter groupings
include Calendar Year, Calendar Quarter, Calendar Month, Calendar Week, Fiscal Year, Fiscal Quarter, Day and a custom value based on
a user-defined date range.

Signature

```
   public List<Reports.StandardDateFilterDurationGroup>

##### `getStandardDateFilterDurationGroups()`

```

Return Value

Type: List<Reports.StandardDateFilterDurationGroup>

##### getStandardFilterInfos()

Returns information about standard date filters that can be applied to this type of report.

Signature

```
   public Map<String,Reports.StandardFilterInfo> getStandardFilterInfos()

```

Return Value

Type: Map<String,Reports.StandardFilterInfo>

### SortColumn Class

Contains information about the sort column used in the report.


Apex Reference Guide SortColumn Class

Namespace

Reports

IN THIS SECTION:

#### SortColumn Methods SortColumn Methods The following are methods for SortColumn .

IN THIS SECTION:

##### getSortColumn()

Returns the column used to sort the records in the report.

##### getSortOrder()

Returns the the sort order— ascending or descending—for the sort column.

setSortColumn(sortColumn)
Sets the column used to sort the records in the report.

setSortOrder(SortOrder)
Sets the sort order— ascending or descending—for the sort column.

##### getSortColumn()

Returns the column used to sort the records in the report.

Signature

```
   public String getSortColumn()

```

Return Value

Type: String

##### getSortOrder()

Returns the the sort order— ascending or descending—for the sort column.

Signature

```
   public Reports.ColumnSortOrder getSortOrder()

```

Return Value

Type: Reports.ColumnSortOrder


### Apex Reference Guide StandardDateFilter Class

##### setSortColumn(sortColumn)

Sets the column used to sort the records in the report.

Signature

```
   public void setSortColumn(String sortColumn)

```

Parameters

```
   sortColumn
```

Type: String

Return Value

Type: void

##### setSortOrder(SortOrder)

Sets the sort order— ascending or descending—for the sort column.

Signature

```
   public void setSortOrder(Reports.ColumnSortOrder sortOrder)

```

Parameters

```
   sortOrder
```

Type: Reports.ColumnSortOrder

Return Value

Type: void

### StandardDateFilter Class

Contains information about standard date filter available in the report—for example, the API name, start date, and end date of the
standard date filter duration as well as the API name of the date field on which the filter is placed.

Namespace

Reports

IN THIS SECTION:

#### StandardDateFilter Methods StandardDateFilter Methods

### The following are methods for StandardDateFilter .


Apex Reference Guide StandardDateFilter Class

IN THIS SECTION:

##### getColumn()

Returns the API name of the standard date filter column.

##### getDurationValue()

Returns duration information about a standard date filter, such as start date, end date, and display name and API name of the date
filter.

##### getEndDate()

Returns the end date of the standard date filter.

getStartDate()
Returns the start date for the standard date filter.

setColumn(standardDateFilterColumnName)
Sets the API name of the standard date filter column.

setDurationValue(durationName)
Sets the API name of the standard date filter.

setEndDate(endDate)
Sets the end date for the standard date filter.

setStartDate(startDate)
Sets the start date for the standard date filter.

##### getColumn()

Returns the API name of the standard date filter column.

Signature

```
   public String getColumn()

```

Return Value

Type: String

##### getDurationValue()

Returns duration information about a standard date filter, such as start date, end date, and display name and API name of the date filter.

Signature

```
   public String getDurationValue()

```

Return Value

Type: String

##### getEndDate()

Returns the end date of the standard date filter.


Apex Reference Guide StandardDateFilter Class

Signature

```
   public String getEndDate()

```

Return Value

Type: String

##### getStartDate()

Returns the start date for the standard date filter.

Signature

```
   public String getStartDate()

```

Return Value

Type: String

##### setColumn(standardDateFilterColumnName)

Sets the API name of the standard date filter column.

Signature

```
   public void setColumn(String standardDateFilterColumnName)

```

Parameters

```
   standardDateFilterColumnName
```

Type: String

Return Value

Type: void

##### setDurationValue(durationName)

Sets the API name of the standard date filter.

Signature

```
   public void setDurationValue(String durationName)

```

Parameters

```
   durationName
```

Type: String


### Apex Reference Guide StandardDateFilterDuration Class

Return Value

Type: void

##### setEndDate(endDate)

Sets the end date for the standard date filter.

Signature

```
   public void setEndDate(String endDate)

```

Parameters

```
   endDate
```

Type: String

Return Value

Type: void

##### setStartDate(startDate)

Sets the start date for the standard date filter.

Signature

```
   public void setStartDate(String startDate)

```

Parameters

```
   startDate
```

Type: String

Return Value

Type: void

### StandardDateFilterDuration Class

Contains information about each standard date filter—also referred to as a relative date filter. It contains the API name and display label
of the standard date filter duration as well as the start and end dates.

Namespace

Reports

IN THIS SECTION:

StandardDateFilterDuration Methods


Apex Reference Guide StandardDateFilterDuration Class

#### StandardDateFilterDuration Methods The following are methods for StandardDateFilterDuration .

IN THIS SECTION:

##### getEndDate()

Returns the end date of the date filter.

##### getLabel()

Returns the display name of the date filter. Possible values are relative date filters—like `Current FY` and `Current FQ` —and
custom date filters.

##### getStartDate()

Returns the start date of the date filter.

getValue()
Returns the API name of the date filter. Possible values are relative date filters—like `THIS_FISCAL_YEAR` and
`NEXT_FISCAL_QUARTER` —and custom date filters.

##### getEndDate()

Returns the end date of the date filter.

Signature

```
   public String getEndDate()

```

Return Value

Type: String

##### getLabel()

Returns the display name of the date filter. Possible values are relative date filters—like `Current FY` and `Current FQ` —and
custom date filters.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getStartDate()

Returns the start date of the date filter.

Signature

```
   public String getStartDate()

```


### Apex Reference Guide StandardDateFilterDurationGroup Class

Return Value

Type: String

##### getValue()

Returns the API name of the date filter. Possible values are relative date filters—like `THIS_FISCAL_YEAR` and
`NEXT_FISCAL_QUARTER` —and custom date filters.

Signature

```
   public String getValue()

```

Return Value

Type: String

### StandardDateFilterDurationGroup Class

Contains information about the standard date filter groupings, such as the grouping display label and all standard date filters that fall
under the grouping. Groupings include `Calendar Year`, `Calendar Quarter`, `Calendar Month`, `Calendar Week`,
`Fiscal Year`, `Fiscal Quarter`, `Day`, and custom values based on user-defined date ranges.

Namespace

Reports

IN THIS SECTION:

#### StandardDateFilterDurationGroup Methods StandardDateFilterDurationGroup Methods

### The following are methods for StandardDateFilterDurationGroup .

IN THIS SECTION:

##### getLabel()

Returns the display label for the standard date filter grouping.

getStandardDateFilterDurations()
Returns the standard date filter groupings.

##### getLabel()

Returns the display label for the standard date filter grouping.

Signature

```
   public String getLabel()

```


### Apex Reference Guide StandardFilter Class

Return Value

Type: String

##### getStandardDateFilterDurations()

Returns the standard date filter groupings.

Signature

```
   public List<Reports.StandardDateFilterDuration> getStandardDateFilterDurations()

```

Return Value

Type: List<Reports.StandardDateFilterDuration>

For example, a standard filter date grouping might look like this:

```
   Reports.StandardDateFilterDuration[endDate=2015-12-31, label=Current FY,

   startDate=2015-01-01, value=THIS_FISCAL_YEAR],

   Reports.StandardDateFilterDuration[endDate=2014-12-31, label=Previous FY,

   startDate=2014-01-01, value=LAST_FISCAL_YEAR],

   Reports.StandardDateFilterDuration[endDate=2014-12-31, label=Previous 2 FY,

   startDate=2013-01-01, value=LAST_N_FISCAL_YEARS:2]

### StandardFilter Class

```

Contains information about the standard filter defined in the report, such as the filter field API name and filter value.

Namespace

Reports

Usage

Use to get or set standard filters on a report. Standard filters vary by report type. For example, standard filters for reports on the Opportunity
object are Show, Opportunity Status, and Probability.

IN THIS SECTION:

#### StandardFilter Methods StandardFilter Methods

### The following are methods for StandardFilter .

IN THIS SECTION:

getName()
Return the API name of the standard filter.


Apex Reference Guide StandardFilter Class

##### getValue()

Returns the standard filter value.

##### setName(name)

Sets the API name of the standard filter.

setValue(value)
Sets the standard filter value.

##### getName()

Return the API name of the standard filter.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getValue()

Returns the standard filter value.

Signature

```
   public String getValue()

```

Return Value

Type: String

##### setName(name)

Sets the API name of the standard filter.

Signature

```
   public void setName(String name)

```

Parameters

```
   name
```

Type: String

Return Value

Type: void


### Apex Reference Guide StandardFilterInfo Class

##### setValue(value)

Sets the standard filter value.

Signature

```
   public void setValue(String value)

```

Parameters

```
   value
```

Type: String

Return Value

Type: void

### StandardFilterInfo Class

Is an abstract base class for an object that provides standard filter information.

Namespace

Reports

IN THIS SECTION:

#### StandardFilterInfo Methods StandardFilterInfo Methods

### The following are methods for StandardFilterInfo .

IN THIS SECTION:

##### getLabel()

Returns the display label of the standard filter.

getType()
Returns the type of standard filter.

##### getLabel()

Returns the display label of the standard filter.

Signature

```
   public String getLabel()

```


### Apex Reference Guide StandardFilterInfoPicklist Class

Return Value

Type: String

##### getType()

Returns the type of standard filter.

Signature

```
   public Reports.StandardFilterType getType()

```

Return Value

Type: Reports.StandardFilterType

### StandardFilterInfoPicklist Class

Contains information about the standard filter picklist, such as the display name and type of the filter field, the default picklist value, and
a list of all possible picklist values.

Namespace

Reports

IN THIS SECTION:

#### StandardFilterInfoPicklist Methods StandardFilterInfoPicklist Methods

### The following are methods for StandardFilterInfoPicklist .

IN THIS SECTION:

##### getDefaultValue()

Returns the default value for the standard filter picklist.

getFilterValues()
Returns a list of standard filter picklist values.

getLabel()
Returns the display name of the standard filter picklist.

##### getType()

Returns the type of the standard filter picklist.

##### getDefaultValue()

Returns the default value for the standard filter picklist.


### Apex Reference Guide StandardFilterType Enum

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getFilterValues()

Returns a list of standard filter picklist values.

Signature

```
   public List<Reports.FilterValue> getFilterValues()

```

Return Value

Type: List<Reports.FilterValue>

##### getLabel()

Returns the display name of the standard filter picklist.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getType()

Returns the type of the standard filter picklist.

Signature

```
   public Reports.StandardFilterType getType()

```

Return Value

Type: Reports.StandardFilterType

### StandardFilterType Enum The StandardFilterType enum describes the type of standard filters in a report. The getType() method returns a

`Reports.StandardFilterType` enum value.


### Apex Reference Guide SummaryValue Class

Namespace

Reports

Enum Values

The following are the values of the `Reports.StandardFilterType` enum.

**Value** **Description**

`PICKLIST` Values for the standard filter type.

`STRING` String values.

### SummaryValue Class

Contains summary data for a cell of the report.

Namespace

Reports

#### SummaryValue Methods

### The following are methods for SummaryValue . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the formatted summary data for a specified cell.

##### getValue()

Returns the numeric value of the summary data for a specified cell.

##### getLabel()

Returns the formatted summary data for a specified cell.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the numeric value of the summary data for a specified cell.


### Apex Reference Guide ThresholdInformation Class

Syntax

```
   public Object getValue()

```

Return Value

Type: Object

### ThresholdInformation Class

Contains a list of evaluated conditions for a report notification.

Namespace

Reports

IN THIS SECTION:

#### ThresholdInformation Constructors ThresholdInformation Methods ThresholdInformation Constructors

### The following are constructors for ThresholdInformation .

IN THIS SECTION:

##### ThresholdInformation(evaluatedConditions)

Creates a new instance of the `Reports.EvaluatedCondition` class.

##### ThresholdInformation(evaluatedConditions)

Creates a new instance of the `Reports.EvaluatedCondition` class.

Signature

```
   public ThresholdInformation(List<Reports.EvaluatedCondition> evaluatedConditions)

```

Parameters

```
   evaluatedConditions
```

Type: List<Reports.EvaluatedCondition>

A list of `Reports.EvaluatedCondition` objects.

#### ThresholdInformation Methods

### The following are methods for ThresholdInformation .


### Apex Reference Guide TopRows Class

IN THIS SECTION:

##### getEvaluatedConditions()

Returns a list of evaluated conditions for a report notification.

##### getEvaluatedConditions()

Returns a list of evaluated conditions for a report notification.

Signature

```
   public List<Reports.EvaluatedCondition> getEvaluatedConditions()

```

Return Value

Type: List<Reports.EvaluatedCondition>

### TopRows Class

Contains methods and constructors for working with information about a row limit filter.

Namespace

Reports

IN THIS SECTION:

#### TopRows Constructors

TopRows Methods

#### TopRows Constructors

### The following are constructors for TopRows .

IN THIS SECTION:

##### TopRows(rowLimit, direction)

Creates an instance of the `Reports.TopRows` class using the specified parameters.

TopRows()
Creates an instance of the `Reports.TopRows` class. You can then set values by using the class’s `set` methods.

##### TopRows(rowLimit, direction)

Creates an instance of the `Reports.TopRows` class using the specified parameters.

Signature

```
   public TopRows(Integer rowLimit, Reports.ColumnSortOrder direction)

```


Apex Reference Guide TopRows Class

Parameters

```
   rowLimit
```

Type: Integer

The number of rows returned in the report.

```
   direction
```

Type: Reports.ColumnSortOrder

The sort order of the report rows.

##### TopRows()

Creates an instance of the `Reports.TopRows` class. You can then set values by using the class’s `set` methods.

Signature

```
   public TopRows()

#### TopRows Methods

##### The following are methods for TopRows .

```

IN THIS SECTION:

##### getDirection()

Returns the sort order of the report rows.

getRowLimit()
Returns the maximum number of rows shown in the report.

setDirection(value)
Sets the sort order of the report’s rows.

setDirection(direction)
Sets the sort order of the report’s rows.

setRowLimit(rowLimit)
Sets the maximum number of rows included in the report.

toString()
Returns a string.

##### getDirection()

Returns the sort order of the report rows.

Signature

```
   public Reports.ColumnSortOrder getDirection()

```

Return Value

Type: Reports.ColumnSortOrder


Apex Reference Guide TopRows Class

##### getRowLimit()

Returns the maximum number of rows shown in the report.

Signature

```
   public Integer getRowLimit()

```

Return Value

Type: Integer

##### setDirection(value)

Sets the sort order of the report’s rows.

Signature

```
   public void setDirection(String value)

```

Parameters

```
   value
```

Type: String

For possible values, see Reports.ColumnSortOrder.

Return Value

Type: void

##### setDirection(direction)

Sets the sort order of the report’s rows.

Signature

```
   public void setDirection(Reports.ColumnSortOrder direction)

```

Parameters

```
   direction
```

Type: Reports.ColumnSortOrder

Return Value

Type: void

##### setRowLimit(rowLimit)

Sets the maximum number of rows included in the report.


### Apex Reference Guide Reports Exceptions

Signature

```
   public void setRowLimit(Integer rowLimit)

```

Parameters

```
   rowLimit
```

Type: Integer

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### Reports Exceptions The Reports namespace contains exception classes.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions on page 3882.

### The Reports namespace contains these exceptions:

**Exception** **Description** **Methods**

`Reports.FeatureNotSupportedException` Invalid report format

`Reports.InstanceAccessException` Unable to access report
instance

`Reports.InvalidFilterException` Filter validation error `List<String> getFilterErrors()` returns a list of
filter errors

`Reports.InvalidReportMetadataException` Missing metadata for `List<String> getReportMetadataErrors()`
filters returns a list of metadata errors

`Reports.InvalidSnapshotDateException` Invalid historical report `List<String> getSnapshotDateErrors()` returns
format a list of snapshot date errors

`Reports.MetadataException` No selected report
columns

`Reports.ReportRunException` Error running report


## Apex Reference Guide RevSignaling Namespace

**Exception** **Description** **Methods**

`Reports.UnsupportedOperationException` Missing permissions for
running reports

## RevSignaling Namespace The RevSignaling namespace provides classes to extend the standard procedure plan implementation through custom logic. A

procedure plan helps you set up your procedures, configure the procedure execution settings, and relate them to a context definition
in one centralized location based on your requirements.

## The RevSignaling namespace includes these classes and an interface.

**•** [ProcedurePlan Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSignaling_ProcedurePlan.htm)

**•** [SignalingApexProcessor Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_interface_RevSignaling_SignalingApexProcessor.htm)

**•** [TransactionRequest Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSignaling_TransactionRequest.htm)

**•** [TransactionResponse Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSignaling_TransactionResponse.htm)

## RevSalesTrxn Namespace The RevSalesTrxn namespace provides classes and methods to create a sales transaction, such as a quote or an order, with

integrated pricing and configuration.

## The RevSalesTrxn namespace includes these classes.

**•** [ConfigurationOptionsInput Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm)

**•** [GraphRequest Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_GraphRequest.htm)

**•** [PlaceSalesTransactionException Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionException.htm)

**•** [PlaceSalesTransactionExecutor Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm)

**•** [PlaceSalesTransactionResponse Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm)

**•** [RecordResource Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_RecordResource.htm)

**•** [RecordWithReferenceRequest Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm)

SEE ALSO:

_Salesforce Help_ [: Build Your Procedure Plan Framework](https://help.salesforce.com/s/articleView?id=ind.pricing_procedure_plan_framework.htm&language=en_US)

## RichMessaging Namespace

Provides objects and methods for handling content in enhanced Messaging channels.

## The following are the classes in the RichMessaging namespace.

IN THIS SECTION:

AbstractTiming Class
Parent class for other RichMessaging timing classes.


Apex Reference Guide RichMessaging Namespace

AddressableContact Class
Represents an addressable contact.

AuthRequestHandler Interface
Use this interface to handle authorization request responses.

AuthRequestResponse Class
This class contains authorization request response data.

AuthRequestResult Class
This class contains the result from handling the authorization request response.

AuthRequestResultStatus Enum
This enum describes the authentication result status.

DeferredTiming Class
Represents timing for a transaction that occurs in the future.

MessageDefinitionInputParameter Class
Represents a messaging component parameter value. This class is used to provide parameter payloads that can be translated to
structured content payloads in rich content messages.

PaymentItemStatus Enum
Represents the status of a payment item in payment requests sent in enhanced Messaging channels.

PaymentLineItem Class
Represents a payment line item in payment requests sent in enhanced Messaging channels.

PaymentMethod Class
Represents a payment method.

PostalAddress Class
Represents the postal address.

ProcessFormHandler Interface
Apex interface that processes the responses to forms submitted in a messaging session.

ProcessPaymentHandler Interface
Interface used to process payment requests.

ProcessPaymentRequest Class
Represents a request to process a payment.

ProcessPaymentResult Class
Represents the result of a payment processing operation.

ProcessPaymentResultStatus Enum
Represents the status of a payment processing result.

RecurringTiming Class
Represents a payment that occurs on a regular basis.

ShippingMethod Class
Represents a shipping method listed in payment requests sent in enhanced Messaging channels.

TimeSlotOption Class
Represents a complex time slot option type. This class is used to provide time option payloads that can be translated to structured
content payloads in rich content messages.


### Apex Reference Guide AbstractTiming Class

TimingIntervalUnit Enum
Represents an enumerated type that describes the timing interval.

TimingType Enum
Represents an enumerated type that describes the type of timing.

### AbstractTiming Class

Parent class for other RichMessaging timing classes.

Namespace

RichMessaging

SEE ALSO:

DeferredTiming Class

RecurringTiming Class

### AddressableContact Class

Represents an addressable contact.

Namespace

RichMessaging

IN THIS SECTION:

#### AddressableContact Constructors

AddressableContact Properties

#### AddressableContact Constructors

### The following are constructors for AddressableContact .

IN THIS SECTION:

##### AddressableContact(givenName, phoneticGivenName, familyName, phoneticFamilyName, emailAddress, phoneNumber, postalAddress)

Creates a new instance of the `RichMessaging.AddressableContact` class.

##### **`AddressableContact(givenName, phoneticGivenName, familyName,`**

```
  phoneticFamilyName, emailAddress, phoneNumber, postalAddress)

```

Creates a new instance of the `RichMessaging.AddressableContact` class.


Apex Reference Guide AddressableContact Class

Signature

```
   public AddressableContact(String givenName, String phoneticGivenName, String familyName,

   String phoneticFamilyName, String emailAddress, String phoneNumber,

   RichMessaging.PostalAddress postalAddress)

```

Parameters

```
   givenName
```

Type: String

The contact’s first name.

```
   phoneticGivenName
```

Type: String

The phonetic spelling of the contact’s first name.

```
   familyName
```

Type: String

The contact’s surname.

```
   phoneticFamilyName
```

Type: String

The phonetic spelling of the contact’s surname.

```
   emailAddress
```

Type: String

The contact’s email address.

```
   phoneNumber
```

Type: String

The contact’s phone number.

```
   postalAddress
```

Type: RichMessaging.PostalAddress

The contact’s postal address.

#### AddressableContact Properties The following are properties for AddressableContact .

IN THIS SECTION:

emailAddress
The contact’s email address.

familyName
The contact’s surname.

givenName
The contact’s first name.

phoneNumber
The contact’s phone number.


Apex Reference Guide AddressableContact Class

phoneticFamilyName
The phonetic spelling of the contact’s surname.

phoneticGivenName
The phonetic spelling of the contact’s first name.

postalAddress
The contact’s postal address.

##### **`emailAddress`**

The contact’s email address.

Signature

```
   public String emailAddress {get; set;}

```

Property Value

Type: String

##### **`familyName`**

The contact’s surname.

Signature

```
   public String familyName {get; set;}

```

Property Value

Type: String

##### **`givenName`**

The contact’s first name.

Signature

```
   public String givenName {get; set;}

```

Property Value

Type: String

##### **`phoneNumber`**

The contact’s phone number.

Signature

```
   public String phoneNumber {get; set;}

```


### Apex Reference Guide AuthRequestHandler Interface

Property Value

Type: String

##### **`phoneticFamilyName`**

The phonetic spelling of the contact’s surname.

Signature

```
   public String phoneticFamilyName {get; set;}

```

Property Value

Type: String

##### **`phoneticGivenName`**

The phonetic spelling of the contact’s first name.

Signature

```
   public String phoneticGivenName {get; set;}

```

Property Value

Type: String

##### **`postalAddress`**

The contact’s postal address.

Signature

```
   public RichMessaging.PostalAddress postalAddress {get; set;}

```

Property Value

Type: RichMessaging.PostalAddress

### AuthRequestHandler Interface

Use this interface to handle authorization request responses.

Namespace

RichMessaging on page 3409


Apex Reference Guide AuthRequestHandler Interface

Usage

[When using this interface, the following limits are overridden. See Execution Governors and Limits in the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)

**Table 1: Overridden Limits**

IN THIS SECTION:

#### AuthRequestHandler Methods

AuthRequestHandler Example Implementation

#### AuthRequestHandler Methods The following are methods for AuthRequestHandler .

IN THIS SECTION:

##### handleAuthRequest(var1)

Handles authorization request response.

##### **`handleAuthRequest(var1)`**

Handles authorization request response.

Signature

```
   public RichMessaging.AuthRequestResult

   handleAuthRequest(RichMessaging.AuthRequestResponse var1)

```

Parameters

```
   var1
```

Type: RichMessaging.AuthRequestResponse on page 3417

The authorization response.

Return Value

Type: RichMessaging.AuthRequestResult on page 3419


Apex Reference Guide AuthRequestHandler Interface

#### AuthRequestHandler Example Implementation

This is an example implementation of the `RichMessaging.AuthRequestHandler` interface.

```
   global class SampleAuthRequestHandler implements RichMessaging.AuthRequestHandler {

      global RichMessaging.AuthRequestResult

   handleAuthRequest(RichMessaging.AuthRequestResponse authReqResponse) {

        // Get contact email from messaging session

        String sessionId = authReqResponse.getContextRecordId();

        String contactEmail = [select MessagingSession.EndUserContact.Email from

   MessagingSession where id = :sessionId].EndUserContact.Email;

        RichMessaging.AuthRequestResultStatus authRequestStatus =

   RichMessaging.AuthRequestResultStatus.DECLINED;

        DateTime dt = DateTime.now();

        // Get user info if there's a valid contact email

        if (!String.isBlank(contactEmail)) {

           String userInfoUrl = 'https://api.MY_AUTH_DOMAIN.com/v1/';

           HttpRequest req = new HttpRequest();

           req.setEndpoint(userInfoUrl);

           req.setHeader('Content-Type','application/json');

           req.setMethod('GET');

           req.setHeader('Authorization', 'Bearer '+authReqResponse.getAccessToken());

           Http http = new Http();

           HTTPResponse res = http.send(req);

           String responseBody = res.getBody();

           UserWrapper userInfo = (UserWrapper)System.JSON.deserialize(responseBody,

   UserWrapper.class);

           if (userInfo.email == contactEmail) {

             authRequestStatus = RichMessaging.AuthRequestResultStatus.AUTHENTICATED;

             dt = dt.addHours(6);

           }

         }

        return new RichMessaging.AuthRequestResult(

           null,

           authRequestStatus,

           dt);

      }

      public class UserWrapper{

        public String href;

        public String display_name;

        public String type;

        public String country;

        public String product;

        public String email;

```


### Apex Reference Guide AuthRequestResponse Class

```
      }

   }

### AuthRequestResponse Class

```

This class contains authorization request response data.

Namespace

RichMessaging

IN THIS SECTION:

#### AuthRequestResponse Constructors

AuthRequestResponse Methods

#### AuthRequestResponse Constructors

### The following are constructors for AuthRequestResponse .

IN THIS SECTION:

##### AuthRequestResponse(accessToken, contextRecordId, authProviderName)

Creates a new instance of the `RichMessaging.AuthRequestResponse` class.

##### **`AuthRequestResponse(accessToken, contextRecordId, authProviderName)`**

Creates a new instance of the `RichMessaging.AuthRequestResponse` class.

Signature

```
   public AuthRequestResponse(String accessToken, String contextRecordId, String

   authProviderName)

```

Parameters

```
   accessToken
```

Type: String

The authorization access token.

```
   contextRecordId
```

Type: String

The context record ID.

```
   authProviderName
```

Type: String

The provider name.


Apex Reference Guide AuthRequestResponse Class

#### AuthRequestResponse Methods The following are methods for AuthRequestResponse .

IN THIS SECTION:

##### getAccessToken()

Gets the authorization access token.

##### getAuthProviderName()

Get the authorization provider name.

##### getContextRecordId()

Gets the context record ID.

##### **`getAccessToken()`**

Gets the authorization access token.

Signature

```
   public String getAccessToken()

```

Return Value

Type: String

The access token.

##### **`getAuthProviderName()`**

Get the authorization provider name.

Signature

```
   public String getAuthProviderName()

```

Return Value

Type: String

The authorization provider name.

##### **`getContextRecordId()`**

Gets the context record ID.

Signature

```
   public String getContextRecordId()

```


### Apex Reference Guide AuthRequestResult Class

Return Value

Type: String

The context record ID.

### AuthRequestResult Class

This class contains the result from handling the authorization request response.

Namespace

RichMessaging

IN THIS SECTION:

#### AuthRequestResult Constructors

AuthRequestResult Properties

#### AuthRequestResult Constructors

### The following are constructors for AuthRequestResult .

IN THIS SECTION:

##### AuthRequestResult(redirectPageReference, resultStatus, expirationDateTime)

Creates a new instance of the `RichMessaging.AuthRequestResult` class.

##### **`AuthRequestResult(redirectPageReference, resultStatus, expirationDateTime)`**

Creates a new instance of the `RichMessaging.AuthRequestResult` class.

Signature

```
   public AuthRequestResult(System.PageReference redirectPageReference,

   RichMessaging.AuthRequestResultStatus resultStatus, Datetime expirationDateTime)

```

Parameters

```
   redirectPageReference
```

Type: System.PageReference on page 4086

The reference to the redirect page.

```
   resultStatus
```

Type: RichMessaging.AuthRequestResultStatus on page 3421

The result status value.

```
   expirationDateTime
```

Type: Datetime

The expiration time.


Apex Reference Guide AuthRequestResult Class

#### AuthRequestResult Properties The following are properties for AuthRequestResult .

IN THIS SECTION:

##### expirationDateTime

The expiration date and time.

##### redirectPageReference

The reference to the redirect page.

##### resultStatus

The result status value.

##### **`expirationDateTime`**

The expiration date and time.

Signature

```
   public Datetime expirationDateTime {get; set;}

```

Property Value

Type: Datetime

##### **`redirectPageReference`**

The reference to the redirect page.

Signature

```
   public System.PageReference redirectPageReference {get; set;}

```

Property Value

Type: System.PageReference on page 4086

##### **`resultStatus`**

The result status value.

Signature

```
   public RichMessaging.AuthRequestResultStatus resultStatus {get; set;}

```

Property Value

Type: RichMessaging.AuthRequestResultStatus on page 3421


### Apex Reference Guide AuthRequestResultStatus Enum AuthRequestResultStatus Enum

This enum describes the authentication result status.

Enum Values

The following are the values of the `RichMessaging.AuthRequestResultStatus` enum.

**Value** **Description**

`AUTHENTICATED` Authenticated result.

`DECLINED` Declined result.

### DeferredTiming Class

Represents timing for a transaction that occurs in the future.

Namespace

RichMessaging

IN THIS SECTION:

#### DeferredTiming Constructors

DeferredTiming Properties

#### DeferredTiming Constructors

### The following are constructors for DeferredTiming .

IN THIS SECTION:

##### DeferredTiming(deferredDate)

Creates a new instance of the `RichMessaging.DeferredTiming` class.

DeferredTiming()
Creates a new instance of the `RichMessaging.DeferredTiming` class.

##### **`DeferredTiming(deferredDate)`**

Creates a new instance of the `RichMessaging.DeferredTiming` class.

Signature

```
   public DeferredTiming(Datetime deferredDate)

```


Apex Reference Guide DeferredTiming Class

Parameters

##### _`deferredDate`_

Type: Datetime

The deferred date.

##### **`DeferredTiming()`**

Creates a new instance of the `RichMessaging.DeferredTiming` class.

Signature

```
   public DeferredTiming()

#### DeferredTiming Properties

##### The following are properties for DeferredTiming .

```

IN THIS SECTION:

##### deferredDate

The deferred date. Invocable variable.

##### deferredDateValue

The deferred date. Enabled for Lightning components.

timingType
Always returns “DeferredTiming”.

##### **`deferredDate`**

The deferred date. Invocable variable.

Signature

```
   public Datetime deferredDate {get; set;}

```

Property Value

Type: Datetime

##### **`deferredDateValue`**

The deferred date. Enabled for Lightning components.

Signature

```
   public Datetime deferredDateValue {get; set;}

```

Property Value

Type: Datetime


### Apex Reference Guide MessageDefinitionInputParameter Class

##### **`timingType`**

Always returns “DeferredTiming”.

Signature

```
   public String timingType {get; set;}

```

Property Value

Type: String

### MessageDefinitionInputParameter Class

Represents a messaging component parameter value. This class is used to provide parameter payloads that can be translated to structured
content payloads in rich content messages.

Namespace

RichMessaging

IN THIS SECTION:

#### MessageDefinitionInputParameter Properties MessageDefinitionInputParameter Properties

### The following are properties for MessageDefinitionInputParameter .

IN THIS SECTION:

booleanValue
A boolean input parameter.

booleanValues
A list of boolean parameters.

dateTimeValue
A datetime input parameter.

dateTimeValues
A list of datetime input parameters.

dateValue
A date input parameter.

dateValues
A list of date input parameters.

name
A name input parameter.

numberValue
A number input parameter.


Apex Reference Guide MessageDefinitionInputParameter Class

numberValues
A list of number input parameters.

recordIdValue
A record ID input parameter.

recordIdValues
A list of record ID input parameters.

textValue
A text input parameter.

textValues
A list of text input parameters.

##### **`booleanValue`**

A boolean input parameter.

Signature

```
   public Boolean booleanValue {get; set;}

```

Property Value

Type: Boolean

##### **`booleanValues`**

A list of boolean parameters.

Signature

```
   public List<Boolean> booleanValues {get; set;}

```

Property Value

Type: List on page 3992<Boolean>

##### **`dateTimeValue`**

A datetime input parameter.

Signature

```
   public Datetime dateTimeValue {get; set;}

```

Property Value

Type: Datetime


Apex Reference Guide MessageDefinitionInputParameter Class

##### **`dateTimeValues`**

A list of datetime input parameters.

Signature

```
   public List<Datetime> dateTimeValues {get; set;}

```

Property Value

Type: List on page 3992<Datetime>

##### **`dateValue`**

A date input parameter.

Signature

```
   public Date dateValue {get; set;}

```

Property Value

Type: Date

##### **`dateValues`**

A list of date input parameters.

Signature

```
   public List<Date> dateValues {get; set;}

```

Property Value

Type: List on page 3992<Date>

##### **`name`**

A name input parameter.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### **`numberValue`**

A number input parameter.


Apex Reference Guide MessageDefinitionInputParameter Class

Signature

```
   public Double numberValue {get; set;}

```

Property Value

Type: Double

##### **`numberValues`**

A list of number input parameters.

Signature

```
   public List<Double> numberValues {get; set;}

```

Property Value

Type: List on page 3992<Double>

##### **`recordIdValue`**

A record ID input parameter.

Signature

```
   public String recordIdValue {get; set;}

```

Property Value

Type: String

##### **`recordIdValues`**

A list of record ID input parameters.

Signature

```
   public List<String> recordIdValues {get; set;}

```

Property Value

Type: List on page 3992<String>

##### **`textValue`**

A text input parameter.

Signature

```
   public String textValue {get; set;}

```


### Apex Reference Guide PaymentItemStatus Enum

Property Value

Type: String

##### **`textValues`**

A list of text input parameters.

Signature

```
   public List<String> textValues {get; set;}

```

Property Value

Type: List on page 3992<String>

### PaymentItemStatus Enum

Represents the status of a payment item in payment requests sent in enhanced Messaging channels.

Enum Values

The following are the values of the `RichMessaging.PaymentItemStatus` enum.

**Value** **Description**

`FinalCost` Indicates that the payment item's cost is final and has been determined.

`PendingCost` Indicates that the payment item's cost is pending and has not been determined
yet.

### PaymentLineItem Class

Represents a payment line item in payment requests sent in enhanced Messaging channels.

Namespace

RichMessaging

Example

```
   public with sharing class MessagingPaymentLineItems {

      @InvocableMethod

      public static List<List<RichMessaging.PaymentLineItem>> getLineItems() {

        Double amount = 0.25;

        List<List<RichMessaging.PaymentLineItem>> result = new

   List<List<RichMessaging.PaymentLineItem>>();

        RichMessaging.PaymentLineItem pizza = new RichMessaging.PaymentLineItem('pizza',

   amount);

```


Apex Reference Guide PaymentLineItem Class

```
        RichMessaging.PaymentLineItem pasta = new RichMessaging.PaymentLineItem('pasta',

   amount);

        pizza.statusValue = RichMessaging.PaymentItemStatus.FinalCost;

        pasta.statusValue = RichMessaging.PaymentItemStatus.FinalCost;

        List<RichMessaging.PaymentLineItem> options = new

   List<RichMessaging.PaymentLineItem>{

           pizza, pasta

        };

        result.add(options);

        return result;

      }

   }

```

IN THIS SECTION:

#### PaymentLineItem Constructors

PaymentLineItem Properties

PaymentLineItem Methods

#### PaymentLineItem Constructors The following are constructors for PaymentLineItem .

IN THIS SECTION:

##### PaymentLineItem(label, amount, timing)

Creates a new instance of the `RichMessaging.PaymentLineItem` class.

PaymentLineItem(label, amount)
Creates a new instance of the `RichMessaging.PaymentLineItem` class.

PaymentLineItem()
Creates a new instance of the `RichMessaging.PaymentLineItem` class.

##### **`PaymentLineItem(label, amount, timing)`**

Creates a new instance of the `RichMessaging.PaymentLineItem` class.

Signature

```
   public PaymentLineItem(String label, Double amount, RichMessaging.AbstractTiming timing)

```

Parameters

```
   label
```

Type: String

The label of the payment line item.


Apex Reference Guide PaymentLineItem Class

```
   amount
```

Type: Double

The amount of the payment line item.

```
   timing
```

Type: RichMessaging.AbstractTiming

The timing of the payment line item.

##### **`PaymentLineItem(label, amount)`**

Creates a new instance of the `RichMessaging.PaymentLineItem` class.

Signature

```
   public PaymentLineItem(String label, Double amount)

```

Parameters

```
   label
```

Type: String

The label of the payment line item.

```
   amount
```

Type: Double

The amount of the payment line item.

##### **`PaymentLineItem()`**

Creates a new instance of the `RichMessaging.PaymentLineItem` class.

Signature

```
   public PaymentLineItem()

#### PaymentLineItem Properties

##### The following are properties for PaymentLineItem .

```

IN THIS SECTION:

amount
The amount of the payment line item.

amountValue
The amount value of the payment line item.

automaticReloadPaymentThresholdAmount
The automatic reload payment threshold amount of the payment line item.

automaticReloadPaymentThresholdAmountValue
The automatic reload payment threshold amount value of the payment line item.


Apex Reference Guide PaymentLineItem Class

label
The label of the payment line item.

labelValue
The label value of the payment line item.

lineItemType
The line item type of the payment line item. Read-only variable.

status
The status of the payment line item.

statusValue
The status value of the payment line item.

timing
The timing of the payment line item.

timingValue
The timing value of the payment line item.

##### **`amount`**

The amount of the payment line item.

Signature

```
   public Double amount {get; set;}

```

Property Value

Type: Double

##### **`amountValue`**

The amount value of the payment line item.

Signature

```
   public Double amountValue {get; set;}

```

Property Value

Type: Double

##### **`automaticReloadPaymentThresholdAmount`**

The automatic reload payment threshold amount of the payment line item.

Signature

```
   public Double automaticReloadPaymentThresholdAmount {get; set;}

```


Apex Reference Guide PaymentLineItem Class

Property Value

Type: Double

##### **`automaticReloadPaymentThresholdAmountValue`**

The automatic reload payment threshold amount value of the payment line item.

Signature

```
   public Double automaticReloadPaymentThresholdAmountValue {get; set;}

```

Property Value

Type: Double

##### **`label`**

The label of the payment line item.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### **`labelValue`**

The label value of the payment line item.

Signature

```
   public String labelValue {get; set;}

```

Property Value

Type: String

##### **`lineItemType`**

The line item type of the payment line item. Read-only variable.

Signature

```
   public String lineItemType {get; set;}

```

Property Value

Type: String


Apex Reference Guide PaymentLineItem Class

##### **`status`**

The status of the payment line item.

Signature

```
   public String status {get; set;}

```

Property Value

Type: String

##### **`statusValue`**

The status value of the payment line item.

Signature

```
   public RichMessaging.PaymentItemStatus statusValue {get; set;}

```

Property Value

Type: RichMessaging.PaymentItemStatus

##### **`timing`**

The timing of the payment line item.

Signature

```
   public RichMessaging.AbstractTiming timing {get; set;}

```

Property Value

Type: RichMessaging.AbstractTiming

##### **`timingValue`**

The timing value of the payment line item.

Signature

```
   public RichMessaging.AbstractTiming timingValue {get; set;}

```

Property Value

Type: RichMessaging.AbstractTiming

#### PaymentLineItem Methods The following are methods for PaymentLineItem .


### Apex Reference Guide PaymentMethod Class PaymentMethod Class

Represents a payment method.

Namespace

RichMessaging

IN THIS SECTION:

#### PaymentMethod Constructors PaymentMethod Properties PaymentMethod Constructors

### The following are constructors for PaymentMethod .

IN THIS SECTION:

##### PaymentMethod(network, paymentType, displayName)

Creates a new instance of the `RichMessaging.PaymentMethod` class.

##### **`PaymentMethod(network, paymentType, displayName)`**

Creates a new instance of the `RichMessaging.PaymentMethod` class.

Signature

```
   public PaymentMethod(String network, String paymentType, String displayName)

```

Parameters

```
   network
```

Type: String

The network associated with the payment method.

```
   paymentType
```

Type: String

The payment type of the payment method.

```
   displayName
```

Type: String

The display name of the payment method.

#### PaymentMethod Properties

### The following are properties for PaymentMethod .


### Apex Reference Guide PostalAddress Class

IN THIS SECTION:

##### displayName

The display name of the payment method.

##### network

The network associated with the payment method.

##### paymentType

The payment type of the payment method.

##### **`displayName`**

The display name of the payment method.

Signature

```
   public String displayName {get; set;}

```

Property Value

Type: String

##### **`network`**

The network associated with the payment method.

Signature

```
   public String network {get; set;}

```

Property Value

Type: String

##### **`paymentType`**

The payment type of the payment method.

Signature

```
   public String paymentType {get; set;}

```

Property Value

Type: String

### PostalAddress Class

Represents the postal address.


Apex Reference Guide PostalAddress Class

Namespace

RichMessaging

IN THIS SECTION:

#### PostalAddress Constructors

PostalAddress Properties

#### PostalAddress Constructors The following are constructors for PostalAddress .

IN THIS SECTION:

##### PostalAddress(addressLines, subLocality, locality, postalCode, subAdministrativeArea, administrativeArea, country, countryCode)

Creates a new instance of the `RichMessaging.PostalAddress` class.

##### **`PostalAddress(addressLines, subLocality, locality, postalCode,`**

```
  subAdministrativeArea, administrativeArea, country, countryCode)

```

Creates a new instance of the `RichMessaging.PostalAddress` class.

Signature

```
   public PostalAddress(List<String> addressLines, String subLocality, String locality,

   String postalCode, String subAdministrativeArea, String administrativeArea, String

   country, String countryCode)

```

Parameters

```
   addressLines
```

Type: List<String>

The street address.

```
   subLocality
```

Type: String

The sub-locality of the address.

```
   locality
```

Type: String

The locality of the address.

```
   postalCode
```

Type: String

The postal code.

```
   subAdministrativeArea
```

Type: String

The sub-administrative area.


Apex Reference Guide PostalAddress Class

```
   administrativeArea
```

Type: String

The administrative area.

```
   country
```

Type: String

The country.

```
   countryCode
```

Type: String

The country code.

#### PostalAddress Properties The following are properties for PostalAddress .

IN THIS SECTION:

##### addressLines

The street address.

administrativeArea
The administrative area.

country
The country.

countryCode
The country code.

locality
The locality of the address.

postalCode
The postal code.

subAdministrativeArea
The sub-administrative area.

subLocality
The sub-locality of the address.

##### **`addressLines`**

The street address.

Signature

```
   public List<String> addressLines {get; set;}

```

Property Value

Type: List<String>


Apex Reference Guide PostalAddress Class

##### **`administrativeArea`**

The administrative area.

Signature

```
   public String administrativeArea {get; set;}

```

Property Value

Type: String

##### **`country`**

The country.

Signature

```
   public String country {get; set;}

```

Property Value

Type: String

##### **`countryCode`**

The country code.

Signature

```
   public String countryCode {get; set;}

```

Property Value

Type: String

##### **`locality`**

The locality of the address.

Signature

```
   public String locality {get; set;}

```

Property Value

Type: String

##### **`postalCode`**

The postal code.


### Apex Reference Guide ProcessFormHandler Interface

Signature

```
   public String postalCode {get; set;}

```

Property Value

Type: String

##### **`subAdministrativeArea`**

The sub-administrative area.

Signature

```
   public String subAdministrativeArea {get; set;}

```

Property Value

Type: String

##### **`subLocality`**

The sub-locality of the address.

Signature

```
   public String subLocality {get; set;}

```

Property Value

Type: String

### ProcessFormHandler Interface

Apex interface that processes the responses to forms submitted in a messaging session.

Namespace

RichMessaging

IN THIS SECTION:

#### ProcessFormHandler Methods ProcessFormHandler Methods

### The following are methods for ProcessFormHandler .


### Apex Reference Guide ProcessPaymentHandler Interface

IN THIS SECTION:

##### processFormRequest

Processes the form request and returns the ID of the record created during form processing.

##### **`processFormRequest`**

Processes the form request and returns the ID of the record created during form processing.

Signature

```
   ID processFormRequest(RichMessaging.ProcessFormResponse formResponse)

```

Parameters

```
   formResponse
```

Type: RichMessaging.ProcessFormResponse

The form response.

Return Value

```
   ID
```

Type: RichMessaging.ProcessFormResponse

ProcessFormHandler Example Implementation

The sample `ContactApexFormHandler` Apex class automatically captures the customer's submitted details, creates a Contact
record in Salesforce, and returns the Contact record ID.

This is an example implementation of the `RichMessaging.ProcessFormHandler` interface.

```
   global class ContactApexFormHandler implements Richmessaging.ProcessFormHandler{

      global ID

##### `processFormRequest(RichMessaging.ProcessFormResponse formResponse) {`

        // Create a new Contact object

           Contact newContact = new Contact(

           Phone = formResponse.formValues.get('Phone'),

           Salutation = formResponse.formValues.get('Salutation'),

           Email = formResponse.formValues.get('Email')

           );

      // Insert the new contact into the database

      insert newContact;

      // Return the ID of the newly created contact

      return newContact.Id;

```

[For more information, see "Create a Form Based on an Apex Class" in this help topic.](https://help.salesforce.com/s/articleView?id=service.messaging_components_forms.htm&language=en_US)

### ProcessPaymentHandler Interface

Interface used to process payment requests.


Apex Reference Guide ProcessPaymentHandler Interface

Namespace

RichMessaging

IN THIS SECTION:

#### ProcessPaymentHandler Methods ProcessPaymentHandler Example Implementation ProcessPaymentHandler Methods The following are methods for ProcessPaymentHandler .

IN THIS SECTION:

##### processPaymentRequest(var1)

Processes a payment request.

##### **`processPaymentRequest(var1)`**

Processes a payment request.

Signature

```
   public RichMessaging.ProcessPaymentResult

   processPaymentRequest(RichMessaging.ProcessPaymentRequest var1)

```

Parameters

```
   var1
```

Type: RichMessaging.ProcessPaymentRequest

The payment request.

Return Value

Type: RichMessaging.ProcessPaymentResult

#### ProcessPaymentHandler Example Implementation

This is an example implementation of the `RichMessaging.ProcessPaymentHandler` interface.

```
   global class MyProcessPaymentHandler implements Richmessaging.ProcessPaymentHandler {

     global RichMessaging.ProcessPaymentResult

   processPaymentRequest(RichMessaging.ProcessPaymentRequest paymentRequest) {

        // TODO: Reach out to your payment processor here and return success or failure

   based on the result of that request

        return new

```


### Apex Reference Guide ProcessPaymentRequest Class

```
   RichMessaging.ProcessPaymentResult(RichMessaging.ProcessPaymentResultStatus.SUCCESS);

     }

   }

### ProcessPaymentRequest Class

```

Represents a request to process a payment.

Namespace

RichMessaging

IN THIS SECTION:

#### ProcessPaymentRequest Constructors

ProcessPaymentRequest Properties

#### ProcessPaymentRequest Constructors

### The following are constructors for ProcessPaymentRequest .

IN THIS SECTION:

##### ProcessPaymentRequest(transactionIdentifier, paymentData, billingContact, shippingContact, paymentMethod, shippingMethod,

contextRecordId)
Creates a new instance of the `RichMessaging.ProcessPaymentRequest` class.

##### **`ProcessPaymentRequest(transactionIdentifier, paymentData, billingContact,`**

```
  shippingContact, paymentMethod, shippingMethod, contextRecordId)

```

Creates a new instance of the `RichMessaging.ProcessPaymentRequest` class.

Signature

```
   public ProcessPaymentRequest(String transactionIdentifier, String paymentData,

   RichMessaging.AddressableContact billingContact, RichMessaging.AddressableContact

   shippingContact, RichMessaging.PaymentMethod paymentMethod, RichMessaging.ShippingMethod

   shippingMethod, String contextRecordId)

```

Parameters

```
   transactionIdentifier
```

Type: String

The transaction identifier associated with the payment request.

```
   paymentData
```

Type: String

The encrypted payment data for the payment request.


Apex Reference Guide ProcessPaymentRequest Class

##### _`billingContact`_

Type: RichMessaging.AddressableContact

The billing contact information for the payment request.

```
   shippingContact
```

Type: RichMessaging.AddressableContact

The shipping contact information for the payment request.

```
   paymentMethod
```

Type: RichMessaging.PaymentMethod

The payment method for the payment request.

```
   shippingMethod
```

Type: RichMessaging.ShippingMethod

The shipping method for the payment request.

```
   contextRecordId
```

Type: String

The context record ID associated with the payment request.

#### ProcessPaymentRequest Properties The following are properties for ProcessPaymentRequest .

IN THIS SECTION:

##### billingContact

The billing contact information for the payment request.

contextRecordId
The context record ID associated with the payment request.

paymentData
The encrypted payment data for the payment request.

paymentMethod
The payment method for the payment request.

shippingContact
The shipping contact information for the payment request.

shippingMethod
The shipping method for the payment request.

transactionIdentifier
The transaction identifier associated with the payment request.

##### **`billingContact`**

The billing contact information for the payment request.


Apex Reference Guide ProcessPaymentRequest Class

Signature

```
   public RichMessaging.AddressableContact billingContact {get; set;}

```

Property Value

Type: RichMessaging.AddressableContact

##### **`contextRecordId`**

The context record ID associated with the payment request.

Signature

```
   public String contextRecordId {get; set;}

```

Property Value

Type: String

##### **`paymentData`**

The encrypted payment data for the payment request.

Signature

```
   public String paymentData {get; set;}

```

Property Value

Type: String

##### **`paymentMethod`**

The payment method for the payment request.

Signature

```
   public RichMessaging.PaymentMethod paymentMethod {get; set;}

```

Property Value

Type: RichMessaging.PaymentMethod

##### **`shippingContact`**

The shipping contact information for the payment request.

Signature

```
   public RichMessaging.AddressableContact shippingContact {get; set;}

```


### Apex Reference Guide ProcessPaymentResult Class

Property Value

Type: RichMessaging.AddressableContact

##### **`shippingMethod`**

The shipping method for the payment request.

Signature

```
   public RichMessaging.ShippingMethod shippingMethod {get; set;}

```

Property Value

Type: RichMessaging.ShippingMethod

##### **`transactionIdentifier`**

The transaction identifier associated with the payment request.

Signature

```
   public String transactionIdentifier {get; set;}

```

Property Value

Type: String

### ProcessPaymentResult Class

Represents the result of a payment processing operation.

Namespace

RichMessaging

IN THIS SECTION:

#### ProcessPaymentResult Constructors

ProcessPaymentResult Properties

#### ProcessPaymentResult Constructors

### The following are constructors for ProcessPaymentResult .

IN THIS SECTION:

ProcessPaymentResult(resultStatus, errorMessage)
Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.


Apex Reference Guide ProcessPaymentResult Class

##### ProcessPaymentResult(resultStatus)

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

##### **`ProcessPaymentResult(resultStatus, errorMessage)`**

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

Signature

```
   public ProcessPaymentResult(RichMessaging.ProcessPaymentResultStatus resultStatus,

   String errorMessage)

```

Parameters

```
   resultStatus
```

Type: RichMessaging.ProcessPaymentResultStatus

The status of the payment processing result.

```
   errorMessage
```

Type: String

The error message associated with the payment processing result, if any.

##### **`ProcessPaymentResult(resultStatus)`**

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

Signature

```
   public ProcessPaymentResult(RichMessaging.ProcessPaymentResultStatus resultStatus)

```

Parameters

```
   resultStatus
```

Type: RichMessaging.ProcessPaymentResultStatus

The status of the payment processing result.

#### ProcessPaymentResult Properties

##### The following are properties for ProcessPaymentResult .

IN THIS SECTION:

errorMessage
The error message associated with the payment processing result, if any.

resultStatus
The status of the payment processing result.


### Apex Reference Guide ProcessPaymentResultStatus Enum

##### **`errorMessage`**

The error message associated with the payment processing result, if any.

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String

##### **`resultStatus`**

The status of the payment processing result.

Signature

```
   public RichMessaging.ProcessPaymentResultStatus resultStatus {get; set;}

```

Property Value

Type: RichMessaging.ProcessPaymentResultStatus

### ProcessPaymentResultStatus Enum

Represents the status of a payment processing result.

Enum Values

The following are the values of the `RichMessaging.ProcessPaymentResultStatus` enum.

**Value** **Description**

`PROCESSOR_ERROR` Indicates an error occurred during payment processing at the processor level.

`SUCCESS` Indicates a successful payment processing result.

### RecurringTiming Class

Represents a payment that occurs on a regular basis.

Namespace

RichMessaging

IN THIS SECTION:

RecurringTiming Constructors

RecurringTiming Properties


Apex Reference Guide RecurringTiming Class

#### RecurringTiming Constructors The following are constructors for RecurringTiming .

IN THIS SECTION:

##### RecurringTiming(startDate, endDate, intervalCount, intervalUnit)

Creates a new instance of the `RichMessaging.RecurringTiming` class.

##### RecurringTiming()

Creates a new instance of the `RichMessaging.RecurringTiming` class.

##### **`RecurringTiming(startDate, endDate, intervalCount, intervalUnit)`**

Creates a new instance of the `RichMessaging.RecurringTiming` class.

Signature

```
   public RecurringTiming(Date startDate, Date endDate, Integer intervalCount,

   RichMessaging.TimingIntervalUnit intervalUnit)

```

Parameters

```
   startDate
```

Type: Date

The start date. Invocable variable.

```
   endDate
```

Type: Date

The end date. Invocable variable.

```
   intervalCount
```

Type: Integer

The number of interval units that make up the total payment interval. Invocable variable.

```
   intervalUnit
```

Type: RichMessaging.TimingIntervalUnit

The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval.
Invocable variable.

##### **`RecurringTiming()`**

Creates a new instance of the `RichMessaging.RecurringTiming` class.

Signature

```
   public RecurringTiming()

#### RecurringTiming Properties The following are properties for RecurringTiming .

```


Apex Reference Guide RecurringTiming Class

IN THIS SECTION:

##### endDate

The end date. Invocable variable.

##### endDateValue

The end date. Enabled for Lightning components.

intervalCount
The number of interval units that make up the total payment interval. Invocable variable.

intervalCountValue
The number of interval units that make up the total payment interval. Enabled for Lightning components.

intervalUnit
The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval.
Invocable variable.

intervalUnitValue
The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval. Enabled
for Lightning components.

startDate
The start date. Invocable variable.

startDateValue
The start date. Enabled for Lightning components.

timingType
Always returns “RecurringTiming”.

##### **`endDate`**

The end date. Invocable variable.

Signature

```
   public Date endDate {get; set;}

```

Property Value

Type: Date

##### **`endDateValue`**

The end date. Enabled for Lightning components.

Signature

```
   public Date endDateValue {get; set;}

```

Property Value

Type: Date


Apex Reference Guide RecurringTiming Class

##### **`intervalCount`**

The number of interval units that make up the total payment interval. Invocable variable.

Signature

```
   public Integer intervalCount {get; set;}

```

Property Value

Type: Integer

##### **`intervalCountValue`**

The number of interval units that make up the total payment interval. Enabled for Lightning components.

Signature

```
   public Integer intervalCountValue {get; set;}

```

Property Value

Type: Integer

##### **`intervalUnit`**

The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval. Invocable
variable.

Signature

```
   public String intervalUnit {get; set;}

```

Property Value

Type: String

##### **`intervalUnitValue`**

The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval. Enabled
for Lightning components.

Signature

```
   public RichMessaging.TimingIntervalUnit intervalUnitValue {get; set;}

```

Property Value

Type: RichMessaging.TimingIntervalUnit


### Apex Reference Guide ShippingMethod Class

##### **`startDate`**

The start date. Invocable variable.

Signature

```
   public Date startDate {get; set;}

```

Property Value

Type: Date

##### **`startDateValue`**

The start date. Enabled for Lightning components.

Signature

```
   public Date startDateValue {get; set;}

```

Property Value

Type: Date

##### **`timingType`**

Always returns “RecurringTiming”.

Signature

```
   public String timingType {get; set;}

```

Property Value

Type: String

### ShippingMethod Class

Represents a shipping method listed in payment requests sent in enhanced Messaging channels.

Namespace

RichMessaging

Example

```
   public with sharing class MessagingShippingMethods {

      @InvocableMethod

      public static List<List<RichMessaging.ShippingMethod>> getShippingMethods(){

```


Apex Reference Guide ShippingMethod Class

```
        Double amount = 0.25;

        List<List<RichMessaging.ShippingMethod>> result = new

   List<List<RichMessaging.ShippingMethod>>();

       List<RichMessaging.ShippingMethod> options = new List<RichMessaging.ShippingMethod>{

          new RichMessaging.ShippingMethod('doordash', amount, '1 hour delivery to your

    door', 'ddash'),

           new RichMessaging.ShippingMethod('UPS', amount, '2 days delivery', 'UPS')

        };

        result.add(options);

        return result;

      }

   }

```

IN THIS SECTION:

#### ShippingMethod Constructors

ShippingMethod Properties

#### ShippingMethod Constructors The following are constructors for ShippingMethod .

IN THIS SECTION:

##### ShippingMethod(label, amount, detail, identifier)

Creates a new instance of the `RichMessaging.ShippingMethod` class.

ShippingMethod()
Creates a new instance of the `RichMessaging.ShippingMethod` class.

##### **`ShippingMethod(label, amount, detail, identifier)`**

Creates a new instance of the `RichMessaging.ShippingMethod` class.

Signature

```
   public ShippingMethod(String label, Double amount, String detail, String identifier)

```

Parameters

```
   label
```

Type: String

The label of the shipping method.

```
   amount
```

Type: Double

The amount of the shipping method.


Apex Reference Guide ShippingMethod Class

```
   detail
```

Type: String

Details about the shipping method.

```
   identifier
```

Type: String

The identifier of the shipping method.

##### **`ShippingMethod()`**

Creates a new instance of the `RichMessaging.ShippingMethod` class.

Signature

```
   public ShippingMethod()

#### ShippingMethod Properties

##### The following are properties for ShippingMethod .

```

IN THIS SECTION:

##### amount

The amount of the shipping method.

##### amountValue

The amount value of the shipping method.

detail
Details about the shipping method.

detailValue
The detail value of the shipping method.

identifier
The identifier of the shipping method.

identifierValue
The identifier value of the shipping method.

label
The label of the shipping method.

labelValue
The label value of the shipping method.

shippingMethodType
The shipping method type. Read only.

##### **`amount`**

The amount of the shipping method.


Apex Reference Guide ShippingMethod Class

Signature

```
   public Double amount {get; set;}

```

Property Value

Type: Double

##### **`amountValue`**

The amount value of the shipping method.

Signature

```
   public Double amountValue {get; set;}

```

Property Value

Type: Double

##### **`detail`**

Details about the shipping method.

Signature

```
   public String detail {get; set;}

```

Property Value

Type: String

##### **`detailValue`**

The detail value of the shipping method.

Signature

```
   public String detailValue {get; set;}

```

Property Value

Type: String

##### **`identifier`**

The identifier of the shipping method.

Signature

```
   public String identifier {get; set;}

```


Apex Reference Guide ShippingMethod Class

Property Value

Type: String

##### **`identifierValue`**

The identifier value of the shipping method.

Signature

```
   public String identifierValue {get; set;}

```

Property Value

Type: String

##### **`label`**

The label of the shipping method.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### **`labelValue`**

The label value of the shipping method.

Signature

```
   public String labelValue {get; set;}

```

Property Value

Type: String

##### **`shippingMethodType`**

The shipping method type. Read only.

Signature

```
   public String shippingMethodType {get; set;}

```

Property Value

Type: String


### Apex Reference Guide TimeSlotOption Class TimeSlotOption Class

Represents a complex time slot option type. This class is used to provide time option payloads that can be translated to structured
content payloads in rich content messages.

Namespace

RichMessaging

IN THIS SECTION:

#### TimeSlotOption Constructors

TimeSlotOption Properties

#### TimeSlotOption Constructors

### The following are constructors for TimeSlotOption .

IN THIS SECTION:

##### TimeSlotOption(startTime, endTime)
### Creates a TimeSlotOption object with a start and end time.

##### TimeSlotOption(startTime, duration)
### Creates a TimeSlotOption object with a start time and a duration.

TimeSlotOption()
### Creates a TimeSlotOption object.

##### **`TimeSlotOption(startTime, endTime)`**

### Creates a TimeSlotOption object with a start and end time.

Signature

```
   public TimeSlotOption(Datetime startTime, Datetime endTime)

```

Parameters

```
   startTime
```

Type: Datetime

Start time.

```
   endTime
```

Type: Datetime

End time.

##### **`TimeSlotOption(startTime, duration)`**

### Creates a TimeSlotOption object with a start time and a duration.


Apex Reference Guide TimeSlotOption Class

Signature

```
   public TimeSlotOption(Datetime startTime, Integer duration)

```

Parameters

```
   startTime
```

Type: Datetime

Start time.

##### _`duration`_

Type: Integer

Duration in seconds.

##### **`TimeSlotOption()`** Creates a TimeSlotOption object.

Signature

```
   public TimeSlotOption()

#### TimeSlotOption Properties

##### The following are properties for TimeSlotOption .

```

IN THIS SECTION:

##### duration

The duration in seconds.

##### durationValue

The duration in seconds. Enabled for Lightning components.

endTimeValue
The end time. Enabled for Lightning components.

startTime
The start time.

startTimeValue
The start time. Enabled for Lightning components.

##### **`duration`**

The duration in seconds.

Signature

```
   public Integer duration {get; set;}

```


Apex Reference Guide TimeSlotOption Class

Property Value

Type: Integer

##### **`durationValue`**

The duration in seconds. Enabled for Lightning components.

Signature

```
   public Integer durationValue {get; set;}

```

Property Value

Type: Integer

##### **`endTimeValue`**

The end time. Enabled for Lightning components.

Signature

```
   public Datetime endTimeValue {get; set;}

```

Property Value

Type: Datetime

##### **`startTime`**

The start time.

Signature

```
   public Datetime startTime {get; set;}

```

Property Value

Type: Datetime

##### **`startTimeValue`**

The start time. Enabled for Lightning components.

Signature

```
   public Datetime startTimeValue {get; set;}

```

Property Value

Type: Datetime


### Apex Reference Guide TimingIntervalUnit Enum TimingIntervalUnit Enum

Represents an enumerated type that describes the timing interval.

Enum Values

The following are the values of the `RichMessaging.TimingIntervalUnit` enum.

**Value** **Description**

`Day` Day interval.

`Hour` Hour interval.

`Minute` Minute interval.

`Month` Month interval.

`Year` Year interval.

### TimingType Enum

Represents an enumerated type that describes the type of timing.

Enum Values

The following are the values of the `RichMessaging.TimingType` enum.

**Value** **Description**

`DeferredTiming` Indicates that the timing is deferred. See DeferredTiming Class.

`RecurringTiming` Indicates that the timing recurs. See RecurringTiming Class.

## RulesAppln Namespace

The RulesAppln namespace contains output classes that store details about a rules-based application of payments and credits.

[The rules are applied by using the applyPaymentsAndCreditsByRules invocable action. See Apply Payments and Credits by Rules Action](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_apply_rules.htm)
in the _Revenue Cloud Developer Guide_ .

## The RulesAppln namespace includes these classes.

**•** [RulesApplicationResponse Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationResponse.htm)

**•** [RulesApplicationSummaryResponse Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationSummaryResponse.htm)

**•** [RulesApplicationErrorResponse Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationErrorResponse.htm)


## Apex Reference Guide runtime_industries_cpq Namespace runtime_industries_cpq Namespace

The runtime_industries_cpq namespace provides classes and methods to search products or to manage products, catalogs, and
categories.

[See runtime_industries_cpq namespace for more information about the available classes and methods.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_runtime_industries_cpq.htm)

## runtime_industries_insurance Namespace The runtime_industries_insurance namespace provides options classes for insurance operations, such as creating and

updating insurance quotes, generating insurance clauses, and running insurance rating.

## The runtime_industries_insurance namespace includes these classes.

**•** [AddEligibleInsuranceClausesOptions](https://developer.salesforce.com/docs/atlas.en-us.262.0.insurance_developer_guide.meta/insurance_developer_guide/apex_class_runtime_industries_insurance_AddEligibleInsuranceClausesOptions.htm)

**•** [CreateInsuranceQuoteOptions](https://developer.salesforce.com/docs/atlas.en-us.262.0.insurance_developer_guide.meta/insurance_developer_guide/apex_class_runtime_industries_insurance_CreateInsuranceQuoteOptions.htm)

**•** [CreateInsuranceRatingOptions](https://developer.salesforce.com/docs/atlas.en-us.262.0.insurance_developer_guide.meta/insurance_developer_guide/apex_class_runtime_industries_insurance_CreateInsuranceRatingOptions.htm)

**•** [GenerateInsuranceClausesOptions](https://developer.salesforce.com/docs/atlas.en-us.262.0.insurance_developer_guide.meta/insurance_developer_guide/apex_class_runtime_industries_insurance_GenerateInsuranceClauseOptions.htm)

**•** [UpdateInsuranceQuoteOptions](https://developer.salesforce.com/docs/atlas.en-us.262.0.insurance_developer_guide.meta/insurance_developer_guide/apex_class_runtime_industries_insurance_UpdateInsuranceQuoteOptions.htm)

## Schema Namespace The Schema namespace provides classes and methods for schema metadata information. The following are the classes in the Schema namespace.

IN THIS SECTION:

ChildRelationship Class
Contains methods for accessing the child relationship as well as the child sObject for a parent sObject.

DataCategory Class
Represents the categories within a category group.

DataCategoryGroupSobjectTypePair Class
Specifies a category group and an associated object.

DescribeColorResult Class
Contains color metadata information for a tab.

DescribeDataCategoryGroupResult Class
Contains the list of the category groups associated with KnowledgeArticleVersion and Question.

DescribeDataCategoryGroupStructureResult Class
Contains the category groups and categories associated with KnowledgeArticleVersion and Question.

DescribeFieldResult Class
Contains methods for describing sObject fields.

DescribeIconResult Class
Contains icon metadata information for a tab.


### Apex Reference Guide ChildRelationship Class

DescribeSObjectResult Class
Contains methods for describing SObjects. None of the methods take an argument.

DescribeTabResult Class
Contains tab metadata information for a tab in a standard or custom app available in the Salesforce user interface.

DescribeTabSetResult Class
Contains metadata information about a Salesforce Classic standard or custom app available in the Salesforce user interface.

DisplayType Enum
A `Schema.DisplayType` enum value is returned by the field describe result's `getType` method.

FieldDescribeOptions Enum
A `Schema.FieldDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

FieldSet Class
Contains methods for discovering and retrieving the details of field sets created on sObjects.

FieldSetMember Class
Contains methods for accessing the metadata for field set member fields.

PicklistEntry Class
Represents a picklist entry.

RecordTypeInfo Class
Contains methods for accessing record type information for an sObject with associated record types.

SOAPType Enum
A `Schema.SOAPType` enum value is returned by the field describe result `getSoapType` method.

SObjectDescribeOptions Enum
A `Schema.SObjectDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

SObjectField Class
A `Schema.sObjectField` object is returned from the field describe result using the `getController` and
`getSObjectField` methods.

SObjectType Class
A `Schema.sObjectType` object is returned from the field describe result using the `getReferenceTo` method, or from
the sObject describe result using the `getSObjectType` method.

### ChildRelationship Class

Contains methods for accessing the child relationship as well as the child sObject for a parent sObject.

Namespace

Schema

Example

A ChildRelationship object is returned from the sObject describe result using the `getChildRelationship` method. For example:

```
   Schema.DescribeSObjectResult R = Account.SObjectType.getDescribe();

   List<Schema.ChildRelationship> C = R.getChildRelationships();

```


Apex Reference Guide ChildRelationship Class

#### ChildRelationship Methods The following are methods for ChildRelationship . All are instance methods.

IN THIS SECTION:

##### getChildSObject()

Returns the token of the child sObject on which there is a foreign key back to the parent sObject.

##### getField()

Returns the token of the field that has a foreign key back to the parent sObject.

##### getRelationshipName()

Returns the name of the relationship.

isCascadeDelete()
Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

isDeprecatedAndHidden()
Reserved for future use.

isRestrictedDelete()
Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

##### getChildSObject()

Returns the token of the child sObject on which there is a foreign key back to the parent sObject.

Signature

```
   public Schema.SObjectType getChildSObject()

```

Return Value

Type: Schema.SObjectType

##### getField()

Returns the token of the field that has a foreign key back to the parent sObject.

Signature

```
   public Schema.SObjectField getField()

```

Return Value

Type: Schema.SObjectField

##### getRelationshipName()

Returns the name of the relationship.


### Apex Reference Guide DataCategory Class

Signature

```
   public String getRelationshipName()

```

Return Value

Type: String

##### isCascadeDelete()

Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

Signature

```
   public Boolean isCascadeDelete()

```

Return Value

Type: Boolean

##### isDeprecatedAndHidden()

Reserved for future use.

Signature

```
   public Boolean isDeprecatedAndHidden()

```

Return Value

Type: Boolean

##### isRestrictedDelete()

Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

Signature

```
   public Boolean isRestrictedDelete()

```

Return Value

Type: Boolean

### DataCategory Class

Represents the categories within a category group.

Namespace

Schema


Apex Reference Guide DataCategory Class

Usage

The `Schema.DataCategory` object is returned by the `getTopCategories` method.

#### DataCategory Methods The following are methods for DataCategory . All are instance methods.

IN THIS SECTION:

##### getChildCategories()

Returns a recursive object that contains the visible sub categories in the data category.

##### getLabel()

Returns the label for the data category used in the Salesforce user interface.

##### getName()

Returns the unique name used by the API to access to the data category.

##### getChildCategories()

Returns a recursive object that contains the visible sub categories in the data category.

Signature

```
   public Schema.DataCategory getChildCategories()

```

Return Value

Type: List<Schema.DataCategory>

##### getLabel()

Returns the label for the data category used in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique name used by the API to access to the data category.

Signature

```
   public String getName()

```


### Apex Reference Guide DataCategoryGroupSobjectTypePair Class

Return Value

Type: String

### DataCategoryGroupSobjectTypePair Class

Specifies a category group and an associated object.

Namespace

Schema

Usage

Schema.DataCategoryGroupSobjectTypePair is used by the `describeDataCategory GroupStructures` method to return
the categories available to this object.

IN THIS SECTION:

#### DataCategoryGroupSobjectTypePair Constructors DataCategoryGroupSobjectTypePair Methods DataCategoryGroupSobjectTypePair Constructors

### The following are constructors for DataCategoryGroupSobjectTypePair .

IN THIS SECTION:

##### DataCategoryGroupSobjectTypePair()

Creates a new instance of the `Schema.DataCategoryGroupSobjectTypePair` class.

##### DataCategoryGroupSobjectTypePair()

Creates a new instance of the `Schema.DataCategoryGroupSobjectTypePair` class.

Signature

```
   public DataCategoryGroupSobjectTypePair()

#### DataCategoryGroupSobjectTypePair Methods

### The following are methods for DataCategoryGroupSobjectTypePair . All are instance methods.

```

IN THIS SECTION:

getDataCategoryGroupName()
Returns the unique name used by the API to access the data category group.

getSobject()
Returns the object name associated with the data category group.


Apex Reference Guide DataCategoryGroupSobjectTypePair Class

##### setDataCategoryGroupName(name)

Specifies the unique name used by the API to access the data category group.

##### setSobject(sObjectName)

Sets the sObject associated with the data category group.

##### getDataCategoryGroupName()

Returns the unique name used by the API to access the data category group.

Signature

```
   public String getDataCategoryGroupName()

```

Return Value

Type: String

##### getSobject()

Returns the object name associated with the data category group.

Signature

```
   public String getSobject()

```

Return Value

Type: String

##### setDataCategoryGroupName(name)

Specifies the unique name used by the API to access the data category group.

Signature

```
   public String setDataCategoryGroupName(String name)

```

Parameters

**name**
Type: String

Return Value

Type: Void

##### setSobject(sObjectName)

Sets the sObject associated with the data category group.


### Apex Reference Guide DescribeColorResult Class

Signature

```
   public Void setSobject(String sObjectName)

```

Parameters

```
   sObjectName
```

Type: String

The _`sObjectName`_ is the object name associated with the data category group. Valid values are:

**•** `KnowledgeArticleVersion` —for article types.

**•** `Question` —for questions from Answers.

Return Value

Type: Void

### DescribeColorResult Class

Contains color metadata information for a tab.

Namespace

Schema

Usage

The `getColors` method of the `Schema.DescribeTabResult` class returns a list of `Schema.DescribeColorResult`
objects that describe colors used in a tab.

The methods in the `Schema.DescribeColorResult` class can be called using their property counterparts. For each method
starting with `get`, you can omit the `get` prefix and the ending parentheses `()` to call the property counterpart. For example,
`colorResultObj.color` is equivalent to `colorResultObj.getColor()` .

Example

This sample shows how to get the color information in the Sales app for the first tab’s first color.

```
   // Get tab set describes for each app

   List<Schema.DescribeTabSetResult> tabSetDesc = Schema.DescribeTabs();

   // Iterate through each tab set describe for each app and display the info

   for(Schema.DescribeTabSetResult tsr : tabSetDesc) {

      // Display tab info for the Sales app

      if (tsr.getLabel() == 'Sales') {

        // Get color information for the first tab

        List<Schema.DescribeColorResult> colorDesc = tsr.getTabs()[0].getColors();

        // Display the icon color, theme, and context of the first color returned

        System.debug('Color: ' + colorDesc[0].getColor());

        System.debug('Theme: ' + colorDesc[0].getTheme());

        System.debug('Context: ' + colorDesc[0].getContext());

      }

```


Apex Reference Guide DescribeColorResult Class

```
   }

   // Example debug statement output

   // DEBUG|Color: 1797C0

   // DEBUG|Theme: theme4

   // DEBUG|Context: primary

#### DescribeColorResult Methods The following are methods for DescribeColorResult . All are instance methods.

```

IN THIS SECTION:

##### getColor()

Returns the Web RGB color code, such as `00FF00` .

##### getContext()

Returns the color context. The context determines whether the color is the main color for the tab or not.

##### getTheme()

Returns the color theme.

##### getColor()

Returns the Web RGB color code, such as `00FF00` .

Signature

```
   public String getColor()

```

Return Value

Type: String

##### getContext()

Returns the color context. The context determines whether the color is the main color for the tab or not.

Signature

```
   public String getContext()

```

Return Value

Type: String

##### getTheme()

Returns the color theme.


Apex Reference Guide DescribeDataCategoryGroupResult Class

Signature

```
   public String getTheme()

```

Return Value

Type: String

Possible theme values include `theme3`, `theme4`, and `custom` .

**•** `theme3` is the Salesforce theme introduced during Spring ‘10.

**•** `theme4` is the Salesforce theme introduced in Winter ‘14 for the mobile touchscreen version of Salesforce.

**•** `custom` is the theme name associated with a custom icon.

DescribeDataCategoryGroupResult Class

Contains the list of the category groups associated with KnowledgeArticleVersion and Question.

Namespace

Schema

Usage

The `describeDataCategoryGroups` method returns a `Schema.DescribeDataCategoryGroupResult` object
containing the list of the category groups associated with the specified object.

For additional information and code examples using `describeDataCategoryGroups` [, see Accessing All Data Categories](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)
[Associated with an sObject.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)

Example

The following is an example of how to instantiate a data category group describe result object:

```
   List <String> objType = new List<String>();

   objType.add('KnowledgeArticleVersion');

   objType.add('Question');

   List<Schema.DescribeDataCategoryGroupResult> describeCategoryResult =

     Schema.describeDataCategoryGroups(objType);

#### DescribeDataCategoryGroupResult Methods The following are methods for DescribeDataCategoryGroupResult . All are instance methods.

```

IN THIS SECTION:

getCategoryCount()
Returns the number of visible data categories in the data category group.

getDescription()
Returns the description of the data category group.


Apex Reference Guide DescribeDataCategoryGroupResult Class

##### getLabel()

Returns the label for the data category group used in the Salesforce user interface.

##### getName()

Returns the unique name used by the API to access to the data category group.

getSobject()
Returns the object name associated with the data category group.

##### getCategoryCount()

Returns the number of visible data categories in the data category group.

Signature

```
   public Integer getCategoryCount()

```

Return Value

Type: Integer

##### getDescription()

Returns the description of the data category group.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getLabel()

Returns the label for the data category group used in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique name used by the API to access to the data category group.

Signature

```
   public String getName()

```


Apex Reference Guide DescribeDataCategoryGroupStructureResult Class

Return Value

Type: String

##### getSobject()

Returns the object name associated with the data category group.

Signature

```
   public String getSobject()

```

Return Value

Type: String

DescribeDataCategoryGroupStructureResult Class

Contains the category groups and categories associated with KnowledgeArticleVersion and Question.

Namespace

Schema

Usage

The `describeDataCategoryGroupStructures` method returns a list of `Schema.Describe`
`DataCategoryGroupStructureResult` objects containing the category groups and categories associated with the specified
object.

[For additional information and code examples, see Accessing All Data Categories Associated with an sObject.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)

Example

The following is an example of how to instantiate a data category group structure describe result object:

```
   List <DataCategoryGroupSobjectTypePair> pairs =

       new List<DataCategoryGroupSobjectTypePair>();

   DataCategoryGroupSobjectTypePair pair1 =

       new DataCategoryGroupSobjectTypePair();

   pair1.setSobject('KnowledgeArticleVersion');

   pair1.setDataCategoryGroupName('Regions');

   DataCategoryGroupSobjectTypePair pair2 =

       new DataCategoryGroupSobjectTypePair();

   pair2.setSobject('Questions');

   pair2.setDataCategoryGroupName('Regions');

   pairs.add(pair1);

   pairs.add(pair2);

```


Apex Reference Guide DescribeDataCategoryGroupStructureResult Class

```
   List<Schema.DescribeDataCategoryGroupStructureResult>results =

       Schema.describeDataCategoryGroupStructures(pairs, true);

#### DescribeDataCategoryGroupStructureResult Methods The following are methods for DescribeDataCategoryGroupStructureResult . All are instance methods.

```

IN THIS SECTION:

##### getDescription()

Returns the description of the data category group.

##### getLabel()

Returns the label for the data category group used in the Salesforce user interface.

##### getName()

Returns the unique name used by the API to access to the data category group.

getSobject()
Returns the name of object associated with the data category group.

getTopCategories()
Returns a `Schema.DataCategory` object, that contains the top categories visible depending on the user's data category group
visibility settings.

##### getDescription()

Returns the description of the data category group.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getLabel()

Returns the label for the data category group used in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique name used by the API to access to the data category group.


### Apex Reference Guide DescribeFieldResult Class

Signature

```
   public String getName()

```

Return Value

Type: String

##### getSobject()

Returns the name of object associated with the data category group.

Signature

```
   public String getSobject()

```

Return Value

Type: String

##### getTopCategories()

Returns a `Schema.DataCategory` object, that contains the top categories visible depending on the user's data category group
visibility settings.

Signature

```
   public List<Schema.DataCategory> getTopCategories()

```

Return Value

Type: List<Schema.DataCategory>

Usage

For more information on data category group visibility, see “Data Category Visibility” in the Salesforce online help.

### DescribeFieldResult Class

Contains methods for describing sObject fields.

Namespace

Schema

Usage

### Instances of field describe results on the same DescribeFieldResult aren’t guaranteed to be equal because the state and

behavior of a describe object is determined by various factors including the API version used. To compare describe results, call the


Apex Reference Guide DescribeFieldResult Class

`getSObjectField()` method on the field describe results and use the equality operator ( `==` ) to compare the `SObjectField`
values.

Example

The following is an example of how to instantiate a field describe result object:

```
   Schema.DescribeFieldResult dfr = Account.Description.getDescribe();

#### DescribeFieldResult Methods The following are methods for DescribeFieldResult . All are instance methods.

```

IN THIS SECTION:

getByteLength()
For variable-length fields (including binary fields), returns the maximum size of the field, in bytes.

getCalculatedFormula()
Returns the formula specified for this field.

getController()
Returns the token of the controlling field.

getDefaultValue()
Returns the default value for this field.

getDefaultValueFormula()
Returns the default formula value that is specified for this formula field.

getDigits()
Returns the maximum number of digits specified for the field. This method is only valid with Integer fields.

getInlineHelpText()
Returns the content of the field-level help.

getLabel()
Returns the text label that is displayed next to the field in the Salesforce user interface. This label can be localized.

getLength()
Returns the maximum size of the field for the DescribeFieldResult object in Unicode characters (not bytes).

getLocalName()
Returns the name of the field, similar to the `getName` method. However, if the field is part of the current namespace, the namespace
portion of the name is omitted.

getName()
Returns the field name used in Apex.

getPicklistValues()
Returns a list of active PicklistEntry objects. A runtime error is returned if the field isn’t a picklist. Only active picklist values are returned.

getPrecision()
For fields of type Double, returns the maximum number of digits that can be stored, including all numbers to the left and to the
right of the decimal point (but excluding the decimal point character).


Apex Reference Guide DescribeFieldResult Class

getReferenceTargetField()
Returns the name of the custom field on the parent standard or custom object whose values are matched against the values of the
child external object's indirect lookup relationship field. The match is done to determine which records are related to each other.

getReferenceTo()
Returns a list of Schema.sObjectType objects for the parent objects of this field. If the `isNamePointing` method returns `true`,
there is more than one entry in the list, otherwise there is only one.

getRelationshipName()
Returns the name of the child-to-parent relationship.

getRelationshipOrder()
Returns 0 if the field is the primary relationship field or 1 if the field is the secondary relationship field.

getScale()
For fields of type Double, returns the number of digits to the right of the decimal point.

getSOAPType()
Returns one of the SoapType enum values, depending on the type of field.

getSObjectField()
Returns the token for this field.

getSObjectType()
Returns the Salesforce object type from which this field originates.

getType()
Returns one of the DisplayType enum values, depending on the type of field.

isAccessible()
Returns `true` if the current user can see this field, `false` otherwise.

isAiPredictionField() (Beta)
Returns `true` if the current field is enabled to display Einstein prediction data, `false` otherwise.

isAutoNumber()
Returns `true` if the field is an Auto Number field, `false` otherwise.

isCalculated()
Returns `true` if the field is a custom formula field, `false` otherwise. Note that custom formula fields are always read-only.

isCascadeDelete()
Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

isCaseSensitive()
Returns `true` if the field is case sensitive, `false` otherwise.

isCreateable()
Returns `true` if the field can be created by the current user, `false` otherwise.

isCustom()
Returns `true` if the field is a custom field, `false` if it is a standard field, such as `Name` .

isDefaultedOnCreate()
Returns `true` if the field receives a default value when created, `false` otherwise.

isDependentPicklist()
Returns `true` if the picklist is a dependent picklist, `false` otherwise.


Apex Reference Guide DescribeFieldResult Class

isDeprecatedAndHidden()
Reserved for future use.

isEncrypted()
Returns `true` if the field is encrypted with Shield Platform Encryption, `false` otherwise.

isExternalID()
Returns `true` if the field is used as an external ID, `false` otherwise.

isFilterable()
Returns `true` if the field can be used as part of the filter criteria of a `WHERE` statement, `false` otherwise.

isFormulaTreatNullNumberAsZero()
Returns `true` if `null` is treated as zero in a formula field, `false` otherwise.

isGroupable()
Returns `true` if the field can be included in the `GROUP BY` clause of a SOQL query, `false` otherwise. This method is only
available for Apex classes and triggers saved using API version 18.0 and higher.

isHtmlFormatted()
Returns `true` if the field has been formatted for HTML and should be encoded for display in HTML, `false` otherwise. One example
of a field that returns `true` for this method is a hyperlink custom formula field. Another example is a custom formula field that has
an `IMAGE` text function.

isIdLookup()
Returns `true` if the field can be used to specify a record in an `upsert` method, `false` otherwise.

isNameField()
Returns `true` if the field is a name field, `false` otherwise.

isNamePointing()
Returns `true` if the field can have multiple types of objects as parents. For example, a task can have both the `Contact/Lead`
`ID` ( `WhoId` ) field and the `Opportunity/Account ID` ( `WhatId` ) field return `true` for this method. because either of
those objects can be the parent of a particular task record. This method returns `false` otherwise.

isNillable()
Returns `true` if the field is nillable, `false` otherwise. A nillable field can have empty content. A non-nillable field must have a
value for the object to be created or saved.

isPermissionable()
Returns `true` if field permissions can be specified for the field, `false` otherwise.

isRestrictedDelete()
Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

isRestrictedPicklist()
Returns `true` if the field is a restricted picklist, `false` otherwise

isSearchPrefilterable()
Returns `true` if a foreign key can be included in prefiltering when used in a SOSL `WHERE` clause, `false` otherwise.

isSortable()
Returns `true` if a query can sort on the field, `false` otherwise

isUnique()
Returns `true` if the value for the field must be unique, `false` otherwise


Apex Reference Guide DescribeFieldResult Class

isUpdateable()
Returns `true` if the field can be edited by the current user, or child records in a master-detail relationship field on a custom object
can be reparented to different parent records; `false` otherwise.

isWriteRequiresMasterRead()
Returns `true` if writing to the detail object requires read sharing instead of read/write sharing of the parent.

##### getByteLength()

For variable-length fields (including binary fields), returns the maximum size of the field, in bytes.

Signature

```
   public Integer getByteLength()

```

Return Value

Type: Integer

##### getCalculatedFormula()

Returns the formula specified for this field.

Signature

```
   public String getCalculatedFormula()

```

Return Value

Type: String

##### getController()

Returns the token of the controlling field.

Signature

```
   public Schema.sObjectField getController()

```

Return Value

Type: Schema.SObjectField

##### getDefaultValue()

Returns the default value for this field.

Signature

```
   public Object getDefaultValue()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Object

##### getDefaultValueFormula()

Returns the default formula value that is specified for this formula field.

Signature

```
   public String getDefaultValueFormula()

```

Return Value

Type: String

##### getDigits()

Returns the maximum number of digits specified for the field. This method is only valid with Integer fields.

Signature

```
   public Integer getDigits()

```

Return Value

Type: Integer

##### getInlineHelpText()

Returns the content of the field-level help.

Signature

```
   public String getInlineHelpText()

```

Return Value

Type: String

Usage

For more information, see “Define Field-Level Help” in the Salesforce online help.

##### getLabel()

Returns the text label that is displayed next to the field in the Salesforce user interface. This label can be localized.

Signature

```
   public String getLabel()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: String

Usage

Note: For the Type field on standard objects, `getLabel` returns a label different from the default label. It returns a label of the
form _`Object`_ `Type`, where _Object_ is the standard object label. For example, for the Type field on Account, `getLabel` returns

`Account Type` instead of the default label `Type` . If the Type label is renamed, `getLabel` returns the new label. You can
check or change the labels of all standard object fields from Setup by entering _`Rename Tabs and Labels`_ in the `Quick`
`Find box`, then selecting **Rename Tabs and Labels** .

##### getLength()

Returns the maximum size of the field for the DescribeFieldResult object in Unicode characters (not bytes).

Signature

```
   public Integer getLength()

```

Return Value

Type: Integer

##### getLocalName() Returns the name of the field, similar to the getName method. However, if the field is part of the current namespace, the namespace

portion of the name is omitted.

Signature

```
   public String getLocalName()

```

Return Value

Type: String

##### getName()

Returns the field name used in Apex.

Signature

```
   public String getName()

```

Return Value

Type: String


Apex Reference Guide DescribeFieldResult Class

##### getPicklistValues()

Returns a list of active PicklistEntry objects. A runtime error is returned if the field isn’t a picklist. Only active picklist values are returned.

Signature

```
   public List<Schema.PicklistEntry> getPicklistValues()

```

Return Value

Type: List<Schema.PicklistEntry>

##### getPrecision()

For fields of type Double, returns the maximum number of digits that can be stored, including all numbers to the left and to the right
of the decimal point (but excluding the decimal point character).

Signature

```
   public Integer getPrecision()

```

Return Value

Type: Integer

##### getReferenceTargetField()

Returns the name of the custom field on the parent standard or custom object whose values are matched against the values of the child
external object's indirect lookup relationship field. The match is done to determine which records are related to each other.

Signature

```
   public String getReferenceTargetField()

```

Return Value

Type: String

Usage

For information about indirect lookup relationships, see “Indirect Lookup Relationship Fields on External Objects” in the Salesforce Help.

##### getReferenceTo()

Returns a list of Schema.sObjectType objects for the parent objects of this field. If the `isNamePointing` method returns `true`,
there is more than one entry in the list, otherwise there is only one.

Signature

```
   public List <Schema.sObjectType> getReferenceTo()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: List<Schema.sObjectType>

Versioned Behavior Changes

In API version 51.0 and later, the `getReferenceTo()` method returns referenced objects that aren’t accessible to the context user.
If the context user has access to an object’s field that references another object, irrespective of the context user’s access to the
cross-referenced object, the method returns references. In API version 50.0 and earlier, if the context user doesn’t have access to the
cross-referenced object, the method returns an empty list.

##### getRelationshipName()

Returns the name of the child-to-parent relationship.

Signature

```
   public String getRelationshipName()

```

Return Value

Type: String

Usage

[For more information about relationships and relationship names, see Understanding Relationship Names in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_understanding.htm) _SOQL and SOSL Reference_ .

##### getRelationshipOrder()

Returns 0 if the field is the primary relationship field or 1 if the field is the secondary relationship field.

Signature

```
   public Integer getRelationshipOrder()

```

Return Value

Type: Integer

Usage

[For more information about primary and secondary relationships, see Considerations for Object Relationships. For more information](https://help.salesforce.com/s/articleView?id=sf.relationships_considerations.htm&language=en_US)
[about relationships and relationship names, see Understanding Relationship Names in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_understanding.htm) _SOQL and SOSL Reference_ .

##### getScale()

For fields of type Double, returns the number of digits to the right of the decimal point.

Signature

```
   public Integer getScale()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Integer

##### getSOAPType()

Returns one of the SoapType enum values, depending on the type of field.

Signature

```
   public Schema.SOAPType getSOAPType()

```

Return Value

Type: Schema.SOAPType

##### getSObjectField()

Returns the token for this field.

Signature

```
   public Schema.sObjectField getSObjectField()

```

Return Value

Type: Schema.SObjectField

##### **`getSObjectType()`**

Returns the Salesforce object type from which this field originates.

Signature

```
   public Schema.SObjectType getSObjectType()

```

Return Value

Type: Schema.SObjectType

Example

```
   Schema.DescribeFieldResult f = Account.Industry.getDescribe();

   Schema.sObjectType sourceType = f.getSObjectType();

   Assert.areEqual(Account.sObjectType, sourceType);

##### getType()

```

Returns one of the DisplayType enum values, depending on the type of field.


Apex Reference Guide DescribeFieldResult Class

Signature

```
   public Schema.DisplayType getType()

```

Return Value

Type: Schema.DisplayType

##### isAccessible()

Returns `true` if the current user can see this field, `false` otherwise.

Signature

```
   public Boolean isAccessible()

```

Return Value

Type: Boolean

##### isAiPredictionField() (Beta)

Returns `true` if the current field is enabled to display Einstein prediction data, `false` otherwise.

Signature

```
   public Boolean isAiPredictionField()

```

Return Value

Type: Boolean

Usage

Custom number fields can be set to display Einstein prediction values. If you are participating in the Einstein Prediction Builder Beta
program, use Einstein Prediction Builder to set up the value to display. Use this method to find out if a field is enabled to display an
Einstein prediction value.

##### isAutoNumber()

Returns `true` if the field is an Auto Number field, `false` otherwise.

Signature

```
   public Boolean isAutoNumber()

```

Return Value

Type: Boolean


Apex Reference Guide DescribeFieldResult Class

Usage

Analogous to a SQL IDENTITY type, Auto Number fields are read-only, non-createable text fields with a maximum length of 30 characters.
Auto Number fields are used to provide a unique ID that is independent of the internal object ID (such as a purchase order number or
invoice number). Auto Number fields are configured entirely in the Salesforce user interface.

##### isCalculated()

Returns `true` if the field is a custom formula field, `false` otherwise. Note that custom formula fields are always read-only.

Signature

```
   public Boolean isCalculated()

```

Return Value

Type: Boolean

##### isCascadeDelete()

Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

Signature

```
   public Boolean isCascadeDelete()

```

Return Value

Type: Boolean

##### isCaseSensitive()

Returns `true` if the field is case sensitive, `false` otherwise.

Signature

```
   public Boolean isCaseSensitive()

```

Return Value

Type: Boolean

##### isCreateable()

Returns `true` if the field can be created by the current user, `false` otherwise.

Signature

```
   public Boolean isCreateable()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Boolean

##### isCustom()

Returns `true` if the field is a custom field, `false` if it is a standard field, such as `Name` .

Signature

```
   public Boolean isCustom()

```

Return Value

Type: Boolean

##### isDefaultedOnCreate()

Returns `true` if the field receives a default value when created, `false` otherwise.

Signature

```
   public Boolean isDefaultedOnCreate()

```

Return Value

Type: Boolean

Usage

If this method returns `true`, Salesforce implicitly assigns a value for this field when the object is created, even if a value for this field is
not passed in on the create call. For example, in the Opportunity object, the Probability field has this attribute because its value is derived
from the Stage field. Similarly, the Owner has this attribute on most objects because its value is derived from the current user (if the
Owner field is not specified).

##### isDependentPicklist()

Returns `true` if the picklist is a dependent picklist, `false` otherwise.

Signature

```
   public Boolean isDependentPicklist()

```

Return Value

Type: Boolean

##### isDeprecatedAndHidden()

Reserved for future use.


Apex Reference Guide DescribeFieldResult Class

Signature

```
   public Boolean isDeprecatedAndHidden()

```

Return Value

Type: Boolean

##### isEncrypted()

Returns `true` if the field is encrypted with Shield Platform Encryption, `false` otherwise.

Signature

```
   public Boolean isEncrypted()

```

Return Value

Type: Boolean

##### isExternalID()

Returns `true` if the field is used as an external ID, `false` otherwise.

Signature

```
   public Boolean isExternalID()

```

Return Value

Type: Boolean

##### isFilterable()

Returns `true` if the field can be used as part of the filter criteria of a `WHERE` statement, `false` otherwise.

Signature

```
   public Boolean isFilterable()

```

Return Value

Type: Boolean

##### isFormulaTreatNullNumberAsZero()

Returns `true` if `null` is treated as zero in a formula field, `false` otherwise.

Signature

```
   public Boolean isFormulaTreatNullNumberAsZero()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Boolean

##### isGroupable()

Returns `true` if the field can be included in the `GROUP BY` clause of a SOQL query, `false` otherwise. This method is only available
for Apex classes and triggers saved using API version 18.0 and higher.

Signature

```
   public Boolean isGroupable()

```

Return Value

Type: Boolean

##### isHtmlFormatted()

Returns `true` if the field has been formatted for HTML and should be encoded for display in HTML, `false` otherwise. One example
of a field that returns `true` for this method is a hyperlink custom formula field. Another example is a custom formula field that has an
`IMAGE` text function.

Signature

```
   public Boolean isHtmlFormatted()

```

Return Value

Type: Boolean

##### isIdLookup()

Returns `true` if the field can be used to specify a record in an `upsert` method, `false` otherwise.

Signature

```
   public Boolean isIdLookup()

```

Return Value

Type: Boolean

##### isNameField()

Returns `true` if the field is a name field, `false` otherwise.

Signature

```
   public Boolean isNameField()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Boolean

Usage

This method is used to identify the name field for standard objects (such as `AccountName` for an Account object) and custom objects.
Objects can only have one name field, except where the `FirstName` and `LastName` fields are used instead (such as on the Contact
object).

If a compound name is present, for example, the `Name` field on a person account, `isNameField` is set to `true` for that record.

##### isNamePointing()

Returns `true` if the field can have multiple types of objects as parents. For example, a task can have both the `Contact/Lead ID`
( `WhoId` ) field and the `Opportunity/Account ID` ( `WhatId` ) field return `true` for this method. because either of those objects
can be the parent of a particular task record. This method returns `false` otherwise.

Signature

```
   public Boolean isNamePointing()

```

Return Value

Type: Boolean

##### isNillable()

Returns `true` if the field is nillable, `false` otherwise. A nillable field can have empty content. A non-nillable field must have a value
for the object to be created or saved.

Signature

```
   public Boolean isNillable()

```

Return Value

Type: Boolean

##### isPermissionable()

Returns `true` if field permissions can be specified for the field, `false` otherwise.

Signature

```
   public Boolean isPermissionable()

```

Return Value

Type: Boolean


Apex Reference Guide DescribeFieldResult Class

##### isRestrictedDelete()

Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

Signature

```
   public Boolean isRestrictedDelete()

```

Return Value

Type: Boolean

##### isRestrictedPicklist()

Returns `true` if the field is a restricted picklist, `false` otherwise

Signature

```
   public Boolean isRestrictedPicklist()

```

Return Value

Type: Boolean

##### isSearchPrefilterable()

Returns `true` if a foreign key can be included in prefiltering when used in a SOSL `WHERE` clause, `false` otherwise.

Signature

```
   public Boolean isSearchPrefilterable()

```

Return Value

Type: Boolean

Usage

_Prefiltering_ means to filter by a specific field value before executing the full search query. Prefiltering is supported only in `WHERE` clauses
with the equals ( `=` ) operator.

##### isSortable()

Returns `true` if a query can sort on the field, `false` otherwise

Signature

```
   public Boolean isSortable()

```


### Apex Reference Guide DescribeIconResult Class

Return Value

Type: Boolean

##### isUnique()

Returns `true` if the value for the field must be unique, `false` otherwise

Signature

```
   public Boolean isUnique()

```

Return Value

Type: Boolean

##### isUpdateable()

Returns `true` if the field can be edited by the current user, or child records in a master-detail relationship field on a custom object can
be reparented to different parent records; `false` otherwise.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Signature

```
   public Boolean isUpdateable()

```

Return Value

Type: Boolean

##### isWriteRequiresMasterRead()

Returns `true` if writing to the detail object requires read sharing instead of read/write sharing of the parent.

Signature

```
   public Boolean isWriteRequiresMasterRead()

```

Return Value

Type: Boolean

### DescribeIconResult Class

Contains icon metadata information for a tab.

Namespace

Schema


Apex Reference Guide DescribeIconResult Class

Usage

The `getIcons` method of the `Schema.DescribeTabResult` class returns a list of `Schema.DescribeIconResult`
objects that describe colors used in a tab.

The methods in the `Schema.DescribeIconResult` class can be called using their property counterparts. For each method
starting with `get`, you can omit the `get` prefix and the ending parentheses `()` to call the property counterpart. For example,
`iconResultObj.url` is equivalent to `iconResultObj.getUrl()` .

Example

This sample shows how to get the icon information in the Sales app for the first tab’s first icon.

```
   // Get tab set describes for each app

   List<Schema.DescribeTabSetResult> tabSetDesc = Schema.describeTabs();

   // Iterate through each tab set

   for(Schema.DescribeTabSetResult tsr : tabSetDesc) {

      // Get tab info for the Sales app

      if (tsr.getLabel() == 'Sales') {

        // Get icon information for the first tab

        List<Schema.DescribeIconResult> iconDesc = tsr.getTabs()[0].getIcons();

        // Display the icon height and width of the first icon

        System.debug('Height: ' + iconDesc[0].getHeight());

        System.debug('Width: ' + iconDesc[0].getWidth());

      }

   }

   // Example debug statement output

   // DEBUG|Height: 32

   // DEBUG|Width: 32

#### DescribeIconResult Methods The following are methods for DescribeIconResult . All are instance methods.

```

IN THIS SECTION:

getContentType()
Returns the tab icon’s content type, such as `image/png` .

getHeight()
Returns the tab icon’s height in pixels.

getTheme()
Returns the tab’s icon theme.

getUrl()
Returns the tab’s icon fully qualified URL.

getWidth()
Returns the tab’s icon width in pixels.


Apex Reference Guide DescribeIconResult Class

##### getContentType()

Returns the tab icon’s content type, such as `image/png` .

Signature

```
   public String getContentType()

```

Return Value

Type: String

##### getHeight()

Returns the tab icon’s height in pixels.

Signature

```
   public Integer getHeight()

```

Return Value

Type: Integer

Usage

Note: If the icon content type is SVG, the icon won’t have a size and its height is zero.

##### getTheme()

Returns the tab’s icon theme.

Signature

```
   public String getTheme()

```

Return Value

Type: String

Possible theme values include `theme3`, `theme4`, and `custom` .

**•** `theme3` is the Salesforce theme introduced during Spring ‘10.

**•** `theme4` is the Salesforce theme introduced in Winter ‘14 for the mobile touchscreen version of Salesforce.

**•** `custom` is the theme name associated with a custom icon.

##### getUrl()

Returns the tab’s icon fully qualified URL.


### Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public String getUrl()

```

Return Value

Type: String

##### getWidth()

Returns the tab’s icon width in pixels.

Signature

```
   public Integer getWidth()

```

Return Value

Type: Integer

Usage

Note: If the icon content type is SVG, the icon won’t have a size and its width is zero.

### DescribeSObjectResult Class

Contains methods for describing SObjects. None of the methods take an argument.

Namespace

Schema

Usage

### Instances of describe results on the same DescribeSObjectResult aren’t guaranteed to be equal because the state and behavior

of a describe object is determined by various factors including the API version used. To compare describe results, call the
`getSObjectType()` method on the SObject describe results and use the equality operator ( `==` ) to compare the `SObjectType`
values.

#### DescribeSObjectResult Properties

### The following are properties for DescribeSObjectResult .

##### **`accessible`**

Indicates whether the current user has access to the SObject.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Boolean accessible {get; set;}

```

Property Value

Type: Boolean

##### **`associateentitytype`**

The type of associated object. For example, `History` or `Share` .

Signature

```
   public String associateentitytype {get; set;}

```

Property Value

Type: String

##### **`associateparententity`**

The parent object of an associated object.

Signature

```
   public String associateparententity {get; set;}

```

Property Value

Type: String

##### **`childrelationships`**

A list of child relationships, which is the name of the sObject that has a foreign key to the sObject being described.

Signature

```
   public List<Schema.ChildRelationship> childrelationships {get; set;}

```

Property Value

Type: List<Schema.ChildRelationship on page 3460>

##### **`createable`**

Indicates whether the SObject can be created by the current user.

Signature

```
   public Boolean createable {get; set;}

```


Apex Reference Guide DescribeSObjectResult Class

Property Value

Type: Boolean

##### **`custom`**

Indicates whether the SObject is a custom object.

Signature

```
   public Boolean custom {get; set;}

```

Property Value

Type: Boolean

##### **`customsetting`**

Indicates whether the SObject is a custom setting.

Signature

```
   public Boolean customsetting {get; set;}

```

Property Value

Type: Boolean

##### **`datatranslationenabled`**

Indicates whether data translation is enabled for the SObject. This property is available in API version 49.0 and later.

Signature

```
   public Boolean datatranslationenabled {get; set;}

```

Property Value

Type: Boolean

##### **`defaultimplementation`**

Reserved for future use.

Signature

```
   public String defaultimplementation {get; set;}

```

Property Value

Type: String


Apex Reference Guide DescribeSObjectResult Class

##### **`deletable`**

Indicates whether the SObject can be deleted by the current user.

Signature

```
   public Boolean deletable {get; set;}

```

Property Value

Type: Boolean

##### **`deprecatedandhidden`**

Reserved for future use.

Signature

```
   public Boolean deprecatedandhidden {get; set;}

```

Property Value

Type: Boolean

##### **`feedenabled`**

Indicates whether Chatter feeds are enabled for the SObject.

Signature

```
   public Boolean feedenabled {get; set;}

```

Property Value

Type: Boolean

##### fields

A list of fields associated with the SObject.

Signature

```
   public Schema.SObjectTypeFields fields {get; set;}

```

Property Value

Type: Schema.SObjectTypeFields

##### Follow fields with the getMap method.


Apex Reference Guide DescribeSObjectResult Class

Example

This sample code shows how to use `fields` . To get a custom field, specify the custom field name.

```
   Schema.DescribeFieldResult dfr = Schema.SObjectType.Account.fields.Name;

##### fieldSets

```

Represents field sets, which is a grouping of the SObject fields.

Signature

```
   public Schema.SObjectTypeFieldSets fieldsets {get; set;}

```

Property Value

Type: Schema.SObjectTypeFieldSets

##### Follow fieldSets with a field set name or with the getMap method.

Example

##### This sample code shows how to use fieldSet .

```
   Schema.DescribeSObjectResult d =

     Account.sObjectType.getDescribe();

   Map<String, Schema.FieldSet> FsMap =

     d.fieldSets.getMap();

##### **`hassubtypes`**

```

Reserved for future use.

Signature

```
   public Boolean hassubtypes {get; set;}

```

Property Value

Type: Boolean

##### **`implementedby`**

Reserved for future use.

Signature

```
   public String implementedby {get; set;}

```

Property Value

Type: String


Apex Reference Guide DescribeSObjectResult Class

##### **`implementsinterfaces`**

Reserved for future use.

Signature

```
   public String implementsinterfaces {get; set;}

```

Property Value

Type: String

##### **`isinterface`**

Reserved for future use.

Signature

```
   public Boolean isinterface {get; set;}

```

Property Value

Type: Boolean

##### **`keyprefix`**

The three-character prefix code in the SObject ID.

Signature

```
   public String keyprefix {get; set;}

```

Property Value

Type: String

##### **`label`**

The SObject's label, which may or may not match the object name. For example, an organization representing a medical vertical might
rename Account to Patient. Tabs and fields can be renamed in the Salesforce user interface.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String


Apex Reference Guide DescribeSObjectResult Class

##### **`labelplural`**

The SObject's plural label, which may or may not match the object name. For example, Accounts.

Signature

```
   public String labelplural {get; set;}

```

Property Value

Type: String

##### **`localname`**

The name of the SObject. If the object is part of the current namespace, the namespace portion of the name is omitted.

Signature

```
   public String localname {get; set;}

```

Property Value

Type: String

##### **`mergeable`**

Indicates whether the SObject can be merged with other objects of its type by the current user. This is set to `true` for leads, contacts,
and accounts.

Signature

```
   public Boolean mergeable {get; set;}

```

Property Value

Type: Boolean

##### **`mruenabled`**

Indicates whether Most Recently Used (MRU) list functionality is enabled for the SObject.

Signature

```
   public Boolean mruenabled {get; set;}

```

Property Value

Type: Boolean


Apex Reference Guide DescribeSObjectResult Class

##### **`name`**

The name field of the SObject.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### **`queryable`**

Indicates whether the SObject can be queried by the current user.

Signature

```
   public Boolean queryable {get; set;}

```

Property Value

Type: Boolean

##### **`recordtypeinfos`**

A list of the record types supported by the SObject.

Signature

```
   public List<Schema.RecordTypeInfo> recordtypeinfos {get; set;}

```

Property Value

Type: List<Schema.RecordTypeInfo>

##### **`recordtypeinfosbydevelopername`**

A map that matches developer names to their associated record type.

Signature

```
   public Map<String,Schema.RecordTypeInfo> recordtypeinfosbydevelopername {get; set;}

```

Property Value

Type: Map<String, Schema.RecordTypeInfo>

##### **`recordtypeinfosbyid`**

A map that matches record IDs to their associated record types.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Map<Id,Schema.RecordTypeInfo> recordtypeinfosbyid {get; set;}

```

Property Value

Type: Map<ID, Schema.RecordTypeInfo>

##### **`recordtypeinfosbyname`**

A map that matches record labels to their associated record type.

Signature

```
   public Map<String,Schema.RecordTypeInfo> recordtypeinfosbyname {get; set;}

```

Property Value

Type: Map<String, Schema.RecordTypeInfo>

##### **`searchable`**

Indicates whether the SObject can be searched by the current user.

Signature

```
   public Boolean searchable {get; set;}

```

Property Value

Type: Boolean

##### **`sobjectdescribeoption`**

The effective describe option used by the system for the SObject.

Signature

```
   public Schema.SObjectDescribeOptions sobjectdescribeoption {get; set;}

```

Property Value

Type: SObjectDescribeOptions Enum

##### **`sobjecttype`**

The Schema.SObjectType object for the SObject.

Signature

```
   public Schema.SObjectType sobjecttype {get; set;}

```


Apex Reference Guide DescribeSObjectResult Class

Property Value

Type: Schema.SObjectType

##### **`undeletable`**

Indicates whether the SObject can be undeleted by the current user.

Signature

```
   public Boolean undeletable {get; set;}

```

Property Value

Type: Boolean

##### **`updateable`**

Indicates whether the SObject can be updated by the current user.

Signature

```
   public Boolean updateable {get; set;}

```

Property Value

Type: Boolean

#### DescribeSObjectResult Methods The following are methods for DescribeSObjectResult . All are instance methods.

IN THIS SECTION:

equals(obj)
Compares the SObject to the specified object and returns true if both are equal. Otherwise, returns false.

getAssociateEntityType()
Returns additional metadata for an associated object of a specified parent but only if it's a specific associated object type. Used in
combination with the `getAssociateParentEntity()` method to get the parent object. For example, invoking the method
on AccountHistory returns the parent object as `Account` and the type of associated object as `History` .

getAssociateParentEntity()
Returns additional metadata for an associated object but only if it's associated to a specific parent object. Used in combination with
the `getAssociateEntityType()` method to get the type of associated object. For example, invoking the method on
AccountHistory returns the parent object as `Account` and the type of associated object as `History` .

getChildRelationships()
Returns a list of child relationships, which are the names of the sObjects that have a foreign key to the sObject being described.

getDataTranslationEnabled()
Returns true if data translation is enabled for the SObject. Otherwise, returns false.


Apex Reference Guide DescribeSObjectResult Class

getDefaultImplementation()
Reserved for future use.

getFields()
Returns the fields that make up the SObject being described.

getFieldSets()
Returns field sets, which is a grouping of the SObject fields.

getHasSubtypes()
Reserved for future use.

getImplementedBy()
Reserved for future use.

getImplementsInterfaces()
Reserved for future use.

getIsInterface()
Reserved for future use.

getKeyPrefix()
Returns the three-character prefix code for the object. Record IDs are prefixed with three-character codes that specify the type of
the object (for example, accounts have a prefix of `001` and opportunities have a prefix of `006` ).

getLabel()
Returns the object's label, which may or may not match the object name.

getLabelPlural()
Returns the object's plural label, which may or may not match the object name.

getLocalName()
Returns the name of the object, similar to the `getName` method. However, if the object is part of the current namespace, the
namespace portion of the name is omitted.

getName()
Returns the name of the object.

getRecordTypeInfos()
Returns a list of the record types supported by this object. The current user is not required to have access to a record type to see it
in this list.

getRecordTypeInfosByDeveloperName()
Returns a map that matches developer names to their associated record type. The current user is not required to have access to a
record type to see it in this map.

getRecordTypeInfosById()
Returns a map that matches record IDs to their associated record types. The current user is not required to have access to a record
type to see it in this map.

getRecordTypeInfosByName()
Returns a map that matches record labels to their associated record type. The current user is not required to have access to a record
type to see it in this map.

getSObjectDescribeOption()
Returns the effective describe option used by the system for the SObject.


Apex Reference Guide DescribeSObjectResult Class

getSobjectType()
Returns the Schema.SObjectType object for the sObject. You can use this to create a similar sObject.

getHasSubtypes()
Reserved for future use.

hashCode()
Returns the hash code for the SObject.

isAccessible()
Returns `true` if the current user can see this object, `false` otherwise.

isCreateable()
Returns `true` if the object can be created by the current user, `false` otherwise.

isCustom()
Returns `true` if the object is a custom object, `false` if it is a standard object.

isCustomSetting()
Returns `true` if the object is a custom setting, `false` otherwise.

isDeletable()
Returns `true` if the object can be deleted by the current user, `false` otherwise.

isDeprecatedAndHidden()
Reserved for future use.

isFeedEnabled()
Returns `true` if Chatter feeds are enabled for the object, `false` otherwise. This method is only available for Apex classes and
triggers saved using SalesforceAPI version 19.0 and later.

isMergeable()
Returns `true` if the object can be merged with other objects of its type by the current user, `false` otherwise. `true` is returned
for leads, contacts, and accounts.

isMruEnabled()
Returns `true` if Most Recently Used (MRU) list functionality is enabled for the object, `false` otherwise.

isQueryable()
Returns `true` if the object can be queried by the current user, `false` otherwise

isSearchable()
Returns `true` if the object can be searched by the current user, `false` otherwise.

isUndeletable()
Returns `true` if the object can be undeleted by the current user, `false` otherwise.

isUpdateable()
Returns `true` if the object can be updated by the current user, `false` otherwise.

toString()
Returns a string that represents the SObject.

##### **`equals(obj)`**

Compares the SObject to the specified object and returns true if both are equal. Otherwise, returns false.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

The object with which to compare.

Return Value

Type: Boolean

##### **`getAssociateEntityType()`**

Returns additional metadata for an associated object of a specified parent but only if it's a specific associated object type. Used in
##### combination with the getAssociateParentEntity() method to get the parent object. For example, invoking the method

on AccountHistory returns the parent object as `Account` and the type of associated object as `History` .

Signature

```
   public String associateentitytype {get; set;}

```

Return Value

Type: String

SEE ALSO:

DescribeSObjectResult Properties

##### **`getAssociateParentEntity()`**

Returns additional metadata for an associated object but only if it's associated to a specific parent object. Used in combination with the
##### getAssociateEntityType() method to get the type of associated object. For example, invoking the method on AccountHistory

returns the parent object as `Account` and the type of associated object as `History` .

Signature

```
   public String getAssociateParentEntity()

```

Return Value

Type: String

SEE ALSO:

DescribeSObjectResult Properties


Apex Reference Guide DescribeSObjectResult Class

##### getChildRelationships()

Returns a list of child relationships, which are the names of the sObjects that have a foreign key to the sObject being described.

Signature

```
   public Schema.ChildRelationship getChildRelationships()

```

Return Value

Type: List<Schema.ChildRelationship>

Example

For example, the Account object includes `Contacts` and `Opportunities` as child relationships.

##### **`getDataTranslationEnabled()`**

Returns true if data translation is enabled for the SObject. Otherwise, returns false.

Signature

```
   public Boolean getDataTranslationEnabled()

```

Return Value

Type: Boolean

##### getDefaultImplementation()

Reserved for future use.

Signature

```
   public String getDefaultImplementation()

```

Return Value

Type: String

##### **`getFields()`**

Returns the fields that make up the SObject being described.

Signature

```
   public Schema.SObjectTypeFields getFields()

```

Return Value

Type: Schema.SObjectTypeFields


Apex Reference Guide DescribeSObjectResult Class

The return value is a special data type. Call the `getMap()` method to get a map of Strings and SObjectFields.

Usage

When you describe SObjects and their fields from within an Apex class, custom fields of new field types are returned regardless of the
API version that the class is saved in. If a field type, such as the geolocation field type, is available only in a recent API version, components
of a geolocation field are returned even if the class is saved in an earlier API version.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_field_tokens.htm)_ : Using Field Tokens

_Apex Developer Guide_ [: Describing sObjects Using Schema Method](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_describeSObject.htm)

_Apex Developer Guide_ [: Understanding Apex Describe Information](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

##### **`getFieldSets()`**

Returns field sets, which is a grouping of the SObject fields.

Signature

```
   public Schema.SObjectTypeFieldSets getFieldSets()

```

Return Value

Type: Schema.SObjectTypeFieldSets

The return value is a special data type. Call the `getMap()` method to get a map of Strings and SObjectFieldSets.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_field_tokens.htm)_ : Using Field Tokens

_Apex Developer Guide_ [: Describing sObjects Using Schema Method](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_describeSObject.htm)

_Apex Developer Guide_ [: Understanding Apex Describe Information](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

##### getHasSubtypes()

Reserved for future use.

To check if Person Accounts are enabled for the current org, use this code snippet:

```
   Schema.SObjectType.Account.fields.getMap().containsKey( 'isPersonAccount' );

```

Signature

```
   public Boolean getHasSubtypes()

```

Return Value

Type: Boolean


Apex Reference Guide DescribeSObjectResult Class

##### getImplementedBy()

Reserved for future use.

Signature

```
   public String getImplementedBy()

```

Return Value

Type: String

##### getImplementsInterfaces()

Reserved for future use.

Signature

```
   public String getImplementsInterfaces()

```

Return Value

Type: String

##### getIsInterface()

Reserved for future use.

Signature

```
   public Boolean getIsInterface()

```

Return Value

Type: Boolean

##### getKeyPrefix()

Returns the three-character prefix code for the object. Record IDs are prefixed with three-character codes that specify the type of the
object (for example, accounts have a prefix of `001` and opportunities have a prefix of `006` ).

Signature

```
   public String getKeyPrefix()

```

Return Value

Type: String


Apex Reference Guide DescribeSObjectResult Class

Usage

The DescribeSobjectResult object returns a value for objects that have a stable prefix. For object types that do not have a stable or
predictable prefix, this field is blank. Client applications that rely on these codes can use this way of determining object type to ensure
forward compatibility.

##### getLabel()

Returns the object's label, which may or may not match the object name.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Usage

The object's label might not always match the object name. For example, an organization in the medical industry might change the
label for Account to Patient. This label is then used in the Salesforce user interface. See the Salesforce online help for more information.

##### getLabelPlural()

Returns the object's plural label, which may or may not match the object name.

Signature

```
   public String getLabelPlural()

```

Return Value

Type: String

Usage

The object's plural label might not always match the object name. For example, an organization in the medical industry might change
the plural label for Account to Patients. This label is then used in the Salesforce user interface. See the Salesforce online help for more
information.

##### getLocalName()

Returns the name of the object, similar to the `getName` method. However, if the object is part of the current namespace, the namespace
portion of the name is omitted.

Signature

```
   public String getLocalName()

```


Apex Reference Guide DescribeSObjectResult Class

Return Value

Type: String

##### getName()

Returns the name of the object.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getRecordTypeInfos()

Returns a list of the record types supported by this object. The current user is not required to have access to a record type to see it in
this list.

Signature

```
   public List<Schema.RecordTypeInfo> getRecordTypeInfos()

```

Return Value

Type: List<Schema.RecordTypeInfo>

##### getRecordTypeInfosByDeveloperName()

Returns a map that matches developer names to their associated record type. The current user is not required to have access to a record
type to see it in this map.

Signature

```
   public Map<String, Schema.RecordTypeInfo> getRecordTypeInfosByDeveloperName()

```

Return Value

Type: Map<String, Schema.RecordTypeInfo>

##### getRecordTypeInfosById()

Returns a map that matches record IDs to their associated record types. The current user is not required to have access to a record type
to see it in this map.

Signature

```
   public Schema.RecordTypeInfo getRecordTypeInfosById()

```


Apex Reference Guide DescribeSObjectResult Class

Return Value

Type: Map<ID, Schema.RecordTypeInfo>

##### getRecordTypeInfosByName()

Returns a map that matches record labels to their associated record type. The current user is not required to have access to a record type
to see it in this map.

Signature

```
   public Schema.RecordTypeInfo getRecordTypeInfosByName()

```

Return Value

Type: Map<String, Schema.RecordTypeInfo>

##### getSObjectDescribeOption()

Returns the effective describe option used by the system for the SObject.

Signature

```
   public Schema.SObjectDescribeOptions getSObjectDescribeOption()

```

Return Value

Type: Schema.SObjectDescribeOptions

Valid values are:

**•** `SObjectDescribeOptions.FULL` : Indicates eager-load all elements of the describe, including child relationships, up-front
at the time of method invocation.

**•** `SObjectDescribeOptions.DEFERRED` : Indicates lazy-load child relationships. This means that all child relationships will
not be loaded at the time of first invocation of the method.

##### getSobjectType()

Returns the Schema.SObjectType object for the sObject. You can use this to create a similar sObject.

Signature

```
   public Schema.SObjectType getSobjectType()

```

Return Value

Type: Schema.SObjectType

##### getHasSubtypes()

Reserved for future use.


Apex Reference Guide DescribeSObjectResult Class

To check if Person Accounts are enabled for the current org, use this code snippet:

```
   Schema.SObjectType.Account.fields.getMap().containsKey( 'isPersonAccount' );

```

Signature

```
   public Boolean getHasSubtypes()

```

Return Value

Type: Boolean

##### **`hashCode()`**

Returns the hash code for the SObject.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### isAccessible()

Returns `true` if the current user can see this object, `false` otherwise.

Signature

```
   public Boolean isAccessible()

```

Return Value

Type: Boolean

Versioned Behavior Changes

In API version 54.0 and later, for custom settings and custom metadata type objects,
`DescribeSObjectResult.isAccessible()` returns `false` if the user doesn’t have permissions to access the queried
objects. In API version 53.0 and earlier, the method returns `true` even if the user doesn't have the required permissions.

##### isCreateable()

Returns `true` if the object can be created by the current user, `false` otherwise.

Signature

```
   public Boolean isCreateable()

```


Apex Reference Guide DescribeSObjectResult Class

Return Value

Type: Boolean

##### isCustom()

Returns `true` if the object is a custom object, `false` if it is a standard object.

Signature

```
   public Boolean isCustom()

```

Return Value

Type: Boolean

##### isCustomSetting()

Returns `true` if the object is a custom setting, `false` otherwise.

Signature

```
   public Boolean isCustomSetting()

```

Return Value

Type: Boolean

##### isDeletable()

Returns `true` if the object can be deleted by the current user, `false` otherwise.

Signature

```
   public Boolean isDeletable()

```

Return Value

Type: Boolean

##### isDeprecatedAndHidden()

Reserved for future use.

Signature

```
   public Boolean isDeprecatedAndHidden()

```

Return Value

Type: Boolean


Apex Reference Guide DescribeSObjectResult Class

##### isFeedEnabled()

Returns `true` if Chatter feeds are enabled for the object, `false` otherwise. This method is only available for Apex classes and triggers
saved using SalesforceAPI version 19.0 and later.

Signature

```
   public Boolean isFeedEnabled()

```

Return Value

Type: Boolean

##### isMergeable()

Returns `true` if the object can be merged with other objects of its type by the current user, `false` otherwise. `true` is returned for
leads, contacts, and accounts.

Signature

```
   public Boolean isMergeable()

```

Return Value

Type: Boolean

##### isMruEnabled()

Returns `true` if Most Recently Used (MRU) list functionality is enabled for the object, `false` otherwise.

Signature

```
   public Boolean isMruEnabled()

```

Return Value

Type: Boolean

##### isQueryable()

Returns `true` if the object can be queried by the current user, `false` otherwise

Signature

```
   public Boolean isQueryable()

```

Return Value

Type: Boolean


### Apex Reference Guide DescribeTabResult Class

##### isSearchable()

Returns `true` if the object can be searched by the current user, `false` otherwise.

Signature

```
   public Boolean isSearchable()

```

Return Value

Type: Boolean

##### isUndeletable()

Returns `true` if the object can be undeleted by the current user, `false` otherwise.

Signature

```
   public Boolean isUndeletable()

```

Return Value

Type: Boolean

##### isUpdateable()

Returns `true` if the object can be updated by the current user, `false` otherwise.

Signature

```
   public Boolean isUpdateable()

```

Return Value

Type: Boolean

##### **`toString()`**

Returns a string that represents the SObject.

Signature

```
   public String toString()

```

Return Value

Type: String

### DescribeTabResult Class

Contains tab metadata information for a tab in a standard or custom app available in the Salesforce user interface.


Apex Reference Guide DescribeTabResult Class

Namespace

Schema

Usage

The `getTabs` method of the `Schema.DescribeTabSetResult` returns a list of `Schema.DescribeTabResult` objects
that describe the tabs of one app.

The methods in the `Schema.DescribeTabResult` class can be called using their property counterparts. For each method starting
##### with get, you can omit the get prefix and the ending parentheses () to call the property counterpart. For example,

`tabResultObj.label` is equivalent to `tabResultObj.getLabel()` . Similarly, for each method starting with `is`, omit
the `is` prefix and the ending parentheses `()` . For example, `tabResultObj.isCustom` is equivalent to
`tabResultObj.custom` .

#### DescribeTabResult Methods The following are methods for DescribeTabResult . All are instance methods.

IN THIS SECTION:

##### getColors()

Returns a list of color metadata information for all colors associated with this tab. Each color is associated with a theme and context.

getIconUrl()
Returns the URL for the main 32 x 32-pixel icon for a tab. This icon corresponds to the current theme (theme3) and appears next to
the heading at the top of most pages.

getIcons()
Returns a list of icon metadata information for all icons associated with this tab. Each icon is associated with a theme and context.

getLabel()
Returns the display label of this tab.

getMiniIconUrl()
Returns the URL for the 16 x 16-pixel icon that represents a tab. This icon corresponds to the current theme (theme3) and appears
in related lists and other locations.

getSobjectName()
Returns the name of the sObject that is primarily displayed on this tab (for tabs that display a particular SObject).

getUrl()
Returns a fully qualified URL for viewing this tab.

isCustom()
Returns `true` if this is a custom tab, or `false` if this is a standard tab.

##### getColors()

Returns a list of color metadata information for all colors associated with this tab. Each color is associated with a theme and context.

Signature

```
   public List<Schema.DescribeColorResult> getColors()

```


Apex Reference Guide DescribeTabResult Class

Return Value

Type: List<Schema.DescribeColorResult>

##### getIconUrl()

Returns the URL for the main 32 x 32-pixel icon for a tab. This icon corresponds to the current theme (theme3) and appears next to the
heading at the top of most pages.

Signature

```
   public String getIconUrl()

```

Return Value

Type: String

##### getIcons()

Returns a list of icon metadata information for all icons associated with this tab. Each icon is associated with a theme and context.

Signature

```
   public List<Schema.DescribeIconResult> getIcons()

```

Return Value

Type: List<Schema.DescribeIconResult>

##### getLabel()

Returns the display label of this tab.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getMiniIconUrl()

Returns the URL for the 16 x 16-pixel icon that represents a tab. This icon corresponds to the current theme (theme3) and appears in
related lists and other locations.

Signature

```
   public String getMiniIconUrl()

```


### Apex Reference Guide DescribeTabSetResult Class

Return Value

Type: String

##### getSobjectName()

Returns the name of the sObject that is primarily displayed on this tab (for tabs that display a particular SObject).

Signature

```
   public String getSobjectName()

```

Return Value

Type: String

##### getUrl()

Returns a fully qualified URL for viewing this tab.

Signature

```
   public String getUrl()

```

Return Value

Type: String

##### isCustom()

Returns `true` if this is a custom tab, or `false` if this is a standard tab.

Signature

```
   public Boolean isCustom()

```

Return Value

Type: Boolean

### DescribeTabSetResult Class

Contains metadata information about a Salesforce Classic standard or custom app available in the Salesforce user interface.

Namespace

Schema


Apex Reference Guide DescribeTabSetResult Class

Usage

The `Schema.describeTabs` method returns a list of `Schema.DescribeTabSetResult` objects that describe Salesforce
Classic standard and custom apps.

The methods in the `Schema.DescribeTabSetResult` class can be called using their property counterparts. For each method
starting with `get`, you can omit the `get` prefix and the ending parentheses `()` to call the property counterpart. For example,
`tabSetResultObj.label` is equivalent to `tabSetResultObj.getLabel()` . Similarly, for each method starting with
`is`, omit the `is` prefix and the ending parentheses `()` . For example, `tabSetResultObj.isSelected` is equivalent to
`tabSetResultObj.selected` .

Example

This example shows how to call the `Schema.describeTabs` method to get describe information for all available Salesforce Classic
apps. This example iterates through each describe result and gets more metadata information for the Sales app.

```
   // App we're interested to get more info about

   String appName = 'Sales';

   // Get tab set describes for each app

   List<Schema.DescribeTabSetResult> tabSetDesc = Schema.describeTabs();

   // Iterate through each tab set describe for each app and display the info

   for(Schema.DescribeTabSetResult tsr : tabSetDesc) {

      // Get more information for the Sales app

      if (tsr.getLabel() == appName) {

        // Find out if the app is selected

        if (tsr.isSelected()) {

           System.debug('The ' + appName + ' app is selected. ');

        }

        // Get the app's Logo URL and namespace

        String logo = tsr.getLogoUrl();

        System.debug('Logo URL: ' + logo);

        String ns = tsr.getNamespace();

        if (ns == '') {

           System.debug('The ' + appName + ' app has no namespace defined.');

        }

        else {

           System.debug('Namespace: ' + ns);

        }

        // Get the number of tabs

        System.debug('The ' + appName + ' app has ' + tsr.getTabs().size() + ' tabs.');

      }

   }

   // Example debug statement output

   // DEBUG|The Sales app is selected.

   // DEBUG|Logo URL:

   https:// MyDomainName .my.salesforce.com/img/seasonLogos/2014_winter_aloha.png

   // DEBUG|The Sales app has no namespace defined.

   // DEBUG|The Sales app has 14 tabs.

```


Apex Reference Guide DescribeTabSetResult Class

#### DescribeTabSetResult Methods The following are methods for DescribeTabSetResult . All are instance methods.

IN THIS SECTION:

##### getDescription()

Returns the display description for the standard or custom app.

##### getLabel()

Returns the display label for the standard or custom app.

getLogoUrl()
Returns a fully qualified URL to the logo image associated with the standard or custom app.

getNamespace()
Returns the developer namespace prefix of a Salesforce AppExchange managed package.

getTabs()
Returns metadata information about the standard or custom app’s displayed tabs.

isSelected()
Returns `true` if this standard or custom app is the user’s currently selected app in Salesforce Classic. Otherwise, returns `false` .

##### getDescription()

Returns the display description for the standard or custom app.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getLabel()

Returns the display label for the standard or custom app.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Usage

The display label changes when tabs are renamed in the Salesforce user interface. See the Salesforce online help for more information.


Apex Reference Guide DescribeTabSetResult Class

##### getLogoUrl()

Returns a fully qualified URL to the logo image associated with the standard or custom app.

Signature

```
   public String getLogoUrl()

```

Return Value

Type: String

##### getNamespace()

Returns the developer namespace prefix of a Salesforce AppExchange managed package.

Signature

```
   public String getNamespace()

```

Return Value

Type: String

Usage

This namespace prefix corresponds to the namespace prefix of the Developer Edition organization that was enabled to allow publishing
a managed package. This method applies to a custom app containing a set of tabs and installed as part of a managed package.

##### getTabs()

Returns metadata information about the standard or custom app’s displayed tabs.

Signature

```
   public List<Schema.DescribeTabResult> getTabs()

```

Return Value

Type: List<Schema.DescribeTabResult>

##### **`isSelected()`**

Returns `true` if this standard or custom app is the user’s currently selected app in Salesforce Classic. Otherwise, returns `false` .

Signature

```
   public Boolean isSelected()

```


### Apex Reference Guide DisplayType Enum

Return Value

Type: Boolean

### DisplayType Enum

A `Schema.DisplayType` enum value is returned by the field describe result's `getType` method.

Namespace

Schema

**Type Field Value** **What the Field Object Contains**

`ADDRESS` Address values

`ANYTYPE` Any value of the following types: `String`, `Picklist`, `Boolean`, `Integer`, `Double`,
`Percent`, `ID`, `Date`, `DateTime`, `URL`, or `Email` .

`BASE64` Base64-encoded arbitrary binary data (of type base64Binary)

`BOOLEAN` Boolean ( `true` or `false` ) values

`COMBOBOX` Comboboxes, which provide a set of enumerated values and allow the user to specify a value
not in the list

`COMPLEXVALUE` Complex Value Type (CVT)

`CURRENCY` Currency values

`DATACATEGORYGROUPREFERENCE` Reference to a data category group or a category unique name

`DATE` Date values

`DATETIME` DateTime values

`DOUBLE` Double values

`EMAIL` Email addresses

`ENCRYPTEDSTRING` Encrypted string

`FLOATARRAY` Array of float values, reserved for future use.

`ID` Primary key field for an object

`INTEGER` Integer values

`JSON` JSON format

`LOCATION` Location values, including latitude and longitude.

`LONG` Long values

`MULTIPICKLIST` Multi-select picklists, which provide a set of enumerated values from which multiple values can
be selected

`PERCENT` Percent values


### Apex Reference Guide FieldDescribeOptions Enum

**Type Field Value** **What the Field Object Contains**

`PHONE` Phone numbers. Values can include alphabetic characters. Client applications are responsible for
phone number formatting.

`PICKLIST` Single-select picklists, which provide a set of enumerated values from which only one value can
be selected

`REFERENCE` Cross-references to a different object, analogous to a foreign key field

`SOBJECT` An sObject variable represents a row of data and can only be declared in Apex using the SOAP
API name of the object.

`STRING` String values

`TEXTAREA` String values that are displayed as multiline text fields

`TEXTARRAY` Array of text values, reserved for future use.

`TIME` Time values

`URL` URL values that are displayed as hyperlinks

Usage

[For more information, see Field Types in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/field_types.htm) _Object Reference for Salesforce_ . For more information about the methods shared by all enums,
see Enum Methods.

### FieldDescribeOptions Enum

A `Schema.FieldDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

Usage

For more information about the method using this enum, see `getDescribe(options)` .

Enum Values

The following are the values of the `Schema.FieldDescribeOptions` enum.

**Value** **Description**

`DEFAULT` Compute context-specific, describe field results.

`FULL_DESCRIBE` Compute all aspects of describe field results.

### FieldSet Class

Contains methods for discovering and retrieving the details of field sets created on sObjects.


Apex Reference Guide FieldSet Class

Namespace

Schema

Usage

Use the methods in the `Schema.FieldSet` class to discover the fields contained within a field set, and get details about the field
set itself, such as the name, namespace, label, and so on. The following example shows how to get a collection of field set describe result
objects for an sObject. The key of the returned Map is the field set name, and the value is the corresponding field set describe result.

```
   Map<String, Schema.FieldSet> FsMap =

      Schema.SObjectType.Account.fieldSets.getMap();

```

Field sets are also available from sObject describe results. The following lines of code are equivalent to the prior sample:

```
   Schema.DescribeSObjectResult d =

     Account.sObjectType.getDescribe();

   Map<String, Schema.FieldSet> FsMap =

     d.fieldSets.getMap();

```

To work with an individual field set, you can access it via the map of field sets on an sObject or, when you know the name of the field
set in advance, using an explicit reference to the field set. The following two lines of code retrieve the same field set:

```
   Schema.FieldSet fs1 = Schema.SObjectType.Account.fieldSets.getMap().get('field_set_name');

   Schema.FieldSet fs2 = Schema.SObjectType.Account.fieldSets.field_set_name;

```

Example: Displaying a Field Set on a Visualforce Page

This sample uses `Schema.FieldSet` and `Schema.FieldSetMember` methods to dynamically get all the fields in the
Dimensions field set for the Merchandise custom object. The list of fields is then used to construct a SOQL query that ensures those fields
are available for display. The Visualforce page uses the `MerchandiseDetails` class as its controller.

```
   public class MerchandiseDetails {

      public Merchandise__c merch { get; set; }

      public MerchandiseDetails() {

        this.merch = getMerchandise();

      }

      public List<Schema.FieldSetMember> getFields() {

        return SObjectType.Merchandise__c.FieldSets.Dimensions.getFields();

      }

      private Merchandise__c getMerchandise() {

        String query = 'SELECT ';

        for(Schema.FieldSetMember f : this.getFields()) {

           query += f.getFieldPath() + ', ';

        }

        query += 'Id, Name FROM Merchandise__c LIMIT 1';

        return Database.query(query);

      }

   }

```


Apex Reference Guide FieldSet Class

The Visualforce page using the above controller is simple:

```
   <apex:page controller="MerchandiseDetails">

      <apex:form >

       <apex:pageBlock title="Product Details">

         <apex:pageBlockSection title="Product">

            <apex:inputField value="{!merch.Name}"/>

         </apex:pageBlockSection>

         <apex:pageBlockSection title="Dimensions">

            <apex:repeat value="{!fields}" var="f">

              <apex:inputField value="{!merch[f.fieldPath]}"

                 required="{!OR(f.required, f.dbrequired)}"/>

            </apex:repeat>

         </apex:pageBlockSection>

        </apex:pageBlock>

      </apex:form>

   </apex:page>

```

One thing to note about the above markup is the expression used to determine if a field on the form should be indicated as being a
required field. A field in a field set can be required by either the field set definition, or the field’s own definition. The expression handles
both cases.

#### FieldSet Methods The following are methods for FieldSet . All are instance methods.

IN THIS SECTION:

##### getDescription()

Returns the field set’s description.

getFields()
Returns a list of `Schema.FieldSetMember` objects for the fields making up the field set.

getLabel()
Returns the translation of the text label that is displayed next to the field in the Salesforce user interface.

getName()
Returns the field set’s name.

getNamespace()
Returns the field set’s namespace.

getSObjectType()
Returns the `Schema.sObjectType` of the sObject containing the field set definition.

##### getDescription()

Returns the field set’s description.


Apex Reference Guide FieldSet Class

Signature

```
   public String getDescription()

```

Return Value

Type: `String`

Usage

Description is a required field for a field set, intended to describe the context and content of the field set. It’s often intended for
administrators who might be configuring a field set defined in a managed package, rather than for end users.

##### getFields()

Returns a list of `Schema.FieldSetMember` objects for the fields making up the field set.

Signature

```
   public List<FieldSetMember> getFields()

```

Return Value

Type: List<Schema.FieldSetMember>

##### getLabel()

Returns the translation of the text label that is displayed next to the field in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: `String`

##### getName()

Returns the field set’s name.

Signature

```
   public String getName()

```

Return Value

Type: `String`


### Apex Reference Guide FieldSetMember Class

##### getNamespace()

Returns the field set’s namespace.

Signature

```
   public String getNamespace()

```

Return Value

Type: `String`

Usage

The returned namespace is an empty string if your organization hasn’t set a namespace, and the field set is defined in your organization.
Otherwise, it’s the namespace of your organization, or the namespace of the managed package containing the field set.

##### getSObjectType()

Returns the `Schema.sObjectType` of the sObject containing the field set definition.

Signature

```
   public Schema.SObjectType getSObjectType()

```

Return Value

Type: `Schema.SObjectType`

### FieldSetMember Class

Contains methods for accessing the metadata for field set member fields.

Namespace

Schema

Usage

Use the methods in the `Schema.FieldSetMember` class to get details about fields contained within a field set, such as the field
label, type, a dynamic SOQL-ready field path, and so on. The following example shows how to get a collection of field set member
describe result objects for a specific field set on an sObject:

```
   List<Schema.FieldSetMember> fields =

      Schema.SObjectType.Account.fieldSets.getMap().get('field_set_name').getFields();

```


Apex Reference Guide FieldSetMember Class

If you know the name of the field set in advance, you can access its fields more directly using an explicit reference to the field set:

```
   List<Schema.FieldSetMember> fields =

      Schema.SObjectType.Account.fieldSets.field_set_name.getFields();

```

SEE ALSO:

FieldSet Class

#### FieldSetMember Methods The following are methods for FieldSetMember . All are instance methods.

IN THIS SECTION:

##### getDBRequired()

Returns `true` if the field is required by the field’s definition in its sObject, otherwise, `false` .

##### getFieldPath()

Returns a field path string in a format ready to be used in a dynamic SOQL query.

getLabel()
Returns the text label that’s displayed next to the field in the Salesforce user interface.

getRequired()
Returns `true` if the field is required by the field set, otherwise, `false` .

getType()
Returns the field’s Apex data type.

getSObjectField()
Returns the token for this field.

##### getDBRequired()

Returns `true` if the field is required by the field’s definition in its sObject, otherwise, `false` .

Signature

```
   public Boolean getDBRequired()

```

Return Value

Type: `Boolean`

##### getFieldPath()

Returns a field path string in a format ready to be used in a dynamic SOQL query.

Signature

```
   public String getFieldPath()

```


Apex Reference Guide FieldSetMember Class

Return Value

Type: `String`

Example

See Displaying a Field Set on a Visualforce Page for an example of how to use this method.

##### getLabel()

Returns the text label that’s displayed next to the field in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: `String`

##### getRequired()

Returns `true` if the field is required by the field set, otherwise, `false` .

Signature

```
   public Boolean getRequired()

```

Return Value

Type: `Boolean`

##### getType()

Returns the field’s Apex data type.

Signature

```
   public Schema.DisplayType getType()

```

Return Value

Type: `Schema.DisplayType`

##### getSObjectField()

Returns the token for this field.

Signature

```
   public Schema.sObjectField getSObjectField()

```


### Apex Reference Guide PicklistEntry Class

Return Value

Type: Schema.SObjectField

### PicklistEntry Class

Represents a picklist entry.

Namespace

Schema

Usage

Picklist fields contain a list of one or more items from which a user chooses a single item. They display as drop-down lists in the Salesforce
user interface. One of the items can be configured as the default item.

A `Schema.PicklistEntry` object is returned from the field describe result using the `getPicklistValues` method. For
example:

```
   Schema.DescribeFieldResult F = Account.Industry.getDescribe();

   List<Schema.PicklistEntry> P = F.getPicklistValues();

#### PicklistEntry Methods

### The following are methods for PicklistEntry . All are instance methods.

```

IN THIS SECTION:

##### getLabel()

Returns the display name of this item in the picklist.

getValue()
Returns the value of this item in the picklist.

isActive()
Returns `true` if this item must be displayed in the drop-down list for the picklist field in the user interface, `false` otherwise.

isDefaultValue()
Returns `true` if this item is the default value for the picklist, `false` otherwise. Only one item in a picklist can be designated as
the default.

##### getLabel()

Returns the display name of this item in the picklist.

Signature

```
   public String getLabel()

```


### Apex Reference Guide RecordTypeInfo Class

Return Value

Type: String

##### getValue()

Returns the value of this item in the picklist.

Signature

```
   public String getValue()

```

Return Value

Type: String

##### isActive()

Returns `true` if this item must be displayed in the drop-down list for the picklist field in the user interface, `false` otherwise.

Signature

```
   public Boolean isActive()

```

Return Value

Type: Boolean

##### isDefaultValue()

Returns `true` if this item is the default value for the picklist, `false` otherwise. Only one item in a picklist can be designated as the
default.

Signature

```
   public Boolean isDefaultValue()

```

Return Value

Type: Boolean

### RecordTypeInfo Class

Contains methods for accessing record type information for an sObject with associated record types.

Namespace

Schema


Apex Reference Guide RecordTypeInfo Class

Usage

A RecordTypeInfo object is returned from the sObject describe result using the `getRecordTypeInfos` method. For example:

```
   Schema.DescribeSObjectResult R = Account.SObjectType.getDescribe();

   List<Schema.RecordTypeInfo> RT = R.getRecordTypeInfos();

```

In addition to the `getRecordTypeInfos` method, you can use the `getRecordTypeInfosById` and the
`getRecordTypeInfosByName` methods. These methods return maps that associate RecordTypeInfo with record IDs and record
labels, respectively.

Example

The following example assumes at least one record type has been created for the Account object:

```
   RecordType rt = [SELECT Id,Name FROM RecordType WHERE SobjectType='Account' LIMIT 1];

   Schema.DescribeSObjectResult d = Schema.SObjectType.Account;

   Map<Id,Schema.RecordTypeInfo> rtMapById = d.getRecordTypeInfosById();

   Schema.RecordTypeInfo rtById = rtMapById.get(rt.id);

   Map<String,Schema.RecordTypeInfo> rtMapByName = d.getRecordTypeInfosByName();

   Schema.RecordTypeInfo rtByName = rtMapByName.get(rt.name);

   System.assertEquals(rtById,rtByName);

#### RecordTypeInfo Methods The following are methods for RecordTypeInfo . All are instance methods.

```

IN THIS SECTION:

getDeveloperName()
Returns the developer name for this record type.

getName()
Returns the UI label of this record type. The label can be translated into any language that Salesforce supports.

getRecordTypeId()
Returns the ID of this record type.

isActive()
Returns `true` if this record type is active, `false` otherwise.

isAvailable()
Returns `true` if this record type is available to the current user, `false` otherwise. Use this method to display a list of available
record types to the user when he or she is creating a new record.

isDefaultRecordTypeMapping()
Returns `true` if this is the default record type for the user, `false` otherwise.

isMaster()
Returns `true` if this is the master record type and `false` otherwise. The master record type is the default record type that’s used
when a record has no custom record type associated with it.


Apex Reference Guide RecordTypeInfo Class

##### getDeveloperName()

Returns the developer name for this record type.

Signature

```
   public String getDeveloperName()

```

Return Value

Type: String

##### getName()

Returns the UI label of this record type. The label can be translated into any language that Salesforce supports.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getRecordTypeId()

Returns the ID of this record type.

Signature

```
   public ID getRecordTypeId()

```

Return Value

Type: ID

##### isActive()

Returns `true` if this record type is active, `false` otherwise.

Signature

```
   public Boolean isActive()

```

Return Value

Type: Boolean


### Apex Reference Guide SOAPType Enum

##### isAvailable()

Returns `true` if this record type is available to the current user, `false` otherwise. Use this method to display a list of available record
types to the user when he or she is creating a new record.

Signature

```
   public Boolean isAvailable()

```

Return Value

Type: Boolean

##### isDefaultRecordTypeMapping()

Returns `true` if this is the default record type for the user, `false` otherwise.

Signature

```
   public Boolean isDefaultRecordTypeMapping()

```

Return Value

Type: Boolean

##### isMaster()

Returns `true` if this is the master record type and `false` otherwise. The master record type is the default record type that’s used
when a record has no custom record type associated with it.

Signature

```
   public Boolean isMaster()

```

Return Value

Type: Boolean

### SOAPType Enum

A `Schema.SOAPType` enum value is returned by the field describe result `getSoapType` method.

Namespace

Schema

**Type Field Value** **What the Field Object Contains**

`anytype` Any value of the following types: `String`, `Boolean`, `Integer`, `Double`, `ID`, `Date` or
`DateTime` .


### Apex Reference Guide SObjectDescribeOptions Enum

**Type Field Value** **What the Field Object Contains**

`base64binary` Base64-encoded arbitrary binary data (of type base64Binary)

`Boolean` Boolean ( `true` or `false` ) values

`Date` Date values

`DateTime` DateTime values

`Double` Double values

`ID` Primary key field for an object

`Integer` Integer values

`String` String values

`Time` Time values

Usage

To programmatically retrieve the list of valid SOAPType enum values, use this code sample.

```
   system.debug(SoapType.values().size()); //Gets the number of supported values

   for (SoapType st : SoapType.values()) system.debug(st);

```

[For more information, see SOAPTypes in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm#soaptype_topic) _SOAP API Developer Guide_ . For more information about the methods shared by all enums,
see Enum Methods.

### SObjectDescribeOptions Enum

A `Schema.SObjectDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

Usage

For more information about the method using this enum, see `getDescribe(options)` .

Enum Values

The following are the values of the `Schema.SObjectDescribeOptions` enum.

**Value** **Description**

`DEFAULT` Either eager-load or lazy-load depending on the API version.

`DEFERRED` Lazy-load child relationships; do not load all child relationships at the time of first
invocation of the method.

`FULL` Eager-load all elements of the describe, including child relationships, up-front at
the time of method invocation.

See `getDescribe(options)` .


### Apex Reference Guide SObjectField Class SObjectField Class

A `Schema.sObjectField` object is returned from the field describe result using the `getController` and `getSObjectField`
methods.

Namespace

Schema

Example

```
   Schema.DescribeFieldResult F = Account.Industry.getDescribe();

   Schema.sObjectField T = F.getSObjectField();

#### sObjectField Methods The following are instance methods for sObjectField .

```

IN THIS SECTION:

##### getDescribe()

Returns the describe field result for this field.

##### getDescribe(options)

Returns the describe field result for this field. This method also provides an option to get all the describe field results for an object.

##### getDescribe()

Returns the describe field result for this field.

Signature

```
   public Schema.DescribeFieldResult getDescribe()

```

Return Value

Type: Schema.DescribeFieldResult

##### getDescribe(options)

Returns the describe field result for this field. This method also provides an option to get all the describe field results for an object.

Signature

```
   public Schema.DescribeFieldResult getDescribe(Object options)

```

Parameters

```
   options
```

Type: Object


### Apex Reference Guide SObjectType Class

Use this parameter to pass `FieldDescribeOptions.FULL_DESCRIBE` when a subset of system objects could have
different results for picklist values based on the context they're invoked in. This parameter computes all aspects of describe field
results.

For example, `AIConversationContext.PersonType` field is a picklist that contains a list of accessible object types.

Return Value

Type: Schema.DescribeFieldResult

### SObjectType Class

A `Schema.sObjectType` object is returned from the field describe result using the `getReferenceTo` method, or from the
sObject describe result using the `getSObjectType` method.

Namespace

Schema

Usage

```
   Schema.DescribeFieldResult F = Account.Industry.getDescribe();

   List<Schema.sObjectType> P = F.getReferenceTo();

#### SObjectType Methods

### The following are methods for SObjectType . All are instance methods.

```

IN THIS SECTION:

##### getDescribe()

Returns the describe sObject result for this field.

getDescribe(options)
Returns the describe sObject result for this field; the parameter value determines whether all child relationships are loaded up-front,
or not.

newSObject()
Constructs a new sObject of this type.

newSObject(id)
Constructs a new sObject of this type, with the specified ID.

newSObject(recordTypeId, loadDefaults)
Constructs a new sObject of this type, and optionally, of the specified record type ID and with default custom field values.

##### getDescribe()

Returns the describe sObject result for this field.


Apex Reference Guide SObjectType Class

Signature

```
   public Schema.DescribeSObjectResult getDescribe()

```

Return Value

Type: Schema.DescribeSObjectResult

##### getDescribe(options)

Returns the describe sObject result for this field; the parameter value determines whether all child relationships are loaded up-front, or
not.

Signature

```
   public Schema.DescribeSObjectResult getDescribe(Object options)

```

Parameters

```
   options
```

Type: Object

The parameter values determine how the elements of the describe operation are loaded.

**•** Use `SObjectDescribeOptions.FULL` to eager-load all elements of the describe, including child relationships, up-front
at the time of method invocation. This describe guarantees fully coherent results, even if the describe object is passed to another
namespace, API version, or other Apex context that may have different results when generating describe attributes.

**•** Use `SObjectDescribeOptions.DEFERRED` to enable lazy initialization of describe attributes on first use. This means
that all child relationships will not be loaded at the time of first invocation of the method.

**•** Use `SObjectDescribeOptions.DEFAULT` to default to either eager-load or lazy-load depending on the API version.

The type of describe operation, as determined by the parameter value is depicted in this table.

**Table 2: Type of Load for SObjectType.getDescribe()**

Return Value

Type: Schema.DescribeSObjectResult

##### newSObject()

Constructs a new sObject of this type.

Signature

```
   public sObject newSObject()

```


Apex Reference Guide SObjectType Class

Return Value

Type: sObject

Example

[For an example, see Dynamic DML.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_dml.htm)

##### newSObject(id)

Constructs a new sObject of this type, with the specified ID.

Signature

```
   public sObject newSObject(ID id)

```

Parameters

```
   id
```

Type: ID

Return Value

Type: sObject

Usage

For the argument, pass the ID of an existing record in the database.

After you create a new sObject, the sObject returned has all fields set to `null` . You can set any updateable field to desired values and
then update the record in the database. Only the fields you set new values for are updated and all other fields which are not system
fields are preserved.

##### newSObject(recordTypeId, loadDefaults)

Constructs a new sObject of this type, and optionally, of the specified record type ID and with default custom field values.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Signature

```
   public sObject newSObject(ID recordTypeId, Boolean loadDefaults)

```

Parameters

```
   recordTypeId
```

Type: ID

Specifies the record type ID of the sObject to create. If no record type exists for this sObject, use `null` . If the sObject has record
types and you specify `null`, the default record type is used.


Apex Reference Guide SObjectType Class

```
   loadDefaults
```

Type: Boolean

Specifies whether to populate custom fields with their predefined default values ( `true` ) or not ( `false` ).

Return Value

Type: sObject

Usage

**•** For required fields that have no default values, make sure to provide a value before inserting the new sObject. Otherwise, the insertion
results in an error. An example is the Account Name field or a master-detail relationship field.

**•** Since picklists and multi-select picklists can have default values specified per record type, this method populates the default value
corresponding to the record type specified.

**•** If fields have no predefined default values and the _`loadDefaults`_ argument is `true`, this method creates the sObject with field
values of `null` .

**•** If the _`loadDefaults`_ argument is `false`, this method creates the sObject with field values of `null` .

**•** This method populates read-only custom fields of the new sObject with default values. You can then insert the new sObject with
the read-only fields, even though these fields cannot be edited after they’re inserted.

**•** If a custom field is marked as unique and also provides a default value, inserting more than one new sObject will cause a run-time
exception because of duplicate field values.

To learn more about default field values, see “Default Field Values” in the Salesforce online help.

Note: You can also use this method to create a platform event with a prepopulated `EventUuid` field value for Apex publish
[callbacks. For more information, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
_Platform Events Developer Guide_ .

Example: Creating New sObject with Default Values

This sample creates an account with any default values populated for its custom fields, if any, using the `newSObject` method. It also
creates a second account for a specific record type. For both accounts, the sample sets the Name field, which is a required field that
doesn’t have a default value, before inserting the new accounts.

```
   // Create an account with predefined default values

   Account acct = (Account)Account.sObjectType.newSObject(null, true);

   // Provide a value for Name

   acct.Name = 'Acme';

   // Insert new account

   insert acct;

   // This is for record type RT1 of Account

   ID rtId = [SELECT Id FROM RecordType WHERE sObjectType='Account' AND Name='RT1'].Id;

   Account acct2 = (Account)Account.sObjectType.newSObject(rtId, true);

   // Provide a value for Name

   acct2.Name = 'Acme2';

   // Insert new account

   insert acct2;

```


## Apex Reference Guide Search Namespace Search Namespace The Search namespace provides classes for getting search results and suggestion results. The following are the classes in the Search namespace.

IN THIS SECTION:

### KnowledgeSuggestionFilter Class

Filter settings that narrow the results from a call to `System.Search.suggest(searchQuery, sObjectType,`
`options)` when the SOSL search query contains a KnowledgeArticleVersion object.

QuestionSuggestionFilter Class
The `Search.QuestionSuggestionFilter` class filters results from a call to
`System.Search.suggest(searchQuery, sObjectType, options)` when the SOSL `searchQuery` contains
a `FeedItem` object.

SearchResult Class
A wrapper object that contains an sObject and search metadata.

SearchResults Class
Wraps the results returned by the `Search.find(String)` method.

SuggestionOption Class
Options that narrow record and article suggestion results returned from a call to `System.Search.suggest(String,`

`String, Search.SuggestionOption)` .

SuggestionResult Class
A wrapper object that contains an sObject.

SuggestionResults Class
Wraps the results returned by the `Search.suggest(String, String, Search.SuggestionOption)` method.

SEE ALSO:

find(searchQuery)

suggest(searchQuery, sObjectType, suggestions)

### KnowledgeSuggestionFilter Class

Filter settings that narrow the results from a call to `System.Search.suggest(searchQuery, sObjectType, options)`
when the SOSL search query contains a KnowledgeArticleVersion object.

Namespace

## Search

#### KnowledgeSuggestionFilter Methods

### The following are methods for KnowledgeSuggestionFilter .


Apex Reference Guide KnowledgeSuggestionFilter Class

IN THIS SECTION:

##### addArticleType(articleType)

Adds a filter that narrows suggestion results to display the specified article type. This filter is optional.

##### addDataCategory(dataCategoryGroupName, dataCategoryName)

Adds a filter that narrows suggestion results to display articles in the specified data category. This filter is optional.

addTopic(topic)
Specifies the article topic to return. This filter is optional.

setChannel(channelName)
Sets a channel to narrow the suggestion results to articles in the specified channel. This filter is optional.

setDataCategories(dataCategoryFilters)
Adds filters that narrow suggestion results to display articles in the specified data categories. Use this method to set multiple data
category group and name pairs in one call. This filter is optional.

setLanguage(localeCode)
Sets a language to narrow the suggestion results to display articles in that language. This filter value is required in calls to
`System.Search.suggest(String, String, Search.SuggestionOption)` .

setPublishStatus(publishStatus)
Sets a publish status to narrow the suggestion results to display articles with that status. This filter value is required in calls to
`System.Search.suggest(String, String, Search.SuggestionOption)` .

setValidationStatus(validationStatus)
Sets a validation status to narrow the suggestion results to display articles with that status. This filter is optional.

##### addArticleType(articleType)

Adds a filter that narrows suggestion results to display the specified article type. This filter is optional.

Signature

```
   public void addArticleType(String articleType)

```

Parameters

```
   articleType
```

Type: String

A three-character ID prefix indicating the desired article type.

Return Value

Type: void

Usage

To add more than 1 article type, call the method multiple times.

##### addDataCategory(dataCategoryGroupName, dataCategoryName)

Adds a filter that narrows suggestion results to display articles in the specified data category. This filter is optional.


Apex Reference Guide KnowledgeSuggestionFilter Class

Signature

```
   public void addDataCategory(String dataCategoryGroupName, String dataCategoryName)

```

Parameters

```
   dataCategoryGroupName
```

Type: String

The name of the data category group

```
   dataCategoryName
```

Type: String

The name of the data category.

Return Value

Type: void

Usage

To set multiple data categories, call the method multiple times. The name of the data category group and name of the data category
for desired articles, expressed as a mapping, for example,
`Search.KnowledgeSuggestionFilter.addDataCategory('Regions', 'Asia')` .

##### addTopic(topic)

Specifies the article topic to return. This filter is optional.

Signature

```
   public void addTopic(String topic)

```

Parameters

##### _`addTopic`_

Type: String

The name of the article topic.

Return Value

Type: void

Usage

To add more than 1 article topic, call the method multiple times.

##### setChannel(channelName)

Sets a channel to narrow the suggestion results to articles in the specified channel. This filter is optional.


Apex Reference Guide KnowledgeSuggestionFilter Class

Signature

```
   public void setChannel(String channelName)

```

Parameters

```
   channelName
```

Type: String

The name of a channel. Valid values are:

**•** `AllChannels` –Visible in all channels the user has access to

**•** `App` –Visible in the internal Salesforce Knowledge application

**•** `Pkb` –Visible in the public knowledge base

**•** `Csp` –Visible in the Customer Portal

**•** `Prm` –Visible in the Partner Portal

If `channel` isn’t specified, the default value is determined by the type of user.

