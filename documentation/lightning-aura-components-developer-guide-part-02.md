Aura Component Bundle Design Resources

### Lightning Page Template Component Best Practices

Make Your Lightning Page Components Width-Aware with lightning:flexipageRegionInfo

### Lightning Page Template Component Best Practices

Keep these best practices and limitations in mind when creating Lightning page template components.


### Using Components Make Your Lightning Page Components Width-Aware with

lightning:flexipageRegionInfo

**•** Don’t add custom background styling to a template component. It interferes with Salesforce’s Lightning Experience page themes.

**•** We strongly recommend including supported form factor information in the design file of all of your components. If you don’t, the
component might behave in unexpected ways.

**•** Template component supported form factors must be equal to, or a subset of, the supported form factors of its page type.

**•** Once a component is in use on a Lightning page, you can only increase the supported form factors for the component, not decrease
them.

**•** Including scrolling regions in your template component can cause problems when you try to view it in the Lightning App Builder.

**•** Custom templates can’t be extensible nor extended—you can’t extend a template from anything else, nor can you extend other
things from a template.

**•** Using getters to get the regions as variables works at design time but not at run time. Here’s an example of what we mean.

```
     <aura:component implements="lightning:appHomeTemplate">

       <aura:attribute name="region" type="Aura.Component[]" />

       <aura:handler name="init" value="{!this}" action="{!c.init}" />

       <div>

          {!v.region}

       </div>

     </aura:component>

     {

       init : function(component, event, helper) {

          var region = cmp.get('v.region'); // This will fail at run time.

          ...

       }

     }

```

**•** You can remove regions from a template if it’s not being used by a Lightning page, and if it’s not set to access=global. You can add
regions at any time.

**•** A region can be used more than once in the code, but only one instance of the region should render at run time.

**•** A template component can contain up to 25 regions.

**•** The order that you list the regions in a page template is the order that the regions appear in when admins migrate region content
using the template switching wizard in the Lightning App Builder. We recommend that you label the regions and list them in a
logical order in your template, such as top to bottom or left to right.

### Make Your Lightning Page Components Width-Aware with

```
  lightning:flexipageRegionInfo

```

When you add a component to a region on a page in the Lightning App Builder, the `lightning:flexipageRegionInfo`
sub-component passes the width of that region to its parent component. With `lightning:flexipageRegionInfo` and some
strategic CSS, you can tell the parent component to render in different ways in different regions at runtime.

For example, the List View component renders differently in a large region than it does in a small region as it’s a width-aware component.


Using Components Make Your Lightning Page Components Width-Aware with
lightning:flexipageRegionInfo

Valid region width values are: `Small`, `Medium`, `Large`, and `Xlarge` .

You can use CSS to style your component and to help determine how your component renders. Here’s an example.

This simple component has two fields, field1 and field2. The component renders with the fields side by side, filling 50% of the region’s
available width when not in a small region. When the component is in a small region, the fields render as a list, using 100% of the region’s
width.

```
   <aura:component implements="flexipage:availableForAllPageTypes">

      <aura:attribute name="width" type="String"/>

      <lightning:flexipageRegionInfo width="{!v.width}"/>

      <div class="{! 'container' + (v.width=='SMALL'?' narrowRegion':'')}">

        <div class="{! 'eachField f1' + (v.width=='SMALL'?' narrowRegion':'')}">

           <lightning:input name="field1" label="First Name"/>

        </div>

        <div class="{! 'eachField f2' + (v.width=='SMALL'?' narrowRegion':'')}">

           <lightning:input name="field2" label="Last Name"/>

        </div>

      </div>

   </aura:component>

```

Here’s the CSS file that goes with the component.

```
   .THIS .eachField.narrowRegion{

      width:100%;

   }

   .THIS .eachField{

      width:50%;

      display:inline-block;

   }

```


### Using Components Tips and Considerations for Configuring Components for

Lightning Pages and the Lightning App Builder

### Tips and Considerations for Configuring Components for Lightning Pages

and the Lightning App Builder

Keep these guidelines in mind when creating components and component bundles for Lightning pages and the Lightning App Builder.

Note: Mark your resources, such as a component, with `access="global"` to make the resource usable outside of your own
org. For example, if you want a component to be usable in an installed package or by a Lightning App Builder user or a Experience
Builder user in another org.

You can also create documentation for a component, event, or interface marked `access="global"` . This documentation is
automatically displayed in the Component Library of an org that uses or installs your package.

Components

**•** Set a friendly name for the component using the `label` attribute in the element in the design file, such as `<design:component`
`label="foo">` .

**•** Make your components fill 100% of the width (including margins) of the region that they display in.

**•** Don’t set absolute width values on your components.

**•** If components require interaction, they must provide an appropriate placeholder behavior in declarative tools.

**•** A component must never display a blank box. Think of how other sites work. For example, Facebook displays an outline of the feed
before the actual feed items come back from the server. The outline improves the user’s perception of UI responsiveness.

**•** If the component depends on a fired event, then give it a default state that displays before the event fires.

**•** Style components in a manner consistent with the styling of Lightning Experience and consistent with the Salesforce Design System.

**•** The Lightning App Builder manages spacing between components automatically. Don't add margins to your component CSS, and
avoid adding padding.

**•** Don’t use `float` or `position: absolute` in your CSS properties. These properties break the component out of the page
structure and, as a result, break the page.

Attributes

**•** Use the design file to control which attributes are exposed to the Lightning App Builder.

**•** Make your attributes easy to use and understandable to an administrator. Don’t expose SOQL queries, JSON objects, or Apex class
names.

**•** Give your required attributes default values. When a component that has required attributes with no default values is added to the
App Builder, it appears invalid, which is a poor user experience.

**•** Use basic supported types (string, integer, boolean) for any exposed attributes.

**•** Specify a min and max attribute for integer attributes in the `<design:attribute>` element to control the range of accepted
values.

**•** String attributes can provide a data source with a set of predefined values allowing the attribute to expose its configuration as a
picklist.

**•** Give all attributes a label with a friendly display name.

**•** Provide descriptions to explain the expected data and any guidelines, such as data format or expected range of values. Description
text appears as a tooltip in the Property Editor.

**•** To delete a design attribute for a component that implements the `flexipage:availableForAllPageTypes` or
`forceCommunity:availableForAllPageTypes` interface, first remove the interface from the component before


## Using Components Use Aura Components in Experience Builder

deleting the design attribute. Then reimplement the interface. If the component is referenced in a Lightning page, you must remove
the component from the page before you can change it.

Limitations

**•** The Lightning App Builder doesn’t support the Map, Object, or java:// complex types.

**•** When you use the Lightning App Builder, there’s a known limitation when you edit a group page. Your changes appear when you
visit the group from the Groups tab. Your changes don’t appear when you visit the group from the Recent Groups list on the Chatter
tab.

**•** Custom components that serve as containers, such as custom Tabs or Accordion components, aren’t supported in Lightning App
Builder. They display on the canvas, but you can’t interact with them or put any components inside them.

SEE ALSO:

Configure Components for Lightning Pages and the Lightning App Builder

Configure Components for Lightning Experience Record Pages

## Use Aura Components in Experience Builder

To use a custom Aura component in Experience Builder, you must configure the component and its component bundle so that they’re
compatible.

Note: As of Spring ’21, you can build Experience Builder sites using two programming models: the Lightning Web Components
model, and the original Aura Components model. The Marketing Website template is based on LWC and can only be used with
Lightning web components, not Aura components. Other templates are based on the Aura Components model and can use both
[Lightning web components and Aura components. See the Experience Builder Developer Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/)

IN THIS SECTION:

Configure Components for Experience Builder
Make your custom Aura components available to drag to the Lightning Components pane in Experience Builder.

Create Custom Theme Layout Components for Experience Builder
Create a custom theme layout to transform the appearance and overall structure of the pages in the Customer Service template.

Create Custom Component for Guest User Flows
Allow flows for your Experience Cloud guest users to provide alternative user registration screens, complex decision trees, and
conditional forms to gather user information. The following example uses the Site Class API. For more information, see “Site Class”
in the Salesforce Apex Developer Guide.

Create Custom Search and Profile Menu Components for Experience Builder
Create custom components to replace the Customer Service template’s standard Profile Header and Search & Post Publisher
components in Experience Builder.

Create Custom Content Layout Components for Experience Builder
Experience Builder includes several ready-to-use layouts that define the content regions of your page, such as a two-column layout
with a 2:1 ratio. However, if you need a layout that’s customized for your site, create a custom content layout component to use
when building new pages in Experience Builder. You can also update the content layout of the default pages that come with your
site template.


### Using Components Configure Components for Experience Builder Configure Components for Experience Builder

Make your custom Aura components available to drag to the Lightning Components pane in Experience Builder.

Note: As of Spring ’21, you can build Experience Builder sites using two programming models: the Lightning Web Components
model, and the original Aura Components model. The Marketing Website template is based on LWC and can only be used with
Lightning web components, not Aura components. Other templates are based on the Aura Components model and can use both
[Lightning web components and Aura components. See the Experience Builder Developer Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/)

Add a New Interface to Your Component

To appear in Experience Builder, a component must implement the `forceCommunity:availableForAllPageTypes`
interface.

Here’s the sample code for a simple “Hello World” component.

```
   <aura:component implements="forceCommunity:availableForAllPageTypes" access="global">

      <aura:attribute name="greeting" type="String" default="Hello" access="global" />

      <aura:attribute name="subject" type="String" default="World" access="global" />

      <div style="box">

       <span class="greeting">{!v.greeting}</span>, {!v.subject}!

      </div>

   </aura:component>

```

Note: Mark your resources, such as a component, with `access="global"` to make the resource usable outside of your own
org. For example, if you want a component to be usable in an installed package or by a Lightning App Builder user or a Experience
Builder user in another org.

You can also create documentation for a component, event, or interface marked `access="global"` . This documentation is
automatically displayed in the Component Library of an org that uses or installs your package.

Next, add a design resource to your component bundle. A design resource describes the design-time behavior of an Aura
component—information that visual tools need to allow adding the component to a page or app. It contains attributes that are available
for administrators to edit in Experience Builder.

Adding this resource is similar to adding it for the Lightning App Builder. For more information, see Configure Components for Lightning
Pages and the Lightning App Builder.

Important: When you add custom components to your Experience Builder site, they can bypass the object- and field-level security
[(FLS) you set for the guest user profile. Lightning components don’t automatically enforce CRUD and FLS when referencing objects](https://developer.salesforce.com/page/Enforcing_CRUD_and_FLS)
or retrieving the objects from an Apex controller. This means that the framework continues to display records and fields for which
users don’t have CRUD permissions and FLS visibility. You must manually enforce CRUD and FLS in your Apex controllers. Alternatively,
use a base component that implements Lightning Data Service on page 382.

SEE ALSO:

Component Bundles

Standard Design Tokens for Experience Builder Sites

### Create Custom Theme Layout Components for Experience Builder

Create a custom theme layout to transform the appearance and overall structure of the pages in the Customer Service template.


Using Components Create Custom Theme Layout Components for Experience
Builder

A theme layout component is the top-level layout for the template pages in your site. Theme layout components are organized and
applied to your pages through theme layouts. A theme layout component includes the common header and footer, and often includes
navigation, search, and the user profile menu. In contrast, the content layout defines the content regions of your pages. The next image
shows a two-column content layout.

A theme layout type categorizes the pages in your Experience Builder site that share the same theme layout.

When you create a custom theme layout component in the Developer Console, it appears in Experience Builder in the **Settings**    - **Theme**
area. Here you can assign it to new or existing theme layout types. Then you apply the theme layout type—and then the theme layout—in
the page’s properties.

1. Add an Interface to Your Theme Layout Component

A theme layout component must implement the `forceCommunity:themeLayout` interface to appear in Experience Builder in
the **Settings**     - **Theme** area.

Explicitly declare `{!v.body}` in your code to ensure that your theme layout includes the content layout. Add `{!v.body}` wherever
you want the page’s contents to appear within the theme layout.

You can add components to the regions in your markup or leave regions open for users to drag-and-drop components into. Attributes
declared as `Aura.Component[]` and included in your markup are rendered as open regions in the theme layout that users can
add components to.

In Customer Service, the Template Header consists of these locked regions:

**•** `search`, which contains the Search Publisher component

**•** `profileMenu`, which contains the User Profile Menu component

**•** `navBar`, which contains the Navigation Menu component

To create a custom theme layout that reuses the existing components in the Template Header region, declare `search`, `profileMenu`,
or `navBar` as the attribute name value, as appropriate. For example:

```
   <aura:attribute name="navBar" type="Aura.Component[]" required="false" />

```

Tip: If you create a custom profile menu or a search component, declaring the attribute name value also lets users select the
custom component when using your theme layout.

Here’s the sample code for a simple theme layout.

```
   <aura:component implements="forceCommunity:themeLayout" access="global" description="Sample

    Custom Theme Layout">

      <aura:attribute name="search" type="Aura.Component[]" required="false"/>

      <aura:attribute name="profileMenu" type="Aura.Component[]" required="false"/>

      <aura:attribute name="navBar" type="Aura.Component[]" required="false"/>

      <aura:attribute name="newHeader" type="Aura.Component[]" required="false"/>

      <div>

        <div class="searchRegion">

           {!v.search}

        </div>

        <div class="profileMenuRegion">

           {!v.profileMenu}

        </div>

        <div class="navigation">

           {!v.navBar}

        </div>

        <div class="newHeader">

```


Using Components Create Custom Theme Layout Components for Experience
Builder

```
           {!v.newHeader}

        </div>

        <div class="mainContentArea">

           {!v.body}

        </div>

      </div>

   </aura:component>

```

Note: Mark your resources, such as a component, with `access="global"` to make the resource usable outside of your own
org. For example, if you want a component to be usable in an installed package or by a Lightning App Builder user or a Experience
Builder user in another org.

You can also create documentation for a component, event, or interface marked `access="global"` . This documentation is
automatically displayed in the Component Library of an org that uses or installs your package.

Note: If you want to use a new, customizable profile menu instead of a self-service profile menu, you must declare the
themeHeaderProfileMenu attribute instead of profileMenu in the theme layout component. This only works in a B2B store or where
an out-of-box theme has been applied.

2. Add a Design Resource to Include Theme Properties

You can expose theme layout properties in Experience Builder by adding a design resource to your bundle.

This example adds two checkboxes to a theme layout called Small Header.

```
   <design:component label="Small Header">

      <design:attribute name="blueBackground" label="Blue Background"/>

      <design:attribute name="smallLogo" label="Small Logo"/>

   </design:component>

```

The design resource only exposes the properties. Implement the properties in the component.

```
   <aura:component implements="forceCommunity:themeLayout" access="global" description="Small

    Header">

      <aura:attribute name="blueBackground" type="Boolean" default="false"/>

      <aura:attribute name="smallLogo" type="Boolean" default="false" />

      ...

```

Design resources must be named _`componentName`_ `.design` .

3. Add a CSS Resource to Avoid Overlapping Issues

Add a CSS resource to your bundle to style the theme layout as needed.

To avoid overlapping issues with positioned elements, such as dialog boxes or hovers:

**•** Apply CSS styles.

```
     .THIS {

       position: relative;

       z-index: 1;

     }

```


### Using Components Create Custom Component for Guest User Flows

**•** Wrap the elements in your custom theme layout in a `div` tag.

```
     <div class="mainContentArea">

       {!v.body}

     </div>

```

Note: For custom theme layouts, SLDS is loaded by default.

CSS resources must be named _`componentName`_ `.css` .

SEE ALSO:

Create Custom Search and Profile Menu Components for Experience Builder

_Salesforce Help_ [: Custom Theme Layouts and Theme Layout Types](https://help.salesforce.com/HTViewHelpDoc?id=community_builder_theme.htm&language=en_US)

### Create Custom Component for Guest User Flows

Allow flows for your Experience Cloud guest users to provide alternative user registration screens, complex decision trees, and conditional
forms to gather user information. The following example uses the Site Class API. For more information, see “Site Class” in the Salesforce
Apex Developer Guide.

1. Create a Custom Aura Component

Using Guest User Flows for login or self registration requires a custom component that implements
`lightning:availableForFlowScreens` .

Here’s the sample code for a simple data collection preferences flow.

```
   <aura:component implements="lightning:availableForFlowScreens"

   controller="CommunitySelfRegController">

      <aura:attribute name="email" type="String" default=""/>

      <aura:attribute name="fname" type="String" default=""/>

      <aura:attribute name="lname" type="String" default=""/>

      <aura:attribute name="starturl" type="String" default=""/>

      <aura:attribute name="password" type="String" default=""/>

      <aura:attribute name="hasOptedTracking" type="Boolean" default="false"/>

      <aura:attribute name="hasOptedSolicit" type="Boolean" default="false"/>

      <aura:attribute name="op_url" type="String" default="" description="login url after

   user is created. "/>

      <aura:handler name="init" value="{!this}" action="{!c.init}" />

      <aura:if isTrue="{! (empty(v.op_url))}">

        <!-- empty url, the user is not yet created -->

        <h3> Registering user. Please wait. </h3>

        <aura:set attribute="else">

           <!-- User created, show link to login -->

           <h3> Success! Your account has been created. </h3>

           <button class="slds-button slds-button_neutral"

   onclick="{!c.login}">Login</button>

        </aura:set>

```


Using Components Create Custom Component for Guest User Flows

```
      </aura:if>

   </aura:component>

```

Controller file:

```
   ({

      init : function(cmp) {

        let email = cmp.get("v.email"),

           fname = cmp.get("v.fname"),

           lname = cmp.get("v.lname"),

           pass = cmp.get("v.password"),

           startUrl = cmp.get("v.starturl"),

           hasOptedSolicit = cmp.get("v.hasOptedSolicit"),

           hasOptedTracking = cmp.get("v.hasOptedTracking");

        let action = cmp.get("c.createExternalUser");

        action.setParams(

           {

             username: email,

             password: pass,

             startUrl: startUrl,

             fname: fname,

             lname: lname,

             hasOptedTracking: hasOptedTracking,

             hasOptedSolicit: hasOptedSolicit

           });

        action.setCallback(this, function(res) {

           if (action.getState() === "SUCCESS") {

             cmp.set("v.op_url", res.getReturnValue());

           }

        });

        $A.enqueueAction(action);

      },

      login: function(cmp){

        let url = cmp.get("v.op_url");

        window.location.href = url;

      }

   })

```

Design file:

```
   <design:component>

      <design:attribute name="email" />

      <design:attribute name="fname" />

      <design:attribute name="lname" />

      <design:attribute name="password" />

      <design:attribute name="hasOptedTracking" />

      <design:attribute name="hasOptedSolicit" />

   </design:component>

```


Using Components Create Custom Component for Guest User Flows

2. Create an Apex Class

The following example creates a class, `CommunitySelfRegController`, which is used with your Aura component to register
new Experience Cloud site users.

Note: Adding self registration with a flow requires the following:

**•** The `UserPreferencesHideS1BrowserUI` preference should be set to True. This prevents the mobile UI from
defaulting to the Salesforce Mobile App interface rather than your Experience Builder site.

**•** `CommunityNickname` is required and must be a unique value.

**•** The self registration preference should be enabled in your site with a valid profile and account.

```
   public class CommunitySelfRegController {

      @AuraEnabled

      public static String createExternalUser(

        String username, String password, String startUrl, String fname,

        String lname, Boolean hasOptedTracking, Boolean hasOptedSolicit) {

           Savepoint sp = null;

           try {

             sp = Database.setsavepoint();

             system.debug(sp);

             // Creating a user object.

             User u = new User();

             u.Username = username;

             u.Email = username;

             u.FirstName = fname;

             u.LastName = lname;

             // Default UI for mobile is set to S1 for user created using site object.

             // Enable this perm to change it to community (Experience Cloud).

             u.UserPreferencesHideS1BrowserUI = true;

             // Generating unique value for Experience Cloud nickname.

      String nickname = ((fname != null && fname.length() > 0) ? fname.substring(0,1) : ''

   ) + lname.substring(0,1);

           nickname += String.valueOf(Crypto.getRandomInteger()).substring(1,7);

             u.CommunityNickname = nickname;

             System.debug('creating user');

             // Creating portal user.

             // Passing in null account ID forces the system to read this from the

   network setting (set using Experience Workspaces).

             String userId = Site.createPortalUser(u, null, password);

             // Setting consent selection values.

             // For this, GDPR (Individual and Consent Management) needs to be enabled

    in the org.

             Individual ind = new Individual();

             ind.LastName = lname;

             ind.HasOptedOutSolicit = !hasOptedSolicit;

             ind.HasOptedOutTracking = !hasOptedTracking;

```


### Using Components Create Custom Search and Profile Menu Components for

Experience Builder

```
             insert(ind);

             // Other contact information can be updated here.

             Contact contact = new Contact();

             contact.Id = u.ContactId;

             contact.IndividualId = ind.Id;

             update(contact);

             // return login url.

             if (userId != null && password != null && password.length() > 1) {

              ApexPages.PageReference lgn = Site.login(username, password, startUrl);

               return lgn.getUrl();

             }

           }

           catch (Exception ex) {

             Database.rollback(sp);

             System.debug(ex.getMessage());

             return null;

           }

           return null;

        }

   }

   Collapse

   }

```

SEE ALSO:

_Salesforce Help_ [: Allow Guest Users to Access Flows](https://help.salesforce.com/HTViewHelpDoc?id=rss_flow_guestuser.htm&language=en_US)

### Create Custom Search and Profile Menu Components for Experience Builder

Create custom components to replace the Customer Service template’s standard Profile Header and Search & Post Publisher components
in Experience Builder.

```
  forceCommunity:profileMenuInterface

```

Add the `forceCommunity:profileMenuInterface` interface to an Aura component to allow it to be used as a custom
profile menu component for the Customer Service site template. After you create a custom profile menu component, admins can select
it in Experience Builder in **Settings**     - **Theme** to replace the template’s standard Profile Header component.

Here’s the sample code for a simple profile menu component.

```
   <aura:component implements="forceCommunity:profileMenuInterface" access="global">

      <aura:attribute name="options" type="String[]" default="['Option 1', 'Option 2']"/>

      <lightning:avatar variant="circle" src="" fallbackIconName="standard:person_account"

   alternativeText="Account User"/>

      <lightning:buttonMenu alternativeText="Profile Menu" variant="container"

   iconName="utility:connected_apps">

        <aura:iteration items="{!v.options}" var="itemLabel">

           <lightning:menuItem label="{!itemLabel}" />

        </aura:iteration>

```


### Using Components Create Custom Content Layout Components for Experience

Builder

```
      </lightning:buttonMenu>

   </aura:component>

  forceCommunity:searchInterface

```

Add the `forceCommunity:searchInterface` interface to an Aura component to allow it to be used as a custom search
component for the Customer Service site template. After you create a custom search component, admins can select it in Experience
Builder in **Settings**     - **Theme** to replace the template’s standard Search & Post Publisher component.

Here’s the sample code for a simple search component.

```
   <aura:component implements="forceCommunity:searchInterface" access="global">

      <div onkeyup="{! c.handleKeyUp }">

      <lightning:input

           aura:id="search-input"

           label="Search"

           type="search"

           variant="label-hidden"

        />

      </div>

   </aura:component>

   ({

      handleKeyUp: function (cmp, evt) {

        var isEnterKey = evt.keyCode === 13;

        if (isEnterKey) {

           var queryTerm = cmp.find('search-input').get('v.value');

           //do something with user input

        }

      }

   })

```

SEE ALSO:

Create Custom Theme Layout Components for Experience Builder

_Salesforce Help_ [: Custom Theme Layouts and Theme Layout Types](https://help.salesforce.com/HTViewHelpDoc?id=community_builder_theme.htm&language=en_US)

### Create Custom Content Layout Components for Experience Builder

Experience Builder includes several ready-to-use layouts that define the content regions of your page, such as a two-column layout with
a 2:1 ratio. However, if you need a layout that’s customized for your site, create a custom content layout component to use when building
new pages in Experience Builder. You can also update the content layout of the default pages that come with your site template.

When you create a custom content layout component in the Developer Console, it appears in Experience Builder in the New Page and
the Change Layout dialog boxes.

1. Add a New Interface to Your Content Layout Component

To appear in the New Page and the Change Layout dialog boxes in Experience Builder, a content layout component must implement
the `forceCommunity:layout` interface.


Using Components Create Custom Content Layout Components for Experience
Builder

Here’s the sample code for a simple two-column content layout.

```
   <aura:component implements="forceCommunity:layout" description=”Custom Content Layout”

   access="global">

     <aura:attribute name="column1" type="Aura.Component[]" required="false"></aura:attribute>

     <aura:attribute name="column2" type="Aura.Component[]" required="false"></aura:attribute>

      <div class="container">

        <div class="contentPanel">

           <div class="left">

             {!v.column1}

           </div>

           <div class="right">

             {!v.column2}

           </div>

        </div>

      </div>

   </aura:component>

```

Note: Mark your resources, such as a component, with `access="global"` to make the resource usable outside of your own
org. For example, if you want a component to be usable in an installed package or by a Lightning App Builder user or a Experience
Builder user in another org.

You can also create documentation for a component, event, or interface marked `access="global"` . This documentation is
automatically displayed in the Component Library of an org that uses or installs your package.

2. Add a CSS Resource to Your Component Bundle

Next, add a CSS resource to style the content layout as needed.

Here’s the sample CSS for our simple two-column content layout.

```
   .THIS .contentPanel:before,

   .THIS .contentPanel:after {

      content: " ";

      display: table;

   }

   .THIS .contentPanel:after {

      clear: both;

   }

   .THIS .left {

      float: left;

      width: 50%;

   }

   .THIS .right {

      float: right;

      width: 50%;

   }

```

CSS resources must be named _`componentName`_ `.css` .


## Using Components Use Aura Components with Flows

3. Optional: Add an SVG Resource to Your Component Bundle

You can include an SVG resource in your component bundle to define a custom icon for the content layout component when it appears
in the Experience Builder.

The recommended image size for a content layout component in Experience Builder is 170px by 170px. However, if the image has
different dimensions, Experience Builder scales the image to fit.

SVG resources must be named _`componentName`_ `.svg` .

SEE ALSO:

Component Bundles

Standard Design Tokens for Experience Builder Sites

## Use Aura Components with Flows

Customize the look-and-feel and functionality of your flows by adding Lightning components to them. Or wrap a flow in an Aura
component to configure the flow at runtime, such as to control how a paused flow is resumed.

IN THIS SECTION:

### Considerations for Configuring Components for Flows

Before you configure an Aura component for a flow, determine whether it should be available in flow screens or as flow actions and
understand how to map data types between a flow and an Aura component. Then review some considerations for defining attributes
and how components behave in flows at runtime.

Customize Flow Screens Using Aura Components
To customize the look and feel of your flow screen, build a custom Aura component. Configure the component and its design
resource so that they’re compatible with flow screens. Then in Flow Builder, add a screen component to the screen.

Create Flow Local Actions Using Aura Components
To execute client-side logic in your flow, build or modify custom Aura components to use as local actions in flows. For example, get
data from third-party systems without going through the Salesforce server, or open a URL in another browser tab. Once you configure
the Aura component’s markup, client-side controller, and design resource, it’s available in Flow Builder as a Core Action element.

Embed a Flow in a Custom Aura Component
Once you embed a flow in an Aura component, use JavaScript and Apex code to configure the flow at run time. For example, pass
values into the flow or to control what happens when the flow finishes. `lightning:flow` supports only screen flows and
autolaunched flows.

Display Flow Stages with an Aura Component
If you’ve added stages to your flow, display them to flow users with an Aura component, such as
`lightning:progressindicator` .

### Considerations for Configuring Components for Flows

Before you configure an Aura component for a flow, determine whether it should be available in flow screens or as flow actions and
understand how to map data types between a flow and an Aura component. Then review some considerations for defining attributes
and how components behave in flows at runtime.

**•** [Lightning components in flows must comply with Lightning Locker restrictions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/security_code.htm)


Using Components Considerations for Configuring Components for Flows

**•** [Flows that include Lightning components are supported only in Lightning runtime.](https://help.salesforce.com/articleView?id=flow_distribute_runtime.htm&language=en_US)

IN THIS SECTION:

#### Flow Screen Components vs. Flow Action Components

You can make your Aura component available in flow screens or as a flow action. When choosing between the flow interfaces,
consider what purpose the component serves in the flow.

#### Which Custom Lightning Component Attribute Types Are Supported in Flows?

Not all custom Lightning component data types are supported in flows. You can map only these types and their associated collection
types between flows and custom Lightning components.

Design Attribute Considerations for Flow Screen Components and Local Actions
To expose an attribute in Flow Builder, define a corresponding `design:attribute` in the component bundle's design resource.
Keep these guidelines in mind when defining design attributes for flows.

Runtime Considerations for Flows That Include Aura Components
Depending on where you run your flow, Aura components may look or behave differently than expected. The flow runtime app
that's used for some distribution methods doesn't include all the necessary resources from the Lightning Component framework.
When a flow is run from Flow Builder or a direct flow URL (https://yourDomain.my.salesforce.com/flow/MyFlowName), `force`
and `lightning` events aren’t handled.

SEE ALSO:

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

_Component Library_ [: lightning:availableForFlowActions Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowActions/documentation)

_[Security for Lightning Components:](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/locker_intro.html)_ Lightning Locker

#### Flow Screen Components vs. Flow Action Components

You can make your Aura component available in flow screens or as a flow action. When choosing between the flow interfaces, consider
what purpose the component serves in the flow.

**For this use case...** **Create a...**

Provide UI for the user to interact with Flow screen component

Update the screen in real time Flow screen component

Prevent the flow from continuing until the component is done Flow action component

Make direct data queries to on-premise or private cloud data Flow action component

SEE ALSO:

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

_Component Library_ [: lightning:availableForFlowActions Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowActions/documentation)

#### Which Custom Lightning Component Attribute Types Are Supported in Flows?

Not all custom Lightning component data types are supported in flows. You can map only these types and their associated collection
types between flows and custom Lightning components.


Using Components Considerations for Configuring Components for Flows

**Flow Data Type**

**Lightning** **Valid Values**
**Component**
**Attribute Type**

Apex Custom Apex Class

Apex classes that define `@AuraEnabled` fields. Supported data types in an Apex class
are Boolean, Integer, Long, Decimal, Double, Date, DateTime, and String. Single values as
well as Lists are supported for each data type.

Boolean Boolean

**•** True values: _`true`_, _`1`_, or equivalent expression

**•** False values: _`false`_, _`0`_, or equivalent expression

Currency Number Numeric value or equivalent expression

Date Date _`"YYYY-MM-DD"`_ or equivalent expression

Date/Time (API DateTime _`"YYYY-MM-DDThh:mm:ssZ"`_ or equivalent expression
name is DateTime)

Number Number Numeric value or equivalent expression

Multi-Select Picklist String

(API name is
Multi-Select Picklist.)

String value or equivalent expression using this format:

```
"Blue; Green; Yellow"

```

Picklist String String value or equivalent expression

Record, with a
specified object

(API name is
SObject.)

The API name of the
specified object,
such as Account or
Case

Map of key-value pairs or equivalent expression.

Flow record values map only to attributes whose type is the specific object. For example,
an account record variable can be mapped only to an attribute whose type is Account.
Flow data types aren’t compatible with attributes whose type is Object.

Text String String value or equivalent expression

(API name is Text.)

Time Time "hh:mm:ss.SSSZ" or equivalent expression

SEE ALSO:

_Component Library_ [: lightning:flow Component](https://developer.salesforce.com/docs/component-library/bundle/lightning:flow/documentation)

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

_Component Library_ [: lightning:availableForFlowActions Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowActions/documentation)

#### Design Attribute Considerations for Flow Screen Components and Local Actions

To expose an attribute in Flow Builder, define a corresponding `design:attribute` in the component bundle's design resource.
Keep these guidelines in mind when defining design attributes for flows.

**Supported Attributes on** **`design:attribute`** **Nodes**
In a `design:attribute` node, Flow Builder supports only the `name`, `label`, `description`, and `default` attributes.
The other attributes, like `min` and `max`, are ignored.


Using Components Considerations for Configuring Components for Flows

For example, for this design attribute definition, Flow Builder ignores required and placeholder.

```
     <design:attribute name="greeting" label="Greeting" placeholder="Hello" required="true"/>

```

**Calculating Minimum and Maximum Values for an Attribute**
To validate min and max lengths for a component attribute, use a flow formula or the component's client-side controller.

**Modifying or Deleting** **`design:attribute`** **Nodes**
If a component’s attribute is referenced in a flow, you can’t change the attribute’s type or remove it from the design resource. This
limitation applies to all flow versions, not just active ones. Remove references to the attribute in all flow versions, and then edit or
delete the attribute in the design resource.

SEE ALSO:

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

_Component Library_ [: lightning:availableForFlowActions Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowActions/documentation)

#### Runtime Considerations for Flows That Include Aura Components

Depending on where you run your flow, Aura components may look or behave differently than expected. The flow runtime app that's
used for some distribution methods doesn't include all the necessary resources from the Lightning Component framework. When a flow
is run from Flow Builder or a direct flow URL (https://yourDomain.my.salesforce.com/flow/MyFlowName), `force` and `lightning`
events aren’t handled.

To verify the behavior of your Aura components, test your flow in a way that handles `force` and `lightning` events, such as
`force:showToast` . You can also add the appropriate event handlers directly to your component.


### Using Components Customize Flow Screens Using Aura Components

SEE ALSO:

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

_Component Library_ [: lightning:availableForFlowActions Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowActions/documentation)

Events Handled in the Salesforce Mobile App and Lightning Experience

### Customize Flow Screens Using Aura Components

To customize the look and feel of your flow screen, build a custom Aura component. Configure the component and its design resource
so that they’re compatible with flow screens. Then in Flow Builder, add a screen component to the screen.

IN THIS SECTION:

#### Configure Components for Flow Screens

Make your custom Aura components available to flow screens in Flow Builder by implementing the
`lightning:availableForFlowScreens` interface.

Control Flow Navigation from an Aura Component
By default, users navigate a flow by clicking standard buttons at the bottom of each screen. The
`lightning:availableForFlowScreens` interface provides two attributes to help you fully customize your screen's
navigation. To figure out which navigation actions are available for the screen, loop through the `availableActions` attribute.
To programmatically trigger one of those actions, call the `navigateFlow` action from your JavaScript controller.

Customize the Flow Header with an Aura Component
To replace the flow header with an Aura component, use the `screenHelpText` parameter from the
`lightning:availableForFlowScreens` interface.

Dynamically Update a Flow Screen with an Aura Component
To conditionally display a field on your screen, build an Aura component that uses `aura:if` to check when parts of the component
should appear.

SEE ALSO:

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

Create Flow Local Actions Using Aura Components

#### Configure Components for Flow Screens

Make your custom Aura components available to flow screens in Flow Builder by implementing the
`lightning:availableForFlowScreens` interface.


Using Components Customize Flow Screens Using Aura Components

Here’s the sample code for a simple “Hello World” component.

```
   <aura:component implements=" lightning:availableForFlowScreens " access="global">

      <aura:attribute name="greeting" type="String" access="global" />

      <aura:attribute name="subject" type="String" access="global" />

      <div style="box">

       <span class="greeting">{!v.greeting}</span>, {!v.subject}!

      </div>

   </aura:component>

```

Note: Mark your resources, such as a component, with `access="global"` to make the resource usable outside of your own
org. For example, you want a component to be usable in an installed package or by a Lightning App Builder user or an Experience
Builder user in another org.

To make an attribute’s value customizable in Flow Builder, add it to the component's design resource. That way, flow admins can pass
values between that attribute and the flow when they configure the screen component.

With this sample design resource, flow admins can customize the values for the “Hello World” component’s attributes.

```
   <design:component label="Hello World">

     <design:attribute name="greeting" label="Greeting" />

     <design:attribute name="subject" label="Subject" />

   </design:component>

```

A design resource describes the design-time behavior of a Lightning component—information that visual tools require to allow adding
the component to a page or app. Adding this resource is similar to adding it for the Lightning App Builder.

When admins reference this component in a flow, they can set each attribute using values from the flow. And they can store each
attribute’s output value in a flow variable.

SEE ALSO:

#### Control Flow Navigation from an Aura Component

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

_[Security for Lightning Components:](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/locker_intro.html)_ Lightning Locker

#### Control Flow Navigation from an Aura Component

By default, users navigate a flow by clicking standard buttons at the bottom of each screen. The
`lightning:availableForFlowScreens` interface provides two attributes to help you fully customize your screen's navigation.
To figure out which navigation actions are available for the screen, loop through the `availableActions` attribute. To
programmatically trigger one of those actions, call the `navigateFlow` action from your JavaScript controller.

When you override the screen's navigation with an Aura component, remember to hide the footer so that the screen has only one
navigation model.

IN THIS SECTION:

Flow Navigation Actions
The `availableActions` attribute lists the valid navigation actions for that screen.


Using Components Customize Flow Screens Using Aura Components

##### Customize the Flow Footer with an Aura Component

To replace the flow footer with an Aura component, use the parameters that the `lightning:availableForFlowScreens`
interface provides. The `availableActions` array lists which actions are available for the screen, and the `navigateFlow`
action lets you invoke one of the available actions.

Build a Custom Navigation Model for Your Flow Screens
Since Aura components have access to a flow screen’s navigation actions, you can fully customize how the user moves between
screens. For example, hide the default navigation buttons and have the flow move to the next screen when the user selects a choice.

SEE ALSO:

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

##### Flow Navigation Actions

The `availableActions` attribute lists the valid navigation actions for that screen.

A screen’s available actions are determined by:

**•** Where in the flow the screen is. For example, Previous isn't supported on the first screen in a flow, Finish is supported for only the
last screen in a flow, and you can never have both Next and Finish.

**•** Whether the flow creator opted to hide any of the actions in the screen's Control Navigation settings. For example, if `Pause` is
de-selected, the Pause action isn't included in availableActions.

Here are the possible actions, their default button label, and what's required for that action to be valid.

**Action** **Button Label** **Description**

`NEXT` Next Navigates to the next screen

`BACK` Previous Navigates to the previous screen

`PAUSE` Pause Saves the interview in its current state to the database, so that the user can resume it later

`RESUME` Resume Resumes a paused interview

`FINISH` Finish Finishes the interview. This action is available only before the final screen in the flow.

SEE ALSO:

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

##### Customize the Flow Footer with an Aura Component

To replace the flow footer with an Aura component, use the parameters that the `lightning:availableForFlowScreens`
interface provides. The `availableActions` array lists which actions are available for the screen, and the `navigateFlow` action
lets you invoke one of the available actions.

By default, the flow footer displays the available actions as standard buttons. Next and Finish use the brand variant style, and Previous
and Pause use the neutral variant. Also, Pause floats left, while the rest of the buttons float right.

Example: This component ( `c:flowFooter` ) customizes the default flow footer in two ways.

**•** It swaps the Pause and Previous buttons, so that Previous floats to the left and Pause floats to the right with Next or Finish.

**•** It changes the label for the Finish button to Done.


Using Components Customize Flow Screens Using Aura Components

`c:flowFooter` **Component**

Since the component implements `lightning:availableForFlowScreens`, it has access to the `availableActions`
attribute, which contains the valid actions for the screen. The declared attributes, like `canPause` and `canBack`, determine
which buttons to display. Those attributes are set by the JavaScript controller when the component initializes.

```
      <aura:component access="global" implements="lightning:availableForFlowScreens">

        <!-- Determine which actions are available -->

        <aura:attribute name="canPause" type="Boolean" />

        <aura:attribute name="canBack" type="Boolean" />

        <aura:attribute name="canNext" type="Boolean" />

        <aura:attribute name="canFinish" type="Boolean" />

        <aura:handler name="init" value="{!this}" action="{!c.init}" />

        <div aura:id="actionButtonBar" class="slds-clearfix slds-p-top_medium">

         <!-- If Previous is available, display to the left -->

         <div class="slds-float_left">

           <aura:if isTrue="{!v.canBack}">

             <lightning:button aura:id="BACK" label="Previous"

               variant="neutral" onclick="{!c.onButtonPressed}" />

           </aura:if>

         </div>

         <div class="slds-float_right">

           <!-- If Pause, Next, or Finish are available, display to the right -->

           <aura:if isTrue="{!v.canPause}">

             <lightning:button aura:id="PAUSE" label="Pause"

               variant="neutral" onclick="{!c.onButtonPressed}" />

           </aura:if>

           <aura:if isTrue="{!v.canNext}">

             <lightning:button aura:id="NEXT" label="Next"

               variant="brand" onclick="{!c.onButtonPressed}" />

           </aura:if>

           <aura:if isTrue="{!v.canFinish}">

             <lightning:button aura:id="FINISH" label="Done"

               variant="brand" onclick="{!c.onButtonPressed}" />

           </aura:if>

         </div>

        </div>

      </aura:component>

```

`c:flowFooter` **Controller**

The `init` function loops through the screen's available actions and determines which buttons the component should show.
When the user clicks one of the buttons in the footer, the `onButtonPressed` function calls the `navigateFlow` action to
perform that action.

```
      ({

        init : function(cmp, event, helper) {

         // Figure out which buttons to display

```


Using Components Customize Flow Screens Using Aura Components

```
         var availableActions = cmp.get('v.availableActions');

         for (var i = 0; i < availableActions.length; i++) {

           if (availableActions[i] == "PAUSE") {

             cmp.set("v.canPause", true);

           } else if (availableActions[i] == "BACK") {

             cmp.set("v.canBack", true);

           } else if (availableActions[i] == "NEXT") {

             cmp.set("v.canNext", true);

           } else if (availableActions[i] == "FINISH") {

             cmp.set("v.canFinish", true);

           }

         }

        },

        onButtonPressed: function(cmp, event, helper) {

         // Figure out which action was called

         var actionClicked = event.getSource().getLocalId();

         // Fire that action

         var navigate = cmp.get('v.navigateFlow');

         navigate(actionClicked);

        }

      })

```

Control Screen Navigation from a Child Component

If you're using a child component to handle the screen's navigation, pass the `availableActions` attribute down from the parent
component – the one that implements `lightning:availableForFlowScreens` . You can pass the available actions by
setting the child component's attributes, but you can’t pass the action. Instead, use a custom event to send the selected action up to
the parent component.

Example: **`c:navigateFlow`** **Event**

Create an event with an action attribute, so that you can pass the selected action into the event.

```
      <aura:event type="APPLICATION" >

        <aura:attribute name="action" type="String"/>

      </aura:event>

```

`c:flowFooter` **Component**

In your component, before the handler:

**•** Define an attribute to pass the screen's available actions from the parent component

**•** Register an event to pass the navigateFlow action to the parent component

```
      <aura:attribute name="availableActions" type="String[]" />

      <aura:registerEvent name="navigateFlowEvent" type="c:navigateFlow"/>

```

`c:flowFooter` **Controller**

Since `navigateFlow` is only available in the parent component, the `onButtonPressed` function fails. Update the
`onButtonPressed` function so that it fires `navigateFlowEvent` instead.

```
      onButtonPressed: function(cmp, event, helper) {

        // Figure out which action was called

        var actionClicked = event.getSource().getLocalId();

```


Using Components Customize Flow Screens Using Aura Components

```
        // Call that action

        var navigate = cmp.getEvent("navigateFlowEvent");

        navigate.setParam("action", actionClicked);

        navigate.fire();

      }

```

`c:flowParent` **Component**

In the parent component's markup, pass `availableActions` into the child component's `availableActions` attribute
and the `handleNavigate` function into the child component's `navigateFlowEvent` event.

```
      <c:flowFooter availableActions="{!v.availableActions}"

        navigateFlowEvent="{!c.handleNavigate}"/>

```

`c:flowParent` **Controller**

When `navigateFlowEvent` fires in the child component, the `handleNavigate` function calls the parent component’s
`navigateFlow` action, using the action selected in the child component.

```
      handleNavigate: function(cmp, event) {

        var navigate = cmp.get("v.navigateFlow");

        navigate(event.getParam("action"));

      }

```

SEE ALSO:

Customize the Flow Header with an Aura Component

Dynamically Update a Flow Screen with an Aura Component

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

##### Build a Custom Navigation Model for Your Flow Screens

Since Aura components have access to a flow screen’s navigation actions, you can fully customize how the user moves between screens.
For example, hide the default navigation buttons and have the flow move to the next screen when the user selects a choice.

Example: This component ( `c:choiceNavigation` ) displays a script and a choice in the form of buttons.


Using Components Customize Flow Screens Using Aura Components

**`c:choiceNavigation`** **Component**

```
      <aura:component implements="lightning:availableForFlowScreens" access="global" >

        <!-- Get the script text from the flow -->

        <aura:attribute name="scriptText" type="String" required="true" />

        <!-- Pass the value of the selected option back to the flow -->

        <aura:attribute name="value" type="String" />

        <!-- Display the script to guide the agent's call -->

        <div class="script-container">

         <div class="slds-card__header slds-grid slds-p-bottom_small slds-m-bottom_none">

           <div class="slds-media slds-media_center slds-has-flexi-truncate" >

             <div class="slds-media__figure slds-align-top">

               <h2><lightning:icon iconName="utility:quotation_marks"

                 title="Suggested script" /></h2>

             </div>

             <div class="slds-media__body">

               <ui:outputRichText class="script" value="{!v.scriptText}"/>

             </div>

           </div>

         </div>

        </div>

        <!-- Buttons for the agent to click, according to the customer’s response -->

        <div class="slds-p-top_large slds-p-bottom_large">

         <p><lightning:formattedText value="Customer Response"

           class="slds-text-body_small" /></p>

         <lightning:buttongroup >

           <lightning:button label="Yes" aura:id="Participate_Yes"

             variant="neutral" onclick="{!c.handleChange}"/>

           <lightning:button label="No" aura:id="Participate_No"

             variant="neutral" onclick="{!c.handleChange}"/>

         </lightning:buttongroup>

        </div>

      </aura:component>

```

**`c:choiceNavigation`** **Design**

The design resource includes the `scriptText` attribute, so you can set the script from the flow.

```
      <design:component>

        <design:attribute name="scriptText" label="Script Text"

         description="What the agent should say to the customer" />

      </design:component>

```

**`c:choiceNavigation`** **Style**

```
      .THIS.script-container {

        border: t(borderWidthThick) solid t(colorBorderBrand);

        border-radius: t(borderRadiusMedium);

      }

      .THIS .script {

        font-size: 1.125rem; /*t(fontSizeTextLarge)*/

        font-weight: t(fontWeightRegular);

```


Using Components Customize Flow Screens Using Aura Components

```
        line-height: t(lineHeightHeading);

      }

```

**`c:choiceNavigation`** **Controller**

When the user clicks either of the buttons, the JavaScript controller calls `navigateFlow(“NEXT”)`, which is the equivalent
of the user clicking **Next** .

```
      ({

        handleChange : function(component, event, helper) {

         // When an option is selected, navigate to the next screen

         var response = event.getSource().getLocalId();

         component.set("v.value", response);

         var navigate = component.get("v.navigateFlow");

         navigate("NEXT");

        }

      })

     defaultTokens.tokens

```

The script in `c:choiceNavigation` uses tokens to stay in sync with the Salesforce Lightning Design System styles.

```
      <aura:tokens extends="force:base" >

      </aura:tokens>

```

SEE ALSO:

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

#### Customize the Flow Header with an Aura Component

To replace the flow header with an Aura component, use the `screenHelpText` parameter from the
`lightning:availableForFlowScreens` interface.

By default, the flow header includes the title of the flow that's running and a button, where users can access screen-level help.

Example: Instead of displaying the flow title and the help button, this component ( `c:flowHeader` ) displays the company
logo and the help button. The help text appears in a tooltip when the user hovers, instead of in a modal when the user clicks.

`c:flowHeader` **Component**

Since the component implements `lightning:availableForFlowScreens`, it has access to the `screenHelpText`
attribute, which contains the screen's help text if it has any.

```
      <aura:component access="global" implements="lightning:availableForFlowScreens">

        <div class="slds-p-top_medium slds-clearfix">

         <div class="slds-float_left">

           <!-- Display company logo -->

```


Using Components Customize Flow Screens Using Aura Components

```
           <h2><img src="{!$Resource.Logo}" alt="A.W. Computing logo"/></h2>

         </div>

         <div class="slds-float_right" style="position:relative;">

           <aura:if isTrue="{!v.screenHelpText ne null}">

             <!-- If the screen has help text, display an info icon in the header.

                On hover, display the screen's help text -->

             <lightning:helptext content="{!v.screenHelpText}" />

           </aura:if>

         </div>

        </div>

      </aura:component>

```

SEE ALSO:

Customize the Flow Footer with an Aura Component

#### Dynamically Update a Flow Screen with an Aura Component

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

#### Dynamically Update a Flow Screen with an Aura Component

To conditionally display a field on your screen, build an Aura component that uses `aura:if` to check when parts of the component
should appear.

Example: This component ( `c:flowDynamicScreen` ) displays a custom script component and a group of radio buttons.
The component gets the contact's existing phone number from the flow, and uses that value to fill in the script.

If the user selects the No radio button, the component displays an input, where the user can enter the new phone number.


Using Components Customize Flow Screens Using Aura Components

`c:flowDynamicScreen` **Component**

```
      <aura:component access="global" implements="lightning:availableForFlowScreens">

        <aura:attribute name="oldPhone" type="String" />

        <aura:attribute name="newPhone" type="String" />

        <aura:attribute name="radioOptions" type="List" default="[

         {'label': 'Yes', 'value': 'false'},

         {'label': 'No', 'value': 'true'} ]"/>

        <aura:attribute name="radioValue" type="Boolean" />

        <!-- Displays script to guide the agent's call -->

        <div class="script-container">

         <div class="slds-card__header slds-grid slds-p-bottom_small slds-m-bottom_none">

           <div class="slds-media slds-media_center slds-has-flexi-truncate" >

             <div class="slds-media__figure slds-align-top">

               <h2><lightning:icon iconName="utility:quotation_marks"

                 title="Suggested script" /></h2>

             </div>

             <div class="slds-media__body">

               <!-- Inserts the user’s current number, pulled from the flow, into the

      script -->

               <ui:outputRichText class="script" value="{!'Let me verify your phone

      number.

                 Is ' + v.oldPhone + ' still a good phone number to reach you?'}"/>

             </div>

           </div>

         </div>

        </div>

        <!-- Displays a radio button group to enter the customer’s response -->

        <div class="slds-p-top_medium slds-p-bottom_medium">

         <lightning:radioGroup aura:id="rbg_correct" name="rbg_correct"

           label="Is the phone number correct?"

           options="{! v.radioOptions }" value="{! v.radioValue }" />

         <!-- If the current number is wrong,

           displays a field to enter the correct number -->

         <aura:if isTrue="{!v.radioValue}">

           <lightning:input type="tel" aura:id="phone_updated" label="Phone"

             onblur="{!c.handleNewPhone}" class="slds-p-top_small"/>

         </aura:if>

        </div>

      </aura:component>

```

**`c:flowDynamicScreen`** **Style**

```
      .THIS.script-container {

        border: t(borderWidthThick) solid t(colorBorderBrand);

        border-radius: t(borderRadiusMedium);

      }

      .THIS .script {

        font-size: 1.125rem; /*t(fontSizeTextLarge)*/

        font-weight: t(fontWeightRegular);

        line-height: t(lineHeightHeading);

      }

```


### Using Components Create Flow Local Actions Using Aura Components

`c:flowDynamicScreen` **Controller**

When the user tabs out, or otherwise removes focus from the Phone input, the controller sets the `newPhone` attribute to the
input value, so that you can reference the new number in the flow.

```
      ({

        handleNewPhone: function(cmp, event, helper) {

         cmp.set("v.newPhone", cmp.find('phone_updated').get('v.value'));

        }

      })

     defaultTokens.tokens

```

The script in `c:flowDynamicScreen` uses tokens to stay in sync with the Salesforce Lightning Design System styles.

```
      <aura:tokens extends="force:base" >

      </aura:tokens>

```

SEE ALSO:

Customize the Flow Header with an Aura Component

Customize the Flow Footer with an Aura Component

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

### Create Flow Local Actions Using Aura Components

To execute client-side logic in your flow, build or modify custom Aura components to use as local actions in flows. For example, get data
from third-party systems without going through the Salesforce server, or open a URL in another browser tab. Once you configure the
Aura component’s markup, client-side controller, and design resource, it’s available in Flow Builder as a Core Action element.

**•** [Lightning components in flows must comply with Lightning Locker restrictions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/security_code.htm)

**•** [Flows that include Lightning components are supported only in Lightning runtime.](https://help.salesforce.com/articleView?id=flow_distribute_runtime.htm&language=en_US)

**•** Lightning components require a browser context to run, so flow action components are supported only in screen flows.

Example: Here’s a sample “c:helloWorld” component and its client-side controller, which triggers a JavaScript alert that says
`Hello, World` . In Flow Builder, local actions are available from the Core Action element.

```
      <aura:component implements="lightning:availableForFlowActions" access="global">

        <aura:attribute name="greeting" type="String" default="Hello" access="global" />

        <aura:attribute name="subject" type="String" default="World" access="global" />

      </aura:component>

      ({

        // When a flow executes this component, it calls the invoke method

        invoke : function(component, event, helper) {

         alert(component.get("v.greeting") + ", " + component.get("v.subject"));

        }

      })

```


Using Components Create Flow Local Actions Using Aura Components

IN THIS SECTION:

#### Configure the Component Markup and Design Resource for a Flow Action

Make your custom Aura components available as flow local actions by implementing the
`lightning:availableForFlowActions` interface.

Configure the Client-Side Controller for a Flow Local Action
When a component is executed as a flow local action, the flow calls the `invoke` method in the client-side controller. To run the
code asynchronously in your client-side controller, such as when you're making an XML HTTP request (XHR), return a Promise. When
the method finishes or the Promise is fulfilled, control is returned back to the flow.

Cancel an Asynchronous Request in a Flow Local Action
If an asynchronous request times out, the flow executes the local action's fault connector and sets `$Flow.FaultMessage` to
the error message. However, the original request isn't automatically canceled. To abort an asynchronous request, use the
`cancelToken` parameter available in the `invoke` method.

SEE ALSO:

_Component Library_ [: lightning:availableForFlowActions Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowActions/documentation)

_[Security for Lightning Components:](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/locker_intro.html)_ Lightning Locker

Customize Flow Screens Using Aura Components

#### Configure the Component Markup and Design Resource for a Flow Action

Make your custom Aura components available as flow local actions by implementing the
`lightning:availableForFlowActions` interface.

Tip: We recommend that you omit markup from local actions. Local actions tend to execute quickly, and any markup you add to
them will likely disappear before the user can make sense of it. If you want to display something to users, check out Customize
Flow Screens Using Aura Components instead.

Here’s sample code for a simple “Hello World” component that sets a couple of attributes.

```
   <aura:component implements=" lightning:availableForFlowActions " access="global">

     <aura:attribute name="greeting" type="String" access="global" />

     <aura:attribute name="subject" type="String" access="global" />

   </aura:component>

```

Note: Mark your resources, such as a component, with `access="global"` to make the resource usable outside of your own
org. For example, you want a component to be usable in an installed package or by a Lightning App Builder user or an Experience
Builder user in another org.

To make an attribute’s value customizable in Flow Builder, add it to the component's design resource. That way, flow admins can pass
values between that attribute and the flow when they configure the corresponding Core Action element.

With this sample design resource, flow admins can customize the values for the “Hello World” component’s attributes.

```
   <design:component>

     <design:attribute name="greeting" label="Greeting" />

     <design:attribute name="subject" label="Subject" />

   </design:component>

```

A design resource describes the design-time behavior of a Lightning component—information that visual tools require to allow adding
the component to a page or app. Adding this resource is similar to adding it for the Lightning App Builder.


Using Components Create Flow Local Actions Using Aura Components

When admins reference this component in a flow, they can pass data between the flow and the Aura component. Use the Set Input
Values tab to set an attribute using values from the flow. Use the Store Output Values tab to store an attribute’s value in a flow variable.

SEE ALSO:

_Component Library_ [: lightning:availableForFlowActions Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowActions/documentation)

#### Configure the Client-Side Controller for a Flow Local Action Configure the Client-Side Controller for a Flow Local Action

When a component is executed as a flow local action, the flow calls the `invoke` method in the client-side controller. To run the code
asynchronously in your client-side controller, such as when you're making an XML HTTP request (XHR), return a Promise. When the
method finishes or the Promise is fulfilled, control is returned back to the flow.

Asynchronous Code

When a Promise is resolved, the next element in the flow is executed. When a Promise is rejected or hits the timeout, the flow takes the
local action's fault connector and sets `$Flow.FaultMessage` to the error message.

By default, the error message is “An error occurred when the elementName element tried to execute the c:myComponent component.”
To customize the error message in `$Flow.FaultMessage`, return it as a new Error object in the `reject()` call.

```
   ({

     invoke : function(component, event, helper) {

       return new Promise(function(resolve, reject) {

         // Do something asynchronously, like get data from

         // an on-premise database

         // Complete the call and return to the flow

         if (/* request was successful */) {

           // Set output values for the appropriate attributes

           resolve();

         } else {

           reject(new Error("My error message")); }

       });

     }

   })

```

Note: If you’re making callouts to an external server, add the external server to the allowlist in your org and enable or configure
CORS in the external server.

Synchronous Code

When the method finishes, the next element in the flow is executed.

```
   ({

     invoke : function(component, event, helper) {

       // Do something synchronously, like open another browser tab

       // with a specified URL

       // Set output values for the appropriate attributes

```


Using Components Create Flow Local Actions Using Aura Components

```
      }

    })

```

SEE ALSO:

_Component Library_ [: lightning:availableForFlowActions Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowActions/documentation)

#### Cancel an Asynchronous Request in a Flow Local Action

Using External JavaScript Libraries

#### Cancel an Asynchronous Request in a Flow Local Action

If an asynchronous request times out, the flow executes the local action's fault connector and sets `$Flow.FaultMessage` to the
error message. However, the original request isn't automatically canceled. To abort an asynchronous request, use the `cancelToken`
parameter available in the `invoke` method.

Note: By default, requests time out after 120 seconds. To override the default, assign a different Integer to the component's
`timeout` attribute.

Example: In this client-side controller, the `invoke` method returns a Promise. When the method has done all it needs to do,
it completes the call and control returns to the flow.

**•** If the request is successful, the method uses `resolve()` to execute the next element in the flow after this action.

**•** If the request isn't successful, it uses `reject()` to execute the local action’s fault connector and sets
`$Flow.FaultMessage` to “My error message”.

**•** If the request takes too long, it uses `cancelToken.promise.then` to abort the request.

```
      ({

        invoke : function(component, event, helper) {

         var cancelToken = event.getParam("arguments").cancelToken;

         return new Promise(function(resolve, reject) {

           var xhttp = new XMLHttpRequest();

           // Do something, like get data from

           // a database behind your firewall

           xhttp.onreadystatechange = $A.getCallback(function() {

             if (/* request was successful */) {

               // Complete the call and return to the flow

               resolve();

             } else {

               reject(new Error("My error message"));

             }

           });

           // If the Promise times out, abort the request and

           // pass set $Flow.FaultMessage to "Request timed out"

           cancelToken.promise.then(function(error) {

             xhttp.abort();

             reject(new Error("Request timed out."));

           });

         });

```


### Using Components Embed a Flow in a Custom Aura Component

```
        }

      })

```

SEE ALSO:

_Component Library_ [: lightning:availableForFlowActions Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowActions/documentation)

Configure the Client-Side Controller for a Flow Local Action

### Embed a Flow in a Custom Aura Component

Once you embed a flow in an Aura component, use JavaScript and Apex code to configure the flow at run time. For example, pass values
into the flow or to control what happens when the flow finishes. `lightning:flow` supports only screen flows and autolaunched
flows.

A _flow_ is an application, built with Flow Builder, that collects, updates, edits, and creates Salesforce information.

To embed a flow in your Aura component, add the `<lightning:flow>` component to it.

```
   <aura:component>

      <aura:handler name="init" value="{!this}" action="{!c.init}" />

      <lightning:flow aura:id="flowData" />

   </aura:component>

   ({

      init : function (component) {

        // Find the component whose aura:id is "flowData"

        var flow = component.find("flowData");

        // In that component, start your flow. Reference the flow's API Name.

        flow.startFlow("myFlow");

      },

   })

```

Note: When a page loads that includes a flow component, such as Lightning App Builder or an active Lightning page, the flow
runs. Make sure that the flow doesn’t perform any actions – such as create or delete records – before the first screen.

IN THIS SECTION:

Reference Flow Output Variable Values in a Wrapper Aura Component
When you embed a flow in an Aura component, you can display or reference the flow’s variable values. Use the `onstatuschange`
action to get values from the flow's output variables. Output variables are returned as an array.

Set Flow Input Variable Values from a Wrapper Aura Component
When you embed a flow in a custom Aura component, give the flow more context by initializing its variables. In the component's
controller, create a list of maps, then pass that list to the startFlow method.

Control a Flow’s Finish Behavior by Wrapping the Flow in a Custom Aura Component
By default, when a flow user clicks **Finish**, a new interview starts and the user sees the first screen of the flow again. By embedding
a flow in a custom Aura component, you can shape what happens when the flow finishes by using the `onstatuschange` action.
To redirect to another page, use one of the `force:navigateTo`       - events such as `force:navigateToObjectHome` or
`force:navigateToUrl` .


Using Components Embed a Flow in a Custom Aura Component

Resume a Flow Interview from an Aura Component
By default, users can resume interviews that they paused from the Paused Interviews component on their home page. To customize
how and where users can resume their interviews, embed the `lightning:flow` component in a custom Aura component. In
your client-side controller, pass the interview ID into the `resumeFlow` method.

SEE ALSO:

_Component Library_ [: lightning:flow Component](https://developer.salesforce.com/docs/component-library/bundle/lightning:flow/documentation)

#### Reference Flow Output Variable Values in a Wrapper Aura Component

When you embed a flow in an Aura component, you can display or reference the flow’s variable values. Use the `onstatuschange`
action to get values from the flow's output variables. Output variables are returned as an array.

Note: The variable must allow output access. If you reference a variable that doesn’t allow output access, attempts to get the
variable are ignored.

Example: This example uses the JavaScript controller to pass the flow's accountName and numberOfEmployees variables into
attributes on the component. Then, the component displays those values in output components.

```
      <aura:component>

        <aura:attribute name="accountName" type="String" />

        <aura:attribute name="numberOfEmployees" type="Decimal" />

        <p><lightning:formattedText value="{!v.accountName}" /></p>

       <p><lightning:formattedNumber style="decimal" value="{!v.numberOfEmployees}" /></p>

        <aura:handler name="init" value="{!this}" action="{!c.init}"/>

        <lightning:flow aura:id="flowData" onstatuschange="{!c.handleStatusChange}" />

      </aura:component>

      ({

        init : function (component) {

         // Find the component whose aura:id is "flowData"

         var flow = component.find("flowData");

         // In that component, start your flow. Reference the flow's API Name.

         flow.startFlow("myFlow");

        },

        handleStatusChange : function (component, event) {

         if(event.getParam("status") === "FINISHED") {

           // Get the output variables and iterate over them

           var outputVariables = event.getParam("outputVariables");

           var outputVar;

           for(var i = 0; i < outputVariables.length; i++) {

             outputVar = outputVariables[i];

             // Pass the values to the component's attributes

             if(outputVar.name === "accountName") {

               component.set("v.accountName", outputVar.value);

             } else {

               component.set("v.numberOfEmployees", outputVar.value);

             }

           }

```


Using Components Embed a Flow in a Custom Aura Component

```
         }

        },

      })

```

SEE ALSO:

_Component Library_ [: lightning:flow Component](https://developer.salesforce.com/docs/component-library/bundle/lightning:flow/documentation)

#### Set Flow Input Variable Values from a Wrapper Aura Component

When you embed a flow in a custom Aura component, give the flow more context by initializing its variables. In the component's
controller, create a list of maps, then pass that list to the startFlow method.

[Tip: We recommend using Lightning web components because they perform better and provide the latest functionality. See Embed](https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-embed-component.html)
[a Flow in a Custom Lightning Web Component.](https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-embed-component.html)

You can set variables only at the beginning of an interview, and the variables you set must allow input access. If you reference a variable
that doesn’t allow input access, attempts to set the variable are ignored.

For each variable you set, provide the variable's `name`, `type`, and `value` . For type, use the API name for the flow data type. For
example, for a record variable use SObject, and for a text variable use String.

```
   {

      name : " varName ",

      type : " flowDataType ",

      value : valueToSet

   },

   {

      name : " varName ",

      type : " flowDataType ",

      value : [ value1, value2 ]

   }, ...

```

Example: This JavaScript controller sets values for a number variable, a date collection variable, and a couple of record variables.
The Record data type in Flow Builder corresponds to SObject here.

```
      ({

        init : function (component) {

         // Find the component whose aura:id is "flowData"

         var flow = component.find("flowData");

         var inputVariables = [

           { name : "numVar", type : "Number", value: 30 },

           { name : "dateColl", type : "String", value: [ "2016-10-27", "2017-08-01" ]

      },

           // Sets values for fields in the account record (sObject) variable. Id uses

           // the value of the component's accountId attribute. Rating uses a string.

           { name : "account", type : "SObject", value: {

              "Id" : component.get("v.accountId"),

              "Rating" : "Warm"

              }

            },

            // Set the contact record (sObject) variable to the value of the

            // component's contact attribute. We're assuming the attribute contains

            // the entire sObject for a contact record.

```


Using Components Embed a Flow in a Custom Aura Component

```
            { name : "contact", type : "SObject", value: component.get("v.contact") }

          ];

          flow.startFlow("myFlow", inputVariables);

        }

      })

```

Example: Here's an example of a component that retrieves the most recently modified account via an Apex controller. The Apex
controller passes the data to the flow's record variable through the JavaScript controller.

```
      <aura:component controller="AccountController" >

        <aura:attribute name="account" type="Account" />

        <aura:handler name="init" value="{!this}" action="{!c.init}"/>

        <lightning:flow aura:id="flowData"/>

      </aura:component>

      public with sharing class AccountController {

        @AuraEnabled

        public static Account getAccount() {

          return [SELECT Id, Name, LastModifiedDate FROM Account

          ORDER BY LastModifiedDate DESC LIMIT 1];

        }

      }

      ({

        init : function (component) {

           // Create action to find an account

           var action = component.get("c.getAccount");

          // Add callback behavior for when response is received

           action.setCallback(this, function(response) {

             var state = response.getState(); if (state === "SUCCESS") {

              // Pass the account data into the component's account attribute

             component.set("v.account", response.getReturnValue());

              // Find the component whose aura:id is "flowData"

             var flow = component.find("flowData");

              // Set the account record (sObject) variable to the value of

              // the component's account attribute.

             var inputVariables = [

               {

                  name : "account",

                  type : "SObject",

                  value: component.get("v.account")

               }

             ];

              // In the component whose aura:id is flowData, start your flow

              // and initialize the account record (sObject) variable.

              // Reference the flow's API name.

             flow.startFlow("myFlow", inputVariables);

           }

             else {

               console.log("Failed to get account date.");

             }

        });

```


Using Components Embed a Flow in a Custom Aura Component

```
           // Send action to be executed

           $A.enqueueAction(action);

        }

      })

```

SEE ALSO:

_Component Library_ [: lightning:flow Component](https://developer.salesforce.com/docs/component-library/bundle/lightning:flow/documentation)

Which Custom Lightning Component Attribute Types Are Supported in Flows?

#### Control a Flow’s Finish Behavior by Wrapping the Flow in a Custom Aura Component

By default, when a flow user clicks **Finish**, a new interview starts and the user sees the first screen of the flow again. By embedding a
flow in a custom Aura component, you can shape what happens when the flow finishes by using the `onstatuschange` action. To
redirect to another page, use one of the `force:navigateTo`     - events such as `force:navigateToObjectHome` or
`force:navigateToUrl` .

Tip: To control a flow’s finish behavior at design time, make your custom Aura component available as a flow action by using the
`lightning:availableForFlowActions` interface. To control what happens when an autolaunched flow finishes,
check for the `FINISHED_SCREEN` status.

```
   <aura:component access="global">

      <aura:handler name="init" value="{!this}" action="{!c.init}" />

      <lightning:flow aura:id="flowData" onstatuschange="{!c.handleStatusChange}" />

   </aura:component>

   // init function here

   handleStatusChange : function (component, event) {

     if(event.getParam("status") === "FINISHED") {

        // Redirect to another page in Salesforce, or

        // Redirect to a page outside of Salesforce, or

        // Show a toast, or...

      }

   }

```

Example: This function redirects the user to a case created in the flow by using the `force:navigateToSObject` event.

```
      handleStatusChange : function (component, event) {

        if(event.getParam("status") === "FINISHED") {

         var outputVariables = event.getParam("outputVariables");

         var outputVar;

         for(var i = 0; i < outputVariables.length; i++) {

           outputVar = outputVariables[i];

           if(outputVar.name === "redirect") {

             var urlEvent = $A.get("e.force:navigateToSObject");

             urlEvent.setParams({

               "recordId": outputVar.value,

               "isredirect": "true"

             });

             urlEvent.fire();

           }

         }

```


Using Components Embed a Flow in a Custom Aura Component

```
        }

      }

```

SEE ALSO:

_Component Library_ [: lightning:flow Component](https://developer.salesforce.com/docs/component-library/bundle/lightning:flow/documentation)

Create Flow Local Actions Using Aura Components

#### Resume a Flow Interview from an Aura Component

By default, users can resume interviews that they paused from the Paused Interviews component on their home page. To customize
how and where users can resume their interviews, embed the `lightning:flow` component in a custom Aura component. In your
client-side controller, pass the interview ID into the `resumeFlow` method.

```
   ({

      init : function (component) {

        // Find the component whose aura:id is "flowData"

        var flow = component.find("flowData");

        // In that component, resume a paused interview. Provide the method with

        // the ID of the interview that you want to resume.

        flow.resumeFlow(" pausedInterviewId ");

      },

   })

```

Example: This example shows how you can resume an interview—or start a new one. When users click **Survey Customer** from
a contact record, the Aura component does one of two things.

**•** If the user has any paused interviews for the Survey Customers flow, it resumes the first one.

**•** If the user doesn’t have any paused interviews for the Survey Customers flow, it starts a new one.

```
      <aura:component controller="InterviewsController">

        <aura:handler name="init" value="{!this}" action="{!c.init}" />

        <lightning:flow aura:id="flowData" />

      </aura:component>

```

This Apex controller gets a list of paused interviews by performing a SOQL query. If nothing is returned from the query,
`getPausedId()` returns a null value, and the component starts a new interview. If at least one interview is returned from the
query, the component resumes the first interview in that list.

```
      public class InterviewsController {

        @AuraEnabled

        public static String getPausedId() {

         // Get the ID of the running user

         String currentUser = UserInfo.getUserId();

         // Find all of that user's paused interviews for the Survey customers flow

         List<FlowInterview> interviews =

           [ SELECT Id FROM FlowInterview

            WHERE CreatedById = :currentUser AND InterviewLabel LIKE '%Survey

      customers%'];

         if (interviews == null || interviews.isEmpty()) {

           return null; // early out

```


### Using Components Display Flow Stages with an Aura Component

```
         }

         // Return the ID for the first interview in the list

         return interviews.get(0).Id;

        }

      }

```

If the Apex controller returned an interview ID, the client-side controller resumes that interview. If the Apex controller returned a
null interview ID, the component starts a new interview.

```
      ({

        init : function (component) {

          //Create request for interview ID

          var action = component.get("c.getPausedId");

          action.setCallback(this, function(response) {

            var interviewId = response.getReturnValue();

            // Find the component whose aura:id is "flowData"

            var flow = component.find("flowData");

            // If an interview ID was returned, resume it in the component

            // whose aura:id is "flowData".

            if ( interviewId !== null ) {

              flow.resumeFlow(interviewID);

            }

            // Otherwise, start a new interview in that component. Reference

            // the flow's API Name.

            else {

              flow.startFlow("Survey_customers");

            }

          });

          //Send request to be enqueued

          $A.enqueueAction(action);

        },

      })

```

SEE ALSO:

_Component Library_ [: lightning:flow Component](https://developer.salesforce.com/docs/component-library/bundle/lightning:flow/documentation)

### Display Flow Stages with an Aura Component

If you’ve added stages to your flow, display them to flow users with an Aura component, such as `lightning:progressindicator` .

To add a progress indicator component to your flow, you have two options:

**•** Wrap the progress indicator with a `lightning:flow` component in a parent component.

```
     <aura:component>

       <lightning:progressindicator/>

       <lightning:flow/>

     </aura:component>

```

**•** Add the progress indicator to your flow screen directly, by using a screen component.


Using Components Display Flow Stages with an Aura Component

IN THIS SECTION:

#### Display Flow Stages by Wrapping a Progress Indicator

If you’re tracking stages in your flow, display them at runtime by creating a custom component that wraps a progress indicator with
the `lightning:flow` component. Use the progress indicator to display the flow’s active stages and current stage, and use the
`lightning:flow` component to display the flow’s screens. To pass the flow’s active stages and current stage to the progress
indicator, use the `lightning:flow` component's `onstatuschange` action.

Display Flow Stages with a Progress Indicator on the Flow Screen
If you track stages in your flow, display them at runtime by adding a custom component to the flow’s screens. Create a progress
indicator component that displays the flow’s active stages and current stage, and make sure that it’s available for flow screens. When
you add the component to each flow screen, pass the `$Flow.ActiveStages` and `$Flow.CurrentStage` global variables
into the component’s attributes.

SEE ALSO:

_Salesforce Help:_ [Show Users Progress Through a Flow with Stages](https://help.salesforce.com/articleView?id=flow_build_stages.htm&language=en_US)

Display Flow Stages with a Progress Indicator on the Flow Screen

#### Display Flow Stages by Wrapping a Progress Indicator

If you’re tracking stages in your flow, display them at runtime by creating a custom component that wraps a progress indicator with the
`lightning:flow` component. Use the progress indicator to display the flow’s active stages and current stage, and use the
`lightning:flow` component to display the flow’s screens. To pass the flow’s active stages and current stage to the progress
indicator, use the `lightning:flow` component's `onstatuschange` action.

Example: This `c:flowStages_global` component uses `lightning:progressindicator` to display the flow’s
stages and `lightning:flow` to display the flow.

Note: This example only applies to flows that have active stages.

`c:flowStages_global` Component

```
      <aura:component implements="flexipage:availableForAllPageTypes" access="global" >

        <aura:attribute name="currentStage" type="Object"/>

        <aura:attribute name="activeStages" type="Object[]"/>

        <!-- Get flow name from the Lightning App Builder -->

        <aura:attribute name="flowName" type="String"/>

        <aura:handler name="init" value="{!this}" action="{!c.init}"/>

        <article class="slds-card">

         <lightning:progressIndicator aura:id="progressIndicator"

           currentStep="{!v.currentStage.name}" type="path"/>

           <lightning:flow aura:id="flow" onstatuschange="{!c.statusChange}"/>

        </article>

      </aura:component>

```


Using Components Display Flow Stages with an Aura Component

`c:flowStages_global` Design

The design resource includes the `flowName` attribute, so you can specify which flow to start from Lightning App Builder.

```
      <design:component>

        <design:attribute name="flowName" label="Flow Name"/>

      </design:component>

```

`c:flowStages_global` Style

```
      .THIS .slds-path__nav { margin-right: 0; }

      .THIS .slds-path__item:only-child { border-radius: 15rem; }

```

`c:flowStages_global` Controller

The controller uses the `flowName` attribute to determine which flow to start.

Each time a new screen loads, the `onstatuschange` action fires, giving the controller access to a handful of parameters about
the flow. The `currentStage` and `activeStages` parameters return the labels and names of the relevant stages.

When `onstatuschange` fires in this component, it calls the controller's `statusChange` method. That method passes the
flow's `currentStage` and `activeStages` parameters into the component's attributes. For each item in the
`activeStages` attribute, the method adds a `lightning:progressStep` component to the component markup.

```
      ({

        init : function(component, event, helper) {

         var flow = component.find("flow");

         flow.startFlow(component.get("v.flowName"));

        },

        // When each screen loads ...

        statusChange : function(component, event, helper) {

         // don't do anything if the flow doesn't have active stages

         if (!event.getParam("currentStage") || !event.getParam("activeStages")) {

            return;

         }

         // Pass $Flow.ActiveStages into the activeStages attribute

         // and $Flow.CurrentStage into the currentStage attribute

         component.set("v.currentStage", event.getParam("currentStage"));

         component.set("v.activeStages", event.getParam("activeStages"));

         var progressIndicator = component.find("progressIndicator");

         var body = [];

         for(let stage of component.get("v.activeStages")) {

           // For each stage in activeStages...

           $A.createComponent(

             "lightning:progressStep",

             {

               // Create a progress step where label is the

               // stage label and value is the stage name

               "aura:id": "step_" + stage.name,

               "label": stage.label,

               "value": stage.name

             },

             function(newProgressStep, status, errorMessage) {

               //Add the new step to the progress array

```


Using Components Display Flow Stages with an Aura Component

```
               if (status === "SUCCESS") {

               body.push(newProgressStep);

               }

               else if (status === "INCOMPLETE") {

                 // Show offline error

                 console.log("No response from server or client is offline.")

               }

               else if (status === "ERROR") {

                 // Show error message

                 console.log("Error: " + errorMessage);

               }

             }

           );

         }

         progressIndicator.set("v.body", body);

        }

      })

```

SEE ALSO:

_Salesforce Help:_ [Show Users Progress Through a Flow with Stages](https://help.salesforce.com/articleView?id=flow_build_stages.htm&language=en_US)

Display Flow Stages with an Aura Component

_[Aura Component Reference](https://developer.salesforce.com/docs/component-library/bundle/lightning:progressIndicator/documentation)_ : Progress Indicator

_Component Library_ [: lightning:flow Component](https://developer.salesforce.com/docs/component-library/bundle/lightning:flow/documentation)

#### Display Flow Stages with a Progress Indicator on the Flow Screen

If you track stages in your flow, display them at runtime by adding a custom component to the flow’s screens. Create a progress indicator
component that displays the flow’s active stages and current stage, and make sure that it’s available for flow screens. When you add the
component to each flow screen, pass the `$Flow.ActiveStages` and `$Flow.CurrentStage` global variables into the
component’s attributes.

**1.** Create the custom `flowStages` component.

The `flowStages` component uses `lightning:progressindicator` to display the flow’s stages.

```
     <aura:component implements="lightning:availableForFlowScreens">

       <!-- Attributes that store $Flow.ActiveStages and $Flow.CurrentStage -->

       <aura:attribute name="stages" type="String[]"/>

       <aura:attribute name="currentStage" type="String"/>

       <aura:handler name="init" value="{!this}" action="{!c.init}"/>

       <a href="#"/>

       <lightning:progressIndicator

          aura:id="progressIndicator"

          currentStep="{!v.currentStage}"

          type="path"/>

     </aura:component>

```

**2.** Create the design resource for the `flowStages` component.


Using Components Display Flow Stages with an Aura Component

The design resource includes the `stages` and `currentStage` attributes so that they’re available in Flow Builder.

```
     <design:component>

       <design:attribute name="stages" label="Stages" description="what stages are active"/>

       <design:attribute name="currentStage" label="Current Stage" description="the current

      stage"/>

     </design:component>

```

**3.** Create the CSS style resource for the `flowStages` component.

```
     .THIS .slds-path__nav { margin-right: 0; }

     .THIS .slds-path__item:only-child { border-radius: 15rem; }

```

**4.** Create the client-side controller for the `flowStages` component.

For each item in the `stages` attribute, the `init` method adds a `lightning:progressStep` component to the
`flowStages` component markup.

```
     ({

       init : function(component, event, helper) {

         var progressIndicator = component.find('progressIndicator');

         for (let step of component.get('v.stages')) {

          $A.createComponent(

            "lightning:progressStep",

            {

              "aura:id": "step_" + step,

              "label": step,

              "value": step

             },

             function(newProgressStep, status, errorMessage){

               // Add the new step to the progress array

               if (status === "SUCCESS") {

                var body = progressIndicator.get("v.body");

                body.push(newProgressStep);

                progressIndicator.set("v.body", body);

               }

               else if (status === "INCOMPLETE") {

                 // Show offline error

                 console.log("No response from server, or client is offline.")

                }

                else if (status === "ERROR") {

                  // Show error message

                  console.log("Error: " + errorMessage);

                }

             }

            );

         }

       }

     })

```

**5.** Create a flow in Flow Builder.

**a.** From Setup, in the Quick Find box, enter _`Flows`_, and then select **Flows** . Then click **New Flow** .

**b.** Select **Start From Scratch**, and then click **Next** .


Using Components Display Flow Stages with an Aura Component

**c.** Select **Screen Flow** as the flow type, and then click **Create** .

**6.** Configure the stages in your flow.

**a.**

Click the Manager panel icon, and then click **New Resource** . Then select **Stage** .

**b.** Enter a label and order, and then specify whether the stage is active by default.

If you select **Active by default**, the stage is added to `{!$Flow.ActiveStages}` when a flow interview starts.

**7.** Configure the screen elements in your flow.

**a.** Click the Add Element icon on the canvas.

**b.** Select the **Screen** interaction element.

**c.** To the screen, add the custom **flowStages** component. For Current Stage, enter _`{!$Flow.CurrentStage}`_ . For Stages,
enter _`{!$Flow.ActiveStages}`_ . In the Advanced section, select **Manually Assign Variables** .

**8.** Configure the assignment elements in your flow.

**a.** Between each screen element, click the Add Element icon on the canvas.

**b.** Select the **Assignment** logic element.

**c.** Set the `Current Stage` variable equal to the following stage in the flow.

For example, for the assignment element between the screens that contain the first and second stages, set the `Current`
`Stage` equal to _`name_of_second_stage`_ .

**9.** Save your flow.


## Using Components Add Components to Apps

SEE ALSO:

_Salesforce Help:_ [Show Users Progress Through a Flow with Stages](https://help.salesforce.com/articleView?id=flow_build_stages.htm&language=en_US)

Display Flow Stages with an Aura Component

Display Flow Stages with an Aura Component

_Component Library_ [: lightning:availableForFlowScreens Interface](https://developer.salesforce.com/docs/component-library/bundle/lightning:availableForFlowScreens/documentation)

## Add Components to Apps

When you’re ready to add components to your app, first look at the built-in base components that Salesforce provides with the framework.
You can also use these components by extending them or using composition to add them to custom components that you’re building.

Note: For all the base components, see the Lightning Component Library on page 465. The `lightning` namespace includes
many base components that implement visual elements common on web pages.

If you can’t find a base component that meets your requirements, consider these options.

**•** Use design variations on page 121 on base components.

**•** [Apply utility classes or custom CSS classes.](https://www.lightningdesignsystem.com/utilities/alignment/)

**•** Combine smaller base components into a more complex, custom component.

**•** [Create your custom component from Lightning Design System blueprints.](https://www.lightningdesignsystem.com/components/overview/)


## Using Components Integrate Your Custom Apps into the Chatter Publisher

Components are encapsulated and their internals stay private, while their public shape is visible to consumers of the component. This
strong separation gives component authors freedom to change the internal implementation details and insulates component consumers
from those changes.

The public shape of a component is defined by the attributes that can be set and the events that interact with the component. The
shape is essentially the API for developers to interact with the component. To design a new component, think about the attributes that
you want to expose and the events that the component can initiate or respond to.

After you’ve defined the shape of any new components, developers can work on the components in parallel. This approach is useful if
you have a team working on an app.

To add a custom component to your app, see Using the Developer Console on page 4.

SEE ALSO:

Component Composition

Using Object-Oriented Development

Component Attributes

Communicating with Events

## Integrate Your Custom Apps into the Chatter Publisher

Use the Chatter Rich Publisher Apps API to integrate your custom apps into the Chatter publisher. The Rich Publisher Apps API enables
developers to attach any custom payload to a feed item. Rich Publisher Apps uses Lightning components for composition and rendering.
We provide two Lightning interfaces and a Lightning event to assist with integration. You can package your apps and upload them to
AppExchange. An Experience Builder site admin page provides a selector for choosing which five of your apps to add to the Chatter
publisher for that site.

Note: Rich Publisher Apps are available to Experience Builder sites in topics, group, and profile feeds and in direct messages.

Use the `lightning:availableForChatterExtensionComposer` and
`lightning:availableForChatterExtensionRenderer` interfaces with the
`lightning:sendChatterExtensionPayload` event to integrate your custom apps into the Chatter publisher and carry
your apps’ payload into a Chatter feed.

[Note: The payload must be an object.](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/ref_attr_types_object.htm)

Example: **Example of a Custom App Integrated into a Chatter Publisher**

This example shows a Chatter publisher with three custom app integrations. There are icons for a video meeting app (1), an emoji
app (2), and an app for selecting a daily quotation (3).


Using Components Integrate Your Custom Apps into the Chatter Publisher

Example: **Example of a Custom App Payload in a Chatter Feed Post**

This example shows the custom app’s payload included in a Chatter feed.

The next sections describe how we integrated the custom quotation app with the Chatter publisher.


Using Components Integrate Your Custom Apps into the Chatter Publisher

1. Set Up the Composer Component

For the composer component, we created component, controller, helper, and style files.

Here’s the component markup in `quotesCompose.cmp` . In this file, we implement the
`lightning:availableForChatterExtensionComposer` interface.

```
   <aura:component implements="lightning:availableForChatterExtensionComposer">

      <aura:handler name="init" value="{!this}" action="{!c.init}"/>

      <div class="container">

      <span class="quote" aura:id="quote"></span>

        <span class="author" aura:id="author"></span>

        <lightning:button label="Get next Quote" onclick="{!c.getQuote}"/>

      </div>

   </aura:component>

```

Use your controller and helper to initialize the composer component and to get the quote from a source. When you get the quote, fire
the event `sendChatterExtensionPayload` . Firing the event enables the **Add** button so the platform can associate the app’s
payload with the feed item. You can also add a title and description as metadata for the payload. The title and description are shown in
a non-Lightning context, like Salesforce Classic.

```
   getQuote: function(cmp, event, helper) {

      // get quote from the source

      var compEvent = cmp.getEvent("sendChatterExtensionPayload");

      compEvent.setParams({

        "payload" : "<payload object>",

        "extensionTitle" : "<title to use when extension is rendered>",

        "extensionDescription" : "<description to use when extension is rendered>"

      });

      compEvent.fire();

   }

```

Add a CSS resource to your component bundle to style your composition component.

2. Set Up the Renderer Component

For the renderer component, we created component, controller, and style files.

Here’s the component markup in `quotesRender.cmp` . In this file, we implement the
`lightning:availableForChatterExtensionRenderer` interface, which provides the payload as an attribute in the
component.

```
   <aura:component implements="lightning:availableForChatterExtensionRenderer">

      <aura:attribute name="_quote" type="String"/>

      <aura:attribute name="_author" type="String"/>

      <aura:handler name="init" value="{!this}" action="{!c.init}"/>

      <div class="container">

      <span class="quote" aura:id="quote">{!v._quote}</span>

        <span class="author" aura:id="author">--- {!v._author} ---</span>

      </div>

   </aura:component>

```


Using Components Integrate Your Custom Apps into the Chatter Publisher

You have a couple of ways of dealing with the payload. You can use the payload directly in the component `{!v.payload}` . You can
use your controller to parse the payload provided by the `lightning:availableForChatterExtensionRenderer`
interface and set its attributes yourself. Add a CSS resource to your renderer bundle to style your renderer component.

3. Set Up a New ChatterExtension Entity

[After you create these components, open Postman or any tool that can make SOAP and REST API calls. Make sure that you’re using at](https://www.postman.com/downloads/)
[least API version 41.0. Log in to your org, and create a ChatterExtension entity using the Salesforce SOAP API.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_calls_create.htm)

[Provide values for ChatterExtension fields (see ChatterExtension for values and descriptions).](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_chatterextension.htm)

Get the `IconId` [for the file asset. Go to Postman, or your preferred tool, and make a new POST request for creating a file asset with a](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_files_asset.htm)
`fileId` from your org. The filepath is `/services/data/v41.0/connect/files/<fileid>/asset` . Replace the
version number with the current version.

Note: Rich Publisher Apps information is cached, so there can be a 5-minute wait before your app appears in the publisher.

4. Package Your App and Upload It to AppExchange

[The Second-Generation Managed Packaging Developer Guide provides useful information about packaging your apps and publishing](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)
them on AppExchange.

5. Select the Apps to Embed in the Chatter Publisher

An admin page is available in each Experience Builder site for selecting and arranging the apps to show in the Chatter publisher. Select
up to five apps, and arrange them in the order you like. The order you set here controls the order the app icons appear in the publisher.

In your site, go to Experience Workspaces and open the Administration page. Click **Rich Publisher Apps** to open the page.


## Using Components Using Background Utility Items

After you move apps to the Selected Items column and click **Save**, the selected apps appear in the Chatter Publisher.

## Using Background Utility Items

Implement the `lightning:backgroundUtilityItem` interface to create a component that fires and responds to events
without rendering in the utility bar.

Note: Lightning Web Components (LWC) doesn’t currently support working with background utility items.

This component implements `lightning:backgroundUtilityItem` and listens for `lightning:tabCreated` events
when the app loads. The component prevents more than 5 tabs from opening.

```
   <aura:component implements="lightning:backgroundUtilityItem">

      <aura:attribute name="limit" default="5" type="Integer" />

      <aura:handler event="lightning:tabCreated" action="{!c.onTabCreated}" />

      <lightning:workspaceAPI aura:id="workspace" />

   </aura:component>

```

When a tab is created, the event handler calls `onTabCreated` in the component’s controller and checks how many tabs are open.
If the number of tabs is more than 5, the leftmost tab automatically closes.

```
   ({

      onTabCreated: function(cmp) {

        var workspace = cmp.find("workspace");

        var limit = cmp.get("v.limit");

        workspace.getAllTabInfo().then(function (tabInfo) {

           if (tabInfo.length > limit) {

             workspace.closeTab({

               tabId: tabInfo[0].tabId

             });

           }

        });

      }

   })

```


## Using Components Use Lightning Components in Visualforce Pages

Background utility items are added to an app the same way normal utility items are, but they don’t appear in the utility bar. The icon
appears next to background utility items on the utility item list. If you have only background utility items in your utility bar, the utility
bar doesn’t appear in your app. You need at least one non-background utility item in your utility bar for it to appear.

## Use Lightning Components in Visualforce Pages

Add Aura components to your Visualforce pages to combine features that use both solutions. Implement new functionality using Aura
components and then use it with existing Visualforce pages.

Important: Lightning Components for Visualforce is based on Lightning Out (Beta), a powerful and flexible feature you can use
to embed Aura and Lightning web components into almost any web page. When used with Visualforce, some of the details
become simpler. For example, you don’t need to deal with authentication, and you don’t need to configure a Connected App.

[In other ways, using Lightning Components for Visualforce is identical to using Lightning Out. See Use Components Outside](https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out.html)
[Salesforce with Lightning Out (Beta) in the](https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out.html) _Lightning Web Components Developer Guide_ .

There are three steps to add Aura components to a Visualforce page.

**1.** Add the Lightning Components for Visualforce JavaScript library to your Visualforce page using the
`<apex:includeLightning/>` component.

**2.** Create and reference a Lightning Out app that declares your component dependencies.

**3.** Write a JavaScript function that creates the component on the page using `$Lightning.createComponent()` .

Add the Lightning Components for Visualforce JavaScript Library

Add `<apex:includeLightning/>` at the beginning of your page. This component loads the JavaScript file used by Lightning
Components for Visualforce.

Important: The Lightning Components for Visualforce JavaScript library loads from the org that the Visualforce page is in, so your
Lightning Out app must exist in the same org as the Visualforce page.

Create and Reference a Lightning Out App

To use Lightning Components for Visualforce, define component dependencies by referencing a Lightning Out app. This app is globally
accessible and extends `ltng:outApp` . The app declares dependencies on any Lightning component that it uses.

Here’s an example of a Lightning Out app named `lcvfTest.app` . The app uses the `<aura:dependency>` tag to indicate that
it uses the standard Lightning component `lightning:button` .

```
   <aura:application access="GLOBAL" extends="ltng:outApp">

      <aura:dependency resource="lightning:button"/>

   </aura:application>

```

Note: Extending from `ltng:outApp` adds SLDS resources to the page so that your Lightning components can be styled with
the Salesforce Lightning Design System (SLDS). If you don’t want SLDS resources added to the page, extend from
`ltng:outAppUnstyled` instead.

To reference this app on your page, use this JavaScript code, where _`theNamespace`_ is the namespace prefix for the app. That is,
either your org’s namespace or the namespace of the managed package that provides the app.

```
   $Lightning.use(" theNamespace :lcvfTest", function() {});

```


Using Components Use Lightning Components in Visualforce Pages

If the app is defined in your org (that is, not in a managed package), you can use the default “c” namespace instead, as shown in the
next example. If your org doesn’t have a namespace defined, you _must_ use the default namespace.

[For details about creating a Lightning Out app, see Lightning Out Dependencies in the](https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-dependencies.html) _Lightning Web Components Developer Guide_ .

Creating a Component on a Page

Finally, add your top-level component to a page using `$Lightning.createComponent(String type, Object`
`attributes, String domLocator, function callback)` . This function is similar to `$A.createComponent()`,
but it includes an additional parameter, `domLocator`, that specifies the DOM element where you want the component inserted.

Let’s look at a sample Visualforce page that creates a `lightning:button` using the `lcvfTest.app` from the previous example.

```
   <apex:page>

      <apex:includeLightning />

      <div id="lightning" />

      <script>

        $Lightning.use("c:lcvfTest", function() {

           $Lightning.createComponent("lightning:button",

             { label : "Press Me!" },

             "lightning",

             function(cmp) {

               console.log("button was created");

               // do some stuff

             }

           );

        });

      </script>

   </apex:page>

```

The `$Lightning.createComponent()` call creates a button with a “Press Me!” label. The button is inserted in a DOM element
with the ID “lightning”. After the button is added and active on the page, the callback function is invoked and executes a
`console.log()` statement. The callback receives the component created as its only argument. In this simple example, the button
isn't configured to do anything.

Important: You can call `$Lightning.use()` multiple times on a page, but all calls must reference the same Lightning
dependency app.

For details about using `$Lightning.use()` and `$Lightning.createComponent()` [, see Lightning Out Markup in the](https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-markup.html)
_Lightning Web Components Developer Guide_ .

Limitations

If a Visualforce page contains an Aura component, you can’t render the Visualforce page as a PDF.

Browser Third-Party Cookies

Lightning components set cookies in a user’s browser. Because Lightning components and Visualforce are served from different domains,
these cookies are “third-party” cookies.

[You can use several approaches for enabling Lightning components in Visualforce to work with third-party cookies. See Enable Browser](https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-third-party-cookies.html)
[Third-Party Cookies for Lightning Out in the](https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-third-party-cookies.html) _Lightning Web Components Developer Guide_ .


## Using Components Use Aura and Lightning Web Components Outside of

Salesforce with Lightning Out (Beta)

## Use Aura and Lightning Web Components Outside of Salesforce with

Lightning Out (Beta)

To run components outside of Salesforce servers, use Lightning Out, a special type of standalone Aura app. Whether it’s a Node.js app
running on Heroku or a department server inside the firewall, add your components as dependencies to a Lightning Out app. Then run
the Lightning Out app wherever your users are.

Important: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole discretion. Any use of the Beta
[Service is subject to the applicable Beta Services Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

Lightning Out supports both Aura components and Lightning web components. The setup process is the same for both component
frameworks. We recommend using Lightning web components for the most modern, performant, and responsive functionality.

[See Use Components Outside Salesforce with Lightning Out (Beta) in the](https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out.html) _Lightning Web Components Developer Guide_ .

SEE ALSO:

Use Lightning Web Components instead of Aura Components

_Lightning Web Components Developer Guide_ [: Use Components Outside Salesforce with Lightning Out (Beta)](https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out.html)

## Lightning Container

Upload an app developed with a third-party framework as a static resource, and host the content in an Aura component using
`lightning:container` . Use `lightning:container` to use third-party frameworks like AngularJS or React within your
Lightning pages.

The `lightning:container` component hosts content in an iframe. You can implement communication to and from the framed
application, allowing it to interact with the Lightning component. `lightning:container` provides the `message()` method,
which you can use in the JavaScript controller to send messages to the application. In the component, specify a method for handling
messages with the `onmessage` attribute.

IN THIS SECTION:

## Lightning Container Component Limits

Understand the limits of `lightning:container` .

lightning:container NPM Module Reference
Use methods included in the lightning:container NPM module in your JavaScript code to send and receive messages to and from
your custom Aura component.

### Using a Third-Party Framework

`lightning:container` allows you to use an app developed with a third-party framework, such as AngularJS or React, in an Aura
component. Upload the app as a static resource.

Your application must have a launch page, which is specified with the `lightning:container src` attribute. By convention, the
launch page is `index.html`, but you can specify another launch page by adding a manifest file to your static resource. The following


Using Components Using a Third-Party Framework

example shows a simple Aura component that references `myApp`, an app uploaded as a static resource, with a launch page of
`index.html` .

```
   <aura:component>

      <lightning:container src="{!$Resource.myApp + '/index.html'}" />

   </aura:component>

```

The contents of the static resource are up to you. It should include the JavaScript that makes up your app, any associated assets, and a
launch page.

As in other Aura components, you can specify custom attributes. This example references the same static resource, `myApp`, and has
three attributes, `messageToSend`, `messageReceived`, and `error` . Because this component includes
`implements="flexipage:availableForAllPageTypes"`, it can be used in the Lightning App Builder and added to
Lightning pages.

```
   <aura:component access="global" implements="flexipage:availableForAllPageTypes" >

      <aura:attribute access="private" name="messageToSend" type="String" default=""/>

      <aura:attribute access="private" name="messageReceived" type="String" default=""/>

      <aura:attribute access="private" name="error" type="String" default=""/>

      <div>

        <lightning:input name="messageToSend" value="{!v.messageToSend}" label="Message

   to send to React app: "/>

        <lightning:button label="Send" onclick="{!c.sendMessage}"/>

        <br/>

       <lightning:textarea value="{!v.messageReceived}" label="Message received from React

    app: "/>

        <br/>

        <aura:if isTrue="{! !empty(v.error)}">

          <lightning:textarea name="errorTextArea" value="{!v.error}" label="Error: "/>

        </aura:if>

        <lightning:container aura:id="ReactApp"

                     src="{!$Resource.SendReceiveMessages + '/index.html'}"

                     onmessage="{!c.handleMessage}"

                     onerror="{!c.handleError}"/>

      </div>

   </aura:component>

```

The component includes a `lightning:input` element, allowing users to enter a value for `messageToSend` . When a user hits
**Send**, the component calls the controller method `sendMessage` . This component also provides methods for handling messages
and errors.

This snippet doesn’t include the component’s controller or other code, but don’t worry. We’ll dive in, break it down, and explain how to
implement message and error handling as we go in Sending Messages from the Lightning Container Component and Handling Errors
in Your Container.

SEE ALSO:

Lightning Container

Sending Messages from the Lightning Container Component

Handling Errors in Your Container


Using Components Using a Third-Party Framework

#### Sending Messages from the Lightning Container Component

Use the `onmessage` attribute of `lightning:container` to specify a method for handling messages to and from the contents
of the component—that is, the embedded app. The contents of `lightning:container` are wrapped within an iframe, and this
method allows you to communicate across the frame boundary.

This example shows an Aura component that includes `lightning:container` and has three attributes, `messageToSend`,
`messageReceived`, and `error` .

This example uses the same code as the one in Using a Third-Party Framework.

```
   <aura:component access="global" implements="flexipage:availableForAllPageTypes" >

      <aura:attribute access="private" name="messageToSend" type="String" default=""/>

      <aura:attribute access="private" name="messageReceived" type="String" default=""/>

      <aura:attribute access="private" name="error" type="String" default=""/>

      <div>

        <lightning:input name="messageToSend" value="{!v.messageToSend}" label="Message

   to send to React app: "/>

        <lightning:button label="Send" onclick="{!c.sendMessage}"/>

        <br/>

       <lightning:textarea value="{!v.messageReceived}" label="Message received from React

    app: "/>

        <br/>

        <aura:if isTrue="{! !empty(v.error)}">

          <lightning:textarea name="errorTextArea" value="{!v.error}" label="Error: "/>

        </aura:if>

        <lightning:container aura:id="ReactApp"

                     src="{!$Resource.SendReceiveMessages + '/index.html'}"

                     onmessage="{!c.handleMessage}"

                     onerror="{!c.handleError}"/>

      </div>

   </aura:component>

```

`messageToSend` represents a message sent from Salesforce to the framed app, while `messageReceived` represents a message
sent by the app to the Aura component. `lightning:container` includes the required `src` attribute, an `aura:id`, and the
`onmessage` attribute. The `onmessage` attribute specifies the message-handling method in your JavaScript controller, and the
`aura:id` allows that method to reference the component.

This example shows the component’s JavaScript controller.

```
   ({

      sendMessage : function(component, event, helper) {

        var msg = {

           name: "General",

           value: component.get("v.messageToSend")

        };

        component.find("ReactApp").message(msg);

      },

      handleMessage: function(component, message, helper) {

        var payload = message.getParams().payload;

        var name = payload.name;

```


Using Components Using a Third-Party Framework

```
        if (name === "General") {

           var value = payload.value;

           component.set("v.messageReceived", value);

        }

        else if (name === "Foo") {

           // A different response

        }

      },

      handleError: function(component, error, helper) {

        var e = error;

      }

   })

```

This code does a couple of different things. The `sendMessage` action sends a message from the enclosing Aura component to the
embedded app. It creates a variable, `msg`, that has a JSON definition including a `name` and a `value` . This definition of the message
is user-defined—the message’s payload can be a value, a structured JSON response, or something else. The `messageToSend` attribute
of the Aura component populates the `value` of the message. The method then uses the component’s `aura:id` and the `message()`
function to send the message back to the Aura component.

The `handleMessage` method receives a message from the embedded app and handles it appropriately. It takes a component, a
message, and a helper as arguments. The method uses conditional logic to parse the message. If this is the message with the `name`
and `value` we’re expecting, the method sets the Aura component’s `messageReceived` attribute to the `value` of the message.
Although this code only defines one message, the conditional statement allows you to handle different types of message, which are
defined in the `sendMessage` method.

The handler code for sending and receiving messages can be complicated. It helps to understand the flow of a message between the
Aura component, its controller, and the app. The process begins when user enters a message as the `messageToSend` attribute.
When the user clicks **Send**, the component calls `sendMessage` . `sendMessage` defines the message payload and uses the
`message()` method to send it to the app. Within the static resource that defines the app, the specified message handler function
receives the message. Specify the message handling function within your JavaScript code using the lightning-container module’s
`addMessageHandler()` method. See the lightning:container NPM Module Reference for more information.

When `lightning:container` receives a message from the framed app, it calls the component controller’s `handleMessage`
method, as set in the `onmessage` attribute of `lightning:container` . The `handleMessage` method takes the message,
and sets its value as the `messageReceived` attribute. Finally, the component displays `messageReceived` in a
`lightning:textarea` .

This is a simple example of message handling across the container. Because you implement the controller-side code and the functionality
of the app, you can use this functionality for any kind of communication between Salesforce and the app embedded in
`lightning:container` .

Important: Don't send cryptographic secrets like an API key in a message. It's important to keep your API key secure.

SEE ALSO:

Lightning Container

Using a Third-Party Framework

Handling Errors in Your Container


Using Components Using a Third-Party Framework

#### Sending Messages to the Lightning Container Component

Use the methods in the lightning-container NPM module to send messages from the JavaScript code framed by
`lightning:container` .

The Lightning-container NPM module provides methods to send and receive messages between your JavaScript app and the Lightning
[container component. You can see the lightning-container module on the NPM website.](https://www.npmjs.com/package/lightning-container)

Add the lightning-container module as a dependency in your code to implement the messaging framework in your app.

```
   import LCC from 'lightning-container';

```

`lightning-container` must also be listed as a dependency in your app’s `package.json` file.

The code to send a message to `lightning:container` from the app is simple. This code corresponds to the code samples in
Sending Messages from the Lightning Container Component and Handling Errors in Your Container.

```
   sendMessage() {

     LCC.sendMessage({name: "General", value: this.state.messageToSend});

   }

```

This code, part of the static resource, sends a message as an object containing a name and a value, which is user-defined.

When the app receives a message, it’s handled by the function mounted by the `addMessageHandler()` method. In a React app,
functions must be mounted to be part of the document-object model and rendered in the output.

The lightning-container module provides similar methods for defining a function to handle errors in the messaging framework. For more
information, see lightning:container NPM Module Reference

Important: Don't send cryptographic secrets like an API key in a message. It's important to keep your API key secure.

#### Handling Errors in Your Container

Handle errors in Lightning container with a method in your component’s controller.

This example uses the same code as the examples in Using a Third-Party Framework and Sending Messages from the Lightning Container
Component.

In this component, the `onerror` attribute of `lightning:container` specifies `handleError` as the error handling method.
To display the error, the component markup uses a conditional statement, and another attribute, `error`, for holding an error message.

```
   <aura:component access="global" implements="flexipage:availableForAllPageTypes" >

      <aura:attribute access="private" name="messageToSend" type="String" default=""/>

      <aura:attribute access="private" name="messageReceived" type="String" default=""/>

      <aura:attribute access="private" name="error" type="String" default=""/>

      <div>

        <lightning:input name="messageToSend" value="{!v.messageToSend}" label="Message

   to send to React app: "/><lightning:button label="Send" onclick="{!c.sendMessage}"/>

        <br/>

        <lightning:textarea name="messageReceived" value="{!v.messageReceived}"

   label="Message received from React app: "/>

        <br/>

```


Using Components Using a Third-Party Framework

```
        <aura:if isTrue="{! !empty(v.error)}">

           <lightning:textarea name="errorMessage" value="{!v.error}" label="Error: "/>

        </aura:if>

        <lightning:container aura:id="ReactApp"

                     src="{!$Resource.SendReceiveMessages + '/index.html'}"

                     onmessage="{!c.handleMessage}"

                     onerror="{!c.handleError}"/>

      </div>

   </aura:component>

```

This is the component’s controller.

```
   ({

      sendMessage : function(component, event, helper) {

        var msg = {

           name: "General",

           value: component.get("v.messageToSend")

        };

        component.find("ReactApp").message(msg);

      },

      handleMessage: function(component, message, helper) {

        var payload = message.getParams().payload;

        var name = payload.name;

        if (name === "General") {

           var value = payload.value;

           component.set("v.messageReceived", value);

        }

        else if (name === "Foo") {

           // A different response

        }

      },

      handleError: function(component, error, helper) {

        var description = error.getParams().description;

        component.set("v.error", description);

      }

   })

```

If the Lightning container application throws an error, the error handling function sets the `error` attribute. Then, in the component
markup, the conditional expression checks if the error attribute is empty. If it isn’t, the component populates a `lightning:textarea`
element with the error message stored in `error` .

SEE ALSO:

Lightning Container

Using a Third-Party Framework

Sending Messages from the Lightning Container Component


Using Components Using a Third-Party Framework

#### Using Apex Services from Your Container

Use the `lightning-container` NPM module to call Apex methods from your Lightning container component.

To call Apex methods from `lightning:container`, you must set the CSP level to `low` in the `manifest.json` file. A CSP
level of `low` allows the Lightning container component load resources from outside of the Lightning domain.

This is an Aura component that includes a Lightning container component that uses Apex services:

```
   <aura:component access="global" implements="flexipage:availableForAllPageTypes">

      <aura:attribute access="private" name="error" type="String" default=""/>

      <div>

        <aura:if isTrue="{! !empty(v.error)}">

          <lightning:textarea name="errorTextArea" value="{!v.error}" label="Error: "/>

        </aura:if>

        <lightning:container aura:id="ReactApp"

                     src="/ApexController/index.html"

                     onerror="{!c.handleError}"/>

      </div>

   </aura:component>

```

This is the component’s controller:

```
   ({

      handleError: function(component, error, helper) {

        var description = error.getParams().description;

        component.set("v.error", description);

      }

   })

```

There’s not a lot going on in the component’s JavaScript controller—the real action is in the JavaScript app, uploaded as a static resource,
that the Lightning container references.

```
   import React, { Component } from 'react';

   import LCC from "lightning-container";

   import logo from './logo.svg';

   import './App.css';

   class App extends Component {

     callApex() {

      LCC.callApex("lcc1.ApexController.getAccount",

              this.state.name,

              this.handleAccountQueryResponse,

              {escape: true});

     }

     handleAccountQueryResponse(result, event) {

      if (event.status) {

       this.setState({account: result});

      }

      else if (event.type === "exception") {

```


### Using Components Lightning Container Component Limits

```
       console.log(event.message + " : " + event.where);

      }

     }

     render() {

      var account = this.state.account;

      return (

       <div className="App">

        <div className="App-header">

         <img src={logo} className="App-logo" alt="logo" />

         <h2>Welcome to LCC</h2>

        </div>

        <p className="App-intro">

         Account Name: <input type="text" id="accountName" value={this.state.name}

   onChange={e => this.onAccountNameChange(e)}/><br/>

         <input type="submit" value="Call Apex Controller" onClick={this.callApex}/><br/>

         Id: {account.Id}<br/>

         Phone: {account.Phone}<br/>

         Type: {account.Type}<br/>

         Number of Employees: {account.NumberOfEmployees}<br/>

        </p>

       </div>

      );

     }

     constructor(props) {

      super(props);

      this.state = {

       name: "",

       account: {}

      };

      this.handleAccountQueryResponse = this.handleAccountQueryResponse.bind(this);

      this.onAccountNameChange = this.onAccountNameChange.bind(this);

      this.callApex = this.callApex.bind(this);

     }

     onAccountNameChange(e) {

      this.setState({name: e.target.value});

     }

   }

   export default App;

```

The first function, `callApex(),` uses the `LCC.callApex` method to call `getAccount`, an Apex method that gets and displays
an account’s information.

### Lightning Container Component Limits

Understand the limits of `lightning:container` .


Using Components Lightning Container Component Limits

`lightning:container` has known limitations. You might observe performance and scrolling issues associated with the use of
iframes. This component isn’t designed for the multi-page model, and it doesn’t integrate with browser navigation history.

If you navigate away from the page and a `lightning:container` component is on, the component doesn’t automatically
remember its state. The content within the iframe doesn’t use the same offline and caching schemes as the rest of Lightning Experience.

Creating a Lightning app that loads a Lightning container static resource from another namespace is not supported. If you install a
package, your apps should use the custom Lightning components published by that package, not their static resources directly. Any
static resource you use as the `lightning:container src` attribute should have your own namespace.

Previous versions of `lightning:container` allowed developers to specify the Content Security Policy (CSP) of the iframed content.
We removed this functionality for security reasons. The CSP level of all pages is now set to the highest level to provide the greatest
security. Content can only be loaded from secure, approved domains. When `lightning:container` is used in Experience Cloud,
the CSP setting in that Experience Builder site will be respected.

Apps that use `lightning:container` should work with data, not metadata. Don’t use the session key for your app to manage
custom objects or fields. You can use the session key to create and update object records.

Content in `lightning:container` is served from the Lightning container domain and is available in Lightning Experience,
Experience Builder sites, and the Salesforce mobile app. `lightning:container` can’t be used in Lightning pages that aren’t
served from the Lightning domain, such as Visualforce pages or in external apps through Lightning Out.

Important: You can’t access the Salesforce REST API from the app inside of `lightning:container` [. See the Spring ’18](https://help.salesforce.com/articleView?id=release-notes.rn_lc_api_revert_cruc.htm&release=212&type=5&language=en_US)
[Release Notes for details.](https://help.salesforce.com/articleView?id=release-notes.rn_lc_api_revert_cruc.htm&release=212&type=5&language=en_US)

IN THIS SECTION:

#### Lightning Container Component Security Requirements

Ensure that your Lightning container components meet security requirements.

SEE ALSO:

#### Lightning Container

_Salesforce Help:_ [Content Security Policy in Experience Builder Sites](https://help.salesforce.com/articleView?id=networks_security_csp_overview.htm&type=5&language=en_US)

#### Lightning Container Component Security Requirements

Ensure that your Lightning container components meet security requirements.

Namespace Validity

The Lightning container component’s security measures check the validity of its namespaces. Suppose that you develop a

`<lightning:container>` component with the namespace “vendor1.” The static resource’s namespace must also be “vendor1.”
If they don’t match, an error message appears.

```
   <aura:component>

     <lightning:container

      src="{!$Resource.vendor1__resource + '/code_belonging_to_vendor1'}"

      onmessage="{!c.vendor1__handles}"/>

   <aura:component>

```


### Using Components lightning:container NPM Module Reference

Static Resource Content Access

You can’t use raw `<iframe>` elements to access a Lightning container component. The `<lightning:container>` component
enforces this requirement with the query parameter `_CONFIRMATIONTOKEN`, which generates a unique ID for each user session.
The following code isn’t permitted, because the `<iframe>` src attribute doesn’t contain a `_CONFIRMATIONTOKEN` query parameter.

```
   <aura:component>

     <iframe

   src="https://domain--vendor2.container.lightning.com/lcc/123456/vendor2__resource/index.html"/>

   </aura:component>

```

Instead, use the `$Resource` global value provider to build the resource URL for the `<lightning:container>` component.

```
   <aura:component>

     <lightning:container

      src="{!$Resource.vendor2__resource + '/index.html' }"/>

   </aura:component>

```

Distribution Requirements

To upload a package to AppExchange, you must supply all the Lightning container component’s original sources and dependencies.
When you provide minified or transpiled code, you must also include the source files for that code and the source map (.js.map) files for
the minified code.

### lightning:container NPM Module Reference

Use methods included in the lightning:container NPM module in your JavaScript code to send and receive messages to and from your
custom Aura component.

IN THIS SECTION:

#### addErrorHandler()

Mounts an error handling function, to be called when the messaging framework encounters an error.

addMessageHandler()
Mounts a message handling function, used to handle messages sent from the Aura component to the framed JavaScript app.

callApex()
Makes an Apex call.

removeErrorHandler()
Unmounts the error handling function.

removeMessageHandler()
Unmounts the message-handling function.

sendMessage()
Sends a message from the framed JavaScript code to the Aura component.

#### addErrorHandler()

Mounts an error handling function, to be called when the messaging framework encounters an error.


Using Components lightning:container NPM Module Reference

Sample

Used within a JavaScript app uploaded as a static resource and referenced by `lightning:container`, this example mounts a
message error handling function. In a React app, functions must be mounted to be part of the document-object model and rendered
in the output.

```
   componentDidMount() {

     LCC.addErrorHandler(this.onMessageError);

   }

```

Arguments

**Name** **Type** **Description**

`handler: (errorMsg:` function The function that handles error messages encountered in
`string) => void)` the messaging framework.

Response

None.

#### addMessageHandler()

Mounts a message handling function, used to handle messages sent from the Aura component to the framed JavaScript app.

Sample

Used within a JavaScript app uploaded as a static resource and referenced by `lightning:container`, this example mounts a
message handling function. In a React app, functions must be mounted to be part of the document-object model and rendered in the
output.

```
   componentDidMount() {

      LCC.addMessageHandler(this.onMessage);

   }

   onMessage(msg) {

     let name = msg.name;

     if (name === "General") {

      let value = msg.value;

      this.setState({messageReceived: value});

     }

     else if (name === "Foo") {

      // A different response

     }

   }

```


Using Components lightning:container NPM Module Reference

Arguments

**Name** **Type** **Description**

`handler: (userMsg: any)` function The function that handles messages sent from the Aura
`=> void` component.

Response

None.

#### callApex()

Makes an Apex call.

Sample

Used within a JavaScript app uploaded as a static resource and referenced by `lightning:container`, this example calls the Apex
method `getAccount` .

#### `callApex() {`

```
      LCC.callApex("lcc1.ApexController.getAccount",

              this.state.name,

              this.handleAccountQueryResponse,

              {escape: true});

     }

```

Arguments

**Name** **Type** **Description**

`fullyQualifiedApexMethodName` string The name of the Apex method.

`apexMethodParameters` array A JSON array of arguments for the Apex method.

`callbackFunction` function A callback function.

`apexCallConfiguration` array Configuration parameters for the Apex call.

Response

None.

#### removeErrorHandler()

Unmounts the error handling function.

When using React, it’s necessary to unmount functions to remove them from the DOM and perform necessary cleanup.


Using Components lightning:container NPM Module Reference

Sample

Used within a JavaScript app uploaded as a static resource and referenced by `lightning:container`, this example unmounts a
message error handling function. In a React app, functions must be mounted to be part of the document-object model and rendered
in the output.

```
   componentWillUnmount() {

     LCC.removeErrorHandler(this.onMessageError);

   }

```

Arguments

**Name** **Type** **Description**

`handler: (errorMsg:` function The function that handles error messages encountered in
`string) => void)` the messaging framework.

Response

None.

#### removeMessageHandler()

Unmounts the message-handling function.

When using React, it’s necessary to unmount functions to remove them from the DOM and perform necessary cleanup.

Sample

Used within a JavaScript app uploaded as a static resource and referenced by `lightning:container`, this example unmounts a
message handling function.

```
   componentWillUnmount() {

     LCC.removeMessageHandler(this.onMessage);

   }

```

Arguments

**Name** **Type** **Description**

`handler: (userMsg: any)` function The function that handles messages sent from the Aura
`=> void` component.

Response

None.

#### sendMessage()

Sends a message from the framed JavaScript code to the Aura component.


Using Components lightning:container NPM Module Reference

Sample

Used within a JavaScript app uploaded as a static resource and referenced by `lightning:container`, this example sends a
message from the app to `lightning:container` .

```
   sendMessage() {

     LCC.sendMessage({name: "General", value: this.state.messageToSend});

   }

```

Arguments

**Name** **Type** **Description**

`userMsg` any

Response

None.

While the data sent in the message is entirely under your
control, by convention it’s an object with name and value
fields.


# CHAPTER 5 Communicating with Events

In this chapter ... The framework uses event-driven programming. You write handlers that respond to interface events as
they occur. The events may or may not have been triggered by user interaction.

**•** Actions and Events
In the Aura Components programming model, events are fired from JavaScript controller actions. Events

**•** Handling Events with
can contain attributes that can be set before the event is fired and read when the event is handled.
Client-Side
Controllers Events are declared by the `aura:event` tag in a `.evt` resource, and they can have one of two types:
component or application.

**•** Component Events

**•** Application Events

**•** Event Handler
Behavior for Active
Components

**•** Event Handling
Lifecycle

**Component Events**
A component event is fired from an instance of a component. A component event can be handled
by the component that fired the event or by a component in the containment hierarchy that receives
the event.

**Application Events**
Application events follow a traditional publish-subscribe model. An application event is fired from
an instance of a component. All components that provide a handler for the event are notified.

**•** Advanced Events
Example
Note: Always try to use a component event instead of an application event, if possible. Component

**•** Firing Events from events can only be handled by components above them in the containment hierarchy so their
Non-Aura Code
usage is more localized to the components that need to know about them. Application events

**•** Events Best Practices are best used for something that should be handled at the application level, such as navigating

**•** Events Fired During to a specific record. Application events allow communication between components that are in
the Rendering separate parts of the application and have no direct containment relationship.
Lifecycle

**•** Events Handled in
the Salesforce Mobile
App and Lightning
Experience

**•** System Events


## Communicating with Events Actions and Events Actions and Events

The framework uses events to communicate data between components. Events are usually triggered by a user action.

## **Actions**

User interaction with an element on a component or app. User actions trigger events, but events aren’t always explicitly triggered
by user actions. This type of action is _not_ the same as a client-side JavaScript controller, which is sometimes known as a _controller_
_action_ . The following button is wired up to a browser `onclick` event in response to a button click.

```
     <lightning:button label = "Click Me" onclick = "{!c.handleClick}" />

```

Clicking the button invokes the `handleClick` method in the component’s client-side controller.

**Events**
A notification by the browser regarding an action. Browser events are handled by client-side JavaScript controllers, as shown in the
previous example. A browser event is not the same as a framework _component event_ or _application event_, which you can create and
fire in a JavaScript controller to communicate data between components. For example, you can wire up the click event of a checkbox
to a client-side controller, which fires a component event to communicate relevant data to a parent component.

Another type of event, known as a _system event_, is fired automatically by the framework during its lifecycle, such as during component
initialization, change of an attribute value, and rendering. Components can handle a system event by registering the event in the
component markup.

The following diagram describes what happens when a user clicks a button that requires the component to retrieve data from the server.

**1.** User clicks a button or interacts with a component, triggering a browser event. For example, you want to save data from the server
when the button is clicked.

**2.** The button click invokes a client-side JavaScript controller, which provides some custom logic before invoking a helper function.

**3.** The JavaScript controller invokes a helper function. A helper function improves code reuse but it’s optional for this example.

**4.** The helper function calls an Apex controller method and queues the action.

**5.** The Apex method is invoked and data is returned.

**6.** A JavaScript callback function is invoked when the Apex method completes.

**7.** The JavaScript callback function evaluates logic and updates the component’s UI.


## Communicating with Events Handling Events with Client-Side Controllers

**8.** User sees the updated component.

SEE ALSO:

## Handling Events with Client-Side Controllers

Detecting Data Changes with Change Handlers

Calling a Server-Side Action

Events Fired During the Rendering Lifecycle

## Handling Events with Client-Side Controllers

A client-side controller handles events within a component. It’s a JavaScript resource that defines the functions for all of the component’s
actions.

A client-side controller is a JavaScript object in object-literal notation containing a map of name-value pairs. Each name corresponds to
a client-side action. Its value is the function code associated with the action. Client-side controllers are surrounded by parentheses and
curly braces. Separate action handlers with commas (as you would with any JavaScript map).

```
   ({

      myAction : function(cmp, event, helper) {

        // add code for the action

      },

      anotherAction : function(cmp, event, helper) {

        // add code for the action

      }

   })

```

Each action function takes in three parameters:

**1.** `cmp` —The component to which the controller belongs.

**2.** `event` —The event that the action is handling.

**3.** `helper` —The component’s helper, which is optional. A helper contains functions that can be reused by any JavaScript code in
the component bundle.

Creating a Client-Side Controller

A client-side controller is part of the component bundle. It is auto-wired via the naming convention,
_`componentName`_ `Controller.js` .

To create a client-side controller using the Developer Console, click **CONTROLLER** in the sidebar of the component.

Calling Client-Side Controller Actions

The following example component creates two buttons to contrast an HTML button with `<lightning:button>`, which is a
standard Lightning component. Clicking on these buttons updates the `text` component attribute with the specified values.
`target.get("v.label")` refers to the `label` attribute value on the button.


Communicating with Events Handling Events with Client-Side Controllers

**Component source**

```
   <aura:component>

     <aura:attribute name="text" type="String" default="Just a string. Waiting for change."/>

      <input type="button" value="Flawed HTML Button"

        onclick="alert('this will not work')"/>

      <br/>

      <lightning:button label="Framework Button" onclick="{!c.handleClick}"/>

      <br/>

      {!v.text}

   </aura:component>

```

If you know some JavaScript, you might be tempted to write something like the first "Flawed" button because you know that HTML tags
are first-class citizens in the framework. However, the "Flawed" button won't work because arbitrary JavaScript, such as the `alert()`
call, in the component is ignored.

The framework has its own event system. DOM events are mapped to Lightning events, since HTML tags are mapped to Lightning
components.

Any browser DOM element event starting with `on`, such as `onclick` or `onkeypress`, can be wired to a controller action. You can
only wire browser events to controller actions.

The "Framework" button wires the `onclick` attribute in the `<lightning:button>` component to the `handleClick` action
in the controller.

**Client-side controller source**

```
   ({

      handleClick : function(cmp, event) {

        var attributeValue = cmp.get("v.text");

        console.log("current text: " + attributeValue);

        var target = event.getSource();

        cmp.set("v.text", target.get("v.label"));

      }

   })

```

The `handleClick` action uses `event.getSource()` to get the source component that fired this component event. In this
case, the source component is the `<lightning:button>` in the markup.

The code then sets the value of the `text` component attribute to the value of the button’s `label` attribute. The `text` component
attribute is defined in the `<aura:attribute>` tag in the markup.

Tip: Use unique names for client-side and server-side actions in a component. A JavaScript function (client-side action) with the
same name as an Apex method (server-side action ) can lead to hard-to-debug issues. In debug mode, the framework logs a
browser console warning about the clashing client-side and server-side action names.

Handling Framework Events

Handle framework events using actions in client-side component controllers. Framework events for common mouse and keyboard
interactions are available with out-of-the-box components.


## Communicating with Events Component Events

Accessing Component Attributes

In the `handleClick` function, notice that the first argument to every action is the component to which the controller belongs. One
of the most common things you'll want to do with this component is look at and change its attribute values.

`cmp.get("v.` _**`attributeName`**_ `")` returns the value of the _**`attributeName`**_ attribute.

`cmp.set("v.` _**`attributeName`**_ `",` `"attribute value")` sets the value of the _**`attributeName`**_ attribute.

Invoking Another Action in the Controller

To call an action method from another method, put the common code in a helper function and invoke it using
`helper.someFunction(cmp)` .

SEE ALSO:

Sharing JavaScript Code in a Component Bundle

Event Handling Lifecycle

Creating Server-Side Logic with Controllers

## Component Events

A component event is fired from an instance of a component. A component event can be handled by the component that fired the
event or by a component in the containment hierarchy that receives the event.

IN THIS SECTION:

Component Event Propagation
The framework supports _capture_ and _bubble_ phases for the propagation of component events. These phases are similar to DOM
handling patterns and provide an opportunity for interested components to interact with an event and potentially control the
behavior for subsequent handlers.

Create Custom Component Events
Create a custom component event using the `<aura:event>` tag in a `.evt` resource. Events can contain attributes that can
be set before the event is fired and read when the event is handled.

Fire Component Events
Fire a component event to communicate data to another component. A component event can be handled by the component that
fired the event or by a component in the containment hierarchy that receives the event.


### Communicating with Events Component Event Propagation

Handling Component Events
A component event can be handled by the component that fired the event or by a component in the containment hierarchy that
receives the event.

SEE ALSO:

aura:method

Application Events

Handling Events with Client-Side Controllers

Advanced Events Example

What is Inherited?

### Component Event Propagation

The framework supports _capture_ and _bubble_ phases for the propagation of component events. These phases are similar to DOM handling
patterns and provide an opportunity for interested components to interact with an event and potentially control the behavior for
subsequent handlers.

The component that fires an event is known as the source component. The framework allows you to handle the event in different phases.
These phases give you flexibility for how to best process the event for your application.

The phases are:

**Capture**
The event is captured and trickles down from the application root to the source component. The event can be handled by a component
in the containment hierarchy that receives the captured event.

Event handlers are invoked in order from the application root down to the source component that fired the event.

Any registered handler in this phase can stop the event from propagating, at which point no more handlers are called in this phase
or the bubble phase.

**Bubble**
The component that fired the event can handle it. The event then bubbles up from the source component to the application root.
The event can be handled by a component in the containment hierarchy that receives the bubbled event.

Event handlers are invoked in order from the source component that fired the event up to the application root.

Any registered handler in this phase can stop the event from propagating, at which point no more handlers are called in this phase.

Here’s the sequence of component event propagation.

**1. Event fired** —A component event is fired.

**2. Capture phase** —The framework executes the capture phase from the application root to the source component until all components
are traversed. Any handling event can stop propagation by calling `stopPropagation()` on the event.

**3. Bubble phase** —The framework executes the bubble phase from the source component to the application root until all components
are traversed or `stopPropagation()` is called.

SEE ALSO:

_Salesforce Developers Blog:_ [An In-Depth Look at Lightning Component Events](https://developer.salesforce.com/blogs/2017/08/depth-look-lightning-component-events)


### Communicating with Events Create Custom Component Events Create Custom Component Events

Create a custom component event using the `<aura:event>` tag in a `.evt` resource. Events can contain attributes that can be set
before the event is fired and read when the event is handled.

Use `type="COMPONENT"` in the `<aura:event>` tag for a component event. For example, this `c:compEvent` component
event has one attribute with a name of `message` .

```
   <!--c:compEvent-->

   <aura:event type="COMPONENT">

      <!-- Add aura:attribute tags to define event shape.

         One sample attribute here. -->

      <aura:attribute name="message" type="String"/>

   </aura:event>

```

The component that fires an event can set the event’s data. To set the attribute values, call `event.setParam()` or
`event.setParams()` . A parameter name set in the event must match the `name` attribute of an `<aura:attribute>` in the
event. For example, if you fire `c:compEvent`, you could use:

```
   event.setParam("message", "event message here");

```

The component that handles an event can retrieve the event data. To retrieve the attribute value in this event, call
`event.getParam("message")` in the handler’s client-side controller.

### Fire Component Events

Fire a component event to communicate data to another component. A component event can be handled by the component that fired
the event or by a component in the containment hierarchy that receives the event.

Register an Event

A component registers that it may fire an event by using `<aura:registerEvent>` in its markup. For example:

```
   <aura:registerEvent name="sampleComponentEvent" type="c:compEvent"/>

```

We’ll see how the value of the `name` attribute is used for firing and handling events.

Fire an Event

To get a reference to a component event in JavaScript, use `cmp.getEvent("evtName")` where `evtName` matches the `name`
attribute in `<aura:registerEvent>` .

Use `fire()` to fire the event from an instance of a component. For example, in an action function in a client-side controller:

```
   var compEvent = cmp.getEvent("sampleComponentEvent");

   // Optional: set some data for the event (also known as event shape)

   // A parameter’s name must match the name attribute

   // of one of the event’s <aura:attribute> tags

   // compEvent.setParams({"myParam" : myValue });

   compEvent.fire();

```

SEE ALSO:

Fire Application Events


### Communicating with Events Handling Component Events Handling Component Events

A component event can be handled by the component that fired the event or by a component in the containment hierarchy that receives
the event.

Use `<aura:handler>` in the markup of the handler component. For example:

```
   <aura:handler name="sampleComponentEvent" event="c:compEvent"

      action="{!c.handleComponentEvent}"/>

```

The `name` attribute in `<aura:handler>` must match the `name` attribute in the `<aura:registerEvent>` tag in the
component that fires the event.

The `action` attribute of `<aura:handler>` sets the client-side controller action to handle the event.

The `event` attribute specifies the event being handled. The format is _**`namespace`**_ `:` _**`eventName`**_ .

In this example, when the event is fired, the `handleComponentEvent` client-side controller action is called.

Event Handling Phases

Component event handlers are associated with the bubble phase by default. To add a handler for the capture phase instead, use the
`phase` attribute.

```
   <aura:handler name="sampleComponentEvent" event="ns:eventName"

      action="{!c.handleComponentEvent}" phase="capture" />

```

Get the Source of an Event

In the client-side controller action for an `<aura:handler>` tag, use `evt.getSource()` to find out which component fired the
event, where `evt` is a reference to the event. To retrieve the source element, use `evt.getSource().getElement()` .

IN THIS SECTION:

Component Handling Its Own Event
A component can handle its own event by using the `<aura:handler>` tag in its markup.

Handle Component Event of Instantiated Component
A parent component can set a handler action when it instantiates a child component in its markup.

Handling Bubbled or Captured Component Events
Event propagation rules determine which components in the containment hierarchy can handle events by default in the bubble or
capture phases. Learn about the rules and how to handle events in the bubble or capture phases.

### Handling Component Events Dynamically

A component can have its handler bound dynamically via JavaScript. This is useful if a component is created in JavaScript on the
client-side.

SEE ALSO:

Component Event Propagation

Handling Application Events


Communicating with Events Handling Component Events

#### Component Handling Its Own Event

A component can handle its own event by using the `<aura:handler>` tag in its markup.

The `action` attribute of `<aura:handler>` sets the client-side controller action to handle the event. For example:

```
   <aura:registerEvent name="sampleComponentEvent" type="c:compEvent"/>

   <aura:handler name="sampleComponentEvent" event="c:compEvent"

      action="{!c.handleSampleEvent}"/>

```

Note: The `name` attributes in `<aura:registerEvent>` and `<aura:handler>` must match, since each event is
defined by its name.

SEE ALSO:

#### Handle Component Event of Instantiated Component Handle Component Event of Instantiated Component

A parent component can set a handler action when it instantiates a child component in its markup.

Let’s a look at an example. `c:child` registers that it may fire a `sampleComponentEvent` event by using
`<aura:registerEvent>` in its markup.

```
   <!-- c:child -->

   <aura:component>

      <aura:registerEvent name="sampleComponentEvent" type="c:compEvent"/>

   </aura:component>

```

`c:parent` sets a handler for this event when it instantiates `c:child` in its markup.

```
   <!-- parent.cmp -->

   <aura:component>

      <c:child sampleComponentEvent="{!c.handleChildEvent}"/>

   </aura:component>

```

Note how `c:parent` uses the following syntax to set a handler for the `sampleComponentEvent` event fired by `c:child` .

```
   <c:child sampleComponentEvent="{!c.handleChildEvent}"/>

```

The syntax looks similar to how you set an attribute called `sampleComponentEvent` . However, in this case,
`sampleComponentEvent` isn’t an attribute. `sampleComponentEvent` matches the event name declared in `c:child` .

```
   <aura:registerEvent name="sampleComponentEvent" type="c:compEvent"/>

```

The preceding syntax is a convenient shortcut for the normal way that a component declares a handler for an event. The parent component
can only use this syntax to handle events from a direct descendent. If you want to be more explicit in `c:parent` that you’re handling
an event, or if the event might be fired by a component further down the component hierarchy, use an `<aura:handler>` tag
instead of declaring the handler within the `<c:child>` tag.

```
   <!-- parent.cmp -->

   <aura:component>

      <aura:handler name="sampleComponentEvent" event="c:compEvent"

       action="{!c.handleSampleEvent}"/>

      <c:child />

   </aura:component>

```


Communicating with Events Handling Component Events

The two versions of `c:parent` markup behave the same. However, using `<aura:handler>` makes it more obvious that you’re
handling a `sampleComponentEvent` event.

SEE ALSO:

Component Handling Its Own Event

#### Handling Bubbled or Captured Component Events Handling Bubbled or Captured Component Events

Event propagation rules determine which components in the containment hierarchy can handle events by default in the bubble or
capture phases. Learn about the rules and how to handle events in the bubble or capture phases.

The framework supports _capture_ and _bubble_ phases for the propagation of component events. These phases are similar to DOM handling
patterns and provide an opportunity for interested components to interact with an event and potentially control the behavior for
subsequent handlers. The capture phase executes before the bubble phase.

Default Event Propagation Rules

By default, every parent in the containment hierarchy can’t handle an event during the capture and bubble phases. Instead, the event
propagates to every owner in the containment hierarchy.

A component’s owner is the component that is responsible for its creation. For declaratively created components, the owner is the
outermost component containing the markup that references the component firing the event. For programmatically created components,
the owner component is the component that invoked `$A.createComponent` to create it.

The same rules apply for the capture phase, although the direction of event propagation (down) is the opposite of the bubble phase
(up).

Confused? It makes more sense when you look at an example in the bubbling phase.

`c:owner` contains `c:container`, which in turn contains `c:eventSource` .

```
   <!--c:owner-->

   <aura:component>

      <c:container>

        <c:eventSource />

      </c:container>

   </aura:component>

```

If `c:eventSource` fires an event, it can handle the event itself. The event then bubbles up the containment hierarchy.

`c:container` contains `c:eventSource` but it’s not the owner because it’s not the outermost component in the markup, so it
can’t handle the bubbled event.

`c:owner` is the owner because `c:container` is in its markup. `c:owner` can handle the event.

Propagation to All Container Components

The default behavior doesn’t allow an event to be handled by every parent in the containment hierarchy. Some components contain
other components but aren’t the owner of those components. These components are known as container components. In the example,
`c:container` is a container component because it’s not the owner for `c:eventSource` . By default, `c:container` can’t
handle events fired by `c:eventSource` .


Communicating with Events Handling Component Events

A container component has a facet attribute whose type is `Aura.Component[]`, such as the default `body` attribute. The container
component includes those components in its definition using an expression, such as `{!v.body}` . The container component isn’t the
owner of the components rendered with that expression.

To allow a container component to handle the event, add `includeFacets="true"` to the `<aura:handler>` tag of the
container component. For example, adding `includeFacets="true"` to the handler in the container component, `c:container`,
enables it to handle the component event bubbled from `c:eventSource` .

```
   <aura:handler name="bubblingEvent" event="c:compEvent" action="{!c.handleBubbling}"

      includeFacets="true" />

```

Handle Bubbled Event

A component that fires a component event registers that it fires the event by using the `<aura:registerEvent>` tag.

```
   <aura:component>

      <aura:registerEvent name="compEvent" type="c:compEvent" />

   </aura:component>

```

A component handling the event in the bubble phase uses the `<aura:handler>` tag to assign a handling action in its client-side
controller.

```
   <aura:component>

      <aura:handler name="compEvent" event="c:compEvent" action="{!c.handleBubbling}"/>

   </aura:component>

```

Note: The `name` attribute in `<aura:handler>` must match the `name` attribute in the `<aura:registerEvent>` tag
in the component that fires the event.

Handle Captured Event

A component handling the event in the capture phase uses the `<aura:handler>` tag to assign a handling action in its client-side
controller.

```
   <aura:component>

      <aura:handler name="compEvent" event="c:compEvent" action="{!c.handleCapture}"

        phase="capture" />

   </aura:component>

```

The default handling phase for component events is bubble if no `phase` attribute is set.

Stop Event Propagation

Use the `stopPropagation()` method in the `Event` object to stop the event propagating to other components.

Pausing Event Propagation for Asynchronous Code Execution

Use `event.pause()` to pause event handling and propagation until `event.resume()` is called. This flow-control mechanism
is useful for any decision that depends on the response from the execution of asynchronous code. For example, you might make a
decision about event propagation based on the response from an asynchronous call to native mobile code.

You can call `pause()` or `resume()` in the capture or bubble phases.


Communicating with Events Handling Component Events

Event Bubbling Example

Let’s look at an example so you can play around with it yourself.

```
   <!--c:eventBubblingParent-->

   <aura:component>

      <c:eventBubblingChild>

        <c:eventBubblingGrandchild />

      </c:eventBubblingChild>

   </aura:component>

```

Note: This sample code uses the default `c` namespace. If your org has a namespace, use that namespace instead.

First, we define a simple component event.

```
   <!--c:compEvent-->

   <aura:event type="COMPONENT">

      <!--simple event with no attributes-->

   </aura:event>

```

`c:eventBubblingEmitter` is the component that fires `c:compEvent` .

```
   <!--c:eventBubblingEmitter-->

   <aura:component>

      <aura:registerEvent name="bubblingEvent" type="c:compEvent" />

      <lightning:button onclick="{!c.fireEvent}" label="Start Bubbling"/>

   </aura:component>

```

Here’s the controller for `c:eventBubblingEmitter` . When you press the button, it fires the `bubblingEvent` event registered
in the markup.

```
   /*eventBubblingEmitterController.js*/

   {

      fireEvent : function(cmp) {

        var cmpEvent = cmp.getEvent("bubblingEvent");

        cmpEvent.fire();

      }

   }

```

`c:eventBubblingGrandchild` contains `c:eventBubblingEmitter` and uses `<aura:handler>` to assign a handler
for the event.

```
   <!--c:eventBubblingGrandchild-->

   <aura:component>

      <aura:handler name="bubblingEvent" event="c:compEvent" action="{!c.handleBubbling}"/>

      <div class="grandchild">

        <c:eventBubblingEmitter />

      </div>

   </aura:component>

```

Here’s the controller for `c:eventBubblingGrandchild` .

```
   /*eventBubblingGrandchildController.js*/

   {

      handleBubbling : function(component, event) {

```


Communicating with Events Handling Component Events

```
        console.log("Grandchild handler for " + event.getName());

      }

   }

```

The controller logs the event name when the handler is called.

Here’s the markup for `c:eventBubblingChild` . We will pass `c:eventBubblingGrandchild` in as the body of
`c:eventBubblingChild` when we create `c:eventBubblingParent` later in this example.

```
   <!--c:eventBubblingChild-->

   <aura:component>

      <aura:handler name="bubblingEvent" event="c:compEvent" action="{!c.handleBubbling}"/>

      <div class="child">

        {!v.body}

      </div>

   </aura:component>

```

Here’s the controller for `c:eventBubblingChild` .

```
   /*eventBubblingChildController.js*/

   {

      handleBubbling : function(component, event) {

        console.log("Child handler for " + event.getName());

      }

   }

```

`c:eventBubblingParent` contains `c:eventBubblingChild`, which in turn contains `c:eventBubblingGrandchild` .

```
   <!--c:eventBubblingParent-->

   <aura:component>

      <aura:handler name="bubblingEvent" event="c:compEvent" action="{!c.handleBubbling}"/>

      <div class="parent">

        <c:eventBubblingChild>

           <c:eventBubblingGrandchild />

        </c:eventBubblingChild>

      </div>

   </aura:component>

```

Here’s the controller for `c:eventBubblingParent` .

```
   /*eventBubblingParentController.js*/

   {

      handleBubbling : function(component, event) {

        console.log("Parent handler for " + event.getName());

      }

   }

```

Now, let’s see what happens when you run the code.

**1.** In your browser, navigate to `c:eventBubblingParent` . Create a `.app` resource that contains
`<c:eventBubblingParent />` .

**2.** Click the **Start Bubbling** button that is part of the markup in `c:eventBubblingEmitter` .


### Communicating with Events Component Event Example

**3.** Note the output in your browser’s console:

```
     Grandchild handler for bubblingEvent

     Parent handler for bubblingEvent

```

The `c:compEvent` event is bubbled to `c:eventBubblingGrandchild` and `c:eventBubblingParent` as they are
owners in the containment hierarchy. The event is not handled by `c:eventBubblingChild` as `c:eventBubblingChild`
is in the markup for `c:eventBubblingParent` but it’s not an owner as it’s not the outermost component in that markup.

Now, let’s see how to stop event propagation. Edit the controller for `c:eventBubblingGrandchild` to stop propagation.

```
   /*eventBubblingGrandchildController.js*/

   {

      handleBubbling : function(component, event) {

        console.log("Grandchild handler for " + event.getName());

        event.stopPropagation();

      }

   }

```

Now, navigate to `c:eventBubblingParent` and click the **Start Bubbling** button.

Note the output in your browser’s console:

```
   Grandchild handler for bubblingEvent

```

The event no longer bubbles up to the `c:eventBubblingParent` component.

SEE ALSO:

Component Event Propagation

Handle Component Event of Instantiated Component

#### Handling Component Events Dynamically

A component can have its handler bound dynamically via JavaScript. This is useful if a component is created in JavaScript on the client-side.

For more information, see Dynamically Adding Event Handlers To a Component on page 370.

### Component Event Example

Here’s a simple use case of using a component event to update an attribute in another component.

**1.** A user clicks a button in the notifier component, `ceNotifier.cmp` .

**2.** The client-side controller for `ceNotifier.cmp` sets a message in a component event and fires the event.

**3.** The handler component, `ceHandler.cmp`, contains the notifier component, and handles the fired event.

**4.** The client-side controller for `ceHandler.cmp` sets an attribute in `ceHandler.cmp` based on the data sent in the event.

Note: The event and components in this example use the default `c` namespace. If your org has a namespace, use that namespace
instead.


Communicating with Events Component Event Example

Component Event

The `ceEvent.evt` component event has one attribute. We’ll use this attribute to pass some data in the event when it’s fired.

```
   <!--c:ceEvent-->

   <aura:event type="COMPONENT">

      <aura:attribute name="message" type="String"/>

   </aura:event>

```

Notifier Component

The `c:ceNotifier` component uses `aura:registerEvent` to declare that it may fire the component event.

The button in the component contains an `onclick` browser event that is wired to the `fireComponentEvent` action in the
client-side controller. The action is invoked when you click the button.

```
   <!--c:ceNotifier-->

   <aura:component>

      <aura:registerEvent name="cmpEvent" type="c:ceEvent"/>

      <h1>Simple Component Event Sample</h1>

      <p><lightning:button

        label="Click here to fire a component event"

        onclick="{!c.fireComponentEvent}" />

      </p>

   </aura:component>

```

The client-side controller gets an instance of the event by calling `cmp.getEvent("cmpEvent")`, where `cmpEvent` matches
the value of the name attribute in the `<aura:registerEvent>` tag in the component markup. The controller sets the `message`
attribute of the event and fires the event.

```
   /* ceNotifierController.js */

   {

      fireComponentEvent : function(cmp, event) {

        // Get the component event by using the

        // name value from aura:registerEvent

        var cmpEvent = cmp.getEvent("cmpEvent");

        cmpEvent.setParams({

           "message" : "A component event fired me. " +

           "It all happened so fast. Now, I'm here!" });

        cmpEvent.fire();

      }

   }

```

Handler Component

The `c:ceHandler` handler component contains the `c:ceNotifier` component. The `<aura:handler>` tag uses the same
value of the `name` attribute, `cmpEvent`, from the `<aura:registerEvent>` tag in `c:ceNotifier` . This wires up
`c:ceHandler` to handle the event bubbled up from `c:ceNotifier` .

When the event is fired, the `handleComponentEvent` action in the client-side controller of the handler component is invoked.

```
   <!--c:ceHandler-->

   <aura:component>

      <aura:attribute name="messageFromEvent" type="String"/>

```


## Communicating with Events Application Events

```
      <aura:attribute name="numEvents" type="Integer" default="0"/>

      <!-- Note that name="cmpEvent" in aura:registerEvent

      in ceNotifier.cmp -->

      <aura:handler name="cmpEvent" event="c:ceEvent" action="{!c.handleComponentEvent}"/>

      <!-- handler contains the notifier component -->

      <c:ceNotifier />

      <p>{!v.messageFromEvent}</p>

      <p>Number of events: {!v.numEvents}</p>

   </aura:component>

```

The controller retrieves the data sent in the event and uses it to update the `messageFromEvent` attribute in the handler component.

```
   /* ceHandlerController.js */

   {

      handleComponentEvent : function(cmp, event) {

        var message = event.getParam("message");

        // set the handler attributes based on event data

        cmp.set("v.messageFromEvent", message);

        var numEventsHandled = parseInt(cmp.get("v.numEvents")) + 1;

        cmp.set("v.numEvents", numEventsHandled);

      }

   }

```

Put It All Together

Add the `c:ceHandler` component to a `c:ceHandlerApp` application. Navigate to the application and click the button to fire
the component event.

`https://` _`MyDomainName`_ `.lightning.force.com/c/ceHandlerApp.app` .

If you want to access data on the server, you could extend this example to call a server-side controller from the handler’s client-side
controller.

SEE ALSO:

Component Events

Creating Server-Side Logic with Controllers

Application Event Example

## Application Events

Application events follow a traditional publish-subscribe model. An application event is fired from an instance of a component. All
components that provide a handler for the event are notified.


### Communicating with Events Application Event Propagation

IN THIS SECTION:

### Application Event Propagation

The framework supports _capture_, _bubble_, and _default_ phases for the propagation of application events. The capture and bubble
phases are similar to DOM handling patterns and provide an opportunity for interested components to interact with an event and
potentially control the behavior for subsequent handlers. The default phase preserves the framework’s original handling behavior.

Create Custom Application Events
Create a custom application event using the `<aura:event>` tag in a `.evt` resource. Events can contain attributes that can be
set before the event is fired and read when the event is handled.

Fire Application Events
Application events follow a traditional publish-subscribe model. An application event is fired from an instance of a component. All
components that provide a handler for the event are notified.

Handling Application Events
Use `<aura:handler>` in the markup of the handler component.

SEE ALSO:

Component Events

Handling Events with Client-Side Controllers

### Application Event Propagation

Advanced Events Example

### Application Event Propagation

The framework supports _capture_, _bubble_, and _default_ phases for the propagation of application events. The capture and bubble phases
are similar to DOM handling patterns and provide an opportunity for interested components to interact with an event and potentially
control the behavior for subsequent handlers. The default phase preserves the framework’s original handling behavior.

A component can publish an application-level event. When the event is fired, any component or application that has subscribed to the
event invokes its handler within a Lightning page. To communicate across the DOM within a Lightning page, or across multiple pages
between Visualforce, Lightning pages, and Lightning web components (LWC), use Lightning Message Service on page 299 instead.

The component that fires an event is known as the source component. The framework allows you to handle the event in different phases.
These phases give you flexibility for how to best process the event for your application.


### Communicating with Events Create Custom Application Events

The phases are:

**Capture**
The event is captured and trickles down from the application root to the source component. The event can be handled by a component
in the containment hierarchy that receives the captured event.

Event handlers are invoked in order from the application root down to the source component that fired the event.

Any registered handler in this phase can stop the event from propagating, at which point no more handlers are called in this phase
or the bubble phase. If a component stops the event propagation using `event.stopPropagation()`, the component
becomes the root node used in the default phase.

Any registered handler in this phase can cancel the default behavior of the event by calling `event.preventDefault()` . This
call prevents execution of any of the handlers in the default phase.

**Bubble**
The component that fired the event can handle it. The event then bubbles up from the source component to the application root.
The event can be handled by a component in the containment hierarchy that receives the bubbled event.

Event handlers are invoked in order from the source component that fired the event up to the application root.

Any registered handler in this phase can stop the event from propagating, at which point no more handlers will be called in this
phase. If a component stops the event propagation using `event.stopPropagation()`, the component becomes the root
node used in the default phase.

Any registered handler in this phase can cancel the default behavior of the event by calling `event.preventDefault()` . This
call prevents execution of any of the handlers in the default phase.

**Default**
Event handlers are invoked in a non-deterministic order from the root node through its subtree. The default phase doesn’t have the
same propagation rules related to component hierarchy as the capture and bubble phases. The default phase can be useful for
handling application events that affect components in different sub-trees of your app.

If the event’s propagation wasn’t stopped in a previous phase, the root node defaults to the application root. If the event’s propagation
was stopped in a previous phase, the root node is set to the component whose handler invoked `event.stopPropagation()` .

Here is the sequence of application event propagation.

**1. Event fired** —An application event is fired. The component that fires the event is known as the source component.

**2. Capture phase** —The framework executes the capture phase from the application root to the source component until all components
are traversed. Any handling event can stop propagation by calling `stopPropagation()` on the event.

**3. Bubble phase** —The framework executes the bubble phase from the source component to the application root until all components
are traversed or `stopPropagation()` is called.

**4. Default phase** —The framework executes the default phase from the root node unless `preventDefault()` was called in the
capture or bubble phases. If the event’s propagation wasn’t stopped in a previous phase, the root node defaults to the application
root. If the event’s propagation was stopped in a previous phase, the root node is set to the component whose handler invoked
`event.stopPropagation()` .

### Create Custom Application Events

Create a custom application event using the `<aura:event>` tag in a `.evt` resource. Events can contain attributes that can be set
before the event is fired and read when the event is handled.


### Communicating with Events Fire Application Events

Use `type="APPLICATION"` in the `<aura:event>` tag for an application event. For example, this `c:appEvent` application
event has one attribute with a name of `message` .

```
   <!--c:appEvent-->

   <aura:event type="APPLICATION">

      <!-- Add aura:attribute tags to define event shape.

         One sample attribute here. -->

      <aura:attribute name="message" type="String"/>

   </aura:event>

```

The component that fires an event can set the event’s data. To set the attribute values, call `event.setParam()` or
`event.setParams()` . A parameter name set in the event must match the `name` attribute of an `<aura:attribute>` in the
event. For example, if you fire `c:appEvent`, you could use:

```
   event.setParam("message", "event message here");

```

The component that handles an event can retrieve the event data. To retrieve the attribute in this event, call
`event.getParam("message")` in the handler’s client-side controller.

SEE ALSO:

Application Event Example

### Fire Application Events

Application events follow a traditional publish-subscribe model. An application event is fired from an instance of a component. All
components that provide a handler for the event are notified.

Register an Event

A component registers that it may fire an application event by using `<aura:registerEvent>` in its markup. The `name` attribute
is required but not used for application events. The `name` attribute is only relevant for component events. This example uses
`name="appEvent"` but the value isn’t used anywhere.

```
   <aura:registerEvent name="appEvent" type="c:appEvent"/>

```

Fire an Event

Use `$A.get("e.myNamespace:myAppEvent")` in JavaScript to get an instance of the `myAppEvent` event in the
`myNamespace` namespace.

Note: The syntax to get an instance of an application event is different than the syntax to get a component event, which is
`cmp.getEvent("` _**`evtName`**_ `")` .

Use `fire()` to fire the event.

```
   var appEvent = $A.get("e.c:appEvent");

   // Optional: set some data for the event (also known as event shape)

   // A parameter’s name must match the name attribute

   // of one of the event’s <aura:attribute> tags

   //appEvent.setParams({ "myParam" : myValue });

   appEvent.fire();

```


### Communicating with Events Handling Application Events

Events Fired on App Rendering

Some events are automatically fired when an app is rendering. For more information, see Events Fired During the Rendering Lifecycle
on page 294.

SEE ALSO:

Fire Component Events

### Handling Application Events

Use `<aura:handler>` in the markup of the handler component.

For example:

```
   <aura:handler event="c:appEvent" action="{!c.handleApplicationEvent}"/>

```

The `event` attribute specifies the event being handled. The format is _**`namespace`**_ `:` _**`eventName`**_ .

The `action` attribute of `<aura:handler>` sets the client-side controller action to handle the event.

Note: The handler for an application event won’t work if you set the `name` attribute in `<aura:handler>` . Use the `name`
attribute only when you’re handling component events.

In this example, when the event is fired, the `handleApplicationEvent` client-side controller action is called.

Event Handling Phases

The framework allows you to handle the event in different phases. These phases give you flexibility for how to best process the event
for your application.

Application event handlers are associated with the default phase. To add a handler for the capture or bubble phases instead, use the
`phase` attribute.

Get the Source of an Event

In the client-side controller action for an `<aura:handler>` tag, use `evt.getSource()` to find out which component fired the
event, where `evt` is a reference to the event. To retrieve the source element, use `evt.getSource().getElement()` .

IN THIS SECTION:

#### Handling Bubbled or Captured Application Events

Event propagation rules determine which components in the containment hierarchy can handle events by default in the bubble or
capture phases. Learn about the rules and how to handle events in the bubble or capture phases.

SEE ALSO:

Handling Component Events

#### Handling Bubbled or Captured Application Events

Event propagation rules determine which components in the containment hierarchy can handle events by default in the bubble or
capture phases. Learn about the rules and how to handle events in the bubble or capture phases.


Communicating with Events Handling Application Events

The framework supports _capture_, _bubble_, and _default_ phases for the propagation of application events. The capture and bubble phases
are similar to DOM handling patterns and provide an opportunity for interested components to interact with an event and potentially
control the behavior for subsequent handlers. The default phase preserves the framework’s original handling behavior.

Default Event Propagation Rules

By default, every parent in the containment hierarchy can’t handle an event during the capture and bubble phases. Instead, the event
propagates to every owner in the containment hierarchy.

A component’s owner is the component that is responsible for its creation. For declaratively created components, the owner is the
outermost component containing the markup that references the component firing the event. For programmatically created components,
the owner component is the component that invoked `$A.createComponent` to create it.

The same rules apply for the capture phase, although the direction of event propagation (down) is the opposite of the bubble phase
(up).

Confused? It makes more sense when you look at an example in the bubbling phase.

`c:owner` contains `c:container`, which in turn contains `c:eventSource` .

```
   <!--c:owner-->

   <aura:component>

      <c:container>

        <c:eventSource />

      </c:container>

   </aura:component>

```

If `c:eventSource` fires an event, it can handle the event itself. The event then bubbles up the containment hierarchy.

`c:container` contains `c:eventSource` but it’s not the owner because it’s not the outermost component in the markup, so it
can’t handle the bubbled event.

`c:owner` is the owner because `c:container` is in its markup. `c:owner` can handle the event.

Propagation to All Container Components

The default behavior doesn’t allow an event to be handled by every parent in the containment hierarchy. Some components contain
other components but aren’t the owner of those components. These components are known as container components. In the example,
`c:container` is a container component because it’s not the owner for `c:eventSource` . By default, `c:container` can’t
handle events fired by `c:eventSource` .

A container component has a facet attribute whose type is `Aura.Component[]`, such as the default `body` attribute. The container
component includes those components in its definition using an expression, such as `{!v.body}` . The container component isn’t the
owner of the components rendered with that expression.

To allow a container component to handle the event, add `includeFacets="true"` to the `<aura:handler>` tag of the
container component. For example, adding `includeFacets="true"` to the handler in the container component, `c:container`,
enables it to handle the component event bubbled from `c:eventSource` .

```
   <aura:handler name="bubblingEvent" event="c:compEvent" action="{!c.handleBubbling}"

      includeFacets="true" />

```


### Communicating with Events Application Event Example

Handle Bubbled Event

To add a handler for the bubble phase, set `phase="bubble"` .

```
   <aura:handler event="c:appEvent" action="{!c.handleBubbledEvent}"

      phase="bubble" />

```

The `event` attribute specifies the event being handled. The format is _**`namespace`**_ `:` _**`eventName`**_ .

The `action` attribute of `<aura:handler>` sets the client-side controller action to handle the event.

Handle Captured Event

To add a handler for the capture phase, set `phase="capture"` .

```
   <aura:handler event="c:appEvent" action="{!c.handleCapturedEvent}"

      phase="capture" />

```

Stop Event Propagation

Use the `stopPropagation()` method in the `Event` object to stop the event propagating to other components.

Pausing Event Propagation for Asynchronous Code Execution

Use `event.pause()` to pause event handling and propagation until `event.resume()` is called. This flow-control mechanism
is useful for any decision that depends on the response from the execution of asynchronous code. For example, you might make a
decision about event propagation based on the response from an asynchronous call to native mobile code.

You can call `pause()` or `resume()` in the capture or bubble phases.

### Application Event Example

Here’s a simple use case of using an application event to update an attribute in another component.

**1.** A user clicks a button in the notifier component, `aeNotifier.cmp` .

**2.** The client-side controller for `aeNotifier.cmp` sets a message in a component event and fires the event.

**3.** The handler component, `aeHandler.cmp`, handles the fired event.

**4.** The client-side controller for `aeHandler.cmp` sets an attribute in `aeHandler.cmp` based on the data sent in the event.

Note: The event and components in this example use the default `c` namespace. If your org has a namespace, use that namespace
instead.

### Application Event

The `aeEvent.evt` application event has one attribute. We’ll use this attribute to pass some data in the event when it’s fired.

```
   <!--c:aeEvent-->

   <aura:event type="APPLICATION">

      <aura:attribute name="message" type="String"/>

   </aura:event>

```


Communicating with Events Application Event Example

Notifier Component

The `aeNotifier.cmp` notifier component uses `aura:registerEvent` to declare that it may fire the application event. The
`name` attribute is required but not used for application events. The `name` attribute is only relevant for component events.

The button in the component contains a `onclick` browser event that is wired to the `fireApplicationEvent` action in the
client-side controller. Clicking this button invokes the action.

```
   <!--c:aeNotifier-->

   <aura:component>

      <aura:registerEvent name="appEvent" type="c:aeEvent"/>

      <h1>Simple Application Event Sample</h1>

      <p><lightning:button

        label="Click here to fire an application event"

        onclick="{!c.fireApplicationEvent}" />

      </p>

   </aura:component>

```

The client-side controller gets an instance of the event by calling `$A.get("e.c:aeEvent")` . The controller sets the `message`
attribute of the event and fires the event.

```
   /* aeNotifierController.js */

   {

      fireApplicationEvent : function(cmp, event) {

        // Get the application event by using the

        // e.<namespace>.<event> syntax

        var appEvent = $A.get("e.c:aeEvent");

        appEvent.setParams({

           "message" : "An application event fired me. " +

           "It all happened so fast. Now, I'm everywhere!" });

        appEvent.fire();

      }

   }

```

Handler Component

The `aeHandler.cmp` handler component uses the `<aura:handler>` tag to register that it handles the application event.

Note: The handler for an application event won’t work if you set the `name` attribute in `<aura:handler>` . Use the `name`
attribute only when you’re handling component events.

When the event is fired, the `handleApplicationEvent` action in the client-side controller of the handler component is invoked.

```
   <!--c:aeHandler-->

   <aura:component>

      <aura:attribute name="messageFromEvent" type="String"/>

      <aura:attribute name="numEvents" type="Integer" default="0"/>

      <aura:handler event="c:aeEvent" action="{!c.handleApplicationEvent}"/>

      <p>{!v.messageFromEvent}</p>

      <p>Number of events: {!v.numEvents}</p>

   </aura:component>

```


## Communicating with Events Event Handler Behavior for Active Components

The controller retrieves the data sent in the event and uses it to update the `messageFromEvent` attribute in the handler component.

```
   /* aeHandlerController.js */

   {

      handleApplicationEvent : function(cmp, event) {

        var message = event.getParam("message");

        // set the handler attributes based on event data

        cmp.set("v.messageFromEvent", message);

        var numEventsHandled = parseInt(cmp.get("v.numEvents")) + 1;

        cmp.set("v.numEvents", numEventsHandled);

      }

   }

```

Container Component

The `aeContainer.cmp` container component contains the notifier and handler components. This is different from the component
event example where the handler contains the notifier component.

```
   <!--c:aeContainer-->

   <aura:component>

      <c:aeNotifier/>

      <c:aeHandler/>

   </aura:component>

```

Put It All Together

You can test this code by adding `<c:aeContainer>` to a sample `aeWrapper.app` application and navigating to the application.

`https://` _`MyDomainName`_ `.lightning.force.com/c/aeWrapper.app` .

If you want to access data on the server, you could extend this example to call a server-side controller from the handler’s client-side
controller.

SEE ALSO:

Application Events

Creating Server-Side Logic with Controllers

Component Event Example

## Event Handler Behavior for Active Components

To prevent active event handlers on cached pages from causing problems, add a workaround to your code to check if the component
is still visible. To avoid this scenario and the workaround, use Lightning message service instead to communicate across the DOM within
a Lightning page. The default scope used by Lightning message service channels publishes only to active components.

When navigating away from a page in Lightning Experience, the framework caches the components in the page so that they remain
active, along with their event handlers. This caching speeds up navigation, but it can cause the cached component to respond to events
that are not intended for it, such as `force:refreshView` or `force:recordSaveSuccess` .

This workaround uses the `offsetParent` property for the component to get its handlers while they’re visible. The workaround is
good only if the component definition has an HTML element in it.


## Communicating with Events Event Handling Lifecycle

This component includes an event handler and some HTML.

```
   <!--myComponent.cmp-->

   <aura:component>

     <aura:handler event="c:appEvent" action="{!c.onEvent}>

     <h1>This component has a handler</h1>

   </aura:component>

```

Here’s the client-side controller that uses the `offsetParent` property to get the component’s handlers while they’re still visible.

```
   /* myComponentController.js */

   ({

     onEvent: function(component, event, helper) {

      var elem = component.getElement();

      if (elem && elem.offsetParent !== null) {

       // event handling logic here

      }

     }

   })

```

SEE ALSO:

Communicating Across the DOM with Lightning Message Service

_[Component Library:](https://developer.salesforce.com/docs/component-library/bundle/lightning-message-service/documentation)_ Message Service

## Event Handling Lifecycle

The following chart summarizes how the framework handles events.


Communicating with Events Event Handling Lifecycle

**1 Detect Firing of Event**

The framework detects the firing of an event. For example, the event could be triggered by a button click in a notifier component.

**2 Determine the Event Type**

**2.1 Component Event**

The parent or container component instance that fired the event is identified. This container component locates all relevant event
handlers for further processing.

**2.2 Application Event**

Any component can have an event handler for this event. All relevant event handlers are located.

**3 Execute each Handler**

**3.1 Executing a Component Event Handler**

Each of the event handlers defined in the container component for the event are executed by the handler controller, which can also:


## Communicating with Events Advanced Events Example

**•** Set attributes or modify data on the component (causing a re-rendering of the component).

**•** Fire another event or invoke a client-side or server-side action.

**3.2 Executing an Application Event Handler**

All event handlers are executed. When the event handler is executed, the event instance is passed into the event handler.

**4 Re-render Component (optional)**

After the event handlers and any callback actions are executed, a component might be automatically re-rendered if it was modified
during the event handling process.

SEE ALSO:

Create a Custom Renderer

## Advanced Events Example

This example builds on the simpler component and application event examples. It uses one notifier component and one handler
component that work with both component and application events. Before we see a component wired up to events, let's look at the
individual resources involved.

This table summarizes the roles of the various resources used in the example. The source code for these resources is included after the
table.

**Resource** **Resource Name** **Usage**

Event files Component event ( `compEvent.evt` ) Defines the component and application events in
and application event ( `appEvent.evt` ) separate resources. `eventsContainer.cmp`

shows how to use both component and application
events.

Notifier

Handler

Component ( `eventsNotifier.cmp` ) The notifier contains an `onclick` browser event to
and its controller initiate the event. The controller fires the event.
( `eventsNotifierController.js` )

Component ( `eventsHandler.cmp` ) The handler component contains the notifier
and its controller component (or a `<aura:handler>` tag for
( `eventsHandlerController.js` ) application events), and calls the controller action that

is executed after the event is fired.

Container Component `eventsContainer.cmp` Displays the event handlers on the UI for the complete
demo.

The definitions of component and application events are stored in separate `.evt` resources, but individual notifier and handler
component bundles can contain code to work with both types of events.

The component and application events both contain a `context` attribute that defines the shape of the event. This is the data that is
passed to handlers of the event.


Communicating with Events Advanced Events Example

Component Event

Here is the markup for `compEvent.evt` .

```
   <!--c:compEvent-->

   <aura:event type="COMPONENT">

      <!-- pass context of where the event was fired to the handler. -->

      <aura:attribute name="context" type="String"/>

   </aura:event>

```

Application Event

Here is the markup for `appEvent.evt` .

```
   <!--c:appEvent-->

   <aura:event type="APPLICATION">

      <!-- pass context of where the event was fired to the handler. -->

      <aura:attribute name="context" type="String"/>

   </aura:event>

```

Notifier Component

The `eventsNotifier.cmp` notifier component contains buttons to initiate a component or application event.

The notifier uses `aura:registerEvent` tags to declare that it may fire the component and application events. Note that the
`name` attribute is required but the value is only relevant for the component event; the value is not used anywhere else for the application
event.

The `parentName` attribute is not set yet. We will see how this attribute is set and surfaced in `eventsContainer.cmp` .

```
   <!--c:eventsNotifier-->

   <aura:component>

     <aura:attribute name="parentName" type="String"/>

     <aura:registerEvent name="componentEventFired" type="c:compEvent"/>

     <aura:registerEvent name="appEvent" type="c:appEvent"/>

     <div>

      <h3>This is {!v.parentName}'s eventsNotifier.cmp instance</h3>

      <p><lightning:button

        label="Click here to fire a component event"

        onclick="{!c.fireComponentEvent}" />

      </p>

      <p><lightning:button

        label="Click here to fire an application event"

        onclick="{!c.fireApplicationEvent}" />

      </p>

     </div>

   </aura:component>

```

**CSS source**

The CSS is in `eventsNotifier.css` .

```
   /* eventsNotifier.css */

   .cEventsNotifier {

```


Communicating with Events Advanced Events Example

```
      display: block;

      margin: 10px;

      padding: 10px;

      border: 1px solid black;

   }

```

**Client-side controller source**

The `eventsNotifierController.js` controller fires the event.

```
   /* eventsNotifierController.js */

   {

      fireComponentEvent : function(cmp, event) {

        var parentName = cmp.get("v.parentName");

        // Look up event by name, not by type

        var compEvents = cmp.getEvent("componentEventFired");

        compEvents.setParams({ "context" : parentName });

        compEvents.fire();

      },

      fireApplicationEvent : function(cmp, event) {

        var parentName = cmp.get("v.parentName");

        // note different syntax for getting application event

        var appEvent = $A.get("e.c:appEvent");

        appEvent.setParams({ "context" : parentName });

        appEvent.fire();

      }

   }

```

You can click the buttons to fire component and application events but there is no change to the output because we haven't wired up
the handler component to react to the events yet.

The controller sets the `context` attribute of the component or application event to the `parentName` of the notifier component
before firing the event. We will see how this affects the output when we look at the handler component.

Handler Component

The `eventsHandler.cmp` handler component contains the `c:eventsNotifier` notifier component and `<aura:handler>`
tags for the application and component events.

```
   <!--c:eventsHandler-->

   <aura:component>

     <aura:attribute name="name" type="String"/>

    <aura:attribute name="mostRecentEvent" type="String" default="Most recent event handled:"/>

     <aura:attribute name="numComponentEventsHandled" type="Integer" default="0"/>

     <aura:attribute name="numApplicationEventsHandled" type="Integer" default="0"/>

     <aura:handler event="c:appEvent" action="{!c.handleApplicationEventFired}"/>

     <aura:handler name="componentEventFired" event="c:compEvent"

   action="{!c.handleComponentEventFired}"/>

```


Communicating with Events Advanced Events Example

```
     <div>

      <h3>This is {!v.name}</h3>

      <p>{!v.mostRecentEvent}</p>

      <p># component events handled: {!v.numComponentEventsHandled}</p>

      <p># application events handled: {!v.numApplicationEventsHandled}</p>

      <c:eventsNotifier parentName="{#v.name}" />

     </div>

   </aura:component>

```

Note: `{#v.name}` is an unbound expression. This means that any change to the value of the `parentName` attribute in
`c:eventsNotifier` doesn’t propagate back to affect the value of the `name` attribute in `c:eventsHandler` . For more
information, see Data Binding Between Components on page 49.

**CSS source**

The CSS is in `eventsHandler.css` .

```
   /* eventsHandler.css */

   .cEventsHandler {

     display: block;

     margin: 10px;

     padding: 10px;

     border: 1px solid black;

   }

```

**Client-side controller source**

The client-side controller is in `eventsHandlerController.js` .

```
   /* eventsHandlerController.js */

   {

      handleComponentEventFired : function(cmp, event) {

        var context = event.getParam("context");

        cmp.set("v.mostRecentEvent",

           "Most recent event handled: COMPONENT event, from " + context);

        var numComponentEventsHandled =

           parseInt(cmp.get("v.numComponentEventsHandled")) + 1;

        cmp.set("v.numComponentEventsHandled", numComponentEventsHandled);

      },

      handleApplicationEventFired : function(cmp, event) {

        var context = event.getParam("context");

        cmp.set("v.mostRecentEvent",

           "Most recent event handled: APPLICATION event, from " + context);

        var numApplicationEventsHandled =

           parseInt(cmp.get("v.numApplicationEventsHandled")) + 1;

        cmp.set("v.numApplicationEventsHandled", numApplicationEventsHandled);

      }

   }

```

The `name` attribute is not set yet. We will see how this attribute is set and surfaced in `eventsContainer.cmp` .


## Communicating with Events Firing Events from Non-Aura Code

You can click buttons and the UI now changes to indicate the type of event. The click count increments to indicate whether it's a
component or application event. We aren't finished yet though. Notice that the source of the event is undefined as the event `context`
attribute hasn't been set .

Container Component

Here is the markup for `eventsContainer.cmp` .

```
   <!--c:eventsContainer-->

   <aura:component>

      <c:eventsHandler name="eventsHandler1"/>

      <c:eventsHandler name="eventsHandler2"/>

   </aura:component>

```

The container component contains two handler components. It sets the `name` attribute of both handler components, which is passed
through to set the `parentName` attribute of the notifier components. This fills in the gaps in the UI text that we saw when we looked
at the notifier or handler components directly.

Add the `c:eventsContainer` component to a `c:eventsContainerApp` application. Navigate to the application.

`https://` _`MyDomainName`_ `.lightning.force.com/c/eventsContainerApp.app` .

Click the **Click here to fire a component event** button for either of the event handlers. Notice that the **# component events handled**
counter only increments for that component because only the firing component's handler is notified.

Click the **Click here to fire an application event** button for either of the event handlers. Notice that the **# application events handled**
counter increments for both the components this time because all the handling components are notified.

SEE ALSO:

Component Event Example

Application Event Example

Event Handling Lifecycle

## Firing Events from Non-Aura Code

You can fire Aura events from JavaScript code outside an Aura app. For example, your Aura app might need to call out to some non-Aura
code, and then have that code communicate back to your Aura app once it's done.

For example, you could call external code that needs to log into another system and return some data to your Aura app by firing an Aura
event. Let's call this event `mynamespace:externalEvent` . The external code fires this event when it’s ready to communicate
with an Aura app.

```
   var myExternalEvent;

   if(window.$A &&

     (myExternalEvent = window.$A.get("e.mynamespace:externalEvent"))) {

      myExternalEvent.setParams({isOauthed:true});

```


## Communicating with Events Events Best Practices

```
      myExternalEvent.fire();

   }

```

SEE ALSO:

Application Events

Modifying Components Outside the Framework Lifecycle

## Events Best Practices

Here are some best practices for working with events.

Use Component Events Whenever Possible

Always try to use a component event instead of an application event, if possible. Component events can only be handled by components
above them in the containment hierarchy so their usage is more localized to the components that need to know about them. Application
events are best used for something that should be handled at the application level, such as navigating to a specific record. Application
events allow communication between components that are in separate parts of the application and have no direct containment
relationship.

Separate Low-Level Events from Business Logic Events

Handle low-level events, such as a click, in your event handler and refire them as higher-level events, such as an `approvalChange`
event or whatever is appropriate for your business logic.

Dynamic Actions Based on Component State

To invoke a different action on a click event depending on the state of the component, try this approach:

**1.** Store the component state as a discrete value, such as New or Pending, in a component attribute.

**2.** Put logic in your client-side controller that determines the next action to take.

**3.** Put logic in the helper if you want to reuse it in the component bundle.

For example:

**1.** Your component markup contains `<lightning:button label="do something"`
`onclick="{!c.handleClick}" />` .

**2.** In your controller, define the `handleClick` function, which delegates to the appropriate helper function or potentially fires the
correct event.


### Communicating with Events Events Anti-Patterns

Using a Dispatcher Component to Listen and Relay Events

If you have a large number of handler component instances listening for an event, identify a dispatcher component to listen for the
event. The dispatcher component can perform some logic to decide which component instances receive further information, and fire
another component or application event targeted at those component instances.

SEE ALSO:

Handling Events with Client-Side Controllers

### Events Anti-Patterns Events Anti-Patterns

These are some anti-patterns that you should avoid when using events.

Don't Fire an Event in a Renderer

Firing an event in a renderer can cause an infinite rendering loop.

**Don’t do this!**

```
   afterRender: function(cmp, helper) {

      this.superAfterRender();

      $A.get("e.myns:mycmp").fire();

   }

```

Instead, use the `init` hook to run a controller action after component construction but before rendering. Add this code to your
component:

```
   <aura:handler name="init" value="{!this}" action="{!c.doInit}"/>

```

For more details, see .Invoking Actions on Component Initialization on page 339.

### Don’t Use onclick and ontouchend Events

You can’t use different actions for `onclick` and `ontouchend` events in a component. The framework translates touch-tap events
into clicks and activates any `onclick` handlers that are present.

SEE ALSO:

Create a Custom Renderer

Events Best Practices

## Events Fired During the Rendering Lifecycle

A component is instantiated, rendered, and rerendered during its lifecycle. A component rerenders only when there’s a programmatic
or value change that requires a rerender. For example, if a browser event triggers an action that updates the component’s data, the
component rerenders.


Communicating with Events Events Fired During the Rendering Lifecycle

Component Creation

The component lifecycle starts when the client sends an HTTP request to the server and the component configuration data is returned
to the client. No server trip is made if the component definition is already on the client from a previous request and the component has
no server dependencies.

Let’s look at an app with several nested components. The framework instantiates the app and goes through the children of the `v.body`
facet to create each component. First, it creates the component definition, its entire parent hierarchy, and then creates the facets within
those components. The framework also creates any component dependencies on the server, including definitions for attributes, interfaces,
controllers, and actions.

The following image lists the order of component creation.

After creating a component instance, the framework sends the serialized component definitions and instances down to the client.
Definitions are cached but not the instance data. The client deserializes the response to create the JavaScript objects or maps, resulting
in an instance tree that’s used to render the component instance. When the component tree is ready, the `init` event is fired for all
the components, starting from the child components and finishing in the parent component.

Component Rendering

The rendering lifecycle happens once in the lifetime of a component unless the component gets explicitly unrendered. When you create
a component:

**1.** The component service that constructs the components fires the `init` event to signal that initialization has completed.

```
     <aura:handler name="init" value="{!this}" action="{!c.doInit}"/>

```

You can customize the `init` handler and add your own controller logic before the component starts rendering. For more information,
see Invoking Actions on Component Initialization on page 339.

**2.** For each component in the tree, the base implementation of `render()` or your custom renderer is called to start component
rendering. For more information, see Create a Custom Renderer on page 357. Similar to the component creation process, rendering
starts at the root component, its child components and their super components, if any, and finally the subchild components.


## Communicating with Events Events Handled in the Salesforce Mobile App and Lightning

Experience

**3.** After your components are rendered to the DOM, `afterRender()` is called to signal that rendering is completed for each of
these component definitions. It enables you to interact with the DOM tree after the framework rendering service has created the
DOM elements.

**4.** To indicate that the client is done waiting for a response to the server request XHR, the `aura:doneWaiting` event is fired. You
can handle this event by adding a handler wired to a client-side controller action.

Note: The `aura:doneWaiting` event is deprecated. The `aura:doneWaiting` application event is fired for every
server response, even for responses from other components in your app. Unless your component is running in complete
isolation in a standalone app and not included in Lightning Experience or the Salesforce mobile app, the container app may
trigger your event handler multiple times. This behavior makes it difficult to handle each event appropriately.

**5.** The framework fires a `render` event, enabling you to interact with the DOM tree after the framework’s rendering service has
inserted DOM elements. Handling the `render` event is preferred to creating a custom renderer and overriding `afterRender()` .
For more information, see Handle the render Event.

**6.** Finally, the `aura:doneRendering` event is fired at the end of the rendering lifecycle.

Note: The `aura:doneRendering` event is deprecated. Unless your component is running in complete isolation in a
standalone app and not included in complex apps, such as Lightning Experience or the Salesforce mobile app, the container
app may trigger your event handler multiple times. This behavior makes it difficult to handle each event appropriately.

Rendering Nested Components

Let’s say that you have an app `myApp.app` that contains a component `myCmp.cmp` with a nested component.

During initialization, the `init()` event is fired in this order: the nested component, `myCmp.cmp`, and `myApp.app` .

SEE ALSO:

Create a Custom Renderer

## Events Handled in the Salesforce Mobile App and Lightning Experience

The Salesforce mobile app and Lightning Experience handle some events, which you can fire in your Aura component.

If you fire one of these `force` or `lightning` events in your Lightning apps or components outside of the Salesforce mobile app
or Lightning Experience:

**•** You must handle the event by using the `<aura:handler>` tag in the handling component.

**•** Use the `<aura:registerEvent>` or `<aura:dependency>` tags to ensure that the event is sent to the client, when
needed.

**Event Name** **Description**

`force:closeQuickAction` Closes a quick action panel. Only one quick action panel can be open in the app
at a time.

`force:createRecord` Opens a page to create a record for the specified `entityApiName`, for example,
“Account” or “myNamespace__MyObject__c”.

`force:editRecord` Opens the page to edit the record specified by `recordId` .

`force:navigateToComponent` (Beta) Navigates from one Aura component to another.


Communicating with Events Events Handled in the Salesforce Mobile App and Lightning
Experience

**Event Name** **Description**

`force:navigateToList` Navigates to the list view specified by `listViewId` .

`force:navigateToObjectHome` Navigates to the object home specified by the `scope` attribute.

`force:navigateToRelatedList` Navigates to the related list specified by `parentRecordId` .

`force:navigateToSObject` Navigates to an sObject record specified by `recordId` .

`force:navigateToURL` Navigates to the specified URL.

`force:recordSave` Saves a record.

`force:recordSaveSuccess` Indicates that the record has been successfully saved.

`force:refreshView` Reloads the view.

`force:showToast` Displays a toast notification with a message. (Not available on login pages.)

`lightning:openFiles` Opens one or more file records from the ContentDocument and ContentHubItem
objects.

Customizing Client-Side Logic for the Salesforce Mobile App, Lightning
Experience, and Standalone Apps

Since the Salesforce mobile app and Lightning Experience automatically handle many events, you have to do extra work if your component
runs in a standalone app. Instantiating the event using `$A.get()` can help you determine if your component is running within the
Salesforce mobile app and Lightning Experience or a standalone app. For example, you want to display a toast when a component loads
in the Salesforce mobile app and Lightning Experience. You can fire the `force:showToast` event and set its parameters for the
Salesforce mobile app and Lightning Experience, but you have to create your own implementation for a standalone app.

```
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

SEE ALSO:

aura:dependency

Fire Component Events

Fire Application Events


## Communicating with Events System Events System Events

The framework fires several system events during its lifecycle.

You can handle these events in your Lightning apps or components, and within the Salesforce mobile app.

For examples, see the Lightning Component Library.

**Event Name** **Description**

`aura:doneRendering` (deprecated) Indicates that the initial rendering of the root application has completed.

Note: The `aura:doneRendering` event is deprecated. Unless your
component is running in complete isolation in a standalone app and not
included in complex apps, such as Lightning Experience or the Salesforce
mobile app, the container app may trigger your event handler multiple
times. This behavior makes it difficult to handle each event appropriately.

`aura:doneWaiting` (deprecated) Indicates that the app is done waiting for a response to a server request. This
event is preceded by an `aura:waiting` event.

Note: The `aura:doneWaiting` event is deprecated. The
`aura:doneWaiting` application event is fired for every server
response, even for responses from other components in your app. Unless
your component is running in complete isolation in a standalone app and
not included in Lightning Experience or the Salesforce mobile app, the
container app may trigger your event handler multiple times. This behavior
makes it difficult to handle each event appropriately.

`aura:locationChange` Indicates that the hash part of the URL has changed.

`aura:noAccess` Indicates that a requested resource is not accessible due to security constraints
on that resource.

`aura:systemError` Indicates that an error has occurred.

`aura:valueChange` Indicates that an attribute value has changed.

`aura:valueDestroy` Indicates that a component has been destroyed.

`aura:valueInit` Indicates that an app or component has been initialized.

`aura:valueRender` Indicates that an app or component has been rendered or rerendered.

`aura:waiting` (deprecated) Indicates that the app is waiting for a response to a server request.

Note: The `aura:waiting` event is deprecated. The
`aura:waiting` application event is fired for every server request, even
for requests from other components in your app. Unless your component
is running in complete isolation in a standalone app and not included in
Lightning Experience or the Salesforce mobile app, the container app may
trigger your event handler multiple times. This behavior makes it difficult
to handle each event appropriately.


# CHAPTER 6 Communicating Across the DOM with Lightning

Message Service

In this chapter ...

**•** Create a Message
Channel

Use Lightning message service to communicate across the DOM within a Lightning page. Communicate
between Visualforce pages embedded in the same Lightning page, Aura components, and Lightning
web components, including components in a utility bar and pop-out utilities. Choose whether a
component subscribes to messages from the entire application, or from only the active area.

**•** Publish on a
If you're switching from Salesforce Classic to Lightning Experience, you can build Lightning web
Message Channel
components that can communicate with existing Visualforce pages or Aura components. You can also

**•** Subscribe to a
use Lightning message service to communicate with softphones via Open CTI.
Message Channel

**•** Lightning Message Important: Lightning message service is available in Lightning Experience and as a beta feature
Service Limitations for Lightning components used in Experience Builder sites.

To access Lightning message service in Aura, use the `lightning:messageChannel` component.
A message is a serializable JSON object. Examples of data that you can pass in a message include strings,
numbers, booleans, and objects. A message can’t contain functions and symbols. The
`lightning:messageChannel` component is only available in Lightning Experience.

SEE ALSO:

[Blog: Lightning Message Service](https://developer.salesforce.com/blogs/2019/10/lightning-message-service-developer-preview.html)

_Lightning Web Components Developer Guide_ [: Communicating Across the DOM with Lightning Message](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/message_channel_intro.htm)
[Service](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/message_channel_intro.htm)

_Visualforce Developer Guide_ [: Communicating Across the DOM with Lightning Message Service](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/message_channel_intro.htm)

_Open CTI Developer Guide_ [: Lightning Message Service Methods for Lightning Experience](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_cti.meta/api_cti/sforce_api_cti_methods_lms.htm)


## Communicating Across the DOM with Lightning Message Create a Message Channel

Service

## Create a Message Channel

To create a `lightning:messageChannel` component in your org, use the LightningMessageChannel metadata type and append
it with `__c` . The message channel isn’t a custom object, it just uses the same suffix.

[Note: See LightningMessageChannel in the Metadata API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_lightningmessagechannel.htm)

To deploy a LightningMessageChannel into your org, create a Salesforce DX project. Include the XML definition in the
`force-app/main/default/messageChannels/` directory. The LightningMessageChannel file name follows the format
_`messageChannelName`_ .messageChannel-meta.xml. To deploy it to your scratch org, sandbox, or Developer Edition org, run the
`sf project deploy start` Salesforce CLI command.

SEE ALSO:

[Trailhead: Set Up Salesforce DX](https://trailhead.salesforce.com/en/content/learn/modules/sfdx_app_dev/sfdx_app_dev_setup_dx)

[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_intro.htm)

## Publish on a Message Channel

To publish a message on a message channel, include a `lightning:messageChannel` component in your Aura component and
use the `publish()` method in your Aura component's controller file.

Example: The `lmsPublisherAuraComponent` [from the github.com/trailheadapps/lwc-recipes repo shows how to](https://github.com/trailheadapps/lwc-recipes)
publish a message to notify subscribers on a Lightning page when a contact is selected.

To reference a message channel, add the `lightning:messageChannel` component to your Aura component. The component
has a required `type` attribute, which is the name of the message channel.

```
   <!-- myComponent.cmp -->

   <aura:component>

      <lightning:messageChannel type="SampleMessageChannel__c"/>

   </aura:component>

```

To reference a message channel from an org that has a namespace, prefix the message channel name with the namespace:
`<lightning:messageChannel type="` _**`Namespace__MessageChannelName__c`**_ `"/>` .

This example shows how to publish a message on the `SampleMessageChannel__c` channel when a button is clicked.

In `myComponent.cmp`, we create two components, `lightning:button` and `lightning:messageChannel` . On
`lightning:button`, the `onclick` handler calls the `handleClick()` JavaScript function in the controller. We assign the
`aura:id` attribute to `lightning:messageChannel` to access the `publish()` method.

```
   <!-- myComponent.cmp -->

   <aura:component>

      <lightning:button onclick="{! c.handleClick }"/>

      <lightning:messageChannel type="SampleMessageChannel__c"

        aura:id="sampleMessageChannel"/>

   </aura:component>

   // myComponentController.js

   ({

      handleClick: function(cmp, event, helper) {

        var payload = {

```


## Communicating Across the DOM with Lightning Message Subscribe to a Message Channel

Service

```
           recordId: "some string",

           recordData: {

             value: "some value"

           }

        };

        cmp.find("sampleMessageChannel").publish(payload);

      }

   })

```

In the controller, `handleClick()` contains the `payload` object. This object holds the message that gets sent on the
`SampleMessageChannel__c` message channel. Here, the message is a `recordId` with the value "some string" and
`recordData`, whose value is the key-value pair `value: "some value"` . Then, the controller finds the
`lightning:messageChannel` component referenced in `myComponent.cmp` and calls `publish()` with the payload.

Note: Lightning message service publishes messages to any subscribed component until the destroy phase of the component's
lifecycle, even if the component isn't visible. Sometimes when you navigate away from a Lightning page, components are cached
and not destroyed. These components still receive messages. For more information, see lifecycle on page 294 and related system
events on page 298

## Subscribe to a Message Channel

To subscribe to a message channel, create a handler method to run when it receives a message.

Example: The `lmsSubscriberAuraComponent` [from the github.com/trailheadapps/lwc-recipes repo shows how to](https://github.com/trailheadapps/lwc-recipes)
subscribe and unsubscribe from a message channel.

In this example, we define an Aura component called `myNewComponent` that contains the custom message channel,
`SampleMessageChannel__c` . The `lightning:messageChannel` component's `onMessage` attribute calls the
`handleChanged` method in the client-side controller.

By default, communication over a message channel can occur only between components in an active navigation tab, an active navigation
item, or a utility item. Utility items are always active. A navigation tab or item is active when it’s selected. Navigation tabs and items
include:

**•** Standard navigation tabs

**•** Console navigation workspace tabs

**•** Console navigations subtabs

**•** Console navigation items

To receive messages on a message channel from anywhere in the application, use `lightning:messageChannel` 's optional
parameter, `scope` . Set `scope` to the value `"APPLICATION"` .

```
   <lightning:messageChannel type=" messageChannel " onMessage="{! listener }"

   scope="APPLICATION"/>

```

The component `myNewComponent` detects a new message and updates the display value.

```
   <!-- myNewComponent.cmp -->

   <aura:component>

      <aura:attribute name="recordValue" type="String"/>

      <lightning:formattedText value="{!v.recordValue}" />

      <lightning:messageChannel type="SampleMessageChannel__c"

```


## Communicating Across the DOM with Lightning Message Lightning Message Service Limitations

Service

```
         onMessage="{!c.handleChanged}"/>

   </aura:component>

   // myNewComponentController.js

   ({

      handleChanged: function(cmp, message, helper) {

      // Read the message argument to get the values in the message payload

      if (message != null && message.getParam("recordData") != null) {

        cmp.set("v.recordValue", message.getParam("recordData").value);

      }

     }

   })

```

Write the handler in your component's client-side controller. The `handleChanged` method fires when there is a new message. It
checks whether there is a payload in the message, and if so, assigns the new data to the `v.recordValue` attribute. The
`lightning:formattedText` element updates to display the new value.

## Lightning Message Service Limitations

Keep the following in mind when working with Lightning message service.

**Supported Experiences**
Lightning message service supports only the following experiences:

**•** Lightning Experience standard navigation

**•** Lightning Experience console navigation

**•** Salesforce mobile app for Aura and Lightning Web Components, but not for Visualforce pages

**•** Lightning components used in Experience Builder sites.

Note: Lightning Message Service doesn't work with Salesforce Tabs + Visualforce sites or with Visualforce pages in
Experience Builder sites.

**Aura Components That Don’t Render Aren’t Supported**
Lightning message service only supports Aura components that render. You can’t use `lightning:messageChannel` in an
Aura component that uses the background utility item interface. Similarly, Aura components that use
`lightning:messageChannel` can’t call Lightning Message Service methods in the `init` lifecycle handler because the
component hasn’t rendered.

**`lightning:messageChannel`** **Must Be a Child of** **`aura:component`**
In a custom Aura component, `lightning:messageChannel` must be an immediate child of the `aura:component` tag.
It can’t be nested in an HTML tag or another component.

For example, the following code renders without a problem.

```
     <aura:component>

      <lightning:messageChannel type="myMessageChannel__c" />

      <lightning:card>...</lightning:card>

     </aura:component>

```

This code throws an error when the Aura component tries to render.

```
     <aura:component>

      <lightning:card>

       <lightning:messageChannel type="myMessageChannel__c" />

```


Communicating Across the DOM with Lightning Message Lightning Message Service Limitations
Service

```
      </lightning:card>

     </aura:component>

```

**Messages are Constrained by iframe Boundary**
If your component uses Lightning message service to publish a message, that message is constrained by any iframe boundary. To
work around this limitation, use the `sforce.one.subscribe()` and `[sforce.one.unsubscribe()](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/message_channel_subscribe.htm)` methods.

**Avoid Dynamically Creating lightning:messageChannel Components in Aura**
Do not use `createComponent()` on page 476 to dynamically create a `lightning:messageChannel` component in
Aura. Dynamically created components may not work as expected. For information on supported ways to create a
`lightning:messageChannel` component, see Create a Message Channel on page 300.

SEE ALSO:

[Invoking Actions on Component Initialization](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/js_cb_init_handler.htm)

_Component Reference_ : `[lightning:backgroundUtilityItem](https://developer.salesforce.com/docs/component-library/bundle/lightning:backgroundUtilityItem/documentation)`


# CHAPTER 7 Creating Apps

In this chapter ... Components are the building blocks of an app. This section shows you a typical workflow to put the
pieces together to create a new app.

**•** App Overview
First, you should decide whether you’re creating a component for a standalone app or for Salesforce

**•** Designing App UI
apps, such as Lightning Experience or Salesforce for Android, iOS, and mobile web. Both components
# • Creating App can access your Salesforce data, but only a component created for Lightning Experience or Salesforce

Templates

for Android, iOS, and mobile web can automatically handle Salesforce events that take advantage of

**•** Using the AppCache record create and edit pages, among other benefits.

**•** Distributing
Applications and
Components

The Quick Start on page 6 walks you through creating components for a standalone app and
components for Salesforce for Android, iOS, and mobile web to help you determine which one you need.


## Creating Apps App Overview App Overview

An app is a special top-level component whose markup is in a `.app` resource.

On a production server, the `.app` resource is the only addressable unit in a browser URL. Access an app using the URL:

`https://` _`MyDomainName`_ `.lightning.force.com/<namespace>/<appName>.app` .

SEE ALSO:

aura:application

Supported HTML Tags

## Designing App UI

Design your app's UI by including markup in the `.app` resource. Each part of your UI corresponds to a component, which can in turn
contain nested components. Compose components to create a sophisticated app.

An app’s markup starts with the `<aura:application>` tag.

Note: Creating a standalone app enables you to host your components outside of Salesforce for Android, iOS, and mobile web
or Lightning Experience, such as with Lightning Out or Lightning components in Visualforce pages. To learn more about the
`<aura:application>` tag, see aura:application.

Let's look at a `sample.app` file, which starts with the `<aura:application>` tag.

```
   <aura:application extends="force:slds">

      <lightning:layout>

        <lightning:layoutItem padding="around-large">

           <h1 class="slds-text-heading_large">Sample App</h1>

        </lightning:layoutItem>

      </lightning:layout>

      <lightning:layout>

        <lightning:layoutItem padding="around-small">

           Sidebar

           <!-- Other component markup here -->

        </lightning:layoutItem>

        <lightning:layoutItem padding="around-small">

           Content

           <!-- Other component markup here -->

        </lightning:layoutItem>

      </lightning:layout>

   </aura:application>

```

The `sample.app` file contains HTML tags, such as `<h1>`, as well as components, such as `<lightning:layout>` . We won't go
into the details for all the components here but note how simple the markup is. The `<lightning:layoutItem>` component
can contain other components or HTML markup.

SEE ALSO:

aura:application


## Creating Apps Creating App Templates Creating App Templates

An app template bootstraps the loading of the framework and the app. Customize an app’s template by creating a component that
extends the default `aura:template` template.

A template must have the `isTemplate` system attribute in the `<aura:component>` tag set to `true` . This informs the framework
to allow restricted items, such as `<script>` tags, which aren't allowed in regular components.

A component with the `isTemplate` system attribute set to `true` can’t be used on a site page. To use a component on a site page,
the `isTemplate` system attribute can’t be set to `true` .

For example, a sample app has a `np:template` template that extends `aura:template` . `np:template` looks like:

```
   <aura:component isTemplate="true" extends="aura:template">

      <aura:set attribute="title" value="My App"/>

      ...

   </aura:component>

```

Note how the component extends `aura:template` and sets the `title` attribute using `aura:set` .

The app points at the custom template by setting the `template` system attribute in `<aura:application>` .

```
   <aura:application template="np:template">

      ...

   </aura:application>

```

A template can only extend a component or another template. A component or an application can't extend a template.

## Using the AppCache

AppCache support is deprecated. Browser vendors have deprecated AppCache, so we followed their lead. Remove the `useAppcache`
attribute in the `<aura:application>` tag of your standalone apps ( `.app` resources) to avoid cross-browser support issues due
to deprecation by browser vendors.

If you don’t currently set `useAppcache` in an `<aura:application>` tag, you don’t have to do anything because the default
value of `useAppcache` is `false` .

[Note: See an introduction to AppCache for more information.](http://www.html5rocks.com/en/tutorials/appcache/beginner/)

SEE ALSO:

aura:application

## Distributing Applications and Components

As an ISV or Salesforce partner, you can package and distribute applications and components to other Salesforce users and organizations,
including those outside your company.

Publish applications and components to and install them from AppExchange.

A managed package ensures that your application and other resources are fully upgradeable. To create and work with managed packages,
you must register a namespace prefix. A managed package includes your namespace prefix in the component names and prevents
naming conflicts in an installer’s organization. After a managed package is released, the application or component names are locked,
but the package developer can still edit these attributes.


### Creating Apps Apex Class Considerations for Packages

**•** API Version

**•** Description

**•** Label

**•** Language

**•** Markup

IN THIS SECTION:

### Apex Class Considerations for Packages

Keep these considerations in mind when you develop Apex classes for packages.

Adding Aura Components to Managed Packages
Add an Aura component to a managed package from a package detail page in Setup.

Deleting Aura Components from Managed Packages
After you’ve released a managed package, you may decide to refactor the package and delete an Aura component. It’s your
responsibility to educate your customers about the potential impact from any components you delete. In the Release Notes for your
upgraded package, list all custom components you’ve deleted and notify customers of any necessary actions.

SEE ALSO:

_[Second-Generation Managed Packaging Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)_

_[First-Generation Managed Packaging Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/sharing_apps.htm)_

Testing Your Apex Code

### Apex Class Considerations for Packages

Keep these considerations in mind when you develop Apex classes for packages.

Test Coverage

Any Apex that is included as part of your definition bundle must have at least 75% cumulative test coverage. When you upload your
package to AppExchange, all tests are run to ensure that they run without errors. The tests are also run when the package is installed.

Grant User Access for Apex Classes

An authenticated or guest user can access an `@AuraEnabled` Apex method only when the user’s profile or an assigned permission
set allows access to the Apex class.

**•** To enable access to a `public` Apex controller that’s part of a managed package, a subscriber org must use a permission set. You
can’t enable access to a `public` Apex controller from a managed package using a user profile.

**•** To enable access to a `global` Apex controller that’s part of a managed package, a subscriber org can use a permission set or a
user profile.

Apex Class Usage in Subscriber Orgs

Only methods marked with the `global` access modifier are accessible by Aura components from outside the managed package’s
namespace. Methods marked with the `public` access modifier are accessible only to Aura components included in the managed
package’s namespace.


### Creating Apps Adding Aura Components to Managed Packages

If you declare an Apex method as `global`, you must also declare the Apex class that contains it as `global` .

An Aura component outside the package can access a public Apex method installed from a non-namespaced unlocked package. The
Aura component can be installed from another package or created in the org. For accessing Apex methods, a non-namespaced unlocked
package is treated the same as an unmanaged package.

SEE ALSO:

Granting User Access for Apex Classes

Apex Server-Side Controller Overview

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_access_modifiers.htm)_ : Access Modifiers

### Adding Aura Components to Managed Packages

Add an Aura component to a managed package from a package detail page in Setup.

When you add an application or component to a package, all definition bundles referenced by the application or component are
automatically included, such as other components, events, and interfaces. Custom fields, custom objects, list views, page layouts, and
Apex classes referenced by the application or component are also included.

However, when you add a custom object to a package, you must explicitly add the application and other definition bundles that reference
that custom object to the package. Other dependencies that you must add to a package explicitly include the following.

**•** Trusted URLs

**•** Remote Site Settings

SEE ALSO:

_[Second-Generation Managed Packaging Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)_

_[First-Generation Managed Packaging Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/sharing_apps.htm)_

### Deleting Aura Components from Managed Packages

After you’ve released a managed package, you may decide to refactor the package and delete an Aura component. It’s your responsibility
to educate your customers about the potential impact from any components you delete. In the Release Notes for your upgraded package,
list all custom components you’ve deleted and notify customers of any necessary actions.

[Note: To enable component deletion in your packaging org, log a case in the Partner Community.](https://partners.salesforce.com/)

To delete an Aura component from a managed package:

**1.** From Setup, enter _`Lightning Components`_ in the Quick Find box.

**2.** Select **Lightning Components** .

### 3. Click Del for the component that you want to delete.


Creating Apps Deleting Aura Components from Managed Packages

You can delete an Aura component from the Developer Console also.

Note: When a developer removes an Aura component from a package, the component remains in a subscriber’s org after they
install the upgraded package. The administrator of the subscriber’s org can delete the component, if desired. This behavior is the
same for an Aura component with a `public` or `global` access value.

The `access` attribute on the `aura:component` tag can be set to `public` or `global` to control whether the component can
be used outside of the component’s namespace.

We recommend a two-stage process to package developers when you delete an Aura component with `global` access. This process
ensures that a global component that you delete from the package has no dependencies on the other items in the package.

**1.** Stage one: Remove references

**a.** Edit the global component that you want to delete to remove all references to other Lightning components.

**b.** Upload your new package version.

**c.** Push the stage-one upgrade to your subscribers.

**2.** Stage two: Delete your obsolete component

**a.** Delete the global Lightning component from the package.

**b.** Optionally, delete other related components and classes.

**c.** Upload your new package version.

**d.** Push the stage-two upgrade to your subscribers.

SEE ALSO:

Component Access Control

_Second-Generation Managed Packaging Developer Guide_ [: Remove Metadata Components from Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

_First-Generation Managed Packaging Developer Guide_ [: Delete Components from First-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/packaging_managed_component_deletion.htm)


# CHAPTER 8 Styling Apps

In this chapter ... An app is a special top-level component whose markup is in a `.app` resource. Just like any other
component, you can put CSS in its bundle in a resource called `<appName>.css` .

**•** Using the Salesforce
Lightning Design
System in Apps

For example, if the app markup is in `notes.app`, its CSS is in `notes.css` .

System in Apps When viewed in Salesforce for Android, iOS, and Lightning Experience, the components include styling

**•** Using External CSS that matches those visual themes. For example, the `lightning:button` includes the
`slds-button_neutral` class to display a neutral style.

**•** More Readable
Styling Markup with
Note: Styles added to Lightning components in Salesforce for Android, iOS, and Lightning
the join Expression
Experience don’t apply to components in standalone apps.

**•** Tips for CSS in
Components

SEE ALSO:

**•** CSS for RTL
Languages CSS in Components

**•** Vendor Prefixes

**•** Styling with Design
Tokens and Styling
Hooks


## Styling Apps Using the Salesforce Lightning Design System in Apps Using the Salesforce Lightning Design System in Apps

The Salesforce Lightning Design System (SLDS) provides a look and feel that’s consistent with Lightning Experience. Use Lightning
Design System styles to give your custom stand-alone Lightning applications a UI that is consistent with Salesforce, without having to
reverse-engineer our styles.

Your application automatically gets Lightning Design System styles and design tokens if it extends `force:slds` . This method is the
easiest way to stay up to date and consistent with Lightning Design System enhancements.

To extend `force:slds` :

```
   <aura:application extends="force:slds">

      <!-- customize your application here -->

   </aura:application>

```

Using a Static Resource

When you extend `force:slds`, the version of Lightning Design System styles is automatically updated whenever the CSS changes.
If you want to use a specific Lightning Design System version, download the version and add it to your org as a static resource.

Note: We recommend extending `force:slds` instead so that you automatically get the latest Lightning Design System styles.
If you stick to a specific Lightning Design System version, your app’s styles will gradually start to drift from later versions in Lightning
Experience or incur the cost of duplicate CSS downloads.

To download a version of Lightning Design System that doesn’t exceed the maximum size for a static resource, go to the Lightning
[Design System downloads page.](https://www.lightningdesignsystem.com/resources/downloads/)

Salesforce recommends that you name the Lightning Design System archive static resource using the name format SLDS _`###`_, where
_`###`_ is the Lightning Design System version number (for example, _`SLDS252`_ ). This lets you have multiple versions of the Lightning
Design System installed, and manage version usage in your components.

To use the static version of the Lightning Design System in a component, include it using `<ltng:require/>` . For example:

```
   <aura:component>

      <ltng:require

        styles="{!$Resource.SLDS252 +

           '/styles/salesforce-lightning-design-system.min.css'}" />

   </aura:component>

```

SEE ALSO:

Styling with Design Tokens and Styling Hooks

## Using External CSS

To reference an external CSS resource, upload it as a static resource and use a `<ltng:require>` tag in your `.cmp` or `.app` markup.

`ltng:require` enables you to load external CSS and JavaScript libraries for your component or app.

Important: You can’t load JavaScript resources from a third-party site, even if it’s a CSP Trusted Site. To use a JavaScript library
from a third-party site, add it to a static resource, and then add the static resource to your component. After the library is loaded
from the static resource, you can use it as normal.


Styling Apps Using External CSS

Here’s an example of using `ltng:require` :

```
   <ltng:require styles="{!$Resource. resourceName }" />

```

_`resourceName`_ is the `Name` of the static resource. In a managed package, the resource name must include the package namespace
prefix, such as `$Resource.yourNamespace__resourceName` . For a stand-alone static resource, such as an individual graphic
or script, you only need the name of the resource. For example, if you uploaded `myScript.js` and set the `Name` to `myScript`,
reference it as `$Resource.myScript` . To reference an item within an archive static resource, add the rest of the path to the item
using string concatenation.

Here are some considerations for loading styles:

**Loading Sets of CSS**
Specify a comma-separated list of resources in the `styles` attribute to load a set of CSS.

Note: Due to a quirk in the way `$Resource` is parsed in expressions, use the `join` operator to include multiple
`$Resource` references in a single attribute. For example, if you have more than one style sheet to include into a component
the `styles` attribute should be something like the following.

```
       styles="{!join(',',

          $Resource.myStyles + '/stylesheetOne.css',

          $Resource.myStyles + '/moreStyles.css')}"

```

**Loading Order**
The styles are loaded in the order that they are listed.

**One-Time Loading**
The styles load only once, even if they’re specified in multiple `<ltng:require>` tags in the same component or across different
components.

**Encapsulation**
To ensure encapsulation and reusability, add the `<ltng:require>` tag to every `.cmp` or `.app` resource that uses the CSS
resource.

`ltng:require` also has a `scripts` attribute to load a list of JavaScript libraries. The `afterScriptsLoaded` event enables
you to call a controller action after the `scripts` are loaded. It's only triggered by loading of the `scripts` and is never triggered
when the CSS in `styles` is loaded.

Styling Components for Lightning Experience or Salesforce for Android, iOS,
and mobile web

To prevent styling conflicts in Lightning Experience or Salesforce for Android, iOS, and mobile web, prefix your external CSS with a unique
namespace. For example, if you prefix your external CSS declarations with `.myBootstrap`, wrap your component markup with a
`<div>` tag that specifies the `myBootstrap` class.

```
   <ltng:require styles="{!$Resource.bootstrap}"/>

   <div class="myBootstrap">

      <c:myComponent />

      <!-- Other component markup -->

   </div>

```


## Styling Apps More Readable Styling Markup with the join Expression

Note: Prefixing your CSS with a unique namespace only applies to external CSS. If you’re using CSS within a component bundle,
the `.THIS` keyword becomes `.namespaceComponentName` during runtime.

SEE ALSO:

Using External JavaScript Libraries

CSS in Components

$Resource

## More Readable Styling Markup with the join Expression

Markup can get messy when you specify the class names to apply based on the component attribute values. Try using a `join` expression
for easier-to-read markup.

This example sets the class names based on the component attribute values. It’s readable, but the spaces between class names are easy
to forget.

```
   <li class="{! 'calendarEvent ' +

      v.zoomDirection + ' ' +

      (v.past ? 'pastEvent ' : '') +

      (v.zoomed ? 'zoom ' : '') +

      (v.multiDayFragment ? 'multiDayFragment ' : '')}">

      <!-- content here -->

   </li>

```

Sometimes, if the markup is not broken into multiple lines, it can hurt your eyes or make you mutter profanities under your breath.

```
   <li class="{! 'calendarEvent ' + v.zoomDirection + ' ' + (v.past ? 'pastEvent ' : '') +

   (v.zoomed ? 'zoom ' : '') + (v.multiDayFragment ? 'multiDayFragment ' : '')}">

      <!-- content here -->

   </li>

```

Try using a `join` expression instead for easier-to-read markup. This example `join` expression sets `' '` as the first argument so that
you don’t have to specify it for each subsequent argument in the expression.

```
   <li

      class="{! join(' ',

        'calendarEvent',

        v.zoomDirection,

        v.past ? 'pastEvent' : '',

        v.zoomed ? 'zoom' : '',

        v.multiDayFragment ? 'multiDayFragment' : ''

      )}">

      <!-- content here -->

   </li>

```

You can also use a `join` expression for dynamic styling.

```
   <div style="{! join(';',

      'top:' + v.timeOffsetTop + '%',

      'left:' + v.timeOffsetLeft + '%',

      'width:' + v.timeOffsetWidth + '%'

   )}">

```


## Styling Apps Tips for CSS in Components

```
      <!-- content here -->

   </div>

```

SEE ALSO:

Expression Functions Reference

## Tips for CSS in Components

Here are some tips for configuring the CSS for components that you plan to use in Lightning pages, the Lightning App Builder, or the
Experience Builder.

**Components must be set to 100% width**
Because they can be moved to different locations on a Lightning page, components must not have a specific width nor a left or
right margin. Components should take up 100% of whatever container they display in. Adding a left or right margin changes the
width of a component and can break the layout of the page.

**Don’t remove HTML elements from the flow of the document**
Some CSS rules remove the HTML element from the flow of the document. For example:

```
     float: left;

     float: right;

     position: absolute;

     position: fixed;

```

Because they can be moved to different locations on the page as well as used on different pages entirely, components must rely on
the normal document flow. Using floats and absolute or fixed positions breaks the layout of the page the component is on. Even if
they don’t break the layout of the page _you’re_ looking at, they will break the layout of _some_ page the component can be put on.

**Child elements shouldn’t be styled to be larger than the root element**
The Lightning page maintains consistent spacing between components, and can’t do that if child elements are larger than the root
element.

For example, avoid these patterns:

```
     <div style="height: 100px">

      <div style="height: 200px">

       <!--Other markup here-->

      </div>

     </div>

     <!--Margin increases the element’s effective size-->

     <div style="height: 100px">

      <div style="height: 100px margin: 10px">

       <!--Other markup here-->

      </div>

     </div>

## CSS for RTL Languages

```

When your Language setting in Salesforce is set to a right-to-left (RTL) language, the framework automatically flips property names,
such as `left` and `border-left` to `right` and `border-right` respectively. The framework also rearranges certain values
like `padding`, `margin`, and `border-radius` so that the `right` and `left` units are swapped.


Styling Apps CSS for RTL Languages

Flipped CSS Properties

These properties are automatically flipped for RTL languages.

Flipped CSS Keywords

These keywords are automatically flipped for RTL languages.


Styling Apps CSS for RTL Languages

Flipped CSS Percentage Values

If the value is a percentage for these properties, the flipped value is set to 100 minus the value.

**•** `background`

**•** `background-position`

**•** `background-position-x`

Flipped Property Arguments

For these properties that can take four values, the second and fourth values are swapped. For example, `property: A B C D`
becomes `property: A D C B` .

**•** `padding`

**•** `margin`

**•** `border-color`

**•** `border-style`

**•** `border-width`

Flipped **`border-radius`** Arguments

The arguments for the `border-radius` property are flipped with these patterns.


## Styling Apps Vendor Prefixes

Override Flipping With **`@noflip`**

To override the automatic flipping, add a `/*@noflip*/` annotation in a comment directly before the property. For example:

```
   .THIS.mycontainer {

      /*@noflip*/ direction : rtl;

   }

```

Use Conditional CSS

Use the `@if(isRTL)` conditional statement to manually provide the appropriately oriented CSS for each direction.

```
   .THIS {

      transform: skew(28deg) translate3d(0, 0, 0);

   }

   @if(isRTL) {

      .THIS {

        transform: skew(-28deg) translate3d(0, 0, 0);

      }

   }

```

SEE ALSO:

_Salesforce Help_ [: Right-to-Left (RTL) Language Support](https://help.salesforce.com/articleView?id=faq_getstart_rtl.htm&language=en_US)

## Vendor Prefixes

Vendor prefixes, such as `—moz-` and `—webkit-` among many others, are automatically added in Lightning.

You only need to write the unprefixed version, and the framework automatically adds any prefixes that are necessary when generating
the CSS output. If you choose to add them, they are used as-is. This enables you to specify alternative values for certain prefixes.

Example: For example, this is an unprefixed version of `border-radius` .

```
      .class {

       border-radius: 2px;

      }

```

The previous declaration results in the following declarations.

```
      .class {

       -webkit-border-radius: 2px;

       -moz-border-radius: 2px;

       border-radius: 2px;

      }

```


## Styling Apps Styling with Design Tokens and Styling Hooks Styling with Design Tokens and Styling Hooks

Capture the essential values of your visual design into named tokens or global styling hooks. Reuse these values throughout your
Lightning components CSS resources. Tokens and styling hooks make it easy to ensure that your design is consistent, and even easier
to update your design as it evolves.

[Important: Salesforce recommends that you use Styling Hooks instead of design tokens if possible. While existing design tokens](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)
still work, styling hooks are the future of customization for Lightning web components and Aura components. See Replace Design
Tokens with Styling Hooks.

Design tokens and styling hooks are visual design “atoms” for building a design for your components or apps. Specifically, they’re named
entities that store visual design attributes: pixel values for margins and spacing, font sizes and families, or hex values for colors. Both
design tokens and styling hooks are a terrific way to centralize the low-level values, which you then use to compose the styles that make
up the design of your component or app.

IN THIS SECTION:

### Tokens Bundles

Tokens are a type of bundle, just like components, events, and interfaces.

Create a Tokens Bundle
Create a tokens bundle in your org using the Developer Console.

Defining and Using Tokens
A token is a name-value pair that you specify using the `<aura:token>` component. Define tokens in a tokens bundle, and then
use tokens in your components’ CSS styles resources.

Using Expressions in Tokens
Tokens support a restricted set of expressions. Use expressions to reuse one token value in another token, or to combine tokens to
form a more complex style property.

Extending Tokens Bundles
Use the `extends` attribute to extend one tokens bundle from another.

Using Standard Design Tokens
Salesforce exposes a set of “base” tokens that you can access in your component style resources. Use these standard tokens to mimic
the look-and-feel of the Salesforce Lightning Design System (SLDS) in your own custom components.

Replace Design Tokens with Styling Hooks
If you use design tokens to customize the styling of your Aura components, use SLDS global styling hooks instead. Custom components
that use design tokens still work, but they no longer receive updates after LWC API version 61.0. By using styling hooks, you can
cleanly adopt future product innovations and updated web accessibility standards.

### Tokens Bundles

Tokens are a type of bundle, just like components, events, and interfaces.

[Important: Salesforce recommends that you use Styling Hooks instead of design tokens if possible. While existing design tokens](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)
still work, styling hooks are the future of customization for Lightning web components and Aura components. See Replace Design
Tokens with Styling Hooks.

A tokens bundle contains only one resource, a tokens collection definition.


### Styling Apps Create a Tokens Bundle

**Resource** **Resource Name** **Usage**

Tokens Collection `defaultTokens.tokens`

The only required resource in a tokens bundle. Contains markup
for one or more tokens. Each tokens bundle contains only one
tokens resource.

Note: You can’t edit the tokens bundle name or description in the Developer Console after you create it. The bundle’s
`AuraBundleDefinition` can be modified using the Metadata API.

A tokens collection starts with the `<aura:tokens>` tag. It can only contain `<aura:token>` tags to define tokens.

Tokens collections have restricted support for expressions; see Using Expressions in Tokens. You can’t use other markup, renderers,
controllers, or anything else in a tokens collection.

SEE ALSO:

Using Expressions in Tokens

### Create a Tokens Bundle

Create a tokens bundle in your org using the Developer Console.

[Important: Salesforce recommends that you use Styling Hooks instead of design tokens if possible. While existing design tokens](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)
still work, styling hooks are the future of customization for Lightning web components and Aura components. See Replace Design
Tokens with Styling Hooks.

To create a tokens bundle:

**1.** In the Developer Console, select **File** - **New** - **Lightning Tokens** .

**2.** Enter a name for the tokens bundle.

Your first tokens bundle should be named _`defaultTokens`_ . The tokens defined within `defaultTokens` are automatically
accessible in your Lightning components. Tokens defined in any other bundle won’t be accessible in your components unless you
import them into the `defaultTokens` bundle.

You have an empty tokens bundle, ready to edit.

```
<aura:tokens>

</aura:tokens>

```

Note: You can’t edit the tokens bundle name or description in the Developer Console after you create it. The bundle’s
`AuraBundleDefinition` can be modified using the Metadata API. Although you can set a version on a tokens bundle,
doing so has no effect.

### Defining and Using Tokens

A token is a name-value pair that you specify using the `<aura:token>` component. Define tokens in a tokens bundle, and then use
tokens in your components’ CSS styles resources.

[Important: Salesforce recommends that you use Styling Hooks instead of design tokens if possible. While existing design tokens](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)
still work, styling hooks are the future of customization for Lightning web components and Aura components. See Replace Design
Tokens with Styling Hooks.


### Styling Apps Using Expressions in Tokens

Defining Tokens

Add new tokens as child components of the bundle’s `<aura:tokens>` component. For example:

```
   <aura:tokens>

      <aura:token name="myBodyTextFontFace"

            value="'Salesforce Sans', Helvetica, Arial, sans-serif"/>

      <aura:token name="myBodyTextFontWeight" value="normal"/>

      <aura:token name="myBackgroundColor" value="#f4f6f9"/>

      <aura:token name="myDefaultMargin" value="6px"/>

   </aura:tokens>

```

The only allowed attributes for the `<aura:token>` tag are `name` and `value` .

Using Tokens

Tokens created in the `defaultTokens` bundle are automatically available in components in your namespace. To use a design token,
reference it using the `token()` function and the token name in the CSS resource of a component bundle. For example:

```
   .THIS p {

      font-family: token(myBodyTextFontFace);

      font-weight: token(myBodyTextFontWeight);

   }

```

If you prefer a more concise function name for referencing tokens, you can use the `t()` function instead of `token()` . The two are
equivalent. If your token names follow a naming convention or are sufficiently descriptive, the use of the more terse function name
won’t affect the clarity of your CSS styles.

### Using Expressions in Tokens

Tokens support a restricted set of expressions. Use expressions to reuse one token value in another token, or to combine tokens to form
a more complex style property.

[Important: Salesforce recommends that you use Styling Hooks instead of design tokens if possible. While existing design tokens](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)
still work, styling hooks are the future of customization for Lightning web components and Aura components. See Replace Design
Tokens with Styling Hooks.

Cross-Referencing Tokens

To reference one token’s value in another token’s definition, wrap the token to be referenced in standard expression syntax.

In the following example, we reference tokens provided by Salesforce in our custom tokens. Although you can’t see the standard tokens
directly, imagine that they look something like the following.

```
   <!-- force:base tokens (SLDS standard tokens) -->

   <aura:tokens>

     ...

     <aura:token name="colorBackground" value="rgb(244, 246, 249)" />

     <aura:token name="fontFamily" value="'Salesforce Sans', Arial, sans-serif" />

     ...

   </aura:tokens>

```


Styling Apps Using Expressions in Tokens

With the preceding in mind, you can reference the standard tokens in your custom tokens, as in the following.

```
   <!-- defaultTokens.tokens (your tokens) -->

   <aura:tokens extends="force:base">

     <aura:token name="mainColor" value="{! colorBackground }" />

     <aura:token name="btnColor" value="{! mainColor }" />

     <aura:token name="myFont" value="{! fontFamily }" />

   </aura:tokens>

```

You can only cross-reference tokens defined in the same file or a parent.

Expression syntax in tokens resources is restricted to references to other tokens.

Combining Tokens

To support combining individual token values into more complex CSS style properties, the `token()` function supports string
concatenation. For example, if you have the following tokens defined:

```
   <!-- defaultTokens.tokens (your tokens) -->

   <aura:tokens>

     <aura:token name="defaultHorizonalSpacing" value="12px" />

     <aura:token name="defaultVerticalSpacing" value="6px" />

   </aura:tokens>

```

You can combine these two tokens in a CSS style definition. For example:

```
   /* myComponent.css */

   .THIS div.notification {

     margin: token(defaultVerticalSpacing + ' ' + defaultHorizonalSpacing);

     /* more styles here */

   }

```

You can mix tokens with strings as much as necessary to create the right style definition. For example, use `margin:`
`token(defaultVerticalSpacing + ' ' + defaultHorizonalSpacing + ' 3px');` to hard code the bottom
spacing in the preceding definition.

The only operator supported within the `token()` function is “+” for string concatenation.

Note: Since Winter ’21, we convert Aura tokens to CSS custom properties under the covers. CSS custom properties are a web
standard that wasn’t supported when we initially created Aura tokens. Concatenating an Aura token with another token that
defines a CSS unit isn’t supported due to how we convert the Aura tokens. The tokens are statically converted to custom properties
and can result in incorrect CSS syntax, which is then discarded by the CSS parser.

For example, don’t separate the size and unit into separate tokens.

```
   <!-- DO NOT DO THIS! -->

   <aura:token name="v24" value="24" />

   <aura:token name="px" value="px" />

```

If you concatenate the tokens, the CSS doesn’t work as you expect.

```
   .THIS { font-size: token(v24+px); }

```

The result is font-size: 24, though you might expect it to be font-size: 24px.


### Styling Apps Extending Tokens Bundles

Instead, define a size and unit in one token for this use case.

```
   <aura:token name="v24" value="24px" />

```

SEE ALSO:

Defining and Using Tokens

### Extending Tokens Bundles

Use the `extends` attribute to extend one tokens bundle from another.

[Important: Salesforce recommends that you use Styling Hooks instead of design tokens if possible. While existing design tokens](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)
still work, styling hooks are the future of customization for Lightning web components and Aura components. See Replace Design
Tokens with Styling Hooks.

To add tokens from one bundle to another, extend the “child” tokens bundle from the “parent” tokens, like this.

```
   <aura:tokens extends="yourNamespace:parentTokens">

      <!-- additional tokens here -->

   </aura:tokens>

```

Overriding tokens values works mostly as you’d expect: tokens in a child tokens bundle override tokens with the same name from a
parent bundle. The exception is if you’re using standard tokens. You can’t override standard tokens in Lightning Experience or the
Salesforce mobile app.

Important: Overriding standard token values is undefined behavior and unsupported. If you create a token with the same name
as a standard token, it overrides the standard token’s value in some contexts, and has no effect in others. This behavior will change
in a future release. Don’t use it.

SEE ALSO:

### Using Standard Design Tokens Using Standard Design Tokens

Salesforce exposes a set of “base” tokens that you can access in your component style resources. Use these standard tokens to mimic
the look-and-feel of the Salesforce Lightning Design System (SLDS) in your own custom components.

[Important: Salesforce recommends that you use Styling Hooks instead of design tokens if possible. While existing design tokens](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)
still work, styling hooks are the future of customization for Lightning web components and Aura components. See Replace Design
Tokens with Styling Hooks.

To add the standard tokens to your org, extend a tokens bundle from the base tokens, like so.

```
   <aura:tokens extends="force:base">

      <!-- your own tokens here -->

   </aura:tokens>

```

Once added to `defaultTokens` (or another tokens bundle that `defaultTokens` extends) you can reference tokens from
`force:base` just like your own tokens, using the `token()` function and token name. For example:

```
   .THIS p {

      font-family: token(fontFamily);

```


Styling Apps Using Standard Design Tokens

```
      font-weight: token(fontWeightRegular);

   }

```

You can mix-and-match your tokens with the standard tokens. It’s a best practice to develop a naming system for your own tokens to
make them easily distinguishable from standard tokens. Consider prefixing your token names with “my”, or something else easily
identifiable.

IN THIS SECTION:

#### Overriding Standard Tokens (Deprecated)

If you override design tokens for your custom components, replace them with SLDS styling hooks.

#### Standard Design Tokens— force:base

The standard tokens available are a subset of the design tokens offered in the Salesforce Lightning Design System (SLDS). The
following tokens are available when extending from `force:base` .

Standard Design Tokens for Experience Builder Sites
Use a subset of the standard design tokens to make your components compatible with the Theme panel in Experience Builder. The
Theme panel enables administrators to quickly style an entire site using these properties. Each property in the Theme panel maps
to one or more standard design tokens. When an administrator updates a property in the Theme panel, the system automatically
updates any Lightning components that use the tokens associated with that branding property.

SEE ALSO:

Extending Tokens Bundles

#### Overriding Standard Tokens (Deprecated)

If you override design tokens for your custom components, replace them with SLDS styling hooks.

Important: Overriding standard tokens is deprecated as of API version 61.0, the Summer ’24 release. We recommend that you
[use Styling Hooks instead. See Replace Design Tokens with Styling Hooks.](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)

SEE ALSO:

#### Standard Design Tokens— force:base Standard Design Tokens— force:base

The standard tokens available are a subset of the design tokens offered in the Salesforce Lightning Design System (SLDS). The following
tokens are available when extending from `force:base` .

[Important: Salesforce recommends that you use Styling Hooks instead of design tokens if possible. While existing design tokens](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)
still work, styling hooks are the future of customization for Lightning web components and Aura components. See Replace Design
Tokens with Styling Hooks.

Available Tokens

Important: The standard token values evolve along with SLDS. Available tokens and their values can change without notice.
Token values presented here are for example only.


Styling Apps Using Standard Design Tokens

**Token Name** **Example Value**

`borderWidthThin` 1px

`borderWidthThick` 2px

`spacingXxxSmall` 0.125rem

`spacingXxSmall` 0.25rem

`spacingXSmall` 0.5rem

`spacingSmall` 0.75rem

`spacingMedium` 1rem

`spacingLarge` 1.5rem

`spacingXLarge` 2rem

`varSpacingXxSmall` 0.25rem

`varSpacingXSmall` 0.5rem

`varSpacingSmall` 0.75rem

`varSpacingMedium` 1rem

`varSpacingLarge` 1.5rem

`varSpacingXLarge` 2rem

`varSpacingXxLarge` 3rem

`varSpacingVerticalXxSmall` 0.25rem

`varSpacingVerticalXSmall` 0.5rem

`varSpacingVerticalSmall` 0.75rem

`varSpacingVerticalMedium` 1rem

`varSpacingVerticalLarge` 1.5rem

`varSpacingVerticalXLarge` 2rem

`varSpacingVerticalXxLarge` 3rem

`varSpacingHorizontalXxSmall` 0.25rem

`varSpacingHorizontalXSmall` 0.5rem

`varSpacingHorizontalSmall` 0.75rem

`varSpacingHorizontalMedium` 1rem

`varSpacingHorizontalLarge` 1.5rem

`varSpacingHorizontalXLarge` 2rem

`varSpacingHorizontalXxLarge` 3rem


Styling Apps Using Standard Design Tokens

**Token Name** **Example Value**

`sizeXxSmall` 6rem

`sizeXSmall` 12rem

`sizeSmall` 15rem

`sizeMedium` 20rem

`sizeLarge` 25rem

`sizeXLarge` 40rem

`sizeXxLarge` 60rem

`squareIconUtilitySmall` 1rem

`squareIconUtilityMedium` 1.25rem

`squareIconUtilityLarge` 1.5rem

`squareIconLargeBoundary` 3rem

`squareIconLargeBoundaryAlt` 5rem

`squareIconLargeContent` 2rem

`squareIconMediumBoundary` 2rem

`squareIconMediumBoundaryAlt` 2.25rem

`squareIconMediumContent` 1rem

`squareIconSmallBoundary` 1.5rem

`squareIconSmallContent` .75rem

`squareIconXSmallBoundary` 1.25rem

`squareIconXSmallContent` .5rem

`fontWeightLight` 300

`fontWeightRegular` 400

`fontWeightBold` 700

`lineHeightHeading` 1.25

`lineHeightText` 1.375

`lineHeightReset` 1

`lineHeightTab` 2.5rem

`fontFamily` 'Salesforce Sans', Arial, sans-serif

`borderRadiusSmall` .125rem

`borderRadiusMedium` .25rem


Styling Apps Using Standard Design Tokens

**Token Name** **Example Value**

`borderRadiusLarge` .5rem

`borderRadiusPill` 15rem

`borderRadiusCircle` 50%

`colorBorder` rgb(216, 221, 230)

`colorBorderBrand` rgb(21, 137, 238)

`colorBorderError` rgb(194, 57, 52)

`colorBorderSuccess` rgb(75, 202, 129)

`colorBorderWarning` rgb(255, 183, 93)

`colorBorderTabSelected` rgb(0, 112, 210)

`colorBorderSeparator` rgb(244, 246, 249)

`colorBorderSeparatorAlt` rgb(216, 221, 230)

`colorBorderSeparatorInverse` rgb(42, 66, 108)

`colorBorderRowSelected` rgb(0, 112, 210)

`colorBorderRowSelectedHover` rgb(21, 137, 238)

`colorBorderButtonBrand` rgb(0, 112, 210)

`colorBorderButtonBrandDisabled` rgba(0, 0, 0, 0)

`colorBorderButtonDefault` rgb(216, 221, 230)

`colorBorderButtonInverseDisabled` rgba(255, 255, 255, 0.15)

`colorBorderInput` rgb(216, 221, 230)

`colorBorderInputActive` rgb(21, 137, 238)

`colorBorderInputDisabled` rgb(168, 183, 199)

`colorBorderInputCheckboxSelectedCheckmark` rgb(255, 255, 255)

`colorBackground` rgb(244, 246, 249)

`colorBackgroundAlt` rgb(255, 255, 255)

`colorBackgroundAltInverse` rgb(22, 50, 92)

`colorBackgroundRowHover` rgb(244, 246, 249)

`colorBackgroundRowActive` rgb(238, 241, 246)

`colorBackgroundRowSelected` rgb(240, 248, 252)

`colorBackgroundRowNew` rgb(217, 255, 223)

`colorBackgroundInverse` rgb(6, 28, 63)


Styling Apps Using Standard Design Tokens

**Token Name** **Example Value**

`colorBackgroundBrowser` rgb(84, 105, 141)

`colorBackgroundChromeMobile` rgb(0, 112, 210)

`colorBackgroundChromeDesktop` rgb(255, 255, 255)

`colorBackgroundHighlight` rgb(250, 255, 189)

`colorBackgroundModal` rgb(255, 255, 255)

`colorBackgroundModalBrand` rgb(0, 112, 210)

`colorBackgroundNotificationBadge` rgb(194, 57, 52)

`colorBackgroundNotificationBadgeHover` rgb(0, 95, 178)

`colorBackgroundNotificationBadgeFocus` rgb(0, 95, 178)

`colorBackgroundNotificationBadgeActive` rgb(0, 57, 107)

`colorBackgroundNotificationNew` rgb(240, 248, 252)

`colorBackgroundPayload` rgb(244, 246, 249)

`colorBackgroundShade` rgb(224, 229, 238)

`colorBackgroundStencil` rgb(238, 241, 246)

`colorBackgroundStencilAlt` rgb(224, 229, 238)

`colorBackgroundScrollbar` rgb(224, 229, 238)

`colorBackgroundScrollbarTrack` rgb(168, 183, 199)

`colorBrand` rgb(21, 137, 238)

`colorBrandDark` rgb(0, 112, 210)

`colorBackgroundModalButton` rgba(0, 0, 0, 0.07)

`colorBackgroundModalButtonActive` rgba(0, 0, 0, 0.16)

`colorBackgroundInput` rgb(255, 255, 255)

`colorBackgroundInputActive` rgb(255, 255, 255)

`colorBackgroundInputCheckbox` rgb(255, 255, 255)

`colorBackgroundInputCheckboxDisabled` rgb(216, 221, 230)

`colorBackgroundInputCheckboxSelected` rgb(21, 137, 238)

`colorBackgroundInputDisabled` rgb(224, 229, 238)

`colorBackgroundInputError` rgb(255, 221, 225)

`colorBackgroundPill` rgb(255, 255, 255)

`colorBackgroundToast` rgba(84, 105, 141, 0.95)


Styling Apps Using Standard Design Tokens

**Token Name** **Example Value**

`colorBackgroundToastSuccess` rgb(4, 132, 75)

`colorBackgroundToastError` rgba(194, 57, 52, 0.95)

`shadowDrag` 0 2px 4px 0 rgba(0, 0, 0, 0.40)

`shadowDropDown` 0 2px 3px 0 rgba(0, 0, 0, 0.16)

`shadowHeader` 0 2px 4px rgba(0, 0, 0, 0.07)

`shadowButtonFocus` 0 0 3px #0070D2

`shadowButtonFocusInverse` 0 0 3px #E0E5EE

`colorTextActionLabel` rgb(84, 105, 141)

`colorTextActionLabelActive` rgb(22, 50, 92)

`colorTextBrand` rgb(21, 137, 238)

`colorTextBrowser` rgb(255, 255, 255)

`colorTextBrowserActive` rgba(0, 0, 0, 0.4)

`colorTextDefault` rgb(22, 50, 92)

`colorTextError` rgb(194, 57, 52)

`colorTextInputDisabled` rgb(84, 105, 141)

`colorTextInputFocusInverse` rgb(22, 50, 92)

`colorTextInputIcon` rgb(159, 170, 181)

`colorTextInverse` rgb(255, 255, 255)

`colorTextInverseWeak` rgb(159, 170, 181)

`colorTextInverseActive` rgb(94, 180, 255)

`colorTextInverseHover` rgb(159, 170, 181)

`colorTextLink` rgb(0, 112, 210)

`colorTextLinkActive` rgb(0, 57, 107)

`colorTextLinkDisabled` rgb(22, 50, 92)

`colorTextLinkFocus` rgb(0, 95, 178)

`colorTextLinkHover` rgb(0, 95, 178)

`colorTextLinkInverse` rgb(255, 255, 255)

`colorTextLinkInverseHover` rgba(255, 255, 255, 0.75)

`colorTextLinkInverseActive` rgba(255, 255, 255, 0.5)

`colorTextLinkInverseDisabled` rgba(255, 255, 255, 0.15)


Styling Apps Using Standard Design Tokens

**Token Name** **Example Value**

`colorTextModal` rgb(255, 255, 255)

`colorTextModalButton` rgb(84, 105, 141)

`colorTextStageLeft` rgb(224, 229, 238)

`colorTextTabLabel` rgb(22, 50, 92)

`colorTextTabLabelSelected` rgb(0, 112, 210)

`colorTextTabLabelHover` rgb(0, 95, 178)

`colorTextTabLabelFocus` rgb(0, 95, 178)

`colorTextTabLabelActive` rgb(0, 57, 107)

`colorTextTabLabelDisabled` rgb(224, 229, 238)

`colorTextToast` rgb(224, 229, 238)

`colorTextWeak` rgb(84, 105, 141)

`colorTextIconBrand` rgb(0, 112, 210)

`colorTextButtonBrand` rgb(255, 255, 255)

`colorTextButtonBrandHover` rgb(255, 255, 255)

`colorTextButtonBrandActive` rgb(255, 255, 255)

`colorTextButtonBrandDisabled` rgb(255, 255, 255)

`colorTextButtonDefault` rgb(0, 112, 210)

`colorTextButtonDefaultHover` rgb(0, 112, 210)

`colorTextButtonDefaultActive` rgb(0, 112, 210)

`colorTextButtonDefaultDisabled` rgb(216, 221, 230)

`colorTextButtonDefaultHint` rgb(159, 170, 181)

`colorTextButtonInverse` rgb(224, 229, 238)

`colorTextButtonInverseDisabled` rgba(255, 255, 255, 0.15)

`colorTextIconDefault` rgb(84, 105, 141)

`colorTextIconDefaultHint` rgb(159, 170, 181)

`colorTextIconDefaultHover` rgb(0, 112, 210)

`colorTextIconDefaultActive` rgb(0, 57, 107)

`colorTextIconDefaultDisabled` rgb(216, 221, 230)

`colorTextIconInverse` rgb(255, 255, 255)

`colorTextIconInverseHover` rgb(255, 255, 255)


Styling Apps Using Standard Design Tokens

**Token Name** **Example Value**

`colorTextIconInverseActive` rgb(255, 255, 255)

`colorTextIconInverseDisabled` rgba(255, 255, 255, 0.15)

`colorTextLabel` rgb(84, 105, 141)

`colorTextPlaceholder` rgb(84, 105, 141)

`colorTextPlaceholderInverse` rgb(224, 229, 238)

`colorTextRequired` rgb(194, 57, 52)

`colorTextPill` rgb(0, 112, 210)

`durationInstantly` 0s

`durationImmediately` 0.05s

`durationQuickly` 0.1s

`durationPromptly` 0.2s

`durationSlowly` 0.4s

`durationPaused` 3.2s

`colorBackgroundButtonBrand` rgb(0, 112, 210)

`colorBackgroundButtonBrandActive` rgb(0, 57, 107)

`colorBackgroundButtonBrandHover` rgb(0, 95, 178)

`colorBackgroundButtonBrandDisabled` rgb(224, 229, 238)

`colorBackgroundButtonDefault` rgb(255, 255, 255)

`colorBackgroundButtonDefaultHover` rgb(244, 246, 249)

`colorBackgroundButtonDefaultFocus` rgb(244, 246, 249)

`colorBackgroundButtonDefaultActive` rgb(238, 241, 246)

`colorBackgroundButtonDefaultDisabled` rgb(255, 255, 255)

`colorBackgroundButtonIcon` rgba(0, 0, 0, 0)

`colorBackgroundButtonIconHover` rgb(244, 246, 249)

`colorBackgroundButtonIconFocus` rgb(244, 246, 249)

`colorBackgroundButtonIconActive` rgb(238, 241, 246)

`colorBackgroundButtonIconDisabled` rgb(255, 255, 255)

`colorBackgroundButtonInverse` rgba(0, 0, 0, 0)

`colorBackgroundButtonInverseActive` rgba(0, 0, 0, 0.24)

`colorBackgroundButtonInverseDisabled` rgba(0, 0, 0, 0)


Styling Apps Using Standard Design Tokens

**Token Name** **Example Value**

`lineHeightButton` 1.875rem

`lineHeightButtonSmall` 1.75rem

`colorBackgroundAnchor` rgb(244, 246, 249)

[For a complete list of the design tokens available in the SLDS, see Design Tokens on the Lightning Design System site.](https://www.lightningdesignsystem.com/design-tokens/)

SEE ALSO:

Extending Tokens Bundles

#### Standard Design Tokens for Experience Builder Sites

Use a subset of the standard design tokens to make your components compatible with the Theme panel in Experience Builder. The
Theme panel enables administrators to quickly style an entire site using these properties. Each property in the Theme panel maps to
one or more standard design tokens. When an administrator updates a property in the Theme panel, the system automatically updates
any Lightning components that use the tokens associated with that branding property.

[Important: Salesforce recommends that you use Styling Hooks instead of design tokens if possible. While existing design tokens](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)
still work, styling hooks are the future of customization for Lightning web components and Aura components. See Replace Design
Tokens with Styling Hooks.


Styling Apps Using Standard Design Tokens

Available Tokens for Experience Builder Sites

For Experience Builder sites, these standard tokens are available when extending from `forceCommunity:base` .

Important: The standard token values evolve along with SLDS. Available tokens and their values can change without notice.

Important: Design tokens are not available for navigation branding properties. To add branding to navigation properties, override
[the navigation bar within the custom components. See CSS Overrides Migration for the Navigation Menu.](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_nav_menu_css.htm)

**These Branding panel properties...** **...map to these standard design tokens**

Text Color `colorTextDefault`

Detail Text Color

**•** `colorTextActionLabel`

**•** `colorTextLabel`

**•** `colorTextPlaceholder`


Styling Apps Using Standard Design Tokens

**These Branding panel properties...** **...map to these standard design tokens**

**•** `colorTextWeak`

Action Color

**•** `colorBackgroundButtonBrand`

**•** `colorBorderBrand`

**•** `colorBorderButtonBrand`

**•** `colorBrand`

**•** `colorTextBrand`

**•** `colorTextTabLabelSelected`

**•** `colorTextActionLabelActive`

Note: As of Summer ’18 `colorBackgroundHighlight` is no longer
mapped to Action Color.

Link Color `colorTextLink`

Overlay Text Color

**•** `colorTextButtonBrand`

**•** `colorTextButtonBrandHover`

**•** `colorTextInverse`

Border Color

**•** `colorBorder`

**•** `colorBorderButtonDefault`

**•** `colorBorderInput`

**•** `colorBorderSeparatorAlt`

Company Logo `brandLogoImage`

Header Image `headerImageUrl`

Login Pages Background Image `LoginBackgroundImage`

Primary Font `fontFamily`

Text Case `textTransform`

In addition, the following standard tokens are available for derived theme properties in the template. You can indirectly access derived
properties when you update the properties in the Theme panel. For example, if you change the Action Color property in the Theme
panel, the system automatically recalculates the Action Color Darker value based on the new value.

**These derived branding properties...** **...map to these standard design tokens**

Action Color Darker

(Derived from Action Color)

Hover Color

(Derived from Action Color)

**•** `colorBackgroundButtonBrandActive`

**•** `colorBackgroundButtonBrandHover`

**•** `colorBackgroundButtonDefaultHover`

**•** `colorBackgroundRowHover`


### Styling Apps Replace Design Tokens with Styling Hooks

**These derived branding properties...** **...map to these standard design tokens**

**•** `colorBackgroundRowSelected`

**•** `colorBackgroundShade`

Link Color Darker

(Derived from Link Color)

**•** `colorTextLinkActive`

**•** `colorTextLinkHover`

[For a complete list of the design tokens available in the SLDS, see Design Tokens on the Lightning Design System site.](http://www.lightningdesignsystem.com/resources/tokens/)

SEE ALSO:

Configure Components for Experience Builder

### Replace Design Tokens with Styling Hooks

If you use design tokens to customize the styling of your Aura components, use SLDS global styling hooks instead. Custom components
that use design tokens still work, but they no longer receive updates after LWC API version 61.0. By using styling hooks, you can cleanly
adopt future product innovations and updated web accessibility standards.

### Replace Design Tokens with Styling Hooks

Directly replace design tokens with `--slds` styling hooks in your Aura CSS file.

```
/* Aura Custom Component CSS */

.THIS .my-custom-container {

  background-color: var(--slds-g-color-surface-container-1);

}

```

Most of the customization options provided by design tokens are available with SLDS global styling hooks. For a full list of global styling
[hooks, see the Global Styling Hooks Reference.](https://www.lightningdesignsystem.com/platforms/lightning/reference/)

Styling if Styling Hooks are Unavailable

Only Lightning Experience supports the latest global styling hooks. In containers such as Experience Cloud sites, newer styling hooks,
such as the `--slds-g-color-*` styling hooks, aren’t available. To accommodate containers that can’t access these styling hooks,
include an `--lwc` custom property as a fallback. Use this solution only if the component is expected to run in a container that doesn’t
support styling hooks.

Convert a design token to an `--lwc` property by adding `--lwc` as a prefix to the design token name. For example, instead of
`t(colorTextBrand)`, use `var(--lwc-colorTextBrand)` .

Example: This example shows an Aura CSS file for a custom component that uses a design token to override the component’s
background color.

```
   /* Aura CSS using an Aura token to override*/

   .THIS .my-custom-container {

    background-color: t(cardColorBackground);

   }

```


Styling Apps Replace Design Tokens with Styling Hooks

The best replacement is the new `--slds-g-color-*` styling hooks. However, in this case the container can’t access newer
styling hooks. So this example replaces the design token by referencing a global color styling hook and also an `--lwc` property
that’s derived from the original design token.

```
      /* Aura Custom Component CSS */

      .THIS .my-custom-container {

       background-color: var(--slds-g-color-surface-container-1, --lwc-cardColorBackground);

      }

```

SEE ALSO:

**[Salesforce Lightning Design System:](https://www.lightningdesignsystem.com/platforms/lightning/styling-hooks/)** Styling Hooks


# CHAPTER 9 Developing Secure Code

Aura components have a client-side security architecture that helps protect your custom components
by automatically blocking or modifying any insecure behavior of APIs. This layer prevents components
from accessing data that belongs to platform code or components from other namespaces without
explicit permission.

[To learn how to build components that work with Lightning Web Security (LWS) or the legacy architecture](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-intro.html)
[Lightning Locker, see the Security for Lightning Components guide.](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/locker-intro.html)

[The framework also uses JavaScript strict mode to turn on native security features in the browser, and](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/js-strict-mode-intro.html)
[Content Security Policy (CSP) rules to control the source of content that can be loaded on a page.](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/content-security-policy-intro.html)

SEE ALSO:

_Security for Lightning Components_ [: Compare Lightning Web Security to Lightning Locker](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/get-started-compare-lws-locker.html)


# CHAPTER 10 Using JavaScript

In this chapter ... Use JavaScript for client-side code. The `$A` namespace is the entry point for using the framework in
JavaScript code.

**•** Supported JavaScript
For all the methods available in `$A`, see the JavaScript API.

**•** Invoking Actions on
Component A component bundle can contain JavaScript code in a client-side controller, helper, or renderer. Client-side
Initialization controllers are the most commonly used of these JavaScript resources.

**•** Sharing JavaScript
Code in a
Component Bundle

**•** Sharing JavaScript
Code Across
Components

**•** Using External
JavaScript Libraries

Expressions in JavaScript Code

In JavaScript, use string syntax to evaluate an expression. For example, this expression retrieves the
`label` attribute in a component.

```
var theLabel = cmp.get("v.label");

```

Note: Only use the `{! }` expression syntax in markup in `.app` or `.cmp` resources.

**•** Dynamically Creating
Components

**•** Detecting Data
Changes with
Change Handlers

**•** Finding Components
by ID

**•** Working with
Attribute Values in
JavaScript

**•** Working with a
Component Body in
JavaScript

**•** Working with Events
in JavaScript

**•** Modifying the DOM

**•** Checking
Component Validity

**•** Modifying
Components Outside
the Framework
Lifecycle

**•** Throwing and
Handling Errors

SEE ALSO:

Handling Events with Client-Side Controllers


Using JavaScript

**•** Calling Component
Methods

**•** Dynamically Adding
Event Handlers To a
Component

**•** Dynamically Showing
or Hiding Markup

**•** Adding and
Removing Styles

**•** Which Button Was
Pressed?

**•** Formatting Dates in
JavaScript

**•** Using JavaScript
Promises

**•** Making API Calls
from Components


## Using JavaScript Supported JavaScript Supported JavaScript

The Aura Components programming model supports ES5 syntax and ES6 Promises.

For the most reliable experience, use ES5 to develop Aura components because the pipeline from authoring to serialization to execution
was built for ES5. Promises from ES6 are also available. Using any other syntax or feature is not supported.

This developer guide explains how to develop Aura components and documents the JavaScript usage that's unique to the Aura
Components programming model.

[If you want to use ES6 or later for development, use the Lightning Web Components programming model, which has been architected](https://developer.salesforce.com/docs/component-library/documentation/lwc)
for modern JavaScript development.

SEE ALSO:

Browser Support for Aura Components

## Invoking Actions on Component Initialization

Use the `init` event to initialize a component or fire an event after component construction but before rendering.

Note: The `init` event is fired only once per lifecycle of the component. The `init` event doesn’t get fired if the component
is served from cache. To execute JavaScript code every time a component is rendered, use the `render` event instead.

Let’s look at an example.

```
   <!--initCmp.cmp-->

   <aura:component>

      <aura:attribute name="setMeOnInit" type="String" default="default value" />

      <aura:handler name="init" value="{!this}" action="{!c.doInit}"/>

      <p>This value is set in the controller after the component initializes and before

   rendering.</p>

      <p><b>{!v.setMeOnInit}</b></p>

   </aura:component>

```

The magic happens in this line.

```
   <aura:handler name="init" value="{!this}" action="{!c.doInit}"/>

```

This code registers an `init` event handler for the component. `init` is a predefined event sent to every component. Setting
`value="{!this}"` marks this as a value event. You should always use this setting for an `init` event.

After the component is initialized, the `doInit` action is called in the component’s controller.

```
   // initCmp.js

   ({

      doInit: function(cmp) {

        // Set the attribute value.

        // You could also fire an event here instead.

        cmp.set("v.setMeOnInit", "controller init magic!");

      }

   })

```

The `doInit` action sets an attribute value, but it could do something more interesting, such as firing an event.


## Using JavaScript Sharing JavaScript Code in a Component Bundle

If a component is contained in another component or app, the inner component is initialized first.

SEE ALSO:

Handling Events with Client-Side Controllers

Handle the render Event

Component Attributes

Detecting Data Changes with Change Handlers

## Sharing JavaScript Code in a Component Bundle

Put functions that you want to reuse in the component’s helper. Helper functions also enable specialization of tasks, such as processing
data and queueing server-side actions. Helper functions are local to a component, improve code reuse, and move the heavy lifting of
JavaScript logic away from the client-side controller, where possible.

A helper function can be called from any JavaScript code in a component’s bundle, such as from a client-side controller or renderer.

Helper functions are similar to client-side controller functions in shape, surrounded by parentheses and curly braces to denote a JavaScript
object in object-literal notation containing a map of name-value pairs. A helper function can pass in any arguments required by the
function, such as the component it belongs to, a callback, or any other objects.

```
   ({

      helperMethod1 : function() {

        // logic here

      },

      helperMethod2 : function(component) {

        // logic here

        this.helperMethod3(var1, var2);

      },

      helperMethod3 : function(var1, var2) {

         // do something with var1 and var2 here

      }

   })

```

To call another function in the same helper, use the syntax: `this.` _`methodName`_, where `this` is a reference to the helper itself. For
example, `helperMethod2` calls `helperMethod3` with this code.

```
   this.helperMethod3(var1, var2);

```

Creating a Helper

A helper resource is part of the component bundle and is auto-wired via the naming convention, _`<componentName>`_ `Helper.js` .

To create a helper using the Developer Console, click **HELPER** in the sidebar of the component. This helper file is valid for the scope of
the component to which it’s auto-wired.

Using a Helper in a Controller

Add a `helper` argument to a controller function to enable the function to use the helper. Specify `(component, event,`
`helper)` in the controller. These are standard parameters and you don't have to access them in the function.


Using JavaScript Sharing JavaScript Code in a Component Bundle

This controller code calls an `updateItem` helper function.

```
   /* controller */

   ({

      newItemEvent: function(component, event, helper) {

        helper.updateItem(component, event.getParam("item"));

      }

   })

```

Here’s the helper that contains the `updateItem` function called by the controller.

```
   /* helper */

   ({

      updateItem : function(component, item, callback) {

        // Update the items via a server-side action

        var action = component.get("c.saveItem");

        action.setParams({"item" : item});

        // Set any optional callback and enqueue the action

        if (callback) {

           action.setCallback(this, callback);

        }

        $A.enqueueAction(action);

      }

   })

```

The `updateItem` function accepts three parameters.

**1.** `component` —The component to which the helper belongs.

**2.** `item` —An item that’s set as an `item` parameter for the `saveItem` Apex action.

**3.** `callback` —An optional callback to call after the `saveItem` Apex action returns. In our example, the `newItemEvent`
controller method passes in only two arguments so there’s no callback.

Using a Helper in a Renderer

Add a helper argument to a renderer function to enable the function to use the helper. In the renderer, specify `(component,`
`helper)` as parameters in a function signature to enable the function to access the component's helper. These are standard parameters
and you don't have to access them in the function. The following code shows an example on how you can override the `afterRender()`
function in the renderer and call `open` in the helper method.

**detailsRenderer.js**

```
   ({

      afterRender : function(component, helper){

        helper.open(component, null, "new");

      }

   })

```

**detailsHelper.js**

```
   ({

      open : function(component, note, mode, sort){

        if(mode === "new") {

           //do something

        }

        // do something else, such as firing an event

```


## Using JavaScript Sharing JavaScript Code Across Components

```
      }

   })

```

SEE ALSO:

Create a Custom Renderer

Component Bundles

Handling Events with Client-Side Controllers

## Sharing JavaScript Code Across Components

You can build simple Lightning components that are entirely self-contained. However, if you build more complex applications, you
probably want to share code, or even client-side data, between components.

The `<ltng:require>` tag enables you to load external JavaScript libraries after you upload them as static resources. You can also
use `<ltng:require>` to import your own JavaScript libraries of utility methods.

Let’s look at a simple counter library that provides a `getValue()` method, which returns the current value of the counter, and an
`increment()` method, which increments the value of that counter.

Create the JavaScript Library

**1.** In the Developer Console, click **File**    - **New**    - **Static Resource** .

**2.** Enter _`counter`_ in the `Name` field.

**3.** Select _`text/javascript`_ in the `MIME Type` field.

**4.** Click **Submit** .

**5.** Enter this code and click **File**    - **Save** .

```
     window._counter = (function() {

       var value = 0; // private

       return { //public API

          increment: function() {

            value = value + 1;

            return value;

          },

          getValue: function() {

            return value;

          }

       };

     }());

```

This code uses the JavaScript module pattern. Using this closure-based pattern, the `value` variable remains private to your library.
Components using the library can’t access `value` directly.

The most important line of the code to note is:

```
   window. _counter = (function() {

```


Using JavaScript Sharing JavaScript Code Across Components

You must attach `_counter` to the `window` object as a requirement of JavaScript strict mode, which is implicitly enabled in Lightning
Locker. Even though `window._counter` looks like a global declaration, `_counter` is attached to the Lightning Locker secure
window object and therefore is a namespace variable, not a global variable.

If you use `_counter` instead of `window._counter`, `_counter` isn’t available. When you try to access it, you get an error similar
to:

```
   Action failed: ... [_counter is not defined]

```

Use the JavaScript Library

Let’s use the library in a `MyCounter` component that has a simple UI to exercise the `counter` methods.

```
   <!--c:MyCounter-->

   <aura:component access="global">

      <ltng:require scripts="{!$Resource.counter}"

              afterScriptsLoaded="{!c.getValue}"/>

      <aura:attribute name="value" type="Integer"/>

      <h1>MyCounter</h1>

      <p>{!v.value}</p>

      <lightning:button label="Get Value" onclick="{!c.getValue}"/>

      <lightning:button label="Increment" onclick="{!c.increment}"/>

   </aura:component>

```

The `<ltng:require>` tag loads the counter library and calls the `getValue` action in the component’s client-side controller after
the library is loaded.

Here’s the client-side controller.

```
   /* MyCounterController.js */

   ({

      getValue : function(component, event, helper) {

        component.set("v.value", _counter.getValue());

      },

      increment : function(component, event, helper) {

        component.set("v.value", _counter.increment());

      }

   })

```

You can access properties of the `window` object without having to type the `window.` prefix. Therefore, you can use
`_counter.getValue()` as shorthand for `window._counter.getValue()` .

Click the buttons to get the value or increment it.

Our counter library shares the counter value between any components that use the library. If you need each component to have a
separate counter, you could modify the counter implementation. To see the per-component code and for more details, see this blog
[post about Modularizing Code in Lightning Components.](https://developer.salesforce.com/blogs/developer-relations/2016/12/lightning-components-code-sharing.html)

SEE ALSO:

Using External JavaScript Libraries

_Security for Lightning Components:_ [JavaScript Strict Mode Enforcement](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/js-strict-mode-intro.html)


## Using JavaScript Using External JavaScript Libraries Using External JavaScript Libraries

To reference a JavaScript library, upload it as a static resource and use a `<ltng:require>` tag in your `.cmp` or `.app` markup.

[Note: Before you use a third-party JavaScript library, we recommend that you check AppExchange for components or apps from](https://appexchange.salesforce.com/)
[Salesforce partners that match your requirements. Alternatively, check if a base component provides your desired functionality.](https://developer.salesforce.com/docs/component-library)

The framework’s content security policy mandates that external JavaScript libraries must be uploaded to Salesforce static resources.

You can’t use a `<script>` tag in a component. This restriction mitigates the risk of cross-site scripting attacks. You can add a

`<script>` tag to an application’s template, which is a special type of component that extends `aura:template` .

Note: Only third-party JavaScript libraries that are loaded via `ltng:require` are supported. Documentation and examples
that demonstrate using a third-party JavaScript library don't constitute an endorsement of that library. We recommend that you
check the third-party JavaScript library documentation for usage information.

Here’s an example of using `ltng:require` .

```
   <ltng:require scripts="{!$Resource. resourceName }"

      afterScriptsLoaded="{!c.afterScriptsLoaded}" />

```

_`resourceName`_ is the `Name` of the static resource. In a managed package, the resource name must include the package namespace
prefix, such as `$Resource.yourNamespace__resourceName` . For a stand-alone static resource, such as an individual graphic
or script, you only need the name of the resource. For example, if you uploaded `myScript.js` and set the `Name` to `myScript`,
reference it as `$Resource.myScript` . To reference an item within an archive static resource, add the rest of the path to the item
using string concatenation.

The `afterScriptsLoaded` action in the client-side controller is called after the scripts are loaded and the component is rendered.
Don’t use the `init` event to access scripts loaded by `ltng:require` . These scripts load asynchronously and are most likely not
available when the `init` event handler is called.

Here are some considerations for loading scripts:

**Loading Sets of Scripts**
Specify a comma-separated list of resources in the `scripts` attribute to load a set of resources.

Note: Due to a quirk in the way `$Resource` is parsed in expressions, use the `join` operator to include multiple
`$Resource` references in a single attribute. For example, if you have more than one JavaScript library to include into a
component the `scripts` attribute should be something like the following.

```
       scripts="{!join(',',

          $Resource.jsLibraries + '/jsLibOne.js',

          $Resource.jsLibraries + '/jsLibTwo.js')}"

```

**Loading Order**
The scripts are loaded in the order that they are listed.

**One-Time Loading**
Scripts load only once, even if they’re specified in multiple `<ltng:require>` tags in the same component or across different
components.

**Parallel Loading**
Use separate `<ltng:require>` tags for parallel loading if you have multiple sets of scripts that are not dependent on each
other.


Using JavaScript Using External JavaScript Libraries

**Encapsulation**
To ensure encapsulation and reusability, add the `<ltng:require>` tag to every `.cmp` or `.app` resource that uses the JavaScript
library.

`ltng:require` also has a `styles` attribute to load a list of CSS resources. You can set the `scripts` and `styles` attributes in
one `<ltng:require>` tag.

Using a Client-Side Controller with External JavaScript Libraries

If you’re using an external library to work with your HTML elements after rendering, use `afterScriptsLoaded` to wire up a
client-side controller. The following example sets up a chart using the `Chart.js` library, which is uploaded as a static resource.

```
   <ltng:require scripts="{!$Resource.chart}"

            afterScriptsLoaded="{!c.setup}"/>

   <canvas aura:id="chart" id="myChart" width="400" height="400"/>

```

The component’s client-side controller sets up the chart after component initialization and rendering.

```
   setup : function(component, event, helper) {

      var data = {

        labels: ["January", "February", "March"],

        datasets: [{

           data: [65, 59, 80, 81, 56, 55, 40]

        }]

      };

      var el = component.find("chart").getElement();

      var ctx = el.getContext("2d");

      var myNewChart = new Chart(ctx).Line(data);

   }

```

Troubleshooting Errors from **`ltng:require`**

Let’s say your component references a custom JavaScript library with `ltng:require` . When you try to load the component, a modal
dialog interrupts and displays information about an error.

For example, the dialog could show a message like the following.

```
   Custom Script Eval error in 'ltng:require' [SecureDOMEvent: [object Event] {key:

   {namespace":"c"}}]

```

The dialog could also include a stack trace. If it doesn’t, check the browser’s JavaScript console for more information. If the component
didn't load, the console doesn’t show much and the problem is likely in the library you referenced.

[Use the Locker Console to evaluate the JavaScript from the library to see if it’s affected by Locker restrictions.](https://developer.salesforce.com/docs/component-library/tools/locker-service-console)

If `ltng:require` encounters errors in your script, you see an error in the JavaScript console that includes details about the problem.
The JavaScript console could show a message such as the following.

```
   WARNING: Failed to load script at

   /resource/156768268766/MyHeader/static/myLib.js:

   Cannot assign to read only property 'someProp' of object '[object Object]'

```


## Using JavaScript Dynamically Creating Components

This also indicates the problem is in the static resource, `myLib.js` in this case. If the Locker Console gives you the same message
when you evaluate the JavaScript from `myLib.js`, this confirms that the script is attempting to perform an action that is not allowed
by Locker.

SEE ALSO:

_Salesforce Help_ [: Static Resources](https://help.salesforce.com/apex/HTViewHelpDoc?id=pages_static_resources.htm&language=en_US)

$Resource

Using External CSS

Lightning Component Library

_Security for Lightning Components:_ [Content Security Policy Overview](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/content-security-policy-intro.html)

Creating App Templates

## Dynamically Creating Components

Create a component dynamically in your client-side JavaScript code by using the `$A.createComponent()` method. To create
multiple components, use `$A.createComponents()` .

Note: Use `$A.createComponent()` instead of the deprecated `$A.newCmp()` and `$A.newCmpAsync()` methods.

Client-Side Versus Server-Side Component Creation

The `$A.createComponent()` and `$A.createComponents()` methods support both client-side (synchronous) and
server-side (asynchronous) component creation. For performance and other reasons, client-side creation is preferred.

To use `$A.createComponent()`, we need the component definition. If we don’t have the definition already on the client, the
framework makes a server trip to get it. You can avoid this server trip by adding an `<aura:dependency>` tag for the component
you’re creating in the markup of the component that calls `$A.createComponent()` . The tag ensures that the component definition
is always available on the client. The tradeoff is that the definition is always downloaded instead of only when it’s needed. This performance
tradeoff decision depends on your use case.

If no server-side dependencies are found, the methods are executed synchronously on the client-side. The top-level component
determines whether a server request is necessary for component creation. A component with server-side dependencies must be created
on the server. Server-side dependencies include component definitions or dynamically loaded labels that aren’t already on the client,
and other elements that can’t be predetermined by static markup analysis.

Note: A server-side controller isn’t a server-side dependency for component creation because controller actions are only called
after the component has been created.

A single call to `createComponent()` or `createComponents()` can result in many components being created. The call creates
the requested component and all its child components. In addition to performance considerations, server-side component creation has
a limit of 10,000 components that can be created in a single request. If you hit this limit, explicitly declare component dependencies
with the `<aura:dependency>` tag or otherwise pre-load dependent elements. The components are then created on the client
side instead.

There’s no limit on component creation on the client side.

Note: Creating components where the top-level components don’t have server dependencies but nested inner components do
have dependencies isn’t currently supported.


Using JavaScript Dynamically Creating Components

Syntax

The syntax is:

```
   $A.createComponent(String type, Object attributes, function callback)

```

**1.** `type` —The type of component to create; for example, `"lightning:button"` .

**2.** `attributes` —A map of attributes for the component, including the local Id ( `aura:id` ).

**3.** `callback(cmp, status, errorMessage)` —The callback to invoke after the component is created.

Tip: Component creation is asynchronous if it requires a server trip. Follow good asynchronous practices, such as only using
the new component in the callback.

The callback has three parameters.

**a.** `cmp` —The component that was created. This parameter enables you to do something with the new component, such as add
it to the body of the component that creates it. If there’s an error, `cmp` is `null` .

**b.** `status` —The status of the call. The possible values are `SUCCESS`, `INCOMPLETE`, or `ERROR` . Always check that the status
is `SUCCESS` before you try to use the component.

**c.** `errorMessage` —The error message if the status is `ERROR` .

Example

Let’s add a dynamically created button to this sample component.

```
   <!--c:createComponent-->

   <aura:component>

      <aura:handler name="init" value="{!this}" action="{!c.doInit}"/>

      <p>Dynamically created button</p>

      {!v.body}

   </aura:component>

```

The client-side controller calls `$A.createComponent()` to create a `lightning:button` with a local ID ( `aura:id` ) and a
handler for the `onclick` attribute. The `function(newButton, ...)` callback appends the button to the `body` of
`c:createComponent` . The `newButton` that’s dynamically created by `$A.createComponent()` is passed as the first
argument to the callback.

```
   /*createComponentController.js*/

   ({

      doInit : function(cmp) {

        $A.createComponent(

           "lightning:button",

           {

             "aura:id": "findableAuraId",

             "label": "Press Me",

             "onclick": cmp.getReference("c.handlePress")

           },

           function(newButton, status, errorMessage){

             //Add the new button to the body array

             if (status === "SUCCESS") {

               var body = cmp.get("v.body");

               body.push(newButton);

```


Using JavaScript Dynamically Creating Components

```
               cmp.set("v.body", body);

             }

             else if (status === "INCOMPLETE") {

               console.log("No response from server or client is offline.")

               // Show offline error

             }

             else if (status === "ERROR") {

               console.log("Error: " + errorMessage);

               // Show error message

             }

           }

        );

      },

      handlePress : function(cmp) {

        // Find the button by the aura:id value

        console.log("button: " + cmp.find("findableAuraId"));

        console.log("button pressed");

      }

   })

```

Note: `c:createComponent` contains a `{!v.body}` expression. When you use `cmp.set("v.body", ...)` to set
the component body, you must explicitly include `{!v.body}` in your component markup.

Creating Nested Components

To dynamically create a component in the body of another component, use `$A.createComponents()` to create the components.
In the function callback, nest the components by setting the inner component in the `body` of the outer component. This example
creates a `lightning:icon` component in the `body` of a `lightning:card` component.

```
   $A.createComponents([

      ["lightning:card",{

             "title" : "Dynamic Components"

           }],

           ["lightning:icon",{

             "iconName" : "utility:success",

             "alternativeText": "Icon that represents a successful step",

             "variant": "success",

             "class": "slds-m-around_small"

           }]

      ],

      function(components, status, errorMessages){

        if (status === "SUCCESS") {

           var card = components[0];

           var icon = components[1];

           // set lightning:icon as the body of lightning:card

           card.set("v.body", icon);

           cmp.set("v.body", card);

        }

        else if (status === "INCOMPLETE") {

           console.log("No response from server or client is offline.")

           // Show offline error

        }

```


## Using JavaScript Detecting Data Changes with Change Handlers

```
        else if (status === "ERROR") {

           console.log("Error message: " + errorMessages[0].message);

        }

      }

   );

```

Destroying Dynamically Created Components

After a component that is declared in markup is no longer in use, the framework automatically destroys it and frees up its memory.

If you create a component dynamically in JavaScript and don’t add it to a facet like `v.body` or another attribute of type
`Aura.Component[]`, you have to destroy it manually. Use `Component.destroy()` to destroy the component and free up
its memory to avoid memory leaks.

Important: When a user navigates to a different page, components on the previous page remain in the cache and are hidden,
not destroyed. See Event Handler Behavior for Active Components on page 285.

SEE ALSO:

aura:dependency

Invoking Actions on Component Initialization

Dynamically Adding Event Handlers To a Component

## Detecting Data Changes with Change Handlers

Configure a component to automatically invoke a change handler, which is a client-side controller action, when a value in one of the
component's attributes changes.

When the value changes, the `valueChange.evt` event is automatically fired. The event has `type="VALUE"` .

In the component, define a handler with `name="change"` .

```
   <aura:handler name="change" value="{!v.numItems}" action="{!c.itemsChange}"/>

```

The `value` attribute sets the component attribute that the change handler tracks.

The `action` attribute sets the client-side controller action to invoke when the attribute value changes.

A component can have multiple `<aura:handler name="change">` tags to detect changes to different attributes.

In the controller, define the action for the handler.

```
   ({

      itemsChange: function(cmp, evt) {

        console.log("numItems has changed");

        console.log("old value: " + evt.getParam("oldValue"));

        console.log("current value: " + evt.getParam("value"));

      }

   })

```

The `valueChange` event gives you access to the previous value ( `oldValue` ) and the current value ( `value` ) in the handler action.


## Using JavaScript Finding Components by ID

When a change occurs to a value that is represented by the `change` handler, the framework handles the firing of the event and
rerendering of the component.

SEE ALSO:

Invoking Actions on Component Initialization

## Finding Components by ID

Retrieve a component by its ID in JavaScript code.

Use `aura:id` to add a local ID of `button1` to the `lightning:button` component.

```
   <lightning:button aura:id="button1" label="button1"/>

```

You can find the component by calling `cmp.find("button1")`, where `cmp` is a reference to the component containing the
button. The `find()` function has one parameter, which is the local ID of a component within the markup.

`find()` returns different types depending on the result.

**•** If the local ID is unique, `find()` returns the component.

**•** If there are multiple components with the same local ID, `find()` returns an array of the components.

**•** If there is no matching local ID, `find()` returns `undefined` .

SEE ALSO:

Component IDs

Value Providers

## Working with Attribute Values in JavaScript

These common patterns are useful for working with attribute values in JavaScript.

`component.get(String key)` and `component.set(String key, Object value)` retrieves and assigns values
associated with the specified key on the component. Keys are passed in as an expression, which represents an attribute value.

To retrieve an attribute value of a component reference, use `component.find("cmpId").get("v.value")` .

Similarly, to set the attribute value of a component reference, use `component.find("cmpId").set("v.value", myValue)` .

This example shows how you can retrieve and set attribute values on a component reference, represented by the button with an ID of
`button1` .

```
   <aura:component>

      <aura:attribute name="buttonLabel" type="String"/>

      <lightning:button aura:id="button1" label="Button 1"/>

      {!v.buttonLabel}

      <lightning:button label="Get Label" onclick="{!c.getLabel}"/>

   </aura:component>

```

This controller action retrieves the `label` attribute value of a button in a component and sets its value on the `buttonLabel`
attribute.

```
   ({

      getLabel : function(component, event, helper) {

```


Using JavaScript Working with Attribute Values in JavaScript

```
        var myLabel = component.find("button1").get("v.label");

        component.set("v.buttonLabel", myLabel);

      }

   })

```

In the following examples, `cmp` is a reference to a component in your JavaScript code.

To get the value of a component’s `label` attribute:

```
   var label = cmp.get("v.label");

```

Set an Attribute Value

To set the value of a component’s `label` attribute:

```
   cmp.set("v.label","This is a label");

```

Deep Set an Attribute Value

If an attribute has an object or collection type, such as `Map`, you can deep set properties in the attribute value using the dot notation
for expressions. For example, this code sets a value for the `firstName` property in the `user` attribute.

```
   component.set("v.user.firstName", "Nina");

```

For deeply nested objects and attributes, continue adding dots to traverse the structure and access the nested values.

Let’s look at a component with a `user` attribute of type `Map` .

```
   <aura:component >

        <aura:attribute name="user" type="Map"

         default="{

           'id': 99,

           'firstName': 'Eunice',

           'lastName': 'Gomez'}" />

      <p>First Name: {!v.user.firstName}</p>

      <lightning:button onclick="{!c.deepSet}" label="Deep Set" />

   </aura:component>

```

When you click the button in the component, you call the `deepSet` action in the client-side controller.

```
   ({

      deepSet : function(component, event, helper) {

        console.log(component.get("v.user.firstName"));

        component.set("v.user.firstName", "Nina");

        console.log(component.get("v.user.firstName"));

      }

   })

```

The `component.set("v.user.firstName", "Nina")` line sets a value for the `firstName` property in the `user`
attribute.


## Using JavaScript Working with a Component Body in JavaScript

Validate That an Attribute Value Is Defined

To determine if a component’s `label` attribute is defined:

```
   var isDefined = !$A.util.isUndefined(cmp.get("v.label"));

```

Validate That an Attribute Value Is Empty

To determine if a component’s `label` attribute is empty:

```
   var isEmpty = $A.util.isEmpty(cmp.get("v.label"));

```

SEE ALSO:

## Working with a Component Body in JavaScript Working with a Component Body in JavaScript

These are useful and common patterns for working with a component’s body in JavaScript.

In these examples, `cmp` is a reference to a component in your JavaScript code. It’s usually easy to get a reference to a component in
JavaScript code. Remember that the `body` attribute is an array of components, so you can use the JavaScript `Array` methods on it.

Note: When you use `cmp.set("v.body", ...)` to set the component body, you must explicitly include `{!v.body}`
in your component markup.

Replace a Component's Body

To replace the current value of a component’s body with another component:

```
   // newCmp is a reference to another component

   cmp.set("v.body", newCmp);

```

Clear a Component's Body

To clear or empty the current value of a component’s body:

```
   cmp.set("v.body", []);

```

Append a Component to a Component's Body

To append a `newCmp` component to a component’s body:

```
   var body = cmp.get("v.body");

   // newCmp is a reference to another component

   body.push(newCmp);

   cmp.set("v.body", body);

```


## Using JavaScript Working with Events in JavaScript

Prepend a Component to a Component's Body

To prepend a `newCmp` component to a component’s body:

```
   var body = cmp.get("v.body");

   body.unshift(newCmp);

   cmp.set("v.body", body);

```

Remove a Component from a Component's Body

To remove an indexed entry from a component’s body:

```
   var body = cmp.get("v.body");

   // Index (3) is zero-based so remove the fourth component in the body

   body.splice(3, 1);

   cmp.set("v.body", body);

```

SEE ALSO:

Component Body

Working with Attribute Values in JavaScript

## Working with Events in JavaScript

These are useful and common patterns for working with events in JavaScript.

Events communicate data across components. Events can contain attributes with values set before the event is fired and read when the
event is handled.

Fire an Event

Fire a component event or an application event that’s registered on a component.

```
   //Fire a component event

   var compEvent = cmp.getEvent("sampleComponentEvent");

   compEvent.fire();

   //Fire an application event

   var appEvent = $A.get("e.c:appEvent");

   appEvent.fire();

```

For more information, see:

**•** Fire Component Events

**•** Fire Application Events

Get an Event Name

To get the name of the event that’s fired:

```
   event.getSource().getName();

```


Using JavaScript Working with Events in JavaScript

Get an Event Parameter

To get an attribute that’s passed into an event:

```
   event.getParam("value");

```

Get Parameters on an Event

To get all attributes that are passed into an event:

```
   event.getParams();

```

`event.getParams()` returns an object containing all event parameters.

Get the Current Phase of an Event

To get the current phase of an event:

```
   event.getPhase();

```

If the event hasn’t been fired, `event.getPhase()` returns `undefined` . Possible return values for component and application
events are `capture`, `bubble`, and `default` . Value events return `default` . For more information, see:

**•** Component Event Propagation

**•** Application Event Propagation

Get the Source Component

To get the component that fired the event:

```
   event.getSource();

```

To retrieve an attribute on the component that fired the event:

```
   event.getSource().get("v.myName");

```

Pause the Event

To pause the fired event:

```
   event.pause();

```

If paused, the event is not handled until `event.resume()` is called. You can pause an event in the `capture` or `bubble` phase
only. For more information, see:

**•** Handling Bubbled or Captured Component Events

**•** Handling Bubbled or Captured Application Events

Prevent the Default Event Execution

To cancel the default action on the event:

```
   event.preventDefault();

```


## Using JavaScript Modifying the DOM

For example, you can prevent a `lightning:button` component from submitting a form when it’s clicked.

Resume a Paused Event

To resume event handling for a paused event:

```
   event.resume();

```

You can resume a paused event in the `capture` or `bubble` phase only. For more information, see:

**•** Handling Bubbled or Captured Component Events

**•** Handling Bubbled or Captured Application Events

Set a Value for an Event Parameter

To set a value for an event parameter:

```
   event.setParam("name", cmp.get("v.myName"));

```

If the event has already been fired, setting a parameter value has no effect on the event.

Set Values for Event Parameters

To set values for parameters on an event:

```
   event.setParams({

      key : value

   });

```

If the event has already been fired, setting the parameter values has no effect on the event.

Stop Event Propagation

To prevent further propagation of an event:

```
   event.stopPropagation();

```

You can stop event propagation in the `capture` or `bubble` phase only.

## Modifying the DOM

The Document Object Model (DOM) is the language-independent model for representing and interacting with objects in HTML and
XML documents. It’s important to know how to modify the DOM safely so that the framework’s rendering service doesn’t stomp on your
changes and give you unexpected results.

IN THIS SECTION:

Modifying DOM Elements Managed by
The framework creates and manages the DOM elements owned by a component. If you want to modify these DOM elements created
by the framework, modify the DOM elements in the handler for the component’s `render` event or in a custom renderer. Otherwise,
the framework will override your changes when the component is rerendered.


### Using JavaScript Modifying DOM Elements Managed by Modifying DOM Elements Managed by External Libraries

You can use different libraries, such as a charting library, to create and manage DOM elements. You don’t have to modify these DOM
elements within the `render` event handler or a renderer because they are managed by the external library.

### Modifying DOM Elements Managed by

The framework creates and manages the DOM elements owned by a component. If you want to modify these DOM elements created
by the framework, modify the DOM elements in the handler for the component’s `render` event or in a custom renderer. Otherwise,
the framework will override your changes when the component is rerendered.

For example, if you modify DOM elements directly from a client-side controller, the changes may be overwritten when the component
is rendered.

You can read from the DOM outside a `render` event handler or a custom renderer.

The simplest approach is to leave DOM updates to the framework. Update a component’s attribute and use an expression in the markup.
The framework’s rendering service takes care of the DOM updates.

You can modify CSS classes for a component outside a renderer by using the `$A.util.addClass()`, `$A.util.removeClass()`,
and `$A.util.toggleClass()` methods.

There are some use cases where you want to perform post-processing on the DOM or react to rendering or rerendering of a component.
For these use cases, there are a few options.

IN THIS SECTION:

#### Handle the render Event

When a component is rendered or rerendered, the `aura:valueRender` event, also known as the `render` event, is fired.
Handle this event to perform post-processing on the DOM or react to component rendering or rerendering. The event is preferred
and easier to use than the alternative of creating a custom renderer.

Create a Custom Renderer
The framework’s rendering service takes in-memory component state and creates and manages the DOM elements owned by the
component. If you want to modify DOM elements created by the framework for a component, you can modify the DOM elements
in the component’s renderer. Otherwise, the framework will override your changes when the component is rerendered.

SEE ALSO:

### Modifying DOM Elements Managed by External Libraries

Using Expressions

Dynamically Showing or Hiding Markup

#### Handle the render Event

When a component is rendered or rerendered, the `aura:valueRender` event, also known as the `render` event, is fired. Handle
this event to perform post-processing on the DOM or react to component rendering or rerendering. The event is preferred and easier
to use than the alternative of creating a custom renderer.

The `render` event is fired after all methods in a custom renderer are invoked. For more details on the sequence in the rendering or
rerendering lifecycles, see Create a Custom Renderer.

Handling the `aura:valueRender` event is similar to handling the `init` hook. Add a handler to your component's markup.

```
   <aura:handler name="render" value="{!this}" action="{!c.onRender}"/>

```


Using JavaScript Modifying DOM Elements Managed by

In this example, the `onRender` action in your client-side controller handles initial rendering and rerendering of the component. You
can choose any name for the `action` attribute.

SEE ALSO:

Invoking Actions on Component Initialization

#### Create a Custom Renderer Create a Custom Renderer

The framework’s rendering service takes in-memory component state and creates and manages the DOM elements owned by the
component. If you want to modify DOM elements created by the framework for a component, you can modify the DOM elements in
the component’s renderer. Otherwise, the framework will override your changes when the component is rerendered.

The DOM is the language-independent model for representing and interacting with objects in HTML and XML documents. The framework
automatically renders your components so you don’t have to know anything more about rendering unless you need to customize the
default rendering behavior for a component.

Note: It’s preferred and easier to handle the `render` event rather than the alternative of creating a custom renderer.

Base Component Rendering

The base component in the framework is `aura:component` . Every component extends this base component.

The renderer for `aura:component` is in `componentRenderer.js` . This renderer has base implementations for the four phases
of the rendering and rerendering cycles:

**•** `render()`

**•** `rerender()`

**•** `afterRender()`

**•** `unrender()`

The framework calls these functions as part of the rendering and rerendering lifecycles and we will learn more about them soon. You
can override the base rendering functions in a custom renderer.

Rendering Lifecycle

The rendering lifecycle happens once in the lifetime of a component unless the component gets explicitly unrendered. When you create
a component:

**1.** The framework fires an `init` event, enabling you to update a component or fire an event after component construction but before
rendering.

**2.** The `render()` method is called to render the component’s body.

**3.** The `afterRender()` method is called to enable you to interact with the DOM tree after the framework’s rendering service has
inserted DOM elements.

**4.** The framework fires a `render` event, enabling you to interact with the DOM tree after the framework’s rendering service has
inserted DOM elements. Handling the `render` event is preferred to creating a custom renderer and overriding `afterRender()` .


Using JavaScript Modifying DOM Elements Managed by

Rerendering Lifecycle

The rerendering lifecycle automatically handles rerendering of components whenever the underlying data changes. Here is a typical
sequence.

**1.** A browser event triggers one or more Lightning events.

**2.** Each Lightning event triggers one or more actions that can update data. The updated data can fire more events.

**3.** The rendering service tracks the stack of events that are fired.

**4.** The framework rerenders all the components that own modified data by calling each component’s `rerender()` method.

**5.** The framework fires a `render` event, enabling you to interact with the DOM tree after the framework rerenders a component.
Handling the `render` event is preferred to creating a custom renderer and overriding `rerender()` .

The component rerendering lifecycle repeats whenever the underlying data changes as long as the component is valid and not explicitly
unrendered.

For more information, see Events Fired During the Rendering Lifecycle .

Custom Renderer

You don’t normally have to write a custom renderer, but it’s useful when you want to interact with the DOM tree after the framework’s
rendering service has inserted DOM elements. If you want to customize rendering behavior and you can’t do it in markup or by using
the `init` event, you can create a client-side renderer.

A renderer file is part of the component bundle and is auto-wired if you follow the naming convention,
`<componentName>Renderer.js` . For example, the renderer for `sample.cmp` would be in `sampleRenderer.js` .

Note: These guidelines are important when you customize rendering.

**•** Only modify DOM elements that are part of the component. Never break component encapsulation by reaching in to another
component and changing its DOM elements, even if you are reaching in from the parent component.

**•** Never fire an event as it can trigger new rendering cycles. An alternative is to use an `init` event instead.

**•** Don’t set attribute values on other components as these changes can trigger new rendering cycles.

**•** Move as much of the UI concerns, including positioning, to CSS.

Customize Component Rendering

Customize rendering by creating a `render()` function in your component’s renderer to override the base `render()` function,
which updates the DOM.

The `render()` function returns a DOM node, an array of DOM nodes, or nothing. The base HTML component expects DOM nodes
when it renders a component.

You generally want to extend default rendering by calling `superRender()` from your `render()` function before you add your
custom rendering code. Calling `superRender()` creates the DOM nodes specified in the markup.

This code outlines a custom `render()` function.

```
   render : function(cmp, helper) {

      var ret = this.superRender();

      // do custom rendering here

      return ret;

   },

```


Using JavaScript Modifying DOM Elements Managed by

Rerender Components

When an event is fired, it may trigger actions to change data and call `rerender()` on affected components. The `rerender()`
function enables components to update themselves based on updates to other components since they were last rendered. This function
doesn’t return a value.

If you update data in a component, the framework automatically calls `rerender()` .

You generally want to extend default rerendering by calling `superRerender()` from your `renderer()` function before you
add your custom rerendering code. Calling `superRerender()` chains the rerendering to the components in the `body` attribute.

This code outlines a custom `rerender()` function.

```
   rerender : function(cmp, helper){

      this.superRerender();

      // do custom rerendering here

   }

```

Access the DOM After Rendering

The `afterRender()` function enables you to interact with the DOM tree after the framework’s rendering service has inserted DOM
elements. It’s not necessarily the final call in the rendering lifecycle; it’s simply called after `render()` and it doesn’t return a value.

You generally want to extend default after rendering by calling `superAfterRender()` function before you add your custom code.

This code outlines a custom `afterRender()` function.

```
   afterRender: function (component, helper) {

      this.superAfterRender();

      // interact with the DOM here

   },

```

Unrender Components

The base `unrender()` function deletes all the DOM nodes rendered by a component’s `render()` function. It is called by the
framework when a component is being destroyed. Customize this behavior by overriding `unrender()` in your component’s renderer.
This method can be useful when you are working with third-party libraries that are not native to the framework.

You generally want to extend default unrendering by calling `superUnrender()` from your `unrender()` function before you
add your custom code.

This code outlines a custom `unrender()` function.

```
   unrender: function () {

      this.superUnrender();

      // do custom unrendering here

   }

```

SEE ALSO:

Modifying the DOM

Invoking Actions on Component Initialization

Component Bundles

Modifying Components Outside the Framework Lifecycle

Sharing JavaScript Code in a Component Bundle


### Using JavaScript Modifying DOM Elements Managed by External Libraries Modifying DOM Elements Managed by External Libraries

You can use different libraries, such as a charting library, to create and manage DOM elements. You don’t have to modify these DOM
elements within the `render` event handler or a renderer because they are managed by the external library.

A `render` event handler or a renderer are used only to customize DOM elements created and managed by the Aura Components
programming model.

To use external libraries, use `<ltng:require>` . The `afterScriptsLoaded` attribute enables you to interact with the DOM
after your libraries have loaded and the DOM is ready. `<ltng:require>` tag orchestrates the loading of your library of choice with
the rendering cycle of the Aura Components programming model to ensure that everything works in concert.

SEE ALSO:

Using External JavaScript Libraries

### Modifying DOM Elements Managed by

## Checking Component Validity

If you navigate elsewhere in the UI while asynchronous code is executing, the framework unrenders and destroys the component that
made the asynchronous request. You can still have a reference to that component, but it is no longer valid. The `cmp.isValid()`
call returns `false` for an invalid component.

If you call `cmp.get()` on an invalid component, `cmp.get()` returns `null` .

If you call `cmp.set()` on an invalid component, nothing happens and no error occurs. It’s essentially a no op.

In many scenarios, the `cmp.isValid()` call isn’t necessary because a `null` check on a value retrieved from `cmp.get()` is
sufficient. The main reason to call `cmp.isValid()` is if you’re making multiple calls against the component and you want to avoid
a `null` check for each result.

Inside the Framework Lifecycle

You don’t need a `cmp.isValid()` check in the callback in a client-side controller when you reference the component associated
with the client-side controller. The framework automatically checks that the component is valid. Similarly, you don’t need a
`cmp.isValid()` check during event handling or in a framework lifecycle hook, such as the `init` event.

Let’s look at a sample client-side controller.

```
   ({

      "doSomething" : function(cmp) {

        var action = cmp.get("c.serverEcho");

        action.setCallback(this, function(response) {

           var state = response.getState();

           if (state === "SUCCESS") {

             if (cmp.get("v.displayResult)) {

               alert("From server: " + response.getReturnValue());

             }

           }

           // other state handling omitted for brevity

        });

        $A.enqueueAction(action);

```


Using JavaScript Checking Component Validity

```
      }

   })

```

The component wired to the client-side controller is passed into the `doSomething` action as the `cmp` parameter. When
`cmp.get("v.displayResult)` is called, we don’t need a `cmp.isValid()` check.

However, if you hold a reference to another component that may not be valid despite your component being valid, you might need a
`cmp.isValid()` check for the other component. Let’s look at another example of a component that has a reference to another
component with a local ID of `child` .

```
   ({

      "doSomething" : function(cmp) {

        var action = cmp.get("c.serverEcho");

        var child = cmp.find("child");

        action.setCallback(this, function(response) {

           var state = response.getState();

           if (state === "SUCCESS") {

             if (child.get("v.displayResult)) {

               alert("From server: " + response.getReturnValue());

             }

           }

           // other state handling omitted for brevity

        });

        $A.enqueueAction(action);

      }

   })

```

This line in the previous example without the child component:

```
   if (cmp.get("v.displayResult)) {

```

changed to:

```
   if (child.get("v.displayResult)) {

```

You don’t need a `child.isValid()` call here as `child.get("v.displayResult)` will return `null` if the child component
is invalid. Add a `child.isValid()` check only if you’re making multiple calls against the child component and you want to avoid
a `null` check for each result.

Outside the Framework Lifecycle

If you reference a component in asynchronous code, such as `setTimeout()` or `setInterval()`, or when you use Promises, a
`cmp.isValid()` call checks that the component is still valid before processing the results of the asynchronous request. In many
scenarios, the `cmp.isValid()` call isn’t necessary because a `null` check on a value retrieved from `cmp.get()` is sufficient.
The main reason to call `cmp.isValid()` is if you’re making multiple calls against the component and you want to avoid a `null`
check for each result.

For example, you don’t need a `cmp.isValid()` check within this `setTimeout()` call as the `cmp.set()` call doesn’t do
anything when the component is invalid.

```
   window.setTimeout(

      $A.getCallback(function() {

        cmp.set("v.visible", true);

```


## Using JavaScript Modifying Components Outside the Framework Lifecycle

```
      }), 5000

   );

```

SEE ALSO:

Handling Events with Client-Side Controllers

Invoking Actions on Component Initialization

## Modifying Components Outside the Framework Lifecycle Modifying Components Outside the Framework Lifecycle

Use `$A.getCallback()` to wrap any code that modifies a component outside the normal rerendering lifecycle, such as in a
`setTimeout()` call. The `$A.getCallback()` call ensures that the framework rerenders the modified component and processes
any enqueued actions.

Note: `$A.run()` is deprecated. Use `$A.getCallback()` instead.

You don't need to use `$A.getCallback()` if your code is executed as part of the framework's call stack; for example, your code is
handling an event or in the callback for a server-side controller action. An exception is when you want to pass the callback to Lightning
Data Service, such as when you are creating a record using `force:recordData` . If the callback is passed in without being wrapped
in `$A.getCallback()`, any attempt to access private attributes of your component results in access check failures.

An example of where you need to use `$A.getCallback()` is calling `window.setTimeout()` in an event handler to execute
some logic after a time delay. This puts your code outside the framework's call stack.

This sample sets the `visible` attribute on a component to `true` after a five-second delay.

```
   window.setTimeout(

      $A.getCallback(function() {

        cmp.set("v.visible", true);

      }), 5000

   );

```

Note how the code updating a component attribute is wrapped in `$A.getCallback()`, which ensures that the framework rerenders
the modified component.

Note: You don't need a `cmp.isValid()` check within this `setTimeout()` call as the `cmp.set()` call doesn't do
anything when the component is invalid.

Warning: Don't save a reference to a function wrapped in `$A.getCallback()` . If you use the reference later to send actions,
the saved transaction state will cause the actions to be aborted.

SEE ALSO:

Creating a Record

Handling Events with Client-Side Controllers

Checking Component Validity

Firing Events from Non-Aura Code

Communicating with Events


## Using JavaScript Throwing and Handling Errors Throwing and Handling Errors

The framework gives you flexibility in handling unrecoverable and recoverable app errors in JavaScript code. For example, you can throw
these errors in a callback when handling an error in a server-side response.

Don’t depend on the internals of a Lightning base component for error handling as its internals can change in future releases. Errors that
are recoverable can change into unrecoverable errors and vice versa. If you encounter an unexpected error, you can sometimes get more
[information by enabling debug mode](https://help.salesforce.com/articleView?id=sf.aura_debug_mode.htm&language=en_US)

Unrecoverable Errors

Use `throw new Error("error message here")` for unrecoverable errors, such as an error that prevents your app from
starting successfully. The error message is displayed.

Note: `$A.error()` is deprecated. Throw the native JavaScript `Error` object instead by using `throw new Error()` .

This example shows you the basics of throwing an unrecoverable error in a JavaScript controller.

```
   <!--c:unrecoverableError-->

   <aura:component>

      <lightning:button label="throw error" onclick="{!c.throwError}"/>

   </aura:component>

```

Here is the client-side controller source.

```
   /*unrecoverableErrorController.js*/

   ({

      throwError : function(component, event){

        throw new Error("I can’t go on. This is the end.");

      }

   })

```

Recoverable Errors

To handle recoverable errors, use a component, such as `ui:message`, to tell users about the problem.

This sample shows you the basics of throwing and catching a recoverable error in a JavaScript controller.

```
   <!--c:recoverableError-->

   <aura:component>

      <p>Click the button to trigger the controller to throw an error.</p>

      <div aura:id="div1"></div>

      <lightning:button label="Throw an Error" onclick="{!c.throwErrorForKicks}"/>

   </aura:component>

```

Here is the client-side controller source.

```
   /*recoverableErrorController.js*/

   ({

      throwErrorForKicks: function(cmp) {

        // this sample always throws an error to demo try/catch

        var hasPerm = false;

        try {

```


## Using JavaScript Calling Component Methods

```
           if (!hasPerm) {

             throw new Error("You don't have permission to edit this record.");

           }

        }

        catch (e) {

           $A.createComponents([

             ["ui:message",{

               "title" : "Sample Thrown Error",

               "severity" : "error",

             }],

             ["lightning:formattedText",{

               "value" : e.message

             }]

             ],

             function(components, status, errorMessage){

               if (status === "SUCCESS") {

                  var message = components[0];

                  var outputText = components[1];

                  // set the body of the ui:message to be the ui:outputText

                  message.set("v.body", outputText);

                  var div1 = cmp.find("div1");

                  // Replace div body with the dynamic component

                  div1.set("v.body", message);

               }

               else if (status === "INCOMPLETE") {

                  console.log("No response from server or client is offline.")

                  // Show offline error

               }

               else if (status === "ERROR") {

                  console.log("Error: " + errorMessage);

                  // Show error message

               }

             }

           );

        }

      }

   })

```

The controller code always throws an error and catches it in this example. The message in the error is displayed to the user in a dynamically
created `ui:message` component. The body of the `ui:message` is a `ui:outputText` component containing the error text.

SEE ALSO:

Dynamically Creating Components

## Calling Component Methods

Use `<aura:method>` to define a method as part of a component's API. This enables you to directly call a method in a component’s
client-side controller instead of firing and handling a component event. Using `<aura:method>` simplifies the code needed for a
parent component to call a method on a child component that it contains.


Using JavaScript Calling Component Methods

Communicate Between Components

Use `aura:method` to communicate down the containment hierarchy. For example, a parent component calls an `aura:method`
on a child component that it contains.

To communicate up the containment hierarchy, fire a component event in the child component and handle it in the parent component.

Syntax

Use this syntax to call a method in JavaScript code.

```
   cmp.sampleMethod(arg1, … argN);

```

`cmp` is a reference to the component.

`sampleMethod` is the name of the `aura:method` .

`arg1, … argN` is an optional comma-separated list of arguments passed to the method. Each argument corresponds to an
`aura:attribute` defined in the `aura:method` markup.

Using Inherited Methods

A sub component that extends a super component has access to any methods defined in the super component.

An interface can also include an `<aura:method>` tag. A component that implements the interface can access the method.

Example

Let's look at an example app.

```
   <!-- c:auraMethodCallerWrapper.app -->

   <aura:application >

      <c:auraMethodCaller />

   </aura:application>

```

`c:auraMethodCallerWrapper.app` contains a `c:auraMethodCaller` component.

```
   <!-- c:auraMethodCaller.cmp -->

   <aura:component >

      <p>Parent component calls aura:method in child component</p>

      <c:auraMethod aura:id="child" />

      ...

   </aura:component>

```

`c:auraMethodCaller` is the parent component. `c:auraMethodCaller` contains the child component, `c:auraMethod` .

We'll show how `c:auraMethodCaller` calls an `aura:method` defined in `c:auraMethod` .

We'll use `c:auraMethodCallerWrapper.app` to see how to return results from synchronous and asynchronous code.

IN THIS SECTION:

Return Result for Synchronous Code

`aura:method` executes synchronously. A synchronous method finishes executing before it returns. Use the `return` statement
to return a value from synchronous JavaScript code.


### Using JavaScript Return Result for Synchronous Code

Return Result for Asynchronous Code

`aura:method` executes synchronously. Use the `return` statement to return a value from synchronous JavaScript code. JavaScript
code that calls a server-side action is asynchronous. Asynchronous code can continue to execute after it returns. You can’t use the

`return` statement to return the result of an asynchronous call because the `aura:method` returns before the asynchronous
code completes. For asynchronous code, use a callback instead of a `return` statement.

SEE ALSO:

aura:method

Component Events

### Return Result for Synchronous Code

`aura:method` executes synchronously. A synchronous method finishes executing before it returns. Use the `return` statement to
return a value from synchronous JavaScript code.

An asynchronous method can continue to execute after it returns. JavaScript code often uses the callback pattern to return a result after
asynchronous code completes. We’ll describe later how to return a result for an asynchronous action.

Step 1: Define **`aura:method`** in Markup

Let’s look at a `logParam aura:method` that executes synchronous code. We’ll use the `c:auraMethodCallerWrapper.app`
and components outlined in Calling Component Methods. Here’s the markup that defines the `aura:method` .

```
   <!-- c:auraMethod -->

   <aura:component>

      <aura:method name="logParam"

       description="Sample method with parameter">

        <aura:attribute name="message" type="String" default="default message" />

      </aura:method>

      <p>This component has an aura:method definition.</p>

   </aura:component>

```

The `logParam aura:method` has an `aura:attribute` with a name of `message` . This attribute enables you to set a
`message` parameter when you call the `logParam` method.

The name attribute of `logParam` configures the `aura:method` to invoke `logParam()` in the client-side controller.

An `aura:method` can have multiple `aura:attribute` tags. Each `aura:attribute` corresponds to a parameter that you
can pass into the `aura:method` . For more details on the syntax, see aura:method.

You don’t explicitly declare a return value in the `aura:method` markup. You just use a `return` statement in the JavaScript controller.

Step 2: Implement **`aura:method`** Logic in Controller

The `logParam aura:method` invokes `logParam()` in `auraMethodController.js` . Let’s look at that source.

```
   /* auraMethodController.js */

   ({

      logParam : function(cmp, event) {

        var params = event.getParam('arguments');

        if (params) {

           var message = params.message;

```


Using JavaScript Return Result for Synchronous Code

```
           console.log("message: " + message);

           return message;

        }

      },

   })

```

`logParam()` simply logs the parameter passed in and returns the parameter value to demonstrate how to use the `return` statement.
If your code is synchronous, you can use a `return` statement; for example, you’re not making an asynchronous server-side action call.

Step 3: Call **`aura:method`** from Parent Controller

`callAuraMethod()` in the controller for `c:auraMethodCaller` calls the `logParam aura:method` defined in its child
component, `c:auraMethod` . Here’s the controller for `c:auraMethodCaller` .

```
   /* auraMethodCallerController.js */

   ({

      callAuraMethod : function(component, event, helper) {

        var childCmp = component.find("child");

        // call the aura:method in the child component

        var auraMethodResult =

         childCmp.logParam("message sent by parent component");

        console.log("auraMethodResult: " + auraMethodResult);

      },

   })

```

`callAuraMethod()` finds the child component, `c:auraMethod`, and calls its `logParam aura:method` with an argument
for the message parameter of the `aura:method` .

```
   childCmp.logParam("message sent by parent component");

```

`auraMethodResult` is the value returned from `logParam` .

Step 4: Add Button to Initiate Call to **`aura:method`**

The `c:auraMethodCaller` markup contains a `lightning:button` that invokes `callAuraMethod()` in
`auraMethodCallerController.js` . We use this button to initiate the call to `aura:method` in the child component.

```
   <!-- c:auraMethodCaller.cmp -->

   <aura:component >

      <p>Parent component calls aura:method in child component</p>

      <c:auraMethod aura:id="child" />

      <lightning:button label="Call aura:method in child component"

        onclick="{! c.callAuraMethod}" />

   </aura:component>

```

SEE ALSO:

Return Result for Asynchronous Code

Calling Component Methods

aura:method


### Using JavaScript Return Result for Asynchronous Code Return Result for Asynchronous Code

`aura:method` executes synchronously. Use the `return` statement to return a value from synchronous JavaScript code. JavaScript
code that calls a server-side action is asynchronous. Asynchronous code can continue to execute after it returns. You can’t use the

`return` statement to return the result of an asynchronous call because the `aura:method` returns before the asynchronous code
completes. For asynchronous code, use a callback instead of a `return` statement.

Step 1: Define **`aura:method`** in Markup

Let’s look at an `echo aura:method` that uses a callback. We’ll use the `c:auraMethodCallerWrapper.app` and components
outlined in Calling Component Methods. Here’s the `echo aura:method` in the `c:auraMethod` component.

```
   <!-- c:auraMethod -->

   <aura:component controller="SimpleServerSideController">

      <aura:method name="echo"

       description="Sample method with server-side call">

        <aura:attribute name="callback" type="Function" />

      </aura:method>

      <p>This component has an aura:method definition.</p>

   </aura:component>

```

The `echo aura:method` has an `aura:attribute` with a name of callback. This attribute enables you to set a callback that’s
invoked by the `aura:method` after execution of the server-side action in `SimpleServerSideController` .

Step 2: Implement **`aura:method`** Logic in Controller

The `echo aura:method` invokes `echo()` in `auraMethodController.js` . Let’s look at the source.

```
   /* auraMethodController.js */

   ({

      echo : function(cmp, event) {

        var params = event.getParam('arguments');

        var callback;

        if (params) {

           callback = params.callback;

        }

        var action = cmp.get("c.serverEcho");

        action.setCallback(this, function(response) {

           var state = response.getState();

           if (state === "SUCCESS") {

             console.log("From server: " + response.getReturnValue());

             // return doesn't work for async server action call

             //return response.getReturnValue();

             // call the callback passed into aura:method

             if (callback) callback(response.getReturnValue());

           }

           else if (state === "INCOMPLETE") {

             // do something

           }

           else if (state === "ERROR") {

             var errors = response.getError();

```


Using JavaScript Return Result for Asynchronous Code

```
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

        $A.enqueueAction(action);

      },

   })

```

`echo()` calls the `serverEcho()` server-side controller action, which we’ll create next.

Note: You can’t return the result with a `return` statement. The `aura:method` returns before the asynchronous server-side
action call completes. Instead, we invoke the callback passed into the `aura:method` and set the result as a parameter in the
callback.

Step 3: Create Apex Server-Side Controller

The `echo aura:method` calls a server-side controller action called `serverEcho` . Here’s the source for the server-side controller.

```
   public with sharing class SimpleServerSideController {

      @AuraEnabled

      public static String serverEcho() {

        return ('Hello from the server');

      }

   }

```

The `serverEcho()` method returns a `String` .

Step 4: Call **`aura:method`** from Parent Controller

Here’s the controller for `c:auraMethodCaller` . It calls the `echo aura:method` in its child component, `c:auraMethod` .

```
   /* auraMethodCallerController.js */

   ({

      callAuraMethodServerTrip : function(component, event, helper) {

        var childCmp = component.find("child");

        // call the aura:method in the child component

        childCmp.echo(function(result) {

           console.log("callback for aura:method was executed");

           console.log("result: " + result);

        });

      },

   })

```

`callAuraMethodServerTrip()` finds the child component, `c:auraMethod`, and calls its `echo aura:method` . `echo()`
passes a callback function into the `aura:method` .


## Using JavaScript Dynamically Adding Event Handlers To a Component

The callback configured in `auraMethodCallerController.js` logs the result.

```
   function(result) {

      console.log("callback for aura:method was executed");

      console.log("result: " + result);

   }

```

Step 5: Add Button to Initiate Call to **`aura:method`**

The `c:auraMethodCaller` markup contains a `lightning:button` that invokes `callAuraMethodServerTrip()`
in `auraMethodCallerController.js` . We use this button to initiate the call to the `aura:method` in the child component.

Here’s the markup for `c:auraMethodCaller` .

```
   <!-- c:auraMethodCaller.cmp -->

   <aura:component >

      <p>Parent component calls aura:method in child component</p>

      <c:auraMethod aura:id="child" />

      <lightning:button label="Call aura:method (server trip) in child component"

        onclick="{! c.callAuraMethodServerTrip}" />

   </aura:component>

```

SEE ALSO:

Return Result for Synchronous Code

Calling Component Methods

aura:method

## Dynamically Adding Event Handlers To a Component

You can dynamically add a handler for an event that a component fires.

The `addEventHandler()` method in the `Component` object replaces the deprecated `addHandler()` method.

To add an event handler to a component dynamically, use the `addEventHandler()` method.

```
   addEventHandler(String event, Function handler, String phase, String includeFacets)

   event
```

The first argument is the name of the event that triggers the handler. You can’t force a component to start firing events that it doesn’t
fire, so make sure that this argument corresponds to an event that the component fires. The `<aura:registerEvent>` tag in
a component’s markup advertises an event that the component fires.

**•** For a component event, set this argument to match the `name` attribute of the `<aura:registerEvent>` tag.

**•** For an application event, set this argument to match the event descriptor in the format `namespace:eventName` .

```
   handler
```

The second argument is the action that handles the event. The format is similar to the value you would put in the `action` attribute
in the `<aura:handler>` tag if the handler was statically defined in the markup. There are two options for this argument.

**•** To use a controller action, use the format: `cmp.getReference("c.actionName")` .


Using JavaScript Dynamically Adding Event Handlers To a Component

**•** To use an anonymous function, use the format:

```
       function(auraEvent) {

         // handling logic here

       }

```

[For a description of the other arguments, see the JavaScript API in the Aura Reference app.](http://documentation.auraframework.org/auradocs#reference)

You can also add an event handler to a component that is created dynamically in the callback function of `$A.createComponent()` .
For more information, see Dynamically Creating Components.

Example

This component has buttons to fire and handle a component event and an application event.

```
   <!--c:dynamicHandler-->

   <aura:component >

      <aura:registerEvent name="compEvent" type="c:sampleEvent"/>

      <aura:registerEvent name="appEvent" type="c:appEvent"/>

      <h1>Add dynamic handler for event</h1>

      <p>

        <lightning:button label="Fire component event" onclick="{!c.fireEvent}" />

        <lightning:button label="Add dynamic event handler for component event"

   onclick="{!c.addEventHandler}" />

      </p>

      <p>

        <lightning:button label="Fire application event" onclick="{!c.fireAppEvent}" />

        <lightning:button label="Add dynamic event handler for application event"

   onclick="{!c.addAppEventHandler}" />

      </p>

   </aura:component>

```

Here’s the client-side controller.

```
   /* dynamicHandlerController.js */

   ({

      fireEvent : function(cmp, event) {

        // Get the component event by using the

        // name value from <aura:registerEvent> tag

        var compEvent = cmp.getEvent("compEvent");

        compEvent.fire();

        console.log("Fired a component event");

      },

      addEventHandler : function(cmp, event) {

        // First param matches name attribute in <aura:registerEvent> tag

        cmp.addEventHandler("compEvent", cmp.getReference("c.handleEvent"));

        console.log("Added handler for component event");

      },

      handleEvent : function(cmp, event) {

        alert("Handled the component event");

      },

```


## Using JavaScript Dynamically Showing or Hiding Markup

```
      fireAppEvent : function(cmp, event) {

        var appEvent = $A.get("e.c:appEvent");

        appEvent.fire();

        console.log("Fired an application event");

      },

      addAppEventHandler : function(cmp, event) {

        // Can use cmp.getReference() or anonymous function for handler

        // First param is event descriptor, "c:appEvent", for application events

        cmp.addEventHandler("c:appEvent", cmp.getReference("c.handleAppEvent"));

        // Can alternatively use anonymous function for handler

        //cmp.addEventHandler("c:appEvent", function(auraEvent) {

           // console.log("Handled the application event in anonymous function");

        //});

        console.log("Added handler for application event");

      },

      handleAppEvent : function(cmp, event) {

        alert("Handled the application event");

      }

   })

```

Notice the first parameter of the `addEventHandler()` calls. The syntax for a component event is:

```
   cmp.addEventHandler("compEvent", cmp.getReference("c.handleEvent"));

```

The syntax for an application event is:

```
   cmp.addEventHandler("c:appEvent", cmp.getReference("c.handleAppEvent"));

```

For either a component or application event, you can use an anonymous function as a handler instead of using `cmp.getReference()`
for a controller action.

For example, the application event handler could be:

```
   cmp.addEventHandler("c:appEvent", function(auraEvent) {

      // add handler logic here

      console.log("Handled the application event in anonymous function");

   });

```

SEE ALSO:

Handling Events with Client-Side Controllers

Handling Component Events

Lightning Component Library

## Dynamically Showing or Hiding Markup

You can use CSS to toggle markup visibility. However, `<aura:if>` is the preferred approach because it defers the creation and
rendering of the enclosed element tree until needed.

For an example using `<aura:if>`, see Best Practices for Conditional Markup.


## Using JavaScript Adding and Removing Styles

This example uses `$A.util.toggleClass(cmp, 'class')` to toggle visibility of markup.

```
   <!--c:toggleCss-->

   <aura:component>

      <lightning:button label="Toggle" onclick="{!c.toggle}"/>

      <p aura:id="text">Now you see me</p>

   </aura:component>

   /*toggleCssController.js*/

   ({

      toggle : function(component, event, helper) {

        var toggleText = component.find("text");

        $A.util.toggleClass(toggleText, "toggle");

      }

   })

   /*toggleCss.css*/

   .THIS.toggle {

      display: none;

   }

```

Note: There’s no space in the `.THIS.toggle` selector because we’re using the rule to match a `<p>` tag, which is a top-level
element. For more information, see CSS in Components.

Add the `c:toggleCss` component to an app. To hide or show the text by toggling the CSS class, click the **Toggle** button.

SEE ALSO:

Handling Events with Client-Side Controllers

Component Attributes

## Adding and Removing Styles Adding and Removing Styles

You can add or remove a CSS style on a component or element during runtime.

To retrieve the class name on a component, use `component.find('myCmp').get('v.class')`, where `myCmp` is the
`aura:id` attribute value.

To append and remove CSS classes from a component or element, use the `$A.util.addClass(cmpTarget, 'class')`
and `$A.util.removeClass(cmpTarget, 'class')` methods.

**Component source**

```
   <aura:component>

      <div aura:id="changeIt">Change Me!</div><br />

      <lightning:button onclick="{!c.applyCSS}" label="Add Style" />

      <lightning:button onclick="{!c.removeCSS}" label="Remove Style" />

   </aura:component>

```

**CSS source**

```
   .THIS.changeMe {

      background-color:yellow;

```


## Using JavaScript Which Button Was Pressed?

```
      width:200px;

   }

```

**Client-side controller source**

```
   {

      applyCSS: function(cmp, event) {

        var cmpTarget = cmp.find('changeIt');

        $A.util.addClass(cmpTarget, 'changeMe');

      },

      removeCSS: function(cmp, event) {

        var cmpTarget = cmp.find('changeIt');

        $A.util.removeClass(cmpTarget, 'changeMe');

      }

   }

```

The buttons in this demo are wired to controller actions that append or remove the CSS styles. To append a CSS style to a component,
use `$A.util.addClass(cmpTarget, 'class')` . Similarly, remove the class by using
`$A.util.removeClass(cmpTarget, 'class')` in your controller. `cmp.find()` locates the component using the local
ID, denoted by `aura:id="changeIt"` in this demo.

Toggling a Class

To toggle a class, use `$A.util.toggleClass(cmp, 'class')`, which adds or removes the class.

The `cmp` parameter can be component or a DOM element.

Note: We recommend using a component instead of a DOM element. If the utility function is not used inside `afterRender()`
or `rerender()`, passing in `cmp.getElement()` might result in your class not being applied when the components are
rerendered. For more information, see Events Fired During the Rendering Lifecycle on page 294.

To hide or show markup dynamically, see Dynamically Showing or Hiding Markup on page 372.

To conditionally set a class for an array of components, pass in the array to `$A.util.toggleClass()` .

```
   mapClasses: function(arr, cssClass) {

      for(var cmp in arr) {

        $A.util.toggleClass(arr[cmp], cssClass);

      }

   }

```

SEE ALSO:

Handling Events with Client-Side Controllers

CSS in Components

Component Bundles

## Which Button Was Pressed?

To find out which button was pressed in a component containing multiple buttons, use `Component.getLocalId()` .


## Using JavaScript Formatting Dates in JavaScript

Let’s look at an example with multiple `lightning:button` components. Each button has a unique local ID, set by an `aura:id`
attribute.

```
   <!--c:buttonPressed-->

   <aura:component>

      <aura:attribute name="whichButton" type="String" />

      <p>You clicked: {!v.whichButton}</p>

      <lightning:button aura:id="button1" label="Click me" onclick="{!c.nameThatButton}"/>

     <lightning:button aura:id="button2" label="Click me too" onclick="{!c.nameThatButton}"/>

   </aura:component>

```

Use `event.getSource()` in the client-side controller to get the button component that was clicked. Call `getLocalId()` to
get the `aura:id` of the clicked button.

```
   /* buttonPressedController.js */

   ({

      nameThatButton : function(cmp, event, helper) {

        var whichOne = event.getSource().getLocalId();

        console.log(whichOne);

        cmp.set("v.whichButton", whichOne);

      }

   })

```

In the client-side controller, you can use one of the following methods to find out which button was clicked.

**•** `event.getSource().getLocalId()` returns the `aura:id` of the clicked button.

**•** `event.getSource().get("v.name")` returns the `name` of the clicked button.

SEE ALSO:

Component IDs

Finding Components by ID

## Formatting Dates in JavaScript

The `AuraLocalizationService` JavaScript API provides methods for formatting and localizing dates.

For example, the `formatDate()` method formats a date based on the `formatString` parameter set as the second argument.

```
   formatDate (String | Number | Date date, String formatString)

```

The `date` [parameter can be a String, Number, or most typically a JavaScript Date. If you provide a String value, use ISO 8601 format to](https://www.iso.org/iso-8601-date-and-time-format.html)
avoid parsing warnings.

The `formatString` parameter contains tokens to format a date and time. For example, `"YYYY-MM-DD"` formats `15th`
`January, 2017` as `"2017-01-15"` . The default format string comes from the `$Locale` value provider.

This table shows the list of tokens supported in `formatString` .


Using JavaScript Formatting Dates in JavaScript


## Using JavaScript Using JavaScript Promises

There are similar methods that differ in their default output values.

**•** `formatDateTime()` —The default formatString outputs datetime instead of date.

**•** `formatDateTimeUTC()` —Formats a datetime in UTC standard time.

**•** `formatDateUTC()` —Formats a date in UTC standard time.

For more information on all the methods in `AuraLocalizationService`, see JavaScript API.

Example: This example converts a selected date on a date field using the given format, `yyyy-MM-dd` . The converted date is
displayed below the date field.

```
      <aura:component implements="flexipage:availableForRecordHome">

        <aura:attribute name="formatDate" type="String"/>

        <lightning:input

           type="date"

           value="{!v.formatDate}"

           onchange="{!c.convertDate}">

        </lightning:input>

        {!v.formatDate}

      </aura:component>

      ({

        convertDate: function (cmp, event) {

           var date = event.getParam("value");

           var formatted = $A.localizationService.formatDate(date, "yyyy-MM-dd");

           cmp.set("v.formatDate", formatted);

        },

      })

```

SEE ALSO:

Localization

## Using JavaScript Promises

You can use ES6 Promises in JavaScript code. Promises can simplify code that handles the success or failure of asynchronous calls, or
code that chains together multiple asynchronous calls.

If the browser doesn’t provide a native version, the framework uses a polyfill so that promises work in all browsers supported for Lightning
Experience.

We assume that you are familiar with the fundamentals of promises. For a great introduction to promises, see
[https://web.dev/articles/promises.](https://web.dev/articles/promises)

Promises are an optional feature. Some people love them, some don’t. Use them if they make sense for your use case.


Using JavaScript Using JavaScript Promises

Create a Promise

This `firstPromise` function returns a Promise.

```
   firstPromise : function() {

      return new Promise($A.getCallback(function(resolve, reject) {

       // do something

       if (/* success */) {

        resolve("Resolved");

       }

       else {

        reject("Rejected");

       }

      }));

   }

```

The promise constructor determines the conditions for calling `resolve()` or `reject()` on the promise.

Chaining Promises

When you need to coordinate or chain together multiple callbacks, promises can be useful. The generic pattern is:

```
   firstPromise()

      .then(

        // resolve handler

        $A.getCallback(function(result) {

           return anotherPromise();

        }),

        // reject handler

        $A.getCallback(function(error) {

           console.log("Promise was rejected: ", error);

           return errorRecoveryPromise();

        })

      )

      .then(

        // resolve handler

        $A.getCallback(function() {

           return yetAnotherPromise();

        })

      );

```

The `then()` method chains multiple promises. In this example, each resolve handler returns another promise.

`then()` is part of the Promises API. It takes two arguments:

**1.** A callback for a fulfilled promise (resolve handler)

**2.** A callback for a rejected promise (reject handler)

The first callback, `function(result)`, is called when `resolve()` is called in the promise constructor. The `result` object in
the callback is the object passed as the argument to `resolve()` .

The second callback, `function(error)`, is called when `reject()` is called in the promise constructor. The `error` object in
the callback is the object passed as the argument to `reject()` .


## Using JavaScript Making API Calls from Components

Note: The two callbacks are wrapped by `$A.getCallback()` in our example. What’s that all about? Promises execute their
resolve and reject functions asynchronously so the code is outside the Lightning event loop and normal rendering lifecycle. If the
resolve or reject code makes any calls to the Lightning Component framework, such as setting a component attribute, use
`$A.getCallback()` to wrap the code. For more information, see Modifying Components Outside the Framework Lifecycle
on page 362.

Always Use **`catch()`** or a Reject Handler

The reject handler in the first `then()` method returns a promise with `errorRecoveryPromise()` . Reject handlers are often
used "midstream" in a promise chain to trigger an error recovery mechanism.

The Promises API includes a `catch()` method to optionally catch unhandled errors. Always include a reject handler or a `catch()`
method in your promise chain.

Throwing an error in a promise doesn’t trigger `window.onerror`, which is where the framework configures its global error handler.
If you don't have a `catch()` method, keep an eye on your browser’s console during development for reports about uncaught errors
in a promise. To show an error message in a `catch()` method, use `$A.reportError()` . The syntax for `catch()` is:

```
   promise.then(...)

      .catch(function(error) {

        $A.reportError("error message here", error);

      });

```

For more information on `catch()` [, see the Mozilla Developer Network.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)

Don’t Use Storable Actions in Promises

The framework stores the response for storable actions in client-side cache. This stored response can dramatically improve the performance
of your app and allow offline usage for devices that temporarily don’t have a network connection. Storable actions are only suitable for
read-only actions.

Storable actions might have their callbacks invoked more than once: first with cached data, then with updated data from the server. The
multiple invocations don't align well with promises, which are expected to resolve or reject only once.

SEE ALSO:

Storable Actions

## Making API Calls from Components

By default, you can’t make calls to third-party APIs from client-side code. Add a remote site as a Trusted URL with Content Security Policy
(CSP) directives to allow client-side component code to load assets from and make API requests to that site’s domain.

[The Lightning Component framework uses Content Security Policy (CSP) to impose restrictions on content. The main objective is to help](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
[prevent cross-site scripting (XSS) and other code injection attacks. Lightning apps are served from a different domain than Salesforce](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS))
APIs, and the default CSP policy doesn’t allow API calls from JavaScript code. You change the policy, and the content of the CSP header,
by adding Trusted URLs.

Important: Otherwise, you can’t load JavaScript resources from a third party, even if it’s a trusted URL. To use a JavaScript library
from a third-party site, add that third-party site to a static resource, and then add the static resource to your component. After the
library is loaded from the static resource, you can use it as normal.


Using JavaScript Making API Calls from Components

Sometimes, you have to make API calls from server-side controllers rather than client-side code. In particular, you can’t make calls to
Salesforce APIs from client-side Aura component code. For information about making API calls from server-side controllers, see Making
API Calls from Apex on page 448.

SEE ALSO:

_Security for Lightning Components:_ [Content Security Policy Overview](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/content-security-policy-intro.html)


# CHAPTER 11 Working with Salesforce Data

In this chapter ...

**•** Lightning Data
Service

**•** Using Apex

To create, read, and update Salesforce data from an Aura component, use Lightning Data Service via
`force:recordData` or the form-based components. To delete Salesforce data, use
`force:recordData` .


## Working with Salesforce Data Lightning Data Service Lightning Data Service

Use Lightning Data Service to load, create, edit, or delete a record in your component without requiring Apex code. Lightning Data
Service handles sharing rules and field-level security for you. In addition to simplifying access to Salesforce data, Lightning Data Service
improves performance and user interface consistency.

At the simplest level, you can think of Lightning Data Service as the Lightning components version of the Visualforce standard controller.
While this statement is an over-simplification, it serves to illustrate a point. Whenever possible, use Lightning Data Service to read and
modify Salesforce data in your components.

Data access with Lightning Data Service is simpler than the equivalent using a server-side Apex controller. Read-only access can be
entirely declarative in your component’s markup. For code that modifies data, your component’s JavaScript controller is roughly the
same amount of code, and you eliminate the Apex entirely. All your data access code is consolidated into your component, which
significantly reduces complexity.

## Lightning Data Service provides other benefits aside from the code. It’s built on highly efficient local storage that’s shared across all

components that use it. Records loaded in Lightning Data Service are cached and shared across components.

[Note: Working with Lightning Data Service in Lightning Web Components? See the Lightning Web Components Developer](https://developer.salesforce.com/docs/component-library/documentation/lwc/lwc.data_ui_api)
[Guide.](https://developer.salesforce.com/docs/component-library/documentation/lwc/lwc.data_ui_api)

Components accessing the same record see significant performance improvements, because a record is loaded only once, no matter
how many components are using it. Shared records also improve user interface consistency. When one component updates a record,
the other components using it are notified, and in most cases, refresh automatically.

Creating Components That Use Lightning Data Service

## Lightning Data Service is available through force:recordData and several base components. To return raw record data, for

example if you need to view or edit only a few fields, and don't need any UI elements or layout information, use `force:recordData` .
When using `force:recordData`, load the data once and pass it to child components as attributes. This approach reduces the
number of listeners and minimizes server calls, which improves performance and ensures that your components show consistent data.
[For more information, see force:recordData documentation.](https://developer.salesforce.com/docs/component-library/bundle/force:recordData/documentation)

To create a form for working with records, use `lightning:recordForm`, `lightning:recordEditForm`, or
`lightning:recordViewForm` . One advantage of using the form-based components is that you can achieve many of your record
display needs entirely in markup without JavaScript. Another powerful feature of the form-based components is automatic field mapping
with field-level validation. The form-based components use a base component that’s appropriate for the field type to render the field
automatically.

`force:recordData` doesn’t include any UI elements; it’s simply logic and a way to communicate to the server. Here are the
components that use Lightning Data Service.

```
   lightning:recordForm
```

Display, create, or edit records

```
   lightning:recordViewForm
```

Display records with `lightning:outputField`

```
   lightning:recordEditForm
```

Create or edit records with `lightning:inputField`

```
   force:recordData
```

Create, edit, or delete record data using your own custom UI components


### Working with Salesforce Data Loading a Record

IN THIS SECTION:

### Loading a Record

Loading a record can be accomplished entirely in markup using `lightning:recordForm` . If you need a custom layout, use
`lightning:recordViewForm` . If you need more customization than the form-based components allow for viewing record
data, use `force:recordData` .

Editing a Record
The simplest way to create a form that enables you to edit a record is to use the `lightning:recordForm` component. If you
want to customize the form layout or preload custom values, use `lightning:recordEditForm` . If you want to customize
a form more than the form-based components allow, use `force:recordData` .

Creating a Record
The simplest way to create a form that enables users create a record is to use `lightning:recordForm` . If you want to customize
the form layout or preload custom values, use `lightning:recordEditForm` . If you need more customization than the
form-based components allow, use `force:recordData` .

Deleting a Record
To delete a record using Lightning Data Service, call `deleteRecord` on the `force:recordData` component, and pass in
a callback function to be invoked after the delete operation completes. The form-based components, such as
`lightning:recordForm`, don’t currently support deleting a record.

Record Changes
To perform more advanced tasks using `force:recordData` when the record changes, handle the `recordUpdated` event.
You can handle record loaded, updated, and deleted changes, applying different actions to each change type.

Handling Errors
Lightning Data Service returns an error when a resource, such as a record or an object, is inaccessible on the server.

Changing the Display Density
In Lightning Experience, the display density setting determines how densely content is displayed and where field labels are located.
Display density is controlled for the org in Setup, and users can also set display density to their liking from their profile menu.

Considerations
Lightning Data Service is powerful and simple to use. However, it’s not a complete replacement for writing your own data access
code. Here are some considerations to keep in mind when using it.

Lightning Action Examples
Here are some examples that use the base components to create a Quick Contact action panel.

SaveRecordResult
Represents the result of a Lightning Data Service operation that makes a persistent change to record data.

Displaying the Create and Edit Record Modals
You can take advantage of built-in events to display modals that let you create or edit records via an Aura component.

### Loading a Record

Loading a record can be accomplished entirely in markup using `lightning:recordForm` . If you need a custom layout, use
`lightning:recordViewForm` . If you need more customization than the form-based components allow for viewing record data,
use `force:recordData` .


Working with Salesforce Data Loading a Record

Display a Record Using **`lightning:recordForm`**

To display a record using `lightning:recordForm`, provide the record ID and the object API name. Additionally, provide fields
using either the `fields` or `layoutType` attribute. You can display a record in two modes using the `mode` attribute.

```
   view
```

Loads the form using output fields with inline editing enabled. Editable fields have edit icons. If a user clicks an edit icon, editable
fields in the form become editable, and the form displays Cancel and Save buttons. This is the default mode when a record ID is
provided.

```
   readonly
```

Loads the form with output fields only. The form doesn’t include edit icons or Cancel and Save buttons.

This example displays an account record in view mode using the compact layout, which includes fewer fields than the full layout. The
`columns` attribute displays the record fields in two columns that are evenly sized. Update the record ID with your own.

```
   <aura:component>

      <lightning:recordForm

        recordId="001XXXXXXXXXXXXXXX"

        objectApiName="Account"

        layoutType="Compact"

        columns="2"/>

   </aura:component>

```

To display the field values on a record page, implement the `flexipage:availableForRecordHome` and
`flexipage:hasRecordId` . The component automatically inherits the record ID.

This example displays read-only values for the account’s `Name` and `Industry` fields. Add this example to an account record page.

```
   <aura:component implements="flexipage:availableForRecordHome,force:hasRecordId">

      <aura:attribute name="recordId" type="String" />

      <aura:attribute name="fields" type="String[]" default="['Name','Industry']" />

      <lightning:recordForm recordId="{!v.recordId}"

                   objectApiName="Account"

                   mode="readonly"

                   fields="{!v.fields}" />

```

If you provide both `fields` and `layoutType` attributes, the display order of the fields is not guaranteed. To specify the field order,
use `fields` without the `layoutType` attribute. Alternatively, use the `lightning:recordViewForm` component as shown
in the next section.

Display a Record with a Custom Layout Using **`lightning:recordViewForm`**

To display a read-only record with a custom layout, use the `lightning:recordViewForm` component. To compose a form field,
use `lightning:outputField` components, which maps to a Salesforce field by using the `fieldName` attribute. Including
individual fields lets you style a custom layout using the Lightning Design System utility classes, such as the grid system.

```
   <aura:component>

      <lightning:recordViewForm recordId="001XXXXXXXXXXXXXXX"

                     objectApiName="Account">

      <div class="slds-grid">

        <div class="slds-col slds-size_2-of-3">

           <lightning:outputField fieldName="Name" />

           <lightning:outputField fieldName="Phone" />

        </div>

        <div class="slds-col slds-size_1-of-3">

```


Working with Salesforce Data Loading a Record

```
           <lightning:outputField fieldName="Industry" />

           <lightning:outputField fieldName="AnnualRevenue" />

        </div>

      </div>

   </lightning:recordViewForm>

   </aura:component>

```

If you require more customization when displaying a record than what `lightning:recordForm` and
`lightning:recordViewForm` allow, consider using `force:recordData` .

Display Record Data in a Custom User Interface Using **`force:recordData`**

`force:recordData` enables granular customization, including providing your own component to load data. To load a record using
Lightning Data Service, add the `force:recordData` tag to your component and specify:

**•** The ID of the record to load

**•** A component attribute to assign the loaded record

**•** A list of fields to load

To specify a list of fields to load, use the `fields` attribute. For example, `fields="Name,BillingCity,BillingState"` .

Alternatively, you can specify a layout using the `layoutType` attribute. All fields on that layout are loaded for the record. The layout
depends on the page layout assignment for the profile. For example, if a user using the Marketing User profile is assigned the default
account layout, all fields on that layout are available to that user. Layouts are typically modified by administrators, so `layoutType`
isn’t as flexible as `fields` when you want to request specific fields. Loading record data using `layoutType` allows your component
to adapt to layout definitions. Valid values for `layoutType` are `FULL` and `COMPACT` .

Note: We recommend that you use the `fields` attribute instead of `layoutType` . Use `layoutType` only if you want the
administrator, not the component, to control the fields that are provisioned. The component must handle receiving every field
that is assigned to the layout for the context user.

To get a field from an object regardless of whether an admin has included it in a layout, use the `fields` attribute and request the field
by name.

`targetRecord` is populated with the current record, containing the fields relevant to the requested `layoutType` or the fields
listed in the `fields` attribute. `targetFields` is populated with a simplified view of the loaded record. For example, for the `Name`
field, `v.targetRecord.fields.Name.value` is equivalent to `v.targetFields.Name` .

Example: **Loading a Record**

The following example illustrates the essentials of loading a record using `force:recordData` . This component can be added
to a record home page in the Lightning App Builder, or as a custom action. The record ID is supplied by the implicit `recordId`
attribute added by the `force:hasRecordId` interface.

```
     ldsLoad.cmp

      <aura:component implements="flexipage:availableForRecordHome,

      force:lightningQuickActionWithoutHeader, force:hasRecordId">

        <aura:attribute name="record" type="Object"/>

        <aura:attribute name="simpleRecord" type="Object"/>

        <aura:attribute name="recordError" type="String"/>

        <force:recordData aura:id="recordLoader"

         fields="Name,BillingCity,BillingState,Industry"

         recordId="{!v.recordId}"

```


Working with Salesforce Data Loading a Record

```
         targetFields="{!v.simpleRecord}"

         targetError="{!v.recordError}"

         recordUpdated="{!c.handleRecordUpdated}"

         />

        <!-- Display a lightning card with details about the record -->

        <div class="Record Details">

        <lightning:card iconName="standard:account" title="{!v.simpleRecord.Name}" >

           <div class="slds-p-horizontal--small">

             <p class="slds-text-heading--small">

               <lightning:formattedText title="Billing City"

      value="{!v.simpleRecord.BillingCity}" /></p>

             <p class="slds-text-heading--small">

               <lightning:formattedText title="Billing State"

      value="{!v.simpleRecord.BillingState}" /></p>

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

When you use the `fields` attribute, the `targetFields` attribute returns the record’s `Id` and `SystemModstamp` fields,
in addition to the fields you requested. In this example, `{!v.simpleRecord}` returns:

```
      {

       "Id":"0011a0000000000000",

       "Name":"Salesforce",

       "SystemModstamp":"2020-06-14T23:44:43.000Z",

       "BillingCity":"San Franscisco",

       "BillingState":"CA",

       "Industry":"Technology"

      }

     ldsLoadController.js

      ({

        handleRecordUpdated: function(component, event, helper) {

           var eventParams = event.getParams();

           if(eventParams.changeType === "LOADED") {

            // record is loaded (render other component which needs record data value)

             console.log("Record is loaded successfully.");

             console.log("You loaded a record in " +

                    component.get("v.simpleRecord.Industry"));

           } else if(eventParams.changeType === "CHANGED") {

             // record is changed

           } else if(eventParams.changeType === "REMOVED") {

             // record is deleted

           } else if(eventParams.changeType === "ERROR") {

             // there’s an error while loading, saving, or deleting the record

```


### Working with Salesforce Data Editing a Record

```
           }

        }

      })

```

When the record loads or updates, to access the record fields in the JavaScript controller, use the
`component.get("v.simpleRecord.fieldName")` syntax.

`force:recordData` loads data asynchronously by design since it may go to the server to retrieve data. To track when the
record is loaded or changed, use the `recordUpdated` event as shown in the previous example. Alternatively, you can place
a change handler on the attribute provided to `targetRecord` or `targetFields` .

SEE ALSO:

_Component Library_ : `[lightning:recordForm](https://developer.salesforce.com/docs/component-library/bundle/lightning:recordForm/documentation)`

_Component Library_ : `[lightning:recordViewForm](https://developer.salesforce.com/docs/component-library/bundle/lightning:recordViewForm/documentation)`

Configure Components for Lightning Experience Record Pages

Configure Components for Record-Specific Actions

### Editing a Record

The simplest way to create a form that enables you to edit a record is to use the `lightning:recordForm` component. If you
want to customize the form layout or preload custom values, use `lightning:recordEditForm` . If you want to customize a form
more than the form-based components allow, use `force:recordData` .

Edit a Record using **`lightning:recordForm`**

To edit a record using `lightning:recordForm`, provide the record ID and object API name. When you provide a record ID, view
mode is the default mode of this component, which displays fields with edit icons. If you click an edit icon, all fields in the form become
editable.

This example creates a form that lets users update fields on an account record when an edit icon is clicked. It displays the fields from the
compact layout in two columns. Add this example component to an account record page. The component inherits the record ID via
the `force:hasRecordId` interface.

```
   <aura:component implements="flexipage:availableForRecordHome, force:hasRecordId">

      <lightning:recordForm

        recordId = "{!v.recordId}"

        objectApiName="Account"

        layoutType="Compact"

        columns="2" />

   </aura:component>

```

When the record is saved successfully, all components that contain the updated field values are refreshed automatically.

Add `mode="edit"` to transform the form to one that displays input fields for editing. The form displays a Save button that updates
the record, and a Cancel button that reverts changes.

```
   <aura:component implements="flexipage:availableForRecordHome, force:hasRecordId">

      <lightning:recordForm

        recordId = "{!v.recordId}"

        objectApiName="Account"

        layoutType="Compact"

```


Working with Salesforce Data Editing a Record

```
        mode="edit" />

   </aura:component>

```

Customize Error Handling in **`lightning:recordForm`**

To customize the behavior when a record is saved successfully, use the `onsuccess` event handler. Errors are automatically handled
and displayed. To customize them, use the `onerror` event handler.

```
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

A toast notification is displayed when a record is saved successfully or when an error is encountered during save.

```
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

[Note: For more information, see lightning:recordForm.](https://developer.salesforce.com/docs/component-library/bundle/lightning:recordForm/documentation)

Edit a Record with a Custom Layout Using **`lightning:recordEditForm`**

To provide a custom layout for your form fields, use the `lightning:recordEditForm` component.

Pass in the fields to `lightning:inputField`, which displays an input control based on the record field type.

This example displays a form with two fields using a custom layout. Add this example component to an account record page.

```
   <aura:component implements="flexipage:availableForRecordHome, force:hasRecordId">

      <lightning:recordEditForm

```


Working with Salesforce Data Editing a Record

```
        recordId="{!v.recordId}"

        objectApiName="Account">

        <lightning:messages />

           <div class="slds-grid">

             <div class="slds-col slds-size_1-of-2">

               <lightning:inputField fieldName="Name"/>

             </div>

             <div class="slds-col slds-size_1-of-2">

               <lightning:inputField fieldName="Industry"/>

             </div>

           </div>

        <lightning:button class="slds-m-top_small" type="submit" label="Create new" />

      </lightning:recordEditForm>

   </aura:component>

```

When a server error is encountered, `lightning:recordEditForm` displays an error message above the form fields using the
`lightning:messages` component. Alternatively, provide your own error handling using the `onerror` event handler.

Another feature that `lightning:recordEditForm` provides that’s not available with `lightning:recordForm` is displaying
the form with custom field values, as shown in the next section.

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

Edit a Record via a Custom User Interface Using **`force:recordData`**

To edit and save a record using `force:recordData`, call `saveRecord` and pass in a callback function to be invoked after the
save operation completes. The save operation is used in two cases.

**•** To save changes to an existing record

**•** To create and save a new record

To save changes to an existing record, load the record in EDIT mode and call `saveRecord` on the `force:recordData` component.

To save a new record, and thus create it, create the record from a record template, as described in Creating a Record. Then call
`saveRecord` on the `force:recordData` component.

Load a Record in EDIT Mode

To load a record that might be updated, set the `force:recordData` tag’s `mode` attribute to “EDIT”. Other than explicitly setting
the `mode`, loading a record for editing is the same as loading it for any other purpose.

Note: Since Lightning Data Service records are shared across multiple components, loading records provides the component
with a copy of the record instead of a direct reference. If a component loads a record in VIEW mode, Lightning Data Service


Working with Salesforce Data Editing a Record

automatically overwrites that copy with a newer copy of the record when the record is changed. If a record is loaded in EDIT mode,
the record is not updated when the record is changed. This prevents unsaved changes from appearing in components that
reference the record while the record is being edited, and prevents any edits in progress from being overwritten. Notifications are
still sent in both modes.

Call **`saveRecord`** to Save Record Changes

To perform the save operation, call `saveRecord` on the `force:recordData` component from the appropriate controller action
handler. The `saveRecord` method takes one argument—a callback function to be invoked when the operation completes. This
callback function receives a `SaveRecordResult` as its only parameter. `SaveRecordResult` includes a `state` attribute that
indicates success or error, and other details you can use to handle the result of the operation.

Example: **Saving a Record**

The following example illustrates the essentials of saving a record using Lightning Data Service. It’s intended for use on a record
page. The record ID is supplied by the implicit `recordId` attribute added by the `force:hasRecordId` interface.

```
     ldsSave.cmp

      <aura:component implements="flexipage:availableForRecordHome,force:hasRecordId">

        <aura:attribute name="record" type="Object"/>

        <aura:attribute name="simpleRecord" type="Object"/>

        <aura:attribute name="recordError" type="String"/>

        <force:recordData aura:id="recordHandler"

         recordId="{!v.recordId}"

         fields="Name,BillingState,BillingCity"

         targetRecord="{!v.record}"

         targetFields="{!v.simpleRecord}"

         targetError="{!v.recordError}"

         mode="EDIT"

         recordUpdated="{!c.handleRecordUpdated}"

         />

        <!-- Display a lightning card with details about the record -->

        <div class="Record Details">

           <lightning:card iconName="standard:account" title="{!v.simpleRecord.Name}" >

             <div class="slds-p-horizontal--small">

               <p class="slds-text-heading--small">

                  <lightning:formattedText title="Billing State"

      value="{!v.simpleRecord.BillingState}" /></p>

               <p class="slds-text-heading--small">

                  <lightning:formattedText title="Billing City"

      value="{!v.simpleRecord.BillingCity}" /></p>

             </div>

           </lightning:card>

        </div>

        <!-- Display an editing form -->

        <div class="Record Details">

           <lightning:card iconName="action:edit" title="Edit Account">

             <div class="slds-p-horizontal--small">

               <lightning:input label="Account Name" value="{!v.simpleRecord.Name}"/>

```


Working with Salesforce Data Editing a Record

```
               <br/>

               <lightning:button label="Save Account" variant="brand"

      onclick="{!c.handleSaveRecord}" />

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

To improve performance, we recommend using the `fields` attribute to query only the fields you need. Use `layoutType`
only if you expect to display or edit a large number of fields on the compact or full layout.

Note: To edit the constituent fields on compound fields, such as the FirstName and LastName fields in the Name compound
field, create a separate `lightning:input` component for `{!v.simpleRecord.FirstName}` and
`{!v.simpleRecord.LastName}` .

This component loads a record using `force:recordData` set to EDIT mode, and provides a form for editing record values.
(In this simple example, just the record name field.)

```
     ldsSaveController.js

      ({

        handleSaveRecord: function(component, event, helper) {

          component.find("recordHandler").saveRecord($A.getCallback(function(saveResult)

      {

             // use the recordUpdated event handler to handle generic logic when record

      is changed

             if (saveResult.state === "SUCCESS" || saveResult.state === "DRAFT") {

               // handle component related logic in event handler

             } else if (saveResult.state === "INCOMPLETE") {

               console.log("User is offline, device doesn't support drafts.");

             } else if (saveResult.state === "ERROR") {

               console.log('Problem saving record, error: ' +

      JSON.stringify(saveResult.error));

             } else {

               console.log('Unknown problem, state: ' + saveResult.state + ', error:

      ' + JSON.stringify(saveResult.error));

             }

           }));

        },

        /**

         * Control the component behavior here when record is changed (via any component)

         */

        handleRecordUpdated: function(component, event, helper) {

           var eventParams = event.getParams();

           if(eventParams.changeType === "CHANGED") {

             // get the fields that changed for this record

```


### Working with Salesforce Data Creating a Record

```
             var changedFields = eventParams.changedFields;

             console.log('Fields that are changed: ' + JSON.stringify(changedFields));

             // record is changed, so refresh the component (or other component logic)

             var resultsToast = $A.get("e.force:showToast");

             resultsToast.setParams({

               "title": "Saved",

               "message": "The record was updated."

             });

             resultsToast.fire();

           } else if(eventParams.changeType === "LOADED") {

             // record is loaded in the cache

           } else if(eventParams.changeType === "REMOVED") {

             // record is deleted and removed from the cache

           } else if(eventParams.changeType === "ERROR") {

             // there’s an error while loading, saving or deleting the record

           }

        }

      })

```

The `handleSaveRecord` action here is a minimal version. There’s no form validation or real error handling. Whatever is
entered in the form is attempted to be saved to the record.

If you are creating multiple instances of `force:recordData` on a page, provide your `saveRecord` and `recordUpdated`
handlers accordingly. For example, if you have two instances of `force:recordData` that updates the same record, assign a
different `aura:id` to each instance, such that `saveRecord` is called uniquely, and subsequently the `recordUpdated`
handler.

SEE ALSO:

_Component Library_ : `[lightning:recordForm](https://developer.salesforce.com/docs/component-library/bundle/lightning:recordForm/documentation)`

_Component Library_ : `[lightning:recordEditForm](https://developer.salesforce.com/docs/component-library/bundle/lightning:recordEditForm/documentation)`

SaveRecordResult

Configure Components for Lightning Experience Record Pages

Configure Components for Record-Specific Actions

### Creating a Record

The simplest way to create a form that enables users create a record is to use `lightning:recordForm` . If you want to customize
the form layout or preload custom values, use `lightning:recordEditForm` . If you need more customization than the form-based
components allow, use `force:recordData` .

Create a Record using **`lightning:recordForm`**

To create a record using `lightning:recordForm`, leave out the `recordId` attribute.


Working with Salesforce Data Creating a Record

This example displays a form that creates an account record with a list of fields. The Cancel and Save buttons are displayed at the bottom
of the form.

```
   <aura:component>

      <aura:attribute name="fields"

               type="String[]"

               default="['Name', 'Industry']"/>

      <lightning:recordForm objectApiName="Account"

                   fields="{!v.fields}"/>

   </aura:component>

```

When the record saves successfully, the fields display pencil icons to denote that inline editing is available. This view is displayed until
you refresh or reload the page. Then the form redisplays the record fields without data, ready to create a new record.

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
[handler. This call returns a Record object to create an empty contact record, which is used by the contact form in the component’s](https://developer.salesforce.com/docs/atlas.en-us.262.0.uiapi.meta/uiapi/ui_api_responses_record.htm)
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

