      Auth.SessionManagement.getLightningLoginEligibility(id);

   if (eligibility == Auth.LightningLoginEligibility.ELIGIBLE) {

      // success

   }

##### getQrCode()

```

Returns a map containing a URL to a quick response (QR) code and a time-based one-time password (TOTP) shared secret to configure
authenticator apps or devices for multi-factor authentication (MFA).

Signature

```
   public static Map<String, String> getQrCode()

```

Return Value

Type: Map<String, String>

Usage

The QR code encodes the returned secret as well as the current user's username. The keys are `qrCodeUrl` and `secret` . Calling this
method does not change any state for the user, nor does it read any state from the user. This method returns a brand new secret every
time it is called, does not save that secret anywhere, and does not validate the TOTP token. The admin must explicitly save the values
for the user after verifying a TOTP token with the secret.

The `secret` is a base32-encoded string of a 20-byte shared key.


Apex Reference Guide SessionManagement Class

Example

The following is an example of how to request the QR code.

```
   public String getGetQRCode() {

        return getQRCode();

      }

      public String getQRCode() {

        Map<String, String> codeResult = Auth.SessionManagement.getQrCode();

        String result = 'URL: '+codeResult.get('qrCodeUrl') + ' SECRET: ' +

   codeResult.get('secret');

        return result;

      }

```

The following is an example of a returned map.

```
   {qrCodeUrl=https://www.salesforce.com/secur/qrCode?w=200&h=200&t=tf&u=user%0000000000.com&s=AAAAA7B5BBBB5AAAAAAA66BBBB,

       secret=AAAAA7B5AAAAAA5BBBBBBBBB66AAA}

##### getRequiredSessionLevelForProfile(profileId)

```

Indicates the required login security session level for the given profile.

Signature

```
   public static Auth.SessionLevel getRequiredSessionLevelForProfile(String profileId)

```

Parameters

```
   profileId
```

Type: String

The 15-character profile ID.

Return Value

Type: Auth.SessionLevel

The session security level required at login for the profile with the ID _`profileId`_ . You can customize the assignment of each level in
Session Settings. For example, you can set the High Assurance level to apply only to users who authenticated with multi-factor
authentication (MFA) or through a specific identity provider.

##### ignoreForConcurrentSessionLimit(sessions)

This method is reserved for internal Salesforce use.

Signature

```
   public static Map<String,String> ignoreForConcurrentSessionLimit(Object sessions)

```


Apex Reference Guide SessionManagement Class

Parameters

```
   sessions
```

Type: Object

Return Value

Type: Map<String, String>

##### inOrgNetworkRange(ipAddress)

Indicates whether the given IP address is within the organization's trusted IP range according to the organization's Network Access
settings.

Signature

```
   public static Boolean inOrgNetworkRange( String ipAddress )

```

Parameters

```
   ipAddress
```

Type: String

The IP address to validate.

Return Value

Type: Boolean

Usage

If a trusted IP range is not defined, this returns `false`, and throws an exception if the IP address is not valid.

**Trusted IP Range Exists?** **User is in the Trusted IP Range?** **Return Value**

Yes Yes `true`

Yes No `false`

No N/A `false`

##### isIpAllowedForProfile(profileId, ipAddress)

Indicates whether the given IP address is within the trusted IP range for the given profile.

Signature

```
   public static Boolean isIpAllowedForProfile(String profileId, String ipAddress)

```


Apex Reference Guide SessionManagement Class

Parameters

```
   profileId
```

Type: String

The 15-character alphanumeric string for the current user’s profile ID.

```
   ipAddress
```

Type: String

The IP address to validate.

Return Value

Type: Boolean

Usage

If a trusted IP range is not defined, this returns `true`, and throws an exception if the IP address is not valid or if the profile ID is not valid.

**Trusted IP Range Exists?** **User is in the Trusted IP Range?** **Return Value**

Yes Yes `true`

Yes No `false`

No N/A `true`

##### setSessionLevel(level)

Sets the user's current session security level.

Signature

```
   public static Void setSessionLevel(Auth.SessionLevel level)

```

Parameters

```
   level
```

Type: Auth.SessionLevel

The session security level to assign to the user. The meaning of each level can be customized in the Session Settings for each
organization, such as setting the High Assurance level to apply only to users who authenticated with multi-factor authentication
(MFA) or through a specific identity provider.

Return Value

Type: Void

Usage

This setting affects the session level of all sessions associated with the current session, such as Visualforce or UI access.

If you create an Apex test method that calls this method, the test fails with an error such as, “Unexpected Exception: Current session
unavailable." An error occurs because there isn’t a session in the context through which the test is being run.


Apex Reference Guide SessionManagement Class

Example

The following is an example class for setting the session level.

```
   public class RaiseSessionLevel{

      public void setLevelHigh() {

        Auth.SessionManagement.setSessionLevel(Auth.SessionLevel.HIGH_ASSURANCE);

      }

      public void setLevelStandard() {

        Auth.SessionManagement.setSessionLevel(Auth.SessionLevel.STANDARD);

      }

   }

##### validateTotpTokenForKey(sharedKey, totpCode) Deprecated. Use validateTotpTokenForKey(totpSharedKey, totpCode, description) instead.

```

Signature

```
   public static Boolean validateTotpTokenForKey( String sharedKey, String totpCode )

```

Parameters

```
   sharedKey
```

Type: String

The shared (secret) key. The _`sharedKey`_ must be a base32-encoded string of a 20-byte shared key.

```
   totpCode
```

Type: String

The time-based one-time password (TOTP) code to validate.

Return Value

Type: Boolean

Usage

If the key is invalid or doesn’t exist, this method throws an invalid parameter value exception or a no data found exception, respectively.
If the current user exceeds the maximum of 10 token validation attempts, this method throws a security exception.

##### validateTotpTokenForKey(totpSharedKey, totpCode, description)

Indicates whether a time-based one-time password (TOTP) code (token) is valid for the given shared key.

Signature

```
   public static Boolean validateTotpTokenForKey(String totpSharedKey, String totpCode,

   String description)

```


Apex Reference Guide SessionManagement Class

Parameters

```
   totpSharedKey
```

Type: String

The shared (secret) key. The _`totpSharedKey`_ must be a base32-encoded string of a 20-byte shared key.

```
   totpCode
```

Type: String

The time-based one-time password (TOTP) code to validate.

```
   description
```

Type: String

The custom description that describes the activity requiring identity verification; for example, “Complete purchase and check out”.
In the Setup user interface, this text is shown in the Activity Message column of Identity Verification History. The _`description`_
must be 128 characters or fewer. If you provide a value that’s longer, it’s truncated to 128 characters.

Return Value

Type: Boolean

Usage

If the key is invalid or doesn’t exist, this method throws an invalid parameter value exception or a no data found exception, respectively.
If the current user exceeds the maximum of 10 token validation attempts, this method throws a security exception.

##### validateTotpTokenForUser(totpCode) Deprecated. Use validateTotpTokenForUser(totpCode, description) instead.

Signature

```
   public static Boolean validateTotpTokenForUser( String totpCode )

```

Parameters

```
   totpCode
```

Type: String

The time-based one-time password (TOTP) code to validate.

Return Value

Type: Boolean

Usage

If the current user does not have a TOTP code, this method throws an exception. If the current user has attempted too many validations,
this method throws an exception.

##### validateTotpTokenForUser(totpCode, description)

Indicates whether a time-based one-time password (TOTP) code (token) is valid for the current user.


Apex Reference Guide SessionManagement Class

Signature

```
   public static Boolean validateTotpTokenForUser(String totpCode, String description)

```

Parameters

```
   totpCode
```

Type: String

The time-based one-time password (TOTP) code to validate.

```
   description
```

Type: String

The custom description that describes the activity requiring identity verification; for example, “Complete purchase and check out”.
This text appears to users when they verify their identity in Salesforce and, if they use Salesforce Authenticator version 2 or later, in
the Salesforce Authenticator mobile app. In addition, in the Setup user interface, this text is shown in the Activity Message column
of Identity Verification History. The _`description`_ must be 128 characters or fewer. If you provide a value that’s longer, it’s
truncated to 128 characters.

Return Value

Type: Boolean

Usage

If the current user does not have a TOTP code, or if the current user has attempted too many validations, this method throws an exception.

##### verifyDeviceFlow(userCode, startUrl)

Verifies the user code entered during the device authentication flow and redirects users to the OAuth approval page. If users aren’t
logged in, they must log in. After successful login, users are prompted to allow the device to access Salesforce data.

Signature

```
   public static System.PageReference verifyDeviceFlow(String userCode, String startUrl)

```

Parameters

```
   userCode
```

Type: String

Human-readable user code provided to the user by Salesforce. The user must enter this code at the verification URL to approve
device access to Salesforce data.

```
   startURL
```

Type: String

The URL for the page that the user is redirected to after successful login and approval of the device to access Salesforce data. If you
don’t specify a start URL, the user is redirected to the Home page.

Return Value

Type:System.PageReference


### Apex Reference Guide SessionLevel Enum

Usage

Include this method in the Apex controller when creating a custom Visualforce User Code Verification page for the OAuth 2.0 device
authentication flow. This method verifies the user code, prompts the user to log in as needed, and prompts the user to allow the device
access to Salesforce data. Upon successful verification and authentication, the user is redirected to the page defined by the start URL.

### SessionLevel Enum

An `Auth.SessionLevel` enum value is used by the `SessionManagement.setSessionLevel` method.

Namespace

Auth

Enum Values

**Value** **Description**

`LOW` The user’s security level for the current session meets the lowest requirements.

Note: This low level is not available, nor used, in the Salesforce UI. User
sessions through the Salesforce UI are either standard or high assurance. You
can set this level using the API, but users assigned this level will experience
unpredictable and reduced functionality in their Salesforce organization.

`STANDARD` The user’s security level for the current session meets the Standard requirements
set in the current organization Session Security Levels.

`HIGH_ASSURANCE` The user’s security level for the current session meets the High Assurance
requirements set in the current organization Session Security Levels.

Usage

With session-level security, you control user access to features that support it, such as connected apps and reporting. For example, you
can customize an organization’s Session Settings to require users to log in with multi-factor authentication (MFA) to get a High Assurance
session. Then, you can restrict access to a specific connected app by requiring a High Assurance session level in the settings for the
connected app.

### TokenValidationResult Class

Contains methods that describe the result of the token validation performed by a token exchange handler using the
`validateIncomingToken` method in the `Auth.Oauth2TokenExchangeHandler` class during the OAuth 2.0 token
exchange flow.

Namespace

Auth


Apex Reference Guide TokenValidationResult Class

Usage

For a full example implementation that shows how to get information from the `TokenValidationResult` [class, see OAuth 2.0](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/token_exchange_handler.htm)
[Token Exchange Handler Examples.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/token_exchange_handler.htm)

Example

Here’s is an example of the `Auth.TokenValidationResult` class.

```
   global class TokenValidationResult {

      global TokenValidationResult(Boolean valid) { this.isValid = valid; }

      global TokenValidationResult(Boolean isValid, Object data, Auth.UserData userData,

        String token, Auth.OAuth2TokenExchangeType tokenType, String customErrorMsg) {

        this.isValid = isValid;

        this.data = data;

        this.userData = userData;

        this.token = token;

        this.tokenType = tokenType;

        this.customErrorMsg = customErrorMsg;

      }

      global Boolean isValid;

      global Object data;

      global Auth.UserData userData;

      global String token;

      global Auth.OAuth2TokenExchangeType tokenType; //Enum

      global String customErrorMsg; //Custom error message that’s returned to the client if

    token validation fails

      global Boolean isValid(){

        return isValid;

      }

      global Object getData(){

        return data;

      }

      global Auth.UserData getUserData(){

        return userData;

      }

      global String getToken(){

        return token;

      }

      global OAuth2TokenExchangeType getTokenType(){

        return tokenType;

      }

      global String getCustomErrorMessage(){

        return customErrorMsg;

      }

   }

```


Apex Reference Guide TokenValidationResult Class

IN THIS SECTION:

#### TokenValidationResult Constructors

TokenValidationResult Properties

TokenValidationResult Methods

#### TokenValidationResult Constructors The following are constructors for TokenValidationResult .

IN THIS SECTION:

##### TokenValidationResult(isValid, data, userData, token, tokenType, customErrorMsg)

Creates an instance of the `Auth.TokenValidationResult` class to describe the result of token validation performed during
the OAuth 2.0 token exchange flow.

TokenValidationResult(valid)
Creates an instance of the `Auth.TokenValidationResult` class to describe a valid token validation result during the OAuth
2.0 token exchange flow.

##### **`TokenValidationResult(isValid, data, userData, token, tokenType,`**

```
  customErrorMsg)

```

Creates an instance of the `Auth.TokenValidationResult` class to describe the result of token validation performed during
the OAuth 2.0 token exchange flow.

Signature

```
   public TokenValidationResult(Boolean isValid, Object data, Auth.UserData userData,

   String token, Auth.OAuth2TokenExchangeType tokenType, String customErrorMsg)

```

Parameters

```
   isValid
```

Type: Boolean

If `true`, the token is valid.

```
   data
```

Type: Object

Stores custom data that isn’t stored in `userData` .

```
   userData
```

[Type: Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_UserData.htm)

Stores information about a Salesforce user.

```
   token
```

Type: String

The token from the external identity provider.

```
   tokenType
```

[Type: Auth.OAuth2TokenExchangeType](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)


Apex Reference Guide TokenValidationResult Class

The type of token from the external identity provider.

##### _`customErrorMsg`_

Type: String

A custom error message that’s returned if the token validation fails.

##### **`TokenValidationResult(valid)`**

Creates an instance of the `Auth.TokenValidationResult` class to describe a valid token validation result during the OAuth
2.0 token exchange flow.

Signature

```
   public TokenValidationResult(Boolean valid)

```

Parameters

```
   valid
```

Type: Boolean

Indicates a valid token validation result.

#### TokenValidationResult Properties

##### The following are properties for TokenValidationResult .

IN THIS SECTION:

##### customErrorMsg

A custom error message that’s returned if token validation fails.

data
Contains information about the user that isn’t stored in the `Auth.UserData` class, such as information obtained via callouts to
the external identity provider.

isValid
Indicates whether the token is valid or not, based on the custom validation logic in your token exchange handler.

token
The token from the external identity provider.

tokenType
The type of token from the external identity provider. It can be an access token, refresh token, ID token, SAML 2.0 assertion, or a JSON
Web Token (JWT).

userData
Information about the user that’s obtained from the identity provider’s token.

##### **`customErrorMsg`**

A custom error message that’s returned if token validation fails.


Apex Reference Guide TokenValidationResult Class

Signature

```
   public String customErrorMsg {get; set;}

```

Property Value

Type: String

##### **`data`**

Contains information about the user that isn’t stored in the `Auth.UserData` class, such as information obtained via callouts to the
external identity provider.

Signature

```
   public Object data {get; set;}

```

Property Value

Type: Object

##### **`isValid`**

Indicates whether the token is valid or not, based on the custom validation logic in your token exchange handler.

Signature

```
   public Boolean isValid {get; set;}

```

Property Value

Type: Boolean

##### **`token`**

The token from the external identity provider.

Signature

```
   public String token {get; set;}

```

Property Value

Type: String

##### **`tokenType`**

The type of token from the external identity provider. It can be an access token, refresh token, ID token, SAML 2.0 assertion, or a JSON
Web Token (JWT).


Apex Reference Guide TokenValidationResult Class

Signature

```
   public Auth.OAuth2TokenExchangeType tokenType {get; set;}

```

Property Value

[Type: Auth.OAuth2TokenExchangeType](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)

##### **`userData`**

Information about the user that’s obtained from the identity provider’s token.

Signature

```
   public Auth.UserData userData {get; set;}

```

Property Value

[Type: Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_UserData.htm)

#### TokenValidationResult Methods The following are methods for TokenValidationResult .

IN THIS SECTION:

##### getCustomErrorMessage()

Retrieves the `CustomErrorMsg` that’s returned when token validation fails.

getData()
##### Retrieves data from the identity provider token. This data can include custom data that isn’t stored in the userData property.

getToken()
Retrieves the token that was passed from the external identity provider.

getTokenType()
Retrieves the type of token that was passed from the external identity provider.

getUserData()
Retrieves information about the user. The user information can be obtained from the identity provider’s token or from callouts to
the identity provider, if applicable.

isValid
Indicates whether the token is valid or not, based on the custom validation logic in your token exchange handler.

##### **`getCustomErrorMessage()`**

Retrieves the `CustomErrorMsg` that’s returned when token validation fails.

Signature

```
   public String getCustomErrorMessage()

```


Apex Reference Guide TokenValidationResult Class

Return Value

Type: String

##### **`getData()`**

Retrieves data from the identity provider token. This data can include custom data that isn’t stored in the `userData` property.

Signature

```
   public Object getData()

```

Return Value

Type: Object

##### **`getToken()`**

Retrieves the token that was passed from the external identity provider.

Signature

```
   public String getToken()

```

Return Value

Type: String

##### **`getTokenType()`**

Retrieves the type of token that was passed from the external identity provider.

Signature

```
   public Auth.OAuth2TokenExchangeType getTokenType()

```

Return Value

[Type: Auth.OAuth2TokenExchangeType](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)

##### **`getUserData()`**

Retrieves information about the user. The user information can be obtained from the identity provider’s token or from callouts to the
identity provider, if applicable.

Signature

```
   public Auth.UserData getUserData()

```


### Apex Reference Guide UserData Class

Return Value

[Type: Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_UserData.htm)

##### **`isValid`**

Indicates whether the token is valid or not, based on the custom validation logic in your token exchange handler.

Signature

```
   public Boolean isValid {get; set;}

```

Property Value

Type: Boolean

### UserData Class

Stores user information for authentication provider registration handlers, including handlers that implement the
`Auth.RegistrationHandler` interface and handlers built using Flow Builder.

Namespace

Auth

Usage

For more information about using this class with the `Auth.RegistrationHandler` [interface, see Storing User Information and](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_auth_plugin.htm#apex_auth_plugin_part2)
[Getting Access Tokens in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_auth_plugin.htm#apex_auth_plugin_part2) `RegistrationHandler` Interface documentation.

[For more information about using this class as an Apex-defined variable in a user registration flow, see Example: Authentication Provider](https://help.salesforce.com/s/articleView?id=xcloud.sso_flow_registration_handler_example.htm&language=en_US)
[Registration Handler Flow in Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.sso_flow_registration_handler_example.htm&language=en_US)

IN THIS SECTION:

#### UserData Constructors

UserData Properties

#### UserData Constructors

### The following are constructors for UserData .

IN THIS SECTION:

UserData(identifier, firstName, lastName, fullName, email, link, userName, locale, provider, siteLoginUrl, attributeMap)
Creates a new instance of the `Auth.UserData` class using the specified arguments.

UserData(identifier, firstName, lastName, fullName, email, link, username, locale, provider, siteLoginUrl, attributeMap, idToken,
userInfoJSONString)
Creates an instance of the Auth.UserData class that includes the ID token and user info response from the identity provider, if returned
during single sign-on.


Apex Reference Guide UserData Class

##### UserData(identifier, firstName, lastName, fullName, email, link, userName, locale, provider,

siteLoginUrl, attributeMap)

Creates a new instance of the `Auth.UserData` class using the specified arguments.

Signature

```
   public UserData(String identifier, String firstName, String lastName, String fullName,

   String email, String link, String userName, String locale, String provider, String

   siteLoginUrl, Map<String,String> attributeMap)

```

Parameters

```
   identifier
```

Type: String

An identifier from the third party for the authenticated user, such as the Facebook user number or the Salesforce user ID.

```
   firstName
```

Type: String

The first name of the authenticated user, according to the third party.

```
   lastName
```

Type: String

The last name of the authenticated user, according to the third party.

```
   fullName
```

Type: String

The full name of the authenticated user, according to the third party.

```
   email
```

Type: String

The email address of the authenticated user, according to the third party.

```
   link
```

Type: String

A stable link for the authenticated user such as `https://www.facebook.com/MyUsername` .

```
   userName
```

Type: String

The username of the authenticated user in the third party.

```
   locale
```

Type: String

The standard locale string for the authenticated user.

```
   provider
```

Type: String

The service used to log in, such as Facebook or Janrain.

```
   siteLoginUrl
```

Type: String

The site login page URL passed in if used with a site; `null` otherwise.


Apex Reference Guide UserData Class

```
   attributeMap
```

Type: Map<String, String>

A map of data from the third party, in case the handler has to access non-standard values. For example, when using Janrain as a
provider, the fields Janrain returns in its `accessCredentials` dictionary are placed into the `attributeMap` . These fields
vary by provider.

##### **`UserData(identifier, firstName, lastName, fullName, email, link, username,`**

```
  locale, provider, siteLoginUrl, attributeMap, idToken, userInfoJSONString)

```

Creates an instance of the Auth.UserData class that includes the ID token and user info response from the identity provider, if returned
during single sign-on.

Signature

```
   public UserData(String identifier, String firstName, String lastName, String fullName,

   String email, String link, String username, String locale, String provider, String

   siteLoginUrl, Map<String,String> attributeMap, String idToken, String userInfoJSONString)

```

Parameters

```
   identifier
```

Type: String

An identifier from the third party for the authenticated user, such as the Facebook user number or the Salesforce user ID.

```
   firstName
```

Type: String

The first name of the authenticated user, according to the third party.

```
   lastName
```

Type: String

The last name of the authenticated user, according to the third party.

```
   fullName
```

Type: String

The full name of the authenticated user, according to the third party.

```
   email
```

Type: String

The email address of the authenticated user, according to the third party.

```
   link
```

Type: String

A stable link for the authenticated user such as `https://www.facebook.com/MyUsername` .

```
   username
```

Type: String

The username of the authenticated user in the third party.

```
   locale
```

Type: String


Apex Reference Guide UserData Class

The standard locale string for the authenticated user.

```
   provider
```

Type: String

The service used to log in, such as Facebook or Janrain.

```
   siteLoginUrl
```

Type: String

The site login page URL passed in if used with a site; `null` otherwise.

```
   attributeMap
```

Type: Map<String, String>

A map of data from the third party, in case the handler has to access non-standard values. For example, when using Janrain as a
provider, the fields Janrain returns in its `accessCredentials` dictionary are placed into the _`attributeMap`_ . These fields
vary by provider.

```
   idToken
```

Type: String

If provided by the third party, the ID token, formatted as an encoded JWT. The ID token contains claims with information about the
authenticated user.

```
   userInfoJSONString
```

Type: String

If provided by the third party, the user info response, formatted as a JSON object that has been serialized into a string.

#### UserData Properties The following are properties for UserData .

IN THIS SECTION:

identifier
An identifier from the third party for the authenticated user, such as the Facebook user number or the Salesforce user ID.

firstName
The first name of the authenticated user, according to the third party.

lastName
The last name of the authenticated user, according to the third party.

fullName
The full name of the authenticated user, according to the third party.

email
The email address of the authenticated user, according to the third party.

link
A stable link for the authenticated user such as `https://www.facebook.com/MyUsername` .

username
The username of the authenticated user in the third party.

locale
The standard locale string for the authenticated user.


Apex Reference Guide UserData Class

provider
The service used to log in, such as Facebook or Janrain.

siteLoginUrl
The site login page URL passed in if used with a site; `null` otherwise.

attributeMap
A map of data from the third party, in case the handler has to access non-standard values. For example, when using Janrain as a
provider, the fields Janrain returns in its `accessCredentials` dictionary are placed into the `attributeMap` . These fields
vary by provider.

idToken
If provided, the ID token from the third party, formatted as an encoded JWT. The ID token contains claims with information about
the authenticated user.

userInfoJSONString
If provided, the user info response from the third party. The user info response is a JSON object containing user attributes. When
used in this property, the JSON object is serialized into a string.

idTokenJSONString
If provided, the ID token from the third party. The ID token is formatted as a JSON Web Token (JWT) containing claims with information
about the user. When used in this property, the ID token is serialized into a string.

##### identifier

An identifier from the third party for the authenticated user, such as the Facebook user number or the Salesforce user ID.

Signature

```
   public String identifier {get; set;}

```

Property Value

Type: String

##### firstName

The first name of the authenticated user, according to the third party.

Signature

```
   public String firstName {get; set;}

```

Property Value

Type: String

##### lastName

The last name of the authenticated user, according to the third party.


Apex Reference Guide UserData Class

Signature

```
   public String lastName {get; set;}

```

Property Value

Type: String

##### fullName

The full name of the authenticated user, according to the third party.

Signature

```
   public String fullName {get; set;}

```

Property Value

Type: String

##### email

The email address of the authenticated user, according to the third party.

Signature

```
   public String email {get; set;}

```

Property Value

Type: String

##### link

A stable link for the authenticated user such as `https://www.facebook.com/MyUsername` .

Signature

```
   public String link {get; set;}

```

Property Value

Type: String

##### username

The username of the authenticated user in the third party.

Signature

```
   public String username {get; set;}

```


Apex Reference Guide UserData Class

Property Value

Type: String

##### locale

The standard locale string for the authenticated user.

Signature

```
   public String locale {get; set;}

```

Property Value

Type: String

##### provider

The service used to log in, such as Facebook or Janrain.

Signature

```
   public String provider {get; set;}

```

Property Value

Type: String

##### siteLoginUrl

The site login page URL passed in if used with a site; `null` otherwise.

Signature

```
   public String siteLoginUrl {get; set;}

```

Property Value

Type: String

##### attributeMap

A map of data from the third party, in case the handler has to access non-standard values. For example, when using Janrain as a provider,
##### the fields Janrain returns in its accessCredentials dictionary are placed into the attributeMap . These fields vary by provider.

Signature

```
   public Map<String, String> attributeMap {get; set;}

```


### Apex Reference Guide VerificationAction Enum

Property Value

Type: Map<String, String>

##### **`idToken`**

If provided, the ID token from the third party, formatted as an encoded JWT. The ID token contains claims with information about the
authenticated user.

Signature

```
   public String idToken {get; set;}

```

Property Value

Type: String

##### **`userInfoJSONString`**

If provided, the user info response from the third party. The user info response is a JSON object containing user attributes. When used
in this property, the JSON object is serialized into a string.

Signature

```
   public String userInfoJSONString {get; set;}

```

Property Value

Type: String

##### **`idTokenJSONString`**

If provided, the ID token from the third party. The ID token is formatted as a JSON Web Token (JWT) containing claims with information
about the user. When used in this property, the ID token is serialized into a string.

Signature

```
   public String idTokenJSONString {get; set;}

```

Property Value

Type: String

### VerificationAction Enum

Indicates the method that you use to send a one-time password (OTP) to a user during the headless passwordless login flow.

Usage

Use this enum to specify the user's method of receiving a one-time password when you implement the
`Auth.HeadlessUserDiscoveryHandler` interface.


### Apex Reference Guide VerificationMethod Enum

Enum Values

The following are the values of the `Auth.VerificationAction` enum.

**Value** **Description**

`EMAIL` Indicates that the user is verifying their identity with email.

`SMS` Indicates that the user is verifying their identity with SMS.

### VerificationMethod Enum

Contains the different ways users can identify themselves when logging in. You can use it to implement mobile-centric passwordless
login pages and to self-register (and deregister) verification methods.

Usage

The enum value is an argument in `System.Site.passwordlessLogin`,
`System.UserManagement.registerVerificationMethod`, and
`System.UserManagement.deregisterVerificationMethod` on page 4398 methods. The value indicates the method
used to verify a user’s identity.

Enum Values

The following are the values of the `Auth.VerificationMethod` enum.

**Value** **Description**

`BUILT_IN_AUTHENTICATOR` Identity verified with a built-in authenticator.

`EMAIL` Identity verified with a verification code sent in an email message.

`PASSWORD` Identity verified with a password.

`SALESFORCE_AUTHENTICATOR` Identity verified by Salesforce Authenticator.

`SECURITY_KEY` Identity verified by a WebAuthn-compatible physical security key. Includes all security
keys registered or used after Summer ’22.

`SMS` Identity verified with a verification code sent via SMS message.

`TOTP` Identity verified with a time-based one-time password (TOTP).

`U2F` Identity verified by a U2F physical security key, such as a YubiKey.

Note: For U2F security keys registered or used after Summer ’22, use
SECURITY_KEY instead.

### VerificationPolicy Enum

The `Auth.VerificationPolicy` enum contains an identity verification policy value used by the
`SessionManagement.generateVerificationUrl` method.


### Apex Reference Guide VerificationResult Class

Usage

The enum value is an argument in the `SessionManagement.generateVerificationUrl` method. The value indicates the
session security policy required to initiate identity verification for the user’s session.

Enum Values

The `Auth.VerificationPolicy` enum has this value.

**Value** **Description**

`HIGH_ASSURANCE` The security level for the user’s current session must be High Assurance.

### VerificationResult Class

Contains the result of a verification challenge that you invoke when you create your own Verify page. The challenge can be initiated by
either the `System.UserManagement.verifyPasswordlessLogin` or
`System.UserManagement.verifySelfRegistration` method.

Namespace

Auth

Usage

When users sign up for or log in to your Experience Cloud site with an email address or phone number, Salesforce sends them a verification
code. At the same time, Salesforce generates the Verify page for users to enter the code to verify their identity. You can replace the
Salesforce-generated Verify page with one that you create with Visualforce. Then invoke the verification challenge and, if the verification
code is entered correctly, log in the user. For sign-up, you use the `System.UserManagement.verifySelfRegistration`
method. For passwordless login, you use the System.UserManagement.verifyPasswordlessLogin method. The methods return the
verification result, which contains the message displayed as a result of the challenge. This message also indicates whether the challenge
is successful and where to direct the user when the verification code is entered correctly.

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

```

IN THIS SECTION:

VerificationResult Constructor

VerificationResult Properties


Apex Reference Guide VerificationResult Class

VerificationResult Method

#### VerificationResult Constructor VerificationResult has the following constructor.

IN THIS SECTION:

##### VerificationResult(redirect, success, message)
#### Creates an instance of the VerificationResult class that contains the verification result from

`System.UserManagement.verifySelfRegistration` .

##### VerificationResult(redirect, success, message)

#### Creates an instance of the VerificationResult class that contains the verification result from

`System.UserManagement.verifySelfRegistration` .

Signature

```
   public VerificationResult(System.PageReference redirect, Boolean success, String message)

```

Parameters

```
   redirect
```

Type: System.PageReferenceSystem.PageReference

Where user is directed upon successful verification.

```
   success
```

Type: Boolean

Indicates whether verification succeeded.

```
   message
```

Type: String

Message that displays as a result of a verification challenge.

#### VerificationResult Properties The following are properties for VerificationResult .

IN THIS SECTION:

message
Message that displays as a result of a verification challenge. `Token is valid` if the identity verification is successful. Other
values are `FAILURE`, `PENDING`, `RATE_LIMITED`, or `FAILURE_REPORT` .

redirect
Where the user is directed after entering the verification code successfully, for example, the Experience Cloud site’s home page or
location specified by the start URL.

success
The verification challenge is successful.


Apex Reference Guide VerificationResult Class

##### message

Message that displays as a result of a verification challenge. `Token is valid` if the identity verification is successful. Other values
are `FAILURE`, `PENDING`, `RATE_LIMITED`, or `FAILURE_REPORT` .

Signature

```
   public String message {get; set;}

```

Property Value

Type: String

##### redirect

Where the user is directed after entering the verification code successfully, for example, the Experience Cloud site’s home page or location
specified by the start URL.

Signature

```
   public System.PageReference redirect {get; set;}

```

Property Value

Type: System.PageReferenceSystem.PageReference

##### success

The verification challenge is successful.

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

#### VerificationResult Method VerificationResult has the following method.

IN THIS SECTION:

##### clone()

Duplicates the Auth.VerificationResult object.

##### clone()

Duplicates the Auth.VerificationResult object.


### Apex Reference Guide Auth Exceptions

Signature

```
   public Object clone()

```

Return Value

Type: VerificationResult

### Auth Exceptions The Auth namespace contains some exception classes.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions.

### The Auth namespace contains the following exception.

**Exception** **Description**

```
Auth.

AuthProviderPluginException

Auth.ConnectedAppPlugin

Exception

Auth.DiscoveryCustomErrorException

Auth.JWTBearerTokenExchange.

JWTBearerTokenExchangeException

```

Throw this exception to indicate that an error occurred when using the auth provider plug-in.
Use to display a custom error message to the user. To get the error message and write it to
debug log, use the `String getMessage()` .

Throw this exception to indicate that an error occurred while running the custom behavior for
a connected app. To get the error message and write it to debug log, use the `String`

`getMessage()` .

Throw this exception to customize error messages that appear on Discovery logins and
Configurable Self-Registration pages. An error message can have up to 200 characters. Use
custom error exceptions to localize error messages.

Include this exception in:

**•** `Auth.MyDomainLoginDiscoveryHandler` to show a custom error message on
the My Domain login page

**•** `Auth.LoginDiscoveryHandler` to show an error message on the Experience
Cloud site login page

**•** `Auth.ConfigurableSelfRegHandler` to show an error message on the
Experience Cloud site self-registration Verify page

The Verify page shows up if you configured self-registration with either an **Email** or **Text**
**Message** verification method. If you didn’t set up sign-up with a verification method, the error
message appears on the self-registration page.

To get the error message and write it to debug log, use the `String getMessage()` .

Throw this exception to indicate a problem with the response from the token endpoint in the
JWTBearerTokenExchange class. This exception occurs during the OAuth 2.0 JWT bearer token
flow when the HTTP response:

**•** Fails to return an access token

**•** Isn’t in JSON format

**•** Returns a response code other than a 200 “OK” success code

To get the error message and write it to debug log, use the `String getMessage()` .


Apex Reference Guide Auth Exceptions

**Exception** **Description**

`Auth.JWTValidationException` Throws this exception to indicate failure to validate a JWT using methods in the `JWTUtil`
class. This exception occurs during the OAuth 2.0 token exchange flow in these scenarios.

**•** Can’t parse the JWT

**•** Can’t validate the JWT using a certificate, a public key, or the remote keys endpoint,
depending on which method you use

```
Auth.LoginDiscoveryException

Auth.VerificationException

```

Examples

Throw this exception to indicate that an error occurred when executing the Login Discovery
handler. For an example, see LoginDiscoveryHandler Example Implementation. To get the error
message and write it to debug log, use the `String getMessage()` .

Throw this exception to trigger verification based on the passed-in policy. You can throw this
exception in an Apex trigger or Visualforce controller. The system automatically sends you to
the verification endpoint, if possible.

Note: You can’t catch this exception. The exception immediately triggers the verification.

This example uses `AuthProviderPluginException` to throw a custom exception in a custom authentication provider
implementation. Use this exception if you want the end user to see a specific message, passing in the error message as a parameter. If
you use another exception, users see a standard Salesforce error message.

```
global override Auth.OAuthRefreshResult refresh(Map<string,string>

authProviderConfiguration,String refreshToken){

        HttpRequest req = new HttpRequest();

        String accessToken = null;

        String error = null;

        try {

        // DEVELOPER TODO: Make a refresh token flow using refreshToken passed

        // in as an argument to get the new access token

        // accessToken = ...

        } catch (System.CalloutException e) {

        error = e.getMessage();

        }

        catch(Exception e) {

        error = e.getMessage();

        throw new Auth.AuthProviderPluginException('My custom error');

        }

        return new Auth.OAuthRefreshResult(accessToken,refreshToken, error);

        }

```

This example uses `Auth.VerificationException` to trigger verification if a user attempts to create an account without a high
assurance session.

```
trigger testTrigger on Account (before insert) {

   Map<String, String> sessionMap = auth.SessionManagement.getCurrentSession();

   if(!sessionMap.get('SessionSecurityLevel').equals('HIGH_ASSURANCE')) {

```


## Apex Reference Guide Cache Namespace

```
        throw new Auth.VerificationException(

           Auth.VerificationPolicy.HIGH_ASSURANCE, 'Insert Account');

      }

   }

## Cache Namespace The Cache namespace contains methods for managing the platform cache. The following are the classes in the Cache namespace.

```

IN THIS SECTION:

### CacheBuilder Interface

An interface for safely retrieving and removing values from a session or org cache. Use the interface to generate a value that you
want to store in the cache. The interface checks for cache misses, which means you no longer need to check for null cache values
yourself.

Org Class
Use the `Cache.Org` class to add, retrieve, and manage values in the org cache. Unlike the session cache, the org cache is not tied
to any session and is available to the organization across requests and to all users.

OrgPartition Class
Contains methods to manage cache values in the org cache of a specific partition. Unlike the session cache, the org cache is not tied
to any session. It’s available to the org across requests and to all users.

Partition Class
Base class of `Cache.OrgPartition` and `Cache.SessionPartition` . Use the subclasses to manage the cache partition
for org caches and session caches.

Session Class
Use the `Cache.Session` class to add, retrieve, and manage values in the session cache. The session cache is active as long as
the user’s Salesforce session is valid (the user is logged in, and the session is not expired).

SessionPartition Class
Contains methods to manage cache values in the session cache of a specific partition.

Cache Exceptions
## The Cache namespace contains exception classes.

Visibility Enum
Use the `Cache.Visibility` enumeration in the `Cache.Session` or `Cache.Org` methods to indicate whether a cached
value is visible only in the value’s namespace or in all namespaces.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

### CacheBuilder Interface

An interface for safely retrieving and removing values from a session or org cache. Use the interface to generate a value that you want
to store in the cache. The interface checks for cache misses, which means you no longer need to check for null cache values yourself.


Apex Reference Guide CacheBuilder Interface

Namespace

#### Cache

IN THIS SECTION:

#### CacheBuilder Methods

CacheBuilder Example Implementation

SEE ALSO:

_Apex Developer Guide_ [: Safely Cache Values with the CacheBuilder Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_platform_cache_builder.htm)

#### CacheBuilder Methods The following are methods for CacheBuilder .

IN THIS SECTION:

##### doLoad(var)

Contains the logic that builds a cached value. You don’t call this method directly. Instead, it’s called indirectly when you reference
#### the class that implements the CacheBuilder interface.

##### doLoad(var)

Contains the logic that builds a cached value. You don’t call this method directly. Instead, it’s called indirectly when you reference the
#### class that implements the CacheBuilder interface.

Signature

```
   public Object doLoad(String var)

```

Parameters

```
   var
```

Type: String

A case-sensitive string value used to build a cached value. This parameter is also used as part of the unique key that identifies the
cached value.

Return Value

Type: Object

The value that was cached. Cast the return value to the appropriate type.


### Apex Reference Guide Org Class

#### CacheBuilder Example Implementation This example creates a class called UserInfoCache that implements the CacheBuilder interface. The class caches the results

of a SOQL query run against the User object.

```
   class UserInfoCache implements Cache.CacheBuilder {

      public Object doLoad(String userid) {

        User u = (User)[SELECT Id, IsActive, username FROM User WHERE id =: userid];

        return u;

      }

   }

```

This example gets a cached User record based on a user ID. If the value exists in the org cache, it is returned. If the value doesn’t exist,
the `doLoad(String var)` method is re-executed, and the new value is cached and returned.

```
   User batman = (User) Cache.Org.get(UserInfoCache.class, ‘00541000000ek4c');

### Org Class

```

Use the `Cache.Org` class to add, retrieve, and manage values in the org cache. Unlike the session cache, the org cache is not tied to
any session and is available to the organization across requests and to all users.

Namespace

#### Cache

Usage

**Cache Key Format**

This table lists the format of the key parameter that some methods in this class take, such as `put`, `get`, and `contains` .

Note:

**•** If no default partition is specified in the org, calling a cache method without fully qualifying the key name causes a
`Cache.Org.OrgCacheException` to be thrown.

**•** The `local` prefix in an installed managed package refers to the namespace of the subscriber org and not the package’s
namespace. The cache `put` calls aren’t allowed in a partition that the invoking class doesn’t own.


Apex Reference Guide Org Class

Example

This class is the controller for a sample Visualforce page (shown in the subsequent code sample). The cached values are initially added
to the cache by the `init()` method, which the Visualforce page invokes when it loads through the `action` attribute. The cache
keys don’t contain the `namespace.partition` prefix. They all refer to the default partition in your org. To run this sample, create
a partition and mark it as default.

The Visualforce page contains four output components. These components call `get` methods on the controller that returns the following
values from the cache: a date, data based on the `MyData` inner class, a counter, a text value, and a list. The size of the list is also returned.

The Visualforce page also contains two buttons. The Rerender button invokes the `go()` method on the controller. This method increases
the values of the counter and the custom data in the cache. When you click **Rerender**, the two counters increase by one each time. The
`go()` method retrieves the values of these counters from the cache, increments their values by one, and stores them again in the
cache.

The Remove datetime Key button deletes the date-time value (with key `datetime` ) from the cache. As a result, the value next to
`Cached datetime:` is cleared on the page.

Note: If another user logs in and runs this sample, this user gets the cache values that were last added or updated by the previous
user. For example, if the counter value was five, the next user sees the counter value as increased to six.

```
   public class OrgCacheController {

      // Inner class.

      // Used as the data type of a cache value.

      class MyData {

        public String value { get; set; }

        public Integer counter { get; set; }

        public MyData(String value) {

           this.value = value;

           this.counter = 0;

        }

        public void inc() {

           counter++;

        }

        override public String toString() {

           return this.value + ':' + this.counter;

        }

      }

      // Apex List.

      // Used as the data type of a cached value.

      private List<String> numbers =

           new List<String> { 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE' };

      // Constructor of the controller for the Visualforce page.

      public OrgCacheController() {

      }

      // Adds various values to the cache.

      // This method is called when the Visualforce page loads.

      public void init() {

        // All key values are not qualified by the namespace.partition

```


Apex Reference Guide Org Class

```
        // prefix because they use the default partition.

        // Add counter to the cache with initial value of 0

        // or increment it if it's already there.

        if (!Cache.Org.contains('counter')) {

           Cache.Org.put('counter', 0);

        } else {

           Cache.Org.put('counter', getCounter() + 1);

        }

        // Add the datetime value to the cache only if it's not already there.

        if (!Cache.Org.contains('datetime')) {

           DateTime dt = DateTime.now();

           Cache.Org.put('datetime', dt);

        }

        // Add the custom data to the cache only if it's not already there.

        if (!Cache.Org.contains('data')) {

           Cache.Org.put('data', new MyData('Some custom value'));

        }

        // Add a list of number to the cache if not already there.

        if (!Cache.Org.contains('list')) {

           Cache.Org.put('list', numbers);

        }

        // Add a string value to the cache if not already there.

        if (!Cache.Org.contains('output')) {

           Cache.Org.put('output', 'Cached text value');

        }

      }

      // Return counter from the cache.

      public Integer getCounter() {

        return (Integer)Cache.Org.get('counter');

      }

      // Return datetime value from the cache.

      public String getCachedDatetime() {

        DateTime dt = (DateTime)Cache.Org.get('datetime');

        return dt != null ? dt.format() : null;

      }

      // Return cached value whose type is the inner class MyData.

      public String getCachedData() {

        MyData mydata = (MyData)Cache.Org.get('data');

        return mydata != null ? mydata.toString() : null;

      }

      // Return output from the cache.

      public String getOutput() {

        return (String)Cache.Org.get('output');

      }

```


Apex Reference Guide Org Class

```
      // Return list from the cache.

      public List<String> getList() {

        return (List<String>)Cache.Org.get('list');

      }

      // Method invoked by the Rerender button on the Visualforce page.

      // Updates the values of various cached values.

      // Increases the values of counter and the MyData counter if those

      // cache values are still in the cache.

      public PageReference go() {

        // Increase the cached counter value or set it to 0

        // if it's not cached.

        if (Cache.Org.contains('counter')) {

           Cache.Org.put('counter', getCounter() + 1);

        } else {

           Cache.Org.put('counter', 0);

        }

        // Get the custom data value from the cache.

        MyData d = (MyData)Cache.Org.get('data');

        // Only if the data is already in the cache, update it.

        if (Cache.Org.contains('data')) {

           d.inc();

           Cache.Org.put('data', d);

        }

        return null;

      }

      // Method invoked by the Remove button on the Visualforce page.

      // Removes the datetime cached value from the org cache.

      public PageReference remove() {

        Cache.Org.remove('datetime');

        return null;

      }

   }

```

This is the Visualforce page that corresponds to the `OrgCacheController` class.

```
   <apex:page controller="OrgCacheController" action="{!init}">

      <apex:outputPanel id="output">

        <br/>Cached datetime: <apex:outputText value="{!cachedDatetime}"/>

        <br/>Cached data: <apex:outputText value="{!cachedData}"/>

        <br/>Cached counter: <apex:outputText value="{!counter}"/>

        <br/>Output: <apex:outputText value="{!output}"/>

        <br/>Repeat: <apex:repeat var="item" value="{!list}">

           <apex:outputText value="{!item}"/>&nbsp;

        </apex:repeat>

        <br/>List size: <apex:outputText value="{!list.size}"/>

      </apex:outputPanel>

      <br/><br/>

      <apex:form >

```


Apex Reference Guide Org Class

```
        <apex:commandButton id="go" action="{!go}" value="Rerender" rerender="output"/>

        <apex:commandButton id="remove" action="{!remove}" value="Remove datetime Key"

   rerender="output"/>

      </apex:form>

   </apex:page>

```

This is the output of the page after clicking the **Rerender** button twice. The counter value could differ in your case if a key named
`counter` was already in the cache before running this sample.

```
   Cached datetime:8/11/2015 1:58 PM

   Cached data:Some custom value:2

   Cached counter:2

   Output:Cached text value

   Repeat:ONE TWO THREE FOUR FIVE

   List size:5

```

IN THIS SECTION:

#### Org Constants

The Org class provides a constant that you can use when setting the time-to-live (TTL) value.

#### Org Methods

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

#### Org Constants

The Org class provides a constant that you can use when setting the time-to-live (TTL) value.

**Constant** **Description**

`MAX_TTL_SECS` Represents the maximum amount of time, in seconds, to keep the cached value in the
org cache.

#### Org Methods The following are methods for Org . All methods are static.

IN THIS SECTION:

contains(key)
Returns `true` if the org cache contains a cached value corresponding to the specified key.

contains(keys)
Returns `true` if the org cache contains values for the specified key entries.

contains(setOfKeys)
Returns `true` if the org cache contains values for a specified set of keys.


Apex Reference Guide Org Class

get(key)
Returns the cached value corresponding to the specified key from the org cache.

get(cacheBuilder, key)
Returns the cached value corresponding to the specified key from the org cache. Use this method if your cached value is a class that
implements the `CacheBuilder` interface.

get(keys)
Returns the cached values corresponding to the specified set of keys from the org cache.

getAvgGetSize()
Returns the average item size of all the keys fetched from the org cache, in bytes.

getAvgGetTime()
Returns the average time taken to get a key from the org cache, in nanoseconds.

getAvgValueSize()
**Deprecated and available only in API versions 49.0 and earlier.** Returns the average item size for keys in the org cache, in bytes.

getCapacity()
Returns the percentage of org cache capacity that has been used.

getKeys()
Returns a set of all keys that are stored in the org cache and visible to the invoking namespace.

getMaxGetSize()
Returns the maximum item size of all the keys fetched from the org cache, in bytes.

getMaxGetTime()
Returns the maximum time taken to get a key from the org cache, in nanoseconds.

getMaxValueSize()
**Deprecated and available only in API versions 49.0 and earlier.** Returns the maximum item size for keys in the org cache, in
bytes.

getMissRate()
Returns the miss rate in the org cache.

getName()
Returns the name of the default cache partition.

getNumKeys()
Returns the total number of keys in the org cache.

getPartition(partitionName)
Returns a partition from the org cache that corresponds to the specified partition name.

put(key, value)
Stores the specified key/value pair as a cached entry in the org cache. The `put` method can write only to the cache in your org’s
namespace.

put(key, value, visibility)
Stores the specified key/value pair as a cached entry in the org cache and sets the cached value’s visibility.

put(key, value, ttlSecs)
Stores the specified key/value pair as a cached entry in the org cache and sets the cached value’s lifetime.


Apex Reference Guide Org Class

put(key, value, ttlSecs, visibility, immutable)
Stores the specified key/value pair as a cached entry in the org cache. This method also sets the cached value’s lifetime, visibility,
and whether it can be overwritten by another namespace.

remove(key)
Deletes the cached value corresponding to the specified key from the org cache.

remove(cacheBuilder, key)
Deletes the cached value corresponding to the specified key from the org cache. Use this method if your cached value is a class that
implements the `CacheBuilder` interface.

##### contains(key)

Returns `true` if the org cache contains a cached value corresponding to the specified key.

Signature

```
   public static Boolean contains(String key)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value. For information about the format of the key name, see Usage.

Return Value

Type: Boolean

`true` if a cache entry is found. Othewise, `false` .

##### contains(keys)

Returns `true` if the org cache contains values for the specified key entries.

Signature

```
   public static List<Boolean> contains(List<String> keys)

```

Parameters

```
   keys
```

Type: List<String>

A list of keys that identifies cached values. For information about the format of the key name, see Usage.

Return Value

Type: List<Boolean>

`true` if the key entries are found. Othewise, `false` .


Apex Reference Guide Org Class

##### contains(setOfKeys)

Returns `true` if the org cache contains values for a specified set of keys.

Signature

```
   public static Map <String, Boolean> contains (Set<String> keys)

```

Parameters

```
   setOfKeys
```

Type: Set <String>

A set of keys that uniquely identifies cached values. For information about the format of the key name, see Usage

Return Value

Type: Map <String, Boolean>

Returns the cache key and corresponding Boolean value indicating that the key entry exists. The Boolean value is `false` if the key
entry doesn't exist.

Usage

The number of input keys cannot exceed the maximum limit of 10.

Example

In this example, the code checks for the presence of multiple keys on the default partition. It fetches the cache key and the corresponding
Boolean value for the key entry from the org cache of the default partition.

```
   Set<String> keys = new Set<String>{'key1','key2','key3','key4','key5'};

   Map<String,Boolean> result = Cache.Org.contains(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('Is Key Present in the cache : ' + result.get(key));

   }

```

In this example, the code checks for the presence of multiple keys on different partitions. It fetches the cache key and the corresponding
Boolean value for the key entry from the org cache of different partitions.

```
   // Assuming there are three partitions p1, p2, p3 with default 'local' namespace

   Set<String> keys = new Set<String>{'local.p1.key','local.p2.key', 'local.p3.key'};

   Map<String,Boolean> result = Cache.Org.contains(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('Is Key Present in the cache : + result.get(key));

   }

##### get(key)

```

Returns the cached value corresponding to the specified key from the org cache.


Apex Reference Guide Org Class

Signature

```
   public static Object get(String key)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value. For information about the format of the key name, see Usage.

Return Value

Type: Object

The cached value as a generic object type. Cast the returned value to the appropriate type.

Usage

Because `Cache.Org.get()` returns an object, cast the returned value to a specific type to facilitate use of the returned value.

```
   // Get a cached value

   Object obj = Cache.Org.get('ns1.partition1.orderDate');

   // Cast return value to a specific data type

   DateTime dt2 = (DateTime)obj;

```

If a `Cache.Org.get()` call doesn’t find the referenced key, it returns `null` .

##### get(cacheBuilder, key)

Returns the cached value corresponding to the specified key from the org cache. Use this method if your cached value is a class that
implements the `CacheBuilder` interface.

Signature

```
   public static Object get(System.Type cacheBuilder, String key)

```

Parameters

```
   cacheBuilder
```

Type: System.Type

The Apex class that implements the `CacheBuilder` interface.

```
   key
```

Type: String

A case-sensitive string value that, combined with the class name corresponding to the _`cacheBuilder`_ parameter, uniquely
identifies a cached value.

Return Value

Type: Object

The cached value as a generic object type. Cast the returned value to the appropriate type.


Apex Reference Guide Org Class

Usage

Because `Cache.Org.get(` _`cacheBuilder`_ `,` _`key`_ `)` returns an object, cast the returned value to a specific type to facilitate use
of the returned value.

```
   return ((DateTime)Cache.Org.get(DateCache.class, 'datetime')).format();

##### get(keys)

```

Returns the cached values corresponding to the specified set of keys from the org cache.

Signature

```
   public static Map <String, Object> get (Set <String> keys)

```

Parameters

```
   keys
```

Type: Set <String>

A set of keys that uniquely identify cached values. For information about the format of the key name, see Usage.

Return Value

Type: Map <String, Object>

Returns the cache key and corresponding value. Returns null when no corresponding value is found for an input key.

Usage

The number of input keys cannot exceed the maximum limit of 10.

Examples

Fetch multiple keys from the org cache of the default partition.

```
   Set<String> keys = new Set<String>{'key1','key2','key3','key4','key5'};

   Map<String,Object> result = Cache.Org.get(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('value: ' + result.get(key));

   }

```

Fetch multiple keys from the org cache of different partitions.

```
   // Assuming there are three partitions p1, p2, p3 with default 'local' namespace

   Set<String> keys = new Set<String>{'local.p1.key','local.p2.key', 'local.p3.key'};

   Map<String,Object> result = Cache.Org.get(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('value: ' + result.get(key));

   }

```


Apex Reference Guide Org Class

##### getAvgGetSize()

Returns the average item size of all the keys fetched from the org cache, in bytes.

Signature

```
   public static Long getAvgGetSize()

```

Return Value

Type: Long

Example

In this example the following keys and their corresponding value sizes are inserted. The code then fetches the keys: key 1, key 2, key 3
and key 4 and returns the average item size of the fetched keys.

```
   // Inserting keys key1, key2, key3, key4, key5

   Cache.Org.put('key1', 'value1');

   Cache.Org.put('key2', 'value2');

   Cache.Org.put('key3', 'this is a big value !!!');

   Cache.Org.put('key4', 4);

   Cache.Org.put('key5', 5);

   // Fetching keys - key1, key2, key3, key4

   Object v1 = Cache.Org.get('key1');

   Object v2 = Cache.Org.get('key2');

   Object v3 = Cache.Org.get('key3');

   Object v4 = Cache.Org.get('key4');

   // Fetching average get size

   Long val = Cache.Org.getAvgGetSize();

   // Avg item size returned is 44 ( average of 42(key1), 42(key2), 58(key3) and 36(key4)

   keys that were fetched )

   System.debug('Avg Get Size :' + val);

##### getAvgGetTime()

```

Returns the average time taken to get a key from the org cache, in nanoseconds.


Apex Reference Guide Org Class

Signature

```
   public static Long getAvgGetTime()

```

Return Value

Type: Long

##### getAvgValueSize()

**Deprecated and available only in API versions 49.0 and earlier.** Returns the average item size for keys in the org cache, in bytes.

Signature

```
   public static Long getAvgValueSize()

```

Return Value

Type: Long

##### getCapacity()

Returns the percentage of org cache capacity that has been used.

Signature

```
   public static Double getCapacity()

```

Return Value

Type: Double

Used cache as a percentage number.

##### getKeys()

Returns a set of all keys that are stored in the org cache and visible to the invoking namespace.

Signature

```
   public static Set<String> getKeys()

```

Return Value

Type: Set<String>

A set containing all cache keys.

##### getMaxGetSize()

Returns the maximum item size of all the keys fetched from the org cache, in bytes.


Apex Reference Guide Org Class

Signature

```
   public static Long getMaxGetSize()

```

Return Value

Type: Long

Example

In this example the following keys and their corresponding value sizes are inserted. The code fetches the keys: key 1, key 2 and key 4
and returns the maximum key value size from the fetched keys.

```
   // Inserting keys key1, key2, key3, key4, key5

   Cache.Org.put('key1', 'value1');

   Cache.Org.put('key2', 'value2');

   Cache.Org.put('key3', 'this is a big value !!!');

   Cache.Org.put('key4', 4);

   Cache.Org.put('key5', 5);

   // Fetching keys - key1, key2, key4

   Object v1 = Cache.Org.get('key1');

   Object v2 = Cache.Org.get('key2');

   Object v4 = Cache.Org.get('key4');

   // Fetching max get size

   Long val = Cache.Org.getMaxGetSize();

   // Max item size returned is 42 ( max of 42(key1), 42(key2), and 36(key4) keys that were

   fetched )

   System.debug('Max Get Size :' + val);

##### getMaxGetTime()

```

Returns the maximum time taken to get a key from the org cache, in nanoseconds.

Signature

```
   public static Long getMaxGetTime()

```


Apex Reference Guide Org Class

Return Value

Type: Long

##### getMaxValueSize()

**Deprecated and available only in API versions 49.0 and earlier.** Returns the maximum item size for keys in the org cache, in bytes.

Signature

```
   public static Long getMaxValueSize()

```

Return Value

Type: Long

##### getMissRate()

Returns the miss rate in the org cache.

Signature

```
   public static Double getMissRate()

```

Return Value

Type: Double

##### getName()

Returns the name of the default cache partition.

Signature

```
   public String getName()

```

Return Value

Type: String

The name of the default cache partition.

##### getNumKeys()

Returns the total number of keys in the org cache.

Signature

```
   public static Long getNumKeys()

```


Apex Reference Guide Org Class

Return Value

Type: Long

##### getPartition(partitionName)

Returns a partition from the org cache that corresponds to the specified partition name.

Signature

```
   public static cache.OrgPartition getPartition(String partitionName)

```

Parameters

```
   partitionName
```

Type: String

A partition name that is qualified by the namespace, for example, _`namespace.partition`_ .

Return Value

Type: Cache.OrgPartition

Example

After you get the org partition, you can add and retrieve the partition’s cache values.

```
   // Get partition

   Cache.OrgPartition orgPart = Cache.Org.getPartition('myNs.myPartition');

   // Retrieve cache value from the partition

   if (orgPart.contains('BookTitle')) {

      String cachedTitle = (String)orgPart.get('BookTitle');

   }

   // Add cache value to the partition

   orgPart.put('OrderDate', Date.today());

   // Or use dot notation to call partition methods

   String cachedAuthor = (String)Cache.Org.getPartition('myNs.myPartition').get('BookAuthor');

##### put(key, value) Stores the specified key/value pair as a cached entry in the org cache. The put method can write only to the cache in your org’s
```

namespace.

Signature

```
   public static void put(String key, Object value)

```


Apex Reference Guide Org Class

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value. For information about the format of the key name, see Usage.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

Return Value

Type: void

##### put(key, value, visibility)

Stores the specified key/value pair as a cached entry in the org cache and sets the cached value’s visibility.

Signature

```
   public static void put(String key, Object value, Cache.Visibility visibility)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value. For information about the format of the key name, see Usage.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

```
   visibility
```

Type: Cache.Visibility

Indicates whether the cached value is available only to Apex code that is executing in the same namespace or to Apex code executing
from any namespace.

Return Value

Type: void

##### put(key, value, ttlSecs)

Stores the specified key/value pair as a cached entry in the org cache and sets the cached value’s lifetime.

Signature

```
   public static void put(String key, Object value, Integer ttlSecs)

```


Apex Reference Guide Org Class

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value. For information about the format of the key name, see Usage.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

```
   ttlSecs
```

Type: Integer

The amount of time, in seconds, to keep the cached value in the org cache. The maximum is 172,800 seconds (48 hours). The
minimum value is 300 seconds or 5 minutes. The default value is 86,400 seconds (24 hours).

Return Value

Type: void

##### put(key, value, ttlSecs, visibility, immutable)

Stores the specified key/value pair as a cached entry in the org cache. This method also sets the cached value’s lifetime, visibility, and
whether it can be overwritten by another namespace.

Signature

```
   public static void put(String key, Object value, Integer ttlSecs, cache.Visibility

   visibility, Boolean immutable)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value. For information about the format of the key name, see Usage.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

```
   ttlSecs
```

Type: Integer

The amount of time, in seconds, to keep the cached value in the org cache. The maximum is 172,800 seconds (48 hours). The
minimum value is 300 seconds or 5 minutes. The default value is 86,400 seconds (24 hours).

```
   visibility
```

Type: Cache.Visibility

Indicates whether the cached value is available only to Apex code that is executing in the same namespace or to Apex code executing
from any namespace.

```
   immutable
```

Type: Boolean

Indicates whether the cached value can be overwritten by another namespace ( `false` ) or not ( `true` ).


Apex Reference Guide Org Class

Return Value

Type: void

##### remove(key)

Deletes the cached value corresponding to the specified key from the org cache.

Signature

```
   public static Boolean remove(String key)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value. For information about the format of the key name, see Usage.

Return Value

Type: Boolean

`true` if the cache value was successfully removed. Otherwise, `false` .

##### remove(cacheBuilder, key)

Deletes the cached value corresponding to the specified key from the org cache. Use this method if your cached value is a class that
implements the `CacheBuilder` interface.

Signature

```
   public static Boolean remove(System.Type cacheBuilder, String key)

```

Parameters

```
   cacheBuilder
```

Type: System.Type

The Apex class that implements the `CacheBuilder` interface.

```
   key
```

Type: String

A case-sensitive string value that, combined with the class name corresponding to the _`cacheBuilder`_ parameter, uniquely
identifies a cached value.

Return Value

Type: Boolean

`true` if the cache value was successfully removed. Otherwise, `false` .


### Apex Reference Guide OrgPartition Class OrgPartition Class

Contains methods to manage cache values in the org cache of a specific partition. Unlike the session cache, the org cache is not tied to
any session. It’s available to the org across requests and to all users.

Namespace

Cache

Usage

This class extends Cache.Partition and inherits all its non-static methods. Utility methods for creating and validating keys aren’t supported
and can be called only from the `Cache.Partition` parent class. For a list of `Cache.Partition` methods, see Partition Methods.

To get an org partition, call `Cache.Org.getPartition` and pass in a fully qualified partition name, as follows.

```
   Cache.OrgPartition orgPartition = Cache.Org.getPartition('namespace.myPartition');

```

See Cache Key Format for Partition Methods.

The org cache supports concurrent reads and writes across multiple simultaneous Apex transactions, but the results can be indeterminate.
[See Platform Cache Considerations in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_platform_cache_limitations.htm) _Apex Developer Guide_ .

Org cache operations are atomic transactions. If the Apex request that the cache operations run in fails, then all cache operations in that
[request are rolled back. See Platform Cache Internals in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_platform_cache_internals.htm) _Apex Developer Guide_ .

Example

This class is the controller for a sample Visualforce page (shown in the subsequent code sample). The controller shows how to use the
methods of `Cache.OrgPartition` to manage a cache value on a particular partition. The controller takes inputs from the Visualforce
page for the partition name, key name for a counter, and initial counter value. The controller contains default values for these inputs.
When you click **Rerender** on the Visualforce page, the `go()` method is invoked and increases the counter by one. When you click
**Remove Key**, the counter key is removed from the cache. The counter value gets reset to its initial value when it’s re-added to the cache.

Note: If another user logs in and runs this sample, the user gets the cache values that were last added or updated by the previous
user. For example, if the counter value was five, the next user sees the counter value as increased to six.

```
   public class OrgPartitionController {

      // Name of a partition

      String partitionInput = 'local.myPartition';

      // Name of the key

      String counterKeyInput = 'counter';

      // Key initial value

      Integer counterInitValue = 0;

      // Org partition object

      Cache.OrgPartition orgPartition;

      // Constructor of the controller for the Visualforce page.

      public OrgPartitionController() {

      }

      // Adds counter value to the cache.

      // This method is called when the Visualforce page loads.

```


Apex Reference Guide OrgPartition Class

```
      public void init() {

        // Create the partition instance based on the partition name

        orgPartition = getPartition();

        // Create the partition instance based on the partition name

        // given in the Visualforce page or the default value.

        orgPartition = Cache.Org.getPartition(partitionInput);

        // Add counter to the cache with an initial value

        // or increment it if it's already there.

        if (!orgPartition.contains(counterKeyInput)) {

           orgPartition.put(counterKeyInput, counterInitValue);

        } else {

           orgPartition.put(counterKeyInput, getCounter() + 1);

        }

      }

      // Returns the org partition based on the partition name

      // given in the Visualforce page or the default value.

      private Cache.OrgPartition getPartition() {

        if (orgPartition == null) {

           orgPartition = Cache.Org.getPartition(partitionInput);

        }

        return orgPartition;

      }

      // Return counter from the cache.

      public Integer getCounter() {

        return (Integer)getPartition().get(counterKeyInput);

      }

      // Invoked by the Submit button to save input values

      // supplied by the user.

      public PageReference save() {

        // Reset the initial key value in the cache

        getPartition().put(counterKeyInput, counterInitValue);

        return null;

      }

      // Method invoked by the Rerender button on the Visualforce page.

      // Updates the values of various cached values.

      // Increases the values of counter and the MyData counter if those

      // cache values are still in the cache.

      public PageReference go() {

        // Get the org partition object

        orgPartition = getPartition();

        // Increase the cached counter value or set it to 0

        // if it's not cached.

        if (orgPartition.contains(counterKeyInput)) {

           orgPartition.put(counterKeyInput, getCounter() + 1);

        } else {

```


Apex Reference Guide OrgPartition Class

```
           orgPartition.put(counterKeyInput, counterInitValue);

        }

        return null;

      }

      // Method invoked by the Remove button on the Visualforce page.

      // Removes the datetime cached value from the org cache.

      public PageReference remove() {

        getPartition().remove(counterKeyInput);

        return null;

      }

      // Get and set methods for accessing variables

      // that correspond to the input text fields on

      // the Visualforce page.

      public String getPartitionInput() {

        return partitionInput;

      }

      public String getCounterKeyInput() {

        return counterKeyInput;

      }

      public Integer getCounterInitValue() {

        return counterInitValue;

      }

      public void setPartitionInput(String partition) {

        this.partitionInput = partition;

      }

      public void setCounterKeyInput(String keyName) {

        this.counterKeyInput = keyName;

      }

      public void setCounterInitValue(Integer counterValue) {

        this.counterInitValue = counterValue;

      }

   }

```

This is the Visualforce page that corresponds to the `OrgPartitionController` class.

```
   <apex:page controller="OrgPartitionController" action="{!init}">

      <apex:form >

        <br/>Partition with Namespace Prefix: <apex:inputText value="{!partitionInput}"/>

        <br/>Counter Key Name: <apex:inputText value="{!counterKeyInput}"/>

        <br/>Counter Initial Value: <apex:inputText value="{!counterInitValue}"/>

        <apex:commandButton action="{!save}" value="Save Key Input Values"/>

      </apex:form>

      <apex:outputPanel id="output">

```


### Apex Reference Guide Partition Class

```
        <br/>Cached Counter: <apex:outputText value="{!counter}"/>

      </apex:outputPanel>

      <br/>

      <apex:form >

        <apex:commandButton id="go" action="{!go}" value="Rerender" rerender="output"/>

        <apex:commandButton id="remove" action="{!remove}" value="Remove Key"

   rerender="output"/>

      </apex:form>

   </apex:page>

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

### Partition Class

Base class of `Cache.OrgPartition` and `Cache.SessionPartition` . Use the subclasses to manage the cache partition
for org caches and session caches.

Namespace

Cache

Cache Key Format for Partition Methods

After you obtain the partition object (an instance of `Cache.OrgPartition` or `Cache.SessionPartition` ), the methods
to add, retrieve, and manage the cache values in a partition take the key name. The key name that you supply to these methods ( `get()`,
`put()`, `remove()`, and `contains()` ) doesn’t include the `namespace.partition` prefix.

IN THIS SECTION:

#### Partition Methods

SEE ALSO:

OrgPartition Class

SessionPartition Class

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

#### Partition Methods

### The following are methods for Partition .

IN THIS SECTION:

contains(key)
Returns `true` if the cache partition contains a cached value corresponding to the specified key.


Apex Reference Guide Partition Class

contains(setOfKeys)
Returns `true` if the cache partition contains values for a specified set of keys.

createFullyQualifiedKey(namespace, partition, key)
Generates a fully qualified key from the passed-in key components. The format of the generated key string is
`namespace.partition.key` .

createFullyQualifiedPartition(namespace, partition)
Generates a fully qualified partition name from the passed-in namespace and partition. The format of the generated partition string
is `namespace.partition` .

get(key)
Returns the cached value corresponding to the specified key from the cache partition.

get(keys)
Returns the cached values corresponding to the specified set of keys from the cache partition.

get(cacheBuilder, key)
Returns the cached value corresponding to the specified key from the partition cache. Use this method if your cached value is a class
that implements the `CacheBuilder` interface.

getAvgGetSize()
Returns the average item size of all the keys fetched from the partition, in bytes.

getAvgGetTime()
Returns the average time taken to get a key from the partition, in nanoseconds.

getAvgValueSize()
**Deprecated and available only in API versions 49.0 and earlier.** Returns the average item size for keys in the partition, in bytes.

getCapacity()
Returns the percentage of cache used of the total capacity for this partition.

getKeys()
Returns a set of all keys that are stored in the cache partition and visible to the invoking namespace.

getMaxGetSize()
Returns the maximum item size of all the keys fetched from the partition, in bytes.

getMaxGetTime()
Returns the maximum time taken to get a key from the partition, in nanoseconds.

getMaxValueSize()
**Deprecated and available only in API versions 49.0 and earlier.** Returns the maximum item size for keys in the partition, in
bytes.

getMissRate()
Returns the miss rate in the partition.

getName()
Returns the name of this cache partition.

getNumKeys()
Returns the total number of keys in the partition.


Apex Reference Guide Partition Class

isAvailable()
Returns `true` if the Salesforce session is available. Only applies to `Cache.SessionPartition` . The session cache isn’t
available when an active session isn’t present, such as in asynchronous Apex or code called by asynchronous Apex. For example, if
batch Apex causes an Apex trigger to execute, the session cache isn’t available in the trigger because the trigger runs in asynchronous
context.

put(key, value)
Stores the specified key/value pair as a cached entry in the cache partition. The `put` method can write only to the cache in your
org’s namespace.

put(key, value, visibility)
Stores the specified key/value pair as a cached entry in the cache partition and sets the cached value’s visibility.

put(key, value, ttlSecs)
Stores the specified key/value pair as a cached entry in the cache partition and sets the cached value’s lifetime.

put(key, value, ttlSecs, visibility, immutable)
Stores the specified key/value pair as a cached entry in the cache partition. This method also sets the cached value’s lifetime, visibility,
and whether it can be overwritten by another namespace.

remove(key)
Deletes the cached value corresponding to the specified key from this cache partition.

remove(cacheBuilder, key)
Deletes the cached value corresponding to the specified key from the partition cache. Use this method if your cached value is a class
that implements the `CacheBuilder` interface.

validateCacheBuilder(cacheBuilder)
Validates that the specified class implements the `CacheBuilder` interface.

validateKey(isDefault, key)
Validates a cache key. This method throws a `Cache.InvalidParamException` if the key is not valid. A valid key is not
`null` and contains alphanumeric characters.

validateKeyValue(isDefault, key, value)
Validates a cache key and ensures that the cache value is non-null. This method throws a `Cache.InvalidParamException`
if the key or value is not valid. A valid key is not `null` and contains alphanumeric characters.

validateKeys(isDefault, keys)
Validates the specified cache keys. This method throws a `Cache.InvalidParamException` if the key is not valid. A valid
key is not `null` and contains alphanumeric characters.

validatePartitionName(name)
Validates the partition name — for example, that it is not null.

##### contains(key)

Returns `true` if the cache partition contains a cached value corresponding to the specified key.

Signature

```
   public Boolean contains(String key)

```


Apex Reference Guide Partition Class

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value.

Return Value

Type: Boolean

`true` if a cache entry is found. Othewise, `false` .

##### contains(setOfKeys)

Returns `true` if the cache partition contains values for a specified set of keys.

Signature

```
   public Map <String, Boolean> contains (Set<String> keys)

```

Parameters

```
   setOfKeys
```

Type: Set <String>

A set of keys that uniquely identifies cached values. For information about the format of the key name, see Usage.

Return Value

Type: Map <String, Boolean>

Returns the cache key and corresponding Boolean value indicating that the key entry exists. The Boolean value is `false` if the key
entry doesn't exist.

Usage

The number of input keys cannot exceed the maximum limit of 10.

Example

In this example, the code checks for the presence of multiple keys on a partition. It fetches the cache key and the corresponding Boolean
value for the key entry from the org cache of the partition.

```
   // Assuming there is a partition p1 in the default 'local' namespace

   Set<String> keys = new Set<String>{'key1','key2','key3','key4','key5'};

   Cache.OrgPartition orgPart = Cache.Org.getPartition('local.p1');

   Map<String,Boolean> result = orgPart.contains(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('Is Key Present in the cache:' + result.get(key));

   }

```


Apex Reference Guide Partition Class

In this example, the code checks for the presence of multiple keys on a partition. It fetches the cache key and the corresponding Boolean
value for the key entry from the session cache of the partition.

```
   // Assuming there are three partitions p1, p2, p3 with default 'local' namespace

   Set<String> keys = new Set<String>{'key1','key2','key3','key4','key5'};

   Cache.SessionPartition sessionPart = Cache.Session.getPartition('local.p1');

   Map<String,Boolean> result = sessionPart.contains(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('value: ' + result.get(key));

   }

##### createFullyQualifiedKey(namespace, partition, key)

```

Generates a fully qualified key from the passed-in key components. The format of the generated key string is
`namespace.partition.key` .

Signature

```
   public static String createFullyQualifiedKey(String namespace, String partition, String

   key)

```

Parameters

```
   namespace
```

Type: String

The namespace of the cache key.

```
   partition
```

Type: String

The partition of the cache key.

```
   key
```

Type: String

The name of the cache key.

Return Value

Type: String

##### createFullyQualifiedPartition(namespace, partition)

Generates a fully qualified partition name from the passed-in namespace and partition. The format of the generated partition string is
`namespace.partition` .

Signature

```
   public static String createFullyQualifiedPartition(String namespace, String partition)

```


Apex Reference Guide Partition Class

Parameters

```
   namespace
```

Type: String

The namespace of the cache key.

```
   partition
```

Type: String

The partition of the cache key.

Return Value

Type: String

##### get(key)

Returns the cached value corresponding to the specified key from the cache partition.

Signature

```
   public Object get(String key)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value.

Return Value

Type: Object

The cached value as a generic object type. Cast the returned value to the appropriate type.

##### get(keys)

Returns the cached values corresponding to the specified set of keys from the cache partition.

Signature

```
   public Map <String, Object> get (Set <String> keys)

```

Parameters

```
   keys
```

Type: Set <String>

A set of keys that uniquely identify cached values. For information about the format of the key name, see Usage.

Return Value

Type: Map <String, Object>


Apex Reference Guide Partition Class

Returns the cache key and corresponding value. Returns null when no corresponding value is found for an input key.

Usage

The number of input keys cannot exceed the maximum limit of 10.

Examples

Fetch multiple keys from the org cache of a partition.

```
   // Assuming there is a partition p1 in the default 'local' namespace

   Set<String> keys = new Set<String>{'key1','key2','key3','key4','key5'};

   Cache.OrgPartition orgPart = Cache.Org.getPartition('local.p1');

   Map<String,Object> result = orgPart.get(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('value: ' + result.get(key));

   }

```

Fetch multiple keys from the session cache of a partition.

```
   // Assuming there is a partition p1 in the default 'local' namespace

   Set<String> keys = new Set<String>{'key1','key2','key3','key4','key5'};

   Cache.SessionPartition sessionPart = Cache.Session.getPartition('local.p1');

   Map<String,Object> result = sessionPart.get(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('value: ' + result.get(key));

   }

##### get(cacheBuilder, key)

```

Returns the cached value corresponding to the specified key from the partition cache. Use this method if your cached value is a class
that implements the `CacheBuilder` interface.

Signature

```
   public Object get(System.Type cacheBuilder, String key)

```

Parameters

```
   cacheBuilder
```

Type: System.Type

The Apex class that implements the `CacheBuilder` interface.

```
   key
```

Type: String

A case-sensitive string value that, combined with the class name corresponding to the _`cacheBuilder`_ parameter, uniquely
identifies a cached value.


Apex Reference Guide Partition Class

Return Value

Type: Object

The cached value as a generic object type. Cast the returned value to the appropriate type.

##### getAvgGetSize()

Returns the average item size of all the keys fetched from the partition, in bytes.

Signature

```
   public Long getAvgGetSize()

```

Return Value

Type: Long

##### getAvgGetTime()

Returns the average time taken to get a key from the partition, in nanoseconds.

Signature

```
   public Long getAvgGetTime()

```

Return Value

Type: Long

##### getAvgValueSize()

**Deprecated and available only in API versions 49.0 and earlier.** Returns the average item size for keys in the partition, in bytes.

Signature

```
   public Long getAvgValueSize()

```

Return Value

Type: Long

##### getCapacity()

Returns the percentage of cache used of the total capacity for this partition.

Signature

```
   public Double getCapacity()

```


Apex Reference Guide Partition Class

Return Value

Type: Double

Used partition cache as a percentage number.

##### getKeys()

Returns a set of all keys that are stored in the cache partition and visible to the invoking namespace.

Signature

```
   public Set<String> getKeys()

```

Return Value

Type: Set<String>

A set containing all cache keys.

##### getMaxGetSize()

Returns the maximum item size of all the keys fetched from the partition, in bytes.

Signature

```
   public Long getMaxGetSize()

```

Return Value

Type: Long

##### getMaxGetTime()

Returns the maximum time taken to get a key from the partition, in nanoseconds.

Signature

```
   public Long getMaxGetTime()

```

Return Value

Type: Long

##### getMaxValueSize()

**Deprecated and available only in API versions 49.0 and earlier.** Returns the maximum item size for keys in the partition, in bytes.

Signature

```
   public Long getMaxValueSize()

```


Apex Reference Guide Partition Class

Return Value

Type: Long

##### getMissRate()

Returns the miss rate in the partition.

Signature

```
   public Double getMissRate()

```

Return Value

Type: Double

##### getName()

Returns the name of this cache partition.

Signature

```
   public String getName()

```

Return Value

Type: String

The name of this cache partition.

##### getNumKeys()

Returns the total number of keys in the partition.

Signature

```
   public Long getNumKeys()

```

Return Value

Type: Long

##### isAvailable()

Returns `true` if the Salesforce session is available. Only applies to `Cache.SessionPartition` . The session cache isn’t available
when an active session isn’t present, such as in asynchronous Apex or code called by asynchronous Apex. For example, if batch Apex
causes an Apex trigger to execute, the session cache isn’t available in the trigger because the trigger runs in asynchronous context.

Signature

```
   public Boolean isAvailable()

```


Apex Reference Guide Partition Class

Return Value

Type: Boolean

##### put(key, value) Stores the specified key/value pair as a cached entry in the cache partition. The put method can write only to the cache in your org’s

namespace.

Signature

```
   public void put(String key, Object value)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

Return Value

Type: void

##### put(key, value, visibility)

Stores the specified key/value pair as a cached entry in the cache partition and sets the cached value’s visibility.

Signature

```
   public void put(String key, Object value, cache.Visibility visibility)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

```
   visibility
```

Type: Cache.Visibility

Indicates whether the cached value is available only to Apex code that is executing in the same namespace or to Apex code executing
from any namespace.


Apex Reference Guide Partition Class

Return Value

Type: void

##### put(key, value, ttlSecs)

Stores the specified key/value pair as a cached entry in the cache partition and sets the cached value’s lifetime.

Signature

```
   public void put(String key, Object value, Integer ttlSecs)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

```
   ttlSecs
```

Type: Integer

The amount of time, in seconds, to keep the cached value in the cache.

Return Value

Type: void

##### put(key, value, ttlSecs, visibility, immutable)

Stores the specified key/value pair as a cached entry in the cache partition. This method also sets the cached value’s lifetime, visibility,
and whether it can be overwritten by another namespace.

Signature

```
   public void put(String key, Object value, Integer ttlSecs, cache.Visibility visibility,

   Boolean immutable)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

```
   ttlSecs
```

Type: Integer


Apex Reference Guide Partition Class

The amount of time, in seconds, to keep the cached value in the cache.

```
   visibility
```

Type: Cache.Visibility

Indicates whether the cached value is available only to Apex code that is executing in the same namespace or to Apex code executing
from any namespace.

```
   immutable
```

Type: Boolean

Indicates whether the cached value can be overwritten by another namespace ( `false` ) or not ( `true` ).

Return Value

Type: void

##### remove(key)

Deletes the cached value corresponding to the specified key from this cache partition.

Signature

```
   public Boolean remove(String key)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value.

Return Value

Type: Boolean

`true` if the cache value was successfully removed. Otherwise, `false` .

##### remove(cacheBuilder, key)

Deletes the cached value corresponding to the specified key from the partition cache. Use this method if your cached value is a class
that implements the `CacheBuilder` interface.

Signature

```
   public Boolean remove(System.Type cacheBuilder, String key)

```

Parameters

```
   cacheBuilder
```

Type: System.Type

The Apex class that implements the `CacheBuilder` interface.

```
   key
```

Type: String


Apex Reference Guide Partition Class

A case-sensitive string value that, combined with the class name corresponding to the _`cacheBuilder`_ parameter, uniquely
identifies a cached value.

Return Value

Type: Boolean

`true` if the cache value was successfully removed. Otherwise, `false` .

##### validateCacheBuilder(cacheBuilder)

Validates that the specified class implements the `CacheBuilder` interface.

Signature

```
   public static void validateCacheBuilder(System.Type cacheBuilder)

```

Parameters

```
   cacheBuilder
```

Type: System.Type

The class to validate.

Return Value

Type: void

##### validateKey(isDefault, key)

Validates a cache key. This method throws a `Cache.InvalidParamException` if the key is not valid. A valid key is not `null`
and contains alphanumeric characters.

Signature

```
   public static void validateKey(Boolean isDefault, String key)

```

Parameters

```
   isDefault
```

Type: Boolean

Set to `true` if the key references a default partition. Otherwise, set to `false` .

```
   key
```

Type: String

The key to validate.

Return Value

Type: void


Apex Reference Guide Partition Class

##### validateKeyValue(isDefault, key, value)

Validates a cache key and ensures that the cache value is non-null. This method throws a `Cache.InvalidParamException` if
the key or value is not valid. A valid key is not `null` and contains alphanumeric characters.

Signature

```
   public static void validateKeyValue(Boolean isDefault, String key, Object value)

```

Parameters

```
   isDefault
```

Type: Boolean

Set to `true` if the key references a default partition. Otherwise, set to `false` .

```
   key
```

Type: String

The key to validate.

```
   value
```

Type: Object

The cache value to validate.

Return Value

Type: void

##### validateKeys(isDefault, keys)

Validates the specified cache keys. This method throws a `Cache.InvalidParamException` if the key is not valid. A valid key
is not `null` and contains alphanumeric characters.

Signature

```
   public static void validateKeys(Boolean isDefault, Set<String> keys)

```

Parameters

```
   isDefault
```

Type: Boolean

Set to `true` if the key references a default partition. Otherwise, set to `false` .

```
   keys
```

Type: Set<String>

A set of key string values to validate.

Return Value

Type: void


### Apex Reference Guide Session Class

##### validatePartitionName(name)

Validates the partition name — for example, that it is not null.

Signature

```
   public static void validatePartitionName(String name)

```

Parameters

```
   name
```

Type: String

The name of the partition to validate.

Return Value

Type: void

### Session Class

Use the `Cache.Session` class to add, retrieve, and manage values in the session cache. The session cache is active as long as the
user’s Salesforce session is valid (the user is logged in, and the session is not expired).

Namespace

Cache

Usage

**Cache Key Format**

This table lists the format of the key parameter that some methods in this class take, such as `put`, `get`, and `contains` .

Note:

**•** If no default partition is specified in the org, calling a cache method without fully qualifying the key name causes a
`Cache.Session.SessionCacheException` to be thrown.

**•** The `local` prefix in an installed managed package refers to the namespace of the subscriber org and not the package’s
namespace. The cache `put` calls are not allowed in a partition that the invoking class doesn’t own.


Apex Reference Guide Session Class

Example

This class is the controller for a sample Visualforce page (shown in the subsequent code sample). The cached values are initially added
to the cache by the `init()` method, which the Visualforce page invokes when it loads through the `action` attribute. The cache
keys don’t contain the `namespace.partition` prefix. They all refer to a default partition in your org. The Visualforce page expects
a partition named `myPartition` . To run this sample, create a default partition in your org with the name `myPartition` .

The Visualforce page contains four output components. The first three components call `get` methods on the controller that return the
following values from the cache: a date, data based on the `MyData` inner class, and a counter. The next output component uses the
`$Cache.Session` global variable to get the cached string value for the key named `output` . Next, the `$Cache.Session` global
variable is used again in the Visualforce page to iterate over the elements of a cached value of type `List` . The size of the list is also
returned.

The Visualforce page also contains two buttons. The Rerender button invokes the `go()` method on the controller. This method increases
the values of the counter and the custom data in the cache. If you click **Rerender**, the two counters increase by one each time. The
`go()` method retrieves the values of these counters from the cache, increments their values by one, and stores them again in the
cache.

The Remove button deletes the date-time value (with key `datetime` ) from the cache. As a result, the value next to `Cached`
`datetime:` is cleared on the page.

```
   public class SessionCacheController {

      // Inner class.

      // Used as the data type of a cache value.

      class MyData {

        public String value { get; set; }

        public Integer counter { get; set; }

        public MyData(String value) {

           this.value = value;

           this.counter = 0;

        }

        public void inc() {

           counter++;

        }

        override public String toString() {

           return this.value + ':' + this.counter;

        }

      }

      // Apex List.

      // Used as the data type of a cached value.

      private List<String> numbers =

           new List<String> { 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE' };

      // Constructor of the controller for the Visualforce page.

      public SessionCacheController() {

      }

      // Adds various values to the cache.

      // This method is called when the Visualforce page loads.

      public void init() {

```


Apex Reference Guide Session Class

```
        // All key values are not qualified by the namespace.partition

        // prefix because they use the default partition.

        // Add counter to the cache with initial value of 0

        // or increment it if it's already there.

        if (!Cache.Session.contains('counter')) {

           Cache.Session.put('counter', 0);

        } else {

           Cache.Session.put('counter', getCounter() + 1);

        }

        // Add the datetime value to the cache only if it's not already there.

        if (!Cache.Session.contains('datetime')) {

           DateTime dt = DateTime.now();

           Cache.Session.put('datetime', dt);

        }

        // Add the custom data to the cache only if it's not already there.

        if (!Cache.Session.contains('data')) {

           Cache.Session.put('data', new MyData('Some custom value'));

        }

        // Add a list of number to the cache if not already there.

        if (!Cache.Session.contains('list')) {

           Cache.Session.put('list', numbers);

        }

        // Add a string value to the cache if not already there.

        if (!Cache.Session.contains('output')) {

           Cache.Session.put('output', 'Cached text value');

        }

      }

      // Return counter from the cache.

      public Integer getCounter() {

        return (Integer)Cache.Session.get('counter');

      }

      // Return datetime value from the cache.

      public String getCachedDatetime() {

        DateTime dt = (DateTime)Cache.Session.get('datetime');

        return dt != null ? dt.format() : null;

      }

      // Return cached value whose type is the inner class MyData.

      public String getCachedData() {

        MyData mydata = (MyData)Cache.Session.get('data');

        return mydata != null ? mydata.toString() : null;

      }

      // Method invoked by the Rerender button on the Visualforce page.

      // Updates the values of various cached values.

      // Increases the values of counter and the MyData counter if those

      // cache values are still in the cache.

```


Apex Reference Guide Session Class

```
      public PageReference go() {

        // Increase the cached counter value or set it to 0

        // if it's not cached.

        if (Cache.Session.contains('counter')) {

           Cache.Session.put('counter', getCounter() + 1);

        } else {

           Cache.Session.put('counter', 0);

        }

        // Get the custom data value from the cache.

        MyData d = (MyData)Cache.Session.get('data');

        // Only if the data is already in the cache, update it.

        if (Cache.Session.contains('data')) {

           d.inc();

           Cache.Session.put('data', d);

        }

        return null;

      }

      // Method invoked by the Remove button on the Visualforce page.

      // Removes the datetime cached value from the session cache.

      public PageReference remove() {

        Cache.Session.remove('datetime');

        return null;

      }

   }

```

This is the Visualforce page that corresponds to the `SessionCacheController` class.

```
   <apex:page controller="SessionCacheController" action="{!init}">

      <apex:outputPanel id="output">

        <br/>Cached datetime: <apex:outputText value="{!cachedDatetime}"/>

        <br/>Cached data: <apex:outputText value="{!cachedData}"/>

        <br/>Cached counter: <apex:outputText value="{!counter}"/>

        <br/>Output: <apex:outputText value="{!$Cache.Session.local.myPartition.output}"/>

        <br/>Repeat: <apex:repeat var="item"

   value="{!$Cache.Session.local.myPartition.list}">

           <apex:outputText value="{!item}"/>&nbsp;

        </apex:repeat>

        <br/>List size: <apex:outputText

   value="{!$Cache.Session.local.myPartition.list.size}"/>

      </apex:outputPanel>

      <br/><br/>

      <apex:form >

        <apex:commandButton id="go" action="{!go}" value="Rerender" rerender="output"/>

        <apex:commandButton id="remove" action="{!remove}" value="Remove datetime Key"

   rerender="output"/>

      </apex:form>

   </apex:page>

```


Apex Reference Guide Session Class

This is the output of the page after clicking the Rerender button twice. The counter value could differ in your case if a key named
`counter` was already in the cache before running this sample.

```
   Cached datetime:8/11/2015 1:58 PM

   Cached data:Some custom value:2

   Cached counter:2

   Output:Cached text value

   Repeat:ONE TWO THREE FOUR FIVE

   List size:5

```

IN THIS SECTION:

#### Session Constants

The Session class provides a constant that you can use when setting the time-to-live (TTL) value.

#### Session Methods

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

#### Session Constants

The Session class provides a constant that you can use when setting the time-to-live (TTL) value.

**Constant** **Description**

`MAX_TTL_SECS` Represents the maximum amount of time, in seconds, to keep the cached value in the
session cache.

#### Session Methods The following are methods for Session . All methods are static.

IN THIS SECTION:

contains(key)
Returns `true` if the session cache contains a cached value corresponding to the specified key.

contains(setOfKeys)
Returns `true` if the cache contains values for a specified set of keys.

get(key)
Returns the cached value corresponding to the specified key from the session cache.

get(keys)
Returns the cached values corresponding to the specified set of keys from the session cache.

get(cacheBuilder, key)
Returns the cached value corresponding to the specified key from the session cache. Use this method if your cached value is a class
that implements the `CacheBuilder` interface.


Apex Reference Guide Session Class

getAvgGetSize()
Returns the average item size of all the keys fetched from the session cache, in bytes.

getAvgGetTime()
Returns the average time taken to get a key from the session cache, in nanoseconds.

getAvgValueSize()
**Deprecated and available only in API versions 49.0 and earlier.** Returns the average item size for keys in the session cache, in
bytes.

getCapacity()
Returns the percentage of session cache capacity that has been used.

getKeys()
Returns all keys that are stored in the session cache and visible to the invoking namespace.

getMaxGetSize()
Returns the maximum item size of all the keys fetched from the session cache, in bytes.

getMaxGetTime()
Returns the maximum time taken to get a key from the session cache, in nanoseconds.

getMaxValueSize()
**Deprecated and available only in API versions 49.0 and earlier.** Returns the maximum item size for keys in the session cache,
in bytes.

getMissRate()
Returns the miss rate in the session cache.

getName()
Returns the name of the default cache partition.

getNumKeys()
Returns the total number of keys in the session cache.

getPartition(partitionName)
Returns a partition from the session cache that corresponds to the specified partition name.

isAvailable()
Returns `true` if the session cache is available for use. The session cache isn’t available when an active session isn’t present, such
as in asynchronous Apex or code called by asynchronous Apex. For example, if batch Apex causes an Apex trigger to execute, the
session cache isn’t available in the trigger because the trigger runs in asynchronous context.

put(key, value)
Stores the specified key/value pair as a cached entry in the session cache. The `put` method can write only to the cache in your org’s
namespace.

put(key, value, visibility)
Stores the specified key/value pair as a cached entry in the session cache and sets the cached value’s visibility.

put(key, value, ttlSecs)
Stores the specified key/value pair as a cached entry in the session cache and sets the cached value’s lifetime.

put(key, value, ttlSecs, visibility, immutable)
Stores the specified key/value pair as a cached entry in the session cache. This method also sets the cached value’s lifetime, visibility,
and whether it can be overwritten by another namespace.


Apex Reference Guide Session Class

remove(key)
Deletes the cached value corresponding to the specified key from the session cache.

remove(cacheBuilder, key)
Deletes the cached value corresponding to the specified key from the session cache. Use this method if your cached value is a class
that implements the `CacheBuilder` interface.

##### contains(key)

Returns `true` if the session cache contains a cached value corresponding to the specified key.

Signature

```
   public static Boolean contains(String key)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value. For information about the format of the key name, see Usage.

Return Value

Type: Boolean

`true` if a cache entry is found. Othewise, `false` .

##### contains(setOfKeys)

Returns `true` if the cache contains values for a specified set of keys.

Signature

```
   public static Map <String, Boolean> contains (Set<String> keys)

```

Parameters

```
   setOfKeys
```

Type: Set <String>

A set of keys that uniquely identifies cached values. For information about the format of the key name, see Usage.

Return Value

Type: Map <String, Boolean>

Returns the cache key and corresponding Boolean value indicating that the key entry exists. The Boolean value is `false` if the key
entry doesn't exist.

Usage

The number of input keys cannot exceed the maximum limit of 10.


Apex Reference Guide Session Class

Example

In this example, the code checks for the presence of multiple keys on the default partition. It fetches the cache key and the corresponding
Boolean value for the key entry from the session cache of the default partition.

```
   Set<String> keys = new Set<String>{'key1','key2','key3','key4','key5'};

   Map<String,Boolean> result = Cache.Session.contains(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('Is Key Present in the cache : ' + result.get(key));

   }

```

In this example, the code checks for the presence of multiple keys on different partitions. It fetches the cache key and the corresponding
Boolean value for the key entry from the session cache of different partitions.

```
   // Assuming there are three partitions p1, p2, p3 with default 'local' namespace

   Set<String> keys = new Set<String>{'local.p1.key','local.p2.key', 'local.p3.key'};

   Map<String,Boolean> result = Cache.Session.contains(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('Is Key Present in the cache : + result.get(key));

   }

##### get(key)

```

Returns the cached value corresponding to the specified key from the session cache.

Signature

```
   public static Object get(String key)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value. For information about the format of the key name, see Usage.

Return Value

Type: Object

The cached value as a generic object type. Cast the returned value to the appropriate type.

Usage

Because `Cache.Session.get()` returns an object, we recommend that you cast the returned value to a specific type to facilitate
use of the returned value.

```
   // Get a cached value

   Object obj = Cache.Session.get('ns1.partition1.orderDate');

   // Cast return value to a specific data type

   DateTime dt2 = (DateTime)obj;

```


Apex Reference Guide Session Class

If a `Cache.Session.get()` call doesn’t find the referenced key, it returns `null` .

##### get(keys)

Returns the cached values corresponding to the specified set of keys from the session cache.

Signature

```
   public static Map <String, Object> get (Set <String> keys)

```

Parameters

```
   keys
```

Type: Set <String>

A set of keys that uniquely identify cached values. For information about the format of the key name, see Usage.

Return Value

Type: Map <String, Object>

Returns the cache key and corresponding value. Returns null when no corresponding value is found for an input key.

Usage

The number of input keys cannot exceed the maximum limit of 10.

Example

Fetch multiple keys from the session cache of the default partition.

```
   Set<String> keys = new Set<String>{'key1','key2','key3','key4','key5'};

   Map<String,Object> result = Cache.Session.get(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('value: ' + result.get(key));

   }

```

Fetch multiple keys from the session cache of different partitions.

```
   // Assuming there are three partitions p1, p2, p3 with default 'local' namespace

   Set<String> keys = new Set<String>{'local.p1.key','local.p2.key', 'local.p3.key'};

   Map<String,Object> result = Cache.Session.get(keys);

   for(String key : result.keySet()) {

      system.debug('key: ' + key);

      system.debug('value: ' + result.get(key));

   }

##### get(cacheBuilder, key)

```

Returns the cached value corresponding to the specified key from the session cache. Use this method if your cached value is a class that
implements the `CacheBuilder` interface.


Apex Reference Guide Session Class

Signature

```
   public static Object get(System.Type cacheBuilder, String key)

```

Parameters

```
   cacheBuilder
```

Type: System.Type

The Apex class that implements the `CacheBuilder` interface.

```
   key
```

Type: String

A case-sensitive string value that, combined with the class name corresponding to the _`cacheBuilder`_ parameter, uniquely
identifies a cached value.

Return Value

Type: Object

The cached value as a generic object type. Cast the returned value to the appropriate type.

Usage

Because `Cache.Session.get(` _`cacheBuilder`_ `,` _`key`_ `)` returns an object, cast the returned value to a specific type to facilitate
use of the returned value.

```
   return ((DateTime)Cache.Session.get(DateCache.class, 'datetime')).format();

##### getAvgGetSize()

```

Returns the average item size of all the keys fetched from the session cache, in bytes.

Signature

```
   public static Long getAvgGetSize()

```

Return Value

Type: Long

##### getAvgGetTime()

Returns the average time taken to get a key from the session cache, in nanoseconds.

Signature

```
   public static Long getAvgGetTime()

```

Return Value

Type: Long


Apex Reference Guide Session Class

##### getAvgValueSize()

**Deprecated and available only in API versions 49.0 and earlier.** Returns the average item size for keys in the session cache, in bytes.

Signature

```
   public static Long getAvgValueSize()

```

Return Value

Type: Long

##### getCapacity()

Returns the percentage of session cache capacity that has been used.

Signature

```
   public static Double getCapacity()

```

Return Value

Type: Double

Used cache as a percentage number.

##### getKeys()

Returns all keys that are stored in the session cache and visible to the invoking namespace.

Signature

```
   public static Set<String> getKeys()

```

Return Value

Type: Set<String>

A set containing all cache keys.

##### getMaxGetSize()

Returns the maximum item size of all the keys fetched from the session cache, in bytes.

Signature

```
   public static Long getMaxGetSize()

```

Return Value

Type: Long


Apex Reference Guide Session Class

##### getMaxGetTime()

Returns the maximum time taken to get a key from the session cache, in nanoseconds.

Signature

```
   public static Long getMaxGetTime()

```

Return Value

Type: Long

##### getMaxValueSize()

**Deprecated and available only in API versions 49.0 and earlier.** Returns the maximum item size for keys in the session cache, in
bytes.

Signature

```
   public static Long getMaxValueSize()

```

Return Value

Type: Long

##### getMissRate()

Returns the miss rate in the session cache.

Signature

```
   public static Double getMissRate()

```

Return Value

Type: Double

##### getName()

Returns the name of the default cache partition.

Signature

```
   public String getName()

```

Return Value

Type: String

The name of the default cache partition.


Apex Reference Guide Session Class

##### getNumKeys()

Returns the total number of keys in the session cache.

Signature

```
   public static Long getNumKeys()

```

Return Value

Type: Long

##### getPartition(partitionName)

Returns a partition from the session cache that corresponds to the specified partition name.

Signature

```
   public static cache.SessionPartition getPartition(String partitionName)

```

Parameters

```
   partitionName
```

Type: String

A partition name that is qualified by the namespace, for example, _`namespace.partition`_ .

Return Value

Type: Cache.SessionPartition

Example

After you get the session partition, you can add and retrieve the partition’s cache values.

```
   // Get partition

   Cache.SessionPartition sessionPart = Cache.Session.getPartition('myNs.myPartition');

   // Retrieve cache value from the partition

   if (sessionPart.contains('BookTitle')) {

      String cachedTitle = (String)sessionPart.get('BookTitle');

   }

   // Add cache value to the partition

   sessionPart.put('OrderDate', Date.today());

   // Or use dot notation to call partition methods

   String cachedAuthor =

   (String)Cache.Session.getPartition('myNs.myPartition').get('BookAuthor');

```


Apex Reference Guide Session Class

##### isAvailable()

Returns `true` if the session cache is available for use. The session cache isn’t available when an active session isn’t present, such as in
asynchronous Apex or code called by asynchronous Apex. For example, if batch Apex causes an Apex trigger to execute, the session
cache isn’t available in the trigger because the trigger runs in asynchronous context.

Signature

```
   public static Boolean isAvailable()

```

Return Value

Type: Boolean

`true` if the session cache is available. Otherwise, `false` .

##### put(key, value) Stores the specified key/value pair as a cached entry in the session cache. The put method can write only to the cache in your org’s

namespace.

Signature

```
   public static void put(String key, Object value)

```

Parameters

```
   key
```

Type: String

A string that uniquely identifies the value to be cached. For information about the format of the key name, see Usage.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

Return Value

Type: void

##### put(key, value, visibility)

Stores the specified key/value pair as a cached entry in the session cache and sets the cached value’s visibility.

Signature

```
   public static void put(String key, Object value, Cache.Visibility visibility)

```

Parameters

```
   key
```

Type: String


Apex Reference Guide Session Class

A string that uniquely identifies the value to be cached. For information about the format of the key name, see Usage.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

```
   visibility
```

Type: Cache.Visibility

Indicates whether the cached value is available only to Apex code that is executing in the same namespace or to Apex code executing
from any namespace.

Return Value

Type: void

##### put(key, value, ttlSecs)

Stores the specified key/value pair as a cached entry in the session cache and sets the cached value’s lifetime.

Signature

```
   public static void put(String key, Object value, Integer ttlSecs)

```

Parameters

```
   key
```

Type: String

A string that uniquely identifies the value to be cached. For information about the format of the key name, see Usage.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

```
   ttlSecs
```

Type: Integer

The amount of time, in seconds, to keep the cached value in the session cache. The cached values remain in the cache as long as
the Salesforce session hasn’t expired. The maximum value is 28,800 seconds or eight hours. The minimum value is 300 seconds or
five minutes.

Return Value

Type: void

##### put(key, value, ttlSecs, visibility, immutable)

Stores the specified key/value pair as a cached entry in the session cache. This method also sets the cached value’s lifetime, visibility,
and whether it can be overwritten by another namespace.


Apex Reference Guide Session Class

Signature

```
   public static void put(String key, Object value, Integer ttlSecs, cache.Visibility

   visibility, Boolean immutable)

```

Parameters

```
   key
```

Type: String

A string that uniquely identifies the value to be cached. For information about the format of the key name, see Usage.

```
   value
```

Type: Object

The value to store in the cache. The cached value must be serializable.

```
   ttlSecs
```

Type: Integer

The amount of time, in seconds, to keep the cached value in the session cache. The cached values remain in the cache as long as
the Salesforce session hasn’t expired. The maximum value is 28,800 seconds or eight hours. The minimum value is 300 seconds or
five minutes.

```
   visibility
```

Type: Cache.Visibility

Indicates whether the cached value is available only to Apex code that is executing in the same namespace or to Apex code executing
from any namespace.

```
   immutable
```

Type: Boolean

Indicates whether the cached value can be overwritten by another namespace ( `false` ) or not ( `true` ).

Return Value

Type: void

##### remove(key)

Deletes the cached value corresponding to the specified key from the session cache.

Signature

```
   public static Boolean remove(String key)

```

Parameters

```
   key
```

Type: String

A case-sensitive string value that uniquely identifies a cached value. For information about the format of the key name, see Usage.

Return Value

Type: Boolean


### Apex Reference Guide SessionPartition Class

`true` if the cache value was successfully removed. Otherwise, `false` .

##### remove(cacheBuilder, key)

Deletes the cached value corresponding to the specified key from the session cache. Use this method if your cached value is a class that
implements the `CacheBuilder` interface.

Signature

```
   public static Boolean remove(System.Type cacheBuilder, String key)

```

Parameters

```
   cacheBuilder
```

Type: System.Type

The Apex class that implements the `CacheBuilder` interface.

```
   key
```

Type: String

A case-sensitive string value that, combined with the class name corresponding to the _`cacheBuilder`_ parameter, uniquely
identifies a cached value.

Return Value

Type: Boolean

`true` if the cache value was successfully removed. Otherwise, `false` .

### SessionPartition Class

Contains methods to manage cache values in the session cache of a specific partition.

Namespace

Cache

Usage

This class extends Cache.Partition and inherits all of its non-static methods. Utility methods for creating and validating keys are not
supported and can be called only from the `Cache.Partition` parent class. For a list of `Cache.Partition` methods, see
Partition Methods.

To get a session partition, call `Cache.Session.getPartition` and pass in a fully qualified partition name, as follows.

```
   Cache.SessionPartition sessionPartition =

   Cache.Session.getPartition('namespace.myPartition');

```

See Cache Key Format for Partition Methods.


Apex Reference Guide SessionPartition Class

Example

This class is the controller for a sample Visualforce page (shown in the subsequent code sample). The controller shows how to use the
methods of `Cache.SessionPartition` to manage a cache value on a particular partition. The controller takes inputs from the
Visualforce page for the partition name, key name for a counter, and initial counter value. The controller contains default values for these
inputs. When you click **Rerender** on the Visualforce page, the `go()` method is invoked and increases the counter by one. When you
click **Remove Key**, the counter key is removed from the cache. The counter value gets reset to its initial value when it’s re-added to the
cache.

```
   public class SessionPartitionController {

     // Name of a partition in the local namespace

     String partitionInput = 'local.myPartition';

     // Name of the key

     String counterKeyInput = 'counter';

     // Key initial value

     Integer counterInitValue = 0;

     // Session partition object

     Cache.SessionPartition sessionPartition;

      // Constructor of the controller for the Visualforce page.

      public SessionPartitionController() {

      }

      // Adds counter value to the cache.

      // This method is called when the Visualforce page loads.

      public void init() {

        // Create the partition instance based on the partition name

        sessionPartition = getPartition();

        // Add counter to the cache with an initial value

        // or increment it if it's already there.

        if (!sessionPartition.contains(counterKeyInput)) {

           sessionPartition.put(counterKeyInput, counterInitValue);

        } else {

           sessionPartition.put(counterKeyInput, getCounter() + 1);

        }

      }

      // Returns the session partition based on the partition name

      // given in the Visualforce page or the default value.

      private Cache.SessionPartition getPartition() {

        if (sessionPartition == null) {

           sessionPartition = Cache.Session.getPartition(partitionInput);

        }

        return sessionPartition;

      }

      // Return counter from the cache.

      public Integer getCounter() {

        return (Integer)getPartition().get(counterKeyInput);

      }

```


Apex Reference Guide SessionPartition Class

```
      // Invoked by the Submit button to save input values

      // supplied by the user.

      public PageReference save() {

        // Reset the initial key value in the cache

        getPartition().put(counterKeyInput, counterInitValue);

        return null;

      }

      // Method invoked by the Rerender button on the Visualforce page.

      // Updates the values of various cached values.

      // Increases the values of counter and the MyData counter if those

      // cache values are still in the cache.

      public PageReference go() {

        // Get the partition object

        sessionPartition = getPartition();

        // Increase the cached counter value or set it to 0

        // if it's not cached.

        if (sessionPartition.contains(counterKeyInput)) {

           sessionPartition.put(counterKeyInput, getCounter() + 1);

        } else {

           sessionPartition.put(counterKeyInput, counterInitValue);

        }

        return null;

      }

      // Method invoked by the Remove button on the Visualforce page.

      // Removes the datetime cached value from the session cache.

      public PageReference remove() {

        getPartition().remove(counterKeyInput);

        return null;

      }

      // Get and set methods for accessing variables

      // that correspond to the input text fields on

      // the Visualforce page.

      public String getPartitionInput() {

        return partitionInput;

      }

      public String getCounterKeyInput() {

        return counterKeyInput;

      }

      public Integer getCounterInitValue() {

        return counterInitValue;

      }

      public void setPartitionInput(String partition) {

        this.partitionInput = partition;

      }

```


### Apex Reference Guide Cache Exceptions

```
      public void setCounterKeyInput(String keyName) {

        this.counterKeyInput = keyName;

      }

      public void setCounterInitValue(Integer counterValue) {

        this.counterInitValue = counterValue;

      }

   }

```

This is the Visualforce page that corresponds to the `SessionPartitionController` class.

```
   <apex:page controller="SessionPartitionController" action="{!init}">

      <apex:form >

        <br/>Partition with Namespace Prefix: <apex:inputText value="{!partitionInput}"/>

        <br/>Counter Key Name: <apex:inputText value="{!counterKeyInput}"/>

        <br/>Counter Initial Value: <apex:inputText value="{!counterInitValue}"/>

        <apex:commandButton action="{!save}" value="Save Key Input Values"/>

      </apex:form>

      <apex:outputPanel id="output">

        <br/>Cached Counter: <apex:outputText value="{!counter}"/>

      </apex:outputPanel>

      <br/>

      <apex:form >

        <apex:commandButton id="go" action="{!go}" value="Rerender" rerender="output"/>

        <apex:commandButton id="remove" action="{!remove}" value="Remove Key"

   rerender="output"/>

      </apex:form>

   </apex:page>

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

### Cache Exceptions The Cache namespace contains exception classes.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions on page 3882 in the _Apex Developer Guide_ .

### The Cache namespace contains these exceptions.

**Exception** **Thrown when**

`Cache.Session.SessionCacheException` An error occurred while adding or retrieving a value in the session
cache.

`Cache.Session.SessionCacheNoSessionException` An attempt is made to access the cache when the session cache
isn’t available.


### Apex Reference Guide Visibility Enum

**Exception** **Thrown when**

`Cache.Org.OrgCacheException` An attempt is made to access a partition that doesn’t exist or whose
name is invalid.

`Cache.InvalidParamException` An invalid parameter value is passed into a method of
`Cache.Session` or `Cache.Org` . This error occurs when:

**•** The key referenced is null or empty or is not alphanumeric.

**•** The key isn’t qualified with the namespace and partition in the
format `<namespace>.<partition>.<key>` .

**•** The key isn’t qualified in the format `<key>` for the default
partition, or for a key inserted through the partition object.

**•** The namespace referenced is null or empty.

**•** The partition name is null or empty or is not alphanumeric.

**•** Another referenced value is null.

`Cache.ItemSizeLimitExceededException` A cache `put` call is made with an item that exceeds the maximum
size limit. To fix this error, break the item into multiple, smaller items.

```
Cache.BulkApiKeysLimitExceededException

Cache.PlatformCacheInvalidOperationException

Cache.CacheBuilderExecutionException

```

The number of key parameters passed into a bulk method `get(keys)` or `contains(setOfKeys)` exceeds the
maximum limit of 10.

A cache `put` or `remove` call is made that is not allowed. For
example, when calling `put` or `remove` inside a Visualforce
constructor.

This error occurs when the execution of the CacheBuilder fails; this
could be due to an error in parsing, a permissions error while
accessing records, or an issue with Apex callouts.

`Cache.InvalidCacheBuilderException` A `get(CacheBuilder cb, String key)`,
`remove(CacheBuilder cb, String key)`, or

`validateCacheBuilder(CacheBuilder cb)` method
is called but the `cb` parameter is a class that does not implement
the `Cache.CacheBuilder` interface.

### Visibility Enum

Use the `Cache.Visibility` enumeration in the `Cache.Session` or `Cache.Org` methods to indicate whether a cached
value is visible only in the value’s namespace or in all namespaces.

Enum Values

The following are the values of the `Cache.Visibility` enum.


## Apex Reference Guide Canvas Namespace

**Value** **Description**

`ALL` The cached value is available to Apex code executing
from any namespace. This is the default state.

```
NAMESPACE

## Canvas Namespace

```

The cached value is available to Apex code executing
from the same namespace.

If a key has the `Visibility.NAMESPACE`
attribute, a `get` method initiated from a different
namespace returns `null` .

## The Canvas namespace provides an interface and classes for canvas apps in Salesforce. The following are the interfaces and classes in the Canvas namespace.

IN THIS SECTION:

### ApplicationContext Interface

Use this interface to retrieve application context information, such as the application version or URL.

CanvasLifecycleHandler Interface
Implement this interface to control context information and add custom behavior during the application render phase.

ContextTypeEnum Enum
Describes context data that can be excluded from canvas app context data. You specify which context types to exclude in the
`excludeContextTypes()` method in your `CanvasLifecycleHandler` implementation.

EnvironmentContext Interface
Use this interface to retrieve environment context information, such as the app display location or the configuration parameters.

RenderContext Interface
A wrapper interface that is used to retrieve application and environment context information.

Test Class
Contains methods for automated testing of your Canvas classes.

Canvas Exceptions
## The Canvas namespace contains exception classes.

SEE ALSO:

[Canvas Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/canvas_framework_intro.htm)

### ApplicationContext Interface

Use this interface to retrieve application context information, such as the application version or URL.


Apex Reference Guide ApplicationContext Interface

Namespace

Canvas

Usage

#### The ApplicationContext interface provides methods to retrieve application information about the canvas app that’s being

rendered. Most of the methods are read-only. For this interface, you don’t need to create an implementation. Use the default
implementation that Salesforce provides.

IN THIS SECTION:

#### ApplicationContext Methods ApplicationContext Methods The following are methods for ApplicationContext .

IN THIS SECTION:

##### getCanvasUrl()

Retrieves the fully qualified URL of the canvas app.

getDeveloperName()
Retrieves the internal API name of the canvas app.

getName()
Retrieves the name of the canvas app.

getNamespace()
Retrieves the namespace prefix of the canvas app.

getVersion()
Retrieves the current version of the canvas app.

setCanvasUrlPath(newPath)
Overrides the URL of the canvas app for the current request.

##### getCanvasUrl()

Retrieves the fully qualified URL of the canvas app.

Signature

```
   public String getCanvasUrl()

```

Return Value

Type: String


Apex Reference Guide ApplicationContext Interface

Usage

Use this method to get the URL of the canvas app, for example:
`http://instance.salesforce.com:8080/canvas_app_path/canvas_app.jsp` .

##### getDeveloperName()

Retrieves the internal API name of the canvas app.

Signature

```
   public String getDeveloperName()

```

Return Value

Type: String

Usage

Use this method to get the API name of the canvas app. You specify this value in the `API Name` field when you expose the canvas
app by creating a connected app.

##### getName()

Retrieves the name of the canvas app.

Signature

```
   public String getName()

```

Return Value

Type: String

Usage

Use this method to get the name of the canvas app.

##### getNamespace()

Retrieves the namespace prefix of the canvas app.

Signature

```
   public String getNamespace()

```

Return Value

Type: String


Apex Reference Guide ApplicationContext Interface

Usage

Use this method to get the Salesforce namespace prefix that’s associated with the canvas app.

##### getVersion()

Retrieves the current version of the canvas app.

Signature

```
   public String getVersion()

```

Return Value

Type: String

Usage

Use this method to get the current version of the canvas app. This value changes after you update and republish a canvas app in an
organization. If you are in a Developer Edition organization, using this method always returns the latest version.

##### setCanvasUrlPath(newPath)

Overrides the URL of the canvas app for the current request.

Signature

```
   public void setCanvasUrlPath(String newPath)

```

Parameters

```
   newPath
```

Type: String

The URL (not including domain) that you need to use to override the canvas app URL.

Return Value

Type: Void

Usage

Use this method to override the URL path and query string of the canvas app. Do not provide a fully qualified URL, because the provided
URL string will be appended to the original canvas URL domain.

For example, if the current canvas app URL is `https://myserver.com:6000/myAppPath` and you call
`setCanvasUrlPath('/alternatePath/args?arg1=1&arg2=2')`, the adjusted canvas app URL will be
`https://myserver.com:6000/alternatePath/args?arg1=1&arg2=2` .

If the provided path results in a malformed URL, or a URL that exceeds 2,048 characters, a System.CanvasException will be thrown.

This method overrides the canvas app URL for the current request and does not permanently change the canvas app URL as configured
in the UI for the Salesforce canvas app settings.


### Apex Reference Guide CanvasLifecycleHandler Interface CanvasLifecycleHandler Interface

Implement this interface to control context information and add custom behavior during the application render phase.

Namespace

### Canvas

Usage

Use this interface to specify what canvas context information is provided to your app by implementing the `excludeContextTypes()`
method. Use this interface to call custom code when the app is rendered by implementing the `onRender()` method.

If you provide an implementation of this interface, you must implement `excludeContextTypes()` and `onRender()` .

Example Implementation

The following example shows a simple implementation of CanvasLifecycleHandler that specifies that organization context information
will be excluded and prints a debug message when the app is rendered.

```
   public class MyCanvasListener

   implements Canvas.CanvasLifecycleHandler{

      public Set<Canvas.ContextTypeEnum> excludeContextTypes(){

        Set<Canvas.ContextTypeEnum> excluded = new Set<Canvas.ContextTypeEnum>();

        excluded.add(Canvas.ContextTypeEnum.ORGANIZATION);

        return excluded;

      }

      public void onRender(Canvas.RenderContext renderContext){

        System.debug('Canvas lifecycle called.');

      }

   }

```

IN THIS SECTION:

#### CanvasLifecycleHandler Methods

SEE ALSO:

_Canvas Developer Guide_ [: Customizing Your App Lifecycle](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/canvas_customizing_app_lifecycle.htm)

#### CanvasLifecycleHandler Methods

### The following are methods for CanvasLifecycleHandler .

IN THIS SECTION:

excludeContextTypes()
Lets the implementation exclude parts of the CanvasRequest context, if the application does not need it.


Apex Reference Guide CanvasLifecycleHandler Interface

##### onRender(renderContext)

Invoked when a canvas app is rendered. Provides the ability to set and retrieve canvas application and environment context information
during the application render phase.

##### excludeContextTypes()

Lets the implementation exclude parts of the CanvasRequest context, if the application does not need it.

Signature

```
   public Set<Canvas.ContextTypeEnum> excludeContextTypes()

```

Return Value

Type: SET<Canvas.ContextTypeEnum>

This method must return `null` or a set of zero or more ContextTypeEnum values. Returning `null` enables all attributes by default.
ContextTypeEnum values that can be set are:

**•** Canvas.ContextTypeEnum.ORGANIZATION

**•** Canvas.ContextTypeEnum.RECORD_DETAIL

**•** Canvas.ContextTypeEnum.USER

See ContextTypeEnum on page 285 for more details on these values.

Usage

Implement this method to specify which attributes to disable in the context of the canvas app. A disabled attribute will set the associated
canvas context information to null.

Disabling attributes can help improve performance by reducing the size of the signed request and canvas context. Also, disabled attributes
do not need to be retrieved by Salesforce, which further improves performance.

See the _[Canvas Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/)_ for more information on context information in the Context object that’s provided in the CanvasRequest.

Example

This example implementation specifies that the organization information will be disabled in the canvas context.

```
   public Set<Canvas.ContextTypeEnum> excludeContextTypes() {

      Set<Canvas.ContextTypeEnum> excluded = new Set<Canvas.ContextTypeEnum>();

      excluded.add(Canvas.ContextTypeEnum.ORGANIZATION);

      return excluded;

   }

```

SEE ALSO:

_Canvas Developer Guide_ [: Filtering CanvasRequest Context Data](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/canvas_filtering_context_data.htm)

##### onRender(renderContext)

Invoked when a canvas app is rendered. Provides the ability to set and retrieve canvas application and environment context information
during the application render phase.


### Apex Reference Guide ContextTypeEnum Enum

Signature

```
   public void onRender(Canvas.RenderContext renderContext)

```

Parameters

```
   renderContext
```

Type: Canvas.RenderContext

Return Value

Type: Void

Usage

If implemented, this method is called whenever the canvas app is rendered. The implementation can set and retrieve context information
by using the provided Canvas.RenderContext.

[This method is called whenever signed request or context information is retrieved by the client. See the Canvas Developer Guide for](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/)
more information on signed request authentication.

Example

This example implementation prints ‘Canvas lifecycle called.’ to the debug log when the canvas app is rendered.

```
   public void onRender(Canvas.RenderContext renderContext) {

      System.debug('Canvas lifecycle called.');

   }

```

SEE ALSO:

_Canvas Developer Guide_ [: Controlling App Behavior](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/canvas_controlling_app_behavior.htm)

### ContextTypeEnum Enum

Describes context data that can be excluded from canvas app context data. You specify which context types to exclude in the
`excludeContextTypes()` method in your `CanvasLifecycleHandler` implementation.

Namespace

Canvas

Enum Values

**Value** **Description**

`ORGANIZATION` Exclude context information about the organization in which the canvas app is
running.

`RECORD_DETAIL` Exclude context information about the object record on which the canvas app
appears.


### Apex Reference Guide EnvironmentContext Interface

**Value** **Description**

`USER` Exclude context information about the current user.

### EnvironmentContext Interface

Use this interface to retrieve environment context information, such as the app display location or the configuration parameters.

Namespace

Canvas

Usage

### The EnvironmentContext interface provides methods to retrieve environment information about the current canvas app. For

this interface, you don’t need to create an implementation. Use the default implementation that Salesforce provides.

IN THIS SECTION:

#### EnvironmentContext Methods EnvironmentContext Methods

### The following are methods for EnvironmentContext .

IN THIS SECTION:

addEntityField(fieldName)
Adds a field to the list of object fields that are returned in the signed request Record object when the component appears on a
Visualforce page that’s placed on an object.

addEntityFields(fieldNames)
Adds a set of fields to the list of object fields that are returned in the signed request Record object when the component appears
on a Visualforce page that’s placed on an object.

getDisplayLocation()
Retrieves the display location where the canvas app is being called from. For example, a value of Visualforce page.

getEntityFields()
Retrieves the list of object fields that are returned in the signed request Record object when the component appears on a Visualforce
page that’s placed on an object.

getLocationUrl()
Retrieves the location URL of the canvas app.

getParametersAsJSON()
Retrieves the current custom parameters for the canvas app. Parameters are returned as a JSON string.

getSublocation()
Retrieves the display sublocation where the canvas app is being called from.


Apex Reference Guide EnvironmentContext Interface

setParametersAsJSON(jsonString)
Sets the custom parameters for the canvas app.

##### addEntityField(fieldName)

Adds a field to the list of object fields that are returned in the signed request Record object when the component appears on a Visualforce
page that’s placed on an object.

Signature

```
   public void addEntityField(String fieldName)

```

Parameters

```
   fieldName
```

Type: String

The object field name that you need to add to the list of returned fields., Using ‘*’ adds all fields that the user has permission to view.

Return Value

Type: Void

Usage

When you use the `<apex:canvasApp>` component to display a canvas app on a Visualforce page, and that page is associated with
[an object (placed on the page layout, for example), you can specify fields to be returned from the related object. See the Canvas Developer](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/)
[Guide for more information on the Record object.](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/)

Use `addEntityField()` to add a field to the list of object fields that are returned in the signed request Record object. By default
the list of fields includes ID. You can add fields by name or add all fields that the user has permission to view by calling
`addEntityField('*')` .

You can inspect the configured list of fields by using Canvas.EnvironmentContext. `getEntityFields()` .

Example

This example adds the Name and BillingAddress fields to the list of object fields. This example assumes the canvas app will appear in a
Visualforce page that's associated with the Account page layout.

```
   Canvas.EnvironmentContext env = renderContext.getEnvironmentContext();

   // Add Name and BillingAddress to fields (assumes we'll run from the Account detail page)

   env.addEntityField('Name');

   env.addEntityField('BillingAddress');

##### addEntityFields(fieldNames)

```

Adds a set of fields to the list of object fields that are returned in the signed request Record object when the component appears on a
Visualforce page that’s placed on an object.


Apex Reference Guide EnvironmentContext Interface

Signature

```
   public void addEntityFields(Set<String> fieldNames)

```

Parameters

```
   fieldNames
```

Type: SET<String>

The set of object field names that you need to add to the list of returned fields. If an item in the set is ‘*’, all fields that the user has
permission to view are added.

Return Value

Type: Void

Usage

When you use the `<apex:canvasApp>` component to display a canvas app on a Visualforce page, and that page is associated with
an object (placed on the page layout, for example), you can specify fields to be returned from the related object. See the _[Canvas Developer](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/)_
_[Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/)_ for more information on the Record object.

Use `addEntityFields()` to add a set of one or more fields to the list of object fields that are returned in the signed request Record
object. By default the list of fields includes ID. You can add fields by name or add all fields that the user has permission to view by adding
a set that includes ‘*’ as one of the strings.

You can inspect the configured list of fields by using Canvas.EnvironmentContext. `getEntityFields()` .

Example

This example adds the Name, BillingAddress, and YearStarted fields to the list of object fields. This example assumes that the canvas app
will appear in a Visualforce page that’s associated with the Account page layout.

```
   Canvas.EnvironmentContext env = renderContext.getEnvironmentContext();

   // Add Name, BillingAddress and YearStarted to fields (assumes we'll run from the Account

    detail page)

   Set<String> fields = new Set<String>{'Name','BillingAddress','YearStarted'};

   env.addEntityFields(fields);

##### getDisplayLocation()

```

Retrieves the display location where the canvas app is being called from. For example, a value of Visualforce page.

Signature

```
   public String getDisplayLocation()

```

Return Value

Type: String

The return value can be one of the following strings:

**•** Chatter—The canvas app was called from the Chatter tab.


Apex Reference Guide EnvironmentContext Interface

**•** ChatterFeed—The canvas app was called from a Chatter canvas feed item.

**•** MobileNav—The canvas app was called from the navigation menu.

**•** OpenCTI—The canvas app was called from an Open CTI component.

**•** PageLayout—The canvas app was called from an element within a page layout. If the displayLocation is PageLayout, one of the
subLocation values might be returned.

**•** Publisher—The canvas app was called from a canvas custom quick action.

**•** ServiceDesk—The canvas app was called from a Salesforce Console component.

**•** Visualforce—The canvas app was called from a Visualforce page.

**•** None—The canvas app was called from the Canvas App Previewer.

Usage

Use this method to obtain the display location for the canvas app.

##### getEntityFields()

Retrieves the list of object fields that are returned in the signed request Record object when the component appears on a Visualforce
page that’s placed on an object.

Signature

```
   public List<String> getEntityFields()

```

Return Value

Type: LIST<String>

Usage

When you use the `<apex:canvasApp>` component to display a canvas app on a Visualforce page, and that page is associated with
an object (placed on the page layout, for example), you can specify fields to be returned from the related object. See the _[Canvas Developer](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/)_
_[Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/)_ for more information on the Record object.

Use getEntityFields() to retrieve the list of object fields that are returned in the signed request Record object. By default the list of fields
includes ID. The list of fields can be configured by using the Canvas.EnvironmentContext. `addEntityField(fieldName)` or
Canvas.EnvironmentContext. `addEntityFields(fieldNames)` methods.

Example

This example gets the current list of object fields and retrieves each item in the list, printing each field name to the debug log.

```
   Canvas.EnvironmentContext env = renderContext.getEnvironmentContext();

   List<String> entityFields = env.getEntityFields();

   for (String fieldVal : entityFields) {

      System.debug('Environment Context entityField: ' + fieldVal);

   }

```

If the canvas app that’s using this lifecycle code was run from the detail page of an Account, the debug log output might look like:

```
   Environment Context entityField: Id

```


Apex Reference Guide EnvironmentContext Interface

##### getLocationUrl()

Retrieves the location URL of the canvas app.

Signature

```
   public String getLocationUrl()

```

Return Value

Type: String

Usage

Use this method to obtain the URL of the page where the user accessed the canvas app. For example, if the user accessed your app by
clicking a link on the Chatter tab, this method returns the URL of the Chatter tab, which would be similar to
‘https:// _`MyDomainName`_ .my.salesforce.com/_ui/core/chatter/ui/ChatterPage’.

##### getParametersAsJSON()

Retrieves the current custom parameters for the canvas app. Parameters are returned as a JSON string.

Signature

```
   public String getParametersAsJSON()

```

Return Value

Type: String

Usage

Use this method to get the current custom parameters for the canvas app. The parameters are returned in a JSON string that can be
de-serialized by using the System.JSON. `deserializeUntyped(jsonString)` method.

Custom parameters can be modified by using the Canvas.EnvironmentContext. `setParametersAsJSON(jsonString)` string.

Example

This example gets the current custom parameters, de-serializes them into a map, and prints the results to the debug log.

```
   Canvas.EnvironmentContext env = renderContext.getEnvironmentContext();

   // Get current custom params

   Map<String, Object> currentParams =

      (Map<String, Object>) JSON.deserializeUntyped(env.getParametersAsJSON());

   System.debug('Environment Context custom paramters: ' + currentParams);

##### getSublocation()

```

Retrieves the display sublocation where the canvas app is being called from.


Apex Reference Guide EnvironmentContext Interface

Signature

```
   public String getSublocation()

```

Return Value

Type: String

The return value can be one of the following strings:

**•** S1MobileCardFullview—The canvas app was called from a mobile card.

**•** S1MobileCardPreview—The canvas app was called from a mobile card preview. The user must click the preview to open the app.

**•** S1RecordHomePreview—The canvas app was called from a record detail page preview. The user must click the preview to open
the app.

**•** S1RecordHomeFullview—The canvas app was called from a page layout.

Usage

Use this method to obtain the display sublocation for the canvas app. Use only if the primary display location can be displayed on mobile
devices.

##### setParametersAsJSON(jsonString)

Sets the custom parameters for the canvas app.

Signature

```
   public void setParametersAsJSON(String jsonString)

```

Parameters

```
   jsonString
```

Type: String

The custom parameters that you need to set, serialized into a JSON format string.

Return Value

Type: Void

Usage

Use this method to set the current custom parameters for the canvas app. The parameters must be provided in a JSON string. You can
use the System.JSON. `serialize(objectToSerialize)` method to serialize a map into a JSON string.

Setting the custom parameters will overwrite the custom parameters that are set for the current request. If you need to modify the
current custom parameters, first get the current set of custom parameters by using `getParametersAsJSON()`, modify the retrieved
parameter set as needed, and then use this modified set in your call to setParametersAsJSON().

If the provided JSON string exceeds 32KB, a System.CanvasException will be thrown.


### Apex Reference Guide RenderContext Interface

Example

This example gets the current custom parameters, adds a new `newCustomParam` parameter with a value of ‘TESTVALUE’, and sets
the current custom parameters.

```
   Canvas.EnvironmentContext env = renderContext.getEnvironmentContext();

   // Get current custom params

   Map<String, Object> previousParams =

      (Map<String, Object>) JSON.deserializeUntyped(env.getParametersAsJSON());

   // Add a new custom param

   previousParams.put('newCustomParam','TESTVALUE');

   // Now replace the parameters with the current parameters plus our new custom param

   env.setParametersAsJSON(JSON.serialize(previousParams));

### RenderContext Interface

```

A wrapper interface that is used to retrieve application and environment context information.

Namespace

Canvas

Usage

Use this interface to retrieve application and environment context information for your canvas app. For this interface, you don’t need to
create an implementation. Use the default implementation that Salesforce provides.

IN THIS SECTION:

#### RenderContext Methods RenderContext Methods

### The following are methods for RenderContext .

IN THIS SECTION:

##### getApplicationContext()

Retrieves the application context information.

getEnvironmentContext()
Retrieves the environment context information.

##### getApplicationContext()

Retrieves the application context information.


Apex Reference Guide RenderContext Interface

Signature

```
   public Canvas.ApplicationContext getApplicationContext()

```

Return Value

Type: Canvas.ApplicationContext

Usage

Use this method to get the application context information for your canvas app.

Example

The following example implementation of the CanvasLifecycleHandler onRender() method uses the provided RenderContext to retrieve
the application context information and then checks the namespace, version, and app URL.

```
   public void onRender(Canvas.RenderContext renderContext){

      Canvas.ApplicationContext app = renderContext.getApplicationContext();

      if (!'MyNamespace'.equals(app.getNamespace())){

        // This application is installed, add code as needed

        ...

      }

      // Check the application version

      Double currentVersion = Double.valueOf(app.getVersion());

      if (currentVersion <= 5){

        // Add version specific code as needed

        ...

        // Tell the canvas application to operate in deprecated mode

        app.setCanvasUrlPath('/canvas?deprecated=true');

      }

   }

##### getEnvironmentContext()

```

Retrieves the environment context information.

Signature

```
   public Canvas.EnvironmentContext getEnvironmentContext()

```

Return Value

Type: Canvas.EnvironmentContext

Usage

Use this method to get the environment context information for your canvas app.


### Apex Reference Guide Test Class

Example

The following example implementation of the CanvasLifecycleHandler onRender() method uses the provided RenderContext to retrieve
the environment context information and then modifies the custom parameters.

```
   public void onRender(Canvas.RenderContext renderContext) {

     Canvas.EnvironmentContext env =

        renderContext.getEnvironmentContext();

      // Retrieve the custom params

      Map<String, Object> previousParams = (Map<String, Object>)

         JSON.deserializeUntyped(env.getParametersAsJSON());

      previousParams.put('param1',1);

      previousParams.put('param2',3.14159);

      ...

      // Now, add in some opportunity record IDs

      Opportunity[] o = [select id, name from opportunity];

      previousParams.put('opportunities',o);

      // Now, replace the parameters

      env.setParametersAsJSON(JSON.serialize(previousParams));

   }

### Test Class

```

Contains methods for automated testing of your Canvas classes.

Namespace

Canvas

Usage

Use this class to test your implementation of Canvas.CanvasLifecycleHandler with mock test data. You can create a test
Canvas.RenderContext with mock application and environment context data and use this data to verify that your CanvasLifecycleHandler
is being invoked correctly.

IN THIS SECTION:

Test Constants
The Test class provides constants that are used as keys when you set mock application and environment context data.

Test Methods
The Test class provides methods for creating test contexts and invoking your CanvasLifecycleHandler with mock data.

SEE ALSO:

_Canvas Developer Guide_ [: Testing Your CanvasLifecycleHandler Implementation](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/canvas_testing_your_canvaslifecyclehandler.htm)


Apex Reference Guide Test Class

#### Test Constants

The Test class provides constants that are used as keys when you set mock application and environment context data.

##### When you call Canvas.Test. mockRenderContext(applicationContextTestValues,

`environmentContextTestValues)`, you need to provide maps of key-value pairs to represent your mock application and
environment context data. The Test class provides static constant strings that you can use as keys for various parts of the application
and environment context.

**Constant** **Description**

`KEY_CANVAS_URL` Represents the canvas app URL key in the ApplicationContext.

`KEY_DEVELOPER_NAME` Represents the canvas app developer or API name key in the ApplicationContext.

`KEY_DISPLAY_LOCATION` Represents the canvas app display location key in the EnvironmentContext.

`KEY_LOCATION_URL` Represents the canvas app location URL key in the EnvironmentContext.

`KEY_NAME` Represents the canvas app name key in the ApplicationContext.

`KEY_NAMESPACE` Represents the canvas app namespace key in the ApplicationContext.

`KEY_SUB_LOCATION` Represents the canvas app sublocation key in the EnvironmentContext.

`KEY_VERSION` Represents the canvas app version key in the ApplicationContext.

#### Test Methods

The Test class provides methods for creating test contexts and invoking your CanvasLifecycleHandler with mock data.

#### The following are methods for Test . All are static methods.

IN THIS SECTION:

##### mockRenderContext(applicationContextTestValues, environmentContextTestValues)

Creates and returns a test Canvas.RenderContext based on the provided application and environment context parameters.

testCanvasLifecycle(lifecycleHandler, mockRenderContext)
Calls the Canvas test framework to invoke a CanvasLifecycleHandler with the provided RenderContext.

##### mockRenderContext(applicationContextTestValues, environmentContextTestValues)

Creates and returns a test Canvas.RenderContext based on the provided application and environment context parameters.

Signature

```
   public static Canvas.RenderContext mockRenderContext(Map<String,String>

   applicationContextTestValues, Map<String,String> environmentContextTestValues)

```

Parameters

```
   applicationContextTestValues
```

Type: Map<String,String>


Apex Reference Guide Test Class

Specifies a map of key-value pairs that provide mock application context data. Use constants that are provided by Canvas.Test as
keys. If `null` is provided for this parameter, the canvas framework generates some default mock application context values.

```
   environmentContextTestValues
```

Type: Map<String,String>

Specifies a map of key-value pairs that provide mock environment context data. Use constants provided by Canvas.Test as keys. If

`null` is provided for this parameter, the canvas framework generates some default mock environment context values.

Return Value

Type: Canvas.RenderContext

Usage

Use this method to create a mock Canvas.RenderContext. Use the returned RenderContext in calls to
##### Canvas.Test. testCanvasLifecycle(lifecycleHandler, mockRenderContext) for testing

Canvas.CanvasLifecycleHandler implementations.

Example

The following example creates maps to represent mock application and environment context data and generates a test
Canvas.RenderContext. This test RenderContext can be used in a call to
##### Canvas.Test. testCanvasLifecycle(lifecycleHandler, mockRenderContext) .

```
   Map<String,String> appValues = new Map<String,String>();

   appValues.put(Canvas.Test.KEY_NAMESPACE,'alternateNamespace');

   appValues.put(Canvas.Test.KEY_VERSION,'3.0');

   Map<String,String> envValues = new Map<String,String>();

   envValues.put(Canvas.Test.KEY_DISPLAY_LOCATION,'Chatter');

   envValues.put(Canvas.Test.KEY_LOCATION_URL,'https:// MyDomainName .my.salesforce.com/_ui/core/chatter/ui/ChatterPage');

   Canvas.RenderContext mock = Canvas.Test.mockRenderContext(appValues,envValues);

```

SEE ALSO:

_Canvas Developer Guide_ [: Testing Your CanvasLifecycleHandler Implementation](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/canvas_testing_your_canvaslifecyclehandler.htm)

##### testCanvasLifecycle(lifecycleHandler, mockRenderContext)

Calls the Canvas test framework to invoke a CanvasLifecycleHandler with the provided RenderContext.

Signature

```
   public static Void testCanvasLifecycle(Canvas.CanvasLifecycleHandler

   lifecycleHandler,Canvas.RenderContext mockRenderContext)

```

Parameters

```
   lifecycleHandler
```

Type: Canvas.CanvasLifecycleHandler


Apex Reference Guide Test Class

Specifies the CanvasLifecycleHandler implementation that you need to invoke.

```
   mockRenderContext
```

Type: Canvas.RenderContext

Specifies the RenderContext information that you need to provide to the invoked CanvasLifecycleHandler. If `null` is provided for
this parameter, the canvas framework generates and uses a default mock RenderContext.

Return Value

Type: Void

Usage

Use this method to invoke an implementation of Canvas.CanvasLifecycleHandler. `onRender(renderContext)` with a mock
Canvas.RenderContext that you provide.

Example

The following example creates an Apex test class that uses maps to represent mock application and environment context data. The
mock RenderContext object is then used to invoke a CanvasLifecycleHandler object. In this example, the CanvasLifecycleHandler is
defined as MyCanvasListener, which is example implementation provided in Canvas.RenderContext.

```
   @IsTest

   global class CanvasRendercontextTest {

      @IsTest

      static void testRenderContext(){

        // Set some application context data in a Map

        Map<String,String> appValues = new Map<String,String>();

        appValues.put(Canvas.Test.KEY_NAMESPACE,'alternateNamespace');

        appValues.put(Canvas.Test.KEY_VERSION,'3.0');

        // Set some environment context data in a MAp

        Map<String,String> envValues = new Map<String,String>();

        envValues.put(Canvas.Test.KEY_DISPLAY_LOCATION,'Chatter');

   envValues.put(Canvas.Test.KEY_LOCATION_URL,'https://MyDomainName.my.salesforce.com/_ui/core/chatter/ui/ChatterPage');

        // Create a mock RenderContext using the test application and environment context

    data Maps

        Canvas.RenderContext mock = Canvas.Test.mockRenderContext(appValues,envValues);

        // Set some custom params on the mock RenderContext

   mock.getEnvironmentContext().setParametersAsJSON('{\"param1\":1,\"boolParam\":true,\"stringParam\":\"test

    string\"}');

        // Create a CanvasLifecycleHandler

        MyCanvasListener handler = new MyCanvasListener();

        // Use the mock RenderContext to invoke the CanvasLifecycleHandler

        Canvas.Test.testCanvasLifecycle(handler,mock);

```


### Apex Reference Guide Canvas Exceptions

```
    }

   }

```

SEE ALSO:

_Canvas Developer Guide_ [: Testing Your CanvasLifecycleHandler Implementation](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/canvas_testing_your_canvaslifecyclehandler.htm)

### Canvas Exceptions The Canvas namespace contains exception classes.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions.

### The Canvas namespace contains this exception:

**Exception** **Description**

`Canvas.CanvasRenderException` Use this class in your implementation of
Canvas.CanvasLifecycleHandler. `onRender(renderContext)` . To show

an error to the user in your `onRender()` implementation, throw a
`Canvas.CanvasRenderException`, and the canvas framework will
render the error message to the user. This exception will be managed only
within the `onRender()` method.

Example

The following example implementation of `onRender()` catches a CanvasException that was thrown because a canvas URL was set
with a string that exceeded the maximum length. A CanvasRenderException is created and thrown to display the error to the user.

```
   public class MyCanvasListener

   implements Canvas.CanvasLifecycleHandler {

      public void onRender(Canvas.RenderContext renderContext) {

        Canvas.ApplicationContext app = renderContext.getApplicationContext();

        // Code to generate a URL string that is too long

        // ...

        // Try to set the canvas app URL using the invalid URL string

        try {

           app.setCanvasUrlPath(aUrlPathThatIsTooLong);

        } catch (CanvasException e) {

           // Display error to user by throwing a new CanvasRenderException

           throw new Canvas.CanvasRenderException(e.getMessage());

        }

      }

   }

```

[See the Canvas Developer Guide for additional examples that use CanvasRenderException.](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/)


## Apex Reference Guide ChatterAnswers Namespace ChatterAnswers Namespace The ChatterAnswers namespace provides an interface for creating Account records. The following is the interface in the ChatterAnswers namespace.

IN THIS SECTION:

### AccountCreator Interface

Creates Account records that will be associated with Chatter Answers users.

### AccountCreator Interface

Creates Account records that will be associated with Chatter Answers users.

Namespace

## ChatterAnswers

Usage

The `ChatterAnswers.AccountCreator` is specified in the `registrationClassName` attribute of a
`chatteranswers:registration` Visualforce component. This interface is called by Chatter Answers and allows for custom
creation of Account records used for portal users.

To implement the `ChatterAnswers.AccountCreator` interface, you must first declare a class with the `implements`
keyword as follows:

```
   public class ChatterAnswersRegistration implements ChatterAnswers.AccountCreator {

```

Next, your class must provide an implementation for the following method:

```
   public String createAccount(String firstname, String lastname, Id siteAdminId) {

      // Your code here

   }

```

The implemented method must be declared as `global` or `public` .

IN THIS SECTION:

#### AccountCreator Methods

AccountCreator Example Implementation

#### AccountCreator Methods

### The following are methods for AccountCreator .

IN THIS SECTION:

createAccount(firstName, lastName, siteAdminId)
Accepts basic user information and creates an Account record. The implementation of this method returns the account ID.


Apex Reference Guide AccountCreator Interface

##### createAccount(firstName, lastName, siteAdminId)

Accepts basic user information and creates an Account record. The implementation of this method returns the account ID.

Signature

```
   public String createAccount(String firstName, String lastName, Id siteAdminId)

```

Parameters

```
   firstName
```

Type: String

The first name of the user who is registering.

```
   lastName
```

Type: String

The last name of the user who is registering.

```
   siteAdminId
```

Type: ID

The user ID of the Site administrator, used for notification if any exceptions occur.

Return Value

Type: String

#### AccountCreator Example Implementation

##### This is an example implementation of the ChatterAnswers.AccountCreator interface. The createAccount method

implementation accepts user information and creates an Account record. The method returns a String value for the Account ID.

```
   public class ChatterAnswersRegistration implements ChatterAnswers.AccountCreator {

      public String createAccount(String firstname, String lastname, Id siteAdminId) {

        Account a = new Account(name = firstname + ' ' + lastname, ownerId = siteAdminId);

         insert a;

         return a.Id;

      }

   }

```

This example tests the code above.

```
   @isTest

   private class ChatterAnswersCreateAccountTest {

      static testMethod void validateAccountCreation() {

        User[] user = [SELECT Id, Firstname, Lastname from User WHERE UserType='Standard'];

        if (user.size() == 0) { return; }

        String firstName = user[0].FirstName;

        String lastName = user[0].LastName;

        String userId = user[0].Id;

        String accountId = new ChatterAnswersRegistration().createAccount(firstName,

   lastName, userId);

```


## Apex Reference Guide CommerceBuyGrp Namespace

```
        Account acct = [SELECT name, ownerId from Account where Id =: accountId];

        System.assertEquals(firstName + ' ' + lastName, acct.name);

        System.assertEquals(userId, acct.ownerId);

     }

   }

## CommerceBuyGrp Namespace The CommerceBuyGrp namespace provides classes and methods for retrieving information about the buyer groups associated with
```

a user.

## The following are the classes in the CommerceBuyGrp namespace.

IN THIS SECTION:

### BuyerGroupEvaluationService Class The BuyerGroupEvaluationService class allows you define and execute custom business logic for dynamically assigning

users to buyer groups. Unlike out-of-the-box configurations limited to account, market, or data segment-based buyer groups, this
service supports extensibility and empowers you to implement tailored buyer group evaluation strategies. It supports both guest
and logged-in user scenarios, enabling highly customizable and context-specific buyer group determination.

BuyerGroupRequest Class
Contains methods to retrieve account and store details used to identify the buyer groups associated with a user.

BuyerGroupResponse Class
Contains constructors and methods to retrieve the buyer groups associated with a user.

SEE ALSO:

_[Salesforce B2B Commerce and D2C Commerce](https://help.salesforce.com/s/articleView?id=commerce.comm_buyer_group_extension.htm&language=en_US)_ : Assign Users to Buyer Groups

_[B2B Commerce and D2C Commerce Developer Guide](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/available-extensions.html)_ : Available Domain Extensions

### BuyerGroupEvaluationService Class The BuyerGroupEvaluationService class allows you define and execute custom business logic for dynamically assigning

users to buyer groups. Unlike out-of-the-box configurations limited to account, market, or data segment-based buyer groups, this service
supports extensibility and empowers you to implement tailored buyer group evaluation strategies. It supports both guest and logged-in
user scenarios, enabling highly customizable and context-specific buyer group determination.

Namespace

## CommerceBuyGrp

Consideration

### When implementing the BuyerGroupEvaluationService, remember these key points:

**•** [The number of buyer groups that can be assigned to a user is determined by the limit set in your Salesforce org. See Shopper Buyer](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-data-model-shopper-buyer-groups-accounts-limits.html)
[Groups and Accounts Data Limits Groups.](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-data-model-shopper-buyer-groups-accounts-limits.html)


Apex Reference Guide BuyerGroupEvaluationService Class

**•** Supported for B2B stores and D2C stores with custom checkout enabled. It isn't available for stores using managed checkout. See
[Configure Custom Checkout for a B2B or D2C Store.](https://help.salesforce.com/s/articleView?id=commerce.comm_custom_checkout.htm&language=en_US)

**•** Buyer group assignments may not take effect immediately if caching is enabled. To make sure the buyer group extensibility service
functions properly and to avoid caching-related issues, disable both the Salesforce Content Delivery Network (CDN) and Salesforce
Edge Network.

Test these changes in your sandbox org before applying them in production. Go to **My Domain Settings** and disable both options
for enhanced domains.

[See Considerations for the Salesforce CDN and Considerations for Salesforce Edge Network.](https://help.salesforce.com/s/articleView?id=platform.community_builder_cdn_considerations.htm&language=en_US)

Usage

#### Use the BuyerGroupEvaluationService to implement custom logic for assigning users to buyer groups. By integrating your

logic with this service, you can evaluate and assign buyer groups in real time based on criteria specific to your organization.

**•** Define Custom Logic—Create your own business rules to evaluate and assign users to appropriate Buyer Groups.

#### • Integration with the Service—Integrate your custom logic into the BuyerGroupEvaluationService to dynamically

determine buyer group membership at runtime.

**•** Test and Validate—Test your implementation to ensure it behaves as expected and doesn’t introduce errors or inconsistencies in
group assignments.

Example

For an example implementation of the `CommerceBuyGrp.BuyerGroupEvaluationService` [class, see Commerce Extensibility.](https://github.com/forcedotcom/commerce-extensibility/blob/main/commerce/domain/buyergroup/service/classes/BuyerGroupEvaluationServiceSample.cls)

IN THIS SECTION:

#### BuyerGroupEvaluationService Methods BuyerGroupEvaluationService Methods The following are methods for BuyerGroupEvaluationService .

IN THIS SECTION:

##### getBuyerGroupIds(request)

Retrieves a list of evaluated buyer group IDs assigned to a user based on custom or predefined business logic.

##### **`getBuyerGroupIds(request)`**

Retrieves a list of evaluated buyer group IDs assigned to a user based on custom or predefined business logic.

Signature

```
   public CommerceBuyGrp.BuyerGroupResponse

   getBuyerGroupIds(CommerceBuyGrp.BuyerGroupRequest request)

```


### Apex Reference Guide BuyerGroupRequest Class

Parameters

```
   request
```

Type: CommerceBuyGrp.BuyerGroupRequest

Return Value

Type: CommerceBuyGrp.BuyerGroupResponseCommerceBuyGrp.BuyerGroupResponse

### BuyerGroupRequest Class

Contains methods to retrieve account and store details used to identify the buyer groups associated with a user.

Namespace

CommerceBuyGrp

IN THIS SECTION:

#### BuyerGroupRequest Methods BuyerGroupRequest Methods

### The following are methods for BuyerGroupRequest .

IN THIS SECTION:

##### getAccountId()

Returns the account ID of a user.

getStoreId()
Returns the ID of the web store.

getRequestContextParameters()
Returns a map of user context parameters evaluated at runtime, including `isGuestUser`, `locale`, and
`guest_uuid_essential_{siteId}` .

##### **`getAccountId()`**

Returns the account ID of a user.

Signature

```
   public String getAccountId()

```

Return Value

Type: String


### Apex Reference Guide BuyerGroupResponse Class

##### **`getStoreId()`**

Returns the ID of the web store.

Signature

```
   public String getStoreId()

```

Return Value

Type: String

##### **`getRequestContextParameters()`**

Returns a map of user context parameters evaluated at runtime, including `isGuestUser`, `locale`, and
`guest_uuid_essential_{siteId}` .

Signature

```
   public Map<String,Object> getRequestContextParameters()

```

Return Value

Type: Map<String,Object>

Here's a list of context parameters to include in the request:

**Name** **Type** **Description**

`guest_uuid_` String Specifies the multiple key-value pair representing guest UUID
`essential_{siteId}` cookie for each store. Generated by the client as a unique device
identifier where `siteId` is the 15-digit ID for the site associated
with the webstore.

`isGuestUser` Boolean Indicates whether the user in context is a guest user ( `true` ) or an
authenticated user ( `false` ).

`locale` String Specifies the user's locale.

### BuyerGroupResponse Class

Contains constructors and methods to retrieve the buyer groups associated with a user.

Namespace

CommerceBuyGrp

IN THIS SECTION:

BuyerGroupResponse Constructors

BuyerGroupResponse Methods


Apex Reference Guide BuyerGroupResponse Class

#### BuyerGroupResponse Constructors The following are constructors for BuyerGroupResponse .

IN THIS SECTION:

##### BuyerGroupResponse(buyerGroupIds)

Creates a new instance of the `CommerceBuyGrp.BuyerGroupResponse` class using the specified `buyerGroupIds`
payload parameter.

##### BuyerGroupResponse()

Creates a new instance of the `CommerceBuyGrp.BuyerGroupResponse` class.

##### **`BuyerGroupResponse(buyerGroupIds)`**

Creates a new instance of the `CommerceBuyGrp.BuyerGroupResponse` class using the specified `buyerGroupIds` payload
parameter.

Signature

```
   public BuyerGroupResponse(Set<String> buyerGroupIds)

```

Parameters

```
   buyerGroupIds
```

Type: Set<String>

List of buyer group IDs for a user.

##### **`BuyerGroupResponse()`**

Creates a new instance of the `CommerceBuyGrp.BuyerGroupResponse` class.

Signature

```
   public BuyerGroupResponse()

#### BuyerGroupResponse Methods The following are methods for BuyerGroupResponse .

```

IN THIS SECTION:

getBuyerGroupIds()
Retrieves a list of evaluated buyer group IDs assigned to a user.

setBuyerGroupIds(buyerGroupIds)
Sets a list of evaluated buyer group IDs assigned to a user.

setError(errorMessage, localizedErrorMessage)
Sets the error message to be returned when the evaluation of buyer group IDs fails.


Apex Reference Guide BuyerGroupResponse Class

##### **`getBuyerGroupIds()`**

Retrieves a list of evaluated buyer group IDs assigned to a user.

Signature

```
   public Set<String> getBuyerGroupIds()

```

Return Value

Type: Set<String>

##### **`setBuyerGroupIds(buyerGroupIds)`**

Sets a list of evaluated buyer group IDs assigned to a user.

Signature

```
   public void setBuyerGroupIds(Set<String> buyerGroupIds)

```

Parameters

```
   buyerGroupIds
```

Type: Set<String>

Return Value

Type: void

##### **`setError(errorMessage, localizedErrorMessage)`**

Sets the error message to be returned when the evaluation of buyer group IDs fails.

Signature

```
   public void setError(String errorMessage, String localizedErrorMessage)

```

Parameters

```
   errorMessage
```

Type: String

The message stating the reason for the error.

```
   localizedErrorMessage
```

Type: String

The translated error message.

Return Value

Type: void


## Apex Reference Guide CommerceExtension Namespace CommerceExtension Namespace Use the CommerceExtension namespace to define resolution strategies for registered Commerce extensions. The following are the classes in the CommerceExtension namespace.

IN THIS SECTION:

### ExtensionInfo Class

Contains static methods to expose extension-related context information.

Resolution Class
Resolution of a resolution strategy, which conditionally invokes default domain logic, logic provided by an extension provider, or no
logic.

ResolutionException Class
Exception indicating a problem with the execution of a resolution strategy.

ResolutionStates Enum
Potential resolution states for a resolution strategy.

ResolutionStrategy Interface
Interface for a resolution strategy.

### ExtensionInfo Class

Contains static methods to expose extension-related context information.

Namespace

CommerceExtension on page 307

Example

```
        // The Sample Extension Provider registered with developer name as

        // 'tax_extension_provider_for_us' will be selected for execution for en_US locale

        if(CommerceExtension.ExtensionInfo.getLocaleString() == 'en_US') {

           return new CommerceExtension.Resolution('tax_extension_provider_for_us');

        }

        // The Sample Extension Provider registered with developer name as

        // 'tax_extension_provider_for_canada' will be selected for execution for en_CA

   locale

        if(CommerceExtension.ExtensionInfo.getLocaleString() == 'en_CA') {

          return new CommerceExtension.Resolution('tax_extension_provider_for_canada');

        }

        // The default Salesforce Internal Tax Api will return an empty response for German

    locale

        if(CommerceExtension.ExtensionInfo.getLocaleString() == 'de') {

          return new CommerceExtension.Resolution(CommerceExtension.ResolutionStates.OFF);

```


Apex Reference Guide ExtensionInfo Class

```
        }

```

IN THIS SECTION:

#### ExtensionInfo Methods ExtensionInfo Methods The following are methods for ExtensionInfo .

IN THIS SECTION:

##### getClientApiVersion()

Returns the version number of the Client API for the extension context.

##### getCustomParameterField(fieldName)

Returns a custom parameter field value, if available, for the extension context.

getLocaleString()
Returns the locale for the extension context.

isCustomParametersAvailable()
Indicates whether custom parameters are available for the extension context.

##### **`getClientApiVersion()`**

Returns the version number of the Client API for the extension context.

Signature

```
   public static Double getClientApiVersion()

```

Return Value

Type: Double

Version number of the Client API for the extension context.

##### **`getCustomParameterField(fieldName)`**

Returns a custom parameter field value, if available, for the extension context.

Signature

```
   public static String getCustomParameterField(String fieldName)

```

Parameters

```
   fieldName
```

Type: String

Custom parameter field name.


### Apex Reference Guide Resolution Class

Return Value

Type: String

Custom parameter field value for the extension context.

##### **`getLocaleString()`**

Returns the locale for the extension context.

Signature

```
   public static String getLocaleString()

```

Return Value

Type: String

Locale for the extension context.

##### **`isCustomParametersAvailable()`**

Indicates whether custom parameters are available for the extension context.

Signature

```
   public static Boolean isCustomParametersAvailable()

```

Return Value

Type: Boolean

Value indicating if custom parameters are available in the extension context ( `true` ) or not ( `false` ).

### Resolution Class

Resolution of a resolution strategy, which conditionally invokes default domain logic, logic provided by an extension provider, or no
logic.

Namespace

CommerceExtension on page 307

Example

```
   public class TaxServiceExtensionResolverSample extends commercestoretax.TaxService implements

    CommerceExtension.ResolutionStrategy {

      public CommerceExtension.Resolution resolve() {

        // The Sample Extension Provider registered with developer name as

   'tax_extension_provider_for_us' will be selected for execution for en_US locale

        if(CommerceExtension.ExtensionInfo.getLocaleString() == 'en_US') {

           return new CommerceExtension.Resolution('tax_extension_provider_for_us');

```


Apex Reference Guide Resolution Class

```
        }

        // The Sample Extension Provider registered with developer name as

   'tax_extension_provider_for_canada' will be selected for execution for en_CA locale

        if(CommerceExtension.ExtensionInfo.getLocaleString() == 'en_CA') {

          return new CommerceExtension.Resolution('tax_extension_provider_for_canada');

        }

        // The default Salesforce Internal Tax Api will return an empty response for German

    locale

        if(CommerceExtension.ExtensionInfo.getLocaleString() == 'de') {

          return new CommerceExtension.Resolution(CommerceExtension.ResolutionStates.OFF);

        }

        // The default Salesforce Internal Tax Api will be selected for execution for all

    other locales than US, Canada and Germany

        return new CommerceExtension.Resolution();

      }

   }

```

IN THIS SECTION:

#### Resolution Constructors

Resolution Methods

#### Resolution Constructors The following are constructors for Resolution .

IN THIS SECTION:

##### Resolution(resolutionState)

Constructor that takes a CommerceExtension.ResolutionStates object as an argument.

Resolution(providerName)
Constructor that takes the name of an extension provider as an argument.

Resolution()
Default constructor for the Resolution class.

##### **`Resolution(resolutionState)`**

Constructor that takes a CommerceExtension.ResolutionStates object as an argument.

Signature

```
   public Resolution(CommerceExtension.ResolutionStates resolutionState)

```

Parameters

```
   resolutionState
```

Type: CommerceExtension.ResolutionStates on page 314


Apex Reference Guide Resolution Class

Resolution state.

##### **`Resolution(providerName)`**

Constructor that takes the name of an extension provider as an argument.

Signature

```
   public Resolution(String providerName)

```

Parameters

```
   providerName
```

Type: String

Name of the extension provider.

##### **`Resolution()`**

Default constructor for the Resolution class.

Signature

```
   public Resolution()

#### Resolution Methods

##### The following are methods for Resolution .

```

IN THIS SECTION:

##### getProviderName()

Returns the name of an extension provider.

getResolutionState()
Returns the resolution state of the resolution.

##### **`getProviderName()`**

Returns the name of an extension provider.

Signature

```
   public String getProviderName()

```

Return Value

Type: String

Name of an extension provider.


### Apex Reference Guide ResolutionException Class

##### **`getResolutionState()`**

Returns the resolution state of the resolution.

Signature

```
   public CommerceExtension.ResolutionStates getResolutionState()

```

Return Value

Type: CommerceExtension.ResolutionStates on page 314

Resolution state of the resolution.

### ResolutionException Class

Exception indicating a problem with the execution of a resolution strategy.

Namespace

CommerceExtension on page 307

IN THIS SECTION:

#### ResolutionException Constructors

ResolutionException Methods

#### ResolutionException Constructors

### The following are constructors for ResolutionException .

IN THIS SECTION:

##### ResolutionException(errorMessage, exception)

Constructor that takes two arguments: an error message and an exception.

ResolutionException(exception)
Constructor that takes an exception as an argument,

ResolutionException(errorMessage)
Constructor that takes an error message as an argument.

ResolutionException()
Default constructor for the ResolutionException class.

##### **`ResolutionException(errorMessage, exception)`**

Constructor that takes two arguments: an error message and an exception.

Signature

```
   public ResolutionException(String errorMessage, Exception exception)

```


Apex Reference Guide ResolutionException Class

Parameters

```
   errorMessage
```

Type: String

Error message.

```
   exception
```

[Type: Exception](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

Exception.

##### **`ResolutionException(exception)`**

Constructor that takes an exception as an argument,

Signature

```
   public ResolutionException(Exception exception)

```

Parameters

```
   exception
```

[Type: Exception](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

Exception.

##### **`ResolutionException(errorMessage)`**

Constructor that takes an error message as an argument.

Signature

```
   public ResolutionException(String errorMessage)

```

Parameters

```
   errorMessage
```

Type: String

Error message.

##### **`ResolutionException()`**

Default constructor for the ResolutionException class.

Signature

```
   public ResolutionException()

#### ResolutionException Methods

##### The following are methods for the ResolutionException class.

```


### Apex Reference Guide ResolutionStates Enum

IN THIS SECTION:

##### getTypeName()

Returns the type of the exception.

##### **`getTypeName()`**

Returns the type of the exception.

Signature

```
   public String getTypeName()

```

Return Value

Type: String

The type of the Exception.

### ResolutionStates Enum

Potential resolution states for a resolution strategy.

Enum Values

The following are the values of the `CommerceExtension.ResolutionStates` enum.

**Value** **Description**

`EXECUTE_DEFAULT` Run the default domain logic (without running extension provider logic).

`EXECUTE_REGISTERED` Run the extension provider logic provided by the Apex class registered for the
endpoint provider name.

`OFF` Don’t run any domain logic (default logic or logic provided by an extension provider).

### ResolutionStrategy Interface

Interface for a resolution strategy.

Namespace

CommerceExtension on page 307

Usage

When you implement this interface, you can register your apex class just like an extension provider class. Your class can then conditionally
decide how to handle each extension invocation. You can delegate to a specific extension provider, you can execute default domain
logic, or you can execute no logic at all.


Apex Reference Guide ResolutionStrategy Interface

IN THIS SECTION:

#### ResolutionStrategy Methods ResolutionStrategy Example Implementation ResolutionStrategy Methods The following are methods for ResolutionStrategy .

IN THIS SECTION:

##### resolve()

Returns a resolution object, which indicates how the resolution strategy was resolved. The resolution indicates whether default logic,
extension provider logic, or no logic is executed.

##### **`resolve()`**

Returns a resolution object, which indicates how the resolution strategy was resolved. The resolution indicates whether default logic,
extension provider logic, or no logic is executed.

Signature

```
   public CommerceExtension.Resolution resolve()

```

Return Value

Type: CommerceExtension.Resolution on page 309

Resolution object that indicates how the resolution strategy was resolved.

#### ResolutionStrategy Example Implementation

This is an example implementation of the `CommerceExtension.ResolutionStrategy` interface.

```
   // This sample is for the situation when different tax behaviors need to be

   // implemented for different locales.

   //

   // These tax behaviors can be 
   // 1. ResolutionState - EXECUTE_DEFAULT (the default Salesforce Internal Tax Api).

   // 2. ResolutionState - EXECUTE_REGISTERED (extended or overridden implementations

   // via the extension point from the default Salesforce Internal Tax Api)

   // 3. ResolutionState - OFF (In this case, the default Salesforce Internal Tax Api

   // will return an empty response).

   //

   // An Extension Provider is a custom apex class which extends or overrides the

   // default Salesforce Internal Tax Api.

   //

   // An Extension Resolver is a custom apex class which selects different resolution

   // states (EXECUTE_DEFAULT, EXECUTE_REGISTERED and OFF) for different locales

   // to execute respective implementations (Extension Providers or the Default

   // Salesforce Internal Tax Api).

```


## Apex Reference Guide CommerceOrders Namespace

```
   // Your custom apex extension providers and the resolver must be registered with

   // the tax extension point and then the resolver must be registered and mapped to

   // the web store via appropriate setup.

   //

   // You can have as many Extension Providers registered as per your use case and

   // select them in your resolver for different locales.

   //

   // Please follow the corresponding salesforce documentation on how to use locales.

   // For more information related to that, please see the corresponding documentation.

   // This must implement the commercestoretax.TaxService class in order to be

   // processed by the tax service flow. It must also implement the

   // CommerceExtension.ResolutionStrategy in order to work as a extension resolver

   // and get the different locales and resolutions.

   //

   public class TaxServiceExtensionResolverSample

      extends commercestoretax.TaxService

      implements CommerceExtension.ResolutionStrategy {

      public CommerceExtension.Resolution resolve() {

        // The Sample Extension Provider registered with developer name as

        // 'tax_extension_provider_for_us' will be selected for execution for en_US locale

        if (CommerceExtension.ExtensionInfo.getLocaleString() == 'en_US') {

           return new CommerceExtension.Resolution('tax_extension_provider_for_us');

        }

        // The Sample Extension Provider registered with developer name as

        // 'tax_extension_provider_for_canada' will be selected for execution for en_CA

   locale

        if (CommerceExtension.ExtensionInfo.getLocaleString() == 'en_CA') {

          return new CommerceExtension.Resolution('tax_extension_provider_for_canada');

        }

        // The default Salesforce Internal Tax Api will return an empty response for German

    locale

        if (CommerceExtension.ExtensionInfo.getLocaleString() == 'de') {

           return new CommerceExtension.Resolution(

             CommerceExtension.ResolutionStates.OFF

           );

        }

        // The default Salesforce Internal Tax Api will be selected for execution for

        // all other locales than US, Canada and Germany

        return new CommerceExtension.Resolution();

      }

   }

## CommerceOrders Namespace The CommerceOrders namespace provides classes and methods to place orders with integrated pricing, configuration, and validation.

```

[See CommerceOrders namespace for more information about the available classes and methods.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_commerceorders.htm)


## Apex Reference Guide CommercePayments Namespace CommercePayments Namespace Use the CommercePayments namespace to provide a safe and customizable platform for managing customer payments and

refunds.

## To review CommercePayments use cases and walkthroughs, go to Use Cases for the CommercePayments Namespace. The following are the classes in the CommercePayments namespace.

IN THIS SECTION:

AbstractResponse Class
Contains the normalized response fields from payment gateways that are common to all the other gateway responses.

AbstractTransactionResponse Class
Abstract class for storing normalized information sent from payment gateways about a payment transaction. Holds the common
response fields sent from payment gateways for authorization, sale, capture, and refund transactions.

AccountType Enum
Specifies the account type.

AccountHolderType Enum
Specifies the type of the account holder.

AddressRequest Class
Contains address request data that is sent to a gateway adapter during a service call.

AlternativePaymentMethodRequest Class
The class contains information about the alternative payment method that are required for a gateway to process the request.

AlternativePaymentMethodResponse Class
The class contains the response details of the alternative payment method.

AuditParamsRequest

`AuditParamsRequest` is used for audit parameters in a transaction request. This is an abstract request class that is extended
by the `BaseRequest` class.

AuthApiPaymentMethodRequest Class
Sends information about a payment method to a gateway adapter during an authorization service call.

AuthorizationRequest Class
Sends information about an authorization request to a gateway adapter during a service call. This class extends the `BaseRequest`
class and inherits all its methods.

AuthorizationResponse Class
Response sent by the payment gateway adapter for an authorization service.

AuthorizationReversalRequest Class
Sends information about an authorization reversal request to a gateway adapter during a service call.

AuthorizationReversalResponse Class
Response sent by the payment gateway following a payment authorization reversal service.

BankType Enum
Specifies the bank type.

BankPaymentMethodRequest Class
Sends data related to a bank payment method to a gateway adapter during a service call.


Apex Reference Guide CommercePayments Namespace

BankPaymentMethodResponse Class
This class contains information about the bank payment method response. The gateway adapter reads the gateway response and
generates a `BankPaymentMethodResponse`, populating the required fields to create a bank payment method.

BaseApiPaymentMethodRequest Class
Abstract class used to send information about a payment method to a gateway adapter during a service call.

BaseNotification Class
Abstract class for storing notification information sent from payment gateways.

BasePaymentMethodRequest Class
Abstract class for storing information about payment methods.

BaseRequest Class

`BaseRequest` is extended by all the request classes.

CaptureNotification Class
When a payment gateway sends a notification for a capture transaction, the payment gateway adapter creates the
`CaptureNotification` object to store information about the notification.

CaptureRequest Class
Represents a capture request. This class extends the `BaseRequest` class and inherits all its methods.

CaptureResponse Class
The payment gateway adapter sends this response for the capture request type. This class extends `AbstractResponse` and
inherits its methods.

CardCategory Enum
Defines whether the payment method represents a credit card or a debit card.

CardPaymentMethodRequest Class
Sends data related to a card payment method to a gateway adapter during a service call.

CardPaymentMethodResponse Class
This class contains details about the card payment method.

CardType Enum
Specifies the credit card issuer.

CustomMetadataTypeInfo Class
Access information about custom metadata. The `PaymentGatewayAdapter` can send `CustomMetadataTypeInfo` to
transaction requests through the response object’s `SalesforceResultCodeInfo` .

EnhancedPaymentDataInput Class
Sends enhanced payment data, including Level 2 and Level 3 fields, to the gateway adapter as part of the service call.

GatewayErrorResponse Class
Use to respond with an error indication following errors from the `PaymentGateway` adapter, such as request-forbidden responses,
custom validation errors, or expired API tokens.

GatewayNotificationResponse Class
When the payment gateway sends a notification to the payments platform, the platform responds with a
`GatewayNotificationResponse` indicating whether the platform succeeded or failed at receiving the notification.

GatewayResponse Interface
Generic payment gateway response interface. This class extends the `CaptureResponse` on page 398,
`AbstractTransactionResponse` on page 324, and `AbstractResponse` on page 320 classes and inherits all their
properties. It has no unique methods or parameters.


Apex Reference Guide CommercePayments Namespace

NotificationClient Class
Communicates with the payment platform regarding the gateway’s notification.

NotificationSaveResult Class
Contains the result of the payment platform’s attempt to record data from the gateway’s notification.

NotificationStatus Enum
Shows whether the payments platform successfully received the notification from the gateway.

PaymentGatewayAdapter Interface

`PaymentGatewayAdapters` can implement this interface in order to process requests.

PaymentGatewayAsyncAdapter Interface
Implement the interface to allow customers to process payments asynchronously.

PaymentGatewayContext Class
Wraps the information related to a payment request.

PaymentGatewayNotificationContext Class
Wraps the information related to a gateway notification.

PaymentGatewayNotificationRequest Class
Contains the notification request data from the gateway.

PaymentMethodDetailsResponse Class
This class contains the details about the payment method.

LineItemInput Class
Sends the list of individual line items associated with the payment to the gateway adapter.

PaymentMethodIdType Enum
Specifies the ID of the payment method type.

PaymentMethodTokenizationRequest Class
Stores data about a request to tokenize a card payment method. The tokenization process occurs in the payment gateway. This
process replaces sensitive customer data, such as a card number or CVV, with unique identification symbols. The symbols are used
while the data is handled by Salesforce, the payment gateway, and the customer bank, allowing Salesforce to store the token without
storing sensitive customer data.

PaymentMethodTokenizationResponse Class
Gateway response sent by payment gateway adapters for the payment method tokenization request. The response includes the
payment method’s token ID value.

PaymentsHttp Class
Makes an HTTP request to start the interaction with the payment gateway.

PostAuthApiPaymentMethodRequest Class
Sends information about a payment method to a gateway adapter during a postauthorization service call.

PostAuthorizationRequest Class
Sends information about a postauthorization request to a gateway adapter during a service call.

PostAuthorizationResponse Class
Response sent by the payment gateway adapter for a postauthorization service.

ReferencedRefundNotification Class
When a payment gateway sends a notification for a refund transaction, the payment gateway adapter creates the
`ReferencedRefundNotification` object to store information about notification.


### Apex Reference Guide AbstractResponse Class

ReferencedRefundRequest
Access information about the referenced refund requests. Extends the `RefundRequest` class.

ReferencedRefundResponse Class
The payment gateway adapter sends this response for the `ReferencedRefund` request type.

RefundRequest Class
Sends data related to a refund to the payment gateway adapter.

RequestType Enum
Defines the type of payment transaction request made to the payment gateway.

RetryCategory Enum
Specifies the retry category.

RetryDecision Enum
Specifies the retry decision.

SaleApiPaymentMethodRequest Class
Sends data related to a card payment method to a gateway adapter during a sale service call.

SaleNotification Class
When a payment gateway sends a notification for a sale payment, the payment gateway adapter creates the `SaleNotification`
object to store information about notification.

SaleRequest Class
Stores information about a sales request.

SaleResponse Class
Response sent by payment gateway adapters for a sales service.

SalesforceResultCode Enum
Defines the gateway call status values in Salesforce based on the call status values that the payment gateway returned.

SalesforceResultCodeInfo
Stores Salesforce result code information from payment gateway adapters.

StandardEntryClassCode Enum
Specifies the three-letter code that identifies the type of electronic payment transaction being processed within the Automated
Clearing House (ACH) network.

TokenizeNotification Class
When a payment gateway sends a notification for a payment method tokenization, the payment gateway adapter creates the
`TokenizeNotification` object to store information about notification.

### AbstractResponse Class

Contains the normalized response fields from payment gateways that are common to all the other gateway responses.

Namespace

CommercePayments


Apex Reference Guide AbstractResponse Class

Usage

You must specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes
no arguments. For example:

```
   CommercePayments.AbstractResponse abr = new CommercePayments.AbstractResponse();

```

This class can’t be instantiated on its own. This class implements the GatewayResponse class. Other GatewayResponse classes extend
this class to inherit common properties.

IN THIS SECTION:

#### AbstractResponse Methods AbstractResponse Methods The following are methods for AbstractResponse .

IN THIS SECTION:

##### setGatewayAvsCode(gatewayAvsCode)

Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the transaction occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the payment request. Maximum length of 255 characters.

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

setRetryCategory(retryCategory)
Sets the retry category returned by the payment gateway for the failed payment in a batch flow.

setRetryDecision(retryDecision)
Sets the retry decision.

##### setGatewayAvsCode(gatewayAvsCode)

Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

Signature

```
   global void setGatewayAvsCode(String gatewayAvsCode)

```


Apex Reference Guide AbstractResponse Class

Parameters

```
   gatewayAvsCode
```

Type: String

Code sent by gateways that use an address verification system.

Return Value

Type: void

##### setGatewayDate(gatewayDate)

Sets the date that the transaction occurred. Some gateways don’t send this value.

Signature

```
   global void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

Date and time of the gateway communication.

Return Value

Type: void

##### setGatewayMessage(gatewayMessage)

Sets error messages that the gateway returned for the payment request. Maximum length of 255 characters.

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String

Information on error messages sent from the gateway.

Return Value

Type: void

##### setGatewayResultCode(gatewayResultCode)

Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.


Apex Reference Guide AbstractResponse Class

Signature

```
   global void setGatewayResultCode(String gatewayResultCode)

```

Parameters

```
   gatewayResultCode
```

Type: String

Gateway-specific result code. Must be used to map a Salesforce-specific result code.

Return Value

Type: void

##### setGatewayResultCodeDescription(gatewayResultCodeDescription)

Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

Signature

```
   global void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Description of the gateway’s result code. Use this field to learn more about why the gateway returned a certain result code.

Return Value

Type: void

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce uses
the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: commercepayments.SalesforceResultCodeInfo on page 519

Description of the Salesforce result code value.


### Apex Reference Guide AbstractTransactionResponse Class

Return Value

Type: void

##### **`setRetryCategory(retryCategory)`**

Sets the retry category returned by the payment gateway for the failed payment in a batch flow.

Signature

```
   public void setRetryCategory(commercepayments.RetryCategory retryCategory)

```

Parameters

```
   retryCategory
```

Type: commercepayments.RetryCategory

Specifies the payment failure category used to determine retry eligibility.

Return Value

Type: void

##### **`setRetryDecision(retryDecision)`**

Sets the retry decision.

Signature

```
   public void setRetryDecision(commercepayments.RetryDecision retryDecision)

```

Parameters

```
   retryDecision
```

Type: commercepayments.RetryDecision

Determines whether the payment operation can be retried based on the retry category.

Return Value

Type: void

### AbstractTransactionResponse Class

Abstract class for storing normalized information sent from payment gateways about a payment transaction. Holds the common response
fields sent from payment gateways for authorization, sale, capture, and refund transactions.

Namespace

CommercePayments


Apex Reference Guide AbstractTransactionResponse Class

Usage

Specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes no arguments.
For example:

```
   CommercePayments.AbstractTransactionResponse atr = new

   CommercePayments.AbstractTransactionResponse();

```

IN THIS SECTION:

#### AbstractTransactionResponse Methods AbstractTransactionResponse Methods The following are methods for AbstractTransactionResponse .

IN THIS SECTION:

##### setAmount(amount)

Sets the transaction amount. Must be a non-negative value.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the notification occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the notification request. Maximum length of 255 characters.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets the payment gateway’s reference details.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the payment gateway’s reference number.

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. You can map the result code to a Salesforce-specific result code. Maximum length of 64 characters.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information.

##### setAmount(amount)

Sets the transaction amount. Must be a non-negative value.

Signature

```
   global void setAmount(Double amount)

```


Apex Reference Guide AbstractTransactionResponse Class

Parameters

```
   amount
```

Type: Double

The amount of the transaction.

Return Value

Type: void

##### setGatewayAvsCode(gatewayAvsCode)

Sets the AVS (address verification system) result code that the gateway returned. Maximum length of 64 characters.

Signature

```
   global void setGatewayAvsCode(String gatewayAvsCode)

```

Parameters

```
   gatewayAvsCode
```

Type: String

Used to verify the address mapped to a payment method when the payments platform requests tokenization from the payment
gateway.

Return Value

Type: void

##### setGatewayDate(gatewayDate)

Sets the date that the notification occurred. Some gateways don’t send this value.

Signature

```
   global void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

The date that the transaction occurred.

Return Value

Type: void

##### setGatewayMessage(gatewayMessage)

Sets error messages that the gateway returned for the notification request. Maximum length of 255 characters.


Apex Reference Guide AbstractTransactionResponse Class

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String

The message that the gateway returned with the transaction request. Contains additional information about the transaction.

Return Value

Type: void

##### setGatewayReferenceDetails(gatewayReferenceDetails)

Sets the payment gateway’s reference details.

Signature

```
   global void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String

Provides information about the gateway communication.

Return Value

Type: void

##### setGatewayReferenceNumber(gatewayReferenceNumber)

Sets the payment gateway’s reference number.

Signature

```
   global void setGatewayReferenceNumber(String gatewayReferenceNumber)

```

Parameters

```
   gatewayReferenceNumber
```

Type: String

Unique transaction ID created by the payment gateway.

Return Value

Type: void


Apex Reference Guide AbstractTransactionResponse Class

##### setGatewayResultCode(gatewayResultCode)

Sets a gateway-specific result code. You can map the result code to a Salesforce-specific result code. Maximum length of 64 characters.

Signature

```
   global void setGatewayResultCode(String gatewayResultCode)

```

Parameters

```
   gatewayResultCode
```

Type: String

Gateway-specific result code. Must be mapped to a Salesforce-specific result code.

Return Value

Type: void

##### setGatewayResultCodeDescription(gatewayResultCodeDescription)

Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

Signature

```
   global void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Provides additional information about the result code and why the gateway returned the specific code. Descriptions vary between
different gateways.

Return Value

Type: void

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Sets the Salesforce-specific result code information.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: commercepayments.SalesforceResultCodeInfo on page 519


### Apex Reference Guide AccountType Enum

Payment gateways have many response codes for payment calls. Salesforce uses the result code information to map payment
gateway codes to a predefined set of standard Salesforce result codes.

Return Value

Type: void

### AccountType Enum

Specifies the account type.

Enum Values

The following are the values of the `commercepayments.AccountType` enum.

**Value** **Description**

```
   Checking

   Savings

### AccountHolderType Enum

```

Specifies the type of the account holder.

Enum Values

The following are the values of the `commercepayments.AccountHolderType` enum.

**Value** **Description**

```
   Business

   Individual

### AddressRequest Class

```

Contains address request data that is sent to a gateway adapter during a service call.

Namespace

CommercePayments

Usage

Contains information about the payment method’s address. Use this information in authorization, sale, and tokenization requests. The
payment gateway adapter uses information in an AddressRequest object to construct a JSON request to send to the payment gateway.

The constructor of this class takes no arguments. For example:


Apex Reference Guide AddressRequest Class

```
   CommercePayments.AddressRequest adr = new CommercePayments.AddressRequest();

```

IN THIS SECTION:

#### AddressRequest Constructors

AddressRequest Properties

AddressRequest Methods

#### AddressRequest Constructors The following are constructors for AddressRequest .

IN THIS SECTION:

##### AddressRequest(street, city, state, country, postalCode)

Constructs a sample address. This constructor is intended for test usage and throws an exception if used outside of the Apex test
context.

##### AddressRequest(street, city, state, country, postalCode)

Constructs a sample address. This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Signature

```
   global AddressRequest(String street, String city, String state, String country, String

   postalCode)

```

Parameters

```
   street
```

Type: String

Street for the payment method's address.

```
   city
```

Type: String

City for the payment method's address.

```
   state
```

Type: String

State for the payment method's address.

```
   country
```

Type: String

Country for the payment method's address.

```
   postalCode
```

Type: String

Postal code for the payment method's address.


Apex Reference Guide AddressRequest Class

#### AddressRequest Properties The following are properties for AddressRequest .

IN THIS SECTION:

##### city

City of the payment method address.

##### companyName

Company name of the payment method address.

##### country

Country for the payment method address.

postalCode
Postal code for the payment method address.

state
State for the payment method address.

street
Street for the payment method address.

##### city

City of the payment method address.

Signature

```
   global String city {get; set;}

```

Property Value

Type: String

##### companyName

Company name of the payment method address.

Signature

```
   global String companyName {get; set;}

```

Property Value

Type: String

##### country

Country for the payment method address.


Apex Reference Guide AddressRequest Class

Signature

```
   global String country {get; set;}

```

Property Value

Type: String

##### postalCode

Postal code for the payment method address.

Signature

```
   global String postalCode {get; set;}

```

Property Value

Type: String

##### state

State for the payment method address.

Signature

```
   global String state {get; set;}

```

Property Value

Type: String

##### street

Street for the payment method address.

Signature

```
   global String street {get; set;}

```

Property Value

Type: String

#### AddressRequest Methods The following are methods for AddressRequest .


Apex Reference Guide AddressRequest Class

IN THIS SECTION:

##### equals(obj)

Maintains the integrity of lists of type `AddressRequest` by determining the equality of external objects in a list. This method
is dynamic and is based on the equals method in Java.

##### hashCode()

Maintains the integrity of lists of type `AddressRequest` .

##### toString()

Converts a date to a string.

##### equals(obj)

Maintains the integrity of lists of type `AddressRequest` by determining the equality of external objects in a list. This method is
dynamic and is based on the equals method in Java.

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### hashCode()

Maintains the integrity of lists of type `AddressRequest` .

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### toString()

Converts a date to a string.

Signature

```
   global String toString()

```


### Apex Reference Guide AlternativePaymentMethodRequest Class

Return Value

Type: String

### AlternativePaymentMethodRequest Class

The class contains information about the alternative payment method that are required for a gateway to process the request.

Namespace

CommercePayments

Example

```
   commercepayments.PostAuthApiPaymentMethodRequest apiPaymentMethod

   =(commercepayments.PostAuthApiPaymentMethodRequest) postAuthRequest.paymentMethod;

   commercepayments.AlternativePaymentMethodRequest alternativePaymentMethod=

   (commercepayments.AlternativePaymentMethodRequest) apiPaymentMethod.alternativePaymentMethod;

   String gatewayToken = (String)alternativePaymentMethod.gatewayToken;

   String gatewayTokenDetails = (String)alternativePaymentMethod.gatewayTokenDetails;

   String name = (String)alternativePaymentMethod.name;

   String accountId = (String)alternativePaymentMethod.accountId;

   String email = (String)alternativePaymentMethod.email;

```

IN THIS SECTION:

#### AlternativePaymentMethodRequest Constructors

AlternativePaymentMethodRequest Properties

AlternativePaymentMethodRequest Methods

#### AlternativePaymentMethodRequest Constructors

### The following are constructors for AlternativePaymentMethodRequest .

IN THIS SECTION:

##### AlternativePaymentMethodRequest(gatewayToken)

Creates a new instance of the `CommercePayments.AlternativePaymentMethodRequest` class.

##### **`AlternativePaymentMethodRequest(gatewayToken)`**

Creates a new instance of the `CommercePayments.AlternativePaymentMethodRequest` class.

Signature

```
   public AlternativePaymentMethodRequest(String gatewayToken)

```


Apex Reference Guide AlternativePaymentMethodRequest Class

Parameters

```
   gatewayToken
```

Type: String

A unique, alphanumeric ID, called a token, that a payment gateway generates when it first processes a payment. The token replaces
the actual payment data so that the data is kept secure. This token is stored as encrypted text, and can be used for recurring payments.

#### AlternativePaymentMethodRequest Properties The following are properties for AlternativePaymentMethodRequest .

IN THIS SECTION:

##### accountId

Salesforce account ID to which this payment method is linked.

##### email

Email address of the card holder.

gatewayToken
A unique, alphanumeric ID, that a payment gateway generates when it first processes a payment.

gatewayTokenDetails
Information about the gateway token.

name
Name that you assign to the PaymentMethod object.

##### **`accountId`**

Salesforce account ID to which this payment method is linked.

Signature

```
   public String accountId {get; set;}

```

Property Value

Type: String

##### **`email`**

Email address of the card holder.

Signature

```
   public String email {get; set;}

```

Property Value

Type: String


Apex Reference Guide AlternativePaymentMethodRequest Class

##### **`gatewayToken`**

A unique, alphanumeric ID, that a payment gateway generates when it first processes a payment.

The token replaces the actual payment data so that the data is kept secure. This token is stored as encrypted text, and can be used for
recurring payments.

Signature

```
   public String gatewayToken {get; set;}

```

Property Value

Type: String

##### **`gatewayTokenDetails`**

Information about the gateway token.

Signature

```
   public String gatewayTokenDetails {get; set;}

```

Property Value

Type: String

##### **`name`**

Name that you assign to the PaymentMethod object.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

#### AlternativePaymentMethodRequest Methods The following are methods for AlternativePaymentMethodRequest .

IN THIS SECTION:

equals(obj)
#### Maintains the integrity of lists of type AlternativePaymentMethodRequest by determining the equality of external

objects in a list. This method is dynamic and based on the equals method in Java.

hashCode()
#### Maintains the integrity of lists of type AlternativePaymentMethodRequest by determining the uniqueness of the external

object records in a list.


### Apex Reference Guide AlternativePaymentMethodResponse Class

##### toString()

Converts a date to a string.

##### **`equals(obj)`**

Maintains the integrity of lists of type `AlternativePaymentMethodRequest` by determining the equality of external objects
in a list. This method is dynamic and based on the equals method in Java.

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### **`hashCode()`**

Maintains the integrity of lists of type `AlternativePaymentMethodRequest` by determining the uniqueness of the external
object records in a list.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a date to a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### AlternativePaymentMethodResponse Class

The class contains the response details of the alternative payment method.


Apex Reference Guide AlternativePaymentMethodResponse Class

Namespace

CommercePayments

Example

```
   commercepayments.AlternativePaymentMethodResponse response = new

   commercepayments.AlternativePaymentMethodResponse();

   response.setEmail('alternativePaymentMethod');

   response.setEmail('foo@foo.com');

   response.setGatewayToken('NMoPoIOnTZSaRaWcV7gUUXe');

   response.setGatewayTokenDetails('gateway token details');

```

IN THIS SECTION:

#### AlternativePaymentMethodResponse Methods AlternativePaymentMethodResponse Methods The following are methods for AlternativePaymentMethodResponse .

IN THIS SECTION:

##### setAccountId(accountId)

Sets the ID of the Salesforce payments account to which the payment method is linked.

setComments(comments)
Sets the notes about the payment method added by users.

setEmail(email)
Sets the email ID of the card holder.

setGatewayToken(gatewayToken)
Sets the token ID that a payment gateway generates when it first processes a payment.

setGatewayTokenDetails(gatewayTokenDetails)
Sets the details about the payment gateway token.

setName(name)
Sets the name that is assigned to the PaymentMethod object.

##### **`setAccountId(accountId)`**

Sets the ID of the Salesforce payments account to which the payment method is linked.

Signature

```
   public void setAccountId(Id accountId)

```


Apex Reference Guide AlternativePaymentMethodResponse Class

Parameters

```
   accountId
```

Type: Id

Salesforce payments account ID.

Return Value

Type: void

##### **`setComments(comments)`**

Sets the notes about the payment method added by users.

Signature

```
   public void setComments(String comments)

```

Parameters

```
   comments
```

Type: String

Notes about the payment method added by users, maximum 1000 characters.

Return Value

Type: void

##### **`setEmail(email)`**

Sets the email ID of the card holder.

Signature

```
   public void setEmail(String email)

```

Parameters

```
   email
```

Type: String

Email ID of the card holder.

Return Value

Type: void

##### **`setGatewayToken(gatewayToken)`**

Sets the token ID that a payment gateway generates when it first processes a payment.


Apex Reference Guide AlternativePaymentMethodResponse Class

Signature

```
   public void setGatewayToken(String gatewayToken)

```

Parameters

```
   gatewayToken
```

Type: String

A unique, alphanumeric ID, called a token, that a payment gateway generates when it first processes a payment. The token replaces
the actual payment data so that the data is kept secure. This token is stored as encrypted text, and can be used for recurring payments.

Return Value

Type: void

##### **`setGatewayTokenDetails(gatewayTokenDetails)`**

Sets the details about the payment gateway token.

Signature

```
   public void setGatewayTokenDetails(String gatewayTokenDetails)

```

Parameters

```
   gatewayTokenDetails
```

Type: String

Detailed information about the gateway token.

Return Value

Type: void

##### **`setName(name)`**

Sets the name that is assigned to the PaymentMethod object.

Signature

```
   public void setName(String name)

```

Parameters

```
   name
```

Type: String

Name that you assign to the payment method object.

Return Value

Type: void


### Apex Reference Guide AuditParamsRequest AuditParamsRequest AuditParamsRequest is used for audit parameters in a transaction request. This is an abstract request class that is extended by

the `BaseRequest` class.

Namespace

CommercePayments

Usage

### AuditParamsRequest is an abstract class that holds attributes related to audit parameters such as email, IP address, MAC address,

and phone number. This class can't be instantiated on its own. All `CommercePayments` request classes extend this class.

IN THIS SECTION:

### AuditParamsRequest Constructors AuditParamsRequest Properties AuditParamsRequest Constructors The following are constructors for AuditParamsRequest .

IN THIS SECTION:

### AuditParamsRequest(email, macAddress, ipAddress, phone)

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

### AuditParamsRequest(email, macAddress, ipAddress, phone)

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Signature

### `AuditParamsRequest(String email, String macAddress, String ipAddress, String phone)`

Parameters

```
   email
```

Type: String

Email of the client that initiated the request.

```
   macAddress
```

Type: String

Mac address of the customer’s device. Gateways often use this data in risk checks.

```
   ipAddress
```

Type: String

The customer’s IP address. Gateways often use this data in risk checks.


#### Apex Reference Guide AuditParamsRequest

##### _`phone`_

Type: String

Phone number of the client that initiated the request.

#### AuditParamsRequest Properties The following are properties for AuditParamsRequest .

IN THIS SECTION:

##### email

Email of the client that initiated the request.

##### ipAddress

The customer’s IP address. Gateways often use this data in risk checks.

##### macAddress

Mac address of the customer’s device. Gateways often use this data in risk checks.

##### phone

Phone number of the client that initiated the request.

##### email

Email of the client that initiated the request.

Property Value

Type: String

##### ipAddress

The customer’s IP address. Gateways often use this data in risk checks.

Property Value

Type: String

##### macAddress

Mac address of the customer’s device. Gateways often use this data in risk checks.

Property Value

Type: String

##### phone

Phone number of the client that initiated the request.


### Apex Reference Guide AuthApiPaymentMethodRequest Class

Property Value

Type: String

### AuthApiPaymentMethodRequest Class

Sends information about a payment method to a gateway adapter during an authorization service call.

Namespace

CommercePayments

Usage

Contains information about the payment method that is used for an authorization request. It contains all available payment methods
as fields, but populates only one field for each request. The gateway adapter uses this class when constructing an authorization request.
An object of this class is available through the `paymentMethod` field on the `AuthorizationRequest Class` object.

IN THIS SECTION:

#### AuthApiPaymentMethodRequest Constructors

AuthApiPaymentMethodRequest Properties

#### AuthApiPaymentMethodRequest Constructors

### The following are constructors for AuthApiPaymentMethodRequest .

IN THIS SECTION:

##### AuthApiPaymentMethodRequest(cardPaymentMethodRequest)

Constructs a sample `cardPaymentMethodRequest` . This constructor is intended for test usage and throws an exception if
used outside of the Apex test context.

AuthApiPaymentMethodRequest()
### Constructor for AuthApiPaymentMethodRequest .

##### AuthApiPaymentMethodRequest(cardPaymentMethodRequest)

Constructs a sample `cardPaymentMethodRequest` . This constructor is intended for test usage and throws an exception if used
outside of the Apex test context.

Signature

```
   global AuthApiPaymentMethodRequest(commercepayments.CardPaymentMethodRequest

   cardPaymentMethodRequest)

```

Parameters

```
   cardPaymentMethodRequest
```

Type: commercepayments.CardPaymentMethodRequest on page 404


### Apex Reference Guide AuthorizationRequest Class

Contains information about the card payment method. Used to send information to a gateway adapter during a service call.

##### AuthApiPaymentMethodRequest() Constructor for AuthApiPaymentMethodRequest .

Signature

```
   global AuthApiPaymentMethodRequest()

#### AuthApiPaymentMethodRequest Properties

##### The following are properties for AuthApiPaymentMethodRequest .

```

IN THIS SECTION:

##### cardPaymentMethod

The card payment method object used in a payment method request.

##### cardPaymentMethod

The card payment method object used in a payment method request.

Signature

```
   global commercepayments.CardPaymentMethodRequest cardPaymentMethod {get; set;}

```

Property Value

Type: commercepayments.CardPaymentMethodRequest on page 404

### AuthorizationRequest Class

Sends information about an authorization request to a gateway adapter during a service call. This class extends the `BaseRequest`
class and inherits all its methods.

Namespace

CommercePayments

Usage

This class contains information about a transaction authorization request. The gateway adapter reads fields from this class while
constructing an authorization JSON request to send to the payment gateway. An object of this class is available by calling
`getPaymentRequest()` in the `PaymentGatewayContext Class` .


Apex Reference Guide AuthorizationRequest Class

Example

Creating a `buildAuthRequest` class to store information about the authorization request.

```
   private String buildAuthRequest(commercepayments.AuthorizationRequest authRequest) {

        // Multiply amount by 100.0 to convert to cents

        String requestBody =

   createRequestBody(String.ValueOf((authRequest.amount*100.0).intValue()), authRequest);

        return requestBody;

       private String createRequestBody(String amount, commercepayments.AuthorizationRequest

    authRequest) {

        JSONGenerator jsonGeneratorInstance = JSON.createGenerator(true);

        String currencyIso = authRequest.currencyIsoCode;

        commercepayments.AuthApiPaymentMethodRequest paymentMethod =

   authRequest.paymentMethod;

        commercepayments.GatewayErrorResponse error;

        // Write data to the JSON string.

        jsonGeneratorInstance.writeStartObject();

       jsonGeneratorInstance.writeStringField('merchantAccount', '{!$Credential.Username}');

        jsonGeneratorInstance.writeStringField('reference', authRequest.comments == null

   ? 'randomstring' : authRequest.comments);

        if(currencyIso == null) {

           currencyIso = UserInfo.getDefaultCurrency();

        }

        jsonGeneratorInstance.writeFieldName('amount');

        jsonGeneratorInstance.writeStartObject();

        jsonGeneratorInstance.writeStringField('value', amount);

        jsonGeneratorInstance.writeStringField('currency', currencyIso);

        jsonGeneratorInstance.writeEndObject();

        commercepayments.CardPaymentMethodRequest cardPaymentMethod;

        if(paymentMethod != null) {

           cardPaymentMethod = paymentMethod.cardPaymentMethod;

           if (cardPaymentMethod != null) {

             if (cardPaymentMethod.CardCategory != null) {

               if (commercepayments.CardCategory.CreditCard ==

   cardPaymentMethod.CardCategory) {

                  jsonGeneratorInstance.writeFieldName('card');

                  jsonGeneratorInstance.writeStartObject();

                  if (cardPaymentMethod.cvv != null)

                    jsonGeneratorInstance.writeStringField('cvc',

   String.ValueOf(cardPaymentMethod.cvv));

                  if (cardPaymentMethod.cardholdername != null)

                    jsonGeneratorInstance.writeStringField('holderName',

   cardPaymentMethod.cardholdername);

                  if (cardPaymentMethod.cardnumber != null)

                    jsonGeneratorInstance.writeStringField('number',

   cardPaymentMethod.cardnumber);

                  if (cardPaymentMethod.expiryMonth != null &&

   cardPaymentMethod.expiryYear != null ) {

                    String expMonth =

```


Apex Reference Guide AuthorizationRequest Class

```
   ((String.ValueOf(cardPaymentMethod.expiryMonth)).length() == 1 ? '0' : '') +

   String.ValueOf(cardPaymentMethod.expiryMonth);

                  jsonGeneratorInstance.writeStringField('expiryMonth', expMonth);

                    jsonGeneratorInstance.writeStringField('expiryYear',

   String.ValueOf(cardPaymentMethod.expiryYear));

                  }

                  jsonGeneratorInstance.writeEndObject();

               } else {

               //Support for other card type

               }

             } else {

               throw new SampleValidationException('Required Field Missing :

   CardCategory');

             }

           } else {

             throw new SampleValidationException('Required Field Missing :

   CardPaymentMethod');

           }

        } else {

          throw new SampleValidationException('Required Field Missing : PaymentMethod');

        }

        jsonGeneratorInstance.writeEndObject();

        return jsonGeneratorInstance.getAsString();

      }

```

IN THIS SECTION:

#### AuthorizationRequest Constructors

AuthorizationRequest Properties

AuthorizationRequest Methods

#### AuthorizationRequest Constructors The following are constructors for AuthorizationRequest .

IN THIS SECTION:

##### AuthorizationRequest(amount)

Constructor for building the amount in an authorization request. This constructor is intended for test usage and throws an exception
if used outside of the Apex test context.

##### AuthorizationRequest(amount)

Constructor for building the amount in an authorization request. This constructor is intended for test usage and throws an exception if
used outside of the Apex test context.

Signature

```
   global AuthorizationRequest(Double amount)

```


Apex Reference Guide AuthorizationRequest Class

Parameters

##### _`amount`_

Type: Double

The amount of the authorization.

#### AuthorizationRequest Properties The following are properties for AuthorizationRequest .

IN THIS SECTION:

##### accountId

The customer account where the authorization is performed.

##### amount

The total amount of the authorization. Can be positive or negative.

comments
Comments about the authorization. Users can enter comments to provide additional information.

currencyIsoCode
The ISO currency code for the authorization request.

paymentMethod
The payment method used to process the authorization in the authorization request.

paymentMethodData
Payment method data used in the authorize payment request.

##### accountId

The customer account where the authorization is performed.

Signature

```
   global String accountId {get; set;}

```

Property Value

Type: String

##### amount

The total amount of the authorization. Can be positive or negative.

Signature

```
   global Double amount {get; set;}

```

Property Value

Type: Double


Apex Reference Guide AuthorizationRequest Class

##### comments

Comments about the authorization. Users can enter comments to provide additional information.

Signature

```
   global String comments {get; set;}

```

Property Value

Type: String

##### currencyIsoCode

The ISO currency code for the authorization request.

Signature

```
   global String currencyIsoCode {get; set;}

```

Property Value

Type: String

##### paymentMethod

The payment method used to process the authorization in the authorization request.

Signature

```
   global AuthApiPaymentMethodRequest paymentMethod {get; set;}

```

Property Value

Type: AuthApiPaymentMethodRequest on page 343

##### **`paymentMethodData`**

Payment method data used in the authorize payment request.

##### This field is populated when AuthorizationInput specifies a saved payment method. Accessible using paymentMethodData

on `AuthorizationRequest` . The map contains these fields from `SavedPaymentMethod` : `GatewayToken`, `Type`,
`GatewayReference`, and `StandardEntryCode` for direct gateway interaction without querying the database. This field is
supported only for saved payment methods of type card.

Signature

```
   public Map<String,String> paymentMethodData {get; set;}

```

Property Value

Type: Map<String,String>


Apex Reference Guide AuthorizationRequest Class

#### AuthorizationRequest Methods The following are methods for AuthorizationRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type AuthorizationRequest by determining the equality of external objects in a list. This

method is dynamic and based on the equals method in Java.

##### hashCode()
#### Maintains the integrity of lists of type AuthorizationRequest by determining the uniqueness of the external object in a list.

##### toString()

Converts a date to a string.

##### equals(obj)

#### Maintains the integrity of lists of type AuthorizationRequest by determining the equality of external objects in a list. This

method is dynamic and based on the equals method in Java.

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### hashCode()

#### Maintains the integrity of lists of type AuthorizationRequest by determining the uniqueness of the external object in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### toString()

Converts a date to a string.


### Apex Reference Guide AuthorizationResponse Class

Signature

```
   global String toString()

```

Return Value

Type: String

### AuthorizationResponse Class

Response sent by the payment gateway adapter for an authorization service.

Namespace

CommercePayments

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.AuthorizationResponse authr = new

   CommercePayments.AuthorizationResponse();

```

Contains information about the payment gateway’s response following an authorization transaction. The gateway adapter uses the
### payment gateway’s response to populate the AuthorizationResponse fields. The payments platform uses the information from

this class to construct the authorization gateway response shown to the user.

Example

```
   private commercepayments.GatewayResponse createAuthResponse(HttpResponse response, Double

    amount) {

        Map<String, Object> mapOfResponseValues = (Map

                    <String, Object>) JSON.deserializeUntyped(response.getBody());

        commercepayments.AuthorizationResponse authResponse = new

   commercepayments.AuthorizationResponse();

        String resultCode = (String)mapOfResponseValues.get('resultCode');

        if(resultCode != null){

           system.debug('Response - success');

           if(resultCode.equals('Authorised')){

             system.debug('status - authorised');

            authResponse.setGatewayAuthCode((String)mapOfResponseValues.get('authCode'));

             authResponse.setSalesforceResultCodeInfo(new

   commercepayments.SalesforceResultCodeInfo(commercepayments.SalesforceResultCode.Success));

           } else {

             //Sample returns 200 with refused status in some cases

             system.debug('status - refused');

```


Apex Reference Guide AuthorizationResponse Class

```
   authResponse.setGatewayResultCodeDescription((String)mapOfResponseValues.get('refusalReason'));

             authResponse.setSalesforceResultCodeInfo(new

   commercepayments.SalesforceResultCodeInfo(commercepayments.SalesforceResultCode.Decline));

           }

   authResponse.setGatewayReferenceNumber((String)mapOfResponseValues.get('pspReference'));

           authResponse.setAmount(amount);

           authResponse.setGatewayDate(system.now());

           return authResponse;

        } else {

           system.debug('Response - failed');

           system.debug('Validation error');

           String statusCode = (String)mapOfResponseValues.get('errorType');

           String message = (String)mapOfResponseValues.get('message');

           commercepayments.GatewayErrorResponse error = new

   commercepayments.GatewayErrorResponse(statusCode, message);

           return error;

        }

      }

```

IN THIS SECTION:

#### AuthorizationResponse Methods AuthorizationResponse Methods The following are methods for AuthorizationResponse .

IN THIS SECTION:

setAmount(amount)
Sets the amount of the authorization. Must be a non-zero value.

setAsync(async)
Indicates whether the gateway response is received asynchronously ( `true` ) or not ( `false` ). When set to `true`, the authorize
payment method remains in a pending state until the async notification is received.

setAuthorizationExpirationDate(authExpDate)
Sets the expiration date of the authorization request.

setGatewayAuthCode(gatewayAuthCode)
Sets the authorization code that the gateway returned. Maximum length of 64 characters.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the authorization occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the authorization request. Maximum length of 255 characters.


Apex Reference Guide AuthorizationResponse Class

setGatewayReferenceDetails(gatewayReferenceDetails)
Stores data that you can use for subsequent authorizations. You can use any data that isn’t normalized in financial entities. This field
has a maximum length of 1000 characters and can store data as JSON or XML.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the unique gateway reference number for the transaction that the gateway returned. Maximum length of 255 characters.

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. The code can be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

setPaymentMethodTokenizationResponse(paymentMethodTokenizationResponse)
Sets information from the gateway about the tokenized payment method.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

##### setAmount(amount)

Sets the amount of the authorization. Must be a non-zero value.

Signature

```
   global void setAmount(Double amount)

```

Parameters

```
   amount
```

Type: Double

Return Value

Type: void

##### **`setAsync(async)`**

Indicates whether the gateway response is received asynchronously ( `true` ) or not ( `false` ). When set to `true`, the authorize payment
method remains in a pending state until the async notification is received.

Signature

```
   public void setAsync(Boolean async)

```

Parameters

```
   async
```

Type: Boolean


Apex Reference Guide AuthorizationResponse Class

Return Value

Type: void

##### setAuthorizationExpirationDate(authExpDate)

Sets the expiration date of the authorization request.

Signature

```
   global void setAuthorizationExpirationDate(Datetime authExpDate)

```

Parameters

```
   authExpDate
```

Type: Datetime

Return Value

Type: void

##### setGatewayAuthCode(gatewayAuthCode)

Sets the authorization code that the gateway returned. Maximum length of 64 characters.

Signature

```
   global void setGatewayAuthCode(String gatewayAuthCode)

```

Parameters

```
   gatewayAuthCode
```

Type: String

The authorization code returned by the gateway.

Return Value

Type: void

##### setGatewayAvsCode(gatewayAvsCode)

Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

Signature

```
   global void setGatewayAvsCode(String gatewayAvsCode)

```

Parameters

```
   gatewayAvsCode
```

Type: String


Apex Reference Guide AuthorizationResponse Class

Used to verify the address mapped to a payment method when the payments platform requests tokenization from the payment
gateway.

Return Value

Type: void

##### setGatewayDate(gatewayDate)

Sets the date that the authorization occurred. Some gateways don’t send this value.

Signature

```
   global void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

Return Value

Type: void

##### setGatewayMessage(gatewayMessage)

Sets error messages that the gateway returned for the authorization request. Maximum length of 255 characters.

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String

Return Value

Type: void

##### setGatewayReferenceDetails(gatewayReferenceDetails)

Stores data that you can use for subsequent authorizations. You can use any data that isn’t normalized in financial entities. This field has
a maximum length of 1000 characters and can store data as JSON or XML.

Signature

```
   global void setGatewayReferenceDetails(String gatewayReferenceDetails)

```


Apex Reference Guide AuthorizationResponse Class

Parameters

```
   gatewayReferenceDetails
```

Type: String

Return Value

Type: void

##### setGatewayReferenceNumber(gatewayReferenceNumber)

Sets the unique gateway reference number for the transaction that the gateway returned. Maximum length of 255 characters.

Signature

```
   global void setGatewayReferenceNumber(String gatewayReferenceNumber)

```

Parameters

```
   gatewayReferenceNumber
```

Type: String

Unique authorization ID created by the payment gateway.

Return Value

Type: void

##### setGatewayResultCode(gatewayResultCode)

Sets a gateway-specific result code. The code can be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

Signature

```
   global void setGatewayResultCode(String gatewayResultCode)

```

Parameters

```
   gatewayResultCode
```

Type: String

Gateway-specific result code. Must be used to map a Salesforce-specific result code.

Return Value

Type: void

##### setGatewayResultCodeDescription(gatewayResultCodeDescription)

Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.


Apex Reference Guide AuthorizationResponse Class

Signature

```
   global void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Description of the gateway’s result code. Use this field to learn more about why the gateway returned a certain result code.

Return Value

Type: void

##### setPaymentMethodTokenizationResponse(paymentMethodTokenizationResponse)

Sets information from the gateway about the tokenized payment method.

Signature

```
   global void

   setPaymentMethodTokenizationResponse(commercepayments.PaymentMethodTokenizationResponse

   paymentMethodTokenizationResponse)

```

Parameters

```
   paymentMethodTokenizationResponse
```

PaymentMethodTokenizationResponse on page 455

Gateway response sent by payment gateway adapters for the payment method tokenization request.

Return Value

Type: void

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce uses
the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: SalesforceResultCodeInfo on page 519

Description of the Salesforce result code value.


### Apex Reference Guide AuthorizationReversalRequest Class

Return Value

Type: void

### AuthorizationReversalRequest Class

Sends information about an authorization reversal request to a gateway adapter during a service call.

Namespace

CommercePayments on page 317

Example

### Add your reversal classes to your payment gateway adapter. We recommend adding AuthorizationReversal as a possible

requestType value when calling processRequest on the gateway’s response.

```
   global commercepayments.GatewayResponse processRequest(commercepayments.paymentGatewayContext

    gatewayContext) {

        commercepayments.RequestType requestType = gatewayContext.getPaymentRequestType();

        commercepayments.GatewayResponse response;

        try {

        //add other requestType values here

        //..

        else if (requestType == commercepayments.RequestType.AuthorizationReversal) {

             response =

   createAuthReversalResponse((commercepayments.AuthorizationReversalRequest)gatewayContext.getPaymentRequest());}

        return response;

```

Then, add a class that sets the amount of the authorization reversal request, as well as gateway information and the Salesforce result
code.

```
   global commercepayments.GatewayResponse

   createAuthReversalResponse(commercepayments.AuthorizationReversalRequest authReversalRequest)

    {

        commercepayments.AuthorizationReversalResponse authReversalResponse = new

   commercepayments.AuthorizationReversalResponse();

        if(authReversalRequest.amount!=null )

        {

           authReversalResponse.setAmount(authReversalRequest.amount);

        }

        else

        {

           throw new SalesforceValidationException('Required Field Missing : Amount');

        }

        system.debug('Response - success');

        authReversalResponse.setGatewayDate(system.now());

```


Apex Reference Guide AuthorizationReversalRequest Class

```
        authReversalResponse.setGatewayResultCode('00');

        authReversalResponse.setGatewayResultCodeDescription('Transaction Normal');

        authReversalResponse.setGatewayReferenceNumber('SF'+getRandomNumber(6));

   authReversalResponse.setSalesforceResultCodeInfo(SUCCESS_SALESFORCE_RESULT_CODE_INFO);

        return authReversalResponse;

      }

```

IN THIS SECTION:

#### AuthorizationReversalRequest Constructors AuthorizationReversalRequest Properties

AuthorizationReversalRequest Methods

#### AuthorizationReversalRequest Constructors The following are constructors for AuthorizationReversalRequest .

IN THIS SECTION:

##### AuthorizationReversalRequest(amount, authorizationId)

Constructor for building the amount in an authorization reversal request. This constructor is intended for test usage and throws an
exception if used outside of the Apex test context.

##### AuthorizationReversalRequest(amount, authorizationId)

Constructor for building the amount in an authorization reversal request. This constructor is intended for test usage and throws an
exception if used outside of the Apex test context.

Signature

```
   global AuthorizationReversalRequest(Double amount, String authorizationId)

```

Parameters

```
   amount
```

Type: Double

The amount of the authorization reversal request.

```
   authorizationId
```

Type: String

The authorization request to be reversed.

#### AuthorizationReversalRequest Properties The following are properties for AuthorizationReversalRequest .


Apex Reference Guide AuthorizationReversalRequest Class

IN THIS SECTION:

##### accountId

References the customer account for the transaction where the authorization reversal was performed.

##### amount

The total amount of the authorization reversal request. Can be positive or negative.

##### paymentAuthorizationId

References the payment authorization to be reversed.

##### accountId

References the customer account for the transaction where the authorization reversal was performed.

Signature

```
   global String accountId {get; set;}

```

Property Value

Type: String

##### amount

The total amount of the authorization reversal request. Can be positive or negative.

Signature

```
   global Double amount {get; set;}

```

Property Value

Type: Double

##### paymentAuthorizationId

References the payment authorization to be reversed.

Signature

```
   global String paymentAuthorizationId {get; set;}

```

Property Value

Type: String

#### AuthorizationReversalRequest Methods The following are methods for AuthorizationReversalRequest .


Apex Reference Guide AuthorizationReversalRequest Class

IN THIS SECTION:

##### equals(obj)

Maintains the integrity of lists of type `AuthorizationReversalRequest` by determining the equality of external objects
in a list. This method is dynamic and based on the equals method in Java.

##### hashCode()

Maintains the integrity of lists of type `AuthorizationReversalRequest` by determining the uniqueness of the external
object in a list.

##### toString()

Converts a date to a string.

##### equals(obj)

Maintains the integrity of lists of type `AuthorizationReversalRequest` by determining the equality of external objects in a
list. This method is dynamic and based on the equals method in Java.

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### hashCode()

Maintains the integrity of lists of type `AuthorizationReversalRequest` by determining the uniqueness of the external object
in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### toString()

Converts a date to a string.

Signature

```
   global String toString()

```


### Apex Reference Guide AuthorizationReversalResponse Class

Return Value

Type: String

### AuthorizationReversalResponse Class

Response sent by the payment gateway following a payment authorization reversal service.

Namespace

CommercePayments

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.AuthorizationReversalResponse authRevRes = new

   CommercePayments.AuthorizationResponse();

```

Contains information about the payment gateway’s response following an authorization reversal transaction. The gateway adapter uses
### the payment gateway’s response to populate the AuthorizationReversalResponse fields. The payments platform uses the

information from this class to construct the authorization gateway response shown to the user.

Example

This class builds an authorization reversal response that contains the amount of the original reversal request, gateway information, and
the Salesforce result code.

```
   global commercepayments.GatewayResponse

   createAuthReversalResponse(commercepayments.AuthorizationReversalRequest authReversalRequest)

    {

        commercepayments.AuthorizationReversalResponse authReversalResponse = new

   commercepayments.AuthorizationReversalResponse();

        if(authReversalRequest.amount!=null )

        {

           authReversalResponse.setAmount(authReversalRequest.amount);

        }

        else

        {

           throw new SalesforceValidationException('Required Field Missing : Amount');

        }

        system.debug('Response - success');

        authReversalResponse.setGatewayDate(system.now());

        authReversalResponse.setGatewayResultCode('00');

        authReversalResponse.setGatewayResultCodeDescription('Transaction Normal');

        authReversalResponse.setGatewayReferenceNumber('SF'+getRandomNumber(6));

   authReversalResponse.setSalesforceResultCodeInfo(SUCCESS_SALESFORCE_RESULT_CODE_INFO);

        return authReversalResponse;

      }

```


Apex Reference Guide AuthorizationReversalResponse Class

IN THIS SECTION:

#### AuthorizationReversalResponse Methods AuthorizationReversalResponse Methods The following are methods for AuthorizationReversalResponse .

IN THIS SECTION:

##### setAmount(amount)

Contains the amount of the authorization reversal. Must be a non-zero value.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (Address Verification System) result code that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the authorization reversal request occurred in the payment gateway. Some gateways don't send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the authorization reversal request. Maximum length of 255 characters.

setGatewayReferenceDetails(gatewayReferenceDetails)
Stores data that you can use for subsequent authorizations. You can use any data that isn’t normalized in financial entities. This field
has a maximum length of 1000 characters and can store data as JSON or XML.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets a unique gateway reference number for the transaction that the gateway returned. Maximum length of 255 characters.

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. The code can be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

##### setAmount(amount)

Contains the amount of the authorization reversal. Must be a non-zero value.

Signature

```
   global void setAmount(Double amount)

```

Parameters

```
   amount
```

Type: Double

Return Value

Type: void


Apex Reference Guide AuthorizationReversalResponse Class

##### setGatewayAvsCode(gatewayAvsCode)

Sets the AVS (Address Verification System) result code that the gateway returned. Maximum length of 64 characters.

Signature

```
   global void setGatewayAvsCode(String gatewayAvsCode)

```

Parameters

```
   gatewayAvsCode
```

Type: String

Used to verify the address mapped to a payment method when the payments platform requests tokenization from the payment
gateway.

Return Value

Type: void

##### setGatewayDate(gatewayDate)

Sets the date that the authorization reversal request occurred in the payment gateway. Some gateways don't send this value.

Signature

```
   global void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

Return Value

Type: void

##### setGatewayMessage(gatewayMessage)

Sets error messages that the gateway returned for the authorization reversal request. Maximum length of 255 characters.

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String


Apex Reference Guide AuthorizationReversalResponse Class

Return Value

Type: void

##### setGatewayReferenceDetails(gatewayReferenceDetails)

Stores data that you can use for subsequent authorizations. You can use any data that isn’t normalized in financial entities. This field has
a maximum length of 1000 characters and can store data as JSON or XML.

Signature

```
   global void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String

Return Value

Type: void

##### setGatewayReferenceNumber(gatewayReferenceNumber)

Sets a unique gateway reference number for the transaction that the gateway returned. Maximum length of 255 characters.

Signature

```
   global void setGatewayReferenceNumber(String gatewayReferenceNumber)

```

Parameters

```
   gatewayReferenceNumber
```

Type: String

Unique reference ID created by the payment gateway.

Return Value

Type: void

##### setGatewayResultCode(gatewayResultCode)

Sets a gateway-specific result code. The code can be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

Signature

```
   global void setGatewayResultCode(String gatewayResultCode)

```


Apex Reference Guide AuthorizationReversalResponse Class

Parameters

```
   gatewayResultCode
```

Type: String

Gateway-specific result code. Must be used to map a Salesforce-specific result code.

Return Value

Type: void

##### setGatewayResultCodeDescription(gatewayResultCodeDescription)

Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

Signature

```
   global void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Description of the gateway’s result code. Use this field to learn more about why the gateway returned a certain result code.

Return Value

Type: void

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce uses
the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: SalesforceResultCodeInfo

Description of the Salesforce result code value.

Return Value

Type: void


### Apex Reference Guide BankType Enum BankType Enum

Specifies the bank type.

Enum Values

The following are the values of the `commercepayments.BankType` enum.

**Value** **Description**

`Ach` Automated Clearing House transaction.

`Bacs` Bankers' Automated Clearing Services transaction.

`Becs` Bulk Electronic Clearing System transaction.

`SepaDebit` Single Euro Payments Area transaction.

### BankPaymentMethodRequest Class

Sends data related to a bank payment method to a gateway adapter during a service call.

Namespace

CommercePayments on page 317

Usage

### Use the BankPaymentMethodRequest class to include bank payment details in a Tokenize request. The gateway adapter reads

the fields from this class when constructing the tokenized JSON request for the payment gateway. You can create an instance of this
class by calling `bankPaymentMethod` on the `PaymentMethodTokenizationRequest` class.

Example

```
   private String buildTokenizationRequest(commercepayments.PaymentMethodTokenizationRequest

    tokenizeRequest) {

      commercepayments.BankPaymentMethodRequest bankPaymentMethod =

   tokenizeRequest.bankPaymentMethod;

      // Setup currency

      String currencyIso = UserInfo.getDefaultCurrency();

      String accountId;

      JSONGenerator jsonGeneratorInstance = JSON.createGenerator(true);

      jsonGeneratorInstance.writeStartObject();

      // Basic fields

      jsonGeneratorInstance.writeStringField('merchantAccount', '{!$Credential.Username}');

      jsonGeneratorInstance.writeStringField('reference', 'Tokenize_' +

```


Apex Reference Guide BankPaymentMethodRequest Class

```
   String.valueOf(Datetime.now().getTime()));

      // Payment method details (from encrypted form input)

      jsonGeneratorInstance.writeFieldName('paymentMethod');

      jsonGeneratorInstance.writeStartObject();

      if (bankPaymentMethod != null) {

        accountId = bankPaymentMethod.accountId;

        if (bankPaymentMethod.bankType.equals(commercepayments.BankType.Ach)) {

           currencyIso = 'USD';

           jsonGeneratorInstance.writeStringField('type', 'ach');

           jsonGeneratorInstance.writeStringField('bankAccountNumber',

   bankPaymentMethod.accountNumber);

           jsonGeneratorInstance.writeStringField('bankLocationId',

   bankPaymentMethod.bankCode);

           jsonGeneratorInstance.writeStringField('ownerName',

   bankPaymentMethod.accountHolderName);

        } else if (bankPaymentMethod.bankType.equals(commercepayments.BankType.SepaDebit))

    {

           currencyIso = 'EUR';

           jsonGeneratorInstance.writeStringField('type', 'sepadirectdebit');

          jsonGeneratorInstance.writeStringField('iban', bankPaymentMethod.accountNumber);

           jsonGeneratorInstance.writeStringField('ownerName',

   bankPaymentMethod.accountHolderName);

        } else if (bankPaymentMethod.bankType.equals(commercepayments.BankType.Bacs)) {

           currencyIso = 'GBP';

           jsonGeneratorInstance.writeStringField('type', 'directdebit_GB');

           jsonGeneratorInstance.writeStringField('bankAccountNumber',

   bankPaymentMethod.accountNumber);

           jsonGeneratorInstance.writeStringField('bankLocationId',

   bankPaymentMethod.bankCode);

           jsonGeneratorInstance.writeStringField('holderName',

   bankPaymentMethod.accountHolderName);

        } else if (bankPaymentMethod.bankType.equals(commercepayments.BankType.Becs)) {

           currencyIso = 'AUD';

           jsonGeneratorInstance.writeStringField('type', 'directdebit_AU');

           jsonGeneratorInstance.writeStringField('bankAccountNumber',

   bankPaymentMethod.accountNumber);

           jsonGeneratorInstance.writeStringField('bsb', bankPaymentMethod.bankCode);

           jsonGeneratorInstance.writeStringField('ownerName',

   bankPaymentMethod.accountHolderName);

        } else {

           //Add support for other banks if required in future.

        }

        jsonGeneratorInstance.writeEndObject();

```


Apex Reference Guide BankPaymentMethodRequest Class

```
      }

      // Zero-dollar amount

      jsonGeneratorInstance.writeFieldName('amount');

      jsonGeneratorInstance.writeStartObject();

      jsonGeneratorInstance.writeNumberField('value', 0);

      jsonGeneratorInstance.writeStringField('currency', currencyIso);

      jsonGeneratorInstance.writeEndObject();

      // Save payment method for later

      jsonGeneratorInstance.writeStringField('shopperReference', accountId);

      jsonGeneratorInstance.writeBooleanField('storePaymentMethod', true);

      jsonGeneratorInstance.writeStringField('shopperInteraction', 'Ecommerce');

      jsonGeneratorInstance.writeStringField('recurringProcessingModel',

   'UnscheduledCardOnFile');

      commercepayments.AddressRequest billingAddress = tokenizeRequest.address;

      if (billingAddress != null) {

        jsonGeneratorInstance.writeFieldName('billingAddress');

        jsonGeneratorInstance.writeStartObject();

        jsonGeneratorInstance.writeStringField('street', billingAddress.street);

        jsonGeneratorInstance.writeStringField('stateOrProvince', billingAddress.state);

        jsonGeneratorInstance.writeStringField('city', billingAddress.city);

        jsonGeneratorInstance.writeStringField('postalCode', billingAddress.postalCode);

        jsonGeneratorInstance.writeStringField('country', billingAddress.country);

        jsonGeneratorInstance.writeEndObject();

      }

      jsonGeneratorInstance.writeEndObject();

      return jsonGeneratorInstance.getAsString();

   }

```

IN THIS SECTION:

#### BankPaymentMethodRequest Properties

BankPaymentMethodRequest Methods

#### BankPaymentMethodRequest Properties The following are properties for BankPaymentMethodRequest .

IN THIS SECTION:

accountHolderFirstName
The first name of the account holder for the bank payment method.

accountHolderLastName
The last name of the account holder for the bank payment method.

accountHolderName
The name of the account holder for the bank payment method.


Apex Reference Guide BankPaymentMethodRequest Class

accountHolderType
The type of the account holder.

accountId
Salesforce Payments account ID associated with the bank payment method.

accountNumber
The unique account number for the bank account.

accountType
The type for the bank account.

autoPay
Indicates whether a token for recurring payments is being requested (true) or not (false). The token enables the payment method
to be used for recurring payments.

bankCode
The routing number is a unique nine-digit code that identifies the bank.

bankType
The bank type associated with the bank payment method.

comments
Additional details about the bank account.

email
The email address of the bank account holder.

mandate
Authorization from the account holder to debit their payment method.

nickName
The nick name of the account holder.

standardEntryClassCode
The three-letter code that identifies the type of electronic payment transaction being processed within the Automated Clearing
House (ACH) network.

##### **`accountHolderFirstName`**

The first name of the account holder for the bank payment method.

Signature

```
   public String accountHolderFirstName {get; set;}

```

Property Value

Type: String

##### **`accountHolderLastName`**

The last name of the account holder for the bank payment method.


Apex Reference Guide BankPaymentMethodRequest Class

Signature

```
   public String accountHolderLastName {get; set;}

```

Property Value

Type: String

##### **`accountHolderName`**

The name of the account holder for the bank payment method.

Signature

```
   public String accountHolderName {get; set;}

```

Property Value

Type: String

##### **`accountHolderType`**

The type of the account holder.

Signature

```
   public commercepayments.AccountHolderType accountHolderType {get; set;}

```

Property Value

Type: commercepayments.AccountHolderType on page 329

##### **`accountId`**

Salesforce Payments account ID associated with the bank payment method.

Signature

```
   public String accountId {get; set;}

```

Property Value

Type: String

##### **`accountNumber`**

The unique account number for the bank account.

Signature

```
   public String accountNumber {get; set;}

```


Apex Reference Guide BankPaymentMethodRequest Class

Property Value

Type: String

##### **`accountType`**

The type for the bank account.

Signature

```
   public commercepayments.AccountType accountType {get; set;}

```

Property Value

Type: commercepayments.AccountType on page 329

##### **`autoPay`**

Indicates whether a token for recurring payments is being requested (true) or not (false). The token enables the payment method to be
used for recurring payments.

Signature

```
   public Boolean autoPay {get; set;}

```

Property Value

Type: Boolean

##### **`bankCode`**

The routing number is a unique nine-digit code that identifies the bank.

Signature

```
   public String bankCode {get; set;}

```

Property Value

Type: String

##### **`bankType`**

The bank type associated with the bank payment method.

Signature

```
   public commercepayments.BankType bankType {get; set;}

```


Apex Reference Guide BankPaymentMethodRequest Class

Property Value

Type: commercepayments.BankType on page 366

##### **`comments`**

Additional details about the bank account.

Signature

```
   public String comments {get; set;}

```

Property Value

Type: String

##### **`email`**

The email address of the bank account holder.

Signature

```
   public String email {get; set;}

```

Property Value

Type: String

##### **`mandate`**

Authorization from the account holder to debit their payment method.

Signature

```
   public String mandate {get; set;}

```

Property Value

Type: String

##### **`nickName`**

The nick name of the account holder.

Signature

```
   public String nickName {get; set;}

```

Property Value

Type: String


Apex Reference Guide BankPaymentMethodRequest Class

##### **`standardEntryClassCode`**

The three-letter code that identifies the type of electronic payment transaction being processed within the Automated Clearing House
(ACH) network.

Signature

```
   public commercepayments.StandardEntryClassCode standardEntryClassCode {get; set;}

```

Property Value

Type: commercepayments.StandardEntryClassCode on page 520

#### BankPaymentMethodRequest Methods The following are methods for BankPaymentMethodRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type BankPaymentMethodRequest by determining the equality of external objects in a list.

This method is dynamic and based on the equals method in Java.

##### hashCode()
#### Maintains the integrity of lists of type BankPaymentMethodRequest .

toString()
Converts a date to a string.

##### **`equals(obj)`**

#### Maintains the integrity of lists of type BankPaymentMethodRequest by determining the equality of external objects in a list. This

method is dynamic and based on the equals method in Java.

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### **`hashCode()`**

#### Maintains the integrity of lists of type BankPaymentMethodRequest .


### Apex Reference Guide BankPaymentMethodResponse Class

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a date to a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### BankPaymentMethodResponse Class

This class contains information about the bank payment method response. The gateway adapter reads the gateway response and
### generates a BankPaymentMethodResponse, populating the required fields to create a bank payment method.

Namespace

CommercePayments on page 317

IN THIS SECTION:

#### BankPaymentMethodResponse Methods BankPaymentMethodResponse Methods

### The following are methods for BankPaymentMethodResponse .

IN THIS SECTION:

setAccountHolderType(accountHolderType)
Sets the account holder type for the bank payment method.

setAccountId(accountId)
Sets the Payments account ID associated with the bank payment method.

setAccountType(accountType)
Sets the account type for the bank payment method.

setBankCode(bankCode)
Sets the unique nine-digit code that identifies the bank code for the bank payment method.


Apex Reference Guide BankPaymentMethodResponse Class

setBankName(bankName)
Sets the bank name for the bank payment method.

setBankType(bankType)
Sets the bank type for the bank payment method.

setComments(comments)
Sets any additional details about the bank account.

setEmail(email)
Sets the email address of the bank account holder.

setGatewayToken(gatewayToken)
Sets the gateway token value that the gateway returned.

setGatewayTokenDetails(gatewayTokenDetails)
Sets any additional information that the gateway returned about the payment token.

setLast4(lastFour)
Sets the last four digits of the bank account number.

setName(name)
Sets the name of the account holder for the bank payment method.

setSavedPaymentMethodId(savedPaymentMethodId)
Sets the saved payment method ID for the bank account holder.

setStandardEntryClassCode(standardEntryClassCode)
Sets the code that identifies the type of electronic payment transaction being processed within the Automated Clearing House
(ACH) network.

##### **`setAccountHolderType(accountHolderType)`**

Sets the account holder type for the bank payment method.

Signature

```
   public void setAccountHolderType(commercepayments.AccountHolderType accountHolderType)

```

Parameters

```
   accountHolderType
```

Type: commercepayments.AccountHolderType on page 329

Return Value

Type: void

##### **`setAccountId(accountId)`**

Sets the Payments account ID associated with the bank payment method.

Signature

```
   public void setAccountId(String accountId)

```


Apex Reference Guide BankPaymentMethodResponse Class

Parameters

```
   accountId
```

Type: String

Return Value

Type: void

##### **`setAccountType(accountType)`**

Sets the account type for the bank payment method.

Signature

```
   public void setAccountType(commercepayments.AccountType accountType)

```

Parameters

```
   accountType
```

Type: commercepayments.AccountType on page 329

Return Value

Type: void

##### **`setBankCode(bankCode)`**

Sets the unique nine-digit code that identifies the bank code for the bank payment method.

Signature

```
   public void setBankCode(String bankCode)

```

Parameters

```
   bankCode
```

Type: String

Return Value

Type: void

##### **`setBankName(bankName)`**

Sets the bank name for the bank payment method.

Signature

```
   public void setBankName(String bankName)

```


Apex Reference Guide BankPaymentMethodResponse Class

Parameters

```
   bankName
```

Type: String

Return Value

Type: void

##### **`setBankType(bankType)`**

Sets the bank type for the bank payment method.

Signature

```
   public void setBankType(commercepayments.BankType bankType)

```

Parameters

```
   bankType
```

Type: commercepayments.BankType on page 366

Return Value

Type: void

##### **`setComments(comments)`**

Sets any additional details about the bank account.

Signature

```
   public void setComments(String comments)

```

Parameters

```
   comments
```

Type: String

Return Value

Type: void

##### **`setEmail(email)`**

Sets the email address of the bank account holder.

Signature

```
   public void setEmail(String email)

```


Apex Reference Guide BankPaymentMethodResponse Class

Parameters

```
   email
```

Type: String

Return Value

Type: void

##### **`setGatewayToken(gatewayToken)`**

Sets the gateway token value that the gateway returned.

Signature

```
   public void setGatewayToken(String gatewayToken)

```

Parameters

```
   gatewayToken
```

Type: String

Return Value

Type: void

##### **`setGatewayTokenDetails(gatewayTokenDetails)`**

Sets any additional information that the gateway returned about the payment token.

Signature

```
   public void setGatewayTokenDetails(String gatewayTokenDetails)

```

Parameters

```
   gatewayTokenDetails
```

Type: String

Return Value

Type: void

##### **`setLast4(lastFour)`**

Sets the last four digits of the bank account number.

Signature

```
   public void setLast4(String lastFour)

```


Apex Reference Guide BankPaymentMethodResponse Class

Parameters

```
   lastFour
```

Type: String

Return Value

Type: void

##### **`setName(name)`**

Sets the name of the account holder for the bank payment method.

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

##### **`setSavedPaymentMethodId(savedPaymentMethodId)`**

Sets the saved payment method ID for the bank account holder.

Signature

```
   public void setSavedPaymentMethodId(String savedPaymentMethodId)

```

Parameters

```
   savedPaymentMethodId
```

Type: String

Return Value

Type: void

##### **`setStandardEntryClassCode(standardEntryClassCode)`**

Sets the code that identifies the type of electronic payment transaction being processed within the Automated Clearing House (ACH)
network.


### Apex Reference Guide BaseApiPaymentMethodRequest Class

Signature

```
   public void setStandardEntryClassCode(commercepayments.StandardEntryClassCode

   standardEntryClassCode)

```

Parameters

```
   standardEntryClassCode
```

Type: commercepayments.StandardEntryClassCode on page 520

Return Value

Type: void

### BaseApiPaymentMethodRequest Class

Abstract class used to send information about a payment method to a gateway adapter during a service call.

Namespace

CommercePayments

Usage

### BaseApiPaymentMethodRequest is the base class for SaleApiPaymentMethodRequest and

`AuthApiPaymentMethodRequest` .

IN THIS SECTION:

#### BaseApiPaymentMethodRequest Constructors

BaseApiPaymentMethodRequest Properties

BaseApiPaymentMethodRequest Methods

#### BaseApiPaymentMethodRequest Constructors

### The following are constructors for BaseApiPaymentMethodRequest .

IN THIS SECTION:

##### BaseApiPaymentMethodRequest(address, id, saveForFuture)

Constructs a payment method. This constructor is intended for test usage and throws an exception if used outside of the Apex test
context.

##### BaseApiPaymentMethodRequest(address, id, saveForFuture)

Constructs a payment method. This constructor is intended for test usage and throws an exception if used outside of the Apex test
context.


Apex Reference Guide BaseApiPaymentMethodRequest Class

Signature

```
   global BaseApiPaymentMethodRequest(commercepayments.AddressRequest address, String id,

   Boolean saveForFuture)

```

Parameters

##### _`address`_

Type: commercepayments.AddressRequest on page 329

Sends data related on address request to a gateway adapter during a service call.

##### _`id`_

Type: String

```
   saveForFuture
```

Type: Boolean

Indicates whether Salesforce saves the payment method for future use.

#### BaseApiPaymentMethodRequest Properties The following are properties for BaseApiPaymentMethodRequest .

IN THIS SECTION:

##### address

The payment method’s address.

##### id

ID of the payment method request.

##### idType

ID of the payment method type.

saveForFuture
Indicates whether the payment method is saved as a record in Salesforce for future use.

##### address

The payment method’s address.

Signature

```
   global commercepayments.AddressRequest address {get; set;}

```

Property Value

Type: AddressRequest on page 329

##### id

ID of the payment method request.


Apex Reference Guide BaseApiPaymentMethodRequest Class

Signature

```
   global String id {get; set;}

```

Property Value

Type: String

##### **`idType`**

ID of the payment method type.

Signature

```
   public commercepayments.PaymentMethodIdType idType {get; set;}

```

Property Value

Type: commercepayments.PaymentMethodIdType

##### saveForFuture

Indicates whether the payment method is saved as a record in Salesforce for future use.

Signature

```
   global Boolean saveForFuture {get; set;}

```

Property Value

Type: Boolean

#### BaseApiPaymentMethodRequest Methods The following are methods for BaseApiPaymentMethodRequest .

IN THIS SECTION:

equals(obj)
#### Maintains the integrity of lists of type BaseApiPaymentMethodRequest by determining the equality of external objects in

a list. This method is dynamic and is based on the equals method in Java.

hashCode()
#### Maintains the integrity of lists of type BaseApiPaymentMethodRequest by determining the uniqueness of the external

object records in a list.

toString()
Converts a date to a string.


### Apex Reference Guide BaseNotification Class

##### equals(obj)

Maintains the integrity of lists of type `BaseApiPaymentMethodRequest` by determining the equality of external objects in a
list. This method is dynamic and is based on the equals method in Java.

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### hashCode()

Maintains the integrity of lists of type `BaseApiPaymentMethodRequest` by determining the uniqueness of the external object
records in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### toString()

Converts a date to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### BaseNotification Class

Abstract class for storing notification information sent from payment gateways.


Apex Reference Guide BaseNotification Class

Namespace

CommercePayments

Usage

#### An abstract class that contains the common fields from payment gateways. BaseNotification can’t be instantiated on its own.

The constructor of this class takes no arguments. For example:

```
   CommercePayments.BaseNotification bnt = new CommercePayments.BaseNotification();

```

Example

```
   commercepayments.BaseNotification notification = null;

        if ('CAPTURE'.equals(eventCode)) {

           notification = new commercepayments.CaptureNotification();

        } else if ('REFUND'.equals(eventCode)) {

           notification = new commercepayments.ReferencedRefundNotification();

        }

```

IN THIS SECTION:

#### BaseNotification Methods BaseNotification Methods The following are methods for BaseNotification .

IN THIS SECTION:

setAmount(amount)
Sets the transaction amount. Must be a non-negative value.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the notification occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the notification request. Maximum length of 255 characters.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets the payment gateway’s reference details.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the payment gateway’s reference number.

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. The code can be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.


Apex Reference Guide BaseNotification Class

setId(id)
Sets the ID of the notification sent by the gateway.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the information about the Salesforce-specific result code used to match a result code from a payment gateway.

setStatus(status)
Sets the status of the notification sent by the gateway.

##### setAmount(amount)

Sets the transaction amount. Must be a non-negative value.

Signature

```
   global void setAmount(Double amount)

```

Parameters

```
   amount
```

Type: Double

The amount of the transaction.

Return Value

Type: void

##### **`setGatewayAvsCode(gatewayAvsCode)`**

Sets the AVS (address verification system) result code that the gateway returned. Maximum length of 64 characters.

Signature

```
   public void setGatewayAvsCode(String gatewayAvsCode)

```

Parameters

```
   gatewayAvsCode
```

Type: String

Used to verify the address mapped to a payment method when the payments platform requests tokenization from the payment
gateway.

Return Value

Type: void

##### setGatewayDate(gatewayDate)

Sets the date that the notification occurred. Some gateways don’t send this value.


Apex Reference Guide BaseNotification Class

Signature

```
   global void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

The date that the notification occurred.

Return Value

Type: void

##### setGatewayMessage(gatewayMessage)

Sets error messages that the gateway returned for the notification request. Maximum length of 255 characters.

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String

The message that the gateway returned with the notification request. Contains additional information about the notification.

Return Value

Type: void

##### setGatewayReferenceDetails(gatewayReferenceDetails)

Sets the payment gateway’s reference details.

Signature

```
   global void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String

Provides information about the gateway communication.

Return Value

Type: void


Apex Reference Guide BaseNotification Class

##### setGatewayReferenceNumber(gatewayReferenceNumber)

Sets the payment gateway’s reference number.

Signature

```
   global void setGatewayReferenceNumber(String gatewayReferenceNumber)

```

Parameters

```
   gatewayReferenceNumber
```

Type: String

Unique transaction ID created by the payment gateway.

Return Value

Type: void

##### setGatewayResultCode(gatewayResultCode)

Sets a gateway-specific result code. The code can be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

Signature

```
   global void setGatewayResultCode(String gatewayResultCode)

```

Parameters

```
   gatewayResultCode
```

Type: String

Gateway-specific result code. Must be used to map a Salesforce-specific result code.

Return Value

Type: void

##### setGatewayResultCodeDescription(gatewayResultCodeDescription)

Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

Signature

```
   global void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Provides additional information about the result code and why the gateway returned the code. Descriptions vary between different
gateways.


Apex Reference Guide BaseNotification Class

Return Value

Type: void

##### setId(id)

Sets the ID of the notification sent by the gateway.

Signature

```
   global void setId(String id)

```

Parameters

```
   id
```

Type: String

Return Value

Type: void

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Sets the information about the Salesforce-specific result code used to match a result code from a payment gateway.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: commercepayments.SalesforceResultCodeInfo on page 519

Payment gateways have many response codes for payment calls. Salesforce uses the result code information to map payment
gateway codes to a predefined set of standard Salesforce result codes.

Return Value

Type: void

##### setStatus(status)

Sets the status of the notification sent by the gateway.

Signature

```
   global void setStatus(commercepayments.NotificationStatus status)

```


### Apex Reference Guide BasePaymentMethodRequest Class

Parameters

```
   status
```

Type: commercepayments.NotificationStatus on page 432

Shows whether the payments platform successfully received the notification from the gateway.

Return Value

Type: void

### BasePaymentMethodRequest Class

Abstract class for storing information about payment methods.

Namespace

CommercePayments

Usage

### The BasePaymentMethodRequest class contains fields common to CardPaymentMethodRequest on page 404

.

IN THIS SECTION:

#### BasePaymentMethodRequest Methods BasePaymentMethodRequest Methods

### The following are methods for BasePaymentMethodRequest .

IN THIS SECTION:

##### equals(obj)
### Maintains the integrity of lists of type BasePaymentMethodRequest by determining the equality of external objects in a list.

This method is dynamic and based on the equals method in Java.

hashCode()
### Maintains the integrity of lists of type BasePaymentMethodRequest by determining the uniqueness of the external object

records in a list.

toString()
Converts a date to a string.

##### equals(obj)

### Maintains the integrity of lists of type BasePaymentMethodRequest by determining the equality of external objects in a list. This

method is dynamic and based on the equals method in Java.


### Apex Reference Guide BaseRequest Class

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### hashCode()

Maintains the integrity of lists of type `BasePaymentMethodRequest` by determining the uniqueness of the external object
records in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### toString()

Converts a date to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### BaseRequest Class BaseRequest is extended by all the request classes.

Namespace

CommercePayments

IN THIS SECTION:

BaseRequest Methods


### Apex Reference Guide CaptureNotification Class

#### BaseRequest Methods The following are methods for BaseRequest .

IN THIS SECTION:

##### BaseRequest(AdditionalData, IdempotencyKey)

Used for testing.

##### BaseRequest(AdditionalData, IdempotencyKey)

Used for testing.

Signature

```
   global Void BaseRequest(String AdditionalData, Map<String, String> IdempotencyKey)

```

Parameters

```
   AdditionalData
```

Type: String

Contains additional data that may be required for a payment request. The `additionalData` object consists of key-value pairs.
You can retrieve the `additionalData` object from the request object: `Map<String, String>`

```
    additionalData=request.additionalData

   IdempotencyKey
```

Type: Map<String, String>

Unique value that's generated by a client and sent to the server in the request. The server stores the value and uses the it to keep
track of the request status.

Return Value

Type: Void

### CaptureNotification Class

When a payment gateway sends a notification for a capture transaction, the payment gateway adapter creates the
### CaptureNotification object to store information about the notification.

Namespace

CommercePayments

Usage

### CaptureNotification is used in asynchronous payment gateway adapters.

Specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes no arguments.
For example:

```
   CommercePayments.CaptureNotification crn = new CommercePayments.CaptureNotification();

```


Apex Reference Guide CaptureNotification Class

Example

```
   commercepayments.BaseNotification notification = null;

        if ('CAPTURE'.equals(eventCode)) {

           notification = new commercepayments.CaptureNotification();

        } else if ('REFUND'.equals(eventCode)) {

           notification = new commercepayments.ReferencedRefundNotification();

        }

```

IN THIS SECTION:

#### CaptureNotification Methods CaptureNotification Methods The following are methods for CaptureNotification .

IN THIS SECTION:

setAmount(amount)
Sets the transaction amount. Must be a non-negative value.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the transaction occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the payment request. Maximum length of 255 characters.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets additional data that you can use for subsequent transactions. You can use any data that isn’t normalized in financial entities.
This field has a maximum length of 1000 characters and can store data as JSON or XML.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the unique gateway reference number for the transaction that the gateway returned. Maximum length of 255 characters.

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. The code can be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a gateway returned. Maximum length of 1000 characters.

setId(id)
Sets the ID of a notification sent by the payment gateway.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

setStatus(status)
Sets the notification status to the same value that was sent by the gateway.


Apex Reference Guide CaptureNotification Class

##### setAmount(amount)

Sets the transaction amount. Must be a non-negative value.

Signature

```
   global void setAmount(Double amount)

```

Parameters

```
   amount
```

Type: Double

The amount to be debited or captured.

Return Value

Type: void

##### **`setGatewayAvsCode(gatewayAvsCode)`**

Sets the AVS (address verification system) result code that the gateway returned. Maximum length of 64 characters.

Signature

```
   public void setGatewayAvsCode(String gatewayAvsCode)

```

Parameters

```
   gatewayAvsCode
```

Type: String

Used to verify the address mapped to a payment method when the payments platform requests tokenization from the payment
gateway.

Return Value

Type: void

##### setGatewayDate(gatewayDate)

Sets the date that the transaction occurred. Some gateways don’t send this value.

Signature

```
   global void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

Date and time of the gateway communication.


Apex Reference Guide CaptureNotification Class

Return Value

Type: void

##### setGatewayMessage(gatewayMessage)

Sets error messages that the gateway returned for the payment request. Maximum length of 255 characters.

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String

Information on error messages sent from the gateway.

Return Value

Type: void

##### setGatewayReferenceDetails(gatewayReferenceDetails)

Sets additional data that you can use for subsequent transactions. You can use any data that isn’t normalized in financial entities. This
field has a maximum length of 1000 characters and can store data as JSON or XML.

Signature

```
   global void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String

Return Value

Type: void

##### setGatewayReferenceNumber(gatewayReferenceNumber)

Sets the unique gateway reference number for the transaction that the gateway returned. Maximum length of 255 characters.

Signature

```
   global void setGatewayReferenceNumber(String gatewayReferenceNumber)

```


Apex Reference Guide CaptureNotification Class

Parameters

```
   gatewayReferenceNumber
```

Type: String

Unique transaction ID created by the payment gateway.

Return Value

Type: void

##### setGatewayResultCode(gatewayResultCode)

Sets a gateway-specific result code. The code can be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

Signature

```
   global void setGatewayResultCode(String gatewayResultCode)

```

Parameters

```
   gatewayResultCode
```

Type: String

Gateway-specific result code. Map this value to a Salesforce-specific result code.

Return Value

Type: void

##### setGatewayResultCodeDescription(gatewayResultCodeDescription)

Sets a description of the gateway-specific result code that a gateway returned. Maximum length of 1000 characters.

Signature

```
   global void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Description of the gateway’s result code. Use this field to learn more about why the gateway returned a certain result code.

Return Value

Type: void

##### setId(id)

Sets the ID of a notification sent by the payment gateway.


Apex Reference Guide CaptureNotification Class

Signature

```
   global void setId(String id)

```

Parameters

```
   id
```

Type: String

Return Value

Type: void

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce uses
the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: commercepayments.SalesforceResultCodeInfo on page 519

Description of the Salesforce result code value.

Return Value

Type: void

##### setStatus(status)

Sets the notification status to the same value that was sent by the gateway.

Signature

```
   global void setStatus(commercepayments.NotificationStatus status)

```

Parameters

```
   status
```

Type: NotificationStatus on page 432

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Return Value

Type: void


### Apex Reference Guide CaptureRequest Class CaptureRequest Class

Represents a capture request. This class extends the `BaseRequest` class and inherits all its methods.

Namespace

CommercePayments on page 317

Usage

### The CaptureRequest class’s buildCaptureRequest method creates a CaptureRequest object to store payment information,

such as value and currency, as JSON strings.

Example

Builds a CaptureRequest object for a multicurrency org.

```
      private String buildCaptureRequest(commercepayments.CaptureRequest captureRequest) {

        Boolean IS_MULTICURRENCY_ORG = UserInfo.isMultiCurrencyOrganization();

        QueryUtils qBuilderForAuth = new QueryUtils(PaymentAuthorization.SObjectType);

        // Add required fields

        qBuilderForAuth.getSelectClause().addField('GatewayRefNumber', false);

        if (IS_MULTICURRENCY_ORG) {

           // addField also takes a boolean to enable translation (uses label instead of

    actual value)

           qBuilderForAuth.getSelectClause().addField('CurrencyIsoCode', false);

        }

```

IN THIS SECTION:

#### CaptureRequest Constructors

CaptureRequest Properties

#### CaptureRequest Constructors

### The following are constructors for CaptureRequest .

IN THIS SECTION:

##### CaptureRequest(amount, authorizationId)

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

##### CaptureRequest(amount, authorizationId)

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Parameters

```
   amount
```

Type: Double


### Apex Reference Guide CaptureResponse Class

The amount to be debited or captured.

```
   authorizationId
```

Type: String

Represents a payment authorization record.

#### CaptureRequest Properties The following are properties for CaptureRequest .

IN THIS SECTION:

##### accountId

Account ID value. References an account record.

##### amount

Amount of currency that needs to be captured.

##### paymentAuthorizationId

ID value that references a PaymentAuthorization.

##### accountId

Account ID value. References an account record.

Property Value

Type: String

##### amount

Amount of currency that needs to be captured.

Property Value

Type: Double

##### paymentAuthorizationId

ID value that references a PaymentAuthorization.

Property Value

Type: String

### CaptureResponse Class

The payment gateway adapter sends this response for the capture request type. This class extends `AbstractResponse` and inherits
its methods.


Apex Reference Guide CaptureResponse Class

Namespace

CommercePayments on page 317

Usage

You must specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes
no arguments. For example:

```
   CommercePayments.Capture Response ctr = new CommercePayments.CaptureResponse();

```

IN THIS SECTION:

#### CaptureResponse Methods CaptureResponse Methods The following are methods for CaptureResponse .

IN THIS SECTION:

##### setAmount(amount)

Sets the transaction amount.

setAsync(async)
Indicates whether the payment gateway adapter used in the payment capture was asynchronous ( `True` ) or synchronous ( `False` ).

setGatewayAvsCode(gatewayAvsCode)
Sets the payment gateway’s AVS (address verification system) code.

setGatewayDate(gatewayDate)
Sets the payment gateway’s date.

setGatewayMessage(gatewayMessage)
Sets information or messages that the gateway returned.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets the payment gateway’s reference details.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the payment gateway’s reference number.

setGatewayResultCode(gatewayResultCode)
Sets the payment gateway’s result code.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets the payment gateway’s result code description.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets Salesforce result code information.

##### setAmount(amount)

Sets the transaction amount.


Apex Reference Guide CaptureResponse Class

Signature

```
   global void setAmount(Double amount)

```

Parameters

```
   amount
```

Type: Double

The amount to be debited or captured.

Return Value

Type: void

##### setAsync(async)

Indicates whether the payment gateway adapter used in the payment capture was asynchronous ( `True` ) or synchronous ( `False` ).

Signature

```
   global void setAsync(Boolean async)

```

Parameters

```
   async
```

Type: Boolean

Return Value

Type: void

##### setGatewayAvsCode(gatewayAvsCode)

Sets the payment gateway’s AVS (address verification system) code.

Signature

```
   global void setGatewayAvsCode(String gatewayAvsCode)

```

Parameters

```
   gatewayAvsCode
```

Type: String

Payment gateways that use an AVS system return this code.

Return Value

Type: void


Apex Reference Guide CaptureResponse Class

##### setGatewayDate(gatewayDate)

Sets the payment gateway’s date.

Signature

```
   global void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

The date that communication happened with the gateway.

Return Value

Type: void

##### setGatewayMessage(gatewayMessage)

Sets information or messages that the gateway returned.

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String

Information or error messages returned by the gateway.

Return Value

Type: void

##### setGatewayReferenceDetails(gatewayReferenceDetails)

Sets the payment gateway’s reference details.

Signature

```
   global void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String

Provides information about the gateway communication.


Apex Reference Guide CaptureResponse Class

Return Value

Type: void

##### setGatewayReferenceNumber(gatewayReferenceNumber)

Sets the payment gateway’s reference number.

Signature

```
   global void setGatewayReferenceNumber(String gatewayReferenceNumber)

```

Parameters

```
   gatewayReferenceNumber
```

Type: String

Unique transaction ID created by the payment gateway.

Return Value

Type: void

##### setGatewayResultCode(gatewayResultCode)

Sets the payment gateway’s result code.

Signature

```
   global void setGatewayResultCode(String gatewayResultCode)

```

Parameters

```
   gatewayResultCode
```

Type: String

The gateway result code. You must map this to a Salesforce result code.

Return Value

Type: void

##### setGatewayResultCodeDescription(gatewayResultCodeDescription)

Sets the payment gateway’s result code description.

Signature

```
   global void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```


### Apex Reference Guide CardCategory Enum

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Description of the GatewayResultCode. Provides additional context about the result code that the gateway returned.

Return Value

Type: void

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Sets Salesforce result code information.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

SalesforceResultCodeInfoType: commercepayments.SalesforceResultCodeInfo

Description of the Salesforce result code value.

Return Value

Type: void

### CardCategory Enum

Defines whether the payment method represents a credit card or a debit card.

Namespace

CommercePayments on page 317

Enum Values

The following are the values of the `commercepayments.CardCategory` enum.

**Value** **Description**

`CreditCard` Shows that the payment method is a credit card.

`DebitCard` Shows that the payment method is a debit card.


### Apex Reference Guide CardPaymentMethodRequest Class CardPaymentMethodRequest Class

Sends data related to a card payment method to a gateway adapter during a service call.

Namespace

CommercePayments on page 317

Usage

This class contains details about the card used as a payment method for authorization, sale, or tokenization transaction requests. The
gateway adapter reads the fields of this class object while constructing a transaction JSON request to send to the payment gateway.
The object of this class is available as the `cardPaymentMethod` field in the `SaleApiPaymentMethodRequest Class`,

`AuthApiPaymentMethodRequest Class`, and `PaymentMethodTokenizationRequest Class` .

Example: This code sample retrieves the `cardPaymentMethodRequest` object from the `paymentMethod` class.

```
      commercepayments.CardPaymentMethodRequest cardPaymentMethod =

      paymentMethod.cardPaymentMethod;

```

IN THIS SECTION:

#### CardPaymentMethodRequest Constructors

CardPaymentMethodRequest Properties

CardPaymentMethodRequest Methods

#### CardPaymentMethodRequest Constructors

### The following are constructors for CardPaymentMethodRequest .

IN THIS SECTION:

##### CardPaymentMethodRequest(cardCategory)

Sets the `cardCategory` value for the card payment method request.

##### CardPaymentMethodRequest(cardCategory)

Sets the `cardCategory` value for the card payment method request.

Signature

```
   global CardPaymentMethodRequest(commercepayments.CardCategory cardCategory)

```

Parameters

```
   cardCategory
```

Type: CardCategory on page 403

Defines whether the card payment method is a credit card or a debit card.


Apex Reference Guide CardPaymentMethodRequest Class

#### CardPaymentMethodRequest Properties The following are properties for CardPaymentMethodRequest .

IN THIS SECTION:

##### accountId

Customer account for this payment method.

autoPay
Indicates whether a token is being requested so that the payment method can be used for recurring payments.

cardCategory
Indicates whether a card payment method is for a credit card or debit card.

cardHolderFirstName
The first name of the cardholder for the card payment method.

cardHolderLastName
The last name of the cardholder for the card payment method.

cardHolderName
Full name of the cardholder on the card payment method.

cardNumber
System-defined unique ID for the card payment method.

cardType
Defines the credit card bank. Possible values are `AmericanExpress`, `DinersClub`, `JCB`, `Maestro`, `MasterCard`,
and `Visa` .

cvv
The card security code for the credit or debit card on a card payment method.

email
Email address of the cardholder for the credit or debit card on a card payment method.

expiryMonth
Expiration month for the credit or debit card on a card payment method.

expiryYear
Expiration year of the credit or debit card for the card payment method.

inputCardType
Input field for the card type. This field doesn’t store the card type directly, but instead populates CardBin, LastFour, and
DisplayCardNumber based on the value entered in `inputCardType` .

startMonth
The credit or debit card becomes valid on the first day of the `startMonth` in the `startYear`

startYear
Year during which the credit or debit card becomes valid.

##### accountId

Customer account for this payment method.


Apex Reference Guide CardPaymentMethodRequest Class

Signature

```
   global String accountId {get; set;}

```

Property Value

Type: String

##### autoPay

Indicates whether a token is being requested so that the payment method can be used for recurring payments.

Signature

```
   global Boolean autoPay {get; set;}

```

Property Value

Type: Boolean

##### cardCategory

Indicates whether a card payment method is for a credit card or debit card.

Signature

```
   global commercepayments.CardCategory cardCategory {get; set;}

```

Property Value

Type: CardCategory on page 403

##### cardHolderFirstName

The first name of the cardholder for the card payment method.

Signature

```
   global String cardHolderFirstName {get; set;}

```

Property Value

Type: String

##### cardHolderLastName

The last name of the cardholder for the card payment method.

Signature

```
   global String cardHolderLastName {get; set;}

```


Apex Reference Guide CardPaymentMethodRequest Class

Property Value

Type: String

##### cardHolderName

Full name of the cardholder on the card payment method.

Signature

```
   global String cardHolderName {get; set;}

```

Property Value

Type: String

##### cardNumber

System-defined unique ID for the card payment method.

Signature

```
   global String cardNumber {get; set;}

```

Property Value

Type: String

##### cardType

Defines the credit card bank. Possible values are `AmericanExpress`, `DinersClub`, `JCB`, `Maestro`, `MasterCard`, and `Visa` .

Signature

```
   global commercepayments.CardType cardType {get; set;}

```

Property Value

Type: CardType

##### cvv

The card security code for the credit or debit card on a card payment method.

Signature

```
   global String cvv {get; set;}

```

Property Value

Type: String


Apex Reference Guide CardPaymentMethodRequest Class

##### email

Email address of the cardholder for the credit or debit card on a card payment method.

Signature

```
   global String email {get; set;}

```

Property Value

Type: String

##### expiryMonth

Expiration month for the credit or debit card on a card payment method.

Signature

```
   global Integer expiryMonth {get; set;}

```

Property Value

Type: Integer

##### expiryYear

Expiration year of the credit or debit card for the card payment method.

Signature

```
   global Integer expiryYear {get; set;}

```

Property Value

Type: Integer

##### inputCardType

Input field for the card type. This field doesn’t store the card type directly, but instead populates CardBin, LastFour, and DisplayCardNumber
##### based on the value entered in inputCardType .

Signature

```
   global String inputCardType {get; set;}

```

Property Value

Type: String


Apex Reference Guide CardPaymentMethodRequest Class

##### startMonth The credit or debit card becomes valid on the first day of the startMonth in the startYear

Signature

```
   global Integer startMonth {get; set;}

```

Property Value

Type: Integer

##### startYear

Year during which the credit or debit card becomes valid.

Signature

```
   global Integer startYear {get; set;}

```

Property Value

Type: Integer

#### CardPaymentMethodRequest Methods The following are methods for CardPaymentMethodRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type CardPaymentMethodRequest by determining the equality of external objects in a list.

This method is dynamic and based on the equals method in Java.

hashCode()
#### Maintains the integrity of lists of type CardPaymentMethodRequest .

toString()
Converts a date to a string.

##### equals(obj)

#### Maintains the integrity of lists of type CardPaymentMethodRequest by determining the equality of external objects in a list. This

method is dynamic and based on the equals method in Java.

Signature

```
   global Boolean equals(Object obj)

```


### Apex Reference Guide CardPaymentMethodResponse Class

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### hashCode()

Maintains the integrity of lists of type `CardPaymentMethodRequest` .

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### toString()

Converts a date to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### CardPaymentMethodResponse Class

This class contains details about the card payment method.

Namespace

CommercePayments

IN THIS SECTION:

#### CardPaymentMethodResponse Methods CardPaymentMethodResponse Methods

### The following are methods for CardPaymentMethodResponse .


Apex Reference Guide CardPaymentMethodResponse Class

IN THIS SECTION:

##### setAccountId(accountId)

Sets the Salesforce payments account to which this payment method is linked.

setAutoPay(autoPay)
Sets whether a token for recurring payments is being requested or not.

setCardBin(cardBin)
Sets the card Bank Identification Number (BIN).

setCardCategory(cardCategory)
Sets the card category.

setCardHolderFirstName(cardHolderFirstName)
Sets the first name of the card holder.

setCardHolderLastName(cardHolderLastName)
Sets the last name of the card holder.

setCardHolderName(cardHolderName)
Sets the name of the card holder.

setCardLastFour(cardLastFour)
Sets the last four digits of the card.

setCardType(cardType)
Specifies the type of the credit card issuer.

setCardTypeCategory(cardTypeCategory)
Sets the credit card issuer.

setComments(comments)
Sets the notes added by a user for card payment.

setDisplayCardNumber(displayCardNumber)
Sets the display card number.

setEmail(email)
Sets the email address of the card holder.

setExpiryMonth(expiryMonth)
Sets the month of expiry of the card.

setExpiryYear(expiryYear)
Sets the year of expiry of the card.

setNickName(nickName)
Sets the nickname of the card.

setStartMonth(startMonth)
Sets the month the card becomes active.

setStartYear(startYear)
Sets the year the card becomes active.

##### **`setAccountId(accountId)`**

Sets the Salesforce payments account to which this payment method is linked.


Apex Reference Guide CardPaymentMethodResponse Class

Signature

```
   public void setAccountId(Id accountId)

```

Parameters

```
   accountId
```

Type: Id

Salesforce Payments account to which this payment method is linked.

Return Value

Type: void

##### **`setAutoPay(autoPay)`**

Sets whether a token for recurring payments is being requested or not.

Signature

```
   public void setAutoPay(Boolean autoPay)

```

Parameters

```
   autoPay
```

Type: Boolean

Indicates whether a token for recurring payments is being requested ( `true` ) or not ( `false` ). The token lets the payment method
be used for recurring payments.

Return Value

Type: void

##### **`setCardBin(cardBin)`**

Sets the card Bank Identification Number (BIN).

Signature

```
   public void setCardBin(String cardBin)

```

Parameters

```
   cardBin
```

Type: String

Bank Identification Number (BIN). The BIN is the first 4-6 numbers on a payment card that identifies the card issuer.

Return Value

Type: void


Apex Reference Guide CardPaymentMethodResponse Class

##### **`setCardCategory(cardCategory)`**

Sets the card category.

Signature

```
   public void setCardCategory(commercepayments.CardCategory cardCategory)

```

Parameters

```
   cardCategory
```

Type: CommercePayments.CardCategory

Specifies whether it is a credit card or debit card.

Return Value

Type: void

##### **`setCardHolderFirstName(cardHolderFirstName)`**

Sets the first name of the card holder.

Signature

```
   public void setCardHolderFirstName(String cardHolderFirstName)

```

Parameters

```
   cardHolderFirstName
```

Type: String

First name of the card holder.

Return Value

Type: void

##### **`setCardHolderLastName(cardHolderLastName)`**

Sets the last name of the card holder.

Signature

```
   public void setCardHolderLastName(String cardHolderLastName)

```

Parameters

```
   cardHolderLastName
```

Type: String

Last name of the card holder.


Apex Reference Guide CardPaymentMethodResponse Class

Return Value

Type: void

##### **`setCardHolderName(cardHolderName)`**

Sets the name of the card holder.

Signature

```
   public void setCardHolderName(String cardHolderName)

```

Parameters

```
   cardHolderName
```

Type: String

Card holder name.

Return Value

Type: void

##### **`setCardLastFour(cardLastFour)`**

Sets the last four digits of the card.

Signature

```
   public void setCardLastFour(String cardLastFour)

```

Parameters

```
   cardLastFour
```

Type: String

Last four digits of the card.

Return Value

Type: void

##### **`setCardType(cardType)`**

Specifies the type of the credit card issuer.

Signature

```
   public void setCardType(String cardType)

```


Apex Reference Guide CardPaymentMethodResponse Class

Parameters

```
   cardType
```

Type: String

Type of the credit card issuer.

Return Value

Type: void

##### **`setCardTypeCategory(cardTypeCategory)`**

Sets the credit card issuer.

Signature

```
   public void setCardTypeCategory(commercepayments.CardType cardTypeCategory)

```

Parameters

```
   cardTypeCategory
```

Type: CommercePayments.CardType

Credit card issuer.

Return Value

Type: void

##### **`setComments(comments)`**

Sets the notes added by a user for card payment.

Signature

```
   public void setComments(String comments)

```

Parameters

```
   comments
```

Type: String

Details about a record added by a user, maximum is 1000 characters.

Return Value

Type: void

##### **`setDisplayCardNumber(displayCardNumber)`**

Sets the display card number.


Apex Reference Guide CardPaymentMethodResponse Class

Signature

```
   public void setDisplayCardNumber(String displayCardNumber)

```

Parameters

```
   displayCardNumber
```

Type: String

Displayed card number.

Return Value

Type: void

##### **`setEmail(email)`**

Sets the email address of the card holder.

Signature

```
   public void setEmail(String email)

```

Parameters

```
   email
```

Type: String

Email address of the card holder.

Return Value

Type: void

##### **`setExpiryMonth(expiryMonth)`**

Sets the month of expiry of the card.

Signature

```
   public void setExpiryMonth(Integer expiryMonth)

```

Parameters

```
   expiryMonth
```

Type: Integer

Month of expiry of the card.

Return Value

Type: void


Apex Reference Guide CardPaymentMethodResponse Class

##### **`setExpiryYear(expiryYear)`**

Sets the year of expiry of the card.

Signature

```
   public void setExpiryYear(Integer expiryYear)

```

Parameters

```
   expiryYear
```

Type: Integer

Year of expiry of the card.

Return Value

Type: void

##### **`setNickName(nickName)`**

Sets the nickname of the card.

Signature

```
   public void setNickName(String nickName)

```

Parameters

```
   nickName
```

Type: String

Card nickname.

Return Value

Type: void

##### **`setStartMonth(startMonth)`**

Sets the month the card becomes active.

Signature

```
   public void setStartMonth(Integer startMonth)

```

Parameters

```
   startMonth
```

Type: Integer

Determines from which month the card becomes active.


### Apex Reference Guide CardType Enum

Return Value

Type: void

##### **`setStartYear(startYear)`**

Sets the year the card becomes active.

Signature

```
   public void setStartYear(Integer startYear)

```

Parameters

```
   startYear
```

Type: Integer

Determines from which year the card becomes active.

Return Value

Type: void

### CardType Enum

Specifies the credit card issuer.

Enum Values

The following are the values of the `commercepayments.CardType` enum.

**Value** **Description**

`AmericanExpress` American Express card

`DinersClub` Diners Club card

`Jcb` Japan Credit Bureau (JCB) card

`Maestro` Maestro card

`MasterCard` Master card

`Visa` Visa card

### CustomMetadataTypeInfo Class Access information about custom metadata. The PaymentGatewayAdapter can send CustomMetadataTypeInfo to

transaction requests through the response object’s `SalesforceResultCodeInfo` .


### Apex Reference Guide EnhancedPaymentDataInput Class

Namespace

CommercePayments on page 317

IN THIS SECTION:

#### CustomMetadataTypeInfo Constructors CustomMetadataTypeInfo Methods CustomMetadataTypeInfo Constructors The following are constructors for CustomMetadataTypeInfo .

IN THIS SECTION:

##### CustomMetadataTypeInfo(cmtRecordId, cmtSfResultCodeFieldName)

Constructor for providing custom metadata type information.

##### CustomMetadataTypeInfo(cmtRecordId, cmtSfResultCodeFieldName)

Constructor for providing custom metadata type information.

Signature

```
   global CustomMetadataTypeInfo(String cmtRecordId, String cmtSfResultCodeFieldName)

```

Parameters

```
   cmtRecordId
```

Type: String

ID of the matchedcustom metadata type record

```
   cmtSfResultCodeFieldName
```

Type: String

Field that contains the Salesforce result code values. Belongs to the custom metadata type.

#### CustomMetadataTypeInfo Methods The following are methods for CustomMetadataTypeInfo .

### EnhancedPaymentDataInput Class

Sends enhanced payment data, including Level 2 and Level 3 fields, to the gateway adapter as part of the service call.

Namespace

CommercePayments on page 317


Apex Reference Guide EnhancedPaymentDataInput Class

Usage

Supported only for third-party payment gateways; not supported for native payments.

IN THIS SECTION:

#### EnhancedPaymentDataInput Properties

EnhancedPaymentDataInput Methods

#### EnhancedPaymentDataInput Properties The following are properties for EnhancedPaymentDataInput .

IN THIS SECTION:

additionalAttributes
Map of gateway-specific or custom fields.

discountAmount
Discount amount.

dutyAmount
The total amount charged as duty or import or export tariffs on the transaction.

invoiceNumber
Invoice number associated with the payment.

lineItems
Collection of individual line items associated with the payment.

referenceId
Customer reference or identifier.

salesTaxAmount
Sales tax amount.

shipFromZip
Origin postal code.

shipToCountry
Destination country code.

shipToZip
Destination postal code.

shippingAmount
Shipping or freight amount.

taxRate
Percentage rate of tax applied to the transaction or line item.

totalTaxAmount
Total tax amount for the transaction.


Apex Reference Guide EnhancedPaymentDataInput Class

##### **`additionalAttributes`**

Map of gateway-specific or custom fields.

Signature

```
   public Map<String,String> additionalAttributes {get; set;}

```

Property Value

Type: Map<String,String>

##### **`discountAmount`**

Discount amount.

Signature

```
   public Double discountAmount {get; set;}

```

Property Value

Type: Double

##### **`dutyAmount`**

The total amount charged as duty or import or export tariffs on the transaction.

Signature

```
   public Double dutyAmount {get; set;}

```

Property Value

Type: Double

##### **`invoiceNumber`**

Invoice number associated with the payment.

Signature

```
   public String invoiceNumber {get; set;}

```

Property Value

Type: String

##### **`lineItems`**

Collection of individual line items associated with the payment.


Apex Reference Guide EnhancedPaymentDataInput Class

Signature

```
   public List<commercepayments.LineItemInput> lineItems {get; set;}

```

Property Value

Type: List<commercepayments.LineItemInput on page 443>

##### **`referenceId`**

Customer reference or identifier.

Signature

```
   public String referenceId {get; set;}

```

Property Value

Type: String

##### **`salesTaxAmount`**

Sales tax amount.

Signature

```
   public Double salesTaxAmount {get; set;}

```

Property Value

Type: Double

##### **`shipFromZip`**

Origin postal code.

Signature

```
   public String shipFromZip {get; set;}

```

Property Value

Type: String

##### **`shipToCountry`**

Destination country code.

Signature

```
   public String shipToCountry {get; set;}

```


Apex Reference Guide EnhancedPaymentDataInput Class

Property Value

Type: String

##### **`shipToZip`**

Destination postal code.

Signature

```
   public String shipToZip {get; set;}

```

Property Value

Type: String

##### **`shippingAmount`**

Shipping or freight amount.

Signature

```
   public Double shippingAmount {get; set;}

```

Property Value

Type: Double

##### **`taxRate`**

Percentage rate of tax applied to the transaction or line item.

Signature

```
   public Double taxRate {get; set;}

```

Property Value

Type: Double

##### **`totalTaxAmount`**

Total tax amount for the transaction.

Signature

```
   public Double totalTaxAmount {get; set;}

```

Property Value

Type: Double


Apex Reference Guide EnhancedPaymentDataInput Class

#### EnhancedPaymentDataInput Methods The following are methods for EnhancedPaymentDataInput .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type EnhancedPaymentDataInput by determining the equality of external objects in a list.

This method is dynamic and based on the equals method in Java.

##### hashCode()
#### Maintains the integrity of lists of type EnhancedPaymentDataInput .

##### toString()

Converts a date to a string.

##### **`equals(obj)`**

#### Maintains the integrity of lists of type EnhancedPaymentDataInput by determining the equality of external objects in a list. This

method is dynamic and based on the equals method in Java.

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### **`hashCode()`**

#### Maintains the integrity of lists of type EnhancedPaymentDataInput .

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a date to a string.


### Apex Reference Guide GatewayErrorResponse Class

Signature

```
   public String toString()

```

Return Value

Type: String

### GatewayErrorResponse Class

Use to respond with an error indication following errors from the `PaymentGateway` adapter, such as request-forbidden responses,
custom validation errors, or expired API tokens.

Namespace

CommercePayments on page 317

Usage

### Use GatewayErrorResponse to create an object that stores information about error responses sent by the payment gateway

adapter.

Example

### If GatewayResponse receives an exception rather than a valid request, it calls GatewayErrorResponse to create an error

object with information about the exception.

```
   global commercepayments.GatewayResponse processRequest(commercepayments.paymentGatewayContext

    gatewayContext) {

        commercepayments.RequestType requestType = gatewayContext.getPaymentRequestType();

        commercepayments.GatewayResponse response;

        try {

           if (requestType == commercepayments.RequestType.Authorize) {

             response =

   createAuthResponse((commercepayments.AuthorizationRequest)gatewayContext.getPaymentRequest());

           } else if (requestType == commercepayments.RequestType.Capture) {

             response =

   createCaptureResponse((commercepayments.CaptureRequest)gatewayContext.getPaymentRequest())

    ;

           } else if (requestType == commercepayments.RequestType.ReferencedRefund) {

             response =

   createRefundResponse((commercepayments.ReferencedRefundRequest)gatewayContext.getPaymentRequest());

           }

           return response;

        } catch(SalesforceValidationException e) {

           commercepayments.GatewayErrorResponse error = new

   commercepayments.GatewayErrorResponse('400', e.getMessage());

           return error;

```


### Apex Reference Guide GatewayNotificationResponse Class

```
        }

      }

```

IN THIS SECTION:

#### GatewayErrorResponse Constructors GatewayErrorResponse Constructors The following are constructors for GatewayErrorResponse .

IN THIS SECTION:

##### GatewayErrorResponse(errorCode, errorMessage)

Constructor to create a GatewayErrorResponse object that accepts `errorCode` and `errorMessage` .

##### GatewayErrorResponse(errorCode, errorMessage)

Constructor to create a GatewayErrorResponse object that accepts `errorCode` and `errorMessage` .

Signature

```
   global GatewayErrorResponse(String errorCode, String errorMessage)

```

Parameters

```
   errorCode
```

Type: String

Should match with the HTTP status code to be returned to the user. Here are a few examples.

**•** If the status code is for a bad request, the errorCode should be 400.

**•** If the status code is for a forbidden request, errorCode should be 403.

**•** If errorCode isn’t a valid HTTP status code, a 500 internal server error is returned.

Note: _`errorCode`_ must have a value, otherwise the platform throws an error.

```
   errorMessage
```

Type: String

The message response to users following an error.

Note: _`errorMessage`_ must have a value, otherwise the platform throws an error.

### GatewayNotificationResponse Class

When the payment gateway sends a notification to the payments platform, the platform responds with a
### GatewayNotificationResponse indicating whether the platform succeeded or failed at receiving the notification.


Apex Reference Guide GatewayNotificationResponse Class

Namespace

CommercePayments on page 317

Usage

You must specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes
no arguments. For example:

```
   CommercePayments.GatewayNotificationResponse gnr = new

   CommercePayments.GatewayNotificationResponse();

```

When an asynchronous payment gateway sends a notification, the gateway requires the platform to acknowledge that it has either
succeeded or failed in receiving the notification. Payment gateway adapters use this class to construct the acknowledgment response,
#### which gateways expect for a notification. GatewayNotificationResponse is the return type of the processNotification

method.

Example

```
   commercepayments.GatewayNotificationResponse gnr = new

   commercepayments.GatewayNotificationResponse();

   if (saveResult.isSuccess()) {

      system.debug('Notification accepted by platform');

   } else {

      system.debug('Errors in the result '+ Blob.valueOf(saveResult.getErrorMessage()));

   }

   gnr.setStatusCode(200);

   gnr.setResponseBody(Blob.valueOf('[accepted]'));

   return gnr;

```

IN THIS SECTION:

#### GatewayNotificationResponse Methods GatewayNotificationResponse Methods The following are methods for GatewayNotificationResponse .

IN THIS SECTION:

##### setResponseBody(responseBody)

Sets the body of the response to the gateway. Some gateways expect the payments platform to acknowledge the notification with
a response regardless of whether the notification was accepted.

setStatusCode(statusCode)
Sets the HTTP status code sent to the gateway as part of the payments platform’s response notification.

##### setResponseBody(responseBody)

Sets the body of the response to the gateway. Some gateways expect the payments platform to acknowledge the notification with a
response regardless of whether the notification was accepted.


Apex Reference Guide GatewayNotificationResponse Class

Signature

```
   global void setResponseBody(Blob responseBody)

```

Parameters

```
   responseBody
```

Type: Blob

Common response values include `accepted` for successfully receiving the response. For example:

```
     commercepayments.GatewayNotificationResponse gnr = new

     commercepayments.GatewayNotificationResponse();

     if (saveResult.isSuccess()) {

       system.debug('Notification accepted by platform');

     } else {

       system.debug('Errors in the result '+ Blob.valueOf(saveResult.getErrorMessage()));

     }

     gnr.setStatusCode(200);

     gnr.setResponseBody(Blob.valueOf('[accepted]'));

     return gnr;

```

Return Value

Type: void

##### setStatusCode(statusCode)

Sets the HTTP status code sent to the gateway as part of the payments platform’s response notification.

Signature

```
   global void setStatusCode(Integer statusCode)

```

Parameters

```
   statusCode
```

Type: Integer

The status code will vary based on the type of payments platform response. Users should configure their
`GatewayNotificationResponse` class to account for all values that their payments platform can possibly return. For
example:

```
     commercepayments.GatewayNotificationResponse gnr = new

     commercepayments.GatewayNotificationResponse();

     if (saveResult.isSuccess()) {

       system.debug('Notification accepted by platform');

     } else {

       system.debug('Errors in the result '+ Blob.valueOf(saveResult.getErrorMessage()));

     }

     gnr.setStatusCode(200);

     gnr.setResponseBody(Blob.valueOf('[accepted]'));

     return gnr;

```


### Apex Reference Guide GatewayResponse Interface

Return Value

Type: void

### GatewayResponse Interface

Generic payment gateway response interface. This class extends the `CaptureResponse` on page 398,
`AbstractTransactionResponse` on page 324, and `AbstractResponse` on page 320 classes and inherits all their properties.
It has no unique methods or parameters.

Namespace

CommercePayments on page 317

IN THIS SECTION:

#### GatewayResponse Example Implementation GatewayResponse Example Implementation

This is an example implementation of the `commercepayments.GatewayResponse` interface.

```
   /**

      * Abstract function to build gateway response for a Transaction

      * The input is the response from gateway

      * It creates and returns GatewayResponse from the HttpResponse

      */

     public abstract commercepayments.GatewayResponse buildResponse(HttpResponse response);

      /**

      * Function to process transaction requests

      * Steps involved are:

      * 1. Build HttpRequest with the input Request from gateway context

      * 2. Send request and get the response from gateway

      * 3. Parse the response from gateway and return GatewayResponse

      */

      public commercepayments.GatewayResponse execute(){

             HttpRequest req;

        try{

           //Building a new request

           req = buildRequest();

        } catch(PayeezeValidationException e) {

           return getValidationExceptionError(e);

        }

        commercepayments.PaymentsHttp http = new commercepayments.PaymentsHttp();

        HttpResponse res = null;

        try{

           //Sending the request

           res = http.send(req);

        } catch(CalloutException ce) {

           return getCalloutExceptionError(ce);

        }

```


### Apex Reference Guide NotificationClient Class

```
        try{

           //Parsing the response from gateway

           return buildResponse(res);

        } catch(Exception e) {

           return getParseExceptionError(e);

        }

      }

```

[For additional context, review the complete Sample Gateway Adapter in the CommercePayments Gateway Reference Implementation.](https://github.com/forcedotcom/Core-Payments-Reference-Gateway-Integration-Adapters/blob/master/PayeezyGatewayAdapter/classes/AbstractTransactionService.apex)

### NotificationClient Class

Communicates with the payment platform regarding the gateway’s notification.

Namespace

CommercePayments on page 317

Usage

Specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes no arguments.
For example:

```
   CommercePayments.NotificationClient ntc = new CommercePayments.NotificationClient();

```

This class is used in asynchronous payment gateway adapters. The notification client contains API for communicating with the payments
platform regarding the gateway’s notification. When the gateway sends a notification, the gateway adapter invokes the `record`
### method in NotificationClient to request that the platform updates notification details.

Example

The `NotificationSaveResult` class creates a saveResult object to store the result of the save request made to the payment
gateway.

```
   commercepayments.NotificationSaveResult saveResult =

   commercepayments.NotificationClient.record(notification);

```

IN THIS SECTION:

#### NotificationClient Methods NotificationClient Methods

### The following are methods for NotificationClient .

IN THIS SECTION:

record(notification)
Stores the results of a notification request.


### Apex Reference Guide NotificationSaveResult Class

##### record(notification)

Stores the results of a notification request.

Signature

```
   global static commercepayments.NotificationSaveResult

   record(commercepayments.BaseNotification notification)

```

Parameters

```
   notification
```

Type: BaseNotification on page 383

Return Value

Type: NotificationSaveResult on page 431

### NotificationSaveResult Class

Contains the result of the payment platform’s attempt to record data from the gateway’s notification.

Namespace

CommercePayments on page 317

Usage

This class is used with asynchronous payments. It is the return type of the `NotificiationClient.record` operation and
contains the result of the payment platform’s attempt to save notification details.

The constructor of this class takes no arguments. For example:

```
   CommercePayments.NotificationSaveResult nsr = new

   CommercePayments.NotificationSaveResult();

```

Example

```
   commercepayments.NotificationSaveResult saveResult =

   commercepayments.NotificationClient.record(notification);

```

IN THIS SECTION:

#### NotificationSaveResult Methods NotificationSaveResult Methods

### The following are methods for NotificationSaveResult .


### Apex Reference Guide NotificationStatus Enum

IN THIS SECTION:

##### getErrorMessage()

Gets the error message, if any, from the payment platform regarding its attempt to save the notification sent from the payment
gateway.

##### getStatusCode()

Gets the status code from the payment platform’s attempt to save the notification sent from the payment gateway.

##### isSuccess()

Gets the status of whether the payment platform successfully saved the notification sent from the payment gateway.

##### getErrorMessage()

Gets the error message, if any, from the payment platform regarding its attempt to save the notification sent from the payment gateway.

Signature

```
   global String getErrorMessage()

```

Return Value

Type: String

##### getStatusCode()

Gets the status code from the payment platform’s attempt to save the notification sent from the payment gateway.

Signature

```
   global Integer getStatusCode()

```

Return Value

Type: Integer

##### isSuccess()

Gets the status of whether the payment platform successfully saved the notification sent from the payment gateway.

Signature

```
   global Boolean isSuccess()

```

Return Value

Type: Boolean

### NotificationStatus Enum

Shows whether the payments platform successfully received the notification from the gateway.


### Apex Reference Guide PaymentGatewayAdapter Interface

Usage

When the gateway sends a notification for a payment request, the payments platform delegates the notification request to the gateway
adapter. First, the adapter evaluates the signature from the notification request. If the signature is valid, the adapter builds a notification
object to store information about the notification. During this process, the adapter sets the `NotificationStatus` to `Failed`
or `Success` based on information from the notification request.

Enum Values

The following are the values of the `commercepayments.NotificationStatus` enum.

**Value** **Description**

`Failed` The payments platform couldn’t receive the notification due to an error.

`Success` The payments platform received the notification.

### PaymentGatewayAdapter Interface

`PaymentGatewayAdapters` can implement this interface in order to process requests.

Namespace

CommercePayments on page 317

IN THIS SECTION:

#### PaymentGatewayAdapter Methods PaymentGatewayAdapter Methods

### The following are methods for PaymentGatewayAdapter .

IN THIS SECTION:

##### processRequest(var1)

The entry point for processing payment requests. Returns the response from the payment gateway.

##### **`processRequest(var1)`**

The entry point for processing payment requests. Returns the response from the payment gateway.

Signature

```
   global commercepayments.GatewayResponse

   processRequest(commercepayments.PaymentGatewayContext var1)

```


### Apex Reference Guide PaymentGatewayAsyncAdapter Interface

Parameters

```
   var1
```

[Type: commercepayments.PaymentGatewayContext](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_PaymentGatewayContext.htm#apex_class_commerce_payments_PaymentGatewayContext)

You can retrieve the request type and the request from the Context object.

Return Value

Type: commercepayments.GatewayResponse

The response from the payment gateway.

### PaymentGatewayAsyncAdapter Interface

Implement the interface to allow customers to process payments asynchronously.

Namespace

CommercePayments on page 317

Usage

Implementing an asynchronous adapter also requires the `processNotification` method from the GatewayNotificationResponse
on page 426 class.

Example

```
   global with sharing class SampleAsyncAdapter

        implements commercepayments.PaymentGatewayAsyncAdapter,

        commercepayments.PaymentGatewayAdapter {

        global SampleAsyncAdapter() {

        }

        global commercepayments.GatewayResponse processRequest(

        commercepayments.paymentGatewayContext gatewayContext) {

        }

        global commercepayments.GatewayNotificationResponse processNotification(

        commercepayments.PaymentGatewayNotificationContext gatewayNotificationContext) {

        }

        }

```

IN THIS SECTION:

PaymentGatewayAsyncAdapter Methods

PaymentGatewayAsyncAdapter Example Implementation


Apex Reference Guide PaymentGatewayAsyncAdapter Interface

#### PaymentGatewayAsyncAdapter Methods The following are methods for PaymentGatewayAsyncAdapter .

IN THIS SECTION:

##### processNotification(paymentGatewayNotificationContext)

Entry point for processing notifications from payment gateways.

##### processNotification(paymentGatewayNotificationContext)

Entry point for processing notifications from payment gateways.

Signature

```
   global commercepayments.GatewayNotificationResponse

   processNotification(commercepayments.PaymentGatewayNotificationContext var1)

```

Parameters

```
   paymentGatewayNotificationContext
```

Type: PaymentGatewayNotificationContext on page 439

The `PaymentGatewayNotificationContext` object wraps all the information related to a gateway notification.

Return Value

Type: GatewayNotificationResponse on page 426

When the payment gateway sends a notification to the payments platform, the platform responds with a
`GatewayNotificationResponse` indicating whether the platform succeeded or failed at receiving the notification.

#### PaymentGatewayAsyncAdapter Example Implementation

This is a sample implementation of the `commercepayments.PaymentGatewayAsyncAdapter` interface.

```
   global with sharing class AdyenAdapter implements

   commercepayments.PaymentGatewayAsyncAdapter, commercepayments.PaymentGatewayAdapter {

      global AdyenAdapter() {}

      global commercepayments.GatewayResponse

   processRequest(commercepayments.paymentGatewayContext gatewayContext) {

      }

      global commercepayments.GatewayNotificationResponse

   processNotification(commercepayments.PaymentGatewayNotificationContext

   gatewayNotificationContext) {

      }

   }

   commercepayments.RequestType requestType = gatewayContext.getPaymentRequestType();

   if (requestType == commercepayments.RequestType.Capture) {

      req.setEndpoint('/pal/servlet/Payment/v52/capture');

```


Apex Reference Guide PaymentGatewayAsyncAdapter Interface

```
      body =

   buildCaptureRequest((commercepayments.CaptureRequest)gatewayContext.getPaymentRequest());

   } else if (requestType == commercepayments.RequestType.ReferencedRefund) {

      req.setEndpoint('/pal/servlet/Payment/v52/refund');

      body =

   buildRefundRequest((commercepayments.ReferencedRefundRequest)gatewayContext.getPaymentRequest());

   }

   req.setBody(body);

   req.setMethod('POST');

   commercepayments.PaymentsHttp http = new commercepayments.PaymentsHttp();

   HttpResponse res = null;

   try {

      res = http.send(req);

   } catch(CalloutException ce) {

      commercepayments.GatewayErrorResponse error = new

   commercepayments.GatewayErrorResponse('500', ce.getMessage());

      return error;

   }

   if ( requestType == commercepayments.RequestType.Capture) {

      response = createCaptureResponse(res);

   } else if ( requestType == commercepayments.RequestType.ReferencedRefund) {

      response = createRefundResponse(res);

   }

   return response;

   commercepayments.PaymentGatewayNotificationRequest notificationRequest =

   gatewayNotificationContext.getPaymentGatewayNotificationRequest();

   Blob request = notificationRequest.getRequestBody();

   Map<String, Object> jsonReq = (Map<String,

   Object>)JSON.deserializeUntyped(request.toString());

   List<Object> notificationItems = (List<Object>)jsonReq.get('notificationItems');

   Map<String, Object> notificationRequestItem =

      (Map<String, Object>)((Map<String,

   Object>)notificationItems[0]).get('NotificationRequestItem');

   Boolean success = Boolean.valueOf(notificationRequestItem.get('success'));

   String pspReference = (String)notificationRequestItem.get('pspReference');

   String eventCode = (String)notificationRequestItem.get('eventCode');

   Double amount = (Double)((Map<String,

   Object>)notificationRequestItem.get('amount')).get('value');

   commercepayments.NotificationStatus notificationStatus = null;

   if (success) {

      notificationStatus = commercepayments.NotificationStatus.Success;

   } else {

      notificationStatus = commercepayments.NotificationStatus.Failed;

   }

   commercepayments.BaseNotification notification = null;

   if ('CAPTURE'.equals(eventCode)) {

      notification = new commercepayments.CaptureNotification();

   } else if ('REFUND'.equals(eventCode)) {

      notification = new commercepayments.ReferencedRefundNotification();

   }

```


### Apex Reference Guide PaymentGatewayContext Class

```
   notification.setStatus(notificationStatus);

   notification.setGatewayReferenceNumber(pspReference);

   notification.setAmount(amount);

   commercepayments.NotificationSaveResult saveResult =

   commercepayments.NotificationClient.record(notification);

   commercepayments.GatewayNotificationResponse gnr = new

   commercepayments.GatewayNotificationResponse();

   if (saveResult.isSuccess()) {

      system.debug('Notification accepted by platform');

   } else {

      system.debug('Errors in the result '+ Blob.valueOf(saveResult.getErrorMessage()));

   }

   gnr.setStatusCode(200);

   gnr.setResponseBody(Blob.valueOf('[accepted]'));

   return gnr;

### PaymentGatewayContext Class

```

Wraps the information related to a payment request.

Namespace

CommercePayments on page 317

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.PaymentGatewayContext pgc = new

   CommercePayments.PaymentGatewayContext();

```

Example

```
   global commercepayments.GatewayResponse processRequest(commercepayments.PaymentGatewayContext

    gatewayContext) {

      commercepayments.RequestType requestType = gatewayContext.getPaymentRequestType();

      if (requestType == commercepayments.RequestType.Capture) {

        commercepayments.CaptureRequest captureRequest = (commercepayments.CaptureRequest)

    gatewayContext.getPaymentRequest();

      }

   }

```

IN THIS SECTION:

PaymentGatewayContext Constructors

PaymentGatewayContext Methods


Apex Reference Guide PaymentGatewayContext Class

#### PaymentGatewayContext Constructors The following are constructors for PaymentGatewayContext .

IN THIS SECTION:

##### PaymentGatewayContext(request, requestType)

Constructor to enable instance creation. This constructor is intended for test usage and throws an exception if used outside of the
Apex test context.

##### **`PaymentGatewayContext(request, requestType)`**

Constructor to enable instance creation. This constructor is intended for test usage and throws an exception if used outside of the Apex
test context.

Signature

```
   global PaymentGatewayContext(commercepayments.PaymentGatewayRequest request, String

   requestType)

```

Parameters

```
   request
```

Type: commercepayments.PaymentGatewayRequest

Raw payload. Sensitive attributes are masked to ensure PCI compliance.

```
   requestType
```

[Type: commercepayments.RequestType Enum](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_commercepayments_RequestType.htm)

Defines the type of request made to the gateway

#### PaymentGatewayContext Methods The following are methods for PaymentGatewayContext .

IN THIS SECTION:

##### getPaymentRequest()

Returns the payment request object.

getPaymentRequestType()
Returns the payment request type.

##### getPaymentRequest()

Returns the payment request object.

Signature

```
   global commercepayments.PaymentGatewayRequest getPaymentRequest()

```


### Apex Reference Guide PaymentGatewayNotificationContext Class

Return Value

Type: PaymentGatewayRequest

##### getPaymentRequestType()

Returns the payment request type.

Signature

```
   global String getPaymentRequestType()

```

Return Value

Type: String

### PaymentGatewayNotificationContext Class

Wraps the information related to a gateway notification.

Namespace

CommercePayments on page 317

Usage

This class is used with asynchronous payments. It wraps all of the information related to a notification from the payment gateway. The
payments platform provides its context to the payment gateway adapters.

The constructor of this class takes no arguments. For example:

```
   CommercePayments.PaymentGatewayNotificationContext pgnc = new

   CommercePayments.PaymentGatewayNotificationContext();

```

Example

```
   global commercepayments.GatewayNotificationResponse

   processNotification(commercepayments.PaymentGatewayNotificationContext

   gatewayNotificationContext) {

   commercepayments.PaymentGatewayNotificationRequest notificationRequest =

   gatewayNotificationContext.getPaymentGatewayNotificationRequest();

   }

```

IN THIS SECTION:

#### PaymentGatewayNotificationContext Methods PaymentGatewayNotificationContext Methods

### The following are methods for PaymentGatewayNotificationContext .


### Apex Reference Guide PaymentGatewayNotificationRequest Class

IN THIS SECTION:

##### getPaymentGatewayNotificationRequest()

Returns the payment gateway’s notification request.

##### getPaymentGatewayNotificationRequest()

Returns the payment gateway’s notification request.

Signature

```
   global commercepayments.PaymentGatewayNotificationRequest

##### `getPaymentGatewayNotificationRequest()`

```

Return Value

Type: PaymentGatewayNotificationRequest on page 440

### PaymentGatewayNotificationRequest Class

Contains the notification request data from the gateway.

Namespace

CommercePayments on page 317

Usage

When the payment gateway sends a notification for a payment request, the payments platform sends the notification request to the
gateway adapter. If the notification payload contains an `eventCode` of `CAPTURE`, the adapter constructs a
`CaptureNotification` . If the notification payload contains an `eventCode` of `REFUND`, the adapter constructs a
`ReferencedRefundNotification` . If the notification payload contains `eventCode` of `AUTHORISATION`, the adapter
constructs a `GatewayNotificationResponse` .

You can obtain a notification request from `PaymentGatewayNotificationContext` on page 439 by invoking its
##### getPaymentGatewayNotificationRequest method.

Example

```
   global commercepayments.GatewayNotificationResponse

      processNotification(commercepayments.PaymentGatewayNotificationContext

   gatewayNotificationContext) {

        commercepayments.PaymentGatewayNotificationRequest notificationRequest =

   gatewayNotificationContext.getPaymentGatewayNotificationRequest();

   }

```

IN THIS SECTION:

PaymentGatewayNotificationRequest Properties

PaymentGatewayNotificationRequest Methods


Apex Reference Guide PaymentGatewayNotificationRequest Class

#### PaymentGatewayNotificationRequest Properties The following are properties for PaymentGatewayNotificationRequest .

IN THIS SECTION:

##### requestBody

Body of the notification request sent by the payment gateway.

##### requestBody

Body of the notification request sent by the payment gateway.

Signature

```
   global Blob requestBody {get; set;}

```

Property Value

Type: Blob

#### PaymentGatewayNotificationRequest Methods The following are methods for PaymentGatewayNotificationRequest .

IN THIS SECTION:

##### getHeaders()

Gets HTTP headers from the notification request sent by the payment gateway.

##### getRequestBody()

Stores the notification request body information from the payment gateway’s notification request.

##### getHeaders()

Gets HTTP headers from the notification request sent by the payment gateway.

Signature

```
   global Map<String,String> getHeaders()

```

Return Value

Type: Map<String,String>

##### getRequestBody()

Stores the notification request body information from the payment gateway’s notification request.


### Apex Reference Guide PaymentMethodDetailsResponse Class

Signature

```
   global Blob getRequestBody()

```

Return Value

Type: Blob

### PaymentMethodDetailsResponse Class

This class contains the details about the payment method.

Namespace

CommercePayments

Example

```
   commercepayments.AlternativePaymentMethodResponse alternativePaymentMethodResponse = new

   commercepayments.AlternativePaymentMethodResponse();

   alternativePaymentMethodResponse.setEmail('alternativePaymentMethod');

   alternativePaymentMethodResponse.setEmail('foo@foo.com');

   alternativePaymentMethodResponse.setGatewayToken('NMoPoIOnTZSaRaWcV7gUUXe');

   alternativePaymentMethodResponse.setGatewayTokenDetails('gateway token details');

   commercepayments.PaymentMethodDetailsResponse response = new

   commercepayments.PaymentMethodDetailsResponse();

   response.setAlternativePaymentMethod(alternativePaymentMethodResponse);

```

IN THIS SECTION:

#### PaymentMethodDetailsResponse Methods PaymentMethodDetailsResponse Methods

### The following are methods for PaymentMethodDetailsResponse .

IN THIS SECTION:

##### setAlternativePaymentMethod(alternativePaymentMethod)

Sets the alternative payment method details.

setCardPaymentMethod(cardPaymentMethod)
Sets the details about the card payment method.

##### **`setAlternativePaymentMethod(alternativePaymentMethod)`**

Sets the alternative payment method details.


### Apex Reference Guide LineItemInput Class

Signature

```
   public void setAlternativePaymentMethod(commercepayments.AlternativePaymentMethodResponse

   alternativePaymentMethod)

```

Parameters

```
   alternativePaymentMethod
```

Type: CommercePayments.AlternativePaymentMethodResponse

Details of the alternative payment method.

Return Value

Type: void

##### **`setCardPaymentMethod(cardPaymentMethod)`**

Sets the details about the card payment method.

Signature

```
   public void setCardPaymentMethod(commercepayments.CardPaymentMethodResponse

   cardPaymentMethod)

```

Parameters

```
   cardPaymentMethod
```

Type: CommercePayments.CardPaymentMethodResponse

Details about the card payment method.

Return Value

Type: void

### LineItemInput Class

Sends the list of individual line items associated with the payment to the gateway adapter.

Namespace

CommercePayments on page 317

IN THIS SECTION:

LineItemInput Properties

LineItemInput Methods


Apex Reference Guide LineItemInput Class

#### LineItemInput Properties The following are properties for LineItemInput .

IN THIS SECTION:

additionalAttributes
Map of additional attributes.

commodityCode
Commodity code.

description
Description of the product.

discount
Discount applied to the line item level.

discountIndicator
Specifies whether a discount was applied to the specific line item.

dutyAmount
Duty or tariff applied specifically to a item (not the whole order).

grossNetIndicator
Specifies if the line item amount is Gross (before discounts) or Net (after discounts).

lineItemId
Line item identifier. Specify when multiple items are present.

lineItemTotal
Total amount for that line item.

name
Product or service name.

quantity
Quantity purchased.

shippingAmount
Shipping or freight cost allocated to that line item.

sku
SKU or product code.

taxAmount
Line-level tax amount.

taxRate
Tax percentage applied to that specific line item.

unitPrice
Unit price.

uom
Unit of measure. For example, EA, HRS, and KG.


Apex Reference Guide LineItemInput Class

##### **`additionalAttributes`**

Map of additional attributes.

Signature

```
   public Map<String,String> additionalAttributes {get; set;}

```

Property Value

Type: Map<String,String>

##### **`commodityCode`**

Commodity code.

Signature

```
   public String commodityCode {get; set;}

```

Property Value

Type: String

##### **`description`**

Description of the product.

Signature

```
   public String description {get; set;}

```

Property Value

Type: String

##### **`discount`**

Discount applied to the line item level.

Signature

```
   public Double discount {get; set;}

```

Property Value

Type: Double

##### **`discountIndicator`**

Specifies whether a discount was applied to the specific line item.


Apex Reference Guide LineItemInput Class

Signature

```
   public Boolean discountIndicator {get; set;}

```

Property Value

Type: Boolean

##### **`dutyAmount`**

Duty or tariff applied specifically to a item (not the whole order).

Signature

```
   public Double dutyAmount {get; set;}

```

Property Value

Type: Double

##### **`grossNetIndicator`**

Specifies if the line item amount is Gross (before discounts) or Net (after discounts).

Signature

```
   public String grossNetIndicator {get; set;}

```

Property Value

Type: String

##### **`lineItemId`**

Line item identifier. Specify when multiple items are present.

Signature

```
   public String lineItemId {get; set;}

```

Property Value

Type: String

##### **`lineItemTotal`**

Total amount for that line item.

Signature

```
   public Double lineItemTotal {get; set;}

```


Apex Reference Guide LineItemInput Class

Property Value

Type: Double

##### **`name`**

Product or service name.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### **`quantity`**

Quantity purchased.

Signature

```
   public Integer quantity {get; set;}

```

Property Value

Type: Integer

##### **`shippingAmount`**

Shipping or freight cost allocated to that line item.

Signature

```
   public Double shippingAmount {get; set;}

```

Property Value

Type: Double

##### **`sku`**

SKU or product code.

Signature

```
   public String sku {get; set;}

```

Property Value

Type: String


Apex Reference Guide LineItemInput Class

##### **`taxAmount`**

Line-level tax amount.

Signature

```
   public Double taxAmount {get; set;}

```

Property Value

Type: Double

##### **`taxRate`**

Tax percentage applied to that specific line item.

Signature

```
   public Double taxRate {get; set;}

```

Property Value

Type: Double

##### **`unitPrice`**

Unit price.

Signature

```
   public Double unitPrice {get; set;}

```

Property Value

Type: Double

##### **`uom`**

Unit of measure. For example, EA, HRS, and KG.

Signature

```
   public String uom {get; set;}

```

Property Value

Type: String

#### LineItemInput Methods The following are methods for LineItemInput .


Apex Reference Guide LineItemInput Class

IN THIS SECTION:

##### equals(obj)

Maintains the integrity of lists of type `LineItemInput` by determining the equality of external objects in a list. This method is
dynamic and based on the equals method in Java.

##### hashCode()

Maintains the integrity of lists of type `LineItemInput` .

##### toString()

Converts a date to a string.

##### **`equals(obj)`**

Maintains the integrity of lists of type `LineItemInput` by determining the equality of external objects in a list. This method is
dynamic and based on the equals method in Java.

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### **`hashCode()`**

Maintains the integrity of lists of type `LineItemInput` .

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a date to a string.

Signature

```
   public String toString()

```


### Apex Reference Guide PaymentMethodIdType Enum

Return Value

Type: String

### PaymentMethodIdType Enum

Specifies the ID of the payment method type.

Enum Values

The following are the values of the `commercepayments.PaymentMethodIdType` enum.

**Value** **Description**

`CardPaymentMethod` Card payment method ID.

`SavedPaymentMethod` Saved payment method ID.

### PaymentMethodTokenizationRequest Class

Stores data about a request to tokenize a card payment method. The tokenization process occurs in the payment gateway. This process
replaces sensitive customer data, such as a card number or CVV, with unique identification symbols. The symbols are used while the
data is handled by Salesforce, the payment gateway, and the customer bank, allowing Salesforce to store the token without storing
sensitive customer data.

Namespace

CommercePayments on page 317

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.PaymentMethodTokenizationRequest pmtr = new

   CommercePayments.PaymentMethodTokenizationRequest();

```

This class holds all the required details about the tokenize request. Gateway adapters read the information in this class while constructing
a tokenization JSON request, which is sent to the payment gateway.

Example

The following code is used within your payment gateway adapter Apex class.

Use the `GatewayResponse` class's `processRequest` method to build responses based on the request type that it receives
from an instance of `PaymentGatewayContext on page 437` . If the request type is Tokenize, `GatewayResponse on`
`page 429` calls the `createTokenizeResponse` method and passes an instance of the
### PaymentMethodTokenizationRequest class. The passed PaymentMethodTokenizationRequest object contains

the address and cardPaymentMethod information that the payment gateway needs to manage the tokenization process. For example:

```
   global commercepayments.GatewayResponse processRequest(commercepayments.paymentGatewayContext

    gatewayContext) {

```


Apex Reference Guide PaymentMethodTokenizationRequest Class

```
        commercepayments.RequestType requestType = gatewayContext.getPaymentRequestType();

         commercepayments.GatewayResponse response;

         try

         {

           if (requestType == commercepayments.RequestType.Tokenize) {

                response =

   createTokenizeResponse((commercepayments.PaymentMethodTokenizationRequest)gatewayContext.getPaymentRequest());

           }

           //Add other else if statements for different request types as needed.

           return response;

         }

         catch(SalesforceValidationException e)

         {

            commercepayments.GatewayErrorResponse error = new

   commercepayments.GatewayErrorResponse('400', e.getMessage());

            return error;

         }

      }

#### Configure the createTokenizeResponse method to accept an instance of PaymentMethodTokenizationRequest .
```

Then, build an instance of `PaymentMethodTokenizationResponse` based on the values received from the payment gateway.

```
      public commercepayments.GatewayResponse

   createTokenizeResponse(commercepayments.PaymentMethodTokenizationRequest tokenizeRequest)

    {

         commercepayments.PaymentMethodTokenizationResponse tokenizeResponse = new

   commercepayments.PaymentMethodTokenizationResponse();

         tokenizeResponse.setGatewayTokenEncrypted(encryptedValue);

         tokenizeResponse.setGatewayTokenDetails(tokenDetails);

         tokenizeResponse.setGatewayAvsCode(avsCode);

         tokenizeResponse.setGatewayMessage(gatewayMessage);

         tokenizeResponse.setGatewayResultCode(resultcode);

         tokenizeResponse.setGatewayResultCodeDescription(resultCodeDescription);

         tokenizeResponse.setSalesforceResultCodeInfo(resultCodeInfo);

         tokenizeResponse.setGatewayDate(system.now());

         return tokenizeResponse;

      }

```

The `tokenizeResponse` contains the results of the gateway's tokenization process, and if successful, the tokenized value.

IN THIS SECTION:

#### PaymentMethodTokenizationRequest Constructors

PaymentMethodTokenizationRequest Properties

PaymentMethodTokenizationRequest Methods

#### PaymentMethodTokenizationRequest Constructors The following are constructors for PaymentMethodTokenizationRequest .


Apex Reference Guide PaymentMethodTokenizationRequest Class

IN THIS SECTION:

##### PaymentMethodTokenizationRequest(paymentGatewayId)

Payment gateway ID constructor used with `paymentMethodTokenizationRequest` . This constructor is intended for test
usage and throws an exception if used outside of the Apex test context.

##### PaymentMethodTokenizationRequest() The following are constructors for PaymentMethodTokenizationRequest . PaymentMethodTokenizationRequest(paymentGatewayId)

Payment gateway ID constructor used with `paymentMethodTokenizationRequest` . This constructor is intended for test
usage and throws an exception if used outside of the Apex test context.

Signature

```
   global PaymentMethodTokenizationRequest(String paymentGatewayId)

```

Parameters

```
   paymentGatewayId
```

Type: String

The payment method’s payment gateway ID that will be tokenized.

##### PaymentMethodTokenizationRequest() The following are constructors for PaymentMethodTokenizationRequest .

Signature

```
   global PaymentMethodTokenizationRequest()

#### PaymentMethodTokenizationRequest Properties

##### The following are properties for PaymentMethodTokenizationRequest .

```

IN THIS SECTION:

address
The card payment method address to be tokenized.

bankPaymentMethod
The bank payment method containing data to be tokenized.

cardPaymentMethod
The card payment method containing data to be tokenized.

savedByMerchant
Indicates whether the payment method to be tokenized is saved by the marchant ( `true` ) or not ( `false` ).


Apex Reference Guide PaymentMethodTokenizationRequest Class

##### address

The card payment method address to be tokenized.

Signature

```
   global commercepayments.AddressRequest address {get; set;}

```

Property Value

Type: AddressRequest on page 329

##### **`bankPaymentMethod`**

The bank payment method containing data to be tokenized.

Signature

```
   public commercepayments.BankPaymentMethodRequest bankPaymentMethod {get; set;}

```

Property Value

Type: commercepayments.BankPaymentMethodRequest on page 366

##### cardPaymentMethod

The card payment method containing data to be tokenized.

Signature

```
   global commercepayments.CardPaymentMethodRequest cardPaymentMethod {get; set;}

```

Property Value

Type: CardPaymentMethodRequest on page 404

##### **`savedByMerchant`**

Indicates whether the payment method to be tokenized is saved by the marchant ( `true` ) or not ( `false` ).

Signature

```
   public Boolean savedByMerchant {get; set;}

```

Property Value

Type: Boolean

#### PaymentMethodTokenizationRequest Methods The following are methods for PaymentMethodTokenizationRequest .


Apex Reference Guide PaymentMethodTokenizationRequest Class

IN THIS SECTION:

##### equals(obj)

Maintains the integrity of lists of type `PaymentMethodTokenizationRequest` by determining the equality of external
objects in a list. This method is dynamic and is based on the equals method in Java.

##### hashCode()

Maintains the integrity of lists of type `PaymentMethodTokenizationRequest` by determining the uniquness of the
external object records in a list.

##### toString()

Converts a date to a string.

##### equals(obj)

Maintains the integrity of lists of type `PaymentMethodTokenizationRequest` by determining the equality of external objects
in a list. This method is dynamic and is based on the equals method in Java.

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### hashCode()

Maintains the integrity of lists of type `PaymentMethodTokenizationRequest` by determining the uniquness of the external
object records in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### toString()

Converts a date to a string.

Signature

```
   global String toString()

```


### Apex Reference Guide PaymentMethodTokenizationResponse Class

Return Value

Type: String

### PaymentMethodTokenizationResponse Class

Gateway response sent by payment gateway adapters for the payment method tokenization request. The response includes the payment
method’s token ID value.

Namespace

CommercePayments on page 317

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.PaymentMethodTokenizationResponse pmtr = new

   CommercePayments.PaymentMethodTokenizationResponse();

### After the payment gateway processes a tokenization request, the fields of PaymentMethodTokenizationResponse receive
```

and store information from the gateway's response. The gateway's response shows whether the tokenization request was successful,
the token value, and any additional messages or information about the tokenization process. You can then pass an instance of
### PaymentMethodTokenizationResponse to an authorization response or a sale response. This class is mapped to a response

class in the Java layer.

Example

### This constructor builds a new instance of the PaymentMethodTokenizationResponse class.

```
   commercepayments.PaymentMethodTokenizationResponse tokenizeResponse = new

   commercepayments.PaymentMethodTokenizationResponse();

### PaymentMethodTokenizationResponse contains only setter methods. Each setter accepts a value from the payment gateway and use it to set an attribute of PaymentMethodTokenizationResponse . The most important method in PaymentMethodTokenizationResponse is setGatewayTokenEncrypted, which
```

[uses Salesforce encryption to set an encrypted token value for a payment method. The](https://help.salesforce.com/s/articleView?id=platform.fields_about_encrypted_fields&type=5&language=en_US) `setGatewayTokenEncrypted` method
is available in Salesforce API v52.0 and later. We recommend using it to ensure your tokenized payment method values are encrypted
and secure. While the `setGatewayToken` method (available in earlier API versions) also returns a payment method token, the
tokenized value isn't encrypted.

If the instantiated class already has a gateway token, `setGatewayTokenEncrypted` throws an error.

```
      /** @description Method to set Gateway token to persist in Encrypted Text */

      global void setGatewayTokenEncrypted(String gatewayTokenEncrypted) {

         if (gatewayTokenSet) {

           throwTokenError();

         }

         this.delegate.setGatewayTokenEncrypted(gatewayTokenEncrypted);

         gatewayTokenEncryptedSet = true;

      }

```


Apex Reference Guide PaymentMethodTokenizationResponse Class

A typical instantiation of `PaymentMethodTokenizationResponse` sets the encrypted gateway token alongside the other
tokenization response values sent by the gateway.

```
      public commercepayments.GatewayResponse

   createTokenizeResponse(commercepayments.PaymentMethodTokenizationRequest tokenizeRequest)

    {

         commercepayments.PaymentMethodTokenizationResponse tokenizeResponse = new

   commercepayments.PaymentMethodTokenizationResponse();

         tokenizeResponse.setGatewayTokenEncrypted(gatewayTokenEncrypted);

         tokenizeResponse.setGatewayTokenDetails(gatewayTokenDetails);

         tokenizeResponse.setGatewayAvsCode(gatewayAvsCode);

         tokenizeResponse.setGatewayMessage(gatewayMessage);

         tokenizeResponse.setGatewayResultCode(gatewayResultCode);

         tokenizeResponse.setGatewayResultCodeDescription(gatewayResultCodeDescription);

        tokenizeResponse.setSalesforceResultCodeInfo(SUCCESS_SALESFORCE_RESULT_CODE_INFO);

         tokenizeResponse.setGatewayDate(system.now());

         return tokenizeResponse;

      }

```

After you've built a PaymentMethodTokenizationResponse object and set the encrypted gateway token, pass the object to the
`setPaymentMethodTokenizationResponse` method of an authorization response or a sale response.

**Authorization Response**

```
        public commercepayments.GatewayResponse

     createAuthResponse(commercepayments.AuthorizationRequest authRequest) {

          commercepayments.AuthorizationResponse authResponse = new

     commercepayments.AuthorizationResponse();

          commercepayments.PaymentMethodTokenizationResponse

     paymentMethodTokenizationResponse = new

     commercepayments.PaymentMethodTokenizationResponse();

          if(authRequest.amount!=null )

          {

             authResponse.setAmount(authRequest.amount);

          }

          else

          {

            throw new SalesforceValidationException('Required Field Missing : Amount');

          }

          authResponse.setGatewayResultCode('00');

          authResponse.setGatewayResultCodeDescription('Transaction Normal');

          authResponse.setGatewayAuthCode('SF'+getRandomNumber(6));

          authResponse.setGatewayReferenceNumber(getRandomNumber(10));

          authResponse.setSalesforceResultCodeInfo(SUCCESS_SALESFORCE_RESULT_CODE_INFO);

          authResponse.setGatewayDate(system.now());

     paymentMethodTokenizationResponse.setGatewayTokenEncrypted(gatewayTokenEncrypted);

     authResponse.setPaymentMethodTokenizationResponse(paymentMethodTokenizationResponse);

          return authResponse;

        }

```


Apex Reference Guide PaymentMethodTokenizationResponse Class

**Sale Response**

```
        public commercepayments.GatewayResponse

     createSaleResponse(commercepayments.SaleRequest saleRequest) {

          commercepayments.SaleResponse saleResponse = new commercepayments.SaleResponse();

          commercepayments.PaymentMethodTokenizationResponse

     paymentMethodTokenizationResponse = new

     commercepayments.PaymentMethodTokenizationResponse();

          if(saleRequest.amount!=null )

          {

             saleResponse.setAmount(saleRequest.amount);

          }

          else

          {

            throw new SalesforceValidationException('Required Field Missing : Amount');

          }

          system.debug('Response - success');

          saleResponse.setGatewayDate(system.now());

          saleResponse.setGatewayResultCode('00');

          saleResponse.setGatewayResultCodeDescription('Transaction Normal');

          saleResponse.setGatewayReferenceNumber('SF'+getRandomNumber(6));

          saleResponse.setSalesforceResultCodeInfo(SUCCESS_SALESFORCE_RESULT_CODE_INFO);

     paymentMethodTokenizationResponse.setGatewayTokenEncrypted(gatewayTokenEncrypted) ;

     saleResponse.setPaymentMethodTokenizationResponse(paymentMethodTokenizationResponse) ;

          return saleResponse;

        }

```

IN THIS SECTION:

#### PaymentMethodTokenizationResponse Methods PaymentMethodTokenizationResponse Methods The following are methods for PaymentMethodTokenizationResponse .

IN THIS SECTION:

setAmount(amount)
Sets the amount for payment tokenization. Can be positive, negative, or zero.

setAsync(async)
Indicates whether the gateway response is received asynchronously ( `true` ) or not ( `false` ). When set to `true`, the saved payment
method remains in a pending state until the async notification is received.

setBankName(bankName)
Sets the bank name for payment tokenization.


Apex Reference Guide PaymentMethodTokenizationResponse Class

setChecksum(checksum)
Sets the unique hash of the payment method that the gateway returned.

setCustomerReference(customerReference)
Sets the customer reference number that the gateway returned.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the tokenization occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the tokenization request. Maximum length of 255 characters.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets any additional reference details that the gateway returned.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the reference number that the gateway returned.

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

setGatewayToken(gatewayToken)
Sets the gateway token value that the gateway returned.

setGatewayTokenDetails(gatewayTokenDetails)
Sets any additional information that the gateway returned about the payment token.

setGatewayTokenEncrypted(gatewayTokenEncrypted)
Sets the value of the `gatewayTokenEncrypted` field on a CardPaymentMethod or DigitalWallet object.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

##### **`setAmount(amount)`**

Sets the amount for payment tokenization. Can be positive, negative, or zero.

Signature

```
   public void setAmount(Double amount)

```

Parameters

```
   amount
```

Type: Double

Return Value

Type: void


Apex Reference Guide PaymentMethodTokenizationResponse Class

##### **`setAsync(async)`**

Indicates whether the gateway response is received asynchronously ( `true` ) or not ( `false` ). When set to `true`, the saved payment
method remains in a pending state until the async notification is received.

Signature

```
   public void setAsync(Boolean async)

```

Parameters

```
   async
```

Type: Boolean

Return Value

Type: void

##### **`setBankName(bankName)`**

Sets the bank name for payment tokenization.

Signature

```
   public void setBankName(String bankName)

```

Parameters

```
   bankName
```

Type: String

Return Value

Type: void

##### **`setChecksum(checksum)`**

Sets the unique hash of the payment method that the gateway returned.

Signature

```
   public void setChecksum(String checksum)

```

Parameters

```
   checksum
```

Type: String

Return Value

Type: void


Apex Reference Guide PaymentMethodTokenizationResponse Class

##### **`setCustomerReference(customerReference)`**

Sets the customer reference number that the gateway returned.

Signature

```
   public void setCustomerReference(String customerReference)

```

Parameters

```
   customerReference
```

Type: String

Return Value

Type: void

##### setGatewayAvsCode(gatewayAvsCode)

Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

Signature

```
   global void setGatewayAvsCode(String gatewayAvsCode)

```

Parameters

```
   gatewayAvsCode
```

Type: String

Used to verify the address mapped to a payment method when the payments platform requests tokenization from the payment
gateway.

Return Value

Type: void

##### setGatewayDate(gatewayDate)

Sets the date that the tokenization occurred. Some gateways don’t send this value.

Signature

```
   global void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime


Apex Reference Guide PaymentMethodTokenizationResponse Class

Return Value

Type: void

##### setGatewayMessage(gatewayMessage)

Sets error messages that the gateway returned for the tokenization request. Maximum length of 255 characters.

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String

Return Value

Type: void

##### **`setGatewayReferenceDetails(gatewayReferenceDetails)`**

Sets any additional reference details that the gateway returned.

Signature

```
   public void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String

Return Value

Type: void

##### **`setGatewayReferenceNumber(gatewayReferenceNumber)`**

Sets the reference number that the gateway returned.

Signature

```
   public void setGatewayReferenceNumber(String gatewayReferenceNumber)

```

Parameters

```
   gatewayReferenceNumber
```

Type: String


Apex Reference Guide PaymentMethodTokenizationResponse Class

Return Value

Type: void

##### setGatewayResultCode(gatewayResultCode)

Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

Signature

```
   global void setGatewayResultCode(String gatewayResultCode)

```

Parameters

```
   gatewayResultCode
```

Type: String

Gateway-specific result code. Must be used to map a Salesforce-specific result code.

Return Value

Type: void

##### setGatewayResultCodeDescription(gatewayResultCodeDescription)

Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

Signature

```
   global void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Provides additional information about the result code and why the gateway returned the specific code. Descriptions will vary between
different gateways.

Return Value

Type: void

##### setGatewayToken(gatewayToken)

Sets the gateway token value that the gateway returned.

Signature

```
   global void setGatewayToken(String gatewayToken)

```


Apex Reference Guide PaymentMethodTokenizationResponse Class

Parameters

```
   gatewayToken
```

Type: String

The gateway token that the payment gateway sends following a tokenization request.

For the CardPaymentMethod and DigitalWallet objects, use the _`gatewyTokenEncrypted`_ parameter, which encrypts the
token value.

Return Value

Type: void

##### setGatewayTokenDetails(gatewayTokenDetails)

Sets any additional information that the gateway returned about the payment token.

Signature

```
   global void setGatewayTokenDetails(String gatewayTokenDetails)

```

Parameters

```
   gatewayTokenDetails
```

Type: String

Return Value

Type: void

##### **`setGatewayTokenEncrypted(gatewayTokenEncrypted)`**

Sets the value of the `gatewayTokenEncrypted` field on a CardPaymentMethod or DigitalWallet object.

Signature

```
   global void setGatewayTokenEncrypted(String gatewayTokenEncrypted)

```

Parameters

```
   gatewayTokenEncrypted
```

Type: String

[The gateway token that the payment gateway sends following a tokenization request. Salesforce Payments uses Salesforce encryption](https://help.salesforce.com/s/articleView?id=platform.fields_about_encrypted_fields&type=5&language=en_US)
to encrypt the token value.

Return Value

Type: void


### Apex Reference Guide PaymentsHttp Class

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce uses
the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: SalesforceResultCodeInfo on page 519

Description of the Salesforce result code value.

Return Value

Type: void

### PaymentsHttp Class

Makes an HTTP request to start the interaction with the payment gateway.

Namespace

CommercePayments on page 317

Usage

You must specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes
no arguments. For example:

```
   CommercePayments.PaymentsHttp payhttp = new CommercePayments.PaymentsHttp();

```

IN THIS SECTION:

#### PaymentsHttp Methods

PaymentsHttp Constructors

#### PaymentsHttp Methods

### The following are methods for PaymentsHttp . All methods are instance methods.

IN THIS SECTION:

send(Request)
Sends an HttpRequest and returns the response.


### Apex Reference Guide PostAuthApiPaymentMethodRequest Class

##### send(Request)

Sends an HttpRequest and returns the response.

Signature

```
   global HttpResponse send(HttpRequest request)

```

Parameters

```
   request
```

[Type: System.HttpRequest](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_restful_http_httprequest.htm#apex_classes_restful_http_httprequest)

Return Value

[Type: System.HttpResponse](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_restful_http_httpresponse.htm#apex_classes_restful_http_httpresponse)

#### PaymentsHttp Constructors The following are constructors for PaymentsHttp .

IN THIS SECTION:

##### PaymentsHttp()

Initiates an HTTP request and response.

##### PaymentsHttp()

Initiates an HTTP request and response.

Signature

```
   global PaymentsHttp()

### PostAuthApiPaymentMethodRequest Class

```

Sends information about a payment method to a gateway adapter during a postauthorization service call.

Namespace

CommercePayments

Usage

Contains information about the payment method that is used for a postauthorization request. It contains all available payment methods
as fields, but populates only one field for each request. The gateway adapter uses this class when constructing a postauthorization
request. An object of this class is available through the `paymentMethod` field on the `PostAuthorizationRequest Class`
object.


Apex Reference Guide PostAuthApiPaymentMethodRequest Class

IN THIS SECTION:

#### PostAuthApiPaymentMethodRequest Constructors

Lists the constructors for the PostAuthApiPaymentMethodRequest.

PostAuthApiPaymentMethodRequest Properties
Lists the properties for PostAuthApiPaymentMethodRequest.

#### PostAuthApiPaymentMethodRequest Constructors

Lists the constructors for the PostAuthApiPaymentMethodRequest.

#### The following are constructors for PostAuthApiPaymentMethodRequest .

IN THIS SECTION:

##### PostAuthApiPaymentMethodRequest(cardPaymentMethodRequest)

Constructs a sample `cardPaymentMethodRequest` . This constructor is intended for test usage and throws an exception if
used outside of the Apex test context.

##### PostAuthApiPaymentMethodRequest(AlternativePaymentMethodRequest)

Constructs a sample `alternativePaymentMethodRequest` . This constructor is intended for test usage and throws an
exception if used outside of the Apex test context.

PostAuthApiPaymentMethodRequest()
#### Constructor for PostAuthApiPaymentMethodRequest .

##### **`PostAuthApiPaymentMethodRequest(cardPaymentMethodRequest)`**

Constructs a sample `cardPaymentMethodRequest` . This constructor is intended for test usage and throws an exception if used
outside of the Apex test context.

Signature

```
   global PostAuthApiPaymentMethodRequest(commercepayments.CardPaymentMethodRequest

   cardPaymentMethodRequest)

```

Parameters

```
   cardPaymentMethodRequest
```

Type: commercepayments.CardPaymentMethodRequest on page 404

Contains information about the card payment method. Used to send information to a gateway adapter during a service call.

##### **`PostAuthApiPaymentMethodRequest(AlternativePaymentMethodRequest)`**

Constructs a sample `alternativePaymentMethodRequest` . This constructor is intended for test usage and throws an exception
if used outside of the Apex test context.

Signature

```
   global

   PostAuthApiPaymentMethodRequest(commercepayments.AlternativePaymentMethodRequestPaymentMethodRequest)

```


Apex Reference Guide PostAuthApiPaymentMethodRequest Class

Parameters

##### _`alternativePaymentMethodRequest`_

Type: commercepayments.AlternativePaymentMethodRequest on page 404

Contains information about the alternative payment method. Used to send information to a gateway adapter during a service call.

##### **`PostAuthApiPaymentMethodRequest()`** Constructor for PostAuthApiPaymentMethodRequest .

Signature

```
   global PostAuthApiPaymentMethodRequest()

#### PostAuthApiPaymentMethodRequest Properties

```

Lists the properties for PostAuthApiPaymentMethodRequest.

##### The following are properties for PostAuthApiPaymentMethodRequest .

IN THIS SECTION:

##### cardPaymentMethod

The card payment method object used in a postauthorizaiton payment method request.

##### alternativePaymentMethod

The alternative payment method object used in a postauthorizaiton payment method request.

##### **`cardPaymentMethod`**

The card payment method object used in a postauthorizaiton payment method request.

Signature

```
   global commercepayments.CardPaymentMethodRequest cardPaymentMethod {get; set;}

```

Property Value

Type: commercepayments.CardPaymentMethodRequest on page 404

##### **`alternativePaymentMethod`**

The alternative payment method object used in a postauthorizaiton payment method request.

Signature

```
   global commercepayments.AlternativePaymentMethodRequest PaymentMethod {get; set;}

```

Property Value

Type: commercepayments.alternativePaymentMethodRequest


### Apex Reference Guide PostAuthorizationRequest Class PostAuthorizationRequest Class

Sends information about a postauthorization request to a gateway adapter during a service call.

Namespace

CommercePayments

Usage

This class extends `[BaseRequest](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_BaseRequest.htm)` and contains information about a transaction postauthorization request. The gateway adapter reads
fields from this class to validate the client-side transaction with the payment gateway. An object of this class is available by calling
`getPaymentRequest()` in the `PaymentGatewayContext Class` ).

```
    ((commercepayments.PostAuthorizationRequest)gatewayContext.getPaymentRequest());

```

IN THIS SECTION:

#### PostAuthorizationRequest Constructors

Lists the constructors for postauthorization requests.

PostAuthorizationRequest Properties
Lists properties for a postauthorizaiton request.

#### PostAuthorizationRequest Constructors

Lists the constructors for postauthorization requests.

### The following are constructors for PostAuthorizationRequest .

IN THIS SECTION:

##### PostAuthorizationRequest(amount)

Constructor for building the amount in a postauthorization request. This constructor is intended for test usage and throws an
exception if used outside of the Apex test context.

##### **`PostAuthorizationRequest(amount)`**

Constructor for building the amount in a postauthorization request. This constructor is intended for test usage and throws an exception
if used outside of the Apex test context.

Signature

```
   global PostAuthorizationRequest(Double amount)

```

Parameters

```
   amount
```

Type: Double

The amount of the authorization.


Apex Reference Guide PostAuthorizationRequest Class

#### PostAuthorizationRequest Properties

Lists properties for a postauthorizaiton request.

#### The following are properties for a PostAuthorizationRequest .

IN THIS SECTION:

##### accountId

The customer account that is settled when the postauthorization is performed.

##### amount

The total amount of the postauthorization request.

##### comments

Comments about the postauthorization. Users can enter comments to provide additional information.

currencyIsoCode
The ISO currency code for the postauthorization request.

paymentMethod
The payment method used to process the postauthorization request.

##### **`accountId`**

The customer account that is settled when the postauthorization is performed.

Signature

```
   global String accountId {get; set;}

```

Property Value

Type: String

##### **`amount`**

The total amount of the postauthorization request.

Signature

```
   global Double amount {get; set;}

```

Property Value

Type: Double

##### **`comments`**

Comments about the postauthorization. Users can enter comments to provide additional information.


### Apex Reference Guide PostAuthorizationResponse Class

Signature

```
   global String comments {get; set;}

```

Property Value

Type: String

##### **`currencyIsoCode`**

The ISO currency code for the postauthorization request.

Signature

```
   global String currencyIsoCode {get; set;}

```

Property Value

Type: String

##### **`paymentMethod`**

The payment method used to process the postauthorization request.

Signature

```
   global PostAuthApiPaymentMethodRequest paymentMethod {get; set;}

```

Property Value

Type: AuthApiPaymentMethodRequest on page 343

### PostAuthorizationResponse Class

Response sent by the payment gateway adapter for a postauthorization service.

Namespace

CommercePayments

Usage

[This class extends AbstractTransactionResponse. The constructor of this class takes no arguments. For example:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_AbstractTransactionResponse.htm)

```
   CommercePayments.PostAuthorizationResponse authr = new

   CommercePayments.PostAuthorizationResponse();

```

Contains information about the payment gateway’s response following an authorization transaction. The gateway adapter uses the
### payment gateway’s response to populate the PostAuthorizationResponse fields. The payments platform uses the information

from this class to settle the transaction.


Apex Reference Guide PostAuthorizationResponse Class

IN THIS SECTION:

#### PostAuthorizationResponse Methods Lists the methods for the PostAuthorizationResponse . PostAuthorizationResponse Methods Lists the methods for the PostAuthorizationResponse . The following are methods for PostAuthorizationResponse .

IN THIS SECTION:

setAlternativePaymentMethodResponse(AlternativePaymentMethodResponsealternativePaymentMethod)
Sets details from the gateway about the authorized alternative payment method.

setAmount(amount)
Sets the amount for payment authorization. Can be positive, negative, or zero.

setAsync(async)
Sets whether the payment capture or authorization is asynchronous ( `True` ) or synchronous ( `False` ). If `True`, then the payment
or payment authorization record created has a status of `Pending` .

setAuthorizationExpirationDate(authExpDate)
Sets the expiration date of the authorization request.

setGatewayAuthCode(gatewayAuthCode)
Sets the authorization code that the gateway returned. Maximum length of 64 characters.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the authorization occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the tokenization request. Maximum length of 255 characters.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets any additional reference details that the gateway returned.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the reference number that the gateway returned.

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

setPaymentMethodDetails(paymentMethodDetails)
Sets details about the payment method.

setPaymentMethodTokenizationResponse(paymentMethodTokenizationResponse)
Sets information from the gateway about the tokenized payment method.


Apex Reference Guide PostAuthorizationResponse Class

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

##### **`setAlternativePaymentMethodResponse(AlternativePaymentMethodResponsealternativePaymentMethod)`**

Sets details from the gateway about the authorized alternative payment method.

Signature

```
   global void

   setAlternativePaymentMethodResponse(commercepayments.AlternativePaymentMethodResponse

   paymentMethodResponse)

```

Parameters

```
   alternativePaymentMethodResponse
```

Gateway response sent by payment gateway adapter for the alternative payment method request.

Return Value

Type: void

##### **`setAmount(amount)`**

Sets the amount for payment authorization. Can be positive, negative, or zero.

Signature

```
   public void setAmount(Double amount)

```

Parameters

```
   amount
```

Type: Double

Return Value

Type: void

##### **`setAsync(async)`**

Sets whether the payment capture or authorization is asynchronous ( `True` ) or synchronous ( `False` ). If `True`, then the payment or
payment authorization record created has a status of `Pending` .

Signature

```
   global void setAsync(Boolean async)

```


Apex Reference Guide PostAuthorizationResponse Class

Parameters

```
   async
```

Type: Boolean

Return Value

Type: void

##### **`setAuthorizationExpirationDate(authExpDate)`**

Sets the expiration date of the authorization request.

Signature

```
   global void setAuthorizationExpirationDate(Datetime authExpDate)

```

Parameters

```
   authExpDate
```

Type: Datetime

Return Value

Type: void

##### **`setGatewayAuthCode(gatewayAuthCode)`**

Sets the authorization code that the gateway returned. Maximum length of 64 characters.

Signature

```
   global void setGatewayAuthCode(String gatewayAuthCode)

```

Parameters

```
   gatewayAuthCode
```

Type: String

The authorization code returned by the gateway.

Return Value

Type: void

##### **`setGatewayAvsCode(gatewayAvsCode)`**

Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

Signature

```
   public void setGatewayAvsCode(String gatewayAvsCode)

```


Apex Reference Guide PostAuthorizationResponse Class

Parameters

```
   gatewayAvsCode
```

Type: String

Used to verify the address mapped to a payment method when the payments platform requests tokenization from the payment
gateway.

Return Value

Type: void

##### **`setGatewayDate(gatewayDate)`**

Sets the date that the authorization occurred. Some gateways don’t send this value.

Signature

```
   public void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

Return Value

Type: void

##### **`setGatewayMessage(gatewayMessage)`**

Sets error messages that the gateway returned for the tokenization request. Maximum length of 255 characters.

Signature

```
   public void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String

Return Value

Type: void

##### **`setGatewayReferenceDetails(gatewayReferenceDetails)`**

Sets any additional reference details that the gateway returned.


Apex Reference Guide PostAuthorizationResponse Class

Signature

```
   public void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String

Return Value

Type: void

##### **`setGatewayReferenceNumber(gatewayReferenceNumber)`**

Sets the reference number that the gateway returned.

Signature

```
   public void setGatewayReferenceNumber(String gatewayReferenceNumber)

```

Parameters

```
   gatewayReferenceNumber
```

Type: String

Return Value

Type: void

##### **`setGatewayResultCode(gatewayResultCode)`**

Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

Signature

```
   public void setGatewayResultCode(String gatewayResultCode)

```

Parameters

```
   gatewayResultCode
```

Type: String

Gateway-specific result code. Must be used to map a Salesforce-specific result code.

Return Value

Type: void

##### **`setGatewayResultCodeDescription(gatewayResultCodeDescription)`**

Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.


Apex Reference Guide PostAuthorizationResponse Class

Signature

```
   public void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Provides additional information about the result code and why the gateway returned the specific code. Descriptions will vary between
different gateways.

Return Value

Type: void

##### **`setPaymentMethodDetails(paymentMethodDetails)`**

Sets details about the payment method.

Signature

```
   public void setPaymentMethodDetails(commercepayments.PaymentMethodDetailsResponse

   paymentMethodDetails)

```

Parameters

```
   paymentMethodDetails
```

Type: commercepayments.PaymentMethodDetailsResponse

Return Value

Type: void

##### **`setPaymentMethodTokenizationResponse(paymentMethodTokenizationResponse)`**

Sets information from the gateway about the tokenized payment method.

Signature

```
   global void

   setPaymentMethodTokenizationResponse(commercepayments.PaymentMethodTokenizationResponse

   paymentMethodTokenizationResponse)

```

Parameters

```
   paymentMethodTokenizationResponse
```

PaymentMethodTokenizationResponse on page 455

Gateway response sent by payment gateway adapters for the payment method tokenization request.


### Apex Reference Guide ReferencedRefundNotification Class

Return Value

Type: void

##### **`setSalesforceResultCodeInfo(salesforceResultCodeInfo)`**

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce uses
the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Signature

```
   public void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: commercepayments.SalesforceResultCodeInfo on page 519

Description of the Salesforce result code value.

Return Value

Type: void

### ReferencedRefundNotification Class

When a payment gateway sends a notification for a refund transaction, the payment gateway adapter creates the
### ReferencedRefundNotification object to store information about notification.

Namespace

CommercePayments on page 317

Usage

This class is used with asynchronous payments. When a payment gateway sends a notification for a refund transcation, the gateway
### adapter creates an object of type ReferencedRefundNotification to populate the respective values.

The constructor of this class takes no arguments. For example:

```
   CommercePayments.ReferencedRefundNotification rrn = new

   CommercePayments.ReferencedRefundNotification();

```

Example

```
   commercepayments.NotificationStatus notificationStatus = null;

        if (success) {

           notificationStatus = commercepayments.NotificationStatus.Success;

        } else {

           notificationStatus = commercepayments.NotificationStatus.Failed;

        }

```


Apex Reference Guide ReferencedRefundNotification Class

```
        commercepayments.BaseNotification notification = null;

        if ('CAPTURE'.equals(eventCode)) {

           notification = new commercepayments.CaptureNotification();

        } else if ('REFUND'.equals(eventCode)) {

           notification = new commercepayments.ReferencedRefundNotification();

        }

```

IN THIS SECTION:

#### ReferencedRefundNotification Methods ReferencedRefundNotification Methods The following are methods for ReferencedRefundNotification .

IN THIS SECTION:

##### setAmount(amount)

Sets the transaction amount. Can be positive, negative, or zero.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that communication for the refund notification occurred with the payment gateway.

setGatewayMessage(gatewayMessage)
Sets information or messages that the gateway returned.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets the payment gateway’s reference details.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the payment gateway’s reference number.

setGatewayResultCode(gatewayResultCode)
Sets the payment gateway’s result code.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets the payment gateway’s result code description.

setId(id)
Sets the ID of a notification sent by the payment gateway.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets Salesforce result code information.

setStatus(status)
Sets the notification status value on the notification object.

##### setAmount(amount)

Sets the transaction amount. Can be positive, negative, or zero.


Apex Reference Guide ReferencedRefundNotification Class

Signature

```
   global void setAmount(Double amount)

```

Parameters

```
   amount
```

Type: Double

The amount to be debited or captured.

Return Value

Type: void

##### **`setGatewayAvsCode(gatewayAvsCode)`**

Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

Signature

```
   public void setGatewayAvsCode(String gatewayAvsCode)

```

Parameters

```
   gatewayAvsCode
```

Type: String

Used to verify the address mapped to a payment method when the payments platform requests tokenization from the payment
gateway.

Return Value

Type: void

##### setGatewayDate(gatewayDate)

Sets the date that communication for the refund notification occurred with the payment gateway.

Signature

```
   global void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

The date that communication happened with the gateway.

Return Value

Type: void


Apex Reference Guide ReferencedRefundNotification Class

##### setGatewayMessage(gatewayMessage)

Sets information or messages that the gateway returned.

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String

Return Value

Type: void

##### setGatewayReferenceDetails(gatewayReferenceDetails)

Sets the payment gateway’s reference details.

Signature

```
   global void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String

Provides information about the gateway communication.

Return Value

Type: void

##### setGatewayReferenceNumber(gatewayReferenceNumber)

Sets the payment gateway’s reference number.

Signature

```
   global void setGatewayReferenceNumber(String gatewayReferenceNumber)

```

Parameters

```
   gatewayReferenceNumber
```

Type: String

Unique transaction ID created by the payment gateway.


Apex Reference Guide ReferencedRefundNotification Class

Return Value

Type: void

##### setGatewayResultCode(gatewayResultCode)

Sets the payment gateway’s result code.

Signature

```
   global void setGatewayResultCode(String gatewayResultCode)

```

Parameters

```
   gatewayResultCode
```

Type: String

The gateway result code. You must map this to a Salesforce-specific result code.

Return Value

Type: void

##### setGatewayResultCodeDescription(gatewayResultCodeDescription)

Sets the payment gateway’s result code description.

Signature

```
   global void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Description of the gateway result code. Provides additional context about the result code .

Return Value

Type: void

##### setId(id)

Sets the ID of a notification sent by the payment gateway.

Signature

```
   global void setId(String id)

```


### Apex Reference Guide ReferencedRefundRequest

Parameters

```
   id
```

Type: String

Return Value

Type: void

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Sets Salesforce result code information.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: SalesforceResultCodeInfo on page 519

Description of the Salesforce result code value.

Return Value

Type: void

##### setStatus(status)

Sets the notification status value on the notification object.

Signature

```
   global void setStatus(commercepayments.NotificationStatus status)

```

Parameters

```
   status
```

Type: NotificationStatus on page 432

Indicates whether the payments platform successfully received the notification from the payment gateway.

Return Value

Type: void

### ReferencedRefundRequest

Access information about the referenced refund requests. Extends the `RefundRequest` class.


#### Apex Reference Guide ReferencedRefundRequest

Namespace

CommercePayments on page 317

Example

```
   global commercepayments.GatewayResponse processRequest(commercepayments.PaymentGatewayContext

    gatewayContext) {

      commercepayments.RequestType requestType = gatewayContext.getPaymentRequestType();

      if (requestType == commercepayments.RequestType.ReferencedRefund) {

        commercepayments.*ReferencedRefundRequest* refundRequest =

   (commercepayments.*ReferencedRefundRequest*) gatewayContext.getPaymentRequest();

      }

   }

```

IN THIS SECTION:

#### ReferencedRefundRequest Constructors ReferencedRefundRequest Properties

ReferencedRefundRequest Methods

#### ReferencedRefundRequest Constructors The following are constructors for ReferencedRefundRequest .

IN THIS SECTION:

##### ReferencedRefundRequest(amount, paymentId)

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

##### ReferencedRefundRequest(amount, paymentId)

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Parameters

```
   amount
```

Type: Double

The amount to be debited or captured.

```
   paymentId
```

Type: String

The payment record.

#### ReferencedRefundRequest Properties The following are properties for ReferencedRefundRequest .


### Apex Reference Guide ReferencedRefundResponse Class

IN THIS SECTION:

##### PaymentId

References a payment object.

##### accountId

References an account.

##### amount

References an amount.

##### PaymentId

References a payment object.

Property Value

Type: String

##### accountId

References an account.

Property Value

Type: String

##### amount

References an amount.

Property Value

Type: Double

#### ReferencedRefundRequest Methods The following are methods for ReferencedRefundRequest .

### ReferencedRefundResponse Class

#### The payment gateway adapter sends this response for the ReferencedRefund request type.

Namespace

CommercePayments on page 317

Usage

The constructor of this class takes no arguments. For example:


Apex Reference Guide ReferencedRefundResponse Class

```
   CommercePayments.ReferencedRefundResponse refr = new

   CommercePayments.ReferencedRefundResponse();

```

IN THIS SECTION:

#### ReferencedRefundResponse Methods ReferencedRefundResponse Methods The following are methods for ReferencedRefundResponse .

IN THIS SECTION:

##### setAmount(amount)

Sets the transaction amount. The value must be a postive number.

setAsync(async)
Sets whether the payment capture or authorization is asynchronous ( `True` ) or synchronous ( `False` ). If `True`, then the payment
refund record created has a status of `Pending` .

setGatewayAvsCode(gatewayAvsCode)
Sets the payment gateway’s address verification system (AVS) code.

setGatewayDate(gatewayDate)
Sets the payment gateway’s date.

setGatewayMessage(gatewayMessage)
Sets information or messages that the gateway returned.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets the payment gateway’s reference details.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the payment gateway’s reference number.

setGatewayResultCode(gatewayResultCode)
Sets the payment gateway’s result code.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets the payment gateway’s result code description.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Set the Salesforce result code info.

##### setAmount(amount)

Sets the transaction amount. The value must be a postive number.

Signature

```
   global void setAmount(Double amount)

```


Apex Reference Guide ReferencedRefundResponse Class

Parameters

```
   amount
```

Type: Double

The amount to be debited or captured.

Return Value

Type: void

##### **`setAsync(async)`**

Sets whether the payment capture or authorization is asynchronous ( `True` ) or synchronous ( `False` ). If `True`, then the payment
refund record created has a status of `Pending` .

Signature

```
   public void setAsync(Boolean async)

```

Parameters

```
   async
```

Type: Boolean

Return Value

Type: void

##### setGatewayAvsCode(gatewayAvsCode)

Sets the payment gateway’s address verification system (AVS) code.

Signature

```
   global void setGatewayAvsCode(String gatewayAvsCode)

```

Parameters

```
   gatewayAvsCode
```

Type: String

Code sent by gateways that use an address verification system.

Return Value

Type: void

##### setGatewayDate(gatewayDate)

Sets the payment gateway’s date.


Apex Reference Guide ReferencedRefundResponse Class

Signature

```
   global void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

Date and time of the gateway communication.

Return Value

Type: void

##### setGatewayMessage(gatewayMessage)

Sets information or messages that the gateway returned.

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```

Parameters

```
   gatewayMessage
```

Type: String

Information or error messages returned by the gateway.

Return Value

Type: void

##### setGatewayReferenceDetails(gatewayReferenceDetails)

Sets the payment gateway’s reference details.

Signature

```
   global void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String

Information about the gateway communication.

Return Value

Type: void


Apex Reference Guide ReferencedRefundResponse Class

##### setGatewayReferenceNumber(gatewayReferenceNumber)

Sets the payment gateway’s reference number.

Signature

```
   global void setGatewayReferenceNumber(String gatewayReferenceNumber)

```

Parameters

```
   gatewayReferenceNumber
```

Type: String

Unique transaction ID created by the payment gateway.

Return Value

Type: void

##### setGatewayResultCode(gatewayResultCode)

Sets the payment gateway’s result code.

Signature

```
   global void setGatewayResultCode(String gatewayResultCode)

```

Parameters

```
   gatewayResultCode
```

Type: String

The gateway result code. Must be mapped to a Salesforce result code.

Return Value

Type: void

##### setGatewayResultCodeDescription(gatewayResultCodeDescription)

Sets the payment gateway’s result code description.

Signature

```
   global void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Description of the `GatewayResultCode` . Provides more information about the result code returned by the gateway.


### Apex Reference Guide RefundRequest Class

Return Value

Type: void

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Set the Salesforce result code info.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: commercepayments.SalesforceResultCodeInfo on page 519

Describes the Salesforce result code value.

Return Value

Type: void

### RefundRequest Class

Sends data related to a refund to the payment gateway adapter.

Namespace

CommercePayments on page 489

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.RefundRequest rrq = new CommercePayments.RefundRequest();

```

Example

```
   commercepayments.ReferencedRefundRequest refundRequest = new

   commercepayments.ReferencedRefundRequest(80, pmt.id);

```

IN THIS SECTION:

#### RefundRequest Methods RefundRequest Methods

### The following are methods for RefundRequest .


### Apex Reference Guide RequestType Enum

IN THIS SECTION:

##### equals(obj)

Maintains the integrity of lists of type `RefundRequest` by determining the equality of external objects in a list. This method is
dynamic and is based on the equals method in Java.

##### hashCode()

Maintains the integrity of lists of type `RefundRequest` by determining the uniqueness of the external object records in a list.

##### equals(obj)

Maintains the integrity of lists of type `RefundRequest` by determining the equality of external objects in a list. This method is
dynamic and is based on the equals method in Java.

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

Return Value

Type: Boolean

##### hashCode()

Maintains the integrity of lists of type `RefundRequest` by determining the uniqueness of the external object records in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

### RequestType Enum

Defines the type of payment transaction request made to the payment gateway.

Enum Values

The following are the values of the `commercepayments.RequestType` enum.

**Value** **Description**

`Authorize` Payment authorization request


### Apex Reference Guide RetryCategory Enum

**Value** **Description**

`PostAuth` Post authorization request

`Capture` Payment capture request

`AuthorizationReversal` Authorization Reversal request

`ReferencedRefund` Payment refund request

`Sale` Sale request

```
    commercepayments.RequestType,

    Sale

```

`Tokenize` Payment tokenize request

```
    commercepayments.RequestType,

    Tokenize

### RetryCategory Enum

```

Specifies the retry category.

Enum Values

The following are the values of the `commercepayments.RetryCategory` enum.

**Value** **Description**

`CardLimit` Insufficient funds, exceeded spending limits, or other restrictions on the card.

`GatewayConnection` Connectivity or communication errors between systems, including upstream gateway
errors.

`PaymentInformation` Missing or incorrect data such as incorrect card numbers, addresses, or currencies.

`PaymentProcessing` Payment account is invalid, closed, restricted, or the transaction was declined for
reasons other than insufficient funds.

`Security` Security violations or issues such as fraud, risk, authentication, verification, and
authorization.

`Unknown` The payment gateway error code isn't recognized or isn't mapped to a specific
category.

### RetryDecision Enum

Specifies the retry decision.


### Apex Reference Guide SaleApiPaymentMethodRequest Class

Enum Values

The following are the values of the `commercepayments.RetryDecision` enum.

**Value** **Description**

`NonRetriable` The payment operation cannot be retried.

`Retriable` The payment operation can be retried.

### SaleApiPaymentMethodRequest Class

Sends data related to a card payment method to a gateway adapter during a sale service call.

Namespace

CommercePayments on page 317

Usage

### This class holds information about a payment method that was used for a Sale request. SaleApiPaymentMethodRequest

contains all the possible payment methods as fields, but only one value is populated for a given request. Gateway adapters use this class
when constructing a sale request. The object of this class is obtained through the `paymentMethod` field on the `SaleRequest`
object.

### Example: This code sample retrieves the SaleApiPaymentMethodRequest object from the SaleRequest class.

```
      commercepayments.SaleApiPaymentMethodRequest paymentMethod = saleRequest.paymentMethod;

```

IN THIS SECTION:

#### SaleApiPaymentMethodRequest Constructors

SaleApiPaymentMethodRequest Properties

SaleApiPaymentMethodRequest Methods

#### SaleApiPaymentMethodRequest Constructors

### The following are constructors for SaleApiPaymentMethodRequest .

IN THIS SECTION:

SaleApiPaymentMethodRequest(cardPaymentMethodRequest)
Sends data related to a card payment method to a gateway adapter during a sale service call.

SaleApiPaymentMethodRequest()
Constructor for building a sale payment method request. This constructor is intended for test usage and throws an exception if used
outside of the Apex test context.


Apex Reference Guide SaleApiPaymentMethodRequest Class

##### SaleApiPaymentMethodRequest(cardPaymentMethodRequest)

Sends data related to a card payment method to a gateway adapter during a sale service call.

Signature

```
   global SaleApiPaymentMethodRequest(commercepayments.CardPaymentMethodRequest

##### `cardPaymentMethodRequest)`

```

Parameters

##### _`cardPaymentMethodRequest`_

Type: CardPaymentMethodRequest on page 404

##### SaleApiPaymentMethodRequest()

Constructor for building a sale payment method request. This constructor is intended for test usage and throws an exception if used
outside of the Apex test context.

Signature

```
   global SaleApiPaymentMethodRequest()

#### SaleApiPaymentMethodRequest Properties

##### The following are properties for SaleApiPaymentMethodRequest .

```

IN THIS SECTION:

##### cardPaymentMethod

Contains details of the card used in a payment method.

##### standardEntryClassCode

Contains details of the standard entry class code used in a payment method.

##### cardPaymentMethod

Contains details of the card used in a payment method.

Signature

```
   global commercepayments.CardPaymentMethodRequest cardPaymentMethod {get; set;}

```

Property Value

Type: CardPaymentMethodRequest on page 404

##### **`standardEntryClassCode`**

Contains details of the standard entry class code used in a payment method.


Apex Reference Guide SaleApiPaymentMethodRequest Class

Signature

```
   public commercepayments.StandardEntryClassCode standardEntryClassCode {get; set;}

```

Property Value

Type: commercepayments.StandardEntryClassCode on page 520

#### SaleApiPaymentMethodRequest Methods The following are methods for SaleApiPaymentMethodRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type SaleApiPaymentMethodRequest by determining the equality of external objects in

a list. This method is dynamic and is based on the equals method in Java.

##### hashCode()
#### Maintains the integrity of lists of type SaleApiPaymentMethodRequest by determining the uniqueness of the external

object records in a list.

toString()
Converts a date to a string.

##### equals(obj)

#### Maintains the integrity of lists of type SaleApiPaymentMethodRequest by determining the equality of external objects in a

list. This method is dynamic and is based on the equals method in Java.

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

Return Value

Type: Boolean

##### hashCode()

#### Maintains the integrity of lists of type SaleApiPaymentMethodRequest by determining the uniqueness of the external object

records in a list.

Signature

```
   global Integer hashCode()

```


### Apex Reference Guide SaleNotification Class

Return Value

Type: Integer

##### toString()

Converts a date to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### SaleNotification Class When a payment gateway sends a notification for a sale payment, the payment gateway adapter creates the SaleNotification

object to store information about notification.

Namespace

CommercePayments on page 317

Usage

### SaleNotification is used in asynchronous payment gateway adapters. Specify the CommercePayments namespace when

creating an instance of this class. The constructor of this class takes no arguments. For example:

```
   commercePayments.SaleNotification saleNotification = new

   commercepayments.SaleNotification();

```

Example

```
   global commercepayments.GatewayNotificationResponse

   processNotification(commercepayments.PaymentGatewayNotificationContext

   gatewayNotificationContext) {

      commercepayments.PaymentGatewayNotificationRequest gatewayNotificationRequest =

   gatewayNotificationContext.getPaymentGatewayNotificationRequest();

      Blob request = gatewayNotificationRequest.getRequestBody();

      AdyenNotificationRequest notificationRequest =

   AdyenNotificationRequest.parse(request.toString().replace('currency', 'currencyCode'));

      List < AdyenNotificationRequest.NotificationItems > notificationItems =

   notificationRequest.notificationItems;

      AdyenNotificationRequest.NotificationRequestItem notificationRequestItem =

   notificationItems[0].NotificationRequestItem;

      Boolean success = Boolean.valueOf(notificationRequestItem.success);

      String pspReference = notificationRequestItem.pspReference;

      String eventCode = notificationRequestItem.eventCode;

```


Apex Reference Guide SaleNotification Class

```
      Double amount = notificationRequestItem.amount.value;

      String reason = notificationRequestItem.reason;

      Datetime eventDate = notificationRequestItem.eventDate;

      commercepayments.NotificationStatus notificationStatus = null;

      if (success) {

        notificationStatus = commercepayments.NotificationStatus.Success;

      } else {

        notificationStatus = commercepayments.NotificationStatus.Failed;

      }

      commercepayments.BaseNotification notification = null;

      if ('AUTHORISATION'.equals(eventCode) && amount > 0) {

        notification = new commercepayments.SaleNotification();

        notification.setGatewayReferenceNumber(pspReference);

      } else {

        system.debug('handling unknown event : ' + eventCode);

        commercepayments.GatewayNotificationResponse unknownEventResponse = new

   commercepayments.GatewayNotificationResponse();

        unknownEventResponse.setStatusCode(200);

        unknownEventResponse.setResponseBody(Blob.valueOf('[not allowed]'));

        return unknownEventResponse;

      }

      notification.setStatus(notificationStatus);

      notification.setAmount(amount / 100);

      notification.setGatewayResultCodeDescription(reason);

      notification.setGatewayDate(eventDate);

      commercepayments.NotificationSaveResult saveResult =

   commercepayments.NotificationClient.record(notification);

      commercepayments.GatewayNotificationResponse gnr = new

   commercepayments.GatewayNotificationResponse();

      if (saveResult.isSuccess()) {

        gnr.setStatusCode(200);

      } else {

        gnr.setStatusCode(400);

      }

      gnr.setResponseBody(Blob.valueOf(saveResult.toString()));

      return gnr;

   }

```

IN THIS SECTION:

#### SaleNotification Methods SaleNotification Methods The following are methods for SaleNotification .


Apex Reference Guide SaleNotification Class

IN THIS SECTION:

##### setAmount(amount)

Sets the amount for the sale payment.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the sale occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the sale request. Maximum length of 255 characters.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets additional data that you can use for the sale payment. You can use any data that isn’t normalized in financial entities. This field
has a maximum length of 1000 characters and can store data as JSON or XML.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the unique gateway reference number for the transaction that the gateway returned. Maximum length of 255 characters.

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

setId(id)
Sets the ID of a notification sent by the payment gateway.

setRetryCategory(retryCategory)
Sets the retry category returned by the payment gateway for the failed payment.

setRetryDecision(retryDecision)
Sets the retry decision.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

setStatus(status)
Sets the notification status value on the notification object.

##### **`setAmount(amount)`**

Sets the amount for the sale payment.

Signature

```
   public void setAmount(Double amount)

```

Parameters

```
   amount
```

Type: Double


Apex Reference Guide SaleNotification Class

Return Value

Type: void

##### **`setGatewayAvsCode(gatewayAvsCode)`**

Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

Signature

```
   public void setGatewayAvsCode(String gatewayAvsCode)

```

Parameters

```
   gatewayAvsCode
```

Type: String

Used to verify the address mapped to a payment method when the payments platform requests tokenization from the payment
gateway.

Return Value

Type: void

##### **`setGatewayDate(gatewayDate)`**

Sets the date that the sale occurred. Some gateways don’t send this value.

Signature

```
   public void setGatewayDate(Datetime gatewayDate)

```

Parameters

```
   gatewayDate
```

Type: Datetime

Return Value

Type: void

##### **`setGatewayMessage(gatewayMessage)`**

Sets error messages that the gateway returned for the sale request. Maximum length of 255 characters.

Signature

```
   public void setGatewayMessage(String gatewayMessage)

```


Apex Reference Guide SaleNotification Class

Parameters

```
   gatewayMessage
```

Type: String

Return Value

Type: void

##### **`setGatewayReferenceDetails(gatewayReferenceDetails)`**

Sets additional data that you can use for the sale payment. You can use any data that isn’t normalized in financial entities. This field has
a maximum length of 1000 characters and can store data as JSON or XML.

Signature

```
   public void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String

Return Value

Type: void

##### **`setGatewayReferenceNumber(gatewayReferenceNumber)`**

Sets the unique gateway reference number for the transaction that the gateway returned. Maximum length of 255 characters.

Signature

```
   public void setGatewayReferenceNumber(String gatewayReferenceNumber)

```

Parameters

```
   gatewayReferenceNumber
```

Type: String

Return Value

Type: void

##### **`setGatewayResultCode(gatewayResultCode)`**

Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

Signature

```
   public void setGatewayResultCode(String gatewayResultCode)

```


Apex Reference Guide SaleNotification Class

Parameters

```
   gatewayResultCode
```

Type: String

Return Value

Type: void

##### **`setGatewayResultCodeDescription(gatewayResultCodeDescription)`**

Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

Signature

```
   public void setGatewayResultCodeDescription(String gatewayResultCodeDescription)

```

Parameters

```
   gatewayResultCodeDescription
```

Type: String

Description of the gateway’s result code. Use this field to learn more about why the gateway returned a certain result code.

Return Value

Type: void

##### **`setId(id)`**

Sets the ID of a notification sent by the payment gateway.

Signature

```
   public void setId(String id)

```

Parameters

```
   id
```

Type: String

Return Value

Type: void

##### **`setRetryCategory(retryCategory)`**

Sets the retry category returned by the payment gateway for the failed payment.

Signature

```
   public void setRetryCategory(commercepayments.RetryCategory retryCategory)

```


Apex Reference Guide SaleNotification Class

Parameters

```
   retryCategory
```

Type: commercepayments.RetryCategory

Specifies the payment failure category used to determine retry eligibility.

Return Value

Type: void

##### **`setRetryDecision(retryDecision)`**

Sets the retry decision.

Signature

```
   public void setRetryDecision(commercepayments.RetryDecision retryDecision)

```

Parameters

```
   retryDecision
```

Type: commercepayments.RetryDecision

Determines whether the payment operation can be retried based on the retry category.

Return Value

Type: void

##### **`setSalesforceResultCodeInfo(salesforceResultCodeInfo)`**

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce uses
the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Signature

```
   public void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```

Parameters

```
   salesforceResultCodeInfo
```

Type: commercepayments.SalesforceResultCodeInfo on page 518

Return Value

Type: void

##### **`setStatus(status)`**

Sets the notification status value on the notification object.


### Apex Reference Guide SaleRequest Class

Signature

```
   public void setStatus(commercepayments.NotificationStatus status)

```

Parameters

```
   status
```

Type: commercepayments.NotificationStatus on page 432

Return Value

Type: void

### SaleRequest Class

Stores information about a sales request.

Namespace

CommercePayments on page 317

Usage

This class holds all the required details about a sale request. Gateway adapters read the fields of this class object while constructing a
sale JSON request thatis sent to the payment gateway. The object of this class is made available through
`commercepayments.paymentGatewayContext` by calling `getPaymentRequest()` .

Example

```
      /**

      * Responsibilities:

      * - Set merchant and reference details

      * - Convert amount into minor units (e.g., cents)

      * - Map payment method types (card, ACH, SEPA, etc.)

      * - Include stored payment method token for recurring payments

      * - Optionally include enhanced Level 2/3 data

      *

      * @param saleRequest Input request containing payment and shopper details

      * @return JSON string payload for the payment gateway

      */

      private String buildSaleRequest(commercepayments.SaleRequest saleRequest) {

        // Resolve currency (fallback to user's default if missing)

        String currencyIso = saleRequest.currencyIsoCode;

        if (currencyIso == null) {

           currencyIso = UserInfo.getDefaultCurrency();

        }

        // Extract payment method

        commercepayments.SaleApiPaymentMethodRequest paymentMethod =

```


Apex Reference Guide SaleRequest Class

```
   saleRequest.paymentMethod;

        // Initialize JSON generator

        JSONGenerator jsonGeneratorInstance = JSON.createGenerator(true);

        jsonGeneratorInstance.writeStartObject();

        // Merchant configuration (from Named Credential)

       jsonGeneratorInstance.writeStringField('merchantAccount', '{!$Credential.Username}');

        // Unique reference using timestamp + random suffix

        jsonGeneratorInstance.writeStringField(

           'reference',

           String.valueOf(Datetime.now().getTime()) +

           String.valueOf(Math.random()).substring(2, 8)

        );

        // Amount block

        jsonGeneratorInstance.writeFieldName('amount');

        jsonGeneratorInstance.writeStartObject();

        jsonGeneratorInstance.writeStringField(

           'value',

           String.valueOf((saleRequest.amount * 100.0).intValue()) // convert to minor

   units

        );

        jsonGeneratorInstance.writeStringField('currency', currencyIso);

        jsonGeneratorInstance.writeEndObject();

        // Payment method block

        jsonGeneratorInstance.writeFieldName('paymentMethod');

        jsonGeneratorInstance.writeStartObject();

        String shopperReference;

        String type = 'scheme'; // default = card

        // Handle stored payment method data (tokenized payments)

        if (saleRequest.paymentMethodData != null) {

           String token = saleRequest.paymentMethodData.get('gatewayToken');

           String paymentMethodType =

   saleRequest.paymentMethodData.get('paymentMethodType');

           shopperReference = saleRequest.paymentMethodData.get('gatewayReference');

           // Map payment method types to gateway-specific values

           if ('us_bank_account'.equals(paymentMethodType)) {

             type = 'ach';

           } else if ('sepa_debit'.equals(paymentMethodType)) {

             type = 'sepadirectdebit';

           } else if ('au_becs_debit'.equals(paymentMethodType)) {

             type = 'directdebit_AU';

           } else if ('bacs_debit'.equals(paymentMethodType)) {

             type = 'directdebit_GB';

           }

```


Apex Reference Guide SaleRequest Class

```
           jsonGeneratorInstance.writeStringField('type', type);

           jsonGeneratorInstance.writeStringField('storedPaymentMethodId', token);

        }

        // Add enhanced scheme data ONLY for card payments

        // Note: Gateway might have validations on L2/L3 data so do test them out before

   using L2/L3 else transactions might fail

        if (enhancedPaymentData != null && 'scheme'.equals(type)) {

           jsonGeneratorInstance.writeFieldName('additionalData');

           jsonGeneratorInstance.writeStartObject();

           populateEnhancedSchemeData(jsonGeneratorInstance, enhancedPaymentData);

           jsonGeneratorInstance.writeEndObject(); // additionalData

        }

        jsonGeneratorInstance.writeEndObject(); // paymentMethod

        // Recurring / shopper configuration

        jsonGeneratorInstance.writeStringField('shopperInteraction', 'ContAuth');

        jsonGeneratorInstance.writeStringField('recurringProcessingModel',

   'UnscheduledCardOnFile');

        jsonGeneratorInstance.writeStringField('shopperReference', shopperReference);

        // Immediate capture

        jsonGeneratorInstance.writeNumberField('captureDelayHours', 0);

        jsonGeneratorInstance.writeEndObject(); // root

        return jsonGeneratorInstance.getAsString();

      }

      /**

      * Populates Level 2 and Level 3 enhanced scheme data.

      *

      * @param jsonGeneratorInstance JSON generator

      * @param enhancedPaymentData Enhanced payment data input

      */

      private void populateEnhancedSchemeData(JSONGenerator jsonGeneratorInstance,

                              commercepayments.EnhancedPaymentDataInput

   enhancedPaymentData) {

        // -------- Level 2 fields -------
        if (enhancedPaymentData.totalTaxAmount != null) {

           jsonGeneratorInstance.writeStringField(

             'enhancedSchemeData.totalTaxAmount',

             toMinorUnits(enhancedPaymentData.totalTaxAmount)

           );

        }

        if (enhancedPaymentData.shippingAmount != null) {

           jsonGeneratorInstance.writeStringField(

             'enhancedSchemeData.freightAmount',

             toMinorUnits(enhancedPaymentData.shippingAmount)

           );

```


Apex Reference Guide SaleRequest Class

```
        }

        if (enhancedPaymentData.discountAmount != null) {

           jsonGeneratorInstance.writeStringField(

             'enhancedSchemeData.discountAmount',

             toMinorUnits(enhancedPaymentData.discountAmount)

           );

        }

        if (enhancedPaymentData.invoiceNumber != null) {

           jsonGeneratorInstance.writeStringField(

             'enhancedSchemeData.customerReference',

             enhancedPaymentData.invoiceNumber

           );

        }

        // -------- Level 3 fields (line items) -------
        if (enhancedPaymentData.lineItems != null) {

           Integer index = 1;

           for (commercepayments.LineItemInput item : enhancedPaymentData.lineItems) {

             populateLineItemData(

               jsonGeneratorInstance,

               item,

               'enhancedSchemeData.itemDetailLine' + index + '.'

             );

             index++;

           }

        }

        // Shipping / destination info

        if (enhancedPaymentData.shipFromZip != null) {

           jsonGeneratorInstance.writeStringField(

             'enhancedSchemeData.shipFromPostalCode',

             enhancedPaymentData.shipFromZip

           );

        }

        if (enhancedPaymentData.shipToZip != null) {

           jsonGeneratorInstance.writeStringField(

             'enhancedSchemeData.destinationPostalCode',

             enhancedPaymentData.shipToZip

           );

        }

        if (enhancedPaymentData.shipToCountry != null) {

           jsonGeneratorInstance.writeStringField(

             'enhancedSchemeData.destinationCountryCode',

             enhancedPaymentData.shipToCountry

           );

        }

      }

```


Apex Reference Guide SaleRequest Class

```
      /**

      * Populates Level 3 line item data.

      *

      * @param jsonGeneratorInstance JSON generator

      * @param item Line item input

      * @param prefix Field prefix for indexed items

      */

      private void populateLineItemData(JSONGenerator jsonGeneratorInstance,

                          commercepayments.LineItemInput item,

                          String prefix) {

        if (item.sku != null) {

           jsonGeneratorInstance.writeStringField(prefix + 'productCode', item.sku);

        }

        if (item.name != null) {

           jsonGeneratorInstance.writeStringField(prefix + 'description', item.name);

        }

        if (item.quantity != null) {

           jsonGeneratorInstance.writeStringField(prefix + 'quantity',

   String.valueOf(item.quantity));

        }

        // Unit price is always written

        jsonGeneratorInstance.writeStringField(

           prefix + 'unitPrice',

           toMinorUnits(item.unitPrice)

        );

        if (item.taxAmount != null) {

           jsonGeneratorInstance.writeStringField(

             prefix + 'taxAmount',

             toMinorUnits(item.taxAmount)

           );

        }

        if (item.discount != null) {

           jsonGeneratorInstance.writeStringField(

             prefix + 'discountAmount',

             toMinorUnits(item.discount)

           );

        }

        if (item.commodityCode != null) {

           jsonGeneratorInstance.writeStringField(prefix + 'commodityCode',

   item.commodityCode);

        }

        if (item.uom != null) {

           jsonGeneratorInstance.writeStringField(prefix + 'unitOfMeasure', item.uom);

        }

      }

```


Apex Reference Guide SaleRequest Class

```
      /**

      * Converts amount to minor units (e.g., dollars →cents).

      *

      * @param amount Decimal amount

      * @return String representation of minor units

      */

      private static String toMinorUnits(Decimal amount) {

        if (amount == null) return null;

        Decimal value = (amount * 100)

           .setScale(0, System.RoundingMode.HALF_UP);

        return String.valueOf(value.intValue());

      }

```

IN THIS SECTION:

#### SaleRequest Constructors SaleRequest Properties

SaleRequest Methods

#### SaleRequest Constructors The following are constructors for SaleRequest .

IN THIS SECTION:

##### SaleRequest(amount)

Constructor for defining an amount for the sale request. This constructor is intended for test usage and throws an exception if used
outside of the Apex test context.

##### SaleRequest(amount)

Constructor for defining an amount for the sale request. This constructor is intended for test usage and throws an exception if used
outside of the Apex test context.

Signature

```
   global SaleRequest(Double amount)

```

Parameters

```
   amount
```

Type: Double

Amount of the sale request.

#### SaleRequest Properties The following are properties for SaleRequest .


Apex Reference Guide SaleRequest Class

IN THIS SECTION:

##### accountId

Customer account ID for the sale request.

##### amount

Amount of the sale request. Can be positive only.

comments
Additional information about the sale request.

currencyIsoCode
Currency code for the sale request.

enhancedPaymentData
Represents enhanced payment data, including Level 2 and Level 3 fields.

paymentInitiationSourceId
ID of the source that initiated the payment.

paymentMethod
Payment method used in the sale request.

paymentMethodData
Payment method data used in the sale request.

submittedByMerchant
Indicates whether the sale request is submitted by the marchant ( `true` ) or not ( `false` ).

##### accountId

Customer account ID for the sale request.

Signature

```
   global String accountId {get; set;}

```

Property Value

Type: String

##### amount

Amount of the sale request. Can be positive only.

Signature

```
   global Double amount {get; set;}

```

Property Value

Type: Double


Apex Reference Guide SaleRequest Class

##### comments

Additional information about the sale request.

Signature

```
   global String comments {get; set;}

```

Property Value

Type: String

##### currencyIsoCode

Currency code for the sale request.

Signature

```
   global String currencyIsoCode {get; set;}

```

Property Value

Type: String

##### **`enhancedPaymentData`**

