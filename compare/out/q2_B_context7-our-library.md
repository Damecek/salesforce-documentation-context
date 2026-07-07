# Q2: How do I configure an OAuth 2.0 JWT bearer token flow for a connected app in Salesforce?

## Approach: B_context7-our-library
- latency: 9438 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### JWT Bearer Token Exchange Example

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-reference-guide-part-01.md

Example demonstrating the JWT bearer token flow, including creating a JWT, signing it, and exchanging it for an access token.

```Apex
public class MyController{

      public MyController() {

        Auth.JWT jwt = new Auth.JWT();

        jwt.setSub('user@salesforce.com');

        jwt.setAud('https://login.salesforce.com');

        jwt.setIss('3MVG99OxTyEMCQ3gNp2PjkqeZKxnmAiG1xV4oHh9AKL_rSK.BoSVPGZHQ

   ukXnVjzRgSuQqGn75NL7yfkQcyy7');

        //Additional claims to set scope

        Map<String, Object> claims = new Map<String, Object>();

        claims.put('scope', 'scope name');

        jwt.setAdditionalClaims(claims);

        //Create the object that signs the JWT bearer token

        Auth.JWS jws = new Auth.JWS(jwt, 'CertFromCertKeyManagement');

        //Get the resulting JWS in case debugging is required

        String token = jws.getCompactSerialization();

        //Set the token endpoint that the JWT bearer token is posted to

        String tokenEndpoint = 'https://login.salesforce.com/services/oauth2/token';

        //POST the JWT bearer token

        Auth.JWTBearerTokenExchange bearer = new Auth.JWTBearerTokenExchange(tokenEndpoint,

    jws);

        //Get the access token

        String accessToken = bearer.getAccessToken();

      }

   }
```

--------------------------------

### OAuth 2.0 Token Exchange Handler Implementation

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-03.md

This example shows a basic implementation of the Auth.Oauth2TokenExchangeHandler class. It includes logic for validating JWT, opaque access/refresh tokens, and SAML assertions, returning a TokenValidationResult.

```Apex
/*Token Exchange Handler Implementation Example*/

public class MyTokenExchangeClass extends Auth.Oauth2TokenExchangeHandler{

  public override Auth.TokenValidationResult validateIncomingToken(String appDeveloperName,

 Auth.IntegratingAppType appType, String incomingToken, Auth.OAuth2TokenExchangeType

 tokenType) {

        //Depending on your incoming token, you validate it in different ways

        //If the incoming token is an opaque access token or refresh token, validate it

   with a callout to the identity provider

        //If it’s a SAML assertion, validate it by checking the XML

        //If it’s an ID Token or JWT, try using our JWT validation methods

        //This example assumes that the incoming token is a JWT and that there is a public

    keys endpoint on the identity provider

        //Be very careful with any logic in this method, and test carefully before using

        Boolean isValid = false;

        Auth.JWT jwt;

        //Custom data structure

        CustomStructuredUserData customData;

        //Standard user data structure

        Auth.UserData userData;

        if (tokenType == Auth.OAuth2TokenExchangeType.JWT || tokenType ==

   Auth.OAuth2TokenExchangeType.ID_TOKEN) {

           try {

             jwt = Auth.JWTUtil.validateJWTWithKeysEndpoint(incomingToken,

   'https://your-idp.com/keys', true);

             isValid = true;

             //These values are sourced from the JWT or ID Token

             userData = new Auth.UserData('identifier', 'firstName', 'lastName',

   'fullName', 'customer@email.com', 'link url', 'remote username', 'local', 'Provider (IDP

   Name)', '', new Map<String,String>());

             //You can also pass data as generic object

             customData = new CustomStructuredUserData();

           } catch (Exception e) {

             isValid = false;

           }

        } else if (tokenType == Auth.OAuth2TokenExchangeType.ACCESS_TOKEN || tokenType ==

    Auth.OAuth2TokenExchangeType.REFRESH_TOKEN) {

           //Putlogic for validating an opaque access token or refresh token here

          //This validation typically involves a callout to the introspect or user info

    endpoints

           //If you call out to the user info endpoint, make sure to pass the data from

   the validation into the getUserForTokenSubject method using an Apex class or the user data

    class

           isValid = false;

        } else if (tokenType == Auth.OAuth2TokenExchangeType.SAML_2) {

           //Put logic for validating a SAML assertion here

           //This validation involves XML parsing

           isValid = false;

        } else {

           //You can add new token types. If you don’t know how to validate the token,

   always check the type and return false

           isValid = false;

        }

        if(isValid){

           return new Auth.TokenValidationResult(true, (object)customData, userData,

   incomingToken, tokenType, 'CustomErrorMessage');

        } else {

           return new Auth.TokenValidationResult(isValid);

        }


```

--------------------------------

### Log in to an Org Using JWT Bearer Flow

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/salesforce-dx-developer-guide-part-01.md

Ideal for CI or automated environments where interactive login is not possible. This is the OAuth 2.0 JWT bearer flow.

```bash
sf org login jwt
```

--------------------------------

### Login to Org using JWT Flow

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/salesforce-dx-developer-guide-part-01.md

Use this command to log in to a Salesforce org using the JWT flow, suitable for CI/CD pipelines. Specify the client ID, JWT key file path, username, and an alias for easy reference.

```bash
sf org login jwt --client-id 04580y4051234051 --jwt-key-file /Users/jdoe/JWT/server.key
--username jdoe@myorg.com --alias my-hub-org
```

### Create an External Client App in Your Org

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/salesforce-dx-developer-guide-part-01.md

Select the following OAuth scopes when creating an external client app: Manage user data via APIs (api), Manage user data via Web browsers (web), and Perform requests at any time (refresh_token, offline_access). For JWT Bearer Flow, enable the `Enable JWT Bearer Flow` option and upload your digital certificate file.
