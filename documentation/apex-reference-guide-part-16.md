**•** 1, 4155551234 (only numbers, no symbols)

**•** 1, 415-555-1234 (extra spaces)

Now, consider the following examples.

**•** Correct examples:

**–** `formatPhoneNumber('1', '4155551234');`

**–** `formatPhoneNumber('+1','(415) 555-1234');`

**–** `formatPhoneNumber('1', '415-555-1234');`

**•** Incorrect example, because the country code and mobile number aren’t separated:

**–** `formatPhoneNumber(null, '+1 415-555-1234');`

**•** Example that doesn’t generate an error, but likely won’t work as intended:

**–** `formatPhoneNumber('+1', '+1 (415) 555-1234');`

Format Phone Number Code Example

Here's a code example that uses the `formatPhoneNumber` method. It gets the mobile number from the user and converts it to the
format required by Salesforce. Then it updates the user’s record with the formatted mobile number.

```
   global with sharing class PhoneRegistrationController {

      //Input variables

```


Apex Reference Guide UserManagement Class

```
      global String countryCode {get; set;}

      global String phoneNumber {get; set;}

      global String addPhoneNumber()

      {

        if(countryCode == null) return 'Country code is required';

        if(phoneNumber == null) return 'Phone number is required';

        String userId = UserInfo.getUserId();

        User u = [SELECT Id FROM User WHERE Id=:userId LIMIT 1];

       String formatNum = System.UserManagement.formatPhoneNumber(countryCode, phoneNumber);

        u.MobilePhone = formatNum;

        update u;

        return null;

      }

   }

```

As long as the country code and phone number are separated, `formatPhoneNumber` returns a value in the proper format.

##### initPasswordlessLogin(userId, method)

Invokes a verification challenge for passwordless login when creating custom (Visualforce) Login and Verify pages for customers and
partners.

Signature

```
   public static String initPasswordlessLogin(Id userId, Auth.VerificationMethod method)

```

Parameters

```
   userId
```

Type: Id

ID of the user who’s logging in.

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the user’s identity, which can be EMAIL or SMS.

Return Value

Type: String

Identifier of the verification attempt.

Usage

Use this method along with its paired `verifyPasswordlessLogin` to customize the login experience with your own Visualforce
##### Login and Verify pages. Invoke initPasswordlessLogin from the Login page where the user enters an email address or phone

number.


Apex Reference Guide UserManagement Class

Note: An alternative to using this combination of methods is to use `Site.passwordlessLogin` . Both approaches let you
customize the Login page in Visualforce. With the paired methods, you can create custom Login and Verify pages. With
`Site.passwordlessLogin`, Salesforce supplies the Verify page.

First call the `initPasswordlessLogin` method to initiate an authentication challenge. This method:

**•** Gets the user ID and verification method, such as EMAIL or SMS, from the Login page.

**•** Looks up the user and checks that the user is unique and active.

**•** Sends a verification code to the user.

**•** Adds an entry for the verification attempt to the Identity Verification History log, assigning an identifier to the verification attempt
and setting the status to **User challenged, waiting for response** .

**•** Adds an entry for the Passwordless Login to the Login History log.

**•** Returns the identifier to `verifyPasswordlessLogin` to link the transactions.

Then call `verifyPasswordlessLogin`, which, if the user enters the verification code correctly, logs in the user.

Note: Users must verify their identity by email address or phone number before they can log in without a password. You can
check whether the user is verified from the user’s detail page in Setup. Or you can check programmatically with
`[TwoFactorMethodsInfo](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_twofactormethodsinfo.htm)` .

##### initRegisterVerificationMethod(method)

Invokes a verification challenge for registering identity verification methods with a custom (Visualforce) page. Users can register either
their email address or phone number.

Signature

```
   public static String initRegisterVerificationMethod(Auth.VerificationMethod method)

```

Parameters

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the user’s identity, which can be EMAIL or SMS.

Return Value

Type: String

The method returns an error message if the phone number is already registered, the user isn’t a customer or partner, or if the context
isn’t an Experience Cloud site.

Usage

Use this method along with its paired `verifyRegisterVerificationMethod` on page 4411 to customize the process for
registering a user’s verification method using a Visualforce Verify page.

##### First call the initRegisterVerificationMethod method to get the verification code sent to the user as input, and validate

it. If the verification code isn’t valid, it returns an error message.


Apex Reference Guide UserManagement Class

Example

Here’s a code example that registers a user’s phone number as a verification method. When the user enters a verification code on the
Visualforce page, it invokes `registerUser()` [. The method calls the UserInfo class to get the User ID of the user who’s registering](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_userinfo.htm)
the verification method. Using the user ID, it then finds the user’s phone number. It also gets the user’s registration status to check
whether the phone number is verified already. If the user is registered with a different phone number, the number is updated.

```
   public void registerUser() {

        try {

           exceptionText='';

           String userId = UserInfo.getUserId();

           User u = [Select MobilePhone, Id from User Where Id=:userId];

           currPhone = u.MobilePhone;

           mobilePhone = getFormattedSms(mobilePhone);

          if (mobilePhone != null && mobilePhone != '') {

          u.MobilePhone = mobilePhone;

          update u;

           // We're updating the email and phone number before verifying. Roll back

          // the change in the verify API if it is unsuccessful.

           exceptionText = System.

           UserManagement.initRegisterVerificationMethod(Auth.VerificationMethod.SMS);

           if(exceptionText!= null && exceptionText!=''){

             isInit = false;

             showInitException = true;

           } else {

              isInit = false;

              isVerify = true;

           }

           } else {

             showInitException = true;

           }

        } catch (Exception e) {

           exceptionText = e.getMessage();

           isInit = false;

           showInitException = true;

        }

      }

   public void verifyUser() {

      // Take the user’s input for the code sent to their phone number

      exceptionText = System.UserManagement.

        verifyRegisterVerificationMethod(code, Auth.VerificationMethod.SMS);

      if(exceptionText != null && exceptionText !=''){

      showInitException = true;

      } else {

           //Success

      }

   }

##### initSelfRegistration(method, user)

```

Invokes a verification challenge for self-registration when creating a custom (Visualforce) Verify page for Experience Cloud self-registration.


Apex Reference Guide UserManagement Class

Signature

```
   public static String initSelfRegistration(Auth.VerificationMethod method, User user)

```

Parameters

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the identity of the user, which can be EMAIL or SMS.

```
   user
```

Type: User

[User object to insert after successful registration. To see which fields are required, see User in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_user.htm) _Object Reference for the Salesforce_
_Platform_ .

Return Value

Type: String

Identifier of the registration attempt.

Usage

By default, when users sign up for your Experience Cloud site with an email address or phone number, Salesforce sends them a verification
code. At the same time, it generates a Verify page for users to confirm their identity. You can replace the default Salesforce Verify page
with your own Visualforce page and then invoke the verification process.

Call this method to initiate the authentication challenge, and include a User object to insert if the registration is successful. The method
returns the identifier for the self-registration attempt.

Note: If you specify a language in the `LanguageLocaleKey` field on the User object, Salesforce uses this language for
verification email and SMS messages.

Then call verifySelfRegistration, which, if the user enters the verification code correctly, logs in the user.

Example

This code contains the result of a verification challenge that registers a new user.

```
   String id = System.UserManagement.initSelfRegistration

         (Auth.VerificationMethod.SMS, user);

        Auth.VerificationResult res = System.UserManagement.verifySelfRegistration

         (Auth.VerificationMethod.SMS, id, ‘123456’, null);

        if(res.success == true){

      //redirect

   }

##### initVerificationMethod(method)

```

Initiates a verification service for email, phone (SMS), and the Salesforce Authenticator verification methods.

Signature

```
   public static String initVerificationMethod(Auth.VerificationMethod method)

```


Apex Reference Guide UserManagement Class

Parameters

```
   method
```

Type: Auth.VerificationMethod

Method used to initiate a verification service for `EMAIL`, `SMS`, or `SALESFORCE_AUTHENTICATOR` verification methods.

Return Value

Type: String

The returned identifier must be passed into `verifyVerificationMethod` .

Usage

Use this method along with its paired `verifyVerificationMethod` to customize a verification service for `EMAIL`, `SMS`, or
##### SALESFORCE_AUTHENTICATOR verification methods. The returned identifier from initVerificationMethod must be

passed into `verifyVerificationMethod` .

##### First invoke the initVerificationMethod method to send a verification code to the user’s email or phone number, or to send

a push notification to the Salesforce Authenticator. The user then enters the code or approves the push notification. If the verification
code isn’t valid or the push notification isn’t approved, the service returns an error message.

Email Example

This example shows multi-factor authentication using email.

```
   public void initVerification() {

   // user will receive code on their registered verified email

    identifier = UserManagement.initVerificationMethod(Auth.VerificationMethod.EMAIL);

   }

   public Auth.VerificationResult verifyVerification() {

   // requiring identifier from the initVerification

   // the code will need to be entered in this method

   return UserManagement.verifyVerificationMethod(identifier, code,

   Auth.VerificationMethod.EMAIL);

   }

##### initVerificationMethod(method, actionName, extras)

```

Initiates a verification service for email, phone (SMS), and the Salesforce Authenticator verification methods.

Signature

```
   public static String initVerificationMethod(Auth.VerificationMethod method, String

   actionName, Map<String,String> extras)

```

Parameters

```
   method
```

Type: Auth.VerificationMethod

Method used to initiate a verification service for `EMAIL`, `SMS`, or `SALESFORCE_AUTHENTICATOR` verification methods.


Apex Reference Guide UserManagement Class

```
   actionName
```

Type: String

For the `SALESFORCE_AUTHENTICATOR` verification method only, the name of the action to display on the Salesforce
Authenticator, such as `Connect to My Salesforce Org` . The default action name is `Apex-Defined Activity` .

```
   extras
```

[Type: Map<String,String>](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_maps.htm)

For the `SALESFORCE_AUTHENTICATOR` verification method only, the following extra settings.

**•** `secure_device_required` –If set to `true`, the user’s device must be secured. For example, the user must enter the
device’s passcode to approve the request. Default setting is `false` .

**•** `challenge_required` –If set to `true`, the user must complete a biometric challenge, such as face recognition, on the
device to approve the request. Default setting is `false` .

Return Value

Type: String

The returned identifier must be passed into `verifyVerificationMethod` method.

Usage

Use this method along with its paired `verifyVerificationMethod` to customize a verification service for `EMAIL`, `SMS`, or
`SALESFORCE_AUTHENTICATOR` verification methods. The returned identifier from `initVerificationMethod` must be
passed into `verifyVerificationMethod` method.

First invoke the `initVerificationMethod` method to send a verification code to the user’s email or phone number, or to send
a push notification to the Salesforce Authenticator. The user then enters the code or approves the push notification. If the verification
code isn’t valid or the push notification isn’t approved, the service returns an error message.

Salesforce Authenticator Example

This example shows multi-factor authentication (MFA) using the Salesforce Authenticator mobile app. In this example, the _`actionName`_
parameter is set to the default setting and the _`extra`_ parameter settings are set to `false` .

```
   public void initVerification() {

   // user will receive push notification on their registered MFA devices

   identifier =

   UserManagement.initVerificationMethod(Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR);

   }

   public Auth.VerificationResult verifyVerification() {

   // requiring identifier from the initVerification

   // user will need to take the action on their registered MFA devices

   return UserManagement.verifyVerificationMethod(identifier, '',

   Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR);

   }

```

This example shows multi-factor authentication using Salesforce Authenticator. In this example, the _`actionName`_ parameter is set
to `Connect to My Salesforce Org` and the `challenge_required` _`extra`_ parameter is set to `true` .

```
   public void initVerification() {

   Map<String,String> extras = new Map<String,String>();

```


Apex Reference Guide UserManagement Class

```
   extras.put('challenge_required','true');

   // user will receive push notification in their registered MFA devices

   identifier =

   UserManagement.initVerificationMethod(Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR,

   'Connect to My Salesforce Org', extras);

   }

   public Auth.VerificationResult verifyVerification() {

   // requiring identifier from the initVerification

   // user will need to take the action on their registered MFA devices

   return UserManagement.verifyVerificationMethod(identifier, '',

   Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR);

   }

##### obfuscateUser(userId, username)

```

Scrambles users’ data on their request when they no longer want their personal data recognized in Salesforce. When you invoke the
method for the user, the data becomes anonymous, and you can never recover it. Use this method to set the username to a specific
value after it’s scrambled.

Signature

```
   public static void obfuscateUser(Id userId, String username)

```

Parameters

```
   userId
```

Type: Id

ID of the user whose data this method scrambles.

```
   username
```

Type: String

The username after the user’s data is scrambled. Sets the value of the scrambled username to a specific string.

Return Value

Type: void

Usage

This method is introduced in API version 43.0. It isn't available in earlier versions.

##### You can use the obfuscateUser method to protect the personal information of your org’s users. When invoked, Salesforce

permanently scrambles the user’s object data and replaces it with random character strings. The user’s detail page exists, but the fields
contain meaningless strings of characters. Salesforce merely obfuscates (scrambles) personal data because you can't delete a user in
Salesforce; you can only disable or deactivate a user. In other words, the user record remains in the database and this method performs
a soft delete.

Note: Take care when using this method. The users’ data becomes anonymous and can never be recovered.

**Considerations**

**•** This method requires that the org’s User Management setting, **Scramble Specific Users' Data**, is enabled from Setup.


Apex Reference Guide UserManagement Class

**•** This method affects the standard fields of the user object—excluding a few fields such as the user ID, timezone, locale, and profile.

**•** It is recommended that you note the user's ID and other attributes for post processing, such as the email address, if you want to
send the user a confirmation.

**•** This method changes only the user object. The association between the user and other objects is removed, but no other objects are
changed. For example, contact, ThirdPartyAccountLink (TPAL), and user password authentication (UPA) objects remain unchanged.

Note: Assure your admins that invoking this method doesn’t trigger an email change notification.

This method is part of our effort to protect users’ personal data and privacy. For more information on what you can do to actively protect
user data, see Data Protection and Privacy in Salesforce Help.

##### obfuscateUser(userId)

Scrambles users’ data on their request when they no longer want their personal data recognized in Salesforce. When you invoke the
method for the user, the data becomes anonymous, and you can never recover it.

Signature

```
   public static void obfuscateUser(Id userId)

```

Parameters

```
   userId
```

Type: Id

ID of the user whose data this method scrambles.

Return Value

Type: void

Usage

This method is introduced in API version 43.0. It isn't available in earlier versions.

##### You can use the obfuscateUser method to protect the personal information of your org’s users. When invoked, Salesforce

permanently scrambles the user’s object data and replaces it with random character strings. The user’s detail page exists, but the fields
contain meaningless strings of characters. Salesforce merely obfuscates (scrambles) personal data because you can't delete a user in
Salesforce; you can only disable or deactivate a user. In other words, the user record remains in the database and this method performs
a soft delete.

Note: Take care when using this method. The users’ data becomes anonymous and can never be recovered.

**Considerations**

**•** This method requires that the org’s User Management setting, **Scramble Specific Users' Data**, is enabled from Setup.

**•** This method affects the standard fields of the user object—excluding a few fields such as the user ID, timezone, locale, and profile.

**•** If you want to send the user a confirmation, it’s recommended that you note the user's ID and other attributes for post processing,
such as the email address.

**•** This method changes only the user object. The association between the user and other objects is removed, but no other objects are
changed. For example, contact, ThirdPartyAccountLink (TPAL), and user password authentication (UPA) objects remain unchanged.


Apex Reference Guide UserManagement Class

Note: Assure your admins that invoking this method doesn’t trigger an email change notification.

This method is part of our effort to protect users’ personal data and privacy. For more information on what you can do to actively protect
user data, see Data Protection and Privacy in Salesforce Help.

ObfuscateUser Code Example

```
   public class UserManagementController{

      public List <User> users {get; set;}

      public UserManagementController()

      {

        Profile p = [select id from profile where name = 'Customer Community User'];

        users = [select username, id from User where profileId=:p.id AND isactive=true];

      }

      //Use method with extreme caution. Data can't be recovered.

      @InvocableMethod(label='User Management' description='Obfuscate User data and more')

      static public void obfuscate(List<User> users)

      {

        String uid = ApexPages.currentPage().getParameters().get('uid');

        if(uid == null)

           return;

        User u = [select contactId from user where id=:uid];

        System.UserManagement.obfuscateUser(uid);

      }

   }

##### registerVerificationMethod(method, startUrl)

```

Registers an identity verification method. Verification methods can be a time-based one-time password (TOTP), email or text verification
code, Salesforce Authenticator, or U2F-compatible security key. End users register verification methods for themselves.

Signature

```
   public static System.PageReference registerVerificationMethod(Auth.VerificationMethod

   method, String startUrl)

```

Parameters

```
   method
```

Type: Auth.VerificationMethod

Verification method used to verify the identity of the user.

```
   startUrl
```

Type: String

Path to the page that users see after they log in.


Apex Reference Guide UserManagement Class

Return Value

Type:System.PageReference

Usage

Use this method to enable users to complete identity verification, such as multi-factor authentication (MFA), or to log in to their Experience
Cloud site without a password. Users register these methods to verify their identity when logging in. You create a custom registration
page when implementing mobile-centric passwordless logins. See VerifyPasswordlessLogin.

The `PageReference` returned by `registerVerificationMethod` redirects the user to the Salesforce Verify page. If the
user enters the correct code, the user is redirected to the Experience Cloud site page specified by the start URL. For example:

```
   PageReference pr =

   System.UserManagement.registerVerificationMethod(Auth.VerificationMethod.TOTP,startUrl);

   PageReference p =

   System.UserManagement.deregisterVerificationMethod(userId,Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR);

```

This method is available in API version 43.0 and later.

Note: As a security measure, when users add or update mobile numbers in their detail page, they must log in again to verify their
identity. As a result, unsaved changes in the app are lost. To disable this security measure, contact Salesforce Support.

##### sendAsyncEmailConfirmation(userId, emailTemplateId, networkId, startUrl)

Send an email message to a user’s email address for verification. The message contains a verification link (URL) that the user clicks to
verify the email address later on. You can send email verifications in bulk.

Signature

```
   public static Boolean sendAsyncEmailConfirmation(String userId, String emailTemplateId,

   String networkId, String startUrl)

```

Parameters

```
   userId
```

Type: String

ID of the user to receive the email confirmation.

```
   emailTemplateId
```

Type: String

ID of the email template in which the verification link is defined. If `null`, Salesforce sends a default email. Here's how the default
email looks.


Apex Reference Guide UserManagement Class

```
   networkId
```

Type: String

If verifying email addresses for Experience Cloud site users, the ID of the Experience Cloud site. In addition to external users (such as
customers and partners), Experience Cloud site users can include internal users (such as employees) who are members of the site.
To verify email addresses for internal users only, set this parameter to `null` .

```
   startUrl
```

Type: String

The user is redirected to this page after verification, with a success or error message as the parameter. If null, the user is redirected
to the login page.

Return Value

Type: Boolean

Indicates whether sending the email message succeeded or failed.

Usage

Sending an async email message is good practice to ensure that users are registered with a valid email address that they truly own. To
determine which users receive an email with the verification link, check whether the User Verified Email field in the User detail page is
set to true. You can also get this information from the `TwoFactorMethodsInfo` API.

Send async email verification to customers and partners to verify their email address. These users must verify their email address before
they can log in with email OTP (passwordless login).

The error code and description are passed as query parameters so that you can process any errors when building a custom landing page.

Example

```
   System.UserManagement.sendAsyncEmailConfirmation('005RM000001a0Ox',

   '00XRM000000hxnG','0DBRM000000015i', '/s/contactsupport');

##### verifyPasswordlessLogin(userId, method, identifier, code, startUrl)

```

Completes a verification challenge during a passwordless login that uses a custom Verify page (Visualforce only). If the user who is trying
to log in enters the verification code successfully, the user is logged in.


Apex Reference Guide UserManagement Class

Signature

```
   public static Auth.VerificationResult verifyPasswordlessLogin(Id userId,

   Auth.VerificationMethod method, String identifier, String code, String startUrl)

```

Parameters

```
   userId
```

Type: Id

ID of the user who’s logging in.

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the identity of the user, which can be either EMAIL or SMS.

```
   identifier
```

Type: String

ID of the verification attempt received from the `initPasswordlessLogin` method.

```
   code
```

Type: String

Code used to verify the identity of the user.

```
   startUrl
```

Type: String

The page where the user is directed after successful login.

Return Value

Type: Auth.VerificationResult

Result of the verification challenge, which includes the message displayed, and where the user is directed if they enter the verification
code correctly.

Usage

Call this method to complete the passwordless login authentication process. It validates the verification method and verification code.
It also checks that the identifier is the same as the one returned by `initPasswordlessLogin` on page 4400.

Example

For an example, see `Auth.VerificationResult` .

##### verifyRegisterVerificationMethod(code, method)

Completes registering a user’s email address or phone number as a verification method when customizing the identity verification
process.

Signature

```
   public static String verifyRegisterVerificationMethod(String code,

   Auth.VerificationMethod method)

```


Apex Reference Guide UserManagement Class

Parameters

```
   code
```

Type: String

Code used to verify the identity of the user.

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the identity of the user, which can be either EMAIL or SMS.

Return Value

Type: String

If the user enters an incorrect verification code, the method returns an error message.

Usage

Call `verifyRegisterVerificationMethod` to complete the process of registering a user’s verification method. This method
checks whether the user entered the correct verification code. If the verification code is correct, the method

**•** Confirms that the user entered the correct verification code

**•** From the user’s detail page, updates the user's verification method status (sets the verification bit)

**•** Sends an email to the user confirming that a verification method has been added to their record

If the verification code is incorrect, an error message is returned.

Note: If users want to change their email address after registering one, don’t use the `initRegisterVerificationMethod`
and `verify RegisterVerificationMethod` methods. To enable automatic identity verification for email address
changes, from the Identity Verification Setup page, select the field **Require email confirmations for email address changes**
**(applies to users in Experience Builder sites)** .

Example

Here’s a code example that registers a user’s phone number as a verification method. When the user enters a verification code on the
Visualforce page, it invokes `registerUser()` . The method gets the User ID of the user who’s registering the verification method
and the user’s phone number. It also gets the user’s registration status to check whether the phone number is verified already. If the
user is registered with a different phone number, the number is updated.

```
   public void registerUser() {

        try {

           exceptionText='';

           String userId = UserInfo.getUserId();

           User u = [Select MobilePhone, Id from User Where Id=:userId];

           currPhone = u.MobilePhone;

           mobilePhone = getFormattedSms(mobilePhone);

          if (mobilePhone != null && mobilePhone != '') {

          u.MobilePhone = mobilePhone;

          update u;

           // We're updating the email and phone number before verifying. Roll back

          // the change in the verify API if it is unsuccessful.

           exceptionText = System.

           UserManagement.initRegisterVerificationMethod(Auth.VerificationMethod.SMS);

           if(exceptionText!= null && exceptionText!=''){

```


Apex Reference Guide UserManagement Class

```
             isInit = false;

             showInitException = true;

           } else {

              isInit = false;

              isVerify = true;

           }

           } else {

             showInitException = true;

           }

        } catch (Exception e) {

           exceptionText = e.getMessage();

           isInit = false;

           showInitException = true;

        }

      }

   public void verifyUser() {

      // Take the user’s input for the code sent to their phone number

      exceptionText = System.UserManagement.

        verifyRegisterVerificationMethod(code, Auth.VerificationMethod.SMS);

      if(exceptionText != null && exceptionText !=''){

      showInitException = true;

      } else {

           //Success

      }

   }

##### verifySelfRegistration(method, identifier, code, startUrl)

```

Completes a verification challenge when creating a custom (Visualforce) Verify page for Experience Cloud site self-registration. If the
person who is attempting to register enters the verification code successfully, the user is created and logged in.

Signature

```
   public static Auth.VerificationResult verifySelfRegistration(Auth.VerificationMethod

   method, String identifier, String code, String startUrl)

```

Parameters

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the identity of the user, which can be either EMAIL or SMS.

```
   identifier
```

Type: String

The unique identifier received from the `initSelfRegistration` method.

```
   code
```

Type: String

Code used to verify the identity of the user.

```
   startUrl
```

Type: String


Apex Reference Guide UserManagement Class

[The page where the user is directed after successful self-registration. For the Self-Registration component, set the Start URL in the](https://help.salesforce.com/s/articleView?id=experience.rss_login_self_register.htm&language=en_US)
component properties instead.

Return Value

Type: Auth.VerificationResult

Result of the verification challenge, which includes the message displayed, and where the user is directed when they enter the verification
code correctly.

Usage

By default, when users sign up for your Experience Cloud site with an email address or phone number, Salesforce sends them a verification
code and generates a Verify page. This Verify page is where users enter the verification code to confirm their identity. You can replace
this Salesforce-generated Verify page with a custom Verify page that you create with Visualforce. Then you invoke the verification process
with Apex methods.

First, call the `initSelfRegistration` method, which returns the identifier of the user to create. Then call this
`verifySelfRegistration` method to complete the verification process. If the user enters the verification code correctly, the
user is created and directed to the page specified in the `startURL` .

This method returns the verification result, which contains the verification status and, if the user is created, the session ID. If the verification
method is SMS, the User object must contain a properly formatted mobile number, which is country code, space, and then phone
number, for example, +1 1234567890. Use `System.UserManagement.formatPhoneNumber` to ensure that the phone
number is formatted correctly.

Example

This code contains the result of a verification challenge that registers a new user.

```
   String id = System.UserManagement.initSelfRegistration

         (Auth.VerificationMethod.SMS, user);

        Auth.VerificationResult res = System.UserManagement.verifySelfRegistration

         (Auth.VerificationMethod.SMS, id, ‘123456’, null);

        if(res.success == true){

      //redirect

   }

##### verifyVerificationMethod(identifier, code, method)

```

Completes the verification service for email, phone (SMS), Salesforce Authenticator, password, or time-based one-time password (TOTP)
verification methods.

Signature

```
   public static VerificationResult verifyVerificationMethod(String identifier, String

   code, Auth.VerificationMethod method)

```

Parameters

```
   identifier
```

Type: String

Identifier returned from `initVerificationMethod` for `EMAIL`, `SMS`, and `SALESFORCE_AUTHENTICATOR` .


Apex Reference Guide UserManagement Class

```
   code
```

Type: String

Code used to verify the user’s identity for `EMAIL`, `SMS`, or `PASSWORD` .

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the user’s identity, which can be `EMAIL`, `PASSWORD`, `SALESFORCE_AUTHENTICATOR`, `SMS`, or `TOTP` .

Return Value

Type: VerificationResult

Usage

Use this method along with its paired `initVerificationMethod` to customize a verification service for `EMAIL`, `SMS`, or
`SALESFORCE_AUTHENTICATOR` verification methods. Or use this method alone to provide a complete verification service for
`PASSWORD` and `TOTP` verification methods.

This method checks whether the user entered the correct verification code or password. If the verification code or password is correct,
the method verifies the user’s identity.

If the verification code or password isn’t valid, the service returns an error message.

Examples

This example shows multi-factor authentication using email.

```
   public void initVerification() {

   // user will receive code on their registered verified email

    identifier = UserManagement.initVerificationMethod(Auth.VerificationMethod.EMAIL);

   }

   public Auth.VerificationResult verifyVerification() {

   // requiring identifier from the initVerification

   // the code will need to be entered in this method

   return UserManagement.verifyVerificationMethod(identifier, code,

   Auth.VerificationMethod.EMAIL);

   }

```

The next two examples show multi-factor authentication using only the `verifyVerificationMethod` for password and TOTP
verifications.

```
   public Auth.VerificationResult verifyVerification() {

   // user will enter their password as a param in the verifyVerificationMethod for password

    verification method

   return UserManagement.verifyVerificationMethod('', password,

   Auth.VerificationMethod.PASSWORD);

   }

   public Auth.VerificationResult verifyVerification() {

   // user will enter their registered time-based one-time password (TOTP) code (token)

   return UserManagement.verifyVerificationMethod('', code, Auth.VerificationMethod.TOTP);

   }

```


### Apex Reference Guide UUID Class UUID Class

Contains methods to randomly generate a version 4 universally unique identifier (UUID), compare UUIDs, and convert UUID instance to
a string.

Namespace

System

Usage

The UUID is generated using a cryptographically strong pseudo-random number generator and is represented as 32 hexadecimal values.

IN THIS SECTION:

#### UUID Methods UUID Methods

### The following are methods for UUID .

IN THIS SECTION:

##### equals(obj)

Compares a UUID instance with the specified object and returns true if both are equal. Otherwise, returns false.

fromString(str)
Converts a 32 character hexadecimal string representation of a UUID to a UUID instance.

hashCode()
Returns the hashcode corresponding to the UUID instance.

randomUUID()
A static method that randomly generates a version 4 UUID.

toString()
Returns the string representation of the UUID instance.

##### **`equals(obj)`**

Compares a UUID instance with the specified object and returns true if both are equal. Otherwise, returns false.

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

The UUID object to be compared.


Apex Reference Guide UUID Class

Return Value

Type: Boolean

Example

```
   // UUIDs are equal when all the characters in the UUID are the same

   String uuidStr = '707b2538-98bb-41e7-95e3-1d77bf42b102';

   UUID fromStr = UUID.fromString(uuidStr);

   UUID fromStr2 = UUID.fromString(uuidStr);

   Assert.isTrue(fromStr.equals(fromStr2));

   // A UUID is never equal to a String or any non-UUID object

   Assert.isFalse(fromStr.equals(uuidStr));

##### **`fromString(str)`**

```

Converts a 32 character hexadecimal string representation of a UUID to a UUID instance.

Signature

```
   public static System.UUID fromString(String str)

```

Parameters

```
   str
```

Type: String

Return Value

Type: System.UUID

Example

```
   String uuidStr = '707b2538-98bb-41e7-95e3-1d77bf42b102';

   UUID fromStr = UUID.fromString(uuidStr);

   UUID.fromString(null); // Throws NullPointerException

   UUID.fromString(‘not a uuid’); // Throws IllegalArgumentException

##### **`hashCode()`**

```

Returns the hashcode corresponding to the UUID instance.

Signature

```
   public Integer hashCode()

```


### Apex Reference Guide Version Class

Return Value

Type: Integer

##### **`randomUUID()`**

A static method that randomly generates a version 4 UUID.

Signature

```
   public static System.UUID randomUUID()

```

Return Value

Type: System.UUID

A 32 hexadecimal value of the UUID generated.

Example

```
   UUID randomUUID = UUID.randomUUID();

   system.debug(randomUUID); // Prints the UUID string that was randomly generated

##### **`toString()`**

```

Returns the string representation of the UUID instance.

Signature

```
   public String toString()

```

Return Value

Type: String

### Version Class

Use the Version methods to get the version of a first-generation managed package (1GP) or a migrated second-generation managed
package (2GP), and to compare package versions.

Namespace

System

Usage

A package version is a number that identifies the set of components uploaded in a package. The version number has the format
_`majorNumber.minorNumber.patchNumber`_ (for example, 2.1.3). The major and minor numbers increase to a chosen value
during every major release. The _`patchNumber`_ is generated and updated only for a patch release.


Apex Reference Guide Version Class

A called component can check the version against which the caller was compiled using the `System.requestVersion` on page
4323 method and behave differently depending on the caller’s expectations. This allows you to continue to support existing behavior in
classes and triggers in previous package versions while continuing to evolve the code.

The value returned by the `System.requestVersion` method is an instance of this class with a two-part version number containing
a major and a minor number. Since the `System.requestVersion` method doesn’t return a patch number, the patch number in
the returned Version object is null.

The `System.Version` class can also hold also a three-part version number that includes a patch number.

[See Version Apex Code Behavior in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_manpkgs_behavior.htm) _Apex Developer Guide_ .

Example

This example shows how to use the methods in this class, along with the `requestVersion` method, to determine the managed
package version of the code that is calling your package.

```
   if (System.requestVersion() == new Version(1,0))

   {

      // Do something

   }

   if ((System.requestVersion().major() == 1)

      && (System.requestVersion().minor() > 0)

      && (System.requestVersion().minor() <=9))

   {

      // Do something different for versions 1.1 to 1.9

   }

   else if (System.requestVersion().compareTo(new Version(2,0)) >= 0)

   {

      // Do something completely different for versions 2.0 or greater

   }

```

IN THIS SECTION:

#### Version Constructors

Version Methods

#### Version Constructors The following are constructors for Version .

IN THIS SECTION:

##### Version(major, minor)
#### Creates a new instance of the Version class as a two-part package version using the specified major and minor version numbers.

Version(major, minor, patch)
#### Creates a new instance of the Version class as a three-part package version using the specified major, minor, and patch version

numbers.

##### Version(major, minor)

#### Creates a new instance of the Version class as a two-part package version using the specified major and minor version numbers.


Apex Reference Guide Version Class

Signature

```
   public Version(Integer major, Integer minor)

```

Parameters

```
   major
```

Type: Integer

The major version number.

```
   minor
```

Type: Integer

The minor version number.

##### Version(major, minor, patch) Creates a new instance of the Version class as a three-part package version using the specified major, minor, and patch version

numbers.

Signature

```
   public Version(Integer major, Integer minor, Integer patch)

```

Parameters

```
   major
```

Type: Integer

The major version number.

```
   minor
```

Type: Integer

The minor version number.

```
   patch
```

Type: Integer

The patch version number.

#### Version Methods

##### The following are methods for Version . All are instance methods.

IN THIS SECTION:

compareTo(version)
Compares the current version with the specified version.

major()
Returns the major package version of the of the calling code.

minor()
Returns the minor package version of the calling code.


Apex Reference Guide Version Class

patch()
Returns the patch package version of the calling code or `null` if there is no patch version.

##### compareTo(version)

Compares the current version with the specified version.

Signature

```
   public Integer compareTo(System.Version version)

```

Parameters

```
   version
```

Type: System.Version

Return Value

Type: Integer

Returns one of the following values:

**•** zero if the current package version is equal to the specified package version

**•** an Integer value greater than zero if the current package version is greater than the specified package version

**•** an Integer value less than zero if the current package version is less than the specified package version

Usage

If a two-part version is being compared to a three-part version, the patch number is ignored and the comparison is based only on the
major and minor numbers.

##### major()

Returns the major package version of the of the calling code.

Signature

```
   public Integer major()

```

Return Value

Type: Integer

##### minor()

Returns the minor package version of the calling code.

Signature

```
   public Integer minor()

```


### Apex Reference Guide WebServiceCallout Class

Return Value

Type: Integer

##### patch()

Returns the patch package version of the calling code or `null` if there is no patch version.

Signature

```
   public Integer patch()

```

Return Value

Type: Integer

### WebServiceCallout Class

Enables making callouts to SOAP operations on an external Web service. This class is used in the Apex stub class that is auto-generated
from a WSDL.

Namespace

System

IN THIS SECTION:

#### WebServiceCallout Methods

SEE ALSO:

_Apex Developer Guide_ [: SOAP Services: Defining a Class from a WSDL Document](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_wsdl2apex.htm)

#### WebServiceCallout Methods

### The following is the static method for WebServiceCallout .

IN THIS SECTION:

##### invoke(stub, request, response, infoArray)

Invokes an external SOAP web service operation based on an Apex class that is auto-generated from a WSDL.

##### invoke(stub, request, response, infoArray)

Invokes an external SOAP web service operation based on an Apex class that is auto-generated from a WSDL.

Signature

```
   public static void invoke(Object stub, Object request, Map<String,Object> response,

   List<String> infoArray)

```


### Apex Reference Guide WebServiceMock Interface

Parameters

```
   stub
```

Type: Object

An instance of the Apex class that is auto-generated from a WSDL (the stub class).

```
   request
```

Type: Object

The request to the external service. The request is an instance of a type that is created as part of the auto-generated stub class.

```
   response
```

Type: Map<String, Object>

A map of key-value pairs that represent the response that the external service sends after receiving the request. In each pair, the key
is a response identifier. The value is the response object, which is an instance of a type that is created as part of the auto-generated
stub class.

```
   infoArray
```

Type: String[]

An array of strings that contains information about the callout—web service endpoint, SOAP action, request, and response. The
order of the elements in the array matters.

**•** Element at index 0 ( `[0]` ): One of the following options for identifying the URL of the external web service.

**–** Endpoint URL. For example: `'http://YourServer/YourService'`

**–** Named credential URL, which contains the scheme `callout`, the name of the named credential, and optionally, an
appended path. For example: `'callout:MyNamedCredential/some/path'`

**•** Element at index 1 ( `[1]` ): The SOAP action. For example:

```
      'urn:dotnet.callouttest.soap.sforce.com/EchoString'

```

**•** Element at index 2 ( `[2]` ): The request namespace. For example: `'http://doc.sample.com/docSample'`

**•** Element at index 3 ( `[3]` ): The request name. For example: `'EchoString'`

**•** Element at index 4 ( `[4]` ): The response namespace. For example: `'http://doc.sample.com/docSample'`

**•** Element at index 5 ( `[5]` ): The response name. For example: `'EchoStringResponse'`

**•** Element at index 6 ( `[6]` ): The response type. For example: `'docSample.EchoStringResponse_element'`

Return Value

Type: Void

SEE ALSO:

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

### WebServiceMock Interface

Enables sending fake responses when testing Web service callouts of a class auto-generated from a WSDL.

Namespace

System


Apex Reference Guide WebServiceMock Interface

Usage

[For an implementation example, see Test Web Service Callouts.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_wsdl2apex_testing.htm)

#### WebServiceMock Methods The following are methods for WebServiceMock .

IN THIS SECTION:

##### doInvoke(stub, soapRequest, responseMap, endpoint, soapAction, requestName, responseNamespace, responseName, responseType)

The implementation of this method is called by the Apex runtime to send a fake response when a Web service callout is made after
`Test.setMock` has been called.

##### doInvoke(stub, soapRequest, responseMap, endpoint, soapAction, requestName,

responseNamespace, responseName, responseType)

The implementation of this method is called by the Apex runtime to send a fake response when a Web service callout is made after
`Test.setMock` has been called.

Signature

```
   public Void doInvoke(Object stub, Object soapRequest, Map<String,Object> responseMap,

   String endpoint, String soapAction, String requestName, String responseNamespace, String

   responseName, String responseType)

```

Parameters

```
   stub
```

Type: Object

An instance of the auto-generated class.

```
   soapRequest
```

Type: Object

The SOAP Web service request being invoked.

```
   responseMap
```

Type: Map<String, Object>

A collection of key/value pairs representing the response to send for the request.

When implementing this interface, set the _`responseMap`_ argument to a key/value pair representing the response desired.

```
   endpoint
```

Type: String

The endpoint URL for the request.

```
   soapAction
```

Type: String

The requested SOAP operation.

```
   requestName
```

Type: String


### Apex Reference Guide XmlStreamReader Class

The requested SOAP operation name.

```
   responseNamespace
```

Type: String

The response namespace.

```
   responseName
```

Type: String

The name of the response element as defined in the WSDL.

```
   responseType
```

Type: String

The class for the response as defined in the auto-generated class.

Return Value

Type: Void

Usage

### XmlStreamReader Class The XmlStreamReader class provides methods for forward, read-only access to XML data. You can pull data from XML or skip

unwanted events. You can parse nested XML content that’s up to 50 nodes deep.

Namespace

System

Usage

### The XmlStreamReader class is similar to the XMLStreamReader utility class from StAX (Streaming API for XML). StAX is an API to

read and write XML documents, originating from the Java programming language community.

### Note: The XmlStreamReader class in Apex is based on its counterpart in Java. See Java XMLStreamReader class .

IN THIS SECTION:

#### XmlStreamReader Constructors

XmlStreamReader Methods

SEE ALSO:

_Apex Developer Guide_ [: Reading XML Using Streams](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_xml_streaming_reading.htm)

#### XmlStreamReader Constructors

### The following are constructors for XmlStreamReader .


Apex Reference Guide XmlStreamReader Class

IN THIS SECTION:

##### XmlStreamReader(xmlInput) Creates a new instance of the XmlStreamReader class for the specified XML input. XmlStreamReader(xmlInput) Creates a new instance of the XmlStreamReader class for the specified XML input.

Signature

```
   public XmlStreamReader(String xmlInput)

```

Parameters

```
   xmlInput
```

Type: String

The XML string input.

#### XmlStreamReader Methods

##### The following are methods for XmlStreamReader . All are instance methods.

IN THIS SECTION:

getAttributeCount()
Returns the number of attributes on the start element, excluding namespace definitions.

getAttributeLocalName(index)
Returns the local name of the attribute at the specified index.

getAttributeNamespace(index)
Returns the namespace URI of the attribute at the specified index.

getAttributePrefix(index)
Returns the prefix of this attribute at the specified index.

getAttributeType(index)
Returns the XML type of the attribute at the specified index.

getAttributeValue(namespaceUri, localName)
Returns the value of the attribute in the specified _`localName`_ at the specified URI.

getAttributeValueAt(index)
Returns the value of the attribute at the specified index.

getEventType()
Returns the type of XML event the cursor is pointing to.

getLocalName()
Returns the local name of the current event.

getLocation()
Return the current location of the cursor.


Apex Reference Guide XmlStreamReader Class

getNamespace()
If the current event is a start element or end element, this method returns the URI of the prefix or the default namespace.

getNamespaceCount()
Returns the number of namespaces declared on a start element or end element.

getNamespacePrefix(index)
Returns the prefix for the namespace declared at the index.

getNamespaceURI(prefix)
Return the URI for the given prefix.

getNamespaceURIAt(index)
Returns the URI for the namespace declared at the index.

getPIData()
Returns the data section of a processing instruction.

getPITarget()
Returns the target section of a processing instruction.

getPrefix()
Returns the prefix of the current XML event or `null` if the event does not have a prefix.

getText()
Returns the current value of the XML event as a string.

getVersion()
Returns the XML version specified on the XML declaration. Returns `null` if none was declared.

hasName()
Returns `true` if the current XML event has a name. Returns `false` otherwise.

hasNext()
Returns `true` if there are more XML events and `false` if there are no more XML events.

hasText()
Returns `true` if the current event has text, `false` otherwise.

isCharacters()
Returns `true` if the cursor points to a character data XML event. Otherwise, returns `false` .

isEndElement()
Returns `true` if the cursor points to an end tag. Otherwise, it returns `false` .

isStartElement()
Returns `true` if the cursor points to a start tag. Otherwise, it returns `false` .

isWhiteSpace()
Returns `true` if the cursor points to a character data XML event that consists of all white space. Otherwise it returns `false` .

next()
Reads the next XML event. A processor may return all contiguous character data in a single chunk, or it may split it into several
chunks. Returns an integer which indicates the type of event.

nextTag()
Skips any white space (the `isWhiteSpace` method returns `true` ), comment, or processing instruction XML events, until a start
element or end element is reached. Returns the index for that XML event.


Apex Reference Guide XmlStreamReader Class

setCoalescing(returnAsSingleBlock)
If you specify `true` for _`returnAsSingleBlock`_, text is returned in a single block, from a start element to the first end element
or the next start element, whichever comes first. If you specify it as `false`, the parser may return text in multiple blocks.

setNamespaceAware(isNamespaceAware)
If you specify `true` for _`isNamespaceAware`_, the parser recognizes namespace. If you specify it as `false`, the parser does
not. The default value is `true` .

toString()
Returns a string containing the length of the input XML given to `XmlStreamReader` and the first 50 characters of the input
XML.

##### getAttributeCount()

Returns the number of attributes on the start element, excluding namespace definitions.

Signature

```
   public Integer getAttributeCount()

```

Return Value

Type: Integer

Usage

This method is only valid on a start element or attribute XML events. The count for the number of attributes for an attribute XML event
starts with zero.

##### getAttributeLocalName(index)

Returns the local name of the attribute at the specified index.

Signature

```
   public String getAttributeLocalName(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

If there is no name, an empty string is returned. This method is only valid with start element or attribute XML events.


Apex Reference Guide XmlStreamReader Class

##### getAttributeNamespace(index)

Returns the namespace URI of the attribute at the specified index.

Signature

```
   public String getAttributeNamespace(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

If no namespace is specified, `null` is returned. This method is only valid with start element or attribute XML events.

##### getAttributePrefix(index)

Returns the prefix of this attribute at the specified index.

Signature

```
   public String getAttributePrefix(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

If no prefix is specified, `null` is returned. This method is only valid with start element or attribute XML events.

##### getAttributeType(index)

Returns the XML type of the attribute at the specified index.

Signature

```
   public String getAttributeType(Integer index)

```


Apex Reference Guide XmlStreamReader Class

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

For example, `id` is an attribute type. This method is only valid with start element or attribute XML events.

##### getAttributeValue(namespaceUri, localName)

Returns the value of the attribute in the specified _`localName`_ at the specified URI.

Signature

```
   public String getAttributeValue(String namespaceUri, String localName)

```

Parameters

```
   namespaceUri
```

Type: String

```
   localName
```

Type: String

Return Value

Type: String

Usage

Returns `null` if the value is not found. You must specify a value for _`localName`_ . This method is only valid with start element or
attribute XML events.

##### getAttributeValueAt(index)

Returns the value of the attribute at the specified index.

Signature

```
   public String getAttributeValueAt(Integer index)

```

Parameters

```
   index
```

Type: Integer


Apex Reference Guide XmlStreamReader Class

Return Value

Type: String

Usage

This method is only valid with start element or attribute XML events.

##### getEventType()

Returns the type of XML event the cursor is pointing to.

Signature

```
   public System.XmlTag getEventType()

```

Return Value

Type: System.XmlTag

**`XmlTag`** Enum

The values for `XmlTag` are:

**•** `ATTRIBUTE`

**•** `CDATA`

**•** `CHARACTERS`

**•** `COMMENT`

**•** `DTD`

**•** `END_DOCUMENT`

**•** `END_ELEMENT`

**•** `ENTITY_DECLARATION`

**•** `ENTITY_REFERENCE`

**•** `NAMESPACE`

**•** `NOTATION_DECLARATION`

**•** `PROCESSING_INSTRUCTION`

**•** `SPACE`

**•** `START_DOCUMENT`

**•** `START_ELEMENT`

##### getLocalName()

Returns the local name of the current event.

Signature

```
   public String getLocalName()

```


Apex Reference Guide XmlStreamReader Class

Return Value

Type: String

Usage

For start element or end element XML events, it returns the local name of the current element. For the entity reference XML event, it
returns the entity name. The current XML event must be start element, end element, or entity reference.

##### getLocation()

Return the current location of the cursor.

Signature

```
   public String getLocation()

```

Return Value

Type: String

Usage

If the location is unknown, returns -1. The location information is only valid until the `next` method is called.

##### getNamespace()

If the current event is a start element or end element, this method returns the URI of the prefix or the default namespace.

Signature

```
   public String getNamespace()

```

Return Value

Type: String

Usage

Returns `null` if the XML event does not have a prefix.

##### getNamespaceCount()

Returns the number of namespaces declared on a start element or end element.

Signature

```
   public Integer getNamespaceCount()

```

Return Value

Type: Integer


Apex Reference Guide XmlStreamReader Class

Usage

This method is only valid on a start element, end element, or namespace XML event.

##### getNamespacePrefix(index)

Returns the prefix for the namespace declared at the index.

Signature

```
   public String getNamespacePrefix(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

Returns `null` if this is the default namespace declaration. This method is only valid on a start element, end element, or namespace
XML event.

##### getNamespaceURI(prefix)

Return the URI for the given prefix.

Signature

```
   public String getNamespaceURI(String prefix)

```

Parameters

```
   prefix
```

Type: String

Return Value

Type: String

Usage

The returned URI depends on the current state of the processor.

##### getNamespaceURIAt(index)

Returns the URI for the namespace declared at the index.


Apex Reference Guide XmlStreamReader Class

Signature

```
   public String getNamespaceURIAt(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

This method is only valid on a start element, end element, or namespace XML event.

##### getPIData()

Returns the data section of a processing instruction.

Signature

```
   public String getPIData()

```

Return Value

Type: String

##### getPITarget()

Returns the target section of a processing instruction.

Signature

```
   public String getPITarget()

```

Return Value

Type: String

##### getPrefix()

Returns the prefix of the current XML event or `null` if the event does not have a prefix.

Signature

```
   public String getPrefix()

```

Return Value

Type: String


Apex Reference Guide XmlStreamReader Class

##### getText()

Returns the current value of the XML event as a string.

Signature

```
   public String getText()

```

Return Value

Type: String

Usage

The valid values for the different events are:

**•** The string value of a character XML event

**•** The string value of a comment

##### • The replacement value for an entity reference. For example, assume getText reads the following XML snippet:

```
     <!ENTITY

      Title "Salesforce For Dummies" >

        ]>

      <moo a=\"b\">Name &Title;</moo>';

##### The getText method returns Salesforce for Dummies, not &Title .

```

**•** The string value of a CDATA section

**•** The string value for a space XML event

**•** The string value of the internal subset of the DTD

##### getVersion()

Returns the XML version specified on the XML declaration. Returns `null` if none was declared.

Signature

```
   public String getVersion()

```

Return Value

Type: String

##### hasName()

Returns `true` if the current XML event has a name. Returns `false` otherwise.

Signature

```
   public Boolean hasName()

```


Apex Reference Guide XmlStreamReader Class

Return Value

Type: Boolean

Usage

This method is only valid for start element and stop element XML events.

##### hasNext()

Returns `true` if there are more XML events and `false` if there are no more XML events.

Signature

```
   public Boolean hasNext()

```

Return Value

Type: Boolean

Usage

This method returns `false` if the current XML event is end document.

##### hasText()

Returns `true` if the current event has text, `false` otherwise.

Signature

```
   public Boolean hasText()

```

Return Value

Type: Boolean

Usage

The following XML events have text: characters, entity reference, comment and space.

##### isCharacters()

Returns `true` if the cursor points to a character data XML event. Otherwise, returns `false` .

Signature

```
   public Boolean isCharacters()

```

Return Value

Type: Boolean


Apex Reference Guide XmlStreamReader Class

##### isEndElement()

Returns `true` if the cursor points to an end tag. Otherwise, it returns `false` .

Signature

```
   public Boolean isEndElement()

```

Return Value

Type: Boolean

##### isStartElement()

Returns `true` if the cursor points to a start tag. Otherwise, it returns `false` .

Signature

```
   public Boolean isStartElement()

```

Return Value

Type: Boolean

##### isWhiteSpace()

Returns `true` if the cursor points to a character data XML event that consists of all white space. Otherwise it returns `false` .

Signature

```
   public Boolean isWhiteSpace()

```

Return Value

Type: Boolean

##### next()

Reads the next XML event. A processor may return all contiguous character data in a single chunk, or it may split it into several chunks.
Returns an integer which indicates the type of event.

Signature

```
   public Integer next()

```

Return Value

Type: Integer


Apex Reference Guide XmlStreamReader Class

##### nextTag()

Skips any white space (the `isWhiteSpace` method returns `true` ), comment, or processing instruction XML events, until a start
element or end element is reached. Returns the index for that XML event.

Signature

```
   public Integer nextTag()

```

Return Value

Type: Integer

Usage

This method throws an error if elements other than white space, comments, processing instruction, start elements or stop elements are
encountered.

##### setCoalescing(returnAsSingleBlock)

If you specify `true` for _`returnAsSingleBlock`_, text is returned in a single block, from a start element to the first end element
or the next start element, whichever comes first. If you specify it as `false`, the parser may return text in multiple blocks.

Signature

```
   public Void setCoalescing(Boolean returnAsSingleBlock)

```

Parameters

```
   returnAsSingleBlock
```

Type: Boolean

Return Value

Type: Void

##### setNamespaceAware(isNamespaceAware)

If you specify `true` for _`isNamespaceAware`_, the parser recognizes namespace. If you specify it as `false`, the parser does not.
The default value is `true` .

Signature

```
   public Void setNamespaceAware(Boolean isNamespaceAware)

```

Parameters

```
   isNamespaceAware
```

Type: Boolean


### Apex Reference Guide XmlStreamWriter Class

Return Value

Type: Void

##### toString()

Returns a string containing the length of the input XML given to `XmlStreamReader` and the first 50 characters of the input XML.

Signature

```
   public String toString()

```

Return Value

Type: String

### XmlStreamWriter Class The XmlStreamWriter class provides methods for writing XML data.

Namespace

System

Usage

### You can use the XmlStreamWriter class to programmatically construct an XML document, then use HTTP classes to send the

document to an external server.

### The XmlStreamWriter class is similar to the XMLStreamWriter utility class from StAX (Streaming API for XML). StAX is an API to

read and write XML documents, originating from the Java programming language community.

### Note: The XmlStreamWriter class in Apex is based on its counterpart in Java. See Java XMLStreamWriter class .

IN THIS SECTION:

#### XmlStreamWriter Constructors

XmlStreamWriter Methods

SEE ALSO:

Http Class

HttpRequest Class

HttpResponse Class

#### XmlStreamWriter Constructors

### The following are constructors for XmlStreamWriter .


Apex Reference Guide XmlStreamWriter Class

IN THIS SECTION:

##### XmlStreamWriter() Creates a new instance of the XmlStreamWriter class. XmlStreamWriter() Creates a new instance of the XmlStreamWriter class.

Signature

```
   public XmlStreamWriter()

#### XmlStreamWriter Methods

##### The following are methods for XmlStreamWriter . All are instance methods.

```

IN THIS SECTION:

close()
Closes this instance of an XmlStreamWriter and free any resources associated with it.

getXmlString()
Returns the XML written by the XmlStreamWriter instance.

setDefaultNamespace(uri)
Binds the specified URI to the default namespace. This URI is bound in the scope of the current START_ELEMENT – END_ELEMENT
pair.

writeAttribute(prefix, namespaceUri, localName, value)
Writes an attribute to the output stream.

writeCData(data)
Writes the specified CData to the output stream.

writeCharacters(text)
Writes the specified text to the output stream.

writeComment(comment)
Writes the specified comment to the output stream.

writeDefaultNamespace(namespaceUri)
Writes the specified namespace to the output stream.

writeEmptyElement(prefix, localName, namespaceUri)
Writes an empty element tag to the output stream.

writeEndDocument()
Closes any start tags and writes corresponding end tags to the output stream.

writeEndElement()
Writes an end tag to the output stream, relying on the internal state of the writer to determine the prefix and local name.

writeNamespace(prefix, namespaceUri)
Writes the specified namespace to the output stream.


Apex Reference Guide XmlStreamWriter Class

writeProcessingInstruction(target, data)
Writes the specified processing instruction.

writeStartDocument(encoding, version)
Writes the XML Declaration using the specified XML encoding and version.

writeStartElement(prefix, localName, namespaceUri)
Writes the start tag specified by _`localName`_ to the output stream.

##### close()

Closes this instance of an XmlStreamWriter and free any resources associated with it.

Signature

```
   public Void close()

```

Return Value

Type: Void

##### getXmlString()

Returns the XML written by the XmlStreamWriter instance.

Signature

```
   public String getXmlString()

```

Return Value

Type: String

##### setDefaultNamespace(uri)

Binds the specified URI to the default namespace. This URI is bound in the scope of the current START_ELEMENT – END_ELEMENT pair.

Signature

```
   public Void setDefaultNamespace(String uri)

```

Parameters

```
   uri
```

Type: String

Return Value

Type: Void


Apex Reference Guide XmlStreamWriter Class

##### writeAttribute(prefix, namespaceUri, localName, value)

Writes an attribute to the output stream.

Signature

```
   public Void writeAttribute(String prefix, String namespaceUri, String localName, String

   value)

```

Parameters

```
   prefix
```

Type: String

```
   namespaceUri
```

Type: String

```
   localName
```

Type: String

Specifies the name of the attribute.

```
   value
```

Type: String

Return Value

Type: Void

##### writeCData(data)

Writes the specified CData to the output stream.

Signature

```
   public Void writeCData(String data)

```

Parameters

```
   data
```

Type: String

Return Value

Type: Void

##### writeCharacters(text)

Writes the specified text to the output stream.

Signature

```
   public Void writeCharacters(String text)

```


Apex Reference Guide XmlStreamWriter Class

Parameters

```
   text
```

Type: String

Return Value

Type: Void

##### writeComment(comment)

Writes the specified comment to the output stream.

Signature

```
   public Void writeComment(String comment)

```

Parameters

```
   comment
```

Type: String

Return Value

Type: Void

##### writeDefaultNamespace(namespaceUri)

Writes the specified namespace to the output stream.

Signature

```
   public Void writeDefaultNamespace(String namespaceUri)

```

Parameters

```
   namespaceUri
```

Type: String

Return Value

Type: Void

##### writeEmptyElement(prefix, localName, namespaceUri)

Writes an empty element tag to the output stream.

Signature

```
   public Void writeEmptyElement(String prefix, String localName, String namespaceUri)

```


Apex Reference Guide XmlStreamWriter Class

Parameters

```
   prefix
```

Type: String

```
   localName
```

Type: String

Specifies the name of the tag to be written.

```
   namespaceUri
```

Type: String

Return Value

Type: Void

##### writeEndDocument()

Closes any start tags and writes corresponding end tags to the output stream.

Signature

```
   public Void writeEndDocument()

```

Return Value

Type: Void

##### writeEndElement()

Writes an end tag to the output stream, relying on the internal state of the writer to determine the prefix and local name.

Signature

```
   public Void writeEndElement()

```

Return Value

Type: Void

##### writeNamespace(prefix, namespaceUri)

Writes the specified namespace to the output stream.

Signature

```
   public Void writeNamespace(String prefix, String namespaceUri)

```

Parameters

```
   prefix
```

Type: String


Apex Reference Guide XmlStreamWriter Class

```
   namespaceUri
```

Type: String

Return Value

Type: Void

##### writeProcessingInstruction(target, data)

Writes the specified processing instruction.

Signature

```
   public Void writeProcessingInstruction(String target, String data)

```

Parameters

```
   target
```

Type: String

```
   data
```

Type: String

Return Value

Type: Void

##### writeStartDocument(encoding, version)

Writes the XML Declaration using the specified XML encoding and version.

Signature

```
   public Void writeStartDocument(String encoding, String version)

```

Parameters

```
   encoding
```

Type: String

```
   version
```

Type: String

Return Value

Type: Void

##### writeStartElement(prefix, localName, namespaceUri)

Writes the start tag specified by _`localName`_ to the output stream.


## Apex Reference Guide TerritoryMgmt Namespace

Signature

```
   public Void writeStartElement(String prefix, String localName, String namespaceUri)

```

Parameters

```
   prefix
```

Type: String

```
   localName
```

Type: String

```
   namespaceUri
```

Type: String

Return Value

Type: Void

## TerritoryMgmt Namespace The TerritoryMgmt namespace provides an interface used for territory management. The following is the interface in the TerritoryMgmt namespace.

IN THIS SECTION:

### OpportunityTerritory2AssignmentFilter Global Interface

Apex interface that allows an implementing class to assign a single territory to an opportunity.

### OpportunityTerritory2AssignmentFilter Global Interface

Apex interface that allows an implementing class to assign a single territory to an opportunity.

Namespace

## TerritoryMgmt

Usage

Method called by Opportunity Territory Assignment job to assign territory to opportunity. Input is a list of (up to 1000) opportunityIds
that have IsExcludedFromTerritory2Filter=false. Returns a map of OpportunityId to Territory2Id, which is used to update the Territory2Id
field on the Opportunity object.

IN THIS SECTION:

OpportunityTerritory2AssignmentFilter Methods

OpportunityTerritory2AssignmentFilter Example Implementation


Apex Reference Guide OpportunityTerritory2AssignmentFilter Global Interface

#### OpportunityTerritory2AssignmentFilter Methods The following are methods for OpportunityTerritory2AssignmentFilter .

IN THIS SECTION:

##### getOpportunityTerritory2Assignments(opportunityIds)

Returns the mapping of opportunities to territory IDs. When Salesforce invokes this method, it supplies the list of opportunity IDs,
except for opportunities that have been excluded from territory assignment (IsExcludedFromTerritory2Filter=false).

##### getOpportunityTerritory2Assignments(opportunityIds)

Returns the mapping of opportunities to territory IDs. When Salesforce invokes this method, it supplies the list of opportunity IDs, except
for opportunities that have been excluded from territory assignment (IsExcludedFromTerritory2Filter=false).

Signature

```
   public Map<Id,Id> getOpportunityTerritory2Assignments(List<Id> opportunityIds)

```

Parameters

```
   opportunityIds
```

Type: List<Id>

Opportunity IDs.

Return Value

Type: Map<Id,Id>

A key value pair associating each Territory ID to an Opportunity ID.

#### OpportunityTerritory2AssignmentFilter Example Implementation

This is an example implementation of the `TerritoryMgmt.OpportunityTerritory2AssignmentFilter` interface.

```
   /*** Apex version of the default logic.

   * If opportunity's assigned account is assigned to

   * Case 1: 0 territories in active model

   * then set territory2Id = null

   * Case 2: 1 territory in active model

   * then set territory2Id = account's territory2Id

   * Case 3: 2 or more territories in active model

   * then set territory2Id = account's territory2Id that is of highest priority.

   * But if multiple territories have same highest priority, then set territory2Id

    = null

   */

   global class OppTerrAssignDefaultLogicFilter implements

   TerritoryMgmt.OpportunityTerritory2AssignmentFilter {

      /**

      * No-arg constructor.

      */

      global OppTerrAssignDefaultLogicFilter() {}

```


Apex Reference Guide OpportunityTerritory2AssignmentFilter Global Interface

```
      /**

       * Get mapping of opportunity to territory2Id. The incoming list of opportunityIds

   contains only those with IsExcludedFromTerritory2Filter=false.

       * If territory2Id = null in result map, clear the opportunity.territory2Id if set.

       * If opportunity is not present in result map, its territory2Id remains intact.

       */

      global Map<Id,Id> getOpportunityTerritory2Assignments(List<Id> opportunityIds) {

        Map<Id, Id> OppIdTerritoryIdResult = new Map<Id, Id>();

        // Get the active territory model Id

        Id activeModelId = getActiveModelId();

        if(activeModelId != null){

           List<Opportunity> opportunities =

            [Select Id, AccountId, Territory2Id from Opportunity where Id IN

   :opportunityIds];

           Set<Id> accountIds = new Set<Id>();

           // Create set of parent accountIds

           for(Opportunity opp:opportunities){

             if(opp.AccountId != null){

               accountIds.add(opp.AccountId);

               }

             }

             Map<Id,Territory2Priority> accountMaxPriorityTerritory =

   getAccountMaxPriorityTerritory(activeModelId, accountIds);

           // For each opportunity, assign the highest priority territory if there is no

    conflict, else assign null.

           for(Opportunity opp: opportunities){

            Territory2Priority tp = accountMaxPriorityTerritory.get(opp.AccountId);

            // Assign highest priority territory if there is only 1.

           if((tp != null) && (tp.moreTerritoriesAtPriority == false) && (tp.territory2Id

    != opp.Territory2Id)){

               OppIdTerritoryIdResult.put(opp.Id, tp.territory2Id);

            }else{

               OppIdTerritoryIdResult.put(opp.Id, null);

            }

           }

        }

        return OppIdTerritoryIdResult;

      }

      /**

       * Query assigned territoryIds in active model for given accountIds.

       * Create a map of accountId to max priority territory.

       */

      private Map<Id,Territory2Priority> getAccountMaxPriorityTerritory(Id activeModelId,

   Set<Id> accountIds){

        Map<Id,Territory2Priority> accountMaxPriorityTerritory = new

   Map<Id,Territory2Priority>();

        for(ObjectTerritory2Association ota:[Select ObjectId, Territory2Id,

   Territory2.Territory2Type.Priority from ObjectTerritory2Association where objectId IN

```


Apex Reference Guide OpportunityTerritory2AssignmentFilter Global Interface

```
   :accountIds and Territory2.Territory2ModelId = :activeModelId]){

           Territory2Priority tp = accountMaxPriorityTerritory.get(ota.ObjectId);

           if((tp == null) || (ota.Territory2.Territory2Type.Priority > tp.priority)){

             // If this is the first territory examined for account or it has greater

   priority than current highest priority territory, then set this as new highest priority

   territory.

             tp = new

   Territory2Priority(ota.Territory2Id,ota.Territory2.Territory2Type.priority,false);

           }else if(ota.Territory2.Territory2Type.priority == tp.priority){

             // The priority of current highest territory is same as this, so set

   moreTerritoriesAtPriority to indicate multiple highest priority territories seen so far.

             tp.moreTerritoriesAtPriority = true;

           }

           accountMaxPriorityTerritory.put(ota.ObjectId, tp);

        }

        return accountMaxPriorityTerritory;

      }

      /**

      * Get the Id of the Active Territory Model.

      * If none exists, return null.

      */

      private Id getActiveModelId() {

        List<Territory2Model> models = [Select Id from Territory2Model where State =

   'Active'];

        Id activeModelId = null;

        if(models.size() == 1){

           activeModelId = models.get(0).Id;

        }

        return activeModelId;

      }

      /**

      * Helper class to help capture territory2Id, its priority, and whether there are more

    territories with same priority assigned to the account.

      */

      private class Territory2Priority {

        public Id territory2Id { get; set; }

        public Integer priority { get; set; }

        public Boolean moreTerritoriesAtPriority { get; set; }

        Territory2Priority(Id territory2Id, Integer priority, Boolean

   moreTerritoriesAtPriority){

           this.territory2Id = territory2Id;

           this.priority = priority;

           this.moreTerritoriesAtPriority = moreTerritoriesAtPriority;

        }

      }

   }

```


## Apex Reference Guide TxnSecurity Namespace TxnSecurity Namespace The TxnSecurity namespace provides an interface used for transaction security. The following is the interface and its supporting class in the TxnSecurity namespace.

IN THIS SECTION:

### Event Class

Contains event information that the `evaluate` method uses to evaluate a transaction security policy.

EventCondition Interface
Allows an implementing class to specify whether to take action when certain events occur based on a transaction security policy.
This interface is only used for Apex policies created in Real-Time Event Monitoring.

AsyncCondition Interface
Allows an implementing class to make asynchronous Apex calls. This interface is used only for transaction security Apex policies
created in Real-Time Event Monitoring.

PolicyCondition Interface
Apex interface that allows an implementing class to specify actions to take when certain events occur based on a transaction security
policy.

### Event Class

Contains event information that the `evaluate` method uses to evaluate a transaction security policy.

Namespace

## TxnSecurity

Usage

The Event class contains the information needed to determine if the event triggers a Transaction Security policy. Not all class attributes
are used for every type of event.

Tip: The `EventClass` interface applies only to Legacy Transaction Security, which is a retired feature as of Summer '20. Use
the `EventCondition` interface instead of the `EventClass` interface.

IN THIS SECTION:

#### Event Constructors

Event Properties

#### Event Constructors

### The following is the constructor for Event .


Apex Reference Guide Event Class

IN THIS SECTION:

##### Event()

Creates an instance of the `TxnSecurity.Event` class.

##### Event()

Creates an instance of the `TxnSecurity.Event` class.

Signature

```
   public Event()

#### Event Properties

##### The following are properties for Event .

```

IN THIS SECTION:

##### action

Specifies the action being taken on the resource for an Entity event. For example, a Login IP resource for an Entity event could have
##### an action of create . The action attribute is not used by any other event type.

data
Contains data used by actions. For example, `data` for a login event includes the login history ID. Returns a map whose keys are
the type of event data, like `SourceIp` .

entityId
The ID of any entity associated with the event. For example, the `entityId` of a DataExport event for an Account object contains
the Account ID.

entityName
The name of the object the event acts on.

organizationId
The ID of the Salesforce org where the event occurred.

resourceType
The type of resource for the event. For example, an AccessResource event could have a Connected Application as a resource type.
Not all event types have resources.

timeStamp
The time the event occurred.

userId
Identifies the user that caused the event.

##### action

Specifies the action being taken on the resource for an Entity event. For example, a Login IP resource for an Entity event could have an
##### action of create . The action attribute is not used by any other event type.


Apex Reference Guide Event Class

Signature

```
   public String action {get; set;}

```

Property Value

Type: String

##### data Contains data used by actions. For example, data for a login event includes the login history ID. Returns a map whose keys are the

type of event data, like `SourceIp` .

Signature

```
   public Map<String,String> data {get; set;}

```

Property Value

Type: Map<String, String>

The following table lists all the available data types. Not all types appear with all event types. The data type values are always string
representations. For example, the `isApi` value is a string in the map, but is actually a Boolean value. Convert the value from a string
to its true type this way: `Boolean.valueOf(event.data.get('isApi'));`


Apex Reference Guide Event Class

##### entityId The ID of any entity associated with the event. For example, the entityId of a DataExport event for an Account object contains the

Account ID.

Signature

```
   public String entityId {get; set;}

```

Property Value

Type: String

##### entityName

The name of the object the event acts on.

Signature

```
   public String entityName {get; set;}

```

Property Value

Type: String

##### organizationId

The ID of the Salesforce org where the event occurred.

Signature

```
   public String organizationId {get; set;}

```

Property Value

Type: String


### Apex Reference Guide EventCondition Interface

##### resourceType

The type of resource for the event. For example, an AccessResource event could have a Connected Application as a resource type. Not
all event types have resources.

Signature

```
   public String resourceType {get; set;}

```

Property Value

Type: String

##### timeStamp

The time the event occurred.

Signature

```
   public Datetime timeStamp {get; set;}

```

Property Value

Type: Datetime

##### userId

Identifies the user that caused the event.

Signature

```
   public String userId {get; set;}

```

Property Value

Type: String

### EventCondition Interface

Allows an implementing class to specify whether to take action when certain events occur based on a transaction security policy. This
interface is only used for Apex policies created in Real-Time Event Monitoring.

Usage

The `evaluate` method is called upon the occurrence of a real-time event monitored by a transaction security policy. A typical
implementation first selects the fields of interest from the event. Then the fields are tested to see if they meet the conditions being
monitored. If the conditions are met, the method returns `true` .

For example, imagine a transaction security policy that triggers when a user queries more than 1,000 lead records. For each API event,
the `evaluate` method checks whether the `RowsProcessed` value is greater than 1,000 and the `QueriedEntities` value
contains “Lead”. If so, `true` is returned.


Apex Reference Guide EventCondition Interface

We recommend having test classes for the policy condition interface to ensure it works correctly. Testing is required regardless of whether
the policy is moved from a sandbox to production, with a change set, or some other way. For example, test your policies in your
development environment before moving the policies to production.

[For more information about testing Apex transaction security policies, read Transaction Security Apex Testing.](https://help.salesforce.com/s/articleView?id=xcloud.enhanced_transaction_security_apex_testing.htm&type=5&language=en_US)

IN THIS SECTION:

#### EventCondition Methods

The EventCondition interface has one method, evaluate(event).

EventCondition Example Implementation
Use EventCondition to create a custom condition for Shield Platform Encryption.

#### EventCondition Methods

The EventCondition interface has one method, evaluate(event).

#### The following are methods for EventCondition .

IN THIS SECTION:

##### evaluate(event)

Evaluates an event against a transaction security policy created in Real-Time Event Monitoring. If the event triggers the policy, the
method returns `true` .

##### evaluate(event)

Evaluates an event against a transaction security policy created in Real-Time Event Monitoring. If the event triggers the policy, the method
returns `true` .

Signature

```
   public Boolean evaluate(SObject event)

```

Parameters

```
   var1
```

Type: SObject

The event to check against the transaction security policy.

Return Value

Type: Boolean

Returns `true` when the policy is triggered. For example, suppose that the policy is to limit users to a single login session. If a user tries
to log in a second time, the policy blocks the attempted login, and updates the Status, PolicyId, and PolicyOutcome fields of that
##### LoginEvent. The policy also sends an email notification to the Salesforce admin. The evaluate method only checks the login event,

and returns `true` if it’s the user’s second login attempt.

##### The system performs the action and notification, not the evaluate method.


### Apex Reference Guide AsyncCondition Interface

#### EventCondition Example Implementation

Use EventCondition to create a custom condition for Shield Platform Encryption.

This example shows an implementation of the `TxnSecurity.EventCondition` interface. The transaction security policy triggers
when the user queries an Account object.

```
   public boolean evaluate(ApiEvent event) {

       switch on event {

         when ApiEvent apiEvent {

           return handleApiEvent(apiEvent);

         }

         when null {

         // Trigger action if event is null

           return true;

         }

         when else {

         // Trigger action for unhandled events

           return true;

         }

       }

     }

     private boolean handleApiEvent(ApiEvent apiEvent){

       if(apiEvent.QueriedEntities.contains('Account')){

         return true;

       }

       return false;

     }

   }

```

[For more examples, see Enhanced Apex Transaction Security Implementation Examples.](https://help.salesforce.com/articleView?id=enhanced_transaction_security_policy_apex_examples.htm&language=en_US)

### AsyncCondition Interface

Allows an implementing class to make asynchronous Apex calls. This interface is used only for transaction security Apex policies created
in Real-Time Event Monitoring.

Namespace

TxnSecurity

Usage

[If you make an Asynchronous Apex call in the class that implements your transaction security policy condition, the class must implement](https://trailhead.salesforce.com/en/content/learn/modules/asynchronous_apex)
the `TxnSecurity.AsyncCondition` interface in addition to `TxnSecurity.EventCondition` . Use Asynchronous Apex
instead of Apex callouts and DML statements, neither of which is allowed in transaction security Apex policies.

Apex offers multiple ways to run your Apex code asynchronously and all are supported in the `TxnSecurity.AsyncCondition`
interface.

This interface has no methods.


### Apex Reference Guide PolicyCondition Interface

IN THIS SECTION:

#### AsyncCondition Example Implementation

SEE ALSO:

_[Apex Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_async_overview.htm)_ Asynchronous Apex

#### AsyncCondition Example Implementation

Here’s an example implementation of the `TxnSecurity.AsyncCondition` interface. The transaction security policy triggers
when a user logs in. In the example, ExternalValidation__c is a custom object that contains information from an external validation
system. The result of the SOQL query on ExternalValidation__c determines whether to block the user from logging in. The policy then
queues the `CalloutToExternalValidator` class for asynchronous execution. When it executes, the
`CalloutToExternalValidator` class makes an external call to the validation system to update it with information about this
log in event. Because `CalloutToExternalValidator` is triggered by Asynchronous Apex, you must implement the
`TxnSecurity.AsyncCondition` interface in the `ExternallyValidatedLoginCondition` Apex class along with
the usual `TxnSecurity.EventCondition` interface.

```
   global class ExternallyValidatedLoginCondition implements TxnSecurity.EventCondition,

   TxnSecurity.AsyncCondition {

      public boolean evaluate(SObject event) {

        LoginEvent loginEvent = (LoginEvent) event;

        Boolean userBlocked = [select blocked from ExternalValidation__c where loginId =

   loginEvent.UserId][0].Blocked;

        System.enqueueJob(new CalloutToExternalValidator(loginEvent.SourceIp,

   loginEvent.LoginUrl));

        return userBlocked;

      }

   }

   public class CalloutToExternalValidator implements Queueable {

      private String sourceIp;

      private String loginUrl;

      public CalloutToExternalValidator(String sourceIp, String loginUrl) {

        this.sourceIp = sourceIp;

        this.loginUrl = loginUrl;

      }

      public void execute(QueueableContext context) {

        // callout to external validation service

        // pass sourceIp, loginUrl

        // update ExternalValidation__c

      }

   }

### PolicyCondition Interface

```

Apex interface that allows an implementing class to specify actions to take when certain events occur based on a transaction security
policy.


Apex Reference Guide PolicyCondition Interface

Namespace

TxnSecurity

Usage

#### Tip: The PolicyCondition interface applies only to Legacy Transaction Security, which is a retired feature as of Summer '20. Use the EventCondition interface instead of the PolicyCondition interface.

##### The evaluate method is called upon the occurrence of an event monitored by a transaction security policy. A typical implementation

first selects the item of interest from the event. Then the item is tested to see if it meets the condition being monitored. If the condition
is met, the method returns `true` .

For example, imagine a transaction security policy that checks for the same user logging in more than once. For each login event, the
method would check if the user logging in already has a login session in progress, and if so, `true` is returned.

We recommend having test classes for the policy condition interface to ensure it works correctly. Testing is required regardless of whether
the policy is moved from a sandbox to production, with a change set, or some other way. For example, test your policies in your
development environment before moving the policies to production.

Don’t include DML statements in your custom policies because they can cause errors. When you send a custom email via Apex during
transaction policy evaluation, you get an error, even if the record isn’t explicitly related to another record. For more information, see
[Apex DML Operations in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_dml_section.htm) _Apex Reference Guide_ .

IN THIS SECTION:

#### PolicyCondition Methods PolicyCondition Methods The following is the method for PolicyCondition .

IN THIS SECTION:

##### evaluate(event)

Evaluates an event against a transaction security policy. If the event triggers the policy, `true` is returned.

##### evaluate(event)

Evaluates an event against a transaction security policy. If the event triggers the policy, `true` is returned.

Signature

```
   public Boolean evaluate(TxnSecurity.Event event)

```

Parameters

```
   event
```

Type: TxnSecurity.Event

The event to check against the transaction security policy.


## Apex Reference Guide UserProvisioning Namespace

Return Value

Type: Boolean

When the policy is triggered, `True` is returned. For example, let’s suppose the policy is to limit users to a single login session. If anyone
tries to log in a second time, the policy’s action requires that they end their current session. The policy also sends an email notification
to the Salesforce admin. The `evaluate()` method only checks the login event, and returns `True` if it’s the user’s second login. The
Transaction Security system performs the action and notification, and not the `evaluate()` method.

## UserProvisioning Namespace The UserProvisioning namespace provides methods for monitoring outbound user provisioning requests. The following is the class in the UserProvisioning namespace.

IN THIS SECTION:

### ConnectorTestUtil Class

Enables developers to write Apex test classes for connectors used by the connected app provisioning solution. This class simulates
provisioning for the associated app.

UserProvisioningLog Class
Provides methods for writing messages to monitor outbound user provisioning requests.

UserProvisioningPlugin Class
The `UserProvisioningPlugin` base class implements `Process.Plugin` for programmatic customization of the user
provisioning process for connected apps.

### ConnectorTestUtil Class

Enables developers to write Apex test classes for connectors used by the connected app provisioning solution. This class simulates
provisioning for the associated app.

Namespace

## UserProvisioning

Usage

Use this class for connector-based test accelerators. You can invoke it only from within an Apex test.

Example

This example creates an instance of a connected app, gets a value, and checks whether the value is correct. The test is simply a row
inserted in the database table.

```
        @isTest

        private class SCIMCreateUserPluginTest {

        public static void callPlugin(Boolean validInputParams) {

```


Apex Reference Guide ConnectorTestUtil Class

```
        //Create an instance of a connected app

        ConnectedApplication capp

   =UserProvisioning.ConnectorTestUtil.createConnectedApp('TestApp');

        Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];

        //Create a user

        User user = new User(username='testuser1@scimuserprov.test', Firstname= 'Test',

   Lastname='User1', email='testuser1@testemail.com',

        FederationIdentifier='testuser1@testemail.com', profileId= p.Id,

   communityNickName='tuser1', alias='tuser', TimeZoneSidKey='GMT',

        LocaleSidKey='en_US', EmailEncodingKey='ISO-8859-1', LanguageLocaleKey='en_US');

        //insert user into a row in the database table

        insert user;

        //Create a UPR

        UserProvisioningRequest upr = new UserProvisioningRequest(appname = capp.name,

   connectedAppId=capp.id, operation='Create',

        state='New', approvalStatus='NotRequired',salesforceUserId=user.id);

        //Insert the UPR to test the flow end to end

        insert upr;

        }}

```

IN THIS SECTION:

#### ConnectorTestUtil Method

SEE ALSO:

_Salesforce Help_ [: User Provisioning for Connected Apps](https://help.salesforce.com/articleView?id=connected_app_user_provisioning.htm&language=en_US)

#### ConnectorTestUtil Method The ConnectorTestUtil class has 1 method.

IN THIS SECTION:

##### createConnectedApp(connectedAppName)

Creates an instance of a connected app to simulate provisioning.

##### createConnectedApp(connectedAppName)

Creates an instance of a connected app to simulate provisioning.

Signature

```
   public static ConnectedApplication createConnectedApp(String connectedAppName)

```

Parameters

```
   connectedAppName
```

Type: String


### Apex Reference Guide UserProvisioningLog Class

Name of the connected app to test for provisioning.

Return Value

Type: ConnectedApplication

The instance of the connected app to test for provisioning.

### UserProvisioningLog Class

Provides methods for writing messages to monitor outbound user provisioning requests.

Namespace

### UserProvisioning

Example

This example writes the user account information sent to a third-party system for a provisioning request to the UserProvisioningLog
object.

```
   String inputParamsStr = 'Input parameters: uprId=' + uprId + ',

   endpointURL=' + endpointURL + ', adminUsername=' + adminUsername + ',

   email=' + email + ', username=' + username + ', defaultPassword=' + defaultPassword + ',

   defaultRoles =' + defaultRoles;

   UserProvisioning.UserProvisioningLog.log(uprId, inputParamsStr);

```

IN THIS SECTION:

#### UserProvisioningLog Methods UserProvisioningLog Methods

### The following are methods for UserProvisioningLog . All methods are static.

IN THIS SECTION:

##### log(userProvisioningRequestId, details)

Writes a specific message, such as an error message, to monitor the progress of a user provisioning request.

log(userProvisioningRequestId, status, details)
Writes a specific status and message, such a status and detailed error message, to monitor the progress of a user provisioning request.

log(userProvisioningRequestId, externalUserId, externalUserName, userId, details)
Writes a specific message, such as an error message, to monitor the progress of a user provisioning request associated with a specific
user.

##### log(userProvisioningRequestId, details)

Writes a specific message, such as an error message, to monitor the progress of a user provisioning request.


Apex Reference Guide UserProvisioningLog Class

Signature

```
   public void log(String userProvisioningRequestId, String details)

```

Parameters

```
   userProvisioningRequestId
```

Type: String

A unique identifier for the user provisioning request.

```
   details
```

Type: String

The text for the message.

Return Value

Type: void

##### log(userProvisioningRequestId, status, details)

Writes a specific status and message, such a status and detailed error message, to monitor the progress of a user provisioning request.

Signature

```
   public void log(String userProvisioningRequestId, String status, String details)

```

Parameters

```
   userProvisioningRequestId
```

Type: String

A unique identifier for the user provisioning request.

```
   status
```

Type: String

A description of the current state. For example, while invoking a third-party API, the status could be `invoke` .

```
   details
```

Type: String

The text for the message.

Return Value

Type: void

##### log(userProvisioningRequestId, externalUserId, externalUserName, userId, details)

Writes a specific message, such as an error message, to monitor the progress of a user provisioning request associated with a specific
user.


### Apex Reference Guide UserProvisioningPlugin Class

Signature

```
   public void log(String userProvisioningRequestId, String externalUserId, String

   externalUserName, String userId, String details)

```

Parameters

```
   userProvisioningRequestId
```

Type: String

A unique identifier for the user provisioning request.

```
   externalUserId
```

Type: String

The unique identifier for the user in the target system.

```
   externalUserName
```

Type: String

The username for the user in the target system.

```
   userId
```

Type: String

Salesforce ID of the user making the request.

```
   details
```

Type: String

The text for the message.

Return Value

Type: void

### UserProvisioningPlugin Class The UserProvisioningPlugin base class implements Process.Plugin for programmatic customization of the user

provisioning process for connected apps.

Namespace

### UserProvisioning

Usage

Extending this class gives you a plug-in that can be used Flow Builder as a legacy Apex action, with the following input and output
parameters.

**Input Parameter Name** **Description**

`userProvisioningRequestId` The unique ID of the request for the plug-in to process.

`userId` The ID of the associated user for the request.


Apex Reference Guide UserProvisioningPlugin Class

**Input Parameter Name** **Description**

```
NamedCredDevName

reconFilter

```

The unique API name for the named credential to use for a request.
The named credential identifies the third-party system and the
third-party authentication settings.

When the named credential is set in the User Provisioning Wizard,
Salesforce stores the value in the

```
UserProvisioningConfig.NamedCredentialId
```

field.

When collecting and analyzing users on a third-party system, the
plug-in uses this filter to limit the scope of the collection.

When the filter is set in the User Provisioning Wizard, Salesforce
stores the value in the
`UserProvisioningConfig.ReconFilter` field.

`reconOffset` When collecting and analyzing users on a third-party system, the
plug-in uses this value as the starting point for the collection.

**Output Parameter Name** **Description**

```
Status

```

The vendor-specific status of the provisioning operation on the
third-party system.

`Details` The vendor-specific message related to the status of the
provisioning operation on the third-party system.

`ExternalUserId` The vendor-specific ID for the associated user on the third-party
system.

`ExternalUsername` The vendor-specific username for the associated user on the
third-party system.

`ExternalEmail` The email address assigned to the user on the third-party system.

`ExternalFirstName` The first name assigned to the user on the third-party system.

`ExternalLastName` The last name assigned to the user on the third-party system.

```
reconState

```

The state of the collecting and analyzing process on the third-party
system. When the value is `complete`, the process is finished and
a subsequent call to the plug-in is no longer needed, nor made.

`nextReconOffset` When collecting and analyzing users on a third-party system, the
process may encounter a transaction limit and have to stop before

finishing. The value specified here initiates a call to the plug-in with
a new quota limit.

If you want to add more custom parameters, use the `buildDescribeCall()` method.


Apex Reference Guide UserProvisioningPlugin Class

Example

The following example uses the `buildDescribeCall()` method to add a new input parameter and a new output parameter.
The example also demonstrates how to bypass the limit of the 10,000 records processed in DML statements in an Apex transaction.

```
   global class SampleConnector extends UserProvisioning.UserProvisioningPlugin {

      // Example of adding more input and output parameters to those defined in the base

   class

      global override Process.PluginDescribeResult buildDescribeCall() {

        Process.PluginDescribeResult describeResult = new Process.PluginDescribeResult();

        describeResult.inputParameters = new

           List<Process.PluginDescribeResult.InputParameter>{

            new Process.PluginDescribeResult.InputParameter('testInputParam',

                 Process.PluginDescribeResult.ParameterType.STRING, false)

           };

        describeResult.outputParameters = new

           List<Process.PluginDescribeResult.OutputParameter>{

            new Process.PluginDescribeResult.OutputParameter('testOutputParam',

                 Process.PluginDescribeResult.ParameterType.STRING)

           };

        return describeResult;

      }

      // Example Plugin that demonstrates how to leverage the

   reconOffset/nextReconOffset/reconState

      // parameters to create more than 10,000 users. (i.e. go beyond the 10,000 DML limit

   per transaction)

      global override Process.PluginResult invoke(Process.PluginRequest request) {

        Map<String,String> result = new Map<String,String>();

        String uprId = (String) request.inputParameters.get('userProvisioningRequestId');

        UserProvisioning.UserProvisioningLog.log(uprId, 'Inserting Log from test Apex

   connector');

        UserProvisioningRequest upr = [SELECT id, operation, connectedAppId, state

               FROM userprovisioningrequest WHERE id = :uprId];

        if (upr.operation.equals('Reconcile')) {

           String reconOffsetStr = (String) request.inputParameters.get('reconOffset');

           Integer reconOffset = 0;

           if (reconOffsetStr != null) {

             reconOffset = Integer.valueOf(reconOffsetStr);

           }

           if (reconOffset > 44999) {

             result.put('reconState', 'Completed');

           }

           Integer i = 0;

           List<UserProvAccountStaging> upasList = new List<UserProvAccountStaging>();

           for (i = 0; i < 5000; i++) {

             UserProvAccountStaging upas = new UserProvAccountStaging();

```


Apex Reference Guide UserProvisioningPlugin Class

```
             upas.Name = i + reconOffset + '';

             upas.ExternalFirstName = upas.Name;

             upas.ExternalEmail = 'externaluser@externalsystem.com';

             upas.LinkState = 'Orphaned';

             upas.Status = 'Active';

             upas.connectedAppId = upr.connectedAppId;

             upasList.add(upas);

           }

           insert upasList;

           result.put('nextReconOffset', reconOffset + 5000 + '');

        }

        return new Process.PluginResult(result);

      }

   }

```

IN THIS SECTION:

#### UserProvisioningPlugin Methods UserProvisioningPlugin Methods The following are methods for UserProvisioningPlugin .

IN THIS SECTION:

##### buildDescribeCall()

Use this method to add more input and output parameters to those defined in the base class.

describe()
Returns a `Process.PluginDescribeResult` object that describes this method call.

getPluginClassName()
Returns the name of the class implementing the plugin.

invoke(request)
Primary method that the system invokes when the class that implements the interface is instantiated.

##### buildDescribeCall()

Use this method to add more input and output parameters to those defined in the base class.

Signature

```
   public Process.PluginDescribeResult buildDescribeCall()

```

Return Value

Type: Process.PluginDescribeResult


## Apex Reference Guide VisualEditor Namespace

##### describe()

Returns a `Process.PluginDescribeResult` object that describes this method call.

Signature

```
   public Process.PluginDescribeResult describe()

```

Return Value

Type: Process.PluginDescribeResult

##### getPluginClassName()

Returns the name of the class implementing the plugin.

Signature

```
   public String getPluginClassName()

```

Return Value

Type: String

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

Type: Process.PluginDescribeResult

## VisualEditor Namespace The VisualEditor namespace provides classes and methods for interacting with the Lightning App Builder. The classes and

methods in this namespace operate on Lightning components, which include Lightning web components and Aura components.

As of Spring ’19 (API version 45.0), you can build Lightning components using two programming models: the Lightning Web Components
model, and the original Aura Components model. Lightning web components are custom HTML elements built using HTML and modern
JavaScript. Lightning web components and Aura components can coexist and interoperate on a page.


### Apex Reference Guide DataRow Class

Configure Lightning web components and Aura components to work in Lightning App Builder and Experience Builder. Admins and end
users don’t know which programming model was used to develop the components. To them, they’re simply Lightning components.

The following are the classes in the `VisualEditor` namespace.

IN THIS SECTION:

### DataRow Class

Contains information about one item in a picklist used in a Lightning component on a Lightning page.

DesignTimePageContext Class
A class that provides context information about a Lightning page. It can be used to help define the values of a picklist in a Lightning
component on a Lightning page based on the page’s type and the object with which it’s associated.

DynamicPickList Class
An abstract class, used to display the values of a picklist in a Lightning component on a Lightning page.

DynamicPickListRows Class
Contains a list of picklist items in a Lightning component on a Lightning page.

### DataRow Class

Contains information about one item in a picklist used in a Lightning component on a Lightning page.

Namespace

VisualEditor

IN THIS SECTION:

#### DataRow Constructors

DataRow Methods

#### DataRow Constructors

### The following are constructors for DataRow .

IN THIS SECTION:

##### DataRow(label, value, selected)

Creates an instance of the `VisualEditor.DataRow` class using the specified label, value, and selected option.

DataRow(label, value)
Creates an instance of the `VisualEditor.DataRow` class using the specified label and value.

##### DataRow(label, value, selected)

Creates an instance of the `VisualEditor.DataRow` class using the specified label, value, and selected option.

Signature

```
   public DataRow(String label, Object value, Boolean selected)

```


Apex Reference Guide DataRow Class

Parameters

```
   label
```

Type: String

User-facing label for the picklist item.

```
   value
```

Type: Object

The value of the picklist item.

```
   selected
```

Type: Boolean

Specifies whether the picklist item is selected ( `true` ) or not ( `false` ).

##### DataRow(label, value)

Creates an instance of the `VisualEditor.DataRow` class using the specified label and value.

Signature

```
   public DataRow(String label, Object value)

```

Parameters

```
   label
```

Type: String

User-facing label for the picklist item.

```
   value
```

Type: Object

The value of the picklist item.

#### DataRow Methods

##### The following are methods for DataRow .

IN THIS SECTION:

clone()
Makes a duplicate copy of the `VisualEditor.DataRow` object.

compareTo(o)
Compares the current `VisualEditor.DataRow` object to the specified one. Returns an integer value that is the result of the
comparison.

getLabel()
Returns the user-facing label of the picklist item.

getValue()
Returns the value of the picklist item.

isSelected()
Returns the state of the picklist item, indicating whether it’s selected or not.


Apex Reference Guide DataRow Class

##### clone()

Makes a duplicate copy of the `VisualEditor.DataRow` object.

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### compareTo(o)

Compares the current `VisualEditor.DataRow` object to the specified one. Returns an integer value that is the result of the
comparison.

Signature

```
   public Integer compareTo(VisualEditor.DataRow o)

```

Parameters

```
   o
```

Type: VisualEditor.DataRow

A single item in a picklist.

Return Value

Type: Integer

Returns one of the following values:

**•** Zero if the current package version is equal to the specified package version

**•** An integer value greater than zero if the current package version is greater than the specified package version

**•** An integer value less than zero if the current package version is less than the specified package version

##### getLabel()

Returns the user-facing label of the picklist item.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the value of the picklist item.


### Apex Reference Guide DesignTimePageContext Class

Signature

```
   public Object getValue()

```

Return Value

Type: Object

##### isSelected()

Returns the state of the picklist item, indicating whether it’s selected or not.

Signature

```
   public Boolean isSelected()

```

Return Value

Type: Boolean

### DesignTimePageContext Class

A class that provides context information about a Lightning page. It can be used to help define the values of a picklist in a Lightning
component on a Lightning page based on the page’s type and the object with which it’s associated.

Namespace

VisualEditor

Usage

To use this class, create a parameterized constructor in the custom Apex class that extends `VisualEditor.DynamicPickList` .

Example

Here’s an example of a custom Apex class extending the `VisualEditor.DynamicPickList` class. It includes
`VisualEditor.DesignTimePageContext` to define a picklist value that is available only if the page type is `HomePage` .

```
   global class MyCustomPickList extends VisualEditor.DynamicPickList{

      VisualEditor.DesignTimePageContext context;

      global MyCustomPickList(VisualEditor.DesignTimePageContext context) {

        this.context = context;

      }

      global override VisualEditor.DataRow getDefaultValue(){

        VisualEditor.DataRow defaultValue = new VisualEditor.DataRow('red', 'RED');

        return defaultValue;

      }

      global override VisualEditor.DynamicPickListRows getValues() {

        VisualEditor.DataRow value1 = new VisualEditor.DataRow('red', 'RED');

```


Apex Reference Guide DesignTimePageContext Class

```
        VisualEditor.DataRow value2 = new VisualEditor.DataRow('yellow', 'YELLOW');

       VisualEditor.DynamicPickListRows myValues = new VisualEditor.DynamicPickListRows();

        myValues.addRow(value1);

        myValues.addRow(value2);

        if (context.pageType == 'HomePage') {

           VisualEditor.DataRow value3 = new VisualEditor.DataRow('purple', 'PURPLE');

           myValues.addRow(value3);

        }

        return myValues;

      }

   }

```

IN THIS SECTION:

#### DesignTimePageContext Properties

DesignTimePageContext Methods

#### DesignTimePageContext Properties The following are properties for DesignTimePageContext .

IN THIS SECTION:

##### entityName The API name of the sObject that a Lightning page is associated with, such as Account, Contact, or Custom_object__c. entityName

is available only for object pages, and not all Lightning pages are associated with objects.

##### pageType

The type of Lightning page, such as `HomePage`, `AppPage`, or `RecordPage` .

##### **`entityName`** The API name of the sObject that a Lightning page is associated with, such as Account, Contact, or Custom_object__c. entityName

is available only for object pages, and not all Lightning pages are associated with objects.

Signature

```
   public String entityName {get; set;}

```

Property Value

Type: String

##### pageType

The type of Lightning page, such as `HomePage`, `AppPage`, or `RecordPage` .


### Apex Reference Guide DynamicPickList Class

Signature

```
   public String pageType {get; set;}

```

Property Value

Type: String

#### DesignTimePageContext Methods The following are methods for DesignTimePageContext .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `VisualEditor.DesignTimePageContext` object.

##### clone()

Makes a duplicate copy of the `VisualEditor.DesignTimePageContext` object.

Signature

```
   public Object clone()

```

Return Value

Type: Object

### DynamicPickList Class

An abstract class, used to display the values of a picklist in a Lightning component on a Lightning page.

Namespace

VisualEditor

Usage

To use this class as the datasource of a picklist in a Lightning component, it must be extended by a custom Apex class and then that
class must be called in the component’s design file.

Example

Here’s an example of a custom Apex class extending the `VisualEditor.DynamicPickList` class.

```
   global class MyCustomPickList extends VisualEditor.DynamicPickList{

      global override VisualEditor.DataRow getDefaultValue(){

        VisualEditor.DataRow defaultValue = new VisualEditor.DataRow('red', 'RED');

```


Apex Reference Guide DynamicPickList Class

```
        return defaultValue;

      }

      global override VisualEditor.DynamicPickListRows getValues() {

        VisualEditor.DataRow value1 = new VisualEditor.DataRow('red', 'RED');

        VisualEditor.DataRow value2 = new VisualEditor.DataRow('yellow', 'YELLOW');

       VisualEditor.DynamicPickListRows myValues = new VisualEditor.DynamicPickListRows();

        myValues.addRow(value1);

        myValues.addRow(value2);

        return myValues;

      }

   }

```

Here’s an example of how the custom Apex class gets called in a design file so that the picklist appears in the Lightning component.

```
   <design:component>

        <design:attribute name="property1" datasource="apex://MyCustomPickList"/>

   </design:component>

```

IN THIS SECTION:

#### DynamicPickList Methods DynamicPickList Methods The following are methods for DynamicPickList .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `VisualEditor.DynamicPicklist` object.

getDefaultValue()
Returns the picklist item that is set as the default value for the picklist.

getLabel(attributeValue)
Returns the user-facing label for a specified picklist value.

getValues()
Returns the list of picklist item values.

isValid(attributeValue)
Returns the valid state of the picklist item’s value. A picklist value is considered valid if it’s a part of any `VisualEditor.DataRow`
in the `VisualEditor.DynamicPickListRows` returned by `getValues()` .

##### clone()

Makes a duplicate copy of the `VisualEditor.DynamicPicklist` object.

Signature

```
   public Object clone()

```


Apex Reference Guide DynamicPickList Class

Return Value

Type: Object

##### getDefaultValue()

Returns the picklist item that is set as the default value for the picklist.

Signature

```
   public VisualEditor.DataRow getDefaultValue()

```

Return Value

Type: VisualEditor.DataRow

##### getLabel(attributeValue)

Returns the user-facing label for a specified picklist value.

Signature

```
   public String getLabel(Object attributeValue)

```

Parameters

```
   attributeValue
```

Type: Object

The value of the picklist item.

Return Value

Type: String

##### getValues()

Returns the list of picklist item values.

Signature

```
   public VisualEditor.DynamicPickListRows getValues()

```

Return Value

Type: VisualEditor.DynamicPickListRows

##### isValid(attributeValue)

Returns the valid state of the picklist item’s value. A picklist value is considered valid if it’s a part of any `VisualEditor.DataRow`
##### in the VisualEditor.DynamicPickListRows returned by getValues() .


### Apex Reference Guide DynamicPickListRows Class

Signature

```
   public Boolean isValid(Object attributeValue)

```

Parameters

```
   attributeValue
```

Type: Object

The value of the picklist item.

Return Value

Type: Boolean

### DynamicPickListRows Class

Contains a list of picklist items in a Lightning component on a Lightning page.

Namespace

VisualEditor

IN THIS SECTION:

#### DynamicPickListRows Constructors

DynamicPickListRows Methods

#### DynamicPickListRows Constructors

### The following are constructors for DynamicPickListRows .

IN THIS SECTION:

##### DynamicPickListRows(rows, containsAllRows)

Creates an instance of the `VisualEditor.DynamicPickListRows` class using the specified parameters.

DynamicPickListRows(rows)
Creates an instance of the `VisualEditor.DynamicPickListRows` class using the specified parameter.

DynamicPickListRows()
Creates an instance of the `VisualEditor.DynamicPickListRows` class. You can then add rows by using the class’s
`addRow` or `addAllRows` methods.

##### DynamicPickListRows(rows, containsAllRows)

Creates an instance of the `VisualEditor.DynamicPickListRows` class using the specified parameters.

Signature

```
   public DynamicPickListRows(List<VisualEditor.DataRow> rows, Boolean containsAllRows)

```


Apex Reference Guide DynamicPickListRows Class

Parameters

```
   rows
```

Type: List VisualEditor.DataRow

List of picklist items.

```
   containsAllRows
```

Type: Boolean

Indicates if all values of the picklist are included in a type-ahead search query (true) or only those values initially displayed when the
list is clicked on (false).

A picklist in a Lightning component can display only the first 200 values of a list. If _`containsAllRows`_ is set to false, when a
user does a type-ahead search to find values in the picklist, the search will only look at those first 200 values that were displayed,
not the complete set of picklist values.

##### DynamicPickListRows(rows)

Creates an instance of the `VisualEditor.DynamicPickListRows` class using the specified parameter.

Signature

```
   public DynamicPickListRows(List<VisualEditor.DataRow> rows)

```

Parameters

```
   rows
```

Type: List VisualEditor.DataRow

List of picklist rows.

##### DynamicPickListRows()

Creates an instance of the `VisualEditor.DynamicPickListRows` class. You can then add rows by using the class’s `addRow`
or `addAllRows` methods.

Signature

```
   public DynamicPickListRows()

#### DynamicPickListRows Methods

##### The following are methods for DynamicPickListRows .

```

IN THIS SECTION:

addAllRows(rows)
Adds a list of picklist items to a dynamic picklist rendered in a Lightning component on a Lightning page.

addRow(row)
Adds a single picklist item to a dynamic picklist rendered in a Lightning component on a Lightning page.

clone()
Makes a duplicate copy of the `VisualEditor.DynamicPickListRows` object.


Apex Reference Guide DynamicPickListRows Class

containsAllRows()
Returns a Boolean value indicating whether all values of the picklist are included when a user does a type-ahead search query (true)
or only those values initially displayed when the list is clicked on (false).

get(i)
Returns a picklist element stored at the specified index.

getDataRows()
Returns a list of picklist items.

setContainsAllRows(containsAllRows)
Sets the value indicating whether all values of the picklist are included when a user does a type-ahead search query (true) or only
those values initially displayed when the list is clicked on (false).

size()
Returns the size of the list of `VisualEditor.DynamicPickListRows` .

sort()
Sorts the list of `VisualEditor.DynamicPickListRows` .

##### addAllRows(rows)

Adds a list of picklist items to a dynamic picklist rendered in a Lightning component on a Lightning page.

Signature

```
   public void addAllRows(List<VisualEditor.DataRow> rows)

```

Parameters

```
   rows
```

Type: List VisualEditor.DataRow

List of picklist items.

Return Value

Type: void

##### addRow(row)

Adds a single picklist item to a dynamic picklist rendered in a Lightning component on a Lightning page.

Signature

```
   public void addRow(VisualEditor.DataRow row)

```

Parameters

```
   row
```

Type: VisualEditor.DataRow

A single picklist item.


Apex Reference Guide DynamicPickListRows Class

Return Value

Type: void

##### clone()

Makes a duplicate copy of the `VisualEditor.DynamicPickListRows` object.

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### containsAllRows()

Returns a Boolean value indicating whether all values of the picklist are included when a user does a type-ahead search query (true) or
only those values initially displayed when the list is clicked on (false).

Signature

```
   public Boolean containsAllRows()

```

Return Value

Type: Boolean

##### A picklist in a Lightning component can display only the first 200 values of a list. If containsAllRows is set to false, when a user

does a type-ahead search to find values in the picklist, the search will only look at those first 200 values that were displayed, not the
complete set of picklist values.

##### get(i)

Returns a picklist element stored at the specified index.

Signature

```
   public VisualEditor.DataRow get(Integer i)

```

Parameters

```
   i
```

Type: Integer

The index.

Return Value

Type: VisualEditor.DataRow


Apex Reference Guide DynamicPickListRows Class

##### getDataRows()

Returns a list of picklist items.

Signature

```
   public List<VisualEditor.DataRow> getDataRows()

```

Return Value

Type: List VisualEditor.DataRow

##### setContainsAllRows(containsAllRows)

Sets the value indicating whether all values of the picklist are included when a user does a type-ahead search query (true) or only those
values initially displayed when the list is clicked on (false).

Signature

```
   public void setContainsAllRows(Boolean containsAllRows)

```

Parameters

```
   containsAllRows
```

Type: Boolean

Indicates if all values of the picklist are included in a type-ahead search query (true) or only those values initially displayed when the
list is clicked on (false).

A picklist in a Lightning component can display only the first 200 values of a list. If _`containsAllRows`_ is set to false, when a
user does a type-ahead search to find values in the picklist, the search will only look at those first 200 values that were displayed,
not the complete set of picklist values.

Return Value

Type: void

##### size()

Returns the size of the list of `VisualEditor.DynamicPickListRows` .

Signature

```
   public Integer size()

```

Return Value

Type: Integer

##### sort()

Sorts the list of `VisualEditor.DynamicPickListRows` .


## Apex Reference Guide Wave Namespace

Signature

```
   public void sort()

```

Return Value

Type: void

## Wave Namespace The classes in the Wave namespace are part of the CRM Analytics Analytics SDK, designed to facilitate querying CRM Analytics data

from Apex code.

## The following are the classes in the Wave namespace.

IN THIS SECTION:

### QueryBuilder Class

The QueryBuilder class provides methods for constructing well-formed SAQL queries to pass to CRM Analytics.

QueryNode Class
Define each node of the query - such as projection, groups, order, filters. Execute the query.

ProjectionNode Class
Add aggregate functions to the query, or define an alias.

Templates Class
The Templates class provides methods for retrieving CRM Analytics template collections, individual templates, and template
configurations.

TemplatesSearchOptions Class
The TemplatesSearchOptions class provides optional properties to filter the template collection.

### QueryBuilder Class

The QueryBuilder class provides methods for constructing well-formed SAQL queries to pass to CRM Analytics.

Namespace

wave

Usage

Use QueryBuilder and its associated classes, `Wave.ProjectionNode` and `Wave.QueryNode`, to incrementally build your SAQL
statement. For example:

```
   public static void executeApexQuery(String name){

     Wave.ProjectionNode[] projs = new Wave.ProjectionNode[]{

      Wave.QueryBuilder.get('State').alias('State'),

      Wave.QueryBuilder.get('City').alias('City'),

      Wave.QueryBuilder.get('Revenue').avg().alias('avg_Revenue'),

      Wave.QueryBuilder.get('Revenue').sum().alias('sum_Revenue'),

```


Apex Reference Guide QueryBuilder Class

```
      Wave.QueryBuilder.count().alias('count')};

     ConnectApi.LiteralJson result = Wave.QueryBuilder.load('0FbD00000004DSzKAM',

   '0FcD00000004FEZKA2')

      .group(new String[]{'State', 'City'})

      .foreach(projs)

      .execute('q');

     String response = result.json;

   }

```

Examples

QueryBuilder is the core of this first phase of the CRM Analytics Apex SDK, so let’s take a closer look. Here’s a simple count query.

```
   Wave.ProjectionNode[] projs = new

   Wave.ProjectionNode[]{Wave.QueryBuilder.count().alias('c')};

   String query = Wave.QueryBuilder.load('datasetId',

   'datasetVersionId').group().foreach(projs).build('q');

```

The resulting SAQL query looks like this:

```
   q = load "datasetId/datasetVersionId";

   q = group q by all;

   q = foreach q generate count as c;

```

Here’s a more complex example that uses a union statement.

```
   Wave.ProjectionNode[] projs = new Wave.ProjectionNode[]{Wave.QueryBuilder.get('Name'),

   Wave.QueryBuilder.get('AnnualRevenue').alias('Revenue')};

   Wave.QueryNode nodeOne =

   Wave.QueryBuilder.load('datasetOne','datasetVersionOne').foreach(projs);

   Wave.QueryNode nodeTwo = Wave.QueryBuilder.load('datasetTwo',

   'datasetVersionTwo').foreach(projs);

   String query = Wave.QueryBuilder.union(new List<Wave.QueryNode>{nodeOne,

   nodeTwo}).build('q');

```

The resulting SAQL query has two projection streams, _`qa`_ and _`qb`_ .

```
   qa = load "datasetOne/datasetVersionOne";

   qa = foreach q generate Name,AnnualRevenue as Revenue;

   qb = load "datasetTwo/datasetVersionTwo";

   qb = foreach q generate Name,AnnualRevenue as Revenue;

   q = union qa, qb;

```

IN THIS SECTION:

#### QueryBuilder Methods QueryBuilder Methods The following are methods for QueryBuilder .


Apex Reference Guide QueryBuilder Class

IN THIS SECTION:

##### load(datasetID, datasetVersionID)

Load a stream from a dataset.

##### count()

Calculate the number of rows that match the query criteria.

get(projection)
Query by selecting specific attributes.

union(unionNodes)
Combine multiple result sets into one result set.

cogroup(cogroupNodes, groups)
Cogrouping means that two input streams are grouped independently and arranged side by side. Only data that exists in both
groups appears in the results.

##### load(datasetID, datasetVersionID)

Load a stream from a dataset.

Signature

```
   public static wave.QueryNode load(String datasetID, String datasetVersionID)

```

Parameters

```
   datasetID
```

Type: String

The ID of the dataset.

```
   datasetVersionID
```

Type: String

The ID identifying the version of the dataset.

Return Value

Type: wave.QueryNode

##### count()

Calculate the number of rows that match the query criteria.

Signature

```
   public static wave.ProjectionNode count()

```

Return Value

Type: wave.ProjectionNode


Apex Reference Guide QueryBuilder Class

##### get(projection)

Query by selecting specific attributes.

Signature

```
   public static wave.ProjectionNode get(String proj)

```

Parameters

```
   proj
```

Type: String

The name of the column to query.

Return Value

Type: wave.ProjectionNode

##### union(unionNodes)

Combine multiple result sets into one result set.

Signature

```
   global static Wave.QueryNode union(List<Wave.QueryNode> unionNodes)

```

Parameters

```
   unionNodes
```

Type: List<wave.QueryNode>

List of nodes to combine.

Return Value

Type: wave.QueryNode

##### cogroup(cogroupNodes, groups)

Cogrouping means that two input streams are grouped independently and arranged side by side. Only data that exists in both groups
appears in the results.

Signature

```
   global static Wave.QueryNode cogroup(List<Wave.QueryNode> cogroupNodes,

   List<List<String>> groups)

```

Parameters

```
   cogroupNodes
```

Type: wave.QueryNode


### Apex Reference Guide QueryNode Class

List of nodes to group.

```
   groups
```

Type: String

The type of grouping.

Return Value

Type: wave.QueryNode

### QueryNode Class

Define each node of the query - such as projection, groups, order, filters. Execute the query.

Namespace

wave

Usage

Refer to the QueryBuilder example.

IN THIS SECTION:

#### QueryNode Methods QueryNode Methods

### The following are methods for QueryNode .

IN THIS SECTION:

build(streamName)
Build the query string represented by this QueryNode and assign it to a stream name.

foreach(projections)
Applies a set of expressions to every row in a dataset. This action is often referred to as projection.

group(groups)
Groups matched records (group by specific dataset attributes).

group()
Groups matched records (group by all).

order(orders)
Sorts in ascending or descending order on one or more fields.

cap(cap)
Limits the number of results that are returned.

filter(filterCondition)
Selects rows from a dataset based on a filter condition (a predicate).


Apex Reference Guide QueryNode Class

filter(filterConditions)
Selects rows from a dataset based on multiple filter conditions (predicates).

execute(streamName)
Execute the query and return rows as JSON.

##### build(streamName)

Build the query string represented by this QueryNode and assign it to a stream name.

Signature

```
   public String build(String streamName)

```

Parameters

```
   streamName
```

Type: String

The identifier for the stream - for example, “q”.

Return Value

Type: String

The SAQL query string represented by the QueryNode.

##### foreach(projections)

Applies a set of expressions to every row in a dataset. This action is often referred to as projection.

Signature

```
   public wave.QueryNode foreach(List<wave.ProjectionNode> projections)

```

Parameters

```
   projections
```

Type: List<wave.ProjectionNode>

A list of ProjectionNodes to be added to this QueryNode.

Return Value

Type: wave.QueryNode

##### group(groups)

Groups matched records (group by specific dataset attributes).

Signature

```
   public wave.QueryNode group(List<String> groups)

```


Apex Reference Guide QueryNode Class

Parameters

```
   groups
```

Type: List<String>

A list of expressions.

Return Value

Type: wave.QueryNode

Example

```
   Wave.ProjectionNode[] projs = new Wave.ProjectionNode[]{Wave.QueryBuilder.get('Name'),

   Wave.QueryBuilder.get('Revenue').sum().alias('REVENUE_SUM')};

   ConnectApi.LiteralJson result = Wave.QueryBuilder.load('datasetId',

   'datasetVersionId').group(new String[]{'Name'}).foreach(projs).build('q');

##### group()

```

Groups matched records (group by all).

Signature

```
   public wave.QueryNode group()

```

Return Value

Type: wave.QueryNode

Example

```
   String query = Wave.QueryBuilder.load('datasetId',

   'datasetVersionId').group().foreach(projs).build('q');

##### order(orders)

```

Sorts in ascending or descending order on one or more fields.

Signature

```
   public wave.QueryNode group(List<String> groups)

```

Parameters

```
   groups
```

Type: List<String>

A list of column names and associated ascending or descending keywords, for example

```
     List<List<String>>{new List<String>{'Name', 'asc'}, new List<String>{'Revenue', 'desc'}}

```


Apex Reference Guide QueryNode Class

Return Value

Type: wave.QueryNode

##### cap(cap)

Limits the number of results that are returned.

Signature

```
   global Wave.QueryNode cap(Integer cap)

```

Parameters

##### _`cap`_

Type: Integer

The maximum number of rows to return.

Return Value

Type: wave.QueryNode

##### filter(filterCondition)

Selects rows from a dataset based on a filter condition (a predicate).

Signature

```
   public wave.QueryNode filter(String filterCondition)

```

Parameters

```
   filterCondition
```

Type: String

For example: `filter('Name != \'My Name\'')`

Return Value

Type: wave.QueryNode

##### filter(filterConditions)

Selects rows from a dataset based on multiple filter conditions (predicates).

Signature

```
   public wave.QueryNode filter(List<String> filterCondition)

```


### Apex Reference Guide ProjectionNode Class

Parameters

```
   filterCondition
```

Type: List<String>

A list of filter conditions.

Return Value

Type: wave.QueryNode

##### execute(streamName)

Execute the query and return rows as JSON.

Signature

```
   global ConnectApi.LiteralJson execute(String streamName)

```

Parameters

```
   streamName
```

Type: String

The query stream to execute. For example:

```
     ConnectApi.LiteralJson result = Wave.QueryBuilder.load('datasetId',

         'datasetVersionId').group().foreach(projs).execute('q');

```

Return Value

Type: ConnectApi.LiteralJson

### ProjectionNode Class

Add aggregate functions to the query, or define an alias.

Namespace

wave on page 4481

Usage

Refer to the QueryBuilder example.

IN THIS SECTION:

#### ProjectionNode Methods ProjectionNode Methods

### The following are methods for ProjectionNode .


Apex Reference Guide ProjectionNode Class

IN THIS SECTION:

##### sum()

Returns the sum of a numeric field.

##### avg()

Returns the average value of a numeric field.

##### min()

Returns the minimum value of a field.

max()
Returns the maximum value of a field.

count()
Returns the number of rows that match the query criteria.

unique()
Returns the count of unique values.

alias(name)
Define output column names.

##### sum()

Returns the sum of a numeric field.

Signature

```
   public wave.ProjectionNode sum()

```

Return Value

Type: wave.ProjectionNode

##### avg()

Returns the average value of a numeric field.

Signature

```
   public wave.ProjectionNode avg()

```

Return Value

Type: wave.ProjectionNode

##### min()

Returns the minimum value of a field.

Signature

```
   public wave.ProjectionNode min()

```


Apex Reference Guide ProjectionNode Class

Return Value

Type: wave.ProjectionNode

##### max()

Returns the maximum value of a field.

Signature

```
   public wave.ProjectionNode max()

```

Return Value

Type: wave.ProjectionNode

##### count()

Returns the number of rows that match the query criteria.

Signature

```
   public wave.ProjectionNode count()

```

Return Value

Type: wave.ProjectionNode

##### unique()

Returns the count of unique values.

Signature

```
   public wave.ProjectionNode unique()

```

Return Value

Type: wave.ProjectionNode

##### alias(name)

Define output column names.

Signature

```
   public wave.ProjectionNode alias(String name)

```


### Apex Reference Guide Templates Class

Parameters

```
   name
```

Type: String

The name to use for this column. For example, this code defines the alias `c` :

```
     Wave.ProjectionNode[] projs = new

     Wave.ProjectionNode[]{Wave.QueryBuilder.count().alias('c')};

```

Return Value

Type: wave.ProjectionNode

### Templates Class

The Templates class provides methods for retrieving CRM Analytics template collections, individual templates, and template configurations.

Namespace

Wave

Usage

Use Templates and its associated class `Wave.TemplatesSearchOptions` to get CRM Analytics template information.

Examples

This code sample declares a method that returns a list of the template names.

```
   @AuraEnabled(cacheable=true)

   public static void List<String> getTemplateNames() {

     Map<String, Object> o = Wave.Templates.getTemplates(new Wave.TemplatesSearchOptions());

     List<Object> templates = (List<Object>) o.get('templates');

     List<String> names = new List<String>();

     for (Object templateObj : templates) {

      names.add((String) ((Map<String, Object>) templateObj.get('name'));

     }

     return names;

   }

```

Adding the `@AuraEnabled` annotation allows Lightning Web Components to access Templates methods directly.

For example, in the lwc.js file:

```
   import getTemplates from '@salesforce/apex/Wave.Templates.getTemplates';

   export default class Templates extends LightningElement {

     @wire(getTemplates, {

      // specifying 'options' is optional

      options: {

       // values in TemplatesSearchOptions go here; all optional

       type: 'app'

      }

```


Apex Reference Guide Templates Class

```
     })

     onTemplates({ data, error }) {

      if (data) {

       console.log('template names=' + data.templates.map(l => l.name).join(', '));

      }

     }

   }

```

IN THIS SECTION:

#### Templates Methods Templates Methods The following are methods for Templates .

IN THIS SECTION:

##### getTemplate(templateIdOrApiName)

Gets a CRM Analytics template by the specified ID or API name. The returned template is a map of the template JSON attributes as
name/value pairs.

getTemplateConfig(templateIdOrApiName)
Gets the CRM Analytics template configuration by the specified ID or API name. The returned template configuration is a map of the
JSON attributes as name/value pairs.

getTemplates(options)
Get a filtered collection of CRM Analytics templates using search options.

getTemplates()
Gets all CRM Analytics templates.

##### **`getTemplate(templateIdOrApiName)`**

Gets a CRM Analytics template by the specified ID or API name. The returned template is a map of the template JSON attributes as
name/value pairs.

Signature

```
   public static Map<String,Object> getTemplate(String templateIdOrApiName)

```

Parameters

```
   templateIdOrApiName
```

Type: String

The template ID or API name of the template to retrieve.

Return Value

[Type: Map<String,Object>](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_maps.htm)


Apex Reference Guide Templates Class

A map of the template JSON attribute name/value pairs, where the name is a string with an object value. For attributes details, see
[TemplateRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_resources_templates_id.htm)

Example

```
   String templateName = (String) Wave.Templates.getTemplate( templateId ).get('name');

##### **`getTemplateConfig(templateIdOrApiName)`**

```

Gets the CRM Analytics template configuration by the specified ID or API name. The returned template configuration is a map of the
JSON attributes as name/value pairs.

Signature

```
   public static Map<String,Object> getTemplateConfig(String templateIdOrApiName)

```

Parameters

```
   templateIdOrApiName
```

Type: String

The template ID or developer name to retrieve the template configuration for.

Return Value

[Type: Map<String,Object>](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dev_guide.htm)

A map of template configuration JSON attribute names and the object values. For attribute details, see
[TemplateConfigurationRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_resources_templates_configuration.htm)

Example

```
   Map<String, Object> templateVariables = (Map<String, Object>)

   Wave.Templates.getTemplateConfig( templateId ).get('variables');

##### **`getTemplates(options)`**

```

Get a filtered collection of CRM Analytics templates using search options.

Signature

```
   public static Map<String,Object> getTemplates(Wave.TemplatesSearchOptions options)

```

Parameters

```
   options
```

Type: Wave.TemplatesSearchOptions on page 4495

The search options to use for filtering the template collection.


### Apex Reference Guide TemplatesSearchOptions Class

Return Value

[Type: Map<String,Object>](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dev_guide.htm)

[A map of template names and the template object values. For template collection details, see TemplateCollectionRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_resources_templates.htm)

Example

```
   Map<String,Object> templatesMap = Wave.Templates.getTemplates(new

   Wave.TemplatesSearchOptions());

##### **`getTemplates()`**

```

Gets all CRM Analytics templates.

Signature

```
   public static Map<String,Object> getTemplates()

```

Return Value

[Type: Map<String,Object>](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dev_guide.htm)

[A map of template names and the template object values. For template collection details, see TemplateCollectionRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_resources_templates.htm)

Example

```
   Map<String,Object> templatesMap = Wave.Templates.getTemplates();

### TemplatesSearchOptions Class

```

The TemplatesSearchOptions class provides optional properties to filter the template collection.

Namespace

Wave

Usage

Use TemplatesSearchOptions with `Wave.Templates` class to filter the CRM Analytics template collection returned. For example:

```
   public static void List<String> getAppTemplates() {

     Wave.TemplateSearchOptions tsOptions = new Wave.TemplatesSearchOptions();

     tsOptions.type = 'app';

     Map<String, Object> o = Wave.Templates.getTemplates(tsOptions);

     List<Object> appTemplates = (List<Object>) o.get('templates');

     List<String> names = new List<String>();

     for (Object templateObj : appTemplates) {

      names.add((String) ((Map<String, Object>) templateObj.get('name'));

     }

```


Apex Reference Guide TemplatesSearchOptions Class

```
     return names;

   }

```

IN THIS SECTION:

#### TemplatesSearchOptions Properties TemplatesSearchOptions Properties The following are properties for TemplatesSearchOptions .

IN THIS SECTION:

##### filterGroup

Specifies the Connect API filter group for CRM Analytics template search options.

##### options

Specifies the template visibility option to filter the CRM Analytics template collection by.

type
Sets the template type to filter the CRM Analytics template collection by.

##### **`filterGroup`**

Specifies the Connect API filter group for CRM Analytics template search options.

Signature

```
   public String filterGroup {get; set;}

```

Property Value

Type: String

[Uses the ConnectFilterGroupEnum values.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_filter_groups.htm)

Example

```
   Wave.TemplateSearchOptions tsOptions = new Wave.TemplatesSearchOptions();

   tsOptions.filterGroup = 'small';

##### **`options`**

```

Specifies the template visibility option to filter the CRM Analytics template collection by.

Signature

```
   public String options {get; set;}

```


## Apex Reference Guide Appendices

Property Value

Type: String

Uses the `ConnectWaveTemplateVisibilityOptionsEnum` values. Valid values are `CreateApp`, `ViewOnly`, and
`ManageableOnly` .

Example

```
   Wave.TemplateSearchOptions tsOptions = new Wave.TemplatesSearchOptions();

   tsOptions.options = 'ViewOnly';

##### **`type`**

```

Sets the template type to filter the CRM Analytics template collection by.

Signature

```
   public String type {get; set;}

```

Property Value

Type: String

Uses the `ConnectWaveTemplateTypeEnum` values. Valid values are `app`, `dashboard`, `embedded`, and `lens` .

Example

```
   Wave.TemplateSearchOptions tsOptions = new Wave.TemplatesSearchOptions();

   tsOptions.type = 'app';

## Appendices

```

IN THIS SECTION:

Apex Versioned Behavior Changes
This document includes major Apex behavior changes across API versions, organized by version number for easy lookup. It isn’t an
exhaustive list of all versioned Apex behavior. For example, this compilation excludes versioned changes to Connect in Apex and
classes in the ConnectApi namespace.

Shipping Invoice Example

Reserved Keywords
These words can be used only as keywords.

Documentation Typographical Conventions
Apex and Visualforce documentation uses these typographical conventions.


### Apex Reference Guide Apex Versioned Behavior Changes Apex Versioned Behavior Changes

This document includes major Apex behavior changes across API versions, organized by version number for easy lookup. It isn’t an
exhaustive list of all versioned Apex behavior. For example, this compilation excludes versioned changes to Connect in Apex and classes
in the ConnectApi namespace.

Keep these guidelines in mind regarding API version usage:

**•** Salesforce strongly recommends that you use the latest available API version.

**•** If you can't upgrade to the latest version yet, use API versions released in the past three years for improved performance, security,
and compatibility.

**•** To reduce complexity, consolidate your Apex codebase to use the minimal number of API versions, ideally, just one API version.

Version 67.0

**Database Operations in User Mode by Default**
In API version 67.0 and later, Apex runs in user context by default, meaning that the current user’s permissions and field-level security
[(FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default. See Set an Access Mode for](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_enforce_usermode.htm)
[Database Operations.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_enforce_usermode.htm)

**Apex Classes Enforce Sharing by Default**
In API version 67.0 and later, classes without an explicit sharing declaration are run in the current user context. In API version 66.0
[and earlier, for classes without an explicit sharing declaration, the current sharing rule remains in effect. See Use the with sharing,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
[without sharing, and inherited sharing Keywords.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

**WITH_SECURITY_ENFORCED Not Supported in SOQL Queries**
With API version 67.0 and later, you cannot use the `WITH SECURITY_ENFORCED` clause in SOQL SELECT queries in Apex code.
Instead, to run a SOQL or SOSL query in user mode, use the `WITH USER_MODE` clause.

Version 65.0

**Access Modifiers with Abstract and Override Methods**

In API version 65.0 and later, an abstract or override method requires a `protected`, `public`, or `global` access modifier. If
one of these access modifiers isn't explicitly included in the method declaration, then method access defaults to private. Private
access is invalid for these method types because the implementing class can't access the abstract method. Therefore, if you attempt
to declare an abstract or override method without an allowed access modifier, you get the compilation error: Abstract methods
require at least one of these modifiers: `global`, `public`, `protected` [. See Extending a Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_extending.htm)

Version 63.0

**DataWeave Version**

API version 63.0 and later support DataWeave 2.9 script syntax. API version 62.0 supports DataWeave 2.8, and API version 61.0 and
[earlier support DataWeave 2.5. See Implementing DataWeave in Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/DataWeaveInApex_impl.htm)

**JSON Serialization of Exceptions**

In API version 63.0 and later, JSON serialization of custom exceptions and most built-in exceptions isn't supported. Attempting to
[serialize an exception throws an error: Type unsupported in JSON: MyException. See JSON Support.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_methods_system_json_overview.htm)


Apex Reference Guide Apex Versioned Behavior Changes

Version 62.0

**DataWeave Version**

[API version 62.0 supports DataWeave 2.8 script syntax. API version 61.0 and earlier versions support DataWeave 2.5. See Implementing](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/DataWeaveInApex_impl.htm)
[DataWeave in Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/DataWeaveInApex_impl.htm)

Version 61.0

**Private Method Override**

In API version 61.0 and later, private methods are no longer overridden by an instance method with the same signature in a subclass.
In API version 60.0 and earlier, if a subclass declares an instance method with the same signature as a private method in one of its
[superclasses, the subclass method overrides the private method. See Interfaces.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_interfaces.htm)

**DMO Information**
In API version 61.0 and later, you can get information on a specific DMO by using `SObjectType.getDescribe()` . Field-level
security isn't enforced because all fields on DMOs that are accessed by field describes and security model checks are read-only. See
[Data Cloud In Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/DataCloudInApex.htm)

Version 60.0

**`instanceof`** **Operator with** **`List`** **and** **`Iterable`**

In API version 60.0 and later, if a `List` [data type implements the Iterable data type, compilation fails. See Using the instanceof](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_instanceof.htm)
[Keyword.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_instanceof.htm)

**Transaction Control: Savepoints**

In API version 60.0 and later, all Apex test savepoints are released when `Test.startTest()` and `Test.stopTest()` are
called. If any savepoints are reset, a SAVEPOINT_RESET event is logged. In API version 59.0 and earlier, making a callout after creating
savepoints throws a CalloutException regardless of whether there was uncommitted DML or the changes were rolled back to a
savepoint. In API version 60.0 and later, `Database.rollback(databaseSavepoint)` and
`Database.setSavepoint()` calls don't increment the DML row usage limit. In API version 59.0 and earlier, these methods
[increment the DML row usage limit. See Transaction Control.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_transaction_control.htm)

API Reference Changes


Apex Reference Guide Apex Versioned Behavior Changes

Version 57.0

API Reference Changes

Version 55.0

**@AuraEnabled Annotation**

[In API version 55.0 and later, overloads aren't allowed on methods annotated with @AuraEnabled. See AuraEnabled Annotation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_annotation_AuraEnabled.htm)

Version 54.0

API Reference Changes


Apex Reference Guide Apex Versioned Behavior Changes

Version 53.0

**DataWeave Integration**
[Apex classes must be at API version 53.0 or later to access DataWeave integration methods. See Implementing DataWeave in Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/DataWeaveInApex_impl.htm)

**JSON DateTime Format**

In API version 53.0 and later, DateTime format and processing has been updated. The API correctly handles DateTime values in JSON
requests that use more than 3 digits after the decimal point. Requests that use an unsupported DateTime format (such as 123456000)
result in an error. Salesforce recommends that you strictly adhere to DateTime formats specified in Valid Date and DateTime Formats.
[See Valid Date and DateTime Formats.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/intro_valid_date_formats.htm)

**Trigger Order of Execution**
[In API version 53.0 and earlier, after-save record-triggered flows run after entitlements are executed. See Triggers and Order of](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)
[Execution.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)

API Reference Changes

Version 52.0

**CardPaymentMethods and DigitalWallets**

In API version 52.0 and later, CardPaymentMethods and DigitalWallets can’t store values for GatewayTokenEncryption and
GatewayToken at the same time on the same record. If you try to assign one while the other exists, Salesforce throws an error. See
[Tokenization Service Apex Class Implementation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_commercepayments_tokenization_service_apex_imp.htm)


Apex Reference Guide Apex Versioned Behavior Changes

API Reference Changes

Version 51.0

API Reference Changes

Version 50.0

**@NamespaceAccessible Annotation**

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that
[are annotated with @NamespaceAccessible. See NamespaceAccessible Annotation and Class Variables.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_annotation_NamespaceAccessible.htm)

Version 49.0

**@JsonAccess Annotation**

In API version 49.0 and later, the default access for both serialization and deserialization is `sameNamespace` . In API version 48.0
and earlier, the default access for deserialization is `always` and the default access for serialization is `sameNamespace` to preserve
[the existing behavior. See JsonAccess Annotation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_annotation_JsonAccess.htm)


Apex Reference Guide Apex Versioned Behavior Changes

**@ReadOnly Annotation on REST Methods**

In API version 49.0 and later, you can annotate Apex REST methods with just @ReadOnly. In API version 49.0 and earlier, Apex REST
[methods with the @ReadOnly annotation also require the @RemoteAction annotation. See ReadOnly Annotation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_annotation_ReadOnly.htm)

Version 47.0

**@NamespaceAccessible Annotation**

In API version 47.0 and later, @NamespaceAccessible isn't allowed on an entity marked with @AuraEnabled. Therefore, an Aura or
Lightning web component installed from a package can't call an Apex method from another package, even if both packages are in
the same namespace. However, an @AuraEnabled public method from one package can call a @NamespaceAccessible public method
[from another package in the same namespace. See NamespaceAccessible Annotation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_annotation_NamespaceAccessible.htm)

API Reference Changes

`changedfields` Properties in `EventBus.ChangeEventHeader` : A list of the fields that were changed in an update operation,
including the LastModifiedDate system field. This field is empty for other operations, including record creation. This property is available
[in Apex saved using API version 47.0 or later. See ChangeEventHeader Properties.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_eventbus_ChangeEventHeader.htm#apex_eventbus_ChangeEventHeader_properties)

Version 45.0

**WITH SECURITY_ENFORCED Clause in SOQL**

The WITH SECURITY_ENFORCED clause is only available in Apex. We don’t recommend using WITH SECURITY_ENFORCED in Apex
[classes or triggers with an API version earlier than 45.0. See Filter SOQL Queries Using WITH SECURITY_ENFORCED.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_with_security_enforced.htm)

API Reference Changes

Version 44.0

**BatchApexErrorEvent**
The BatchApexErrorEvent object represents a platform event associated with a batch Apex class. This object is available in API version
44.0 and later. If the `start`, `execute`, or `finish` method of a batch Apex job encounters an unhandled exception, a
`BatchApexErrorEvent` [platform event is fired. For more details, see BatchApexErrorEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_batchapexerrorevent.htm)

**AuraEnabled Annotation**
In API version 44.0 and later, you can improve runtime performance by caching method results on the client by using the annotation
`@AuraEnabled(cacheable=true)` . You can cache method results only for methods that retrieve data but don’t modify it.
Using this annotation eliminates the need to call `setStorable()` in JavaScript code on every action that calls the Apex method.
[See AuraEnabled Annotation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_annotation_AuraEnabled.htm)


Apex Reference Guide Apex Versioned Behavior Changes

Version 42.0

**Hierarchy Custom Settings**
In API version 42.0 and later, if a hierarchy custom setting is inserted in a `testSetup` method, inserting a hierarchy custom setting
record with the same SetupOwnerId in a test method throws a DUPLICATE_VALUE exception. In API version 41.0 and earlier, each
method in an Apex test class, including `testSetup` methods, is able to insert hierarchy custom setting values. This behavior is
true even when the methods have the same SetupOwnerId value as a hierarchy custom setting record inserted in a different test
[method. See Hierarchy Custom Setting Methods.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_custom_settings.htm#apex_System_HierarchyCustomSetting_instance_methods)

**Apex Properties**
[In API version 42.0 and later, unless a variable value is set in a set accessor, you can’t update its value in a get accessor. See Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_properties.htm)
[Properties.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_properties.htm)

Version 41.0

**Exception Handling**

[In API version 41.0 and later, unreachable statements in your code cause compilation errors. See Exception Statements.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_exception_statements.htm)

API Reference Changes

Version 39.0

API Reference Changes


Apex Reference Guide Apex Versioned Behavior Changes

Version 35.0

**Serialization of IDs**
In API version 35.0 and later, ID comparison using `==` does not fail for IDs that have been through roundtrip JSON serialization and
[deserialization. See Roundtrip Serialization and Deserialization.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_json_json.htm)

API Reference Changes

Version 34.0

**Schema Namespace Prefixes**

In API version 34.0 and later, `Schema.DescribeSObjectResult` on a custom SObjectType includes map keys prefixed with
the namespace, even if the namespace is that of currently executing code. If you work with multiple namespaces and generate
[run-time describe data, make sure that your code accesses keys correctly by using the namespace prefix. See Namespace Prefix.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_namespace_prefix.htm)

API Reference Changes


Apex Reference Guide Apex Versioned Behavior Changes

Version 33.0

API Reference Changes

Version 32.0

**`instanceof`** **Operator**

In API version 32.0 and later, `instanceof` returns `false` if the left operand is a null object. In API version 31.0 and earlier,

`instanceof` returns `true` [in this case. See Using the Instance of Keyword.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_instanceof.htm)

Version 28.0

**Null Fields in JSON Serialization**

In API version 28.0 and later, null fields aren’t serialized and aren’t included in the JSON string, unlike in earlier versions. This change
[doesn’t affect deserializing JSON strings with JSON methods, such as Json.deserialize(). This change is noticeable when you inspect](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Json.htm#apex_System_Json_deserialize)
the JSON string.

**VLOOKUP Validation Rule Function**
In API version 28.0 and later, the VLOOKUP validation rule function no longer accesses organization data from a running Apex test.
The function looks up only data created by the test, unless the test class or method is annotated with
`IsTest(SeeAllData=true)` . In API version 27.0 and earlier, the VLOOKUP validation rule function always looks up org data
[in addition to test data when fired by a running Apex test. See Isolation of Test Data from Organization Data in Unit Tests.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_data_access.htm)

Version 26.0

**Chaining Batch Jobs**

In API version 26.0 and later, you can start another batch job from an existing batch job to chain jobs together, enforcing strict
[sequential execution. See Use Batch Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)


Apex Reference Guide Apex Versioned Behavior Changes

**Calling** **`Database.executeBatch`** **and** **`System.scheduleBatch`** **Methods**

In API version 26.0 and later, you can call `Database.executeBatch` and `System.scheduleBatch` from any batch
[Apex method. See Use Batch Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)

Version 24.0

**Apex Test Methods**
In API version 24.0 and later, Apex test methods can’t access pre-existing org data by default, such as standard objects, custom
objects, and custom settings data. They can only access data that they create. However, objects that are used to manage your
organization or metadata objects can still be accessed in your tests. In API version 23.0 and earlier, test code continues to have access
[to all data in the organization and its data access is unchanged. See Isolation of Test Data from Organization Data in Unit Tests.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_data_access.htm)

Version 22.0

**Batch Apex Exceptions with Test Methods**

In API version 22.0 and later, exceptions that occur during the execution of a batch Apex job invoked by a test method are passed
[to the calling test method. As a result, these exceptions cause the test method to fail. See Use Batch Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)

Version 21.0

**Bulk API Requests**
In API version 21.0 and later, if a Bulk API request causes a trigger to fire, each chunk of 200 records for the trigger to process is no
longer split into smaller chunks. If a Bulk API request causes a trigger to fire multiple times for chunks of 200 records, governor limits
are reset between these trigger invocations for the same HTTP request. Static variables aren’t reset within the multiple trigger
invocations for the same Bulk API request. In API version 20.0 and earlier, if a Bulk API request causes a trigger to fire, each chunk of
200 records for the trigger to process is split into chunks of 100 records.

**`FeedPost`** **Objects**
In API version 21.0, insert and delete triggers on FeedPost objects are supported. In API version 20.0 and earlier, these trigger operations
[on FeedPost aren't supported. See Triggers for Chatter Objects.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers_fields_not_updated_chatter.htm)

Note: The `FeedPost` object is discontinued in API version 22.0 and later. Use `FeedItem` [instead. See FeedItem](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_feeditem.htm)

Version 17.0

**HTTP Response Decoding**
In API version 17.0 and later, HTTP responses are decoded using the encoding specified in the Content-Type header. In API versions
[16.0 and earlier, HTTP responses for callouts are always decoded using UTF-8, regardless of the Content-Type header. See SOAP](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_wsdl2apex.htm)
[Services: Defining a Class from a WSDL Document.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_wsdl2apex.htm)

Version 16.0

**Decimal Data Type**

In API version 16.0 and later, Apex uses the higher-precision `Decimal` [data type in certain types such as currency. See Primitive](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)
[Data Types.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)


### Apex Reference Guide Shipping Invoice Example

Version 15.0

**`anyType`** **datatype**
The Salesforce datatype `anyType` is not supported in WSDLs used to generate Apex code that is saved by using API version 15.0
and later. In API version 14.0 and earlier, `anyType` [is mapped to String. See SOAP Services: Defining a Class from a WSDL Document.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_wsdl2apex.htm)

**DMLOptions Settings**
DMLOptions settings are only available for Apex saved against API versions 15.0 and higher. DMLOptions settings take effect only
for record operations performed by using Apex DML and not through the Salesforce user interface.

In API version 15.0 and later, the Database.DMLOptions `emailHeader` property enables you to specify information about the
[email sent when an event occurs because of Apex DML code execution. See Setting DML Options.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_dml_database_dmloptions.htm)

**String values**
In API version 15.0 and higher, assigning a `String` value that is too long for the field produces a run-time error.

### Shipping Invoice Example

This appendix provides an example of an Apex application. This is a more complex example than the Hello World example.

**•** Shipping Invoice Walk-Through

### • Shipping Invoice Example Code

IN THIS SECTION:

### 1. Shipping Invoice Example Walk-Through 2. Shipping Invoice Example Code Shipping Invoice Example Walk-Through

The sample application in this section includes traditional Salesforce functionality blended with Apex. Many of the syntactic and semantic
features of Apex, along with common idioms, are illustrated in this application.

Note: The Shipping Invoice sample requires custom objects. You can either create these on your own, or download the objects
and Apex code as an unmanaged package from the Salesforce AppExchange. To obtain the sample assets in your org, install the
[Apex Tutorials Package. This package also contains sample code and objects for the Apex Quick Start.](https://appexchange.salesforce.com/listingDetail?listingId=a0N30000001saDCEAY)

Scenario

In this sample application, the user creates a new shipping invoice, or order, and then adds items to the invoice. The total amount for
the order, including shipping cost, is automatically calculated and updated based on the items added or deleted from the invoice.

Data and Code Models

This sample application uses two new objects: Item and Shipping_invoice.

The following assumptions are made:

**•** Item A cannot be in both orders shipping_invoice1 and shipping_invoice2. Two customers cannot obtain the same (physical)
product.

**•** The tax rate is 9.25%.

**•** The shipping rate is 75 cents per pound.


Apex Reference Guide Shipping Invoice Example

**•** Once an order is over $100, the shipping discount is applied (shipping becomes free).

The fields in the Item custom object include:

**Name** **Type** **Description**

Name String The name of the item

Price Currency The price of the item

Quantity Number The number of items in the order

Weight Number The weight of the item, used to calculate shipping costs

Shipping_invoice Master-Detail (shipping_invoice) The order this item is associated with

The fields in the Shipping_invoice custom object include:

**Name** **Type** **Description**

Name String The name of the shipping invoice/order

Subtotal Currency The subtotal

GrandTotal Currency The total amount, including tax and shipping

Shipping Currency The amount charged for shipping (assumes $0.75 per pound)

ShippingDiscount Currency Only applied once when subtotal amount reaches $100

Tax Currency The amount of tax (assumes 9.25%)

TotalWeight Number The total weight of all items

All of the Apex for this application is contained in triggers. This application has the following triggers:

**Object** **Trigger Name** **When Runs** **Description**

Item Calculate after insert, after update, after delete Updates the shipping invoice, calculates the totals and
shipping

Shipping_invoice ShippingDiscount after update Updates the shipping invoice, calculating if there is a
shipping discount

The following is the general flow of user actions and when triggers run:


#### Apex Reference Guide Shipping Invoice Example

**Flow of user action and triggers for the shopping cart application**

**1.** User clicks **Orders**    - **New**, names the shipping invoice and clicks **Save** .

**2.** User clicks **New Item**, fills out information, and clicks **Save** .

**3.** Calculate trigger runs. Part of the Calculate trigger updates the shipping invoice.

**4.** ShippingDiscount trigger runs.

**5.** User can then add, delete or change items in the invoice.

In Shipping Invoice Example Code both of the triggers and the test class are listed. The comments in the code explain the functionality.

Testing the Shipping Invoice Application

Before an application can be included as part of a package, 75% of the code must be covered by unit tests. Therefore, one piece of the
shipping invoice application is a class used for testing the triggers.

The test class verifies the following actions are completed successfully:

**•** Inserting items

**•** Updating items

**•** Deleting items

**•** Applying shipping discount

**•** Negative test for bad input

#### Shipping Invoice Example Code

The following triggers and test class make up the shipping invoice example application:


Apex Reference Guide Shipping Invoice Example

**•** Calculate trigger

**•** ShippingDiscount trigger

**•** Test class

Calculate Trigger

```
   trigger calculate on Item__c (after insert, after update, after delete) {

   // Use a map because it doesn't allow duplicate values

   Map<ID, Shipping_Invoice__C> updateMap = new Map<ID, Shipping_Invoice__C>();

   // Set this integer to -1 if we are deleting

   Integer subtract ;

   // Populate the list of items based on trigger type

   List<Item__c> itemList;

      if(trigger.isInsert || trigger.isUpdate){

        itemList = Trigger.new;

        subtract = 1;

      }

      else if(trigger.isDelete)

      {

        // Note -- there is no trigger.new in delete

        itemList = trigger.old;

        subtract = -1;

      }

   // Access all the information we need in a single query

   // rather than querying when we need it.

   // This is a best practice for bulkifying requests

   set<Id> AllItems = new set<id>();

   for(item__c i :itemList){

   // Assert numbers are not negative.

   // None of the fields would make sense with a negative value

   System.assert(i.quantity__c > 0, 'Quantity must be positive');

   System.assert(i.weight__c >= 0, 'Weight must be non-negative');

   System.assert(i.price__c >= 0, 'Price must be non-negative');

   // If there is a duplicate Id, it won't get added to a set

   AllItems.add(i.Shipping_Invoice__C);

   }

   // Accessing all shipping invoices associated with the items in the trigger

   List<Shipping_Invoice__C> AllShippingInvoices = [SELECT Id, ShippingDiscount__c,

               SubTotal__c, TotalWeight__c, Tax__c, GrandTotal__c

               FROM Shipping_Invoice__C WHERE Id IN :AllItems];

   // Take the list we just populated and put it into a Map.

   // This will make it easier to look up a shipping invoice

```


Apex Reference Guide Shipping Invoice Example

```
   // because you must iterate a list, but you can use lookup for a map,

   Map<ID, Shipping_Invoice__C> SIMap = new Map<ID, Shipping_Invoice__C>();

   for(Shipping_Invoice__C sc : AllShippingInvoices)

   {

      SIMap.put(sc.id, sc);

   }

   // Process the list of items

      if(Trigger.isUpdate)

      {

        // Treat updates like a removal of the old item and addition of the

        // revised item rather than figuring out the differences of each field

        // and acting accordingly.

        // Note updates have both trigger.new and trigger.old

        for(Integer x = 0; x < Trigger.old.size(); x++)

        {

           Shipping_Invoice__C myOrder;

           myOrder = SIMap.get(trigger.old[x].Shipping_Invoice__C);

           // Decrement the previous value from the subtotal and weight.

           myOrder.SubTotal__c -= (trigger.old[x].price__c *

                         trigger.old[x].quantity__c);

           myOrder.TotalWeight__c -= (trigger.old[x].weight__c *

                           trigger.old[x].quantity__c);

           // Increment the new subtotal and weight.

           myOrder.SubTotal__c += (trigger.new[x].price__c *

                         trigger.new[x].quantity__c);

           myOrder.TotalWeight__c += (trigger.new[x].weight__c *

                           trigger.new[x].quantity__c);

        }

        for(Shipping_Invoice__C myOrder : AllShippingInvoices)

        {

           // Set tax rate to 9.25% Please note, this is a simple example.

           // Generally, you would never hard code values.

           // Leveraging Custom Settings for tax rates is a best practice.

           // See Custom Settings in the Apex Developer Guide

           // for more information.

           myOrder.Tax__c = myOrder.Subtotal__c * .0925;

           // Reset the shipping discount

           myOrder.ShippingDiscount__c = 0;

           // Set shipping rate to 75 cents per pound.

           // Generally, you would never hard code values.

           // Leveraging Custom Settings for the shipping rate is a best practice.

           // See Custom Settings in the Apex Developer Guide

           // for more information.

           myOrder.Shipping__c = (myOrder.totalWeight__c * .75);

           myOrder.GrandTotal__c = myOrder.SubTotal__c + myOrder.tax__c +

                         myOrder.Shipping__c;

```


Apex Reference Guide Shipping Invoice Example

```
           updateMap.put(myOrder.id, myOrder);

         }

      }

      else

      {

        for(Item__c itemToProcess : itemList)

        {

           Shipping_Invoice__C myOrder;

           // Look up the correct shipping invoice from the ones we got earlier

           myOrder = SIMap.get(itemToProcess.Shipping_Invoice__C);

           myOrder.SubTotal__c += (itemToProcess.price__c *

                         itemToProcess.quantity__c * subtract);

           myOrder.TotalWeight__c += (itemToProcess.weight__c *

                           itemToProcess.quantity__c * subtract);

        }

        for(Shipping_Invoice__C myOrder : AllShippingInvoices)

        {

           // Set tax rate to 9.25% Please note, this is a simple example.

           // Generally, you would never hard code values.

           // Leveraging Custom Settings for tax rates is a best practice.

           // See Custom Settings in the Apex Developer Guide

           // for more information.

           myOrder.Tax__c = myOrder.Subtotal__c * .0925;

           // Reset shipping discount

           myOrder.ShippingDiscount__c = 0;

           // Set shipping rate to 75 cents per pound.

           // Generally, you would never hard code values.

           // Leveraging Custom Settings for the shipping rate is a best practice.

           // See Custom Settings in the Apex Developer Guide

           // for more information.

           myOrder.Shipping__c = (myOrder.totalWeight__c * .75);

           myOrder.GrandTotal__c = myOrder.SubTotal__c + myOrder.tax__c +

                         myOrder.Shipping__c;

           updateMap.put(myOrder.id, myOrder);

         }

      }

      // Only use one DML update at the end.

      // This minimizes the number of DML requests generated from this trigger.

      update updateMap.values();

   }

```

ShippingDiscount Trigger

```
   trigger ShippingDiscount on Shipping_Invoice__C (before update) {

      // Free shipping on all orders greater than $100

```


Apex Reference Guide Shipping Invoice Example

```
      for(Shipping_Invoice__C myShippingInvoice : Trigger.new)

      {

        if((myShippingInvoice.subtotal__c >= 100.00) &&

          (myShippingInvoice.ShippingDiscount__c == 0))

        {

           myShippingInvoice.ShippingDiscount__c =

                  myShippingInvoice.Shipping__c * -1;

           myShippingInvoice.GrandTotal__c += myShippingInvoice.ShippingDiscount__c;

        }

      }

   }

```

Shipping Invoice Test

```
   @IsTest

   private class TestShippingInvoice{

      // Test for inserting three items at once

      public static testmethod void testBulkItemInsert(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items

        insert Order1;

        List<Item__c> list1 = new List<Item__c>();

        Item__c item1 = new Item__C(Price__c = 10, weight__c = 1, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 25, weight__c = 2, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        list1.add(item1);

        list1.add(item2);

        list1.add(item3);

        insert list1;

        // Retrieve the order, then do assertions

        order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,

              grandtotal__c, shippingdiscount__c

              FROM Shipping_Invoice__C

              WHERE id = :order1.id];

        System.assert(order1.subtotal__c == 75,

             'Order subtotal was not $75, but was '+ order1.subtotal__c);

        System.assert(order1.tax__c == 6.9375,

             'Order tax was not $6.9375, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 4.50,

             'Order shipping was not $4.50, but was ' + order1.shipping__c);

```


Apex Reference Guide Shipping Invoice Example

```
        System.assert(order1.totalweight__c == 6.00,

             'Order weight was not 6 but was ' + order1.totalweight__c);

        System.assert(order1.grandtotal__c == 86.4375,

             'Order grand total was not $86.4375 but was '

              + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == 0,

             'Order shipping discount was not $0 but was '

             + order1.shippingdiscount__c);

      }

      // Test for updating three items at once

      public static testmethod void testBulkItemUpdate(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items.

        insert Order1;

        List<Item__c> list1 = new List<Item__c>();

        Item__c item1 = new Item__C(Price__c = 1, weight__c = 1, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 2, weight__c = 2, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 4, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        list1.add(item1);

        list1.add(item2);

        list1.add(item3);

        insert as system list1;

        // Update the prices on the 3 items

        list1[0].price__c = 10;

        list1[1].price__c = 25;

        list1[2].price__c = 40;

        update as system list1;

        // Access the order and assert items updated

        order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,

              grandtotal__c, shippingdiscount__c

              FROM Shipping_Invoice__C

              WHERE Id = :order1.Id];

        System.assert(order1.subtotal__c == 75,

                 'Order subtotal was not $75, but was '+ order1.subtotal__c);

        System.assert(order1.tax__c == 6.9375,

                 'Order tax was not $6.9375, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 4.50,

                 'Order shipping was not $4.50, but was '

                 + order1.shipping__c);

        System.assert(order1.totalweight__c == 6.00,

```


Apex Reference Guide Shipping Invoice Example

```
                 'Order weight was not 6 but was ' + order1.totalweight__c);

        System.assert(order1.grandtotal__c == 86.4375,

                 'Order grand total was not $86.4375 but was '

                 + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == 0,

                 'Order shipping discount was not $0 but was '

                 + order1.shippingdiscount__c);

      }

      // Test for deleting items

      public static testmethod void testBulkItemDelete(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items

        insert Order1;

        List<Item__c> list1 = new List<Item__c>();

        Item__c item1 = new Item__C(Price__c = 10, weight__c = 1, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 25, weight__c = 2, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c itemA = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c itemB = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c itemC = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c itemD = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        list1.add(item1);

        list1.add(item2);

        list1.add(item3);

        list1.add(itemA);

        list1.add(itemB);

        list1.add(itemC);

        list1.add(itemD);

        insert list1;

        // Seven items are now in the shipping invoice.

        // The following deletes four of them.

        List<Item__c> list2 = new List<Item__c>();

        list2.add(itemA);

        list2.add(itemB);

        list2.add(itemC);

        list2.add(itemD);

        delete list2;

```


Apex Reference Guide Shipping Invoice Example

```
        // Retrieve the order and verify the deletion

        order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,

              grandtotal__c, shippingdiscount__c

              FROM Shipping_Invoice__C

              WHERE Id = :order1.Id];

        System.assert(order1.subtotal__c == 75,

                 'Order subtotal was not $75, but was '+ order1.subtotal__c);

        System.assert(order1.tax__c == 6.9375,

                 'Order tax was not $6.9375, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 4.50,

                 'Order shipping was not $4.50, but was ' + order1.shipping__c);

        System.assert(order1.totalweight__c == 6.00,

                 'Order weight was not 6 but was ' + order1.totalweight__c);

        System.assert(order1.grandtotal__c == 86.4375,

                 'Order grand total was not $86.4375 but was '

                 + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == 0,

                 'Order shipping discount was not $0 but was '

                 + order1.shippingdiscount__c);

      }

      // Testing free shipping

      public static testmethod void testFreeShipping(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items.

        insert Order1;

        List<Item__c> list1 = new List<Item__c>();

        Item__c item1 = new Item__C(Price__c = 10, weight__c = 1,

                       quantity__c = 1, Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 25, weight__c = 2,

                       quantity__c = 1, Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 40, weight__c = 3,

                       quantity__c = 1, Shipping_Invoice__C = order1.id);

        list1.add(item1);

        list1.add(item2);

        list1.add(item3);

        insert list1;

        // Retrieve the order and verify free shipping not applicable

        order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,

              grandtotal__c, shippingdiscount__c

              FROM Shipping_Invoice__C

              WHERE Id = :order1.Id];

        // Free shipping not available on $75 orders

        System.assert(order1.subtotal__c == 75,

```


Apex Reference Guide Shipping Invoice Example

```
                 'Order subtotal was not $75, but was '+ order1.subtotal__c);

        System.assert(order1.tax__c == 6.9375,

                 'Order tax was not $6.9375, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 4.50,

                 'Order shipping was not $4.50, but was ' + order1.shipping__c);

        System.assert(order1.totalweight__c == 6.00,

                 'Order weight was not 6 but was ' + order1.totalweight__c);

        System.assert(order1.grandtotal__c == 86.4375,

                 'Order grand total was not $86.4375 but was '

                 + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == 0,

                 'Order shipping discount was not $0 but was '

                 + order1.shippingdiscount__c);

        // Add items to increase subtotal

        item1 = new Item__C(Price__c = 25, weight__c = 20, quantity__c = 1,

                    Shipping_Invoice__C = order1.id);

        insert item1;

        // Retrieve the order and verify free shipping is applicable

        order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,

              grandtotal__c, shippingdiscount__c

              FROM Shipping_Invoice__C

              WHERE Id = :order1.Id];

        // Order total is now at $100, so free shipping should be enabled

        System.assert(order1.subtotal__c == 100,

                 'Order subtotal was not $100, but was '+ order1.subtotal__c);

        System.assert(order1.tax__c == 9.25,

                 'Order tax was not $9.25, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 19.50,

                 'Order shipping was not $19.50, but was '

                 + order1.shipping__c);

        System.assert(order1.totalweight__c == 26.00,

                 'Order weight was not 26 but was ' + order1.totalweight__c);

        System.assert(order1.grandtotal__c == 109.25,

                 'Order grand total was not $86.4375 but was '

                 + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == -19.50,

                 'Order shipping discount was not -$19.50 but was '

                 + order1.shippingdiscount__c);

      }

      // Negative testing for inserting bad input

      public static testmethod void testNegativeTests(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items.

```


### Apex Reference Guide Reserved Keywords

```
        insert Order1;

        Item__c item1 = new Item__C(Price__c = -10, weight__c = 1, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 25, weight__c = -2, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = -1,

                         Shipping_Invoice__C = order1.id);

        Item__c item4 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = 0,

                         Shipping_Invoice__C = order1.id);

        try{

           insert item1;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Price must be non-negative'),

                  'Price was negative but was not caught');

        }

        try{

           insert item2;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Weight must be non-negative'),

                  'Weight was negative but was not caught');

        }

        try{

           insert item3;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Quantity must be positive'),

                  'Quantity was negative but was not caught');

        }

        try{

           insert item4;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Quantity must be positive'),

                  'Quantity was zero but was not caught');

        }

      }

   }

### Reserved Keywords

```

These words can be used only as keywords.


Apex Reference Guide Reserved Keywords

**Table 3: Reserved Keywords**

abstract false package

activate final parallel

and finally pragma

any float private

array for protected

as from public

asc global retrieve

autonomous goto return

begin group rollback

bigdecimal having select

blob hint set

boolean if short

break implements sObject

bulk import sort

by in static

byte inner string

case insert super

cast instanceof switch

catch int synchronized

char integer system

class interface testmethod

collect into then

commit join this

const like throw

continue limit time

currency list transaction

date long trigger

datetime loop true

decimal map try

default merge undelete

delete new update

desc not upsert

do null using

double nulls virtual

else number void


### Apex Reference Guide Documentation Typographical Conventions

end object webservice

enum of when

exception on where

exit or while

export outer

extends override

These words are special types of keywords that aren't reserved words and can be used as identifiers.

**•** after

**•** before

**•** count

**•** excludes

**•** first

**•** includes

**•** last

**•** order

**•** sharing

**•** with

### Documentation Typographical Conventions

Apex and Visualforce documentation uses these typographical conventions.

**Convention** **Description**

```
Courier font

Italics

```

In descriptions of syntax, a monospace font indicates items that you should type as shown,
except for brackets. For example:

```
Public class HelloWorld

```

In descriptions of syntax, italics represent variables. You supply the actual value. In the following
example, three values must be supplied: _`datatype variable_name`_ [ = _`value`_ ];

If the syntax is bold and italic, the text represents a code element that needs a value supplied
by you, such as a class name or variable value:

```
 public static class YourClassHere { ... }

```

**`Bold Courier font`** In code samples and syntax descriptions, a bold courier font emphasizes a portion of the code
or syntax.

< >

In descriptions of syntax, less-than and greater-than symbols (< >) are typed exactly as shown.


Apex Reference Guide Documentation Typographical Conventions

**Convention** **Description**

```
                     <apex:column value="{!contact.Name}"/>

                     <apex:column value="{!contact.MailingCity}"/>

                     <apex:column value="{!contact.Phone}"/>

                    </apex:pageBlockTable>

```

{ }

[ ]

|

In descriptions of syntax, braces ({ }) are typed exactly as shown.

```
<apex:page>

   Hello {!$User.FirstName}!

</apex:page>

```

In descriptions of syntax, anything included in brackets is optional. In the following example,
specifying _**`value`**_ is optional:

```
 data_type variable_name [ = value ];

```

In descriptions of syntax, the pipe sign means “or”. You can do one of the following (not all).
In the following example, you can create a new unpopulated set in one of two ways, or you
can populate the set:

```
Set< data_type > set_name

  [= new Set< data_type >();] |

  [= new Set< data_type { value [, value2 . . .] };] |

  ;

```

