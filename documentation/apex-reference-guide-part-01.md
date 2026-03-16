# Apex Reference Guide

> Source: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/salesforce_apex_reference_guide.pdf
> Fetched: 2026-03-16T10:00:11Z
Apex Reference Guide

Version 66.0, Spring ’26

Last updated: March 13, 2026

© Copyright 2000–2026 Salesforce, Inc. All rights reserved. Salesforce is a registered trademark of Salesforce, Inc., as are other
names and marks. Other marks appearing herein may be trademarks of their respective owners.

CONTENTS

Apex Reference Guide **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**

Release Notes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5**
Apex DML Operations **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5**

Apex DML Statements **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5**
ApexPages Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10**

Action Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10**
Component Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12**
IdeaStandardController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14**
IdeaStandardSetController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16**
KnowledgeArticleVersionStandardController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . 19**
Message Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23**
StandardController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27**
StandardSetController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32**
AppLauncher Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43**

AppMenu Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43**
ChangePasswordController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45**
CommunityLogoController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45**
EmployeeLoginLinkController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
ForgotPasswordController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
IdentityHeaderController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
LoginFormController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
SelfRegisterController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
SocialLoginController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
Approval Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47**

LockResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47**
ProcessRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49**
ProcessResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51**
ProcessSubmitRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53**
ProcessWorkitemRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57**
UnlockResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59**
Auth Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62**

AuthConfiguration Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65**
AuthProviderCallbackState Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76**
AuthProviderPlugin Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78**
AuthProviderPluginClass Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81**
AuthProviderTokenResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91**
AuthToken Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94**
CommunitiesUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99**
ConfigurableSelfRegHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101**

**Contents**

ConfirmUserRegistrationHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106**
ConnectedAppPlugin Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108**
CustomOneTimePasswordDeliveryHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . 115**
CustomOneTimePasswordDeliveryResult Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117**
ExternalClientAppOauthHandler Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118**
GeneratedUserData Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120**
HeadlessSelfRegistrationHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125**
HeadlessUserDiscoveryHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129**
HeadlessUserDiscoveryResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133**
HttpCalloutMockUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135**
IntegratingAppType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136**
InvocationContext Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136**
JsonValueOutput Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137**
JWS Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141**
JWT Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143**
JWTBearerTokenExchange Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149**
JWTUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154**
LightningLoginEligibility Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157**
LoginDiscoveryHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158**
LoginDiscoveryMethod Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165**
MyDomainLoginDiscoveryHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166**
Oauth2TokenExchangeHandler Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170**
OAuth2TokenExchangeType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172**
OAuthRefreshResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172**
OauthToken Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175**
OauthTokenType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176**
RegistrationHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177**
SamlJitHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182**
SessionManagement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186**
SessionLevel Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198**
TokenValidationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199**
UserData Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205**
VerificationAction Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213**
VerificationMethod Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213**
VerificationPolicy Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214**
VerificationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214**
Auth Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217**
Cache Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219**

CacheBuilder Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220**
Org Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221**
OrgPartition Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239**
Partition Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242**
Session Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257**
SessionPartition Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274**

**Contents**

Cache Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277**
Visibility Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278**
Canvas Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278**

ApplicationContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279**
CanvasLifecycleHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282**
ContextTypeEnum Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285**
EnvironmentContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285**
RenderContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291**
Test Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293**
Canvas Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297**
ChatterAnswers Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 298**

AccountCreator Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 298**
CommerceBuyGrp Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300**

BuyerGroupEvaluationService Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301**
BuyerGroupRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302**
BuyerGroupResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304**
CommerceExtension Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306**

ExtensionInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 307**
Resolution Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309**
ResolutionException Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311**
ResolutionStates Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314**
ResolutionStrategy Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314**
CommerceOrders Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316**
CommercePayments Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316**

AbstractResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 320**
AbstractTransactionResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324**
AccountType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328**
AccountHolderType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329**
AddressRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329**
AlternativePaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 333**
AlternativePaymentMethodResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337**
AuditParamsRequest **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340**
AuthApiPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342**
AuthorizationRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 344**
AuthorizationResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349**
AuthorizationReversalRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 356**
AuthorizationReversalResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 360**
BankType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365**
BankPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365**
BankPaymentMethodResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373**
BaseApiPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 379**
BaseNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 382**
BasePaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 388**
BaseRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 389**

**Contents**

CaptureNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 390**
CaptureRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 396**
CaptureResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 397**
CardCategory Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 402**
CardPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 403**
CardPaymentMethodResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 409**
CardType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 417**
CustomMetadataTypeInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 417**
GatewayErrorResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 418**
GatewayNotificationResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 420**
GatewayResponse Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 422**
NotificationClient Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423**
NotificationSaveResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425**
NotificationStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 426**
PaymentGatewayAdapter Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 427**
PaymentGatewayAsyncAdapter Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 427**
PaymentGatewayContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 431**
PaymentGatewayNotificationContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432**
PaymentGatewayNotificationRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434**
PaymentMethodDetailsResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435**
PaymentMethodIdType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437**
PaymentMethodTokenizationRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437**
PaymentMethodTokenizationResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 442**
PaymentsHttp Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 451**
PostAuthApiPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 452**
PostAuthorizationRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455**
PostAuthorizationResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 457**
ReferencedRefundNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 464**
ReferencedRefundRequest **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 470**
ReferencedRefundResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 472**
RefundRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 476**
RequestType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 478**
RetryCategory Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 478**
RetryDecision Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 479**
SaleApiPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 479**
SaleNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 482**
SaleRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489**
SaleResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 494**
SalesforceResultCode Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 501**
SalesforceResultCodeInfo **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 502**
StandardEntryClassCode Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 503**
TokenizeNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 503**
CommerceTax Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 510**

AbstractTransactionResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512**

**Contents**

AddressesResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 518**
AddressResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 520**
AmountDetailsResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 522**
CalculateTaxRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 524**
CalculateTaxResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 528**
CalculateTaxType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 536**
CustomTaxAttributesResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 536**
ErrorResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 538**
HeaderTaxAddressesRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 539**
ImpositionResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 543**
JurisdictionResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 546**
LineItemResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 549**
LineTaxAddressesRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 555**
RequestType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 559**
ResultCode Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 559**
RuleDetailsResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 560**
TaxAddressesRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 562**
TaxAddressRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 566**
TaxApiException Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 572**
TaxCustomerDetailsRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 573**
TaxDetailsResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 577**
TaxEngineAdapter Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 584**
TaxEngineContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 610**
TaxLineItemRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 613**
TaxSellerDetailsRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 619**
TaxTransactionRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 621**
TaxTransactionStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 628**
TaxTransactionType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 629**
ComplianceMgmt Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 629**
Compression Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 629**

Level Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 630**
Method Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 630**
ZipEntry Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 631**
ZipReader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 636**
ZipWriter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 639**
Compression Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 645**
ConnectApi Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 646**

ActionLinks Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 651**
Announcements Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 660**
BotVersionActivation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 665**
CdpActivation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 667**
CdpActivationExternalPlatform Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 672**
CdpActivationTarget Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 673**
CdpAudienceDMO Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 677**

**Contents**

CdpCalculatedInsight Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 678**
CdpConnection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 683**
CdpDataSpace Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 684**
CdpDataStreams Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 686**
CdpIdentityResolution Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 687**
CdpMachineLearning Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 691**
CdpQuery Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 692**
CdpSegment Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 750**
Chatter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 760**
ChatterFavorites Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 766**
ChatterFeeds Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 787**
ChatterGroups Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1190**
ChatterMessages Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1235**
ChatterUsers Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1259**
Clm Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1295**
CommerceBuyerExperience Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1296**
CommerceCart Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1354**
CommerceCatalog Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1404**
CommerceCatalogManagement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1431**
CommercePromotions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1433**
CommerceSearch Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1435**
CommerceSearchConnectFamily Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1439**
CommerceSearchSettings Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1441**
CommerceStorePricing Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1444**
CommerceWishlist Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1450**
Communities Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1469**
CommunityModeration Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1471**
ContentHub Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1500**
ConversationApplicationDefinition Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1575**
Datacloud Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1576**
EinsteinLLM Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1581**
EmailMergeFieldService Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1585**
EmployeeProfiles Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1585**
Exchanges Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1594**
ExtendedCommerceDelivery Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1596**
ExternalEmailServices Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1597**
ExternalManagedAccount Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1598**
FieldService Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1601**
FlowApprovalProcesses Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1603**
FulfillmentOrder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1604**
IBusinessObjectivesAndRecsFamily Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1609**
Knowledge Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1614**
LightningScheduler Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1619**
ManagedContent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1624**

**Contents**

ManagedContentChannels Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1656**
ManagedContentDelivery Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1660**
ManagedContentSpaces Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1685**
ManagedTopics Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1690**
MarketingIntegration Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1704**
Mentions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1706**
Missions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1712**
NamedCredentials Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1717**
NavigationMenu Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1735**
NextBestAction Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1739**
OmnichannelInventoryService Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1745**
OMSAnalytics Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1753**
Orchestration Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1758**
OrderPaymentSummary Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1761**
OrderSummary Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1762**
OrderSummaryCreation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1775**
Organization Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1776**
PardotBusinessUnitContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1776**
Payments Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1778**
Personalization Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1783**
PickTicket Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1796**
QuestionAndAnswers Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1797**
Recommendations Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1801**
RecordFilterCriteriaFamily Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1861**
Records Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1862**
RecordUi Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1864**
RegisterGuestBuyer Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1865**
Repricing Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1866**
ReturnOrder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1869**
Routing Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1871**
SalesforceInbox Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1876**
Search Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1877**
Sites Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1887**
SmartDataDiscovery Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1889**
SocialEngagement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1889**
Surveys Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1900**
TaxPlatform Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1901**
Topics Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1902**
UserProfiles Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1939**
Zones Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1949**
ConnectApi Input Classes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1959**
ConnectApi Output Classes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2151**
ConnectApi Enums **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2594**
ConnectApi Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2638**

**Contents**

ConnectApi Utilities **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2638**
ConnectApi Release Notes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2639**
Context Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2640**
Database Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2640**

Batchable Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2641**
BatchableContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2643**
Cursor Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2644**
CursorFetchResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2646**
DeletedRecord Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2648**
DeleteResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2649**
DMLOptions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2651**
DmlOptions.AssignmentRuleHeader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2654**
DMLOptions.DuplicateRuleHeader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2656**
DmlOptions.EmailHeader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2658**
DuplicateError Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2660**
EmptyRecycleBinResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2662**
Error Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2664**
GetDeletedResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2665**
GetUpdatedResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2667**
LeadConvert Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2668**
LeadConvertResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2679**
MergeResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2681**
PaginationCursor Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2683**
QueryLocator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2685**
QueryLocatorIterator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2686**
SaveResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2688**
UndeleteResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2690**
UpsertResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2692**
Datacloud Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2693**

AdditionalInformationMap Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2694**
DuplicateResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2695**
FieldDiff Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2700**
FindDuplicates Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2701**
FindDuplicatesByIds Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2704**
FindDuplicatesResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2706**
MatchRecord Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2709**
MatchResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2711**
DataRetrieval Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2713**
DataSource Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2714**

AsyncDeleteCallback Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2716**
AsyncSaveCallback Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2717**
AuthenticationCapability Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2718**
AuthenticationProtocol Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2718**
Capability Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2719**

**Contents**

Column Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2720**
ColumnSelection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2743**
Connection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2745**
ConnectionParams Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2750**
DataSourceUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2754**
DataType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2755**
DeleteContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2756**
DeleteResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2757**
Filter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2760**
FilterType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2762**
IdentityType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2763**
Order Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2763**
OrderDirection Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2766**
Provider Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2766**
QueryAggregation Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2768**
QueryContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2768**
QueryUtils Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2770**
ReadContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2773**
SearchContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2774**
SearchUtils Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2776**
Table Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2777**
TableResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2781**
TableSelection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2787**
UpsertContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2789**
UpsertResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2790**
DataSource Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2793**
DataWeave Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2793**

Result Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2794**
Script Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2795**
Dom Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2797**

Document Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2798**
XmlNode Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2800**
XmlNodeType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2811**
embeddedai Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2811**

ApexMap Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2811**
RecordApexRepresentation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2814**
EventBus Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2817**

ChangeEventHeader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2818**
EventPublishFailureCallback Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2823**
EventPublishSuccessCallback Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2825**
FailureResult Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2826**
SuccessResult Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2826**
TestBroker Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2827**
TriggerContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2829**

**Contents**

ExternalService Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2832**
Flow Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2832**

Interview Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2832**
Flowtesting Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2837**
flowuiruntime Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2837**

ComplexObjectFieldDetails Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2837**
PropertyTypeDetails Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2837**
ToastLink Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2838**
FormulaEval Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2838**

FormulaBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2838**
FormulaGlobal Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2843**
FormulaInstance Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2844**
FormulaReturnType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2846**
fsccashflow Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2846**

FSCCashFlowUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2847**
Functions Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2857**

Function Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2858**
FunctionCallback Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2862**
FunctionErrorType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2863**
FunctionInvocation Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2864**
FunctionInvocationError Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2866**
FunctionInvocationStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2868**
FunctionInvokeMock Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2868**
MockFunctionInvocationFactory Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2871**
ise_bots_apex Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2873**

DynamicMenuItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2873**
industriesNlpSvc **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2877**

NlpResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2877**
NlpSummarizationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2878**
IndustriesDigitalLending Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2879**
Invocable Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2880**

Action Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2880**
Action.Error Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2886**
Action.Result Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2888**
InvoiceWriteOff Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2890**
IsvPartners Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2890**

AppAnalytics Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2890**
KbManagement Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2893**

PublishingService Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2893**
LxScheduler Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2904**

GetAppointmentCandidatesInput Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2905**
GetAppointmentCandidatesInputBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 2907**
GetAppointmentSlotsInput Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2915**
GetAppointmentSlotsInputBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2917**

**Contents**

SchedulerResources Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2924**
SkillRequirement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2929**
SkillRequirementBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2929**
WorkType Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2931**
WorkTypeBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2931**
ServiceResourceScheduleHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2935**
ServiceAppointmentRequestInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2938**
ServiceResourceInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2942**
ServiceResourceSchedule Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2945**
UnavailableTimeslot Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2947**
Messaging Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2949**

AttachmentRetrievalOption Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2950**
Email Class (Base Email Methods) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2950**
EmailFileAttachment Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2954**
InboundEmail Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2956**
InboundEmail.AuthenticationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2962**
InboundEmail.AuthenticationResultField Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 2964**
InboundEmail.BinaryAttachment Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2965**
InboundEmail.TextAttachment Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2967**
InboundEmailResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2970**
InboundEnvelope Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2971**
MassEmailMessage Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2972**
InboundEmail.Header Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2975**
PushNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2976**
PushNotificationPayload Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2979**
CustomNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2982**
RenderEmailTemplateBodyResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2989**
RenderEmailTemplateError Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2990**
SendEmailError Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2992**
SendEmailResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2993**
SingleEmailMessage Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2994**
Metadata Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3011**

AnalyticsCloudComponentLayoutItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3014**
ConsoleComponent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3018**
Container Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3020**
CustomConsoleComponents Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3023**
CustomMetadata Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3025**
CustomMetadataValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3027**
DeployCallback Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3029**
DeployCallbackContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3031**
DeployContainer Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3032**
DeployDetails Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3035**
DeployMessage Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3036**
DeployProblemType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3041**

**Contents**

DeployResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3042**
DeployStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3050**
FeedItemTypeEnum Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3050**
FeedLayout Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3052**
FeedLayoutComponent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3055**
FeedLayoutComponentType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3057**
FeedLayoutFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3058**
FeedLayoutFilterPosition Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3060**
FeedLayoutFilterType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3060**
Layout Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3060**
LayoutColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3068**
LayoutHeader Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3070**
LayoutItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3070**
LayoutSection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3075**
LayoutSectionStyle Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3078**
Metadata Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3078**
MetadataType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3079**
MetadataValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3080**
MiniLayout Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3080**
Operations Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3082**
PlatformActionList Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3086**
PlatformActionListContextEnum Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3088**
PlatformActionListItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3089**
PlatformActionTypeEnum Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3091**
PrimaryTabComponents Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3091**
QuickActionList Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3093**
QuickActionListItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3094**
RelatedContent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3095**
RelatedContentItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3096**
RelatedList Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3098**
RelatedListItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3099**
ReportChartComponentLayoutItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3102**
ReportChartComponentSize Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3106**
SidebarComponent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3106**
SortOrder Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3110**
StatusCode Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3111**
SubtabComponents Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3111**
SummaryLayoutStyleEnum Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3113**
SummaryLayout Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3113**
SummaryLayoutItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3116**
UiBehavior Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3118**
PlaceQuote Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3119**
Pref_center Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3119**

LoadFormData Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3119**

**Contents**

LoadParameters Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3126**
PreferenceCenterApexHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3127**
SubmitFormData Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3128**
SubmitParameters Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3132**
TokenType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3133**
TokenUtility Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3133**
ValidationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3136**
Process Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3136**

Plugin Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3137**
PluginDescribeResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3139**
PluginDescribeResult.InputParameter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3141**
PluginDescribeResult.OutputParameter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3145**
PluginDescribeResult.ParameterType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3147**
PluginRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3148**
PluginResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3149**
QuickAction Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3149**

DescribeAvailableQuickActionResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3150**
DescribeLayoutComponent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3152**
DescribeLayoutItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3153**
DescribeLayoutRow Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3156**
DescribeLayoutSection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3157**
DescribeQuickActionDefaultValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3160**
DescribeQuickActionParameter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3161**
DescribeQuickActionResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3164**
QuickActionDefaults Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3181**
QuickActionDefaultsHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3183**
QuickActionRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3188**
QuickActionResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3191**
SendEmailQuickActionDefaults Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3193**
Reports Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3195**

AggregateColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3199**
BucketField Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3200**
BucketFieldValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3207**
BucketType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3211**
ColumnDataType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3211**
ColumnSortOrder Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3212**
CrossFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3213**
CsfGroupType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3218**
DateGranularity Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3218**
DetailColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3219**
Dimension Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3220**
EvaluatedCondition Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3221**
EvaluatedConditionOperator Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3224**
FilterOperator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3225**

**Contents**

FilterValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3226**
FormulaType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3227**
GroupingColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3227**
GroupingInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3229**
GroupingValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3230**
NotificationAction Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3232**
NotificationActionContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3233**
ReportCsf Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3235**
ReportCurrency Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3244**
ReportDataCell Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3245**
ReportDescribeResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3246**
ReportDetailRow Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3247**
ReportDivisionInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3248**
ReportExtendedMetadata Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3249**
ReportFact Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3250**
ReportFactWithDetails Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3251**
ReportFactWithSummaries Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3252**
ReportFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3254**
ReportFormat Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3260**
ReportFilterType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3260**
ReportInstance Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3260**
ReportManager Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3263**
ReportMetadata Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3269**
ReportResults Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3288**
ReportScopeInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3290**
ReportScopeValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3291**
ReportType Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3293**
ReportTypeColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3294**
ReportTypeColumnCategory Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3295**
ReportTypeMetadata Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3297**
SortColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3299**
StandardDateFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3300**
StandardDateFilterDuration Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3304**
StandardDateFilterDurationGroup Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3305**
StandardFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3306**
StandardFilterInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3308**
StandardFilterInfoPicklist Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3309**
StandardFilterType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3311**
SummaryValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3311**
ThresholdInformation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3312**
TopRows Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3313**
Reports Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3316**
RevSignaling Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3317**
RevSalesTrxn Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3317**

**Contents**

RichMessaging Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3318**

AbstractTiming Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3319**
AddressableContact Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3319**
AuthRequestHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3323**
AuthRequestResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3325**
AuthRequestResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3327**
AuthRequestResultStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3329**
DeferredTiming Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3329**
MessageDefinitionInputParameter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3331**
PaymentItemStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3335**
PaymentLineItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3335**
PaymentMethod Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3341**
PostalAddress Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3343**
ProcessFormHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3346**
ProcessPaymentHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3348**
ProcessPaymentRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3349**
ProcessPaymentResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3352**
ProcessPaymentResultStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3354**
RecurringTiming Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3354**
ShippingMethod Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3358**
TimeSlotOption Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3363**
TimingIntervalUnit Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3366**
TimingType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3366**
RulesAppln Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3366**
runtime_industries_insurance Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3367**
Schema Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3367**

ChildRelationship Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3368**
DataCategory Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3370**
DataCategoryGroupSobjectTypePair Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3372**
DescribeColorResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3374**
DescribeDataCategoryGroupResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3376**
DescribeDataCategoryGroupStructureResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . 3378**
DescribeFieldResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3380**
DescribeIconResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3397**
DescribeSObjectResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3400**
DescribeTabResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3422**
DescribeTabSetResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3425**
DisplayType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3429**
FieldDescribeOptions Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3430**
FieldSet Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3430**
FieldSetMember Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3434**
PicklistEntry Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3437**
RecordTypeInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3438**
SOAPType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3441**

**Contents**

SObjectDescribeOptions Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3442**
SObjectField Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3443**
SObjectType Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3444**
Search Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3448**

KnowledgeSuggestionFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3448**
QuestionSuggestionFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3453**
SearchResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3456**
SearchResults Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3458**
SuggestionOption Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3459**
SuggestionResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3461**
SuggestionResults Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3461**
setup_flow_performance Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3462**

FlowPerformanceSetupDetails Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3463**
Sfc Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3463**

ContentDownloadContext Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3463**
ContentDownloadHandler Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3464**
ContentDownloadHandlerFactory Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3465**
Sfdc_Checkout Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3467**

AsyncCartProcessor Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3467**
B2BCheckoutController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3468**
IntegrationInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3469**
IntegrationStatus Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3471**
IntegrationStatus.Status Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3471**
Sfdc_Enablement Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3472**

LearningEvaluation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3472**
LearningEvaluationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3474**
LearningItemEvaluationHandler Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3476**
LearningItemProgressStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3478**
LearningItemSerializeDeserializer Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3479**
sfdc_surveys Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3482**

SurveyInvitationLinkShortener Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3482**
Example Implementation to Associate SurveySubjects with SurveyInvitation and
SurveyResponses **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3484**
Site Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3485**

UrlRewriter Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3486**
Site Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3487**
Slack Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3487**
Support Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3489**

EmailTemplateSelector Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3489**
MilestoneTriggerTimeCalculator Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3491**
System Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3493**

AccessLevel Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3500**
AccessType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3504**
Address Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3504**

**Contents**

Answers Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3509**
ApexPages Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3511**
Approval Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3514**
Assert Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3526**
AsyncInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3538**
AsyncOptions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3540**
Blob Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3541**
Boolean Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3544**
BusinessHours Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3546**
CallbackStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3549**
Callable Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3549**
Cases Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3552**
Collator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3555**
Comparable Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3557**
Comparator Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3560**
Continuation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3562**
Cookie Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3566**
Crypto Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3574**
Custom Metadata Type Methods **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3600**
Custom Settings Methods **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3604**
Database Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3614**
Date Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3711**
Datetime Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3721**
Decimal Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3745**
Domain Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3758**
DomainCreator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3761**
DomainParser Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3765**
DomainType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3767**
Double Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3768**
EmailMessages Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3771**
EncodingUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3775**
Enum Methods **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3779**
EventBus Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3779**
Exception Class and Built-In Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3784**
ExternalServiceTest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3789**
FlexQueue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3790**
FeatureManagement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3793**
Formula Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3799**
FormulaRecalcFieldError Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3800**
FormulaRecalcResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3801**
Http Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3803**
HttpCalloutMock Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3804**
HttpRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3805**
HttpResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3815**

**Contents**

Id Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3821**
Ideas Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3828**
InstallHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3833**
Integer Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3836**
JSON Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3838**
JSONGenerator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3845**
JSONParser Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3859**
JSONToken Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3871**
Label Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3872**
Limits Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3875**
List Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3891**
Location Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3906**
LoggingLevel Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3909**
Long Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3910**
Map Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3911**
Matcher Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3924**
Math Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3936**
Messaging Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3962**
MultiStaticResourceCalloutMock Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3970**
Network Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3973**
Object Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3978**
OrgLimit Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3981**
OrgLimits Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3983**
PageReference Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3984**
Packaging Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3997**
Pattern Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3998**
Queueable Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4002**
QueueableContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4004**
QueueableDuplicateSignature Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4005**
QueueableDuplicateSignature.Builder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4005**
QuickAction Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4009**
Quiddity Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4013**
RemoteObjectController **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4014**
Request Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4018**
ResetPasswordResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4019**
RestContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4020**
RestRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4021**
RestResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4027**
SandboxPostCopy Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4031**
Schedulable Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4033**
SchedulableContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4034**
Schema Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4035**
Search Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4040**
Security Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4045**

**Contents**

SelectOption Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4049**
Set Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4055**
Site Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4066**
SObject Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4088**
SObjectAccessDecision Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4115**
SoqlStubProvider Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4118**
StaticResourceCalloutMock Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4121**
String Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4124**
StubProvider Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4199**
System Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4201**
Test Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4229**
Time Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4249**
TimeZone Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4254**
Trigger Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4257**
TriggerOperation Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4260**
Type Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4260**
UninstallHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4268**
URL Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4271**
UserInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4281**
UserManagement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4290**
UUID Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4310**
Version Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4312**
WebServiceCallout Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4316**
WebServiceMock Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4317**
XmlStreamReader Class Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4319**
XmlStreamWriter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4333**
TerritoryMgmt Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4340**

OpportunityTerritory2AssignmentFilter Global Interface **. . . . . . . . . . . . . . . . . . . . . . 4340**
TxnSecurity Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4344**

Event Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4344**
EventCondition Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4348**
AsyncCondition Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4350**
PolicyCondition Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4351**
UserProvisioning Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4353**

ConnectorTestUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4353**
UserProvisioningLog Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4355**
UserProvisioningPlugin Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4357**
VisualEditor Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4361**

DataRow Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4362**
DesignTimePageContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4365**
DynamicPickList Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4367**
DynamicPickListRows Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4370**
Wave Namespace Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4375**

QueryBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4375**

**Contents**

QueryNode Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4379**
ProjectionNode Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4383**
Templates Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4386**
TemplatesSearchOptions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4389**
Appendices **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4391**

Shipping Invoice Example **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4391**
Reserved Keywords **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4403**
Documentation Typographical Conventions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4404**

APEX REFERENCE GUIDE

Apex is a strongly typed, object-oriented programming language that allows developers to execute flow and transaction control
statements on the Salesforce Platform server, in conjunction with calls to the API. This reference guide includes built-in Apex classes,
interfaces, enums, and exceptions, grouped by namespace. It also includes Apex DML statements to insert, update, merge, delete, and
restore data in Salesforce.

[For information on the Apex development process, see Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)

Note: In API version 51.0 and earlier, Apex Reference information was included in the Apex Developer Guide in the **Apex Language**
**Reference** section.

IN THIS SECTION:

Apex Release Notes
Use the Salesforce Release Notes to learn about the most recent updates and changes to Apex.

Apex DML Operations
You can perform DML operations using the Apex DML statements or the methods of the `Database` class. For lead conversion,
use the `convertLead` method of the `Database` class. There is no DML counterpart for it.

ApexPages Namespace
The `ApexPages` namespace provides classes used in Visualforce controllers.

AppLauncher Namespace
The `AppLauncher` namespace provides methods for managing the appearance of apps in the App Launcher, including their
visibility and sort order.

Approval Namespace
The `Approval` namespace provides classes and methods for approval processes.

Auth Namespace
The `Auth` namespace provides an interface and classes for single sign-on into Salesforce and session security management.

Cache Namespace
The `Cache` namespace contains methods for managing the platform cache.

Canvas Namespace
The `Canvas` namespace provides an interface and classes for canvas apps in Salesforce.

ChatterAnswers Namespace
The `ChatterAnswers` namespace provides an interface for creating Account records.

CommerceBuyGrp Namespace
The `CommerceBuyGrp` namespace provides classes and methods for retrieving information about the buyer groups associated
with a user.

CommerceExtension Namespace
Use the `CommerceExtension` namespace to define resolution strategies for registered Commerce extensions.

CommerceOrders Namespace
The `CommerceOrders` namespace provides classes and methods to place orders with integrated pricing, configuration, and
validation.


Apex Reference Guide

CommercePayments Namespace
Use the `CommercePayments` namespace to provide a safe and customizable platform for managing customer payments and
refunds.

CommerceTax Namespace
Manage the communication between Salesforce and an external tax engine.

ComplianceMgmt Namespace
The `ComplianceMgmt` namespace provides classes and methods to implement rule processors for compliance control.

Compression Namespace
The Compression namespace provides classes and methods to create and extract zip files.

ConnectApi Namespace
The `ConnectApi` namespace (also called Connect in Apex) provides classes for accessing the same data available in Connect
REST API. Use Connect in Apex to create custom experiences in Salesforce.

Context Namespace
The `Context` namespace provides classes and methods to manage the sharing and consumption of business application data
by using Context Service.

Database Namespace
The `Database` namespace provides classes used with DML operations.

Datacloud Namespace
The `Datacloud` namespace provides classes and methods for retrieving information about duplicate rules. Duplicate rules let
you control whether and when users can save duplicate records within Salesforce.

DataRetrieval Namespace
The `DataRetrieval` namespace provides classes and methods to record details of customer-agent engagements, as well as
transcripts of their conversations.

DataSource Namespace
The `DataSource` namespace provides the classes for the Apex Connector Framework. Use the Apex Connector Framework to
develop a custom adapter for Salesforce Connect. Then connect your Salesforce organization to any data anywhere via the Salesforce
Connect custom adapter.

DataWeave Namespace
The DataWeave namespace provides classes and methods to support the invocation of DataWeave scripts from Apex.

Dom Namespace
The `Dom` namespace provides classes and methods for parsing and creating XML content.

embeddedai Namespace
The `embeddedai` namespace provides classes and methods to manage and represent records and data in Apex to support
embedded AI features.

EventBus Namespace
The `EventBus` namespace provides classes and methods for platform events and Change Data Capture events.

ExternalService Namespace
The `ExternalService` namespace provides dynamically generated Apex service interfaces and Apex classes for complex
object data types.

Flow Namespace
The `Flow` namespace provides a class for advanced access to flows from Apex such as from Visualforce controllers and asynchronous
Apex.


Apex Reference Guide

Flowtesting Namespace
The `flowtesting` namespace provides dynamically generated Apex classes for flow tests that are created in Flow Builder.

flowuiruntime Namespace
The classes and methods in this namespace are reserved for internal use only or future use.

FormulaEval Namespace
The FormulaEval namespace provides classes and methods to evaluate dynamic formulas for SObjects and Apex objects. Use the
methods to avoid unnecessary DML statements to recalculate formula field values or evaluate dynamic formula expressions.

fsccashflow Namespace
The `fsccashflow` namespace provides classes used in the FSCCashFlow Flexcards and its child Flexcards.

Functions Namespace
The Functions namespace provides classes and methods used to invoke and manage Salesforce Functions.

ise_bots_apex Namespace
The ise_bots_apex namespace provides classes and properties to facilitate dynamic content generation and data handling for
menu-driven bot interactions. Create and manage dynamic menu items that adapt to user inputs, context, and underlying object
data.

industriesNlpSvc
Stores the objects used in Industries Einstein Natural Language Processing (NLP) services.

IndustriesDigitalLending Namespace
The `industriesDigitalLending` namespace provides classes used in the Digital Lending OmniScripts and Integration
Procedures.

Invocable Namespace
The `Invocable` namespace provides classes for calling invocable actions from Apex.

InvoiceWriteOff Namespace
The `InvoiceWriteOff` namespace provides classes to create credit memos with the total charge amount on the invoice as
the write-off amount.

IsvPartners Namespace
The `IsvPartners` namespace provides a class associated with Salesforce ISV partner use cases, such as optimizing code, providing
great customer trial experiences, and driving feature adoption.

KbManagement Namespace
The `KbManagement` namespace provides a class for managing knowledge articles.

LxScheduler Namespace
The `LxScheduler` namespace provides an interface and classes for integrating Salesforce Scheduler with external calendars.

Messaging Namespace
The `Messaging` namespace provides classes and methods for Salesforce outbound and inbound email functionality.

Metadata Namespace
The `Metadata` namespace provides classes and methods for working with custom metadata in Salesforce

PlaceQuote Namespace
The `PlaceQuote` namespace provides classes and methods to create or update quotes with pricing preferences and configuration
options.

Pref_center Namespace
The Pref_center namespace provides an interface, classes, and methods to create and retrieve data in forms in Preference Manager.
Preference Manager, previously called Preference Center, is a feature within the Privacy Center app.


Apex Reference Guide

Process Namespace
The `Process` namespace provides an interface and classes for passing data between your organization and a flow.

QuickAction Namespace
The `QuickAction` namespace provides classes and methods for quick actions.

Reports Namespace
The `Reports` namespace provides classes for accessing the same data as is available in the Salesforce Reports and Dashboards
REST API.

RevSignaling Namespace
The `RevSignaling` namespace provides classes to extend the standard procedure plan implementation through custom logic.
A procedure plan helps you set up your procedures, configure the procedure execution settings, and relate them to a context
definition in one centralized location based on your requirements.

RevSalesTrxn Namespace
The `RevSalesTrxn` namespace provides classes and methods to create a sales transaction, such as a quote or an order, with
integrated pricing and configuration.

RichMessaging Namespace
Provides objects and methods for handling content in enhanced Messaging channels.

RulesAppln Namespace
The RulesAppln namespace contains output classes that store details about a rules-based application of payments and credits.

runtime_industries_insurance Namespace
The `runtime_industries_insurance` namespace provides options classes for insurance operations, such as creating
and updating insurance quotes, generating insurance clauses, and running insurance rating.

Schema Namespace
The `Schema` namespace provides classes and methods for schema metadata information.

Search Namespace
The `Search` namespace provides classes for getting search results and suggestion results.

setup_flow_performance Namespace
The class and methods in this namespace are for internal use only.

Sfc Namespace
The Sfc namespace contains classes used in Salesforce Files.

Sfdc_Checkout Namespace
The Sfdc_Checkout namespace provides an interface and classes for B2B Commerce apps in Salesforce.

Sfdc_Enablement Namespace
The `sfdc_enablement` namespace provides classes for creating custom learning items to implement custom exercise types
in Enablement programs. Lightning web components are used to render the custom exercises on Program Builder.

sfdc_surveys Namespace
The `sfdc_surveys` namespace provides an interface for shortening survey invitations.

Site Namespace
The `Site` namespace provides an interface for rewriting Sites URLs.

Slack Namespace
The `Slack` Namespace provides tools designed to accelerate and ease the process of developing Slack apps on the Salesforce
platform.


Apex Reference Guide Apex Release Notes

Support Namespace
The `Support` namespace provides an interface used for Case Feed.

System Namespace
The `System` namespace provides classes and methods for core Apex functionality.

TerritoryMgmt Namespace
The `TerritoryMgmt` namespace provides an interface used for territory management.

TxnSecurity Namespace
The `TxnSecurity` namespace provides an interface used for transaction security.

UserProvisioning Namespace
The `UserProvisioning` namespace provides methods for monitoring outbound user provisioning requests.

VisualEditor Namespace
The `VisualEditor` namespace provides classes and methods for interacting with the Lightning App Builder. The classes and
methods in this namespace operate on Lightning components, which include Lightning web components and Aura components.

Wave Namespace Namespace
The classes in the `Wave` namespace are part of the CRM Analytics Analytics SDK, designed to facilitate querying CRM Analytics data
from Apex code.

Appendices

Apex Release Notes

Use the Salesforce Release Notes to learn about the most recent updates and changes to Apex.

[For Apex updates and changes that impact the Salesforce Platform, see the Apex Release Notes.](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex.htm&language=en_US)

[For new and changed Apex classes, methods, exceptions and interfaces, see Apex: New and Changed Items in the Salesforce Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_nc.htm&language=en_US)
Notes.

## Apex DML Operations

You can perform DML operations using the Apex DML statements or the methods of the `Database` class. For lead conversion, use
the `convertLead` method of the `Database` class. There is no DML counterpart for it.

SEE ALSO:

_Apex Developer Guide_ [: Working with Data in Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_data_intro.htm)

Database Class

### Apex DML Statements

Use Data Manipulation Language (DML) statements to insert, update, merge, delete, and restore data in Salesforce.

The following Apex DML statements are available:


Apex Reference Guide Apex DML Statements

#### Insert Statement

The `insert` DML operation adds one or more sObjects, such as individual accounts or contacts, to your organization’s data. `insert`
is analogous to the INSERT statement in SQL.

Syntax

```
   insert sObject

   insert sObject[]

```

Example

The following example inserts an account named 'Acme':

```
   Account newAcct = new Account(name = 'Acme');

   try {

     insert newAcct;

   } catch (DmlException e) {

   // Process exception here

   }

```

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)

#### Update Statement

The `update` DML operation modifies one or more existing sObject records, such as individual accounts or contacts, in your organization’s
data. `update` is analogous to the UPDATE statement in SQL.

Syntax

```
   update sObject

   update sObject[]

```

Example

The following example updates the `BillingCity` field on a single account named 'Acme':

```
   Account a = new Account(Name='Acme2');

   insert(a);

   Account myAcct = [SELECT Id, Name, BillingCity FROM Account WHERE Id = :a.Id];

   myAcct.BillingCity = 'San Francisco';

   try {

      update myAcct;

   } catch (DmlException e) {

      // Process exception here

   }

```

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)


Apex Reference Guide Apex DML Statements

#### Upsert Statement

The `upsert` DML operation creates new records and updates sObject records within a single statement, using a specified field to
determine the presence of existing objects, or the ID field if no field is specified.

Syntax

```
   upsert sObject [ opt_field ]

   upsert sObject[] [ opt_field ]

```

The `upsert` statement matches the sObjects with existing records by comparing values of one field. If you don’t specify a field when
calling this statement, the `upsert` statement uses the sObject’s ID to match the sObject with existing records in Salesforce. Alternatively,
you can specify a field to use for matching. For custom objects, specify a custom field marked as external ID. For standard objects, you
can specify any field that has the `idLookup` attribute set to true. For example, the Email field of Contact or User has the `idLookup`
[attribute set. To check a field’s attribute, see the Object Reference for Salesforce.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/)

[Also, you can use foreign keys to upsert sObject records if they have been set as reference fields. For more information, see Field Types](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/field_types.htm)
in the _Object Reference for Salesforce._

The optional field parameter, _`opt_field`_, is a field token (of type `Schema.SObjectField` ). For example, to specify the
MyExternalID custom field, the statement is:

```
   upsert sObjectList Account.Fields.MyExternalId__c;

```

If the field used for matching doesn’t have the `Unique` attribute set, the context user must have the “View All Records” object-level
permission for the target object or the “View All Data” permission so that `upsert` doesn’t accidentally insert a duplicate record.

Note: Custom field matching is case-insensitive only if the custom field has the **Unique** and **Treat "ABC" and "abc" as duplicate**
**values (case insensitive)** attributes selected as part of the field definition. If so, “ABC123” is matched with “abc123.” For more
information, see “Create Custom Fields” in the Salesforce online help.

How Upsert Chooses to Insert or Update

Upsert uses the sObject record's primary key (the ID), an idLookup field, or an external ID field to determine whether it should create a
record or update an existing one:

**•** If the key isn’t matched, a new object record is created.

**•** If the key is matched once, the existing object record is updated.

**•** If the key is matched multiple times, an error is generated and the object record isn’t inserted or updated.

Example

This example performs an upsert of a list of accounts.

```
   List<Account> acctList = new List<Account>();

   // Fill the accounts list with some accounts

   try {

      upsert acctList;

   } catch (DmlException e) {

   }

```


Apex Reference Guide Apex DML Statements

This next example performs an upsert of a list of accounts using a foreign key for matching existing records, if any.

```
   List<Account> acctList = new List<Account>();

   // Fill the accounts list with some accounts

   try {

      // Upsert using an external ID field

      upsert acctList myExtIDField__c;

   } catch (DmlException e) {

   }

#### Delete Statement

```

The `delete` DML operation deletes one or more existing sObject records, such as individual accounts or contacts, from your organization’s
data. `delete` is analogous to the `delete()` statement in the SOAP API.

Syntax

```
   delete sObject

   delete sObject[]

```

Example

The following example deletes all accounts that are named 'DotCom':

```
   Account[] doomedAccts = [SELECT Id, Name FROM Account

                  WHERE Name = 'DotCom'];

   try {

      delete doomedAccts;

   } catch (DmlException e) {

      // Process exception here

   }

```

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)

#### Undelete Statement

The `undelete` DML operation restores one or more existing sObject records, such as individual accounts or contacts, from your
organization’s Recycle Bin. `undelete` is analogous to the UNDELETE statement in SQL.

Syntax

```
   undelete sObject | ID

   undelete sObject[] | ID[]

```


Apex Reference Guide Apex DML Statements

Example

The following example undeletes an account named 'Universal Containers’. The `ALL ROWS` keyword queries all rows for both top
level and aggregate relationships, including deleted records and archived activities.

```
   Account[] savedAccts = [SELECT Id, Name FROM Account WHERE Name = 'Universal Containers'

   ALL ROWS];

   try {

      undelete savedAccts;

   } catch (DmlException e) {

      // Process exception here

   }

```

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)

#### Merge Statement

The `merge` statement merges up to three records of the same sObject type into one of the records, deleting the others, and re-parenting
any related records.

Note: This DML operation does not have a matching Database system method.

Syntax

```
   merge sObject sObject

   merge sObject sObject[]

   merge sObject ID

   merge sObject ID[]

```

The first parameter represents the master record into which the other records are to be merged. The second parameter represents the
one or two other records that should be merged and then deleted. You can pass these other records into the `merge` statement as a
single sObject record or ID, or as a list of two sObject records or IDs.

Example

The following example merges two accounts named 'Acme Inc.' and 'Acme' into a single record:

```
   List<Account> ls = new List<Account>{new Account(name='Acme Inc.'),new Account(name='Acme')};

   insert ls;

   Account masterAcct = [SELECT Id, Name FROM Account WHERE Name = 'Acme Inc.' LIMIT 1];

   Account mergeAcct = [SELECT Id, Name FROM Account WHERE Name = 'Acme' LIMIT 1];

   try {

      merge masterAcct mergeAcct;

   } catch (DmlException e) {

      // Process exception here

   }

```

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)


## Apex Reference Guide ApexPages Namespace ApexPages Namespace The ApexPages namespace provides classes used in Visualforce controllers. The following are the classes in the ApexPages namespace.

IN THIS SECTION:

### Action Class

You can use `ApexPages.Action` to create an action method that you can use in a Visualforce custom controller or controller
extension.

Component Class
Represents a dynamic Visualforce component in Apex.

IdeaStandardController Class

`IdeaStandardController` objects offer Ideas-specific functionality in addition to what is provided by the
`StandardController` .

IdeaStandardSetController Class

`IdeaStandardSetController` objects offer Ideas-specific functionality in addition to what is provided by the
`StandardSetController` .

KnowledgeArticleVersionStandardController Class

`KnowledgeArticleVersionStandardController` objects offer article-specific functionality in addition to what is
provided by the `StandardController` .

Message Class
Contains validation errors that occur when the user saves the page that uses a standard controller.

StandardController Class
Use a StandardController when defining an extension for a standard controller.

StandardSetController Class

`StandardSetController` objects allow you to create list controllers similar to, or as extensions of, the pre-built Visualforce
list controllers provided by Salesforce.

### Action Class

You can use `ApexPages.Action` to create an action method that you can use in a Visualforce custom controller or controller
extension.

Namespace

## ApexPages

Usage

For example, you could create a `saveOver` method on a controller extension that performs a custom save.


Apex Reference Guide Action Class

Instantiation

The following code snippet illustrates how to instantiate a new `ApexPages.Action` object that uses the save action:

```
   ApexPages.Action saveAction = new ApexPages.Action('{!save}');

```

IN THIS SECTION:

#### Action Constructors Action Methods Action Constructors The following are constructors for Action .

IN THIS SECTION:

##### Action(action)

Creates a new instance of the `ApexPages.Action` class using the specified action.

##### Action(action)

Creates a new instance of the `ApexPages.Action` class using the specified action.

Signature

```
   public Action(String action)

```

Parameters

```
   action
```

Type: String

The action.

#### Action Methods The following are methods for Action . All are instance methods.

IN THIS SECTION:

##### getExpression()

Returns the expression that is evaluated when the action is invoked.

invoke()
Invokes the action.

##### getExpression()

Returns the expression that is evaluated when the action is invoked.


### Apex Reference Guide Component Class

Signature

```
   public String getExpression()

```

Return Value

Type: String

##### invoke()

Invokes the action.

Signature

```
   public System.PageReference invoke()

```

Return Value

Type: System.PageReference

### Component Class

Represents a dynamic Visualforce component in Apex.

Namespace

ApexPages

#### Dynamic Component Properties

### The following are properties for Component .

IN THIS SECTION:

##### childComponents

Returns a reference to the child components for the component.

expressions
Sets the content of an attribute using the expression language notation. The notation for this is
`expressions` . _`name_of_attribute`_ .

facets
Sets the content of a facet to a dynamic component. The notation is `facet` . _`name_of_facet`_ .

##### childComponents

Returns a reference to the child components for the component.

Signature

```
   public List <ApexPages.Component> childComponents {get; set;}

```


Apex Reference Guide Component Class

Property Value

Type: List<ApexPages.Component>

Example

```
   Component.Apex.PageBlock pageBlk = new Component.Apex.PageBlock();

   Component.Apex.PageBlockSection pageBlkSection = new

   Component.Apex.PageBlockSection(title='dummy header');

   pageBlk.childComponents.add(pageBlkSection);

##### expressions Sets the content of an attribute using the expression language notation. The notation for this is expressions . name_of_attribute .

```

Signature

```
   public String expressions {get; set;}

```

Property Value

Type: String

Example

```
   Component.Apex.InputField inpFld = new

   Component.Apex.InputField();

   inpField.expressions.value = '{!Account.Name}';

   inpField.expressions.id = '{!$User.FirstName}';

##### facets Sets the content of a facet to a dynamic component. The notation is facet . name_of_facet .

```

Signature

```
   public String facets {get; set;}

```

Property Value

Type: String

Usage

Note: This property is only accessible by components that support facets.


### Apex Reference Guide IdeaStandardController Class

Example

```
   Component.Apex.DataTable myDT = new

   Component.Apex.DataTable();

   Component.Apex.OutputText footer = new

   Component.Apex.OutputText(value='Footer Copyright');

   myDT.facets.footer = footer;

### IdeaStandardController Class IdeaStandardController objects offer Ideas-specific functionality in addition to what is provided by the
```

`StandardController` .

Namespace

ApexPages

Usage

A method in the IdeaStandardController object is called by and operated on a particular instance of an IdeaStandardController.

### Note: The IdeaStandardSetController and IdeaStandardController classes are currently available through

a limited release program. For information on enabling these classes for your organization, contact your Salesforce representative.

### In addition to the methods listed in this class, the IdeaStandardController class inherits all the methods associated with the

`StandardController` class.

Instantiation

An IdeaStandardController object cannot be instantiated. An instance can be obtained through a constructor of a custom extension
controller when using the standard ideas controller.

Example

The following example shows how an IdeaStandardController object can be used in the constructor for a custom list controller. This
example provides the framework for manipulating the comment list data before displaying it on a Visualforce page.

```
   public class MyIdeaExtension {

      private final ApexPages.IdeaStandardController ideaController;

      public MyIdeaExtension(ApexPages.IdeaStandardController controller) {

        ideaController = (ApexPages.IdeaStandardController)controller;

      }

      public List<IdeaComment> getModifiedComments() {

        IdeaComment[] comments = ideaController.getCommentList();

        // modify comments here

        return comments;

      }

   }

```


Apex Reference Guide IdeaStandardController Class

The following Visualforce markup shows how the IdeaStandardController example shown above can be used in a page. This page must
be named _`detailPage`_ for this example to work.

Note: For the Visualforce page to display the idea and its comments, in the following example you need to specify the ID of a
specific idea (for example, `/apex/detailPage?id=<ideaID>` ) whose comments you want to view.

```
   <!-- page named detailPage -->

   <apex:page standardController="Idea" extensions="MyIdeaExtension">

      <apex:pageBlock title="Idea Section">

        <ideas:detailOutputLink page="detailPage" ideaId="{!idea.id}">{!idea.title}

        </ideas:detailOutputLink>

        <br/><br/>

        <apex:outputText >{!idea.body}</apex:outputText>

      </apex:pageBlock>

      <apex:pageBlock title="Comments Section">

        <apex:dataList var="a" value="{!modifiedComments}" id="list">

           {!a.commentBody}

        </apex:dataList>

        <ideas:detailOutputLink page="detailPage" ideaId="{!idea.id}"

            pageOffset="-1">Prev</ideas:detailOutputLink>

        |

        <ideas:detailOutputLink page="detailPage" ideaId="{!idea.id}"

            pageOffset="1">Next</ideas:detailOutputLink>

      </apex:pageBlock>

   </apex:page>

```

SEE ALSO:

StandardController Class

#### IdeaStandardController Methods The following are instance methods for IdeaStandardController .

IN THIS SECTION:

##### getCommentList()

Returns the list of read-only comments from the current page.

##### getCommentList()

Returns the list of read-only comments from the current page.

Signature

```
   public IdeaComment[] getCommentList()

```

Return Value

Type: IdeaComment[]

This method returns the following comment properties:

**•** `id`


### Apex Reference Guide IdeaStandardSetController Class

**•** `commentBody`

**•** `createdDate`

**•** `createdBy.Id`

**•** `createdBy.communityNickname`

### IdeaStandardSetController Class IdeaStandardSetController objects offer Ideas-specific functionality in addition to what is provided by the

`StandardSetController` .

Namespace

ApexPages

Usage

### Note: The IdeaStandardSetController and IdeaStandardController classes are currently available through

a limited release program. For information on enabling these classes for your organization, contact your Salesforce representative.

### In addition to the method listed above, the IdeaStandardSetController class inherits the methods associated with the

`StandardSetController` .

Note: The methods inherited from the `StandardSetController` cannot be used to affect the list of ideas returned by
the `getIdeaList` method.

Instantiation

An IdeaStandardSetController object cannot be instantiated. An instance can be obtained through a constructor of a custom extension
controller when using the standard list controller for ideas.

Example: Displaying a Profile Page

The following example shows how an IdeaStandardSetController object can be used in the constructor for a custom list controller:

```
   public class MyIdeaProfileExtension {

      private final ApexPages.IdeaStandardSetController ideaSetController;

      public MyIdeaProfileExtension(ApexPages.IdeaStandardSetController controller) {

        ideaSetController = (ApexPages.IdeaStandardSetController)controller;

      }

      public List<Idea> getModifiedIdeas() {

        Idea[] ideas = ideaSetController.getIdeaList();

        // modify ideas here

        return ideas;

      }

   }

```

The following Visualforce markup shows how the IdeaStandardSetController example shown above and the

`<ideas:profileListOutputLink>` component can display a profile page that lists the recent replies, submitted ideas, and


Apex Reference Guide IdeaStandardSetController Class

votes associated with a user. Because this example does not identify a specific user ID, the page automatically shows the profile page
for the current logged in user. This page must be named _`profilePage`_ in order for this example to work:

```
   <!-- page named profilePage -->

   <apex:page standardController="Idea" extensions="MyIdeaProfileExtension"

   recordSetVar="ideaSetVar">

      <apex:pageBlock >

        <ideas:profileListOutputLink sort="recentReplies" page="profilePage">

         Recent Replies</ideas:profileListOutputLink>

        |

        <ideas:profileListOutputLink sort="ideas" page="profilePage">Ideas Submitted

        </ideas:profileListOutputLink>

        |

        <ideas:profileListOutputLink sort="votes" page="profilePage">Ideas Voted

        </ideas:profileListOutputLink>

      </apex:pageBlock>

      <apex:pageBlock >

        <apex:dataList value="{!modifiedIdeas}" var="ideadata">

           <ideas:detailoutputlink ideaId="{!ideadata.id}" page="viewPage">

           {!ideadata.title}</ideas:detailoutputlink>

        </apex:dataList>

      </apex:pageBlock>

   </apex:page>

```

In the previous example, the `<ideas:detailoutputlink>` component links to the following Visualforce markup that displays
the detail page for a specific idea. This page must be named _`viewPage`_ in order for this example to work:

```
   <!-- page named viewPage -->

   <apex:page standardController="Idea">

      <apex:pageBlock title="Idea Section">

        <ideas:detailOutputLink page="viewPage" ideaId="{!idea.id}">{!idea.title}

        </ideas:detailOutputLink>

        <br/><br/>

        <apex:outputText>{!idea.body}</apex:outputText>

      </apex:pageBlock>

   </apex:page>

```

Example: Displaying a List of Top, Recent, and Most Popular Ideas and Comments

The following example shows how an IdeaStandardSetController object can be used in the constructor for a custom list controller:

Note: You must have created at least one idea for this example to return any ideas.

```
   public class MyIdeaListExtension {

      private final ApexPages.IdeaStandardSetController ideaSetController;

      public MyIdeaListExtension (ApexPages.IdeaStandardSetController controller) {

        ideaSetController = (ApexPages.IdeaStandardSetController)controller;

      }

      public List<Idea> getModifiedIdeas() {

        Idea[] ideas = ideaSetController.getIdeaList();

        // modify ideas here

```


Apex Reference Guide IdeaStandardSetController Class

```
        return ideas;

      }

   }

```

The following Visualforce markup shows how the IdeaStandardSetController example shown above can be used with the

`<ideas:listOutputLink>` component to display a list of recent, top, and most popular ideas and comments. This page must
be named _`listPage`_ in order for this example to work:

```
   <!-- page named listPage -->

   <apex:page standardController="Idea" extensions="MyIdeaListExtension"

   recordSetVar="ideaSetVar">

      <apex:pageBlock >

        <ideas:listOutputLink sort="recent" page="listPage">Recent Ideas

        </ideas:listOutputLink>

        |

        <ideas:listOutputLink sort="top" page="listPage">Top Ideas

        </ideas:listOutputLink>

        |

        <ideas:listOutputLink sort="popular" page="listPage">Popular Ideas

        </ideas:listOutputLink>

        |

        <ideas:listOutputLink sort="comments" page="listPage">Recent Comments

        </ideas:listOutputLink>

      </apex:pageBlock>

      <apex:pageBlock >

        <apex:dataList value="{!modifiedIdeas}" var="ideadata">

           <ideas:detailoutputlink ideaId="{!ideadata.id}" page="viewPage">

           {!ideadata.title}</ideas:detailoutputlink>

        </apex:dataList>

      </apex:pageBlock>

   </apex:page>

```

In the previous example, the `<ideas:detailoutputlink>` component links to the following Visualforce markup that displays
the detail page for a specific idea. This page must be named _`viewPage`_ .

```
   <!-- page named viewPage -->

   <apex:page standardController="Idea">

      <apex:pageBlock title="Idea Section">

        <ideas:detailOutputLink page="viewPage" ideaId="{!idea.id}">{!idea.title}

        </ideas:detailOutputLink>

        <br/><br/>

        <apex:outputText>{!idea.body}</apex:outputText>

      </apex:pageBlock>

   </apex:page>

```

SEE ALSO:

StandardSetController Class

#### IdeaStandardSetController Methods The following are instance methods for IdeaStandardSetController .


### Apex Reference Guide KnowledgeArticleVersionStandardController Class

IN THIS SECTION:

##### getIdeaList()

Returns the list of read-only ideas in the current page set.

##### getIdeaList()

Returns the list of read-only ideas in the current page set.

Signature

```
   public Idea[] getIdeaList()

```

Return Value

Type: Idea[]

Usage

You can use the `<ideas:listOutputLink>`, `<ideas:profileListOutputLink>`, and

`<ideas:detailOutputLink>` components to display profile pages as well as idea list and detail pages (see the examples below).
The following is a list of properties returned by this method:

**•** `Body`

**•** `Categories`

**•** `Category`

**•** `CreatedBy.CommunityNickname`

**•** `CreatedBy.Id`

**•** `CreatedDate`

**•** `Id`

**•** `LastCommentDate`

**•** `LastComment.Id`

**•** `LastComment.CommentBody`

**•** `LastComment.CreatedBy.CommunityNickname`

**•** `LastComment.CreatedBy.Id`

**•** `NumComments`

**•** `Status`

**•** `Title`

**•** `VoteTotal`

### KnowledgeArticleVersionStandardController Class KnowledgeArticleVersionStandardController objects offer article-specific functionality in addition to what is provided

by the `StandardController` .


Apex Reference Guide KnowledgeArticleVersionStandardController Class

Namespace

ApexPages

Usage

In addition to the method listed above, the `KnowledgeArticleVersionStandardController` class inherits all the methods
associated with `StandardController` .

Note: Though inherited, the `edit`, `delete`, and `save` methods don't serve a function when used with the
`KnowledgeArticleVersionStandardController` class.

Example

The following example shows how a `KnowledgeArticleVersionStandardController` object can be used to create a
custom extension controller. In this example, you create a class named `AgentContributionArticleController` that allows
customer-support agents to see pre-populated fields on the draft articles they create while closing cases.

Prerequisites:

**1.** Create an article type called _`FAQ`_ . For instructions, see “Create Article Types” in the Salesforce online help.

**2.** Create a text custom field called `Details` . For instructions, see “Add Custom Fields to Article Types” in the Salesforce online help.

**3.** Create a category group called _`Geography`_ and assign it to a category called _`USA`_ . For instructions, see “Create and Modify
Category Groups” and “Add Data Categories to Category Groups” in the Salesforce online help.

**4.** Create a category group called _`Topics`_ and assign it a category called _`Maintenance`_ .

```
   /** Custom extension controller for the simplified article edit page that

      appears when an article is created on the close-case page.

   */

   public class AgentContributionArticleController {

      // The constructor must take a ApexPages.KnowledgeArticleVersionStandardController as

    an argument

      public AgentContributionArticleController(

        ApexPages.KnowledgeArticleVersionStandardController ctl) {

        // This is the SObject for the new article.

        //It can optionally be cast to the proper article type.

        // For example, FAQ__kav article = (FAQ__kav) ctl.getRecord();

        SObject article = ctl.getRecord();

        // This returns the ID of the case that was closed.

        String sourceId = ctl.getSourceId();

        Case c = [SELECT Subject, Description FROM Case WHERE Id=:sourceId];

        // This overrides the default behavior of pre-filling the

        // title of the article with the subject of the closed case.

        article.put('title', 'From Case: '+c.subject);

        article.put('details__c',c.description);

        // Only one category per category group can be specified.

        ctl.selectDataCategory('Geography','USA');

        ctl.selectDataCategory('Topics','Maintenance');

```


Apex Reference Guide KnowledgeArticleVersionStandardController Class

```
      }

   }

   /** Test class for the custom extension controller.

   */

   @isTest

   private class AgentContributionArticleControllerTest {

      static testMethod void testAgentContributionArticleController() {

         String caseSubject = 'my test';

         String caseDesc = 'my test description';

         Case c = new Case();

         c.subject= caseSubject;

         c.description = caseDesc;

         insert c;

         String caseId = c.id;

         System.debug('Created Case: ' + caseId);

         ApexPages.currentPage().getParameters().put('sourceId', caseId);

         ApexPages.currentPage().getParameters().put('sfdc.override', '1');

         ApexPages.KnowledgeArticleVersionStandardController ctl =

           new ApexPages.KnowledgeArticleVersionStandardController(new FAQ__kav());

         new AgentContributionArticleController(ctl);

         System.assertEquals(caseId, ctl.getSourceId());

         System.assertEquals('From Case: '+caseSubject, ctl.getRecord().get('title'));

         System.assertEquals(caseDesc, ctl.getRecord().get('details__c'));

     }

   }

```

If you created the custom extension controller for the purpose described in the previous example (that is, to modify submitted-via-case
articles), complete the following steps after creating the class:

**1.** Log into your Salesforce organization and from Setup, enter _`Knowledge Settings`_ in the `Quick Find` box, then select
**Knowledge Settings** .

**2.** Click **Edit** .

**3.** Assign the class to the `Use Apex customization` field. This associates the article type specified in the new class with the
article type assigned to closed cases.

**4.** Click **Save** .

IN THIS SECTION:

KnowledgeArticleVersionStandardController Constructors

KnowledgeArticleVersionStandardController Methods

SEE ALSO:

StandardController Class


Apex Reference Guide KnowledgeArticleVersionStandardController Class

#### KnowledgeArticleVersionStandardController Constructors The following are constructors for KnowledgeArticleVersionStandardController .

IN THIS SECTION:

##### KnowledgeArticleVersionStandardController(article)

Creates a new instance of the `ApexPages.KnowledgeArticleVersionStandardController` class using the
specified knowledge article.

##### KnowledgeArticleVersionStandardController(article)

Creates a new instance of the `ApexPages.KnowledgeArticleVersionStandardController` class using the specified
knowledge article.

Signature

```
   public KnowledgeArticleVersionStandardController(SObject article)

```

Parameters

```
   article
```

Type: SObject

The knowledge article, such as `FAQ_kav` .

#### KnowledgeArticleVersionStandardController Methods The following are instance methods for KnowledgeArticleVersionStandardController .

IN THIS SECTION:

##### getSourceId()

Returns the ID for the source object record when creating a new article from another object.

setDataCategory(categoryGroup, category)
Specifies a default data category for the specified data category group when creating a new article.

##### getSourceId()

Returns the ID for the source object record when creating a new article from another object.

Signature

```
   public String getSourceId()

```

Return Value

Type: String


### Apex Reference Guide Message Class

##### setDataCategory(categoryGroup, category)

Specifies a default data category for the specified data category group when creating a new article.

Signature

```
   public Void setDataCategory(String categoryGroup, String category)

```

Parameters

```
   categoryGroup
```

Type: String

```
   category
```

Type: String

Return Value

Type: Void

### Message Class

Contains validation errors that occur when the user saves the page that uses a standard controller.

Namespace

ApexPages

Usage

When using a standard controller, all validation errors, both custom and standard, that occur when the user saves the page are automatically
added to the page error collections. If an `inputField` component is bound to the field with an error, the message is added to the
[component’s error collection. All messages are added to the page’s error collection. For more information, see Validation Rules and](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_std.htm#validation_rules_and_standard_controllers)
[Standard Controllers in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_std.htm#validation_rules_and_standard_controllers) _Visualforce Developer's Guide_ .

If your application uses a custom controller or extension, you must use the `message` class for collecting errors.

Instantiation

In a custom controller or controller extension, you can instantiate a Message in one of these ways:


Apex Reference Guide Message Class

**•** `ApexPages.Message myMsg = new ApexPages.Message(ApexPages.` _**`severity`**_ `,` _**`summary`**_ `);`

where `ApexPages.` _`severity`_ is the enum that determines how severe a message is, and _`summary`_ is the String used to
summarize the message. For example:

```
     ApexPages.Message myMsg = new ApexPages.Message(ApexPages.Severity.FATAL, 'my error

     msg');

```

**•** `ApexPages.Message myMsg = new ApexPages.Message(ApexPages.` _**`severity`**_ `,` _**`summary`**_ `,` _**`detail`**_ `);`

where `ApexPages.` _`severity`_ is the enum that determines how severe a message is, _`summary`_ is the String used to
summarize the message, and _`detail`_ is the String used to provide more detailed information about the error.

ApexPages.Severity Enum

To specify the severity of the message, use the `ApexPages.Severity` enum values. The following are the valid values:

**•** `CONFIRM`

**•** `ERROR`

**•** `FATAL`

**•** `INFO`

**•** `WARNING`

All enums have access to standard methods, such as `name` and `value` .

IN THIS SECTION:

#### Message Constructors

Message Methods

#### Message Constructors The following are constructors for Message .

IN THIS SECTION:

##### Message(severity, summary)

Creates a new instance of the `ApexPages.Message` class using the specified message severity and summary.

Message(severity, summary, detail)
Creates a new instance of the `ApexPages.Message` class using the specified message severity, summary, and message detail.

Message(severity, summary, detail, id)
Creates a new instance of the `ApexPages.Message` class using the specified severity, summary, detail, and component ID.

##### Message(severity, summary)

Creates a new instance of the `ApexPages.Message` class using the specified message severity and summary.


Apex Reference Guide Message Class

Signature

```
   public Message(ApexPages.Severity severity, String summary)

```

Parameters

```
   severity
```

Type: ApexPages.Severity

The severity of a Visualforce message.

```
   summary
```

Type: String

The summary Visualforce message.

##### Message(severity, summary, detail)

Creates a new instance of the `ApexPages.Message` class using the specified message severity, summary, and message detail.

Signature

```
   public Message(ApexPages.Severity severity, String summary, String detail)

```

Parameters

```
   severity
```

Type: ApexPages.Severity

The severity of a Visualforce message.

```
   summary
```

Type: String

The summary Visualforce message.

```
   detail
```

Type: String

The detailed Visualforce message.

##### Message(severity, summary, detail, id)

Creates a new instance of the `ApexPages.Message` class using the specified severity, summary, detail, and component ID.

Signature

```
   public Message(ApexPages.Severity severity, String summary, String detail, String id)

```

Parameters

```
   severity
```

Type: ApexPages.Severity

The severity of a Visualforce message.


Apex Reference Guide Message Class

```
   summary
```

Type: String

The summary Visualforce message.

```
   detail
```

Type: String

The detailed Visualforce message.

```
   id
```

Type: String

The ID of the Visualforce component to associate with the message, for example, a form field with an error.

#### Message Methods The following are methods for Message . All are instance methods.

IN THIS SECTION:

##### getComponentLabel()

Returns the label of the associated `inputField` component. If no label is defined, this method returns `null` .

##### getDetail()

Returns the value of the detail parameter used to create the message. If no detail String was specified, this method returns `null` .

getSeverity()
Returns the severity enum used to create the message.

getSummary()
Returns the summary String used to create the message.

##### getComponentLabel()

Returns the label of the associated `inputField` component. If no label is defined, this method returns `null` .

Signature

```
   public String getComponentLabel()

```

Return Value

Type: String

##### getDetail()

Returns the value of the detail parameter used to create the message. If no detail String was specified, this method returns `null` .

Signature

```
   public String getDetail()

```


### Apex Reference Guide StandardController Class

Return Value

Type: String

##### getSeverity()

Returns the severity enum used to create the message.

Signature

```
   public ApexPages.Severity getSeverity()

```

Return Value

Type: ApexPages.Severity

##### getSummary()

Returns the summary String used to create the message.

Signature

```
   public String getSummary()

```

Return Value

Type: String

### StandardController Class

Use a StandardController when defining an extension for a standard controller.

Namespace

ApexPages

Usage

StandardController objects reference the pre-built Visualforce controllers provided by Salesforce. The only time it is necessary to refer
to a StandardController object is when defining an extension for a standard controller. StandardController is the data type of the single
argument in the extension class constructor.

Instantiation

You can instantiate a StandardController in the following way:

```
   ApexPages.StandardController sc = new ApexPages.StandardController(sObject);

```


Apex Reference Guide StandardController Class

Example

The following example shows how a StandardController object can be used in the constructor for a standard controller extension:

```
   public class myControllerExtension {

      private final Account acct;

      // The extension constructor initializes the private member

      // variable acct by using the getRecord method from the standard

      // controller.

      public myControllerExtension(ApexPages.StandardController stdController) {

        this.acct = (Account)stdController.getRecord();

      }

      public String getGreeting() {

        return 'Hello ' + acct.name + ' (' + acct.id + ')';

      }

   }

```

The following Visualforce markup shows how the controller extension from above can be used in a page:

```
   <apex:page standardController="Account" extensions="myControllerExtension">

      {!greeting} <p/>

      <apex:form>

        <apex:inputField value="{!account.name}"/> <p/>

        <apex:commandButton value="Save" action="{!save}"/>

      </apex:form>

   </apex:page>

```

IN THIS SECTION:

#### StandardController Constructors

StandardController Methods

#### StandardController Constructors The following are constructors for StandardController .

IN THIS SECTION:

##### StandardController(controllerSObject)

Creates a new instance of the `ApexPages.StandardController` class for the specified standard or custom object.

##### StandardController(controllerSObject)

Creates a new instance of the `ApexPages.StandardController` class for the specified standard or custom object.

Signature

```
   public StandardController(SObject controllerSObject)

```


Apex Reference Guide StandardController Class

Parameters

```
   controllerSObject
```

Type: SObject

A standard or custom object.

#### StandardController Methods The following are methods for StandardController . All are instance methods.

IN THIS SECTION:

##### addFields(fieldNames)

When a Visualforce page is loaded, the fields accessible to the page are based on the fields referenced in the Visualforce markup.
This method adds a reference to each field specified in `fieldNames` so that the controller can explicitly access those fields as
well.

cancel()
Returns the PageReference of the cancel page.

delete()
Deletes record and returns the PageReference of the delete page.

edit()
Returns the PageReference of the standard edit page.

getId()
Returns the ID of the record that is currently in context, based on the value of the `id` query string parameter in the Visualforce page
URL.

getRecord()
Returns the record that is currently in context, based on the value of the `id` query string parameter in the Visualforce page URL.

reset()
Forces the controller to reacquire access to newly referenced fields. Any changes made to the record prior to this method call are
discarded.

save()
Saves changes and returns the updated PageReference.

view()
Returns the PageReference object of the standard detail page.

##### addFields(fieldNames)

When a Visualforce page is loaded, the fields accessible to the page are based on the fields referenced in the Visualforce markup. This
method adds a reference to each field specified in `fieldNames` so that the controller can explicitly access those fields as well.

Signature

```
   public Void addFields(List<String> fieldNames)

```


Apex Reference Guide StandardController Class

Parameters

```
   fieldNames
```

Type: List<String>

Return Value

Type: Void

Usage

This method should be called before a record has been loaded—typically, it's called by the controller's constructor. If this method is
called outside of the constructor, you must use the `reset()` method before calling `addFields()` .

The strings in `fieldNames` can either be the API name of a field, such as AccountId, or they can be explicit relationships to fields,
such as `something__r.myField__c` .

This method is only for controllers used by dynamicVisualforce bindings.

##### cancel()

Returns the PageReference of the cancel page.

Signature

```
   public System.PageReference cancel()

```

Return Value

Type: System.PageReference

##### delete()

Deletes record and returns the PageReference of the delete page.

Signature

```
   public System.PageReference delete()

```

Return Value

Type: System.PageReference

##### edit()

Returns the PageReference of the standard edit page.

Signature

```
   public System.PageReference edit()

```


Apex Reference Guide StandardController Class

Return Value

Type: System.PageReference

##### getId()

Returns the ID of the record that is currently in context, based on the value of the `id` query string parameter in the Visualforce page
URL.

Signature

```
   public String getId()

```

Return Value

Type: String

##### getRecord()

Returns the record that is currently in context, based on the value of the `id` query string parameter in the Visualforce page URL.

Signature

```
   public SObject getRecord()

```

Return Value

Type: sObject

Usage

Note that only the fields that are referenced in the associated Visualforce markup are available for querying on this SObject. All other
fields, including fields from any related objects, must be queried using a SOQL expression.

Tip: You can work around this restriction by including a hidden component that references any additional fields that you want
to query. Hide the component from display by setting the component's `rendered` attribute to `false` .

Example

```
   <apex:outputText

   value="{!account.billingcity}

   {!account.contacts}"

   rendered="false"/>

##### reset()

```

Forces the controller to reacquire access to newly referenced fields. Any changes made to the record prior to this method call are
discarded.

Signature

```
   public Void reset()

```


### Apex Reference Guide StandardSetController Class

Return Value

Type: Void

Usage

This method is only used if `addFields` is called outside the constructor, and it must be called directly before `addFields` .

This method is only for controllers used by dynamicVisualforce bindings.

##### save()

Saves changes and returns the updated PageReference.

Signature

```
   public System.PageReference save()

```

Return Value

Type: System.PageReference

##### view()

Returns the PageReference object of the standard detail page.

Signature

```
   public System.PageReference view()

```

Return Value

Type: System.PageReference

### StandardSetController Class StandardSetController objects allow you to create list controllers similar to, or as extensions of, the pre-built Visualforce list

controllers provided by Salesforce.

Namespace

ApexPages

Usage

### The StandardSetController class also contains a prototype object . This is a single sObject contained within the Visualforce

StandardSetController class. If the prototype object's fields are set, those values are used during the save action, meaning that the values
are applied to every record in the set controller's collection. This is useful for writing pages that perform mass updates (applying identical
changes to fields within a collection of objects).

Note: Fields that are required in other Salesforce objects will keep the same requiredness when used by the prototype object.


Apex Reference Guide StandardSetController Class

Instantiation

You can instantiate a StandardSetController in either of the following ways:

**•** From a list of sObjects:

```
     List<account> accountList = [SELECT Name FROM Account LIMIT 20];

     ApexPages.StandardSetController ssc = new ApexPages.StandardSetController(accountList);

```

**•** From a query locator:

```
     ApexPages.StandardSetController ssc =

     new ApexPages.StandardSetController(Database.getQueryLocator([SELECT Name,CloseDate FROM

      Opportunity]));

```

Note: The maximum record limit for StandardSetController is 10,000 records. Instantiating StandardSetController using a query
locator returning more than 10,000 records causes a LimitException to be thrown. However, instantiating StandardSetController
with a list of more than 10,000 records doesn’t throw an exception, and instead truncates the records to the limit.

Example

The following example shows how a StandardSetController object can be used in the constructor for a custom list controller:

```
   public class opportunityList2Con {

      // ApexPages.StandardSetController must be instantiated

      // for standard list controllers

      public ApexPages.StandardSetController setCon {

        get {

           if(setCon == null) {

             setCon = new ApexPages.StandardSetController(Database.getQueryLocator(

               [SELECT Name, CloseDate FROM Opportunity]));

           }

           return setCon;

        }

        set;

      }

      // Initialize setCon and return a list of records

      public List<Opportunity> getOpportunities() {

        return (List<Opportunity>) setCon.getRecords();

      }

   }

```

The following Visualforce markup shows how the controller above can be used in a page:

```
   <apex:page controller="opportunityList2Con">

      <apex:pageBlock>

        <apex:pageBlockTable value="{!opportunities}" var="o">

           <apex:column value="{!o.Name}"/>

           <apex:column value="{!o.CloseDate}"/>

        </apex:pageBlockTable>

      </apex:pageBlock>

   </apex:page>

```


Apex Reference Guide StandardSetController Class

IN THIS SECTION:

#### StandardSetController Constructors

StandardSetController Methods

#### StandardSetController Constructors The following are constructors for StandardSetController .

IN THIS SECTION:

##### StandardSetController(queryLocator)

Creates an instance of the `ApexPages.StandardSetController` class for the list of objects returned by the query locator.

##### StandardSetController(controllerSObjects)

Creates an instance of the `ApexPages.StandardSetController` class for the specified list of standard or custom objects.

##### StandardSetController(queryLocator)

Creates an instance of the `ApexPages.StandardSetController` class for the list of objects returned by the query locator.

Signature

```
   public StandardSetController(Database.QueryLocator queryLocator)

```

Parameters

```
   queryLocator
```

Type: Database.QueryLocator

A query locator representing a list of sObjects.

##### StandardSetController(controllerSObjects)

Creates an instance of the `ApexPages.StandardSetController` class for the specified list of standard or custom objects.

Signature

```
   public StandardSetController(List<sObject> controllerSObjects)

```

Parameters

```
   controllerSObjects
```

Type: List on page 3891<sObject on page 4088>

A List of standard or custom objects.

Example

```
   List<account> accountList = [SELECT Name FROM Account LIMIT 20];

   ApexPages.StandardSetController ssc = new ApexPages.StandardSetController(accountList);

```


Apex Reference Guide StandardSetController Class

#### StandardSetController Methods The following are methods for StandardSetController . All are instance methods.

IN THIS SECTION:

cancel()
Returns the PageReference of the original page, if known, or the home page.

first()
Changes the set of records that the controller returns to the first page of records.

getCompleteResult()
Indicates whether there are more records in the set than the maximum record limit. If this is false, there are more records than you
can process using the list controller. The maximum record limit is 10,000 records.

getFilterId()
Returns the ID of the filter that is currently in context.

getHasNext()
Indicates whether there are more records after the current page set.

getHasPrevious()
Indicates whether there are more records before the current page set.

getListViewOptions()
Returns a list of the listviews available to the current user.

getPageNumber()
Returns the page number of the current page set. Note that the first page returns 1.

getPageSize()
Returns the number of records included in each page set.

getRecord()
Returns the sObject that represents the changes to the selected records. This retrieves the prototype object contained within the
class, and is used for performing mass updates.

getRecords()
Returns the list of sObjects in the current page set. This list is immutable, i.e. you can't call `clear` () on it.

getResultSize()
Returns the number of records in the set.

getSelected()
Returns the list of sObjects that have been selected.

last()
Changes the set of records that the controller returns to the last page of records.

next()
Changes the set of records that the controller returns to the next page of records.

previous()
Changes the set of records that the controller returns to the previous page of records.


Apex Reference Guide StandardSetController Class

save()
Inserts new records or updates existing records that have been changed. After this operation is finished, it returns a PageReference
to the original page, if known, or the home page.

setFilterID(filterId)
Sets the filter ID of the controller.

setpageNumber(pageNumber)
Sets the page number.

setPageSize(pageSize)
Sets the number of records in each page set.

setSelected(selectedRecords)
Set the selected records to the records specified in the _`selectedRecords`_ argument.

##### cancel()

Returns the PageReference of the original page, if known, or the home page.

Signature

```
   public System.PageReference cancel()

```

Return Value

Type: System.PageReference

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_actions.htm)

##### **`first()`**

Changes the set of records that the controller returns to the first page of records.

Signature

```
   public Void first()

```

Return Value

Type: Void

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_actions.htm)

##### getCompleteResult()

Indicates whether there are more records in the set than the maximum record limit. If this is false, there are more records than you can
process using the list controller. The maximum record limit is 10,000 records.


Apex Reference Guide StandardSetController Class

Signature

```
   public Boolean getCompleteResult()

```

Return Value

Type: Boolean

##### getFilterId()

Returns the ID of the filter that is currently in context.

Note: The `getFilterID()` method doesn’t support list views without filter IDs, such as the Recently Viewed list view. In
these cases, the method returns the first filter ID of the object’s available list views. If called within an `<apex:enhancedList>`
component, the method returns the filter ID of the last used list view.

Signature

```
   public String getFilterId()

```

Return Value

Type: String

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_actions.htm)

_Visualforce Developer Guide_ [: List Views with Standard List Controllers](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_list_views.htm)

##### getHasNext()

Indicates whether there are more records after the current page set.

Signature

```
   public Boolean getHasNext()

```

Return Value

Type: Boolean

##### getHasPrevious()

Indicates whether there are more records before the current page set.

Signature

```
   public Boolean getHasPrevious()

```

Return Value

Type: Boolean


Apex Reference Guide StandardSetController Class

##### getListViewOptions()

Returns a list of the listviews available to the current user.

Signature

```
   public System.SelectOption getListViewOptions()

```

Return Value

Type: System.SelectOption[]

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_actions.htm)

_Visualforce Developer Guide_ [: List Views with Standard List Controllers](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_list_views.htm)

##### getPageNumber()

Returns the page number of the current page set. Note that the first page returns 1.

Signature

```
   public Integer getPageNumber()

```

Return Value

Type: Integer

##### getPageSize()

Returns the number of records included in each page set.

Signature

```
   public Integer getPageSize()

```

Return Value

Type: Integer

##### getRecord()

Returns the sObject that represents the changes to the selected records. This retrieves the prototype object contained within the class,
and is used for performing mass updates.

Signature

```
   public sObject getRecord()

```


Apex Reference Guide StandardSetController Class

Return Value

Type: sObject

SEE ALSO:

_Visualforce Developer Guide_ [: Building a Custom List Controller](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_custom_list_controller.htm)

##### getRecords()

Returns the list of sObjects in the current page set. This list is immutable, i.e. you can't call `clear` () on it.

Signature

```
   public sObject[] getRecords()

```

Return Value

Type: sObject[]

SEE ALSO:

_Visualforce Developer Guide_ [: Building a Custom List Controller](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_custom_list_controller.htm)

##### getResultSize()

Returns the number of records in the set.

Signature

```
   public Integer getResultSize()

```

Return Value

Type: Integer

##### getSelected()

Returns the list of sObjects that have been selected.

Signature

```
   public sObject[] getSelected()

```

Return Value

Type: sObject[]

##### **`last()`**

Changes the set of records that the controller returns to the last page of records.


Apex Reference Guide StandardSetController Class

Signature

```
   public Void last()

```

Return Value

Type: Void

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_actions.htm)

##### **`next()`**

Changes the set of records that the controller returns to the next page of records.

Signature

```
   public Void next()

```

Return Value

Type: Void

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_actions.htm)

##### **`previous()`**

Changes the set of records that the controller returns to the previous page of records.

Signature

```
   public Void previous()

```

Return Value

Type: Void

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_actions.htm)

##### save()

Inserts new records or updates existing records that have been changed. After this operation is finished, it returns a PageReference to
the original page, if known, or the home page.

Signature

```
   public System.PageReference save()

```


Apex Reference Guide StandardSetController Class

Return Value

Type: System.PageReference

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_actions.htm)

##### setFilterID(filterId)

Sets the filter ID of the controller.

Signature

```
   public Void setFilterID(String filterId)

```

Parameters

```
   filterId
```

Type: String

Return Value

Type: Void

##### setpageNumber(pageNumber)

Sets the page number.

Signature

```
   public Void setpageNumber(Integer pageNumber)

```

Parameters

```
   pageNumber
```

Type: Integer

Return Value

Type: Void

##### setPageSize(pageSize)

Sets the number of records in each page set.

Signature

```
   public Void setPageSize(Integer pageSize)

```


Apex Reference Guide StandardSetController Class

Parameters

```
   pageSize
```

Type: Integer

Return Value

Type: Void

##### **`setSelected(selectedRecords)`**

Set the selected records to the records specified in the _`selectedRecords`_ argument.

Signature

```
   public Void setSelected(sObject[] selectedRecords)

```

Parameters

```
   selectedRecords
```

Type: sObject[]

Return Value

Type: Void

Usage

Use the `setSelected()` method in your Apex controller or controller extension to manually set the records displayed on a Visualforce
page. The `setSelected()` method overwrites any previously selected records with the records specified in the _`selectedRecords`_
argument.

Example

`AccountNamePage` shows a table of account names. `MyControllerExtension` ’s constructor contains a SOQL query that
returns a list of accounts. This list is passed into `setSelected()` so that the account records in the list are selected and displayed
in the table.

```
   <!-- AccountNamePage.page -->

   <apex:page standardController="Account" recordSetVar="accounts"

   extensions="MyControllerExtension">

      <apex:pageBlock>

        <apex:pageBlockTable value="{!accounts}" var="acc">

           <apex:column value="{!acc.name}"/>

        </apex:pageBlockTable>

      </apex:pageBlock>

   </apex:page>

   // MyControllerExtension.cls

   public with sharing class MyControllerExtension {

      private ApexPages.StandardSetController setController;

```


## Apex Reference Guide AppLauncher Namespace

```
      public MyControllerExtension(ApexPages.StandardSetController setController) {

        this.setController = setController;

        Account [] records = [SELECT Id, Name FROM Account LIMIT 30];

        setController.setSelected(records);

      }

   }

```

SEE ALSO:

_Visualforce Developer Guide_ [: Accessing Data with List Controllers](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_sosc_access_data.htm)

## AppLauncher Namespace The AppLauncher namespace provides methods for managing the appearance of apps in the App Launcher, including their visibility

and sort order.

## The following class is in the AppLauncher namespace.

IN THIS SECTION:

### AppMenu Class

Contains methods to set the appearance of apps in the App Launcher.

ChangePasswordController Class
This class and its methods are for internal use only.

CommunityLogoController Class
This class and its methods are for internal use only.

EmployeeLoginLinkController Class
This class and its methods are for internal use only.

ForgotPasswordController Class
This class and its methods are for internal use only.

IdentityHeaderController Class
This class and its methods are for internal use only.

LoginFormController Class
This class and its methods are for internal use only.

SelfRegisterController Class
This class and its methods are for internal use only.

SocialLoginController Class
This class and its methods are for internal use only.

### AppMenu Class

Contains methods to set the appearance of apps in the App Launcher.


Apex Reference Guide AppMenu Class

Namespace

AppLauncher

IN THIS SECTION:

#### AppMenu Methods AppMenu Methods The following are methods for AppMenu .

IN THIS SECTION:

##### setAppVisibility(appMenuItemId, isVisible)

Shows or hides specific apps in the App Launcher.

##### setOrgSortOrder(appIds)

Sets the organization-wide default sort order for the App Launcher based on a List of app menu item IDs in the desired order.

setUserSortOrder(appIds)
Sets an individual user’s default sort order for the App Launcher based on a List of app menu item IDs in the desired order.

##### setAppVisibility(appMenuItemId, isVisible)

Shows or hides specific apps in the App Launcher.

Signature

```
   public static void setAppVisibility(Id appMenuItemId, Boolean isVisible)

```

Parameters

```
   appMenuItemId
```

Type: Id

The 15-character application ID value for an app. For more information, see the `ApplicationId` [field for AppMenuItem or the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_appmenuitem.htm)
`AppMenuItemId` [field for UserAppMenuItem in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_userappmenuitem.htm) _Salesforce Object Reference_

```
   isVisible
```

Type: Boolean

If `true`, the app is visible.

Return Value

Type: void

##### setOrgSortOrder(appIds)

Sets the organization-wide default sort order for the App Launcher based on a List of app menu item IDs in the desired order.


### Apex Reference Guide ChangePasswordController Class

Signature

```
   public static void setOrgSortOrder(List<Id> appIds)

```

Parameters

```
   appIds
```

Type: List<Id>

A list of application ID values. For more information, see the `ApplicationId` [field for AppMenuItem in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_appmenuitem.htm) _Salesforce Object_
_Reference_ .

Return Value

Type: void

##### setUserSortOrder(appIds)

Sets an individual user’s default sort order for the App Launcher based on a List of app menu item IDs in the desired order.

Signature

```
   public static void setUserSortOrder(List<Id> appIds)

```

Parameters

```
   appIds
```

Type: List<Id>

A list of application ID values. For more information, see the `AppMenuItemId` [field for UserAppMenuItem in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_userappmenuitem.htm) _Salesforce Object_
_Reference_ .

Return Value

Type: void

### ChangePasswordController Class

This class and its methods are for internal use only.

Namespace

AppLauncher

### CommunityLogoController Class

This class and its methods are for internal use only.

Namespace

AppLauncher


### Apex Reference Guide EmployeeLoginLinkController Class EmployeeLoginLinkController Class

This class and its methods are for internal use only.

Namespace

AppLauncher

### ForgotPasswordController Class

This class and its methods are for internal use only.

Namespace

AppLauncher

### IdentityHeaderController Class

This class and its methods are for internal use only.

Namespace

AppLauncher

### LoginFormController Class

This class and its methods are for internal use only.

Namespace

AppLauncher

### SelfRegisterController Class

This class and its methods are for internal use only.

Namespace

AppLauncher

### SocialLoginController Class

This class and its methods are for internal use only.

Namespace

AppLauncher


## Apex Reference Guide Approval Namespace Approval Namespace The Approval namespace provides classes and methods for approval processes. The following are the classes in the Approval namespace.

IN THIS SECTION:

### LockResult Class

The result of a record lock returned by a `System.Approval.lock()` method.

ProcessRequest Class
The `ProcessRequest` class is the parent class for the `ProcessSubmitRequest` and `ProcessWorkitemRequest`
classes. Use the `ProcessRequest` class to write generic Apex that can process objects from either class.

ProcessResult Class
After you submit a record for approval, use the `ProcessResult` class to process the results of an approval process.

ProcessSubmitRequest Class
Use the `ProcessSubmitRequest` class to submit a record for approval.

ProcessWorkitemRequest Class
Use the `ProcessWorkitemRequest` class for processing an approval request after it is submitted.

UnlockResult Class
The result of a record unlock, returned by a `System.Approval.unlock()` method.

### LockResult Class

The result of a record lock returned by a `System.Approval.lock()` method.

Namespace

## Approval

Usage

The `System.Approval.lock()` methods return Approval.LockResult objects. Each element in a LockResult array corresponds
to an element in the ID or sObject array passed as a parameter to a `lock` method. The first element in the LockResult array corresponds
to the first element in the ID or sObject array, the second element corresponds to the second element, and so on. If only one ID or sObject
is passed in, the LockResult array contains a single element.

Example

The following example obtains and iterates through the returned Approval.LockResult objects. It locks some queried accounts using
`Approval.lock` with a `false` second parameter to allow partial processing of records on failure. Next, it iterates through the
results to determine whether the operation was successful for each record. It writes the ID of every record that was processed successfully
to the debug log, or writes error messages and failed fields of the failed records.

```
   // Query the accounts to lock

   Account[] accts = [SELECT Id from Account WHERE Name LIKE 'Acme%'];

   // Lock the accounts

```


Apex Reference Guide LockResult Class

```
   Approval.LockResult[] lrList = Approval.lock(accts, false);

   // Iterate through each returned result

   for(Approval.LockResult lr : lrList) {

      if (lr.isSuccess()) {

        // Operation was successful, so get the ID of the record that was processed

        System.debug('Successfully locked account with ID: ' + lr.getId());

      }

      else {

        // Operation failed, so get all errors

        for(Database.Error err : lr.getErrors()) {

           System.debug('The following error has occurred.');

           System.debug(err.getStatusCode() + ': ' + err.getMessage());

           System.debug('Account fields that affected this error: ' + err.getFields());

        }

      }

   }

```

IN THIS SECTION:

#### LockResult Methods

SEE ALSO:

Approval Class

#### LockResult Methods The following are methods for LockResult .

IN THIS SECTION:

##### getErrors()

If an error occurred, returns an array of one or more database error objects, providing the error code and description.

getId()
Returns the ID of the sObject you are trying to lock.

isSuccess()
A Boolean value that is set to `true` if the lock operation is successful for this object, or `false` otherwise.

##### getErrors()

If an error occurred, returns an array of one or more database error objects, providing the error code and description.

Signature

```
   public List<Database.Error> getErrors()

```

Return Value

Type: List<Database.Error>


### Apex Reference Guide ProcessRequest Class

##### getId()

Returns the ID of the sObject you are trying to lock.

Signature

```
   public Id getId()

```

Return Value

Type: Id

Usage

If the field contains a value, the object was locked. If the field is empty, the operation was not successful.

##### isSuccess()

A Boolean value that is set to `true` if the lock operation is successful for this object, or `false` otherwise.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### ProcessRequest Class The ProcessRequest class is the parent class for the ProcessSubmitRequest and ProcessWorkitemRequest classes. Use the ProcessRequest class to write generic Apex that can process objects from either class.

Namespace

Approval

Usage

The request must be instantiated via the child classes, `ProcessSubmitRequest` and `ProcessWorkItemRequest` .

#### ProcessRequest Methods

### The following are methods for ProcessRequest . All are instance methods.

IN THIS SECTION:

getComments()
Returns the comments that have been added previously to the approval request.


Apex Reference Guide ProcessRequest Class

##### getNextApproverIds()

Returns the list of user IDs of user specified as approvers.

##### setComments(comments)

Sets the comments to be added to the approval request.

setNextApproverIds(nextApproverIds)
If the next step in your approval process is another Apex approval process, you specify exactly one user ID as the next approver. If
not, you cannot specify a user ID and this method must be `null` . This method sets the ActorId field of the associated
ProcessInstanceWorkItem.

##### getComments()

Returns the comments that have been added previously to the approval request.

Signature

```
   public String getComments()

```

Return Value

Type: String

##### getNextApproverIds()

Returns the list of user IDs of user specified as approvers.

Signature

```
   public ID[] getNextApproverIds()

```

Return Value

Type: ID[]

##### setComments(comments)

Sets the comments to be added to the approval request.

Signature

```
   public Void setComments(String comments)

```

Parameters

```
   comments
```

Type: String

Return Value

Type: Void


### Apex Reference Guide ProcessResult Class

##### setNextApproverIds(nextApproverIds)

If the next step in your approval process is another Apex approval process, you specify exactly one user ID as the next approver. If not,
you cannot specify a user ID and this method must be `null` . This method sets the ActorId field of the associated ProcessInstanceWorkItem.

Signature

```
   public Void setNextApproverIds(ID[] nextApproverIds)

```

Parameters

```
   nextApproverIds
```

Type: ID[]

Must be a single-entry list.

Return Value

Type: Void

### ProcessResult Class After you submit a record for approval, use the ProcessResult class to process the results of an approval process.

Namespace

Approval

Usage

A ProcessResult object is returned by the `process` method. You must specify the Approval namespace when creating an instance of
this class. For example:

```
   Approval.ProcessResult result = Approval.process(req1);

#### ProcessResult Methods

### The following are methods for ProcessResult . All are instance methods.

```

IN THIS SECTION:

getEntityId()
The ID of the record being processed.

getErrors()
If an error occurred, returns an array of one or more database error objects including the error code and description.

getInstanceId()
The ID of the approval process that has been submitted for approval.

getInstanceStatus()
The status of the current approval process. Valid values are: Approved, Rejected, Removed or Pending.


Apex Reference Guide ProcessResult Class

getNewWorkitemIds()
The IDs of the new items submitted to the approval process. There can be 0 or 1 approval processes.

isSuccess()
A Boolean value that is set to `true` if the approval process completed successfully; otherwise, it is set to `false` .

##### getEntityId()

The ID of the record being processed.

Signature

```
   public String getEntityId()

```

Return Value

Type: String

##### getErrors()

If an error occurred, returns an array of one or more database error objects including the error code and description.

Signature

```
   public Database.Error[] getErrors()

```

Return Value

Type: Database.Error[]

##### getInstanceId()

The ID of the approval process that has been submitted for approval.

Signature

```
   public String getInstanceId()

```

Return Value

Type: String

##### getInstanceStatus()

The status of the current approval process. Valid values are: Approved, Rejected, Removed or Pending.

Signature

```
   public String getInstanceStatus()

```


### Apex Reference Guide ProcessSubmitRequest Class

Return Value

Type: String

##### getNewWorkitemIds()

The IDs of the new items submitted to the approval process. There can be 0 or 1 approval processes.

Signature

```
   public ID[] getNewWorkitemIds()

```

Return Value

Type: ID[]

##### isSuccess()

A Boolean value that is set to `true` if the approval process completed successfully; otherwise, it is set to `false` .

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### ProcessSubmitRequest Class Use the ProcessSubmitRequest class to submit a record for approval.

Namespace

Approval

Usage

You must specify the Approval namespace when creating an instance of this class. The constructor for this class takes no arguments.
For example:

```
   Approval.ProcessSubmitRequest psr = new Approval.ProcessSubmitRequest();

```

Inherited Methods

### In addition to the methods listed, the ProcessSubmitRequest class has access to all the methods in its parent class, ProcessRequest

Class.

**•** getComments()

**•** getNextApproverIds()


Apex Reference Guide ProcessSubmitRequest Class

**•** setComments(comments)

**•** setNextApproverIds(nextApproverIds)

Example

[To view sample code, refer to Approval Processing Example.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_process_example.htm)

#### ProcessSubmitRequest Methods The following are methods for ProcessSubmitRequest . All are instance methods.

IN THIS SECTION:

##### getObjectId()

Returns the ID of the record that has been submitted for approval. For example, it can return an account, contact, or custom object
record.

getProcessDefinitionNameOrId()
Returns the developer name or ID of the process definition.

getSkipEntryCriteria()
If `getProcessDefinitionNameOrId()` returns a value other than `null`, `getSkipEntryCriteria()` determines
whether to evaluate the entry criteria for the process ( `true` ) or not ( `false` ).

getSubmitterId()
Returns the user ID of the submitter requesting the approval record. The user must be one of the allowed submitters in the process
definition setup.

setObjectId(recordId)
Sets the ID of the record to be submitted for approval. For example, it can specify an account, contact, or custom object record.

setProcessDefinitionNameOrId(nameOrId)
Sets the developer name or ID of the process definition to be evaluated.

setSkipEntryCriteria(skipEntryCriteria)
If the process definition name or ID is not null, `setSkipEntryCriteria()` determines whether to evaluate the entry criteria
for the process ( `true` ) or not ( `false` ).

setSubmitterId(userID)
Sets the user ID of the submitter requesting the approval record. The user must be one of the allowed submitters in the process
definition setup. If you don’t set a submitter ID, the process uses the current user as the submitter.

##### getObjectId()

Returns the ID of the record that has been submitted for approval. For example, it can return an account, contact, or custom object
record.

Signature

```
   public String getObjectId()

```


Apex Reference Guide ProcessSubmitRequest Class

Return Value

Type: String

##### getProcessDefinitionNameOrId()

Returns the developer name or ID of the process definition.

Signature

```
   public String getProcessDefinitionNameOrId()

```

Return Value

Type: String

Usage

The default is null. If the return value is `null`, when a user submits a record for approval Salesforce evaluates the entry criteria for all
processes applicable to the user.

##### getSkipEntryCriteria() If getProcessDefinitionNameOrId() returns a value other than null, getSkipEntryCriteria() determines

whether to evaluate the entry criteria for the process ( `true` ) or not ( `false` ).

Signature

```
   public Boolean getSkipEntryCriteria()

```

Return Value

Type: Boolean

##### getSubmitterId()

Returns the user ID of the submitter requesting the approval record. The user must be one of the allowed submitters in the process
definition setup.

Signature

```
   public String getSubmitterId()

```

Return Value

Type: String

##### setObjectId(recordId)

Sets the ID of the record to be submitted for approval. For example, it can specify an account, contact, or custom object record.


Apex Reference Guide ProcessSubmitRequest Class

Signature

```
   public Void setObjectId(String recordId)

```

Parameters

```
   recordId
```

Type: String

Return Value

Type: Void

##### setProcessDefinitionNameOrId(nameOrId)

Sets the developer name or ID of the process definition to be evaluated.

Signature

```
   public Void setProcessDefinitionNameOrId(String nameOrId)

```

Parameters

```
   nameOrId
```

Type: String

The process definition developer name or process definition ID. The record is submitted to this specific process. If set to `null`,
submission of a record approval follows standard evaluation; that is, every entry criteria of the process definition in the process order
is evaluated and the one that satisfies is picked and submitted.

Return Value

Type: Void

Usage

If the process definition name or ID is not set via this method, then by default it is null. If it is null, the submission of a record for approval
evaluates entry criteria for all processes applicable to the submitter. The order of evaluation is based on the process order of the setup.

##### setSkipEntryCriteria(skipEntryCriteria)

If the process definition name or ID is not null, `setSkipEntryCriteria()` determines whether to evaluate the entry criteria for
the process ( `true` ) or not ( `false` ).

Signature

```
   public Void setSkipEntryCriteria(Boolean skipEntryCriteria)

```

Parameters

```
   skipEntryCriteria
```

Type: Boolean


### Apex Reference Guide ProcessWorkitemRequest Class

If set to `true`, request submission skips the evaluation of entry criteria for the process set in setProcessDefinitionNameOrId(nameOrId).
If the process definition name or ID is not specified, this parameter is ignored and standard evaluation is followed based on process
order. If set to `false`, or if this method isn’t called, the entry criteria is not skipped.

Return Value

Type: Void

##### setSubmitterId(userID)

Sets the user ID of the submitter requesting the approval record. The user must be one of the allowed submitters in the process definition
setup. If you don’t set a submitter ID, the process uses the current user as the submitter.

Signature

```
   public Void setSubmitterId(String userID)

```

Parameters

```
   userID
```

Type: String

The user ID on behalf of which the record is submitted. If set to `null`, the current user is the submitter. If the submitter is not set
with this method, the default submitter is null (the current user).

Return Value

Type: Void

### ProcessWorkitemRequest Class Use the ProcessWorkitemRequest class for processing an approval request after it is submitted.

Namespace

Approval

Usage

You must specify the Approval namespace when creating an instance of this class. The constructor for this class takes no arguments.
For example:

```
   Approval.ProcessWorkitemRequest pwr = new Approval.ProcessWorkitemRequest();

```

Inherited Methods

### In addition to the methods listed, the ProcessWorkitemRequest class has access to all the methods in its parent class,

ProcessRequest Class:

**•** getComments()

**•** getNextApproverIds()


Apex Reference Guide ProcessWorkitemRequest Class

**•** setComments(comments)

**•** setNextApproverIds(nextApproverIds)

#### ProcessWorkitemRequest Methods The following are methods for ProcessWorkitemRequest . All are instance methods.

IN THIS SECTION:

##### getAction()

Returns the type of action already associated with the approval request. Valid values are: Approve, Reject, or Removed.

##### getWorkitemId()

Returns the ID of the approval request that is in the process of being approved, rejected, or removed.

##### setAction(actionType)

Sets the type of action to take for processing an approval request.

setWorkitemId(id)
Sets the ID of the approval request that is being approved, rejected, or removed.

##### getAction()

Returns the type of action already associated with the approval request. Valid values are: Approve, Reject, or Removed.

Signature

```
   public String getAction()

```

Return Value

Type: String

##### getWorkitemId()

Returns the ID of the approval request that is in the process of being approved, rejected, or removed.

Signature

```
   public String getWorkitemId()

```

Return Value

Type: String

##### setAction(actionType)

Sets the type of action to take for processing an approval request.

Signature

```
   public Void setAction(String actionType)

```


### Apex Reference Guide UnlockResult Class

Parameters

```
   actionType
```

Type: String

Valid values are: Approve, Reject, or Removed. Only system administrators can specify Removed.

Return Value

Type: Void

##### setWorkitemId(id)

Sets the ID of the approval request that is being approved, rejected, or removed.

Signature

```
   public Void setWorkitemId(String id)

```

Parameters

```
   id
```

Type: String

Return Value

Type: Void

### UnlockResult Class

The result of a record unlock, returned by a `System.Approval.unlock()` method.

Namespace

Approval

Usage

The `System.Approval.unlock()` methods return Approval.UnlockResult objects. Each element in an UnlockResult array
corresponds to an element in the ID or sObject array passed as a parameter to an `unlock` method. The first element in the UnlockResult
array corresponds to the first element in the ID or sObject array, the second element corresponds to the second element, and so on. If
only one ID or sObject is passed in, the UnlockResult array contains a single element.

Example

The following example shows how to obtain and iterate through the returned Approval.UnlockResult objects. It locks some queried
accounts using `Approval.unlock` with a `false` second parameter to allow partial processing of records on failure. Next, it


Apex Reference Guide UnlockResult Class

iterates through the results to determine whether the operation was successful for each record. It writes the ID of every record that was
processed successfully to the debug log, or writes error messages and failed fields of the failed records.

```
   // Query the accounts to unlock

   Account[] accts = [SELECT Id from Account WHERE Name LIKE 'Acme%'];

   for(Account acct:accts) {

     // Create an approval request for the account

     Approval.ProcessSubmitRequest req1 =

          new Approval.ProcessSubmitRequest();

     req1.setComments('Submitting request for approval.');

     req1.setObjectId(acct.id);

     // Submit the record to specific process and skip the criteria evaluation

     req1.setProcessDefinitionNameOrId('PTO_Request_Process');

     req1.setSkipEntryCriteria(true);

     // Submit the approval request for the account

     Approval.ProcessResult result = Approval.process(req1);

     // Verify the result

     System.assert(result.isSuccess());

   }

   // Unlock the accounts

   Approval.UnlockResult[] urList = Approval.unlock(accts, false);

   // Iterate through each returned result

   for(Approval.UnlockResult ur : urList) {

      if (ur.isSuccess()) {

        // Operation was successful, so get the ID of the record that was processed

        System.debug('Successfully unlocked account with ID: ' + ur.getId());

      }

      else {

        // Operation failed, so get all errors

        for(Database.Error err : ur.getErrors()) {

           System.debug('The following error has occurred.');

           System.debug(err.getStatusCode() + ': ' + err.getMessage());

           System.debug('Account fields that affected this error: ' + err.getFields());

        }

      }

   }

```

IN THIS SECTION:

#### UnlockResult Methods

SEE ALSO:

Approval Class

#### UnlockResult Methods The following are methods for UnlockResult .


Apex Reference Guide UnlockResult Class

IN THIS SECTION:

##### getErrors()

If an error occurred, returns an array of one or more database error objects, providing the error code and description.

##### getId()

Returns the ID of the sObject you are trying to unlock.

##### isSuccess()

A Boolean value that is set to `true` if the unlock operation is successful for this object, or `false` otherwise.

##### getErrors()

If an error occurred, returns an array of one or more database error objects, providing the error code and description.

Signature

```
   public List<Database.Error> getErrors()

```

Return Value

Type: List<Database.Error>

##### getId()

Returns the ID of the sObject you are trying to unlock.

Signature

```
   public Id getId()

```

Return Value

Type: Id

Usage

If the field contains a value, the object was unlocked. If the field is empty, the operation was not successfult.

##### isSuccess()

A Boolean value that is set to `true` if the unlock operation is successful for this object, or `false` otherwise.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean


## Apex Reference Guide Auth Namespace Auth Namespace The Auth namespace provides an interface and classes for single sign-on into Salesforce and session security management. The following is the interface in the Auth namespace.

IN THIS SECTION:

AuthConfiguration Class
Contains methods for configuring settings for users to log in to a Salesforce org using their authentication provider credentials
instead of their Salesforce credentials. The authentication provider can be any authentication provider that supports the OpenID
Connect protocol, such as Google, Facebook, or Twitter. Users log in to either an Experience Cloud site
( `https://` _`MyDomainName`_ `.my.site.com` ) or your My Domain login URL
( `https://` _`MyDomainName`_ `.my.salesforce.com` ).

AuthProviderCallbackState Class
Provides request HTTP headers, body, and query parameters to the `AuthProviderPlugin.handleCallback` method
for user authentication. This class allows you to group the information passed in rather than passing headers, body, and query
parameters individually.

AuthProviderPlugin Interface
This interface is deprecated. For new development, use the abstract class `Auth.AuthProviderPluginClass` to create a
custom OAuth-based authentication provider plug-in for single sign-on in to Salesforce.

AuthProviderPluginClass Class
Contains methods to create a custom OAuth-based authentication provider plug-in for single sign-on in to Salesforce. Use this class
to create a custom authentication provider plug-in if you can’t use one of the authentication providers that Salesforce provides.

AuthProviderTokenResponse Class
Stores the response from the `AuthProviderPlugin.handleCallback` method.

AuthToken Class
Contains methods for getting and revoking access and refresh tokens that are issued when a user logs in via a single sign-on (SSO)
flow that uses an authentication provider, such as Facebook.

CommunitiesUtil Class
Contains methods for getting information about an Experience Cloud user.

ConfigurableSelfRegHandler Interface
Gives you more control over how customers or partners self-register for your Experience Cloud site by creating a class that implements
`Auth.ConfigurableSelfRegHandler` . You choose the user information to collect, and how users identify themselves—with
their email address, phone number, or another identifier. When verified, you create a customer or partner user and log in the user
to your Experience Cloud site.

ConfirmUserRegistrationHandler Interface
Manages single sign-on (SSO) user mappings between Salesforce and a third-party identity provider. Use this interface to confirm
user mappings before updating them.

ConnectedAppPlugin Class
Contains methods for extending the behavior of a connected app, for example, customizing how a connected app is invoked
depending on the protocol used. This class gives you more control over the interaction between Salesforce and your connected
app.


Apex Reference Guide Auth Namespace

CustomOneTimePasswordDeliveryHandler Interface
To use a custom SMS provider to send one-time passwords (OTPs) for Experience Cloud identity verification, create a class that
implements the `Auth.CustomOneTimePasswordDeliveryHandler` interface.

CustomOneTimePasswordDeliveryResult Enum
Indicates the status of an attempt to send a one-time password (OTP) to an external user via a custom messaging provider.

ExternalClientAppOauthHandler Class
Contains methods for extending the behavior of an external client app. For example, customize how an external client app is invoked
depending on the protocol used. This class gives you more control over the interaction between Salesforce and your external client
app.

GeneratedUserData Class
Stores the output of the Generate User Data invocable action, which you can access in Flow Builder.

HeadlessSelfRegistrationHandler Interface
Creates customer and partner users during the Headless Registration Flow.

HeadlessUserDiscoveryHandler Interface
Use this interface to create a headless user discovery handler that you implement during headless login, passwordless login, and
forgot password flows.

HeadlessUserDiscoveryResponse Class
Contains methods to describe the result of headless user discovery using a handler that implements the
`Auth.HeadlessUserDiscoveryHandler` interface during headless login, passwordless login, and forgot password flows.

HttpCalloutMockUtil Class
Contains a method to send fake HTTP callouts for classes in the `Auth` namespace.

IntegratingAppType Enum
Specifies whether you’re integrating your app as a connected app or as an external client app in methods used in your customized
Apex token exchange handler, which extends the `Auth.Oauth2TokenExchangeHandler` class.

InvocationContext Enum
The context in which the connected app is invoked, such as the protocol flow used and the token type issued, if any. Developers
can use the context information to write code that is unique to the type of invocation.

JsonValueOutput Class
Stores the output of the Get User Data from JSON String invocable action, which you can access in Flow Builder..

JWS Class
Contains methods that apply a digital signature to a JSON Web Token (JWT), using a JSON Web Signature (JWS) data structure. This
class creates the signed JWT bearer token, which can be used to request an OAuth access token in the OAuth 2.0 JWT bearer token
flow.

JWT Class
Generates the JSON Claims Set in a JSON Web Token (JWT). The resulting Base64-encoded payload can be passed as an argument
to create an instance of the `Auth.JWS` class.

JWTBearerTokenExchange Class
Contains methods that POST the signed JWT bearer token to a token endpoint to request an access token, in the OAuth 2.0 JWT
bearer token flow.

JWTUtil Class
Contains methods for validating a JSON Web Token (JWT) from an external identity provider as part of the OAuth 2.0 token exchange
flow. Use these methods as part of the `validateIncomingToken` method in the
`Auth.Oauth2TokenExchangeHandler` class.


Apex Reference Guide Auth Namespace

LightningLoginEligibility Enum
Contains a Lightning Login eligibility value used by the `Auth.SessionManagement.getLightningLoginEligibility`
method.

LoginDiscoveryHandler Interface
Salesforce gives you the ability to log in users based on other verification methods than username and password. For example, it
can prompt users to log in with their email, phone number, or another identifier like a Federation ID or device identifier. Login
Discovery is available to these licenses: Customer Community, Customer Community Plus, External Identity, Partner Community,
and Partner Community Plus.

LoginDiscoveryMethod Enum
Contains methods used to verify the user’s identity when the My Domain login process uses Login Discovery.

MyDomainLoginDiscoveryHandler Interface
The handler used to implement the My Domain Login Discovery page, which is an interview-based (two-step) login process. First
the user is prompted for a unique identifier such as an email address or phone number. Then the handler determines (discovers)
how to authenticate the user. Either the user enters a password or is directed to an identity provider’s login page.

Oauth2TokenExchangeHandler Class
Use this class to create a token exchange handler that validates tokens from an external identity provider and maps the token’s
subject to a Salesforce user during the OAuth 2.0 token exchange flow. The handler can also be used to create users by setting up
a new User object and returning it to Salesforce for automatic insertion.

OAuth2TokenExchangeType Enum
Used during the OAuth 2.0 token exchange flow to specify the type of token that’s being exchanged for a Salesforce token.

OAuthRefreshResult Class
Stores the result of an `AuthProviderPluginClass` refresh method. OAuth authentication flow provides a refresh token that
can be used to get a new access token. Access tokens have a limited lifetime as specified by the session timeout value. When an
access token expires, use a refresh token to get a new access token.

OauthToken Class
Contains a method to revoke OAuth access tokens and refresh tokens. This method supports opaque tokens and JSON Web Token
(JWT)-based access tokens, including guest and named user JWT-based access tokens.

OauthTokenType Enum
Specifies the type of Salesforce-issued OAuth 2.0 token being revoked in the `OauthToken.revokeToken` method.

RegistrationHandler Interface
Salesforce provides the ability to use an authentication provider, such as Facebook [©] or Janrain [©], for single sign-on into Salesforce.

SamlJitHandler Interface
Use this interface to control and customize Just-in-Time user provisioning logic during SAML single sign-on.

SessionManagement Class
Contains methods for verifying users’ identity, creating custom login flows, customizing security levels, and defining trusted IP ranges
for a current session.

SessionLevel Enum
An `Auth.SessionLevel` enum value is used by the `SessionManagement.setSessionLevel` method.

TokenValidationResult Class
Contains methods that describe the result of the token validation performed by a token exchange handler using the
`validateIncomingToken` method in the `Auth.Oauth2TokenExchangeHandler` class during the OAuth 2.0 token
exchange flow.


### Apex Reference Guide AuthConfiguration Class

UserData Class
Stores user information for authentication provider registration handlers, including handlers that implement the
`Auth.RegistrationHandler` interface and handlers built using Flow Builder.

VerificationAction Enum
Indicates the method that you use to send a one-time password (OTP) to a user during the headless passwordless login flow.

VerificationMethod Enum
Contains the different ways users can identify themselves when logging in. You can use it to implement mobile-centric passwordless
login pages and to self-register (and deregister) verification methods.

VerificationPolicy Enum
The `Auth.VerificationPolicy` enum contains an identity verification policy value used by the
`SessionManagement.generateVerificationUrl` method.

VerificationResult Class
Contains the result of a verification challenge that you invoke when you create your own Verify page. The challenge can be initiated
by either the `System.UserManagement.verifyPasswordlessLogin` or
`System.UserManagement.verifySelfRegistration` method.

Auth Exceptions
### The Auth namespace contains some exception classes. AuthConfiguration Class

Contains methods for configuring settings for users to log in to a Salesforce org using their authentication provider credentials instead
of their Salesforce credentials. The authentication provider can be any authentication provider that supports the OpenID Connect protocol,
such as Google, Facebook, or Twitter. Users log in to either an Experience Cloud site ( `https://` _`MyDomainName`_ `.my.site.com` )
or your My Domain login URL ( `https://` _`MyDomainName`_ `.my.salesforce.com` ).

Namespace

### Auth

Example

This example shows how to call some methods on the `Auth.AuthConfiguration` class. Before you can run this sample, you
must provide valid values for the URLs and developer name.

```
   String communityUrl = ' MyDomainName .my.site.com';

   String startUrl = '<Add URL>';

   Auth.AuthConfiguration authConfig = new Auth.AuthConfiguration(communityUrl,startUrl);

   List<AuthProvider> authPrvs = authConfig.getAuthProviders();

   String bColor = authConfig.getBackgroundColor();

   String fText = authConfig.getFooterText();

   String sso = Auth.AuthConfiguration.getAuthProviderSsoUrl(communityUrl, startUrl,

   'developerName');

#### AuthConfiguration Constructors

### The following are constructors for AuthConfiguration .

```


Apex Reference Guide AuthConfiguration Class

Note: The `AuthConfiguration (networkId, startUrl)` constructor is deprecated in API version 56.0 and later.

##### AuthConfiguration(communityOrCustomUrl, startUrl) Creates an instance of the AuthConfiguration class using the specified URL for an Experience Cloud site or a My Domain subdomain

and the start URL for authenticated users.

Signature

```
   public AuthConfiguration(String communityOrCustomUrl, String startUrl)

```

Parameters

```
   communityOrCustomUrl
```

Type: String

The URL for the domain, which can be a Salesforce subdomain created with My Domain ( `my.salesforce.com` ) or a subdomain
of an Experience Cloud site ( `force.com` ).

```
   startUrl
```

Type: String

The page users see after successfully logging in to the Experience Cloud site or My Domain subdomain.

#### AuthConfiguration Methods

##### The following are methods for AuthConfiguration . Use these methods to manage and customize authentication for a Salesforce

community.

IN THIS SECTION:

getAllowInternalUserLoginEnabled()
Indicates whether the Experience Cloud site allows internal users to log in using the Experience Cloud site login page. To enable,
admins configure the setting **Allow internal users to log in directly to the experience** on the Login & Registration page in
Experience Workspaces. It’s disabled by default.

getAuthConfig()
Returns the AuthConfig sObject, which represents the authentication options for an Experience Cloud site or Salesforce My Domain
subdomain.

getAuthConfigProviders()
Returns the list of authentication providers configured for an Experience Cloud site or Salesforce My Domain subdomain.

getAuthProviders()
Returns the list of authentication providers available for an Experience Cloud site or Salesforce My Domain subdomain.

getAuthProviderSsoDomainUrl(communityUrl, startUrl, developerName)
Returns the single sign-on URL for an Experience Cloud site subdomain.

getAuthProviderSsoUrl(communityUrl, startUrl, developerName)
Returns the single sign-on URL for an Experience Cloud site or Salesforce My Domain subdomain.

getBackgroundColor()
Returns the color for the background of the login page for a community.


Apex Reference Guide AuthConfiguration Class

getCertificateLoginEnabled(domainUrl)
Returns true if certificate-based authentication is enabled for the My Domain URL.

getCertificateLoginUrl(domainUrl, startUrl)
Returns the certificate-based authentication endpoint for the My Domain URL if the org has certificate-based authentication enabled.

getDefaultProfileForRegistration()
Returns the profile ID assigned to new community users.

getFooterText()
Returns the text at the bottom of the login page for a community.

getForgotPasswordUrl()
Returns the URL for the standard or custom Forgot Password page that is specified for an Experience Cloud site or portal by the
administrator.

getHeadlessForgotPasswordEnabled()
Returns `true` if the Headless Forgot Password Flow is enabled.

getHeadlessFrgtPswEnabled()
This method will be deprecated in a future release. Use the `getHeadlessForgotPasswordEnabled()` method in this
class instead.

getHeadlessPasswordlessLoginEnabled()
Determines if headless passwordless login is enabled.

getHeadlessRegistrationEnabled()
Determines if the Headless Registration Flow is enabled.

getLogoUrl()
Returns the location of the icon image at the bottom of the login page for a community.

getRightFrameUrl()
Returns the URL for the right-frame content to display on the right side of the Experience Cloud site login page. The admin supplies
the URL.

getSamlProviders()
Returns the list of SAML-based authentication providers available for an Experience Cloud site or Salesforce My Domain subdomain.

getSamlSsoUrl(communityUrl, startURL, samlId)
Returns the single sign-on URL for an Experience Cloud site or Salesforce My Domain subdomain.

getSelfRegistrationEnabled()
Indicates whether the current community allows new users to create their own account by filling out a registration form.

getSelfRegistrationUrl()
Returns the location of the self-registration page for new users to sign up for an account with a community.

getStartUrl()
Returns the start page of an Experience Cloud site or Salesforce My Domain subdomain. This URL is the first page that users see when
they log in.

getUsernamePasswordEnabled()
Indicates whether the current community is set to display a login form asking for a username and password. You can configure the
community not to request a username and password if it is for unauthenticated users or users logging in with a third-party
authentication provider.


Apex Reference Guide AuthConfiguration Class

isCommunityUsingSiteAsContainer()
Returns `true` if the Experience Cloud site uses Site.com pages; otherwise, returns `false` .

##### getAllowInternalUserLoginEnabled()

Indicates whether the Experience Cloud site allows internal users to log in using the Experience Cloud site login page. To enable, admins
configure the setting **Allow internal users to log in directly to the experience** on the Login & Registration page in Experience
Workspaces. It’s disabled by default.

Signature

```
   public Boolean getAllowInternalUserLoginEnabled()

```

Return Value

Type: Boolean

Usage

If true, internal users log in to an Experience Cloud site from the site’s login page with their internal credentials. If they navigate to their
internal org from the Experience Cloud site, they don't have to log in again.

##### getAuthConfig()

Returns the AuthConfig sObject, which represents the authentication options for an Experience Cloud site or Salesforce My Domain
subdomain.

Signature

```
   public AuthConfig getAuthConfig()

```

Return Value

Type: AuthConfig

The AuthConfig sObject for the Experience Cloud site or Salesforce My Domain subdomain.

##### getAuthConfigProviders()

Returns the list of authentication providers configured for an Experience Cloud site or Salesforce My Domain subdomain.

Signature

```
   public List<AuthConfigProviders> getAuthConfigProviders()

```

Return Value

Type: List<AuthConfigProviders>

A list of authentication providers (AuthConfigProviders sObjects), which are children of the AuthProvider sObject.


Apex Reference Guide AuthConfiguration Class

##### getAuthProviders()

Returns the list of authentication providers available for an Experience Cloud site or Salesforce My Domain subdomain.

Signature

```
   public List<AuthProvider> getAuthProviders()

```

Return Value

Type: List<AuthProvider>

A list of authentication providers (AuthProvider sObjects) for the Experience Cloud site or My Domain subdomain.

##### getAuthProviderSsoDomainUrl(communityUrl, startUrl, developerName)

Returns the single sign-on URL for an Experience Cloud site subdomain.

##### Note: For better performance, we recommend using this method instead of getAuthProviderSsoUrl . If the authentication

provider has `User Subdomain for Callback` enabled, changing the single sign-on URL also changes the callback URL
to use the Experience Cloud site subdomain. Before switching to this method, update the callback URL in your third-party applications
to avoid getting an invalid callback URL error during single sign-on.

Signature

```
   public static String getAuthProviderSsoDomainUrl(String communityUrl, String startUrl,

   String developerName)

```

Parameters

```
   communityUrl
```

Type: String

The URL for the Experience Cloud site subdomain. If null or specified as an empty string, you get the single sign-on URL for the org’s
My Domain.

```
   startUrl
```

Type: String

The page that users see after logging in to the Experience Cloud site subdomain.

```
   developerName
```

Type: String

The unique name of the authentication provider.

Return Value

Type: String

The Single Sign-On Initialization URL for the Experience Cloud site subdomain.

##### getAuthProviderSsoUrl(communityUrl, startUrl, developerName)

Returns the single sign-on URL for an Experience Cloud site or Salesforce My Domain subdomain.


Apex Reference Guide AuthConfiguration Class

Signature

```
   public static String getAuthProviderSsoUrl(String communityUrl, String startUrl, String

   developerName)

```

Parameters

```
   communityUrl
```

Type: String

The URL for the Experience Cloud site or My Domain subdomain. If not null and not specified as an empty string, you get the URL
for the Experience Cloud site. If null or specified as an empty string, you get the URL for a custom domain.

```
   startUrl
```

Type: String

The page that users see after logging in to the Experience Cloud site or My Domain subdomain.

```
   developerName
```

Type: String

The unique name of the authentication provider.

Return Value

Type: String

The Single Sign-On Initialization URL for the Experience Cloud site or Salesforce My Domain subdomain.

##### getBackgroundColor()

Returns the color for the background of the login page for a community.

Signature

```
   public String getBackgroundColor()

```

Return Value

Type: String

##### getCertificateLoginEnabled(domainUrl)

Returns true if certificate-based authentication is enabled for the My Domain URL.

Signature

```
   public Boolean getCertificateLoginEnabled(String domainUrl)

```

Parameters

```
   domainUrl
```

Type: String

The My Domain URL that is being checked for certificate-based authentication.


Apex Reference Guide AuthConfiguration Class

Return Value

Type: Boolean

##### getCertificateLoginUrl(domainUrl, startUrl)

Returns the certificate-based authentication endpoint for the My Domain URL if the org has certificate-based authentication enabled.

Signature

```
   public static String getCertificateLoginUrl(String domainUrl, String startUrl)

```

Parameters

```
   domainUrl
```

Type: String

The My Domain URL being checked for its certificate-based authentication endpoint .

```
   startUrl
```

Type: String

The page that the user is directed to after logging in to the My Domain with certificate-based authentication.

Return Value

Type: String

The certificate-based authentication endpoint for the My Domain URL:

```
   mydomainURL :8443/services/certauth?startURL= startURLParam

##### getDefaultProfileForRegistration()

```

Returns the profile ID assigned to new community users.

Signature

```
   public String getDefaultProfileForRegistration()

```

Return Value

Type: String

The profile ID.

##### getFooterText()

Returns the text at the bottom of the login page for a community.

Signature

```
   public String getFooterText()

```


Apex Reference Guide AuthConfiguration Class

Return Value

Type: String

The text string displayed at the bottom of the login page, for example “Log in with an existing account.”

##### getForgotPasswordUrl()

Returns the URL for the standard or custom Forgot Password page that is specified for an Experience Cloud site or portal by the
administrator.

Signature

```
   public String getForgotPasswordUrl()

```

Return Value

Type: String

URL for the standard or custom Forgot Password page.

##### **`getHeadlessForgotPasswordEnabled()`**

Returns `true` if the Headless Forgot Password Flow is enabled.

Signature

```
   public Boolean getHeadlessForgotPasswordEnabled()

```

Return Value

Type: Boolean

##### **`getHeadlessFrgtPswEnabled()`** This method will be deprecated in a future release. Use the getHeadlessForgotPasswordEnabled() method in this class

instead.

Signature

```
   public Boolean getHeadlessFrgtPswEnabled()

```

Return Value

Type: Boolean

##### **`getHeadlessPasswordlessLoginEnabled()`**

Determines if headless passwordless login is enabled.

Signature

```
   public Boolean getHeadlessPasswordlessLoginEnabled()

```


Apex Reference Guide AuthConfiguration Class

Return Value

Type: Boolean

Returns `true` if headless passwordless login is enabled.

##### **`getHeadlessRegistrationEnabled()`**

Determines if the Headless Registration Flow is enabled.

Signature

```
   public Boolean getHeadlessRegistrationEnabled()

```

Return Value

Type: Boolean

Returns `true` if headless registration is enabled.

##### getLogoUrl()

Returns the location of the icon image at the bottom of the login page for a community.

Signature

```
   public String getLogoUrl()

```

Return Value

Type: String

The path to the icon image.

##### getRightFrameUrl()

Returns the URL for the right-frame content to display on the right side of the Experience Cloud site login page. The admin supplies the
URL.

Signature

```
   public String getLoginRightFrameUrl()

```

Return Value

Type: String

URL for the right-frame content of the Experience Cloud site login page. Salesforce creates an inline (iframe) on the right side of the login
page to display the contents specified by the URL.

##### getSamlProviders()

Returns the list of SAML-based authentication providers available for an Experience Cloud site or Salesforce My Domain subdomain.


Apex Reference Guide AuthConfiguration Class

Signature

```
   public List<SamlSsoConfig> getSamlProviders()

```

Return Value

Type: List<SamlSsoConfig>

A list of SAML-based authentication providers, which are SamlSsoConfig sObjects.

##### getSamlSsoUrl(communityUrl, startURL, samlId)

Returns the single sign-on URL for an Experience Cloud site or Salesforce My Domain subdomain.

Signature

```
   public static String getSamlSsoUrl(String communityUrl, String startURL, String samlId)

```

Parameters

```
   communityUrl
```

Type: String

The URL for the Experience Cloud site or My Domain subdomain. If not `null` and not specified as an empty string, you get the URL
for the Experience Cloud site. If `null` or specified as an empty string, you get the URL for a My Domain subdomain.

```
   startUrl
```

Type: String

The page users see after successfully logging in to the Experience Cloud site or My Domain subdomain

```
   samlId
```

Type: String

The unique identifier of the SamlSsoConfig standard object for the Experience Cloud site or My Domain subdomain

Return Value

Type: String

The Single Sign-On Initialization URL for the Experience Cloud site or Salesforce My Domain subdomain.

##### getSelfRegistrationEnabled()

Indicates whether the current community allows new users to create their own account by filling out a registration form.

Signature

```
   public Boolean getSelfRegistrationEnabled()

```

Return Value

Type: Boolean


Apex Reference Guide AuthConfiguration Class

##### getSelfRegistrationUrl()

Returns the location of the self-registration page for new users to sign up for an account with a community.

Signature

```
   public String getSelfRegistrationUrl()

```

Return Value

Type: String

The location of the self-registration page.

##### getStartUrl()

Returns the start page of an Experience Cloud site or Salesforce My Domain subdomain. This URL is the first page that users see when
they log in.

Signature

```
   public String getStartUrl()

```

Return Value

Type: String

The location of the start page for the Experience Cloud site or My Domain subdomain.

##### getUsernamePasswordEnabled()

Indicates whether the current community is set to display a login form asking for a username and password. You can configure the
community not to request a username and password if it is for unauthenticated users or users logging in with a third-party authentication
provider.

Signature

```
   public Boolean getUsernamePasswordEnabled()

```

Return Value

Type: Boolean

##### isCommunityUsingSiteAsContainer()

Returns `true` if the Experience Cloud site uses Site.com pages; otherwise, returns `false` .

Signature

```
   public Boolean isCommunityUsingSiteAsContainer()

```


### Apex Reference Guide AuthProviderCallbackState Class

Return Value

Type: Boolean

### AuthProviderCallbackState Class

Provides request HTTP headers, body, and query parameters to the `AuthProviderPlugin.handleCallback` method for
user authentication. This class allows you to group the information passed in rather than passing headers, body, and query parameters
individually.

Namespace

### Auth

IN THIS SECTION:

#### AuthProviderCallbackState Constructors

AuthProviderCallbackState Properties

SEE ALSO:

handleCallback(authProviderConfiguration, callbackState)

#### AuthProviderCallbackState Constructors

### The following are constructors for AuthProviderCallbackState .

IN THIS SECTION:

##### AuthProviderCallbackState(headers, body, queryParameters)
### Creates an instance of the AuthProviderCallbackState class using the specified HTTP headers, body, and query parameters

of the authentication request.

##### AuthProviderCallbackState(headers, body, queryParameters)

### Creates an instance of the AuthProviderCallbackState class using the specified HTTP headers, body, and query parameters

of the authentication request.

Signature

```
   public AuthProviderCallbackState(Map<String,String> headers, String body,

   Map<String,String> queryParameters)

```

Parameters

```
   headers
```

Type: Map<String,String>

The HTTP headers of the authentication request.


Apex Reference Guide AuthProviderCallbackState Class

##### _`body`_

Type: String

The HTTP body of the authentication request.

##### _`queryParameters`_

Type: Map<String,String>

The HTTP query parameters of the authentication request.

#### AuthProviderCallbackState Properties The following are properties for AuthProviderCallbackState .

IN THIS SECTION:

##### body

The HTTP body of the authentication request.

##### headers

The HTTP headers of the authentication request.

##### queryParameters

The HTTP query parameters of the authentication request.

##### body

The HTTP body of the authentication request.

Signature

```
   public String body {get; set;}

```

Property Value

Type: String

##### headers

The HTTP headers of the authentication request.

Signature

```
   public Map<String,String> headers {get; set;}

```

Property Value

Type: Map<String,String>

##### queryParameters

The HTTP query parameters of the authentication request.


### Apex Reference Guide AuthProviderPlugin Interface

Signature

```
   public Map<String,String> queryParameters {get; set;}

```

Property Value

Type: Map<String,String>

### AuthProviderPlugin Interface

This interface is deprecated. For new development, use the abstract class `Auth.AuthProviderPluginClass` to create a custom
OAuth-based authentication provider plug-in for single sign-on in to Salesforce.

Namespace

### Auth

Usage

Deprecated. Existing implementations that use `Auth.AuthProviderPlugin` still work. For new development, use
`Auth.AuthProviderPluginClass` .

IN THIS SECTION:

#### AuthProviderPlugin Methods

AuthProviderPlugin Example Implementation

#### AuthProviderPlugin Methods

### The following methods are for AuthProviderPlugin, which, as of API version 39.0, is deprecated. Use themethods in

`AuthProviderPluginClass` instead.

IN THIS SECTION:

getCustomMetadataType()
Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

getUserInfo(authProviderConfiguration, response)
Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

handleCallback(authProviderConfiguration, callbackState)
Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

initiate(authProviderConfiguration, stateToPropagate)
Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

SEE ALSO:

[Salesforce Help: Create a Custom External Authentication Provider](https://help.salesforce.com/HTViewHelpDoc?id=sso_provider_plugin_custom.htm&language=en_US)


Apex Reference Guide AuthProviderPlugin Interface

##### getCustomMetadataType()

Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

Signature

```
   public String getCustomMetadataType()

```

Return Value

Type: String

The custom metadata type API name for the authentication provider.

Usage

Returns the custom metadata type API name for a custom OAuth-based authentication provider for single sign-on to Salesforce. The
`getCustomMetatadaType()` method returns only custom metadata type names. It does not return custom metadata record
names.

##### getUserInfo(authProviderConfiguration, response)

Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

Signature

```
   public Auth.UserData getUserInfo(Map<String,String> authProviderConfiguration,

   Auth.AuthProviderTokenResponse response)

```

Parameters

```
   authProviderConfiguration
```

Type: Map<String,String>

The configuration for the custom authentication provider. When you create a custom metadata type in Salesforce, the configuration
populates with the custom metadata type default values. Or you can set the configuration with values you enter when you create
the custom provider in Auth. Providers in Setup.

```
   response
```

Type: Auth.AuthProviderTokenResponse

The OAuth access token, OAuth secret or refresh token, and state provided by the authentication provider to authenticate the current
user.

Return Value

Type: Auth.UserData

Creates a new instance of the `Auth.UserData` class.

Usage

Returns information from the custom authentication provider about the current user. The registration handler and other authentication
provider flows use this information.


Apex Reference Guide AuthProviderPlugin Interface

##### handleCallback(authProviderConfiguration, callbackState)

Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

Signature

```
   public Auth.AuthProviderTokenResponse handleCallback(Map<String,String>

   authProviderConfiguration, Auth.AuthProviderCallbackState callbackState)

```

Parameters

```
   authProviderConfiguration
```

Type: Map<StringString>

The configuration for the custom authentication provider. When you create a custom metadata type in Salesforce, the configuration
populates with the custom metadata type default values. Or you can set the configuration with values you enter when you create
the custom provider in Auth. Providers in Setup.

```
   callbackState
```

Type: Auth.AuthProviderCallbackState

The class that contains the HTTP headers, body, and queryParams of the authentication request.

Return Value

Type: Auth.AuthProviderTokenResponse

Creates an instance of the `AuthProviderTokenResponse` class.

Usage

Uses the authentication provider’s supported authentication protocol to return an OAuth access token, OAuth secret or refresh token,
and the state passed in when the request for the current user was initiated.

##### initiate(authProviderConfiguration, stateToPropagate)

Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

Signature

```
   public System.PageReference initiate(Map<String,String> authProviderConfiguration,

   String stateToPropagate)

```

Parameters

```
   authProviderConfiguration
```

Type: Map<StringString>

The configuration for the custom authentication provider. When you create a custom metadata type in Salesforce, the configuration
populates with the custom metadata type default values. Or you can set the configuration with values you enter when you create
the custom provider in Auth. Providers in Setup.

```
   stateToPropagate
```

Type: String


### Apex Reference Guide AuthProviderPluginClass Class

The state passed in to initiate the authentication request for the user.

Return Value

Type: System.PageReference

The URL of the page where the user is redirected for authentication.

Usage

Returns the URL where the user is redirected for authentication.

#### AuthProviderPlugin Example Implementation

We’ve removed the example implementation for the `Auth.AuthProviderPlugin` interface because we’ve deprecated the
interface and replaced it with an abstract class. See AuthProviderPluginClass Class.

### AuthProviderPluginClass Class

Contains methods to create a custom OAuth-based authentication provider plug-in for single sign-on in to Salesforce. Use this class to
create a custom authentication provider plug-in if you can’t use one of the authentication providers that Salesforce provides.

Namespace

#### Auth

Usage

To create a custom authentication provider for single sign-on, create a class that extends `Auth.AuthProviderPluginClass` .
This class allows you to store the custom configuration for your authentication provider and handle authentication protocols when users
log in to Salesforce with their login credentials for an external service provider. In Salesforce, the class that implements this interface
appears in the `Provider Type` drop-down list in Auth. Providers in Setup. Make sure that the user you specify to run the class has
“Customize Application” and “Manage Auth. Providers” permissions.

### As of API version 39.0, use the abstract class AuthProviderPluginClass to create a custom external authentication provider.
#### This class replaces the AuthProviderPlugin interface. If you’ve already implemented a custom authentication provider plug-in
### using the interface, it still works. However, use AuthProviderPluginClass to extend your plug-in. If you haven’t created an

[interface, create a custom authentication provider plug-in by extending this abstract class. For more information, see Create a Custom](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/authproviderplugin.htm)
[Authentication Provider Plug-in.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/authproviderplugin.htm)

IN THIS SECTION:

#### AuthProviderPluginClass Methods

AuthProviderPluginClass Code Example

#### AuthProviderPluginClass Methods

### The AuthProviderPluginClass methods don’t support DML options.

[This class doesn't include a method for single logout. You can easily configure single logout in Setup. For steps, see Configure OpenID](https://help.salesforce.com/s/articleView?id=xcloud.security_auth_slo_oidc_rp_configuring.htm&language=en_US)
[Connect Single Logout with Salesforce as the Relying Party in](https://help.salesforce.com/s/articleView?id=xcloud.security_auth_slo_oidc_rp_configuring.htm&language=en_US) _Salesforce Help_ . Alternatively, create custom methods for single logout.


Apex Reference Guide AuthProviderPluginClass Class

IN THIS SECTION:

##### getCustomMetadataType()

Returns the custom metadata type API name for a custom OAuth-based authentication provider for single sign-on to Salesforce.

##### getUserInfo(authProviderConfiguration, response)

Returns information from the custom authentication provider about the current user. This information is used by the registration
handler and in other authentication provider flows.

handleCallback(authProviderConfiguration, callbackState)
Uses the authentication provider’s supported authentication protocol to return an OAuth access token, OAuth secret or refresh token,
and the state passed in when the request for the current user was initiated.

initiate(authProviderConfiguration, stateToPropagate)
Returns the URL where the user is redirected for authentication.

refresh(authProviderConfiguration, refreshToken)
Returns a new access token, which is used to update an expired access token.

##### getCustomMetadataType()

Returns the custom metadata type API name for a custom OAuth-based authentication provider for single sign-on to Salesforce.

Signature

```
   public String getCustomMetadataType()

```

Return Value

Type: String

The custom metadata type API name for the authentication provider.

Usage

The `getCustomMetatadaType()` method returns only custom metadata type names. It does not return custom metadata record
names. As of API version 39.0, use this method when extending `Auth.AuthProviderPluginClass` to create a custom external
authentication provider.

##### getUserInfo(authProviderConfiguration, response)

Returns information from the custom authentication provider about the current user. This information is used by the registration handler
and in other authentication provider flows.

Signature

```
   public Auth.UserData getUserInfo(Map<String,String> authProviderConfiguration,

   Auth.AuthProviderTokenResponse response)

```

Parameters

```
   authProviderConfiguration
```

Type: Map<String,String>


Apex Reference Guide AuthProviderPluginClass Class

The configuration for the custom authentication provider. When you create a custom metadata type in Salesforce, the configuration
populates it with the custom metadata type default values. Or you can set the configuration with values that you enter when you
create the custom provider in Auth. Providers in Setup.

```
   response
```

Type: Auth.AuthProviderTokenResponse

The OAuth access token, OAuth secret or refresh token, and state provided by the authentication provider to authenticate the current
user.

Return Value

Type: Auth.UserData

Creates a new instance of the `Auth.UserData` class.

Usage

As of API version 39.0, use this method when extending `Auth.AuthProviderPluginClass` to create a custom authentication
provider.

##### handleCallback(authProviderConfiguration, callbackState)

Uses the authentication provider’s supported authentication protocol to return an OAuth access token, OAuth secret or refresh token,
and the state passed in when the request for the current user was initiated.

Signature

```
   public Auth.AuthProviderTokenResponse handleCallback(Map<String,String>

   authProviderConfiguration, Auth.AuthProviderCallbackState callbackState)

```

Parameters

```
   authProviderConfiguration
```

Type: Map<StringString>

The configuration for the custom authentication provider. When you create a custom metadata type in Salesforce, the configuration
populates with the custom metadata type default values. Or you can set the configuration with values you enter when you create
the custom provider in Auth. Providers in Setup.

```
   callbackState
```

Type: Auth.AuthProviderCallbackState

The class that contains the HTTP headers, body, and queryParams of the authentication request.

Return Value

Type: Auth.AuthProviderTokenResponse

Creates an instance of the `AuthProviderTokenResponse` class.

Usage

As of API version 39.0, use this method when extending `Auth.AuthProviderPluginClass` to create a custom authentication
provider.


Apex Reference Guide AuthProviderPluginClass Class

##### initiate(authProviderConfiguration, stateToPropagate)

Returns the URL where the user is redirected for authentication.

Signature

```
   public System.PageReference initiate(Map<String,String> authProviderConfiguration,

   String stateToPropagate)

```

Parameters

```
   authProviderConfiguration
```

Type: Map<StringString>

The configuration for the custom authentication provider. When you create a custom metadata type in Salesforce, the configuration
populates with the custom metadata type default values. Or you can set the configuration with values you enter when you create
the custom provider in Auth. Providers in Setup.

```
   stateToPropagate
```

Type: String

The state passed in to initiate the authentication request for the user.

Return Value

Type: System.PageReference

The URL of the page where the user is redirected for authentication.

Usage

As of API version 39.0, use this method when extending `Auth.AuthProviderPluginClass` to create a custom authentication
provider.

##### refresh(authProviderConfiguration, refreshToken)

Returns a new access token, which is used to update an expired access token.

Signature

```
   public Auth.OAuthRefreshResult refresh(Map<String,String> authProviderConfiguration,

   String refreshToken)

```

Parameters

```
   authProviderConfiguration
```

Type: Map<String,String>

The configuration for the custom authentication provider. When you create a custom metadata type in Salesforce, the configuration
populates with the custom metadata type default values. Or you can set the configuration with values you enter when you create
the custom provider in Auth. Providers in Setup.

```
   refreshToken
```

Type: String


Apex Reference Guide AuthProviderPluginClass Class

The refresh token for the user who is logged in.

Return Value

Type: Auth.OAuthRefreshResult

Returns the new access token, or an error message if an error occurs.

Usage

A successful request returns a `Auth.OAuthRefreshResult` with the access token and refresh token in the response. If you receive
an error, make sure that you set the error string to the error message. A `NULL` error string indicates no error.

The refresh method works only with named credentials; it doesn’t respect the standard OAuth refresh flow. The refresh method with
named credentials works only if the earlier request returns a 401.

#### AuthProviderPluginClass Code Example

The following example demonstrates how to implement a custom Auth. provider plug-in using the abstract class,
`Auth.AuthProviderPluginClass` .

```
         global class Concur extends Auth.AuthProviderPluginClass {

         // Use this URL for the endpoint that the

         // authentication provider calls back to for configuration.

         public String redirectUrl;

         private String key;

         private String secret;

         // Application redirection to the Concur website for

         // authentication and authorization.

         private String authUrl;

         // URI to get the new access token from concur using the GET verb.

         private String accessTokenUrl;

         // Api name for the custom metadata type created for this auth provider.

         private String customMetadataTypeApiName;

         // Api URL to access the user in Concur

         private String userAPIUrl;

         // Version of the user api URL to access data from Concur

         private String userAPIVersionUrl;

         global String getCustomMetadataType() {

            return customMetadataTypeApiName;

         }

         global PageReference initiate(Map<string,string>

           authProviderConfiguration, String stateToPropagate)

           {

             authUrl = authProviderConfiguration.get('Auth_Url__c');

```


Apex Reference Guide AuthProviderPluginClass Class

```
             key = authProviderConfiguration.get('Key__c');

             // Here the developer can build up a request of some sort.

             // Ultimately, they return a URL where we will redirect the user.

             String url = authUrl + '?client_id='+ key

   +'&scope=USER,EXPRPT,LIST&redirect_uri='+ redirectUrl + '&state=' + stateToPropagate;

             return new PageReference(url);

           }

           global Auth.AuthProviderTokenResponse handleCallback(Map<string,string>

           authProviderConfiguration, Auth.AuthProviderCallbackState state )

           {

             // Here, the developer will get the callback with actual protocol.

             // Their responsibility is to return a new object called

             // AuthProviderTokenResponse.

             // This will contain an optional accessToken and refreshToken

             key = authProviderConfiguration.get('Key__c');

             secret = authProviderConfiguration.get('Secret__c');

             accessTokenUrl = authProviderConfiguration.get('Access_Token_Url__c');

             Map<String,String> queryParams = state.queryParameters;

             String code = queryParams.get('code');

             String sfdcState = queryParams.get('state');

             HttpRequest req = new HttpRequest();

             String url = accessTokenUrl+'?code=' + code + '&client_id=' + key +

             '&client_secret=' + secret;

             req.setEndpoint(url);

             req.setHeader('Content-Type','application/xml');

             req.setMethod('GET');

             Http http = new Http();

             HTTPResponse res = http.send(req);

             String responseBody = res.getBody();

             String token = getTokenValueFromResponse(responseBody, 'Token', null);

             return new Auth.AuthProviderTokenResponse('Concur', token,

             'refreshToken', sfdcState);

           }

           global Auth.UserData getUserInfo(Map<string,string>

           authProviderConfiguration,

           Auth.AuthProviderTokenResponse response)

           {

             //Here the developer is responsible for constructing an

             //Auth.UserData object

             String token = response.oauthToken;

             HttpRequest req = new HttpRequest();

             userAPIUrl = authProviderConfiguration.get('API_User_Url__c');

             userAPIVersionUrl = authProviderConfiguration.get

             ('API_User_Version_Url__c');

             req.setHeader('Authorization', 'OAuth ' + token);

             req.setEndpoint(userAPIUrl);

             req.setHeader('Content-Type','application/xml');

```


Apex Reference Guide AuthProviderPluginClass Class

```
             req.setMethod('GET');

             Http http = new Http();

             HTTPResponse res = http.send(req);

             String responseBody = res.getBody();

             String id = getTokenValueFromResponse(responseBody,

             'LoginId',userAPIVersionUrl);

             String fname = getTokenValueFromResponse(responseBody,

             'FirstName', userAPIVersionUrl);

             String lname = getTokenValueFromResponse(responseBody,

             'LastName', userAPIVersionUrl);

             String flname = fname + ' ' + lname;

             String uname = getTokenValueFromResponse(responseBody,

             'EmailAddress', userAPIVersionUrl);

             String locale = getTokenValueFromResponse(responseBody,

             'LocaleName', userAPIVersionUrl);

             Map<String,String> provMap = new Map<String,String>();

             provMap.put('what1', 'noidea1');

             provMap.put('what2', 'noidea2');

             return new Auth.UserData(id, fname, lname, flname,

             uname, 'what', locale, null, 'Concur', null, provMap);

           }

           private String getTokenValueFromResponse(String response,

           String token, String ns)

           {

             Dom.Document docx = new Dom.Document();

             docx.load(response);

             String ret = null;

             dom.XmlNode xroot = docx.getrootelement() ;

             if(xroot != null){ ret = xroot.getChildElement(token, ns).getText();

             }

           return ret;

           }

        }

```

Sample Test Classes

The following example contains test classes for the Concur class.

```
           @IsTest

           public class ConcurTestClass {

             private static final String OAUTH_TOKEN = 'testToken';

             private static final String STATE = 'mocktestState';

             private static final String REFRESH_TOKEN = 'refreshToken';

             private static final String LOGIN_ID = 'testLoginId';

             private static final String USERNAME = 'testUsername';

             private static final String FIRST_NAME = 'testFirstName';

             private static final String LAST_NAME = 'testLastName';

             private static final String EMAIL_ADDRESS = 'testEmailAddress';

```


Apex Reference Guide AuthProviderPluginClass Class

```
             private static final String LOCALE_NAME = 'testLocalName';

             private static final String FULL_NAME = FIRST_NAME + ' ' + LAST_NAME;

             private static final String PROVIDER = 'Concur';

             private static final String REDIRECT_URL =

             'http://localhost/services/authcallback/orgId/Concur';

             private static final String KEY = 'testKey';

             private static final String SECRET = 'testSecret';

             private static final String STATE_TO_PROPOGATE = 'testState';

             private static final String ACCESS_TOKEN_URL =

             'http://www.dummyhost.com/accessTokenUri';

             private static final String API_USER_VERSION_URL =

             'http://www.dummyhost.com/user/20/1';

             private static final String AUTH_URL =

             'http://www.dummy.com/authurl';

             private static final String API_USER_URL =

             'www.concursolutions.com/user/api';

           // In the real world scenario, the key and value would be read

           // from the (custom fields in) custom metadata type record.

           private static Map<String,String> setupAuthProviderConfig ()

           {

             Map<String,String> authProviderConfiguration = new Map<String,String>();

             authProviderConfiguration.put('Key__c', KEY);

             authProviderConfiguration.put('Auth_Url__c', AUTH_URL);

             authProviderConfiguration.put('Secret__c', SECRET);

             authProviderConfiguration.put('Access_Token_Url__c', ACCESS_TOKEN_URL);

             authProviderConfiguration.put('API_User_Url__c',API_USER_URL);

             authProviderConfiguration.put('API_User_Version_Url__c',

             API_USER_VERSION_URL);

             authProviderConfiguration.put('Redirect_Url__c',REDIRECT_URL);

             return authProviderConfiguration;

           }

           static testMethod void testInitiateMethod()

           {

             String stateToPropogate = 'mocktestState';

             Map<String,String> authProviderConfiguration = setupAuthProviderConfig();

             Concur concurCls = new Concur();

             concurCls.redirectUrl = authProviderConfiguration.get('Redirect_Url__c');

           PageReference expectedUrl = new

   PageReference(authProviderConfiguration.get('Auth_Url__c') + '?client_id='+

         authProviderConfiguration.get('Key__c') +'&scope=USER,EXPRPT,LIST&redirect_uri='+

           authProviderConfiguration.get('Redirect_Url__c') + '&state=' +

           STATE_TO_PROPOGATE);

             PageReference actualUrl = concurCls.initiate(authProviderConfiguration,

   STATE_TO_PROPOGATE);

             System.assertEquals(expectedUrl.getUrl(), actualUrl.getUrl());

           }

```


Apex Reference Guide AuthProviderPluginClass Class

```
           static testMethod void testHandleCallback()

           {

             Map<String,String> authProviderConfiguration =

             setupAuthProviderConfig();

             Concur concurCls = new Concur();

             concurCls.redirectUrl = authProviderConfiguration.get

             ('Redirect_Url_c');

             Test.setMock(HttpCalloutMock.class, new

             ConcurMockHttpResponseGenerator());

             Map<String,String> queryParams = new Map<String,String>();

             queryParams.put('code','code');

             queryParams.put('state',authProviderConfiguration.get('State_c'));

             Auth.AuthProviderCallbackState cbState =

             new Auth.AuthProviderCallbackState(null,null,queryParams);

             Auth.AuthProviderTokenResponse actualAuthProvResponse =

             concurCls.handleCallback(authProviderConfiguration, cbState);

             Auth.AuthProviderTokenResponse expectedAuthProvResponse =

             new Auth.AuthProviderTokenResponse(

             'Concur', OAUTH_TOKEN, REFRESH_TOKEN, null);

             System.assertEquals(expectedAuthProvResponse.provider,

             actualAuthProvResponse.provider);

             System.assertEquals(expectedAuthProvResponse.oauthToken,

             actualAuthProvResponse.oauthToken);

             System.assertEquals(expectedAuthProvResponse.oauthSecretOrRefreshToken,

             actualAuthProvResponse.oauthSecretOrRefreshToken);

             System.assertEquals(expectedAuthProvResponse.state,

             actualAuthProvResponse.state);

           }

           static testMethod void testGetUserInfo()

           {

             Map<String,String> authProviderConfiguration =

             setupAuthProviderConfig();

             Concur concurCls = new Concur();

             Test.setMock(HttpCalloutMock.class, new

             ConcurMockHttpResponseGenerator());

             Auth.AuthProviderTokenResponse response =

             new Auth.AuthProviderTokenResponse(

             PROVIDER, OAUTH_TOKEN,'sampleOauthSecret', STATE);

             Auth.UserData actualUserData = concurCls.getUserInfo(

             authProviderConfiguration, response) ;

             Map<String,String> provMap = new Map<String,String>();

             provMap.put('key1', 'value1');

             provMap.put('key2', 'value2');

             Auth.UserData expectedUserData = new Auth.UserData(LOGIN_ID,

             FIRST_NAME, LAST_NAME, FULL_NAME, EMAIL_ADDRESS,

```


Apex Reference Guide AuthProviderPluginClass Class

```
             null, LOCALE_NAME, null, PROVIDER, null, provMap);

             System.assertNotEquals(expectedUserData,null);

             System.assertEquals(expectedUserData.firstName,

             actualUserData.firstName);

             System.assertEquals(expectedUserData.lastName,

             actualUserData.lastName);

             System.assertEquals(expectedUserData.fullName,

             actualUserData.fullName);

             System.assertEquals(expectedUserData.email,

             actualUserData.email);

             System.assertEquals(expectedUserData.username,

             actualUserData.username);

             System.assertEquals(expectedUserData.locale,

             actualUserData.locale);

             System.assertEquals(expectedUserData.provider,

             actualUserData.provider);

             System.assertEquals(expectedUserData.siteLoginUrl,

             actualUserData.siteLoginUrl);

           }

           // Implement a mock http response generator for Concur.

           public class ConcurMockHttpResponseGenerator implements HttpCalloutMock

           {

             public HTTPResponse respond(HTTPRequest req)

             {

               String namespace = API_USER_VERSION_URL;

               String prefix = 'mockPrefix';

               Dom.Document doc = new Dom.Document();

               Dom.XmlNode xmlNode = doc.createRootElement(

               'mockRootNodeName', namespace, prefix);

               xmlNode.addChildElement('LoginId', namespace, prefix)

               .addTextNode(LOGIN_ID);

               xmlNode.addChildElement('FirstName', namespace, prefix)

               .addTextNode(FIRST_NAME);

               xmlNode.addChildElement('LastName', namespace, prefix)

               .addTextNode(LAST_NAME);

               xmlNode.addChildElement('EmailAddress', namespace, prefix)

               .addTextNode(EMAIL_ADDRESS);

               xmlNode.addChildElement('LocaleName', namespace, prefix)

               .addTextNode(LOCALE_NAME);

               xmlNode.addChildElement('Token', null, null)

               .addTextNode(OAUTH_TOKEN);

               System.debug(doc.toXmlString());

               // Create a fake response

               HttpResponse res = new HttpResponse();

               res.setHeader('Content-Type', 'application/xml');

               res.setBody(doc.toXmlString());

               res.setStatusCode(200);

               return res;

             }

```


### Apex Reference Guide AuthProviderTokenResponse Class

```
           }

        }

### AuthProviderTokenResponse Class

```

Stores the response from the `AuthProviderPlugin.handleCallback` method.

Namespace

### Auth

IN THIS SECTION:

#### AuthProviderTokenResponse Constructors

AuthProviderTokenResponse Properties

#### AuthProviderTokenResponse Constructors

### The following are constructors for AuthProviderTokenResponse .

IN THIS SECTION:

##### AuthProviderTokenResponse(provider, oauthToken, oauthSecretOrRefreshToken, state)
### Creates an instance of the AuthProviderTokenResponse class for a custom authentication provider plug-in using the

specified arguments.

AuthProviderTokenResponse(provider, oauthToken, oauthSecretOrRefreshToken, state, idToken)
Creates an instance of the AuthProviderTokenResponse class for a custom authentication provider plug-in using the specified
arguments. This constructor includes a parameter for the ID token.

##### AuthProviderTokenResponse(provider, oauthToken, oauthSecretOrRefreshToken, state)

### Creates an instance of the AuthProviderTokenResponse class for a custom authentication provider plug-in using the specified

arguments.

Signature

```
   public AuthProviderTokenResponse(String provider, String oauthToken, String

   oauthSecretOrRefreshToken, String state)

```

Parameters

```
   provider
```

Type: String

The custom authentication provider.

```
   oauthToken
```

Type: String

The OAuth access token.


Apex Reference Guide AuthProviderTokenResponse Class

```
   oauthSecretOrRefreshToken
```

Type: String

The OAuth secret or refresh token for the currently logged-in user.

```
   state
```

Type: String

The state passed in to initiate the authentication request for the user.

##### **`AuthProviderTokenResponse(provider, oauthToken, oauthSecretOrRefreshToken,`**

```
  state, idToken)

```

Creates an instance of the AuthProviderTokenResponse class for a custom authentication provider plug-in using the specified arguments.
This constructor includes a parameter for the ID token.

Signature

```
   public AuthProviderTokenResponse(String provider, String oauthToken, String

   oauthSecretOrRefreshToken, String state)

```

Parameters

```
   provider
```

Type: String

The custom authentication provider.

```
   oauthToken
```

Type: String

The OAuth access token.

```
   oauthSecretOrRefreshToken
```

Type: String

The OAuth secret or refresh token for the currently logged-in user.

```
   state
```

Type: String

The state passed in to initiate the authentication request for the user.

```
   idToken
```

Type: String

The ID token in encoded JWT format.

#### AuthProviderTokenResponse Properties

##### The following are properties for AuthProviderTokenResponse .

IN THIS SECTION:

oauthSecretOrRefreshToken
The OAuth secret or refresh token for the currently logged-in user.


Apex Reference Guide AuthProviderTokenResponse Class

##### oauthToken

The OAuth access token.

##### provider

The authentication provider.

##### state

The state passed in to initiate the authentication request for the user.

idToken
The ID token from the third party in encoded JWT format.

##### oauthSecretOrRefreshToken

The OAuth secret or refresh token for the currently logged-in user.

Signature

```
   public String oauthSecretOrRefreshToken {get; set;}

```

Property Value

Type: String

##### oauthToken

The OAuth access token.

Signature

```
   public String oauthToken {get; set;}

```

Property Value

Type: String

##### provider

The authentication provider.

Signature

```
   public String provider {get; set;}

```

Property Value

Type: String

##### state

The state passed in to initiate the authentication request for the user.


### Apex Reference Guide AuthToken Class

Signature

```
   public String state {get; set;}

```

Property Value

Type: String

##### **`idToken`**

The ID token from the third party in encoded JWT format.

Signature

```
   public String idToken {get; set;}

```

Property Value

Type: String

### AuthToken Class

Contains methods for getting and revoking access and refresh tokens that are issued when a user logs in via a single sign-on (SSO) flow
that uses an authentication provider, such as Facebook.

Namespace

### Auth

Usage

To authenticate users via an authentication provider, you must create a class that implements the `[Auth.RegistrationHandler](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_auth_plugin.htm)`
[interface. When a user logs in to Salesforce via a provider such as Facebook, they’re issued an access token and in some cases, a refresh](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_auth_plugin.htm)
token. To retrieve and revoke these tokens, use the methods in the `Auth.AuthToken` class.

#### AuthToken Methods

### The following are methods for AuthToken . All methods are static.

IN THIS SECTION:

getAccessToken(authProviderId, providerName)
Returns an access token for the current user using the specified 18-character identifier of an AuthProvider definition in your org and
the proper name of the provider, such as Salesforce or Facebook.

getAccessTokenMap(authProviderId, providerName)
Returns a map from the provider’s identifier to the access token for the currently logged-in Salesforce user. The identifier value
depends on the provider. For example, for Salesforce, it’s the user ID, while for Facebook, it’s the user number.


Apex Reference Guide AuthToken Class

refreshAccessToken(authProviderId, providerName, oldAccessToken)
Returns a map from the third-party provider’s identifier containing a refreshed access token for the currently logged-in Salesforce
user.

revokeAccess(authProviderId, providerName, userId, remoteIdentifier)
Revokes the access token for a specified SSO user from a provider such as Facebook. You can use this method only if the
`IsNotSsoUsable` field on the associated ThirdPartyAccountLink object is set to `false` .

##### getAccessToken(authProviderId, providerName)

Returns an access token for the current user using the specified 18-character identifier of an AuthProvider definition in your org and the
proper name of the provider, such as Salesforce or Facebook.

Signature

```
   public static String getAccessToken(String authProviderId, String providerName)

```

Parameters

```
   authProviderId
```

Type: String

```
   providerName
```

Type: String

The proper name of the provider. Here are valid values for each provider type.

**•** Apple— `Apple`

**•** Custom—For a custom authentication provider, use the value in the `FriendlyName` [field on the AuthProvider object, such](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_authprovider.htm)
as `MyProvider` .

**•** Facebook— `Facebook`

**•** GitHub— `GitHub`

**•** Google— `Google`

**•** Janrain—Use the proper name of the third party, such as `Yahoo!` .

**•** LinkedIn— `LinkedIn`

**•** Microsoft— `Microsoft`

**•** Microsoft Access Control Service— `Microsoft Access Control Service`

**•** MuleSoft— `MuleSoft`

**•** Open ID Connect— `Open ID Connect`

**•** Salesforce— `Salesforce`

**•** Slack— `Slack`

**•** Twitter—This method doesn’t support the Twitter authentication provider.

Note: The `providerName` value that you pass into this method can be different from the value that’s returned if you
query the `ProviderType` field on the AuthProvider object. For example, for Open ID Connect providers, `OpenIdConnect`
is the `ProviderType` value for the AuthProvider object, but the expected `providerName` is `Open ID Connect` .


Apex Reference Guide AuthToken Class

Return Value

Type: String

##### getAccessTokenMap(authProviderId, providerName)

Returns a map from the provider’s identifier to the access token for the currently logged-in Salesforce user. The identifier value depends
on the provider. For example, for Salesforce, it’s the user ID, while for Facebook, it’s the user number.

Signature

```
   public static Map<String, String> getAccessTokenMap(String authProviderId, String

   providerName)

```

Parameters

```
   authProviderId
```

Type: String

```
   providerName
```

Type: String

The proper name of the provider. Here are valid values for each provider type.

**•** Apple— `Apple`

**•** Custom—For a custom authentication provider, use the value in the `FriendlyName` [field on the AuthProvider object, such](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_authprovider.htm)
as `MyProvider` .

**•** Facebook— `Facebook`

**•** GitHub— `GitHub`

**•** Google— `Google`

**•** Janrain—Use the proper name of the third party, such as `Yahoo!` .

**•** LinkedIn— `LinkedIn`

**•** Microsoft— `Microsoft`

**•** Microsoft Access Control Service— `Microsoft Access Control Service`

**•** MuleSoft— `MuleSoft`

**•** Open ID Connect— `Open ID Connect`

**•** Salesforce— `Salesforce`

**•** Slack— `Slack`

**•** Twitter—This method doesn’t support the Twitter authentication provider.

Note: The `providerName` value that you pass into this method can be different from the value that’s returned if you
query the `ProviderType` field on the AuthProvider object. For example, for Open ID Connect providers, `OpenIdConnect`
is the `ProviderType` value for the AuthProvider object, but the expected `providerName` is `Open ID Connect` .

Return Value

Type: Map<String, String>


Apex Reference Guide AuthToken Class

##### refreshAccessToken(authProviderId, providerName, oldAccessToken)

Returns a map from the third-party provider’s identifier containing a refreshed access token for the currently logged-in Salesforce user.

Signature

```
   public static Map<String, String> refreshAccessToken(String authProviderId, String

   providerName, String oldAccessToken)

```

Parameters

```
   authProviderId
```

Type: String

```
   providerName
```

Type: String

The proper name of the third party. Here are valid values for each provider type.

**•** Apple— `Apple`

**•** Custom—For a custom authentication provider, use the value in the `FriendlyName` [field on the AuthProvider object, such](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_authprovider.htm)
as `MyProvider` .

**•** Facebook— `Facebook`

**•** GitHub— `GitHub`

**•** Google— `Google`

**•** Janrain—Use the proper name of the third party, such as `Yahoo!` .

**•** LinkedIn— `LinkedIn`

**•** Microsoft— `Microsoft`

**•** Microsoft Access Control Service— `Microsoft Access Control Service`

**•** MuleSoft— `MuleSoft`

**•** Open ID Connect— `Open ID Connect`

**•** Salesforce— `Salesforce`

**•** Slack— `Slack`

**•** Twitter—This method doesn’t support the Twitter authentication provider.

Note: The `providerName` value that you pass into this method can be different from the value that’s returned if you
query the `ProviderType` field on the AuthProvider object. For example, for Open ID Connect providers, `OpenIdConnect`
is the `ProviderType` value for the AuthProvider object, but the expected `providerName` is `Open ID Connect` .

```
   oldAccessToken
```

Type: String

Return Value

Type: Map<String, String>


Apex Reference Guide AuthToken Class

Usage

The returned map contains `AccessToken` and `RefreshError` keys. Evaluate the keys in the response to check if the request
was successful. For a successful request, the `RefreshError` value is `null`, and `AccessToken` is a token value. For an unsuccessful
request, the `RefreshError` value is an error message, and the `AccessToken` value is `null` .

When successful, this method updates the token stored in the database, which you can get using
`Auth.AuthToken.getAccessToken()` .

If you’re using an OpenID Connect authentication provider, an `id_token` isn’t required in the response from the provider. If a **Token**
**Issuer** is specified in the **Auth. Provider** settings and an `id_token` is provided anyway, Salesforce verifies it.

Example

```
   String accessToken = Auth.AuthToken.getAccessToken('0SOD000000000DeOAI', 'Open ID Connect');

   Map<String, String> responseMap = Auth.AuthToken.refreshAccessToken('0SOD000000000DeOAI',

    'Open ID Connect', accessToken);

```

A successful request includes the access token in the response.

```
    (RefreshError,null)(AccessToken,00DD00000007BhE!AQkAQFzj...)

##### revokeAccess(authProviderId, providerName, userId, remoteIdentifier)

```

Revokes the access token for a specified SSO user from a provider such as Facebook. You can use this method only if the
`IsNotSsoUsable` field on the associated ThirdPartyAccountLink object is set to `false` .

Signature

```
   public static Boolean revokeAccess(String authProviderId, String providerName, String

   userId, String remoteIdentifier)

```

Parameters

```
   authProviderId
```

Type: String

The ID of the authentication provider in Salesforce.

```
   providerName
```

Type: String

The name of the third party. Here are valid `providerName` values for each provider type.

Important: The `providerName` value that you pass into this method must be lowercase.

**•** Apple— `apple`

**•** Custom—For a custom authentication provider, use a lowercase version of the value in the `FriendlyName` field on the
[AuthProvider object. For example, if the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_authprovider.htm) `FriendlyName` is `MyProvider`, use `myprovider` .

**•** Facebook— `facebook`

**•** GitHub— `github`

**•** Google— `google`

**•** Janrain—Use a lowercase version of the name of the third party, such as `yahoo!` .


### Apex Reference Guide CommunitiesUtil Class

**•** LinkedIn— `linkedin`

**•** Microsoft— `microsoft`

**•** Microsoft Access Control Service— `microsoft access control service`

**•** MuleSoft— `mulesoft`

**•** Open ID Connect— `open id connect`

**•** Salesforce— `salesforce`

**•** Slack— `slack`

**•** Twitter— `twitter`

Note: The `providerName` that you pass into this method is different from the value that you get if you query the
`ProviderType` field on the AuthProvider object. For example, for Open ID Connect providers, the `providerType`
value for the AuthProvider object is `OpenIdConnect`, but the `providerName` for the `revokeAccess` method is
`open id connect` .

```
   userId
```

Type: String

The 15-character ID for the user whose access is being revoked.

```
   remoteIdentifier
```

Type: String

The unique ID for the user in the third-party system (this value is in the associated ThirdPartyAccountLink standard object).

Return Value

Type: Boolean

The return value is `true` if the `revokeAccess()` operation is successful; otherwise `false` .

Example

The following example revokes a Facebook user's access token.

```
   Auth.AuthToken.revokeAccess('0SOxx00000#####', 'facebook', '005xx00000#####',

   'ThirdPartyIdentifier_exist214176560#####');

### CommunitiesUtil Class

```

Contains methods for getting information about an Experience Cloud user.

Namespace

Auth

Example

The following example directs a guest (unauthenticated) user to one page, and authenticated users of the Experience Cloud site’s parent
organization to another page.

```
   if (Auth.CommunitiesUtil.isGuestUser())

      // Redirect to the login page if user is an unauthenticated user

```


Apex Reference Guide CommunitiesUtil Class

```
      return new PageReference(LOGIN_URL);

   if (Auth.CommunitiesUtil.isInternalUser())

      // Redirect to the home page if user is an internal user

      return new PageReference(HOME_URL);

#### CommunitiesUtil Methods The following are methods for CommunitiesUtil . All methods are static.

```

IN THIS SECTION:

##### getLogoutUrl()

Returns the page to display after the current Experience Cloud user logs out.

##### getUserDisplayName()

Returns the current user’s Experience Cloud display name.

##### isGuestUser()

Indicates whether the current user isn’t logged in to the Experience Cloud site. Redirect the user to log in, if necessary.

isInternalUser()
Indicates whether the current user is logged in as a member of the parent Salesforce organization, such as an employee.

##### getLogoutUrl()

Returns the page to display after the current Experience Cloud user logs out.

Signature

```
   public static String getLogoutUrl()

```

Return Value

Type: String

##### getUserDisplayName()

Returns the current user’s Experience Cloud display name.

Signature

```
   public static String getUserDisplayName()

```

Return Value

Type: String

##### isGuestUser()

Indicates whether the current user isn’t logged in to the Experience Cloud site. Redirect the user to log in, if necessary.


### Apex Reference Guide ConfigurableSelfRegHandler Interface

Signature

```
   public static Boolean isGuestUser()

```

Return Value

Type: Boolean

##### isInternalUser()

Indicates whether the current user is logged in as a member of the parent Salesforce organization, such as an employee.

Signature

```
   public static Boolean isInternalUser()

```

Return Value

Type: Boolean

### ConfigurableSelfRegHandler Interface

Gives you more control over how customers or partners self-register for your Experience Cloud site by creating a class that implements
`Auth.ConfigurableSelfRegHandler` . You choose the user information to collect, and how users identify themselves—with
their email address, phone number, or another identifier. When verified, you create a customer or partner user and log in the user to
your Experience Cloud site.

Namespace

Auth

Usage

You set up site self-registration declaratively on the Login & Registration (L&R) page of the Administration workspace. When combined
with a configurable self-registration setup, the handler class can programmatically fill in user fields, including custom fields, and determine
how to create a user and log them in.

When you select the Configurable Self-Reg Page registration page, you choose the user fields to collect from the self-registration form,
such as last name, first name, username, nickname, mobile, or email. You also determine the verification method that the user identifies
themselves with, which can be email, mobile, or neither. Salesforce generates the `Auth.ConfigurableSelfRegHandler`
handler, which contains logic on how to create an Experience Cloud site member. Modify the handler to change how users are created,
and how collected user information is used.

You can add custom logic to ensure that the email or phone number is unique to the customer or partner who's registering. For example,
you can add a custom unique field, and write a copy of the email or phone number to it. You can also change how the user is created.
By default, the user is created as a contact associated with the account that you select on the L&R page.

### The generated ConfigurableSelfRegHandler is located on the Setup Apex Classes page, and begins with

`AutocreatedConfigSelfReg`, for example, `AutocreatedConfigSelfReg1532475901849` .

[For an example, see ConfigurableSelfRegHandler Example Implementation. For more details, see Salesforce Customer Identity in](https://help.salesforce.com/articleView?id=identity_about_customers_partners.htm&language=en_US) _Salesforce_
_Help_ .


Apex Reference Guide ConfigurableSelfRegHandler Interface

IN THIS SECTION:

#### ConfigurableSelfRegHandler Method

ConfigurableSelfRegHandler Example Implementation
This Apex code implements the `Auth.ConfigurableSelfRegHandler` interface. After the customer or partner fills out
the sign-up page and submits it, the handler is invoked to create an Experience Cloud member with the supplied information. If the
registration process requires email or phone verification, the verification process finishes before the
##### Auth.ConfigurableSelfRegHandler.createUser is invoked. If verification isn’t required, createUser is invoked

when the customer or partner submits the page.

#### ConfigurableSelfRegHandler Method The following is the method for ConfigurableSelfRegHandler .

IN THIS SECTION:

##### createUser(accountId, profileId, registrationAttributes, password)

Create a community member from the information that the visitor provided on your community’s self-registration page.

##### createUser(accountId, profileId, registrationAttributes, password)

Create a community member from the information that the visitor provided on your community’s self-registration page.

Signature

```
   public Id createUser(Id accountId, Id profileId, Map<Schema.SObjectField,String>

   registrationAttributes, String password)

```

Parameters

```
   accountId
```

Type: Id

Default account with which the new user is associated. This value comes from the Account field setting on Login and Registration
(L&R) page under Registration Page Configuration.

```
   profileID
```

Type: Id

Profile to assign the new user. This value comes from the Profile field setting on the L&R page under Registration Page Configuration.

```
   registrationAttributes
```

Type: Map<Schema.sObjectField,String>

A map of attributes that the registering user entered on the self-registration page. The fields that appear on the self-registration
page come from the User Fields selected on the L&R page when the registration type is Configurable Self-Reg Page.

```
   password
```

Type: String

The password entered by the user if “Include Password” is selected on the L&R page. (If a password isn’t entered, the handler must
generate one because a password is required to create a user.)


Apex Reference Guide ConfigurableSelfRegHandler Interface

Return Value

Type: Id

Returns an identifier for the created User object. `Auth.ConfigurableSelfRegHandler` inserts a user and then returns the ID
of that user.

#### ConfigurableSelfRegHandler Example Implementation

This Apex code implements the `Auth.ConfigurableSelfRegHandler` interface. After the customer or partner fills out the
sign-up page and submits it, the handler is invoked to create an Experience Cloud member with the supplied information. If the registration
process requires email or phone verification, the verification process finishes before the
`Auth.ConfigurableSelfRegHandler.createUser` is invoked. If verification isn’t required, `createUser` is invoked
when the customer or partner submits the page.

Verification occurs by email if the admin chose Email as the verification method when setting up the Configurable Self-Reg handler on
the Login & Registration (L&R) page. When a visitor clicks the sign-up link from the login page, Salesforce prompts for an email address
and then sends a one-time password to the specified email address. If the visitor enters the verification code successfully on the verify
page, the user is created and logged in. Likewise, if the admin chose Text Message as the verification method on the L&R page, the visitor
is prompted to enter a phone number. Salesforce sends a challenge (verification code) via SMS to the user. If successful, the user is
created and logged in. Requiring verification before creating a user reduces the number of dummy users cluttering your org.

The `Auth.ConfigurableSelfRegHandler` class contains logic for generating the user fields required to create a user in case
the user doesn’t supply them. The handler generates default values, ensuring that the values are unique by appending a timestamp.
You can modify the handler to make sure that the email address and phone number of the customer or partner are also unique.

```
   global class AutocreatedConfigSelfReg implements Auth.ConfigurableSelfRegHandler {

      private final Long CURRENT_TIME = Datetime.now().getTime();

      private final String[] UPPERCASE_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

      private final String[] LOWERCASE_CHARS = 'abcdefghijklmnopqrstuvwxyz'.split('');

      private final String[] NUMBER_CHARS = '1234567890'.split('');

      private final String[] SPECIAL_CHARS = '!#$%-_=+<>'.split('');

      // This method is called once after verification (if any was configured).

      // This method should create a user and insert it.

      // Password can be null.

      // Return null or throw an exception to fail creation.

      global Id createUser(Id accountId, Id profileId, Map<SObjectField, String>

   registrationAttributes, String password) {

        User u = new User();

        u.ProfileId = profileId;

        for (SObjectField field : registrationAttributes.keySet()) {

           String value = registrationAttributes.get(field);

           u.put(field, value);

        }

        u = handleUnsetRequiredFields(u);

        generateContact(u, accountId);

        if (String.isBlank(password)) {

           password = generateRandomPassword();

        }

        Site.validatePassword(u, password, password);

        if (u.contactId == null) {

           return Site.createExternalUser(u, accountId, password);

```


Apex Reference Guide ConfigurableSelfRegHandler Interface

```
        }

        u.languagelocalekey = UserInfo.getLocale();

        u.localesidkey = UserInfo.getLocale();

        u.emailEncodingKey = 'UTF-8';

        u.timeZoneSidKey = UserInfo.getTimezone().getID();

        insert u;

        System.setPassword(u.Id, password);

        return u.id;

      }

      // Method to autogenerate a password if one isn't passed in.

      // By setting a password for a user, we won't send a

      // welcome email to set the password.

      private String generateRandomPassword() {

        String[] characters = new List<String>(UPPERCASE_CHARS);

        characters.addAll(LOWERCASE_CHARS);

        characters.addAll(NUMBER_CHARS);

        characters.addAll(SPECIAL_CHARS);

        String newPassword = '';

        Boolean needsUpper = true, needsLower = true, needsNumber = true, needsSpecial =

   true;

        while (newPassword.length() < 50) {

           Integer randomInt = generateRandomInt(characters.size());

           String c = characters[randomInt];

           if (needsUpper && c.isAllUpperCase()) {

             needsUpper = false;

           } else if (needsLower && c.isAllLowerCase()) {

             needsLower = false;

           } else if (needsNumber && c.isNumeric()) {

             needsNumber = false;

           } else if (needsSpecial && !c.isAlphanumeric()) {

             needsSpecial = false;

           }

           newPassword += c;

        }

        newPassword = addMissingPasswordRequirements(newPassword, needsLower, needsUpper,

    needsNumber, needsSpecial);

        return newPassword;

      }

      private String addMissingPasswordRequirements(String password, Boolean addLowerCase,

   Boolean addUpperCase, Boolean addNumber, Boolean addSpecial) {

        if (addLowerCase) {

           password += LOWERCASE_CHARS[generateRandomInt(LOWERCASE_CHARS.size())];

        }

        if (addUpperCase) {

           password += UPPERCASE_CHARS[generateRandomInt(UPPERCASE_CHARS.size())];

        }

        if (addNumber) {

           password += NUMBER_CHARS[generateRandomInt(NUMBER_CHARS.size())];

        }

        if (addSpecial) {

           password += SPECIAL_CHARS[generateRandomInt(SPECIAL_CHARS.size())];

        }

        return password;

```


Apex Reference Guide ConfigurableSelfRegHandler Interface

```
      }

     // Generates a random number from 0 up to, but not including, max.

      private Integer generateRandomInt(Integer max) {

        return Math.mod(Math.abs(Crypto.getRandomInteger()), max);

      }

      // Loops over required fields that were not passed in to

      // set to some default value.

      private User handleUnsetRequiredFields(User u) {

        if (String.isBlank(u.LastName)){

           u.LastName = generateLastName();

        }

        if (String.isBlank(u.Username)) {

           u.Username = generateUsername();

        }

        if (String.isBlank(u.Email)) {

           u.Email = generateEmail();

        }

        if (String.isBlank(u.Alias)) {

           u.Alias = generateAlias();

        }

        if (String.isBlank(u.CommunityNickname)) {

           u.CommunityNickname = generateCommunityNickname();

        }

        return u;

      }

      // Method to construct a contact for a user.

      private void generateContact(User u, Id accountId) {

        // Add logic here if you want to build your own

        // contact for the use.

      }

     // Default implementation to try to provide uniqueness.

      private String generateAlias() {

        String timeString = String.valueOf(CURRENT_TIME);

        return timeString.substring(timeString.length() - 8);

      }

      // Default implementation to try to provide uniqueness.

      private String generateLastName() {

        return 'ExternalUser' + CURRENT_TIME;

      }

      // Default implementation to try to provide uniqueness.

      private String generateUsername() {

        return 'externaluser' + CURRENT_TIME + '@company.com';

      }

      // Default implementation to try to provide uniqueness.

      private String generateEmail() {

        return 'externaluser' + CURRENT_TIME + '@company.com';

      }

      // Default implementation to try to provide uniqueness.

      private String generateCommunityNickname() {

        return 'ExternalUser' + CURRENT_TIME;

      }

   }

```


### Apex Reference Guide ConfirmUserRegistrationHandler Interface ConfirmUserRegistrationHandler Interface

Manages single sign-on (SSO) user mappings between Salesforce and a third-party identity provider. Use this interface to confirm user
mappings before updating them.

Namespace

Auth

Usage

When you set up SSO with a third-party identity provider, you create a class that implements a registration handler using the
`Auth.RegistrationHandler` interface. This class manages the process of creating and updating users. For advanced use cases
that require you to confirm user information during the update process, implement the
`Auth.ConfirmUserRegistrationHandler` interface in your class. This interface must be implemented in addition to
`Auth.RegistrationHandler` .

You can use the `Auth.ConfirmUserRegistrationHandler` interface to ensure that users are mapped correctly between
Salesforce and the third party. When a user who has previously logged in with an authentication provider logs in again, you can confirm
that the incoming user data is consistent with the user's third-party identifier. If not, you can identify which user is supposed to be logged
in.

You can also use the `Auth.ConfirmUserRegistrationHandler` interface to switch context for users with multiple records.
For example, a user has two records—an admin user and a standard user. When the user logs in, the third-party identity provider confirms
[the account used to log in and sends the response to Salesforce via the UserInfo endpoint. You can then use this information to determine](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_using_userinfo_endpoint.htm&type=5&language=en_US)
whether to log in the user as an admin or standard user.

IN THIS SECTION:

#### ConfirmUserRegistrationHandler Methods

ConfirmUserRegistrationHandler Example Implementation

#### ConfirmUserRegistrationHandler Methods

### The following are methods for ConfirmUserRegistrationHandler .

IN THIS SECTION:

##### confirmUser(userId, tpalId, portalId, userdata)

Returns the ID of the user to be logged in based on their mapping to a third-party identifier. This method is called before calling the
`[updateUser()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_auth_plugin.htm#apex_Auth_RegistrationHandler_updateUser)` method. It's called only if the incoming user has previously logged in and has a third-party account link to a
Salesforce user.

##### **`confirmUser(userId, tpalId, portalId, userdata)`**

Returns the ID of the user to be logged in based on their mapping to a third-party identifier. This method is called before calling the
`[updateUser()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_auth_plugin.htm#apex_Auth_RegistrationHandler_updateUser)` method. It's called only if the incoming user has previously logged in and has a third-party account link to a Salesforce
user.


Apex Reference Guide ConfirmUserRegistrationHandler Interface

Signature

```
   public Id confirmUser(Id userId, Id tpalId, Id portalId, Auth.UserData userdata)

```

Parameters

```
   userId
```

Type: Id

The ID of the user who is mapped to the third-party identifier via a third-party account link.

```
   tpalId
```

Type: Id

The third-party account link corresponding to the third-party identifier.

```
   portalId
```

Type: Id

The portal ID the user is logging in to. If there's no portal configured, this value can be null.

```
   userData
```

[Type: Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_UserData.htm#apex_class_Auth_UserData)

Contains user information from the third-party identity provider.

Return Value

Type: Id

The Id of the user to be logged in. If null, login fails.

#### ConfirmUserRegistrationHandler Example Implementation

This example implements the `Auth.ConfirmUserRegistrationHandler` interface during the user update process to
confirm that the correct user is logging in based on their email address and last name.

```
   global class StandardUserRegistrationHandler implements Auth.RegistrationHandler,

   Auth.ConfirmUserRegistrationHandler {

      global User createUser(Id portalId, Auth.UserData data){

        User u = new User();

        Profile p = [SELECT Id FROM profile WHERE name='Standard User'];

        u.username = data.username + '@salesforce.com';

        u.email = data.email;

        u.lastName = data.lastName;

        u.firstName = data.firstName;

        String alias = data.username;

        if(alias.length() > 8) {

           alias = alias.substring(0, 8);

        }

        u.alias = alias;

        u.languagelocalekey = data.attributeMap.get('language');

        u.localesidkey = data.locale;

        u.emailEncodingKey = 'UTF-8';

        u.timeZoneSidKey = 'America/Los_Angeles';

        u.profileId = p.Id;

        return u;

```


### Apex Reference Guide ConnectedAppPlugin Class

```
      }

      global void updateUser(Id userId, Id portalId, Auth.UserData data) {

        User u = new User(id=userId);

        u.username = data.username + '@salesforce.com';

        u.email = data.email;

        u.lastName = data.lastName;

        u.firstName = data.firstName;

        String alias = data.username;

        if(alias.length() > 8) {

           alias = alias.substring(0, 8);

        }

        u.alias = alias;

        u.languagelocalekey = data.attributeMap.get('language');

        u.localesidkey = data.locale;

        update(u);

      }

      global Id confirmUser(Id userId, Id tpalId, Id portalId, Auth.UserData data) {

        if (data.email.contains(data.lastName)) { // looks genuine

           return userId;

        } else { // find the right user

           User confirmedUser = [SELECT id FROM user WHERE email=:data.email];

           return confirmedUser.Id;

        }

      }

   }

```

The following example tests the implementation:

```
   @isTest

   public class StandardUserRegistrationHandlerTest {

      static testMethod void testConfirmUser() {

        StandardUserRegistrationHandler handler = new StandardUserRegistrationHandler();

        Auth.UserData sampleData = new Auth.UserData('idA', 'firstName', 'A',

           'firstName A', 'userA@example.org', null, 'usernameA', 'en_US', 'facebook',

           null, new Map<String, String>{'language' => 'en_US'});

        User u = handler.createUser(null, sampleData);

        insert(u);

        String uid = u.id;

        sampleData = new Auth.UserData('idB', 'firstName', 'B',

           'firstName B', 'userA@example.org', null, 'usernameB', 'en_US', 'facebook',

           null, new Map<String, String>{}); // note that user B is using userA's email

       Id confirmedUserId = handler.confirmUser(uid, '060xx0000004Eh6', null, sampleData);

        System.assertEquals(uid, confirmedUserId); // we should see userA's id

      }

   }

### ConnectedAppPlugin Class

```

Contains methods for extending the behavior of a connected app, for example, customizing how a connected app is invoked depending
on the protocol used. This class gives you more control over the interaction between Salesforce and your connected app.


Apex Reference Guide ConnectedAppPlugin Class

Namespace

Auth

Usage

When you create a connected app, you specify general information about the app and settings for OAuth, web apps, mobile apps, and
canvas apps. To customize how the app is invoked, create a connected app handler with this `ConnectedAppPlugin` Apex class.
For example, use this class to support new authentication protocols or respond to user attributes in a way that benefits a business process.

When you create a connected app handler, you also configure the `ConnectedAppPlugin` class to run as an execution user. The
execution user authorizes access for the connected app. For example, when you use the `authorize` method, the execution user
authorizes the connected app to access data.

If you don't specify an execution user, the plug-in runs as an Automated Process User, which is a system user that executes tasks behind
the scenes. Most `ConnectedAppPlugin` methods require that you specify an execution user, with the exception of the
`customAttributes` [method. For more information, see Create a Custom Connected App Handler.](https://help.salesforce.com/articleView?id=xcloud.connected_app_create_custom_handler.htm&type=5&language=en_US)

Example

This example authorizes the connected app user to use the connected app if the context is SAML and the user has reached the quota
tracked in a custom field. It returns the user’s permission set assignments. The example uses `Auth.InvocationContext` to
modify a SAML assertion before it’s sent to the service provider.

```
   global class ConnectedAppPluginExample extends Auth.ConnectedAppPlugin

   {

      // Authorize the app if the user has achieved quota tracked in a custom field

     global override Boolean authorize(Id userId, Id connectedAppId, Boolean isAdminApproved,

    Auth.InvocationContext context)

      {

        // Create a custom boolean field HasAchievedQuota__c on the user record

        // and then uncomment the block below

        // User u = [select id, HasAchievedQuota__c from User where id =: userId].get(0);

        // return u.HasAchievedQuota__c;

        return isAdminApproved;

      }

      // Call a flow during refresh

      global override void refresh(Id userId, Id connectedAppId, Auth.InvocationContext

   context)

      {

        try

        {

         Map<String, Object> inputVariables = new Map<String, Object>();

         inputVariables.put('userId', userId);

         inputVariables.put('connectedAppId', connectedAppId);

         // Create a custom trigger ready flow and uncomment the block below

         // Flow.Interview.MyCustomFlow interview = new

   Flow.Interview.MyCustomFlow(inputVariables);

         // interview.start();

        } catch ( Exception e ) {

```


Apex Reference Guide ConnectedAppPlugin Class

```
          System.debug('FLOW Exception:' + e);

        }

      }

      // Return a user’s permission set assignments

      global override Map<String,String> customAttributes(Id userId, Id connectedAppId,

   Map<String,String>

        formulaDefinedAttributes, Auth.InvocationContext context)

      {

        List<PermissionSetAssignment> psas = [SELECT id, PermissionSet.Name FROM

   PermissionSetAssignment

        WHERE PermissionSet.IsOwnedByProfile = false AND (AssigneeId = :userId)];

        String permsets = '[';

        for (PermissionSetAssignment psa :psas)

        {

           permsets += psa.PermissionSet.Name + ';';

        }

        permsets += ']';

        formulaDefinedAttributes.put('PermissionSets', permsets);

        return formulaDefinedAttributes;

      }

   }

```

IN THIS SECTION:

#### ConnectedAppPlugin Methods ConnectedAppPlugin Methods The following are methods for ConnectedAppPlugin .

IN THIS SECTION:

authorize(userId, connectedAppId, isAdminApproved)
Deprecated and available only in API versions 35.0 and 36.0. As of version 37.0, use `authorize(userId, connectedAppId,`
`isAdminApproved, context)` instead.

authorize(userId, connectedAppId, isAdminApproved, context)
Authorizes the specified user to access the connected app. If the connected app is set for users to self-authorize, this method isn’t
invoked.

customAttributes(userId, connectedAppId, formulaDefinedAttributes)
Deprecated and available only in API versions 35.0 and 36.0. As of version 37.0, use `customAttributes(userId,`
`connectedAppId, formulaDefinedAttributes, context)` instead.

customAttributes(userId, connectedAppId, formulaDefinedAttributes, context)
Sets new attributes for the specified user. When the connected app gets the user’s attributes from the UserInfo endpoint or through
a SAML assertion, use this method to update the attribute values.

modifySAMLResponse(authSession, connectedAppId, samlResponse)
Modifies the XML generated by the Salesforce SAML Identity Provider (IDP) before it’s sent to the service provider.


Apex Reference Guide ConnectedAppPlugin Class

refresh(userId, connectedAppId)
Deprecated and available only in API versions 35.0 and 36.0. As of version 37.0, use `refresh(userId, connectedAppId,`
`context)` instead.

refresh(userId, connectedAppId, context)
Salesforce calls this method during a refresh token exchange.

##### authorize(userId, connectedAppId, isAdminApproved) Deprecated and available only in API versions 35.0 and 36.0. As of version 37.0, use authorize(userId, connectedAppId,

`isAdminApproved, context)` instead.

Signature

```
   public Boolean authorize(Id userId, Id connectedAppId, Boolean isAdminApproved)

```

Parameters

```
   userId
```

Type: Id

The 15-character ID of the user attempting to use the connected app.

```
   connectedAppId
```

Type: String

The 15-character ID of the connected app.

```
   isAdminApproved
```

Type: Boolean

The approval state of the specified user when the connected app requires approval.

Return Value

Type: Boolean

If the connected app requires admin approval, a returned value of `true` indicates that the current user is approved.

##### authorize(userId, connectedAppId, isAdminApproved, context)

Authorizes the specified user to access the connected app. If the connected app is set for users to self-authorize, this method isn’t invoked.

Signature

```
   public Boolean authorize(Id userId, Id connectedAppId, Boolean isAdminApproved,

   Auth.InvocationContext context)

```

Parameters

```
   userId
```

Type: Id

The 15-character ID of the user attempting to use the connected app.


Apex Reference Guide ConnectedAppPlugin Class

```
   connectedAppId
```

Type: Id

The 15-character ID of the connected app.

```
   isAdminApproved
```

Type: Boolean

The approval state of the specified user when the connected app requires approval.

```
   context
```

Type: InvocationContext

The context in which the connected app is invoked.

Return Value

Type: Boolean

If the connected app requires admin approval, a returned value of `true` indicates that the user is approved.

Usage

`ConnectedAppPlugin` runs on behalf of the current user. But the user must have permission to use the connected app for the
plug-in to work. Use this method to authorize the user.

##### customAttributes(userId, connectedAppId, formulaDefinedAttributes) Deprecated and available only in API versions 35.0 and 36.0. As of version 37.0, use customAttributes(userId,

`connectedAppId, formulaDefinedAttributes, context)` instead.

Signature

```
   public Map<String,String> customAttributes(Id userId, Id connectedAppId,

   Map<String,String> formulaDefinedAttributes,)

```

Parameters

```
   userId
```

Type: Id

The 15-character ID of the user attempting to use the connected app.

```
   connectedAppId
```

Type: Id

The 15-character ID of the connected app.

```
   formulaDefinedAttributes
```

Type: Map<String,String>

[A map of the new set of attributes from the UserInfo endpoint (OAuth) or from a SAML assertion. For more information, see The](https://help.salesforce.com/HTViewHelpDoc?id=remoteaccess_using_userinfo_endpoint.htm&language=en_US)
[UserInfo Endpoint in the online help.](https://help.salesforce.com/HTViewHelpDoc?id=remoteaccess_using_userinfo_endpoint.htm&language=en_US)

Return Value

Type: Map<String,String>


Apex Reference Guide ConnectedAppPlugin Class

A map of the updated set of attributes.

##### customAttributes(userId, connectedAppId, formulaDefinedAttributes, context)

Sets new attributes for the specified user. When the connected app gets the user’s attributes from the UserInfo endpoint or through a
SAML assertion, use this method to update the attribute values.

Signature

```
   public Map<String,String> customAttributes(Id userId, Id connectedAppId,

   Map<String,String> formulaDefinedAttributes, Auth.InvocationContext context)

```

Parameters

```
   userId
```

Type: Id

The 15-character ID of the user attempting to use the connected app.

```
   connectedAppId
```

Type: Id

The 15-character ID for the connected app.

```
   formulaDefinedAttributes
```

Type: Map<String,String>

[A map of the current set of attributes from the UserInfo endpoint (OAuth) or from a SAML assertion. For more information, see The](https://help.salesforce.com/HTViewHelpDoc?id=remoteaccess_using_userinfo_endpoint.htm&language=en_US)
[UserInfo Endpoint in the online help.](https://help.salesforce.com/HTViewHelpDoc?id=remoteaccess_using_userinfo_endpoint.htm&language=en_US)

```
   context
```

Type: InvocationContext

The context in which the connected app is invoked.

Return Value

Type: Map<String,String>

A map of the updated set of attributes.

##### modifySAMLResponse(authSession, connectedAppId, samlResponse)

Modifies the XML generated by the Salesforce SAML Identity Provider (IDP) before it’s sent to the service provider.

Signature

```
   public dom.XmlNode modifySAMLResponse(Map<String,String> authSession, Id connectedAppId,

   dom.XmlNode samlResponse)

```

Parameters

```
   authSession
```

Type: Map<String,String>


Apex Reference Guide ConnectedAppPlugin Class

The attributes for the authorized user’s session. The map includes the 15-character ID of the authorized user who’s accessing the
connected app.

```
   connectedAppId
```

Type: Id

The 15-character ID of the connected app.

```
   samlResponse
```

Type: Dom.XmlNode

Contains the SAML XML response generated by the IDP.

Return Value

Type: Dom.XmlNode

Returns an instance of Dom.XmlNode containing the modified SAML XML response.

Usage

Use this method to modify the XML SAML response to perform an action based on the context of the SAML request before it’s verified,
signed, and sent to the target service provider. This method enables developers to extend the connected app plug-in to meet their
specific needs.

The developer assumes full responsibility for changes made within the connected app plug-in. The plug-in must include validation and
error handling. If the plug-in throws an exception, catch it, log it, and stop the process. Don’t send anything to the target service provider.

##### refresh(userId, connectedAppId) Deprecated and available only in API versions 35.0 and 36.0. As of version 37.0, use refresh(userId, connectedAppId,

`context)` instead.

Signature

```
   public void refresh(Id userId, Id connectedAppId)

```

Parameters

```
   userId
```

Type: Id

The 15-character ID of the user requesting the refresh token.

```
   connectedAppId
```

Type: Id

The 15-character ID of the connected app.

Return Value

Type: void

##### refresh(userId, connectedAppId, context)

Salesforce calls this method during a refresh token exchange.


### Apex Reference Guide CustomOneTimePasswordDeliveryHandler Interface

Signature

```
   public void refresh(Id userId, Id connectedAppId, Auth.InvocationContext context)

```

Parameters

```
   userId
```

Type: Id

The 15-character ID of the user requesting the refresh token.

```
   connectedAppId
```

Type: Id

The 15-character ID of the connected app.

```
   context
```

Type: InvocationContext

The context in which the connected app is invoked.

Return Value

Type: void

### CustomOneTimePasswordDeliveryHandler Interface

To use a custom SMS provider to send one-time passwords (OTPs) for Experience Cloud identity verification, create a class that implements
the `Auth.CustomOneTimePasswordDeliveryHandler` interface.

Namespace

Auth

IN THIS SECTION:

#### CustomOneTimePasswordDeliveryHandler Methods

CustomOneTimePasswordDeliveryHandler Example Implementation

#### CustomOneTimePasswordDeliveryHandler Methods

### The following are methods for CustomOneTimePasswordDeliveryHandler .

IN THIS SECTION:

sendOneTimePassword(userId, phoneNumber, oneTimePassword, networkId, defaultText, expId)
Calls out to an external SMS messaging provider to send a Salesforce one-time password to an external user for identity verification.
Returns an `Auth.CustomOneTimePasswordDeliveryResult` indicating whether the provider sent the message.


Apex Reference Guide CustomOneTimePasswordDeliveryHandler Interface

##### **`sendOneTimePassword(userId, phoneNumber, oneTimePassword, networkId,`**

```
  defaultText, expId)

```

Calls out to an external SMS messaging provider to send a Salesforce one-time password to an external user for identity verification.
Returns an `Auth.CustomOneTimePasswordDeliveryResult` indicating whether the provider sent the message.

Signature

```
   public Auth.CustomOneTimePasswordDeliveryResult sendOneTimePassword(Id userId, String

   phoneNumber, String oneTimePassword, String defaultText, Id networkId, String

   experienceId)

```

Parameters

```
   userId
```

Type: Id

ID of the external user.

```
   phoneNumber
```

Type: String

The user’s phone number. The phone number isn't necessarily verified by Salesforce.

```
   oneTimePassword
```

Type: String

The OTP that the user receives.

```
   networkId
```

Type: String

ID of the Experience Cloud site.

```
   defaultText
```

Type: Id

The content of the default SMS message that the user receives. You can create custom messages instead of sending the default. For
example, write code to send custom messages based on the Experience Cloud site ID.

```
   expId
```

Type: String

A custom value that determines what the user experiences.

Return Value

Type: Auth.CustomOneTimePasswordDeliveryResult

#### CustomOneTimePasswordDeliveryHandler Example Implementation

This example implements the `Auth.CustomOneTimePasswordDeliveryHandler` interface. For a detailed explanation of
[this example, see Example: Custom One-Time Password Delivery Handler in Salesforce Help.](https://help.salesforce.com/s/articleView?id=xcloud.custom_otp_provider_example.htm&type=5&language=en_US)

```
   global class TelesignMessaging implements Auth.CustomOneTimePasswordDeliveryHandler{

     global Auth.CustomOneTimePasswordDeliveryResult sendOneTimePassword(Id userId, String

   phoneNumber, String oneTimePassword,

```


### Apex Reference Guide CustomOneTimePasswordDeliveryResult Enum

```
     String defaultText, Id networkId, String experienceId){

      //Send the message from Telesign

      HttpRequest request = new HttpRequest();

      //The commented-out code on the next line isn't necessary if you use named credentials

      //request.setEndpoint('https://rest-ww.telesign.com/v1/messaging');

      request.setEndpoint('callout:Telesign_SMS_Named');

      request.setMethod('POST');

     String requestBody = 'is_primary=true&phone_number=' + phoneNumber + '&message='+'Custom

    OTP%20'+ oneTimePassword+';

   '+defaultText+'&message_type=OTP';

      request.setHeader('accept', 'application/json');

      request.setHeader('content-type', 'application/x-www-form-urlencoded');

      //The commented-out code on the next line isn't necessary if you use named credentials

      //request.setHeader('authorization', 'Basic <Base64-encoded Telesign customer ID:API

   key>');

      request.setBody(requestBody);

      HttpResponse response = new Http().send(request);

      // Handle the response as needed

      return Auth.CustomOneTimePasswordDeliveryResult.SUCCESS;

     }

   }

### CustomOneTimePasswordDeliveryResult Enum

```

Indicates the status of an attempt to send a one-time password (OTP) to an external user via a custom messaging provider.

Usage

To use this feature, contact Salesforce Customer Support.

This enum specifies the result of the `sendOneTimePassword` method in an implementation of the
`Auth.CustomOneTimePasswordDeliveryHandler` interface.

Enum Values

The following are the values of the `Auth.CustomOneTimePasswordDeliveryResult` enum.

**Value** **Description**

`COUNTRY_BLOCK` Indicates that the user’s phone number has a country code that Salesforce doesn’t
support.

`EXCEPTION` Indicates that the handler threw an exception.

`INVALID_PHONE_NUMBER` Indicates that the user’s phone number isn’t valid. For example, it’s in the wrong
format or contains characters that aren’t numbers.


### Apex Reference Guide ExternalClientAppOauthHandler Class

**Value** **Description**

`MESSAGE_LIMIT_EXCEEDED` Indicates that your Experience Cloud site reached the message limit allowed by
your license.

`PROVIDER_ERROR` Indicates an error with the custom OTP service.

`SUCCESS` Indicates that the OTP message was successfully sent to the user.

### ExternalClientAppOauthHandler Class

Contains methods for extending the behavior of an external client app. For example, customize how an external client app is invoked
depending on the protocol used. This class gives you more control over the interaction between Salesforce and your external client app.

Namespace

Auth

Usage

When you create an external client app, you specify general information about the app and settings for OAuth. To customize how the
### app is invoked, create a external client app handler with the ExternalClientAppOauthHandler Apex class. For example, use

this class to support new authentication protocols or respond to user attributes in a way that benefits the business process.

### When you create an external client app handler, you also configure the ExternalClientAppOauthHandler class to run as an

execution user. The execution user authorizes access for the external client app. For example, when you use the authorize method, the
execution user authorizes the external client app to access data.

If you don't specify an execution user, the plug-in runs as an Automated Process User, which is a system user that executes tasks behind
### the scenes. Most ExternalClientAppOauthHandler methods require that you specify an execution user, with the exception

of the `customAttributes` method.

IN THIS SECTION:

#### ExternalClientAppOauthHandler Methods ExternalClientAppOauthHandler Methods

### The following are methods for ExternalClientAppOauthHandler .

IN THIS SECTION:

authorize(userId, ecAppId, isAdminApproved, context)
Authorizes the specified user to access the external client app. If the external client app is set for users to self-authorize, this method
isn’t invoked.

customAttributes(userId, ecAppId, formulaDefinedAttributes, context)
Sets new attributes for the specified user. When the external client app gets the user’s attributes from the UserInfo endpoint, use
this method to update the attribute values.

refresh(userId, ecAppId, context)
Salesforce calls this method during a refresh token exchange.


Apex Reference Guide ExternalClientAppOauthHandler Class

##### **`authorize(userId, ecAppId, isAdminApproved, context)`**

Authorizes the specified user to access the external client app. If the external client app is set for users to self-authorize, this method isn’t
invoked.

Signature

```
   public Boolean authorize(Id userId, Id ecAppId, Boolean isAdminApproved,

   Auth.InvocationContext context)

```

Parameters

```
   userId
```

Type: Id

The 15-character ID of the user attempting to use the external client app.

```
   ecAppId
```

Type: Id

The 15-character ID of the external client app.

```
   isAdminApproved
```

Type: Boolean

The approval state of the specified user when the external client app requires approval.

```
   context
```

Type: Auth.InvocationContext on page 136

The context in which the external client app is invoked.

Return Value

Type: Boolean

A returned value of `true` indicates that the user is approved.

##### **`customAttributes(userId, ecAppId, formulaDefinedAttributes, context)`**

Sets new attributes for the specified user. When the external client app gets the user’s attributes from the UserInfo endpoint, use this
method to update the attribute values.

Signature

```
   public Map<String,String> customAttributes(Id userId, Id ecAppId, Map<String,String>

   formulaDefinedAttributes, Auth.InvocationContext context)

```

Parameters

```
   userId
```

Type: Id

The 15-character ID of the user attempting to use the external client app.

```
   ecAppId
```

Type: Id


### Apex Reference Guide GeneratedUserData Class

The 15-character ID for the external client app.

```
   formulaDefinedAttributes
```

Type: Map<String,String>

A map of the current set of attributes from the UserInfo endpoint (OAuth) or from a SAML assertion. For more information, see The
UserInfo Endpoint in the online help.

```
   context
```

Type: Auth.InvocationContext

The context in which the external client app is invoked.

Return Value

Type: Map<String,String>

A map of the updated set of attributes.

##### **`refresh(userId, ecAppId, context)`**

Salesforce calls this method during a refresh token exchange.

Signature

```
   public void refresh(Id userId, Id ecAppId, Auth.InvocationContext context)

```

Parameters

```
   userId
```

Type: Id

The 15-character ID of the user requesting the refresh token.

```
   ecAppId
```

Type: Id

The 15-character ID of the external client app.

```
   context
```

Type: Auth.InvocationContext

The context in which the external client app is invoked.

Return Value

Type: void

### GeneratedUserData Class

Stores the output of the Generate User Data invocable action, which you can access in Flow Builder.

Namespace

Auth


Apex Reference Guide GeneratedUserData Class

Usage

For single sign-on (SSO) implementations that use the authentication provider framework, you must set up a registration handler that
creates and updates users who log in via the identity provider. In some cases, the identity provider doesn't return enough information
to create a user record in Salesforce. If you use Flow Builder for your registration handler, you can use the Generate User Data invocable
action to help you create complete user records. This action generates placeholder data for all required fields for the User object.

The `Auth.GeneratedUserData` class stores the output of this action. Use the output as an Apex-defined variable in the flow.
When you create a user, reference specific properties from this class to set values for required fields.

For more information, see these resources in Salesforce Help.

**•** [Flow Core Action: Generate User Data](http://platform.flow_ref_elements_actions_generate_user_data.htm)

**•** [Example: Authentication Provider Registration Handler Flow](https://help.salesforce.com/s/articleView?id=xcloud.sso_flow_registration_handler_example.htm&language=en_US)

IN THIS SECTION:

#### GeneratedUserData Constructors

GeneratedUserData Properties

#### GeneratedUserData Constructors The following are constructors for GeneratedUserData .

IN THIS SECTION:

##### GeneratedUserData(firstName, lastName, email, username, alias, languageLocaleKey, localesIdKey, emailEncodingKey, timeZoneSidKey)

The Generate User Data action in Flow Builder uses this constructor to create an instance of the `Auth.GeneratedUserData`
class.

##### **`GeneratedUserData(firstName, lastName, email, username, alias,`**

```
  languageLocaleKey, localesIdKey, emailEncodingKey, timeZoneSidKey)

```

The Generate User Data action in Flow Builder uses this constructor to create an instance of the `Auth.GeneratedUserData` class.

Signature

```
   public GeneratedUserData(String firstName, String lastName, String email, String

   username, String alias, String languageLocaleKey, String localesIdKey, String

   emailEncodingKey, String timeZoneSidKey)

```

Parameters

```
   firstName
```

Type: String

Stores a generated placeholder value for the user's first name. The generated value is `placeholder-first-name` .

```
   lastName
```

Type: String

Stores a generated placeholder value for the user's last name, also known as family name. The generated value is
`placeholder-last-name` .


Apex Reference Guide GeneratedUserData Class

```
   email
```

Type: String

Stores a generated placeholder value for the user's email address. The generated value is `placeholder-email@example.com` .

```
   username
```

Type: String

Stores a generated placeholder value for the user's username. The generated value is `placeholder-username<unique`
`14-character number>@example com`, such as `placeholder-username17370000000000@example`
`com` .

```
   alias
```

Type: String

Stores a generated placeholder value for the user's alias. The generated value is `alias` .

```
   languageLocaleKey
```

Type: String

Stores the default value for the user's language, such as `en_US` for English. The default value is the language for the registration
handler execution user. The execution user is specified in the Run As field in the authentication provider definition.

```
   localesIdKey
```

Type: String

Stores the default value for the user's locale, defined using two-letter International Organization for Standardization (ISO) codes. For
example, `en_US` indicates English (United States). The default value is the language for the registration handler execution user.
The execution user is specified in the Run As field in the authentication provider definition.

```
   emailEncodingKey
```

Type: String

Stores the default value for the email encoding type for the user, such as `UTF-8` . The email encoding type determines how Salesforce
encodes characters in outgoing emails. The default value is the email encoding key for the registration handler execution user. The
execution user is specified in the Run As field in the authentication provider definition.

```
   timeZoneSidKey
```

Type: String

Stores the default value for the user's time zone, such as `GMT-07:00) Pacific Daylight Time`
`(America/Los_Angeles)` . The time zone is defined using region and key city according to ISO standards. The default value
is the time zone for the registration handler execution user. The execution user is specified in the Run As field in the authentication
provider definition.

#### GeneratedUserData Properties The following are properties for GeneratedUserData .

IN THIS SECTION:

alias
Stores a generated placeholder value for the user's alias. The placeholder value is `alias` .

email
Stores a generated placeholder value for the user's email address. The placeholder value is
`placeholder-email@example.com` .


Apex Reference Guide GeneratedUserData Class

##### emailEncodingKey

Stores the default value for the email encoding type for the user, such as `UTF-8` . The email encoding type determines how Salesforce
encodes characters in outgoing emails. The default value is the email encoding key for the execution user specified in the Run As
field in the authentication provider definition.

firstName
Stores a generated placeholder value for the user's first name. The placeholder value is `placeholder-first-name` .

languageLocaleKey
Stores the default value for the user's language, such as `en_US` for English. The default value is the language for the registration
handler execution user. The execution user is specified in the Run As field in the authentication provider definition.

lastName
Stores a generated placeholder value for the user's last name, also known as family name. The placeholder value is
`placeholder-last-name` .

localesIdKey
Stores the default value for the user's locale, defined using two-letter International Organization for Standardization (ISO) codes. For
example, `en_US` indicates English (United States). The default value is the language for the registration handler execution user.
The execution user is specified in the Run As field in the authentication provider definition.

timeZoneSidKey
Stores the default value for the user's time zone, such as `(GMT-07:00) Pacific Daylight Time`
`(America/Los_Angeles)` . The time zone is defined using region and key city according to ISO standards. The default value
is the time zone for the registration handler execution user. The execution user is specified in the Run As field in the authentication
provider definition.

username
Stores a generated placeholder value for the user's username. The placeholder value is `placeholder-username<unique`
`14-character number>@example com`, such as `placeholder-username17370000000000@example`
`com` .

##### **`alias`** Stores a generated placeholder value for the user's alias. The placeholder value is alias .

Signature

```
   public String alias {get; set;}

```

Property Value

Type: String

##### **`email`**

Stores a generated placeholder value for the user's email address. The placeholder value is `placeholder-email@example.com` .

Signature

```
   public String email {get; set;}

```


Apex Reference Guide GeneratedUserData Class

Property Value

Type: String

##### **`emailEncodingKey`**

Stores the default value for the email encoding type for the user, such as `UTF-8` . The email encoding type determines how Salesforce
encodes characters in outgoing emails. The default value is the email encoding key for the execution user specified in the Run As field
in the authentication provider definition.

Signature

```
   public String emailEncodingKey {get; set;}

```

Property Value

Type: String

##### **`firstName`**

Stores a generated placeholder value for the user's first name. The placeholder value is `placeholder-first-name` .

Signature

```
   public String firstName {get; set;}

```

Property Value

Type: String

##### **`languageLocaleKey`**

Stores the default value for the user's language, such as `en_US` for English. The default value is the language for the registration handler
execution user. The execution user is specified in the Run As field in the authentication provider definition.

Signature

```
   public String languageLocaleKey {get; set;}

```

Property Value

Type: String

##### **`lastName`**

Stores a generated placeholder value for the user's last name, also known as family name. The placeholder value is
`placeholder-last-name` .

Signature

```
   public String lastName {get; set;}

```


### Apex Reference Guide HeadlessSelfRegistrationHandler Interface

Property Value

Type: String

##### **`localesIdKey`**

Stores the default value for the user's locale, defined using two-letter International Organization for Standardization (ISO) codes. For
example, `en_US` indicates English (United States). The default value is the language for the registration handler execution user. The
execution user is specified in the Run As field in the authentication provider definition.

Signature

```
   public String localesIdKey {get; set;}

```

Property Value

Type: String

##### **`timeZoneSidKey`**

Stores the default value for the user's time zone, such as `(GMT-07:00) Pacific Daylight Time`
`(America/Los_Angeles)` . The time zone is defined using region and key city according to ISO standards. The default value is
the time zone for the registration handler execution user. The execution user is specified in the Run As field in the authentication provider
definition.

Signature

```
   public String timeZoneSidKey {get; set;}

```

Property Value

Type: String

##### **`username`**

Stores a generated placeholder value for the user's username. The placeholder value is `placeholder-username<unique`
`14-character number>@example com`, such as `placeholder-username17370000000000@example com` .

Signature

```
   public String username {get; set;}

```

Property Value

Type: String

### HeadlessSelfRegistrationHandler Interface

Creates customer and partner users during the Headless Registration Flow.


Apex Reference Guide HeadlessSelfRegistrationHandler Interface

Namespace

Auth

Usage

The Headless Registration Flow allows you to control user registration experience in a third-party app while using Salesforce to authenticate
users and manage their data access. When you set up this flow, add users in the class that is implementing the
`Auth.HeadlessSelfRegistrationHandler` interface. This class runs after the user verifies their identity. For a detailed
[explanation of headless registration, see Headless Registration Flow for Private Clients or Headless Registration Flow for Public Clients,](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_headless_registration_private_clients.htm&type=5&language=en_US)
depending on your app type.

IN THIS SECTION:

#### HeadlessSelfRegistrationHandler Methods The following are methods for HeadlessSelfRegistrationHandler .

HeadlessSelfRegistrationHandler Example Implementation
This example class implements the `Auth.HeadlessSelfRegistrationHandler` interface to create a user. It finds or
creates an account to store the new user and creates a contact to associate with the account. It then creates the user based on
information that your client sends to Headless Registration API.

#### HeadlessSelfRegistrationHandler Methods The following are methods for HeadlessSelfRegistrationHandler .

IN THIS SECTION:

##### createUser(profileId, data, customUserDataMap, experienceId, password)

Returns a User object using information submitted by your off-platform app to Headless Registration API. The User object can be a
new user that hasn’t been inserted in your org’s database, or it can represent an existing user record. If it’s a new User object, Salesforce
inserts the user record for you.

##### **`createUser(profileId, data, customUserDataMap, experienceId, password)`**

Returns a User object using information submitted by your off-platform app to Headless Registration API. The User object can be a new
user that hasn’t been inserted in your org’s database, or it can represent an existing user record. If it’s a new User object, Salesforce inserts
the user record for you.

Signature

```
   public User createUser(Id profileId, Auth.UserData data, String customUserDataMap,

   String experienceId, String password)

```

Parameters

```
   profileId
```

Type: Id

The ID of the profile that is assigned to new users.


Apex Reference Guide HeadlessSelfRegistrationHandler Interface

```
   data
```

[Type: Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_UserData.htm)

A class that stores information about the user, such as their name and locale.

```
   customUserDataMap
```

Type: String

A string representation of a JSON object containing custom user information passed in during registration. We recommend that you
deserialize this string into the equivalent Apex class structure. Determine what custom information to collect when you build your
app’s registration experience.

```
   experienceId
```

Type: String

A custom value that determines what the end user experiences.

```
   password
```

Type: String

The user password.

Return Value

Type: User

#### HeadlessSelfRegistrationHandler Example Implementation

This example class implements the `Auth.HeadlessSelfRegistrationHandler` interface to create a user. It finds or creates
an account to store the new user and creates a contact to associate with the account. It then creates the user based on information that
your client sends to Headless Registration API.

```
   global class ExampleHeadlessReg implements Auth.HeadlessSelfRegistrationHandler {

      // TO DO: Update this constant with the actual value for your use case

      private static final String CUSTOMER_ACCOUNT = 'My Account';

      /*

      * Retrieve an existing account or create a new one if it doesn't exist

      *

      * @param accountName - The name of the Account to find or create

      * @return Account - The found or newly created Account record

      */

      private Account findOrCreateAccount(String accountName) {

        List<Account> existingAccounts = [SELECT Id FROM Account WHERE Name=:accountName

   LIMIT 1];

        if (existingAccounts.isEmpty()) {

           Account newAccount = new Account(Name = accountName);

           insert(newAccount);

           return newAccount;

        }

        return existingAccounts[0];

      }

      /*

```


Apex Reference Guide HeadlessSelfRegistrationHandler Interface

```
      * Create a contact and associate it with an account

      *

      * @param account - The Account object to associate the contact with

      * @param user - The User object containing the first and last name for the contact

      * @return Contact - The newly created contact record

      */

      private Contact createContact(Account account, User user) {

        Contact c = new Contact();

        c.accountId = account.Id;

        c.firstName = user.firstName;

        c.lastName = user.lastName;

        insert(c);

        return c;

      }

      //TO DO: Implement any additional password validation that you want in this method.

      // In this example, the password was already checked to ensure that it complies with

   the org’s password policy,

      // and the password, if present, is set automatically for the new user when they are

   returned from the createUserMethod.

      private Boolean isPasswordValid(String password) {

        return true;

      }

      global User createUser(Id profileId, Auth.UserData data, String customUserDataMap,

   String experienceId, String password){

        if (!isPasswordValid(password)) {

           return null;

        }

        User u = new User();

        u.Username = data.username;

        u.ProfileId = profileId;

        u.Email = data.email;

        u.LastName = data.lastName;

        u.FirstName = data.firstName;

        String alias = data.username;

        // Alias must be 8 characters or less

        if (alias.length() > 8) {

           alias = alias.substring(0, 8);

        }

        u.Alias = alias;

        Account a = findOrCreateAccount(CUSTOMER_ACCOUNT);

        Contact c = createContact(a, u);

        u.ContactId = c.Id;

        u.LanguageLocaleKey = UserInfo.getLocale();

        u.LocaleSidKey = UserInfo.getLocale();

        u.EmailEncodingKey = 'UTF-8';

        u.TimeZoneSidKey = UserInfo.getTimezone().getID();

        return u;

```


### Apex Reference Guide HeadlessUserDiscoveryHandler Interface

```
      }

   }

### HeadlessUserDiscoveryHandler Interface

```

Use this interface to create a headless user discovery handler that you implement during headless login, passwordless login, and forgot
password flows.

Namespace

Auth

Usage

Develop headless authorization flows where users log in to an off-platform app with an identifier other than their username, such as an
email address, phone number, or order number. When a user enters the identifier in your headless app, your app sends the identifying
information to a Salesforce endpoint. Salesforce then passes the identifying information to your implementation of the
`Auth.HeadlessUserDiscoveryHandler` interface. The handler finds the user's account and its associated email address or
phone number.

Headless user discovery supports these use cases.

**•** Headless login with any identifier and a password. For example, a user goes to your headless app and enters their order number and
password to log in.

**•** Headless login with any identifier and a one-time password (OTP). For example, a user goes to your app and enters just their order
number. Your Apex handler finds the user's account based on the order number. Salesforce sends an OTP to the verified email
address that's associated with the account. To log in, the user enters the OTP.

**•** Headless password reset with any identifier. For example a user goes to your app and enters their phone number. Your Apex handler
finds the user account and Salesforce sends an OTP to the user's verified phone number. To verify their identity for password reset,
the user enters the OTP and can then set a new password.

Headless user discovery is supported for Headless Identity API flows and OAuth 2.0 for First-Party Applications flows. For more information
[about supported flows and implementation details, see Headless Login Without a Username.](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_headless_discovery.htm&type=5&language=en_US)

IN THIS SECTION:

#### HeadlessUserDiscoveryHandler Methods

HeadlessUserDiscoveryHandler Example Implementation

#### HeadlessUserDiscoveryHandler Methods

### The following are methods for HeadlessUserDiscoveryHandler .

IN THIS SECTION:

discoverUserFromLoginHint(networkId, loginHint, verificationAction, customDataJson, requestAttributes)
Finds a user's Salesforce account based on user information, such as their email address, phone number, or other data, that's passed
to a Salesforce endpoint during headless login, passwordless login, and forgot password flows.


Apex Reference Guide HeadlessUserDiscoveryHandler Interface

##### **`discoverUserFromLoginHint(networkId, loginHint, verificationAction,`**

```
  customDataJson, requestAttributes)

```

Finds a user's Salesforce account based on user information, such as their email address, phone number, or other data, that's passed to
a Salesforce endpoint during headless login, passwordless login, and forgot password flows.

Signature

```
   public Auth.HeadlessUserDiscoveryResponse discoverUserFromLoginHint(Id networkId, String

   loginHint, Auth.VerificationAction verificationAction, String customDataJson,

   Map<String,String> requestAttributes)

```

Parameters

```
   networkId
```

Type: Id

The ID of the Experience Cloud site where your headless app sends requests.

```
   loginHint
```

Type: String

Information about the user that Salesforce can use to find their associated account, such as their email address or phone number.

```
   verificationAction
```

Type: Auth.VerificationAction on page 213

The verification method that's used to log the user in, either email or SMS.

```
   customDataJson
```

Type: String

Custom user data, such as first name, that you collect when the user logs in to your headless app.

```
   requestAtttibutes
```

[Type: Map<String,String>](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_map.htm#apex_methods_system_map)

Information about the login request that's based on the user’s browser state when accessing the login page. `requestAttributes`
passes in the CommunityUrl, IpAddress, UserAgent, Platform, Application, City, Country, and Subdivision values. The City, Country,
and Subdivision values come from IP geolocation.

Return Value

Type: Auth.HeadlessUserDiscoveryResponse on page 133

If the handler finds a user, it returns a user ID. If not, it returns an error message.

#### HeadlessUserDiscoveryHandler Example Implementation

Here's an example implementation of the `Auth.HeadlessUserDiscoveryHandler` interface. This example supports login
with email and login with SMS.

##### The discoverUserFromLoginHint method uses custom logic to search for a user account with a verified email address or

phone number that matches the data passed in the login hint. As a security best practice, Salesforce always recommends writing code
to determine if the user's email address or phone number is verified.

For users logging in with email, the custom logic first checks whether the email address passed in the login hint is in a valid format. Then,
[to look for a verified Salesforce email address that matches the email address passed in the login hint, it queries the TwoFactorMethodsInfo](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_twofactormethodsinfo.htm)


Apex Reference Guide HeadlessUserDiscoveryHandler Interface

object. If successful, it returns an instance of `Auth.HeadlessUserDiscoveryResponse` with the user ID. If something goes
wrong, it returns an instance of `Auth.HeadlessUserDiscoveryResponse` with a custom error message. In this example, it
returns error messages when the email address format isn't valid, the email address isn't verified, there's no user with that email address,
or there are multiple users with that email address.

For users logging in with SMS, the custom logic is similar. It checks whether the phone number passed in the login hint is in a valid
format. Then, it looks for a verified Salesforce phone number that matches the phone number passed in the login hint. If successful, it
returns an instance of `Auth.HeadlessUserDiscoveryResponse` with the user ID, and if not, it returns custom error messages.

```
   /*

    * Headless User Discovery Handler

    */

   global class MyHeadlessUserDiscoveryHandler implements Auth.HeadlessUserDiscoveryHandler

   {

     /*

    * This method handles the logic to determine the user account based on the loginHint and

    verificationMethod

     */

    global Auth.HeadlessUserDiscoveryResponse discoverUserFromLoginHint(Id networkId, String

    loginHint,

     Auth.VerificationAction verificationAction, String customDataJson,

   Map<String,String>requestAttributes) {

      if (verificationAction == Auth.VerificationAction.EMAIL) {

       return doLookupByVerifiedEmail(loginHint, verificationAction);

      } else if (verificationAction == Auth.VerificationAction.SMS) {

       return doLookupByVerifiedMobile(loginHint, verificationAction);

      } else {

       return new Auth.HeadlessUserDiscoveryResponse(null, 'Unsupported

   Auth.VerificationAction');

      }

     }

     private Auth.HeadlessUserDiscoveryResponse doLookupByVerifiedEmail(String loginHint,

   Auth.VerificationAction verificationAction) {

      if (String.isBlank(loginHint) || !isValidEmail(loginHint)) {

      return new Auth.HeadlessUserDiscoveryResponse(null, 'Invalid email sent as loginHint:

    ' + loginHint);

      }

      // Search for an user account by email

      List<User> users = [SELECT Id FROM User WHERE Email = :loginHint AND IsActive = TRUE];

      if (!users.isEmpty() && users.size() == 1) {

       Id userId = users[0].Id;

       // Check if the user has a verified email

       List<TwoFactorMethodsInfo> verifiedInfo = [SELECT HasUserVerifiedEmailAddress FROM

   TwoFactorMethodsInfo WHERE UserId = :userId];

       if (!verifiedInfo.isEmpty() && verifiedInfo[0].HasUserVerifiedEmailAddress == true)

    {

        // Prepare and return HeadlessUserDiscoveryResponse with userId

        return new Auth.HeadlessUserDiscoveryResponse(new Set<Id>{userId}, null);

       } else {

        // Return HeadlessUserDiscoveryResponse with error message

        return new Auth.HeadlessUserDiscoveryResponse(null, 'Email ' + loginHint + ' not

```


Apex Reference Guide HeadlessUserDiscoveryHandler Interface

```
   verified for the given user account');

       }

      } else {

       if (users.isEmpty()) {

        return new Auth.HeadlessUserDiscoveryResponse(null, 'No user identified for the

   email: ' + loginHint);

       } else {

        return new Auth.HeadlessUserDiscoveryResponse(null, 'Multiple users identified for

    the email: ' + loginHint);

       }

      }

     }

     private Auth.HeadlessUserDiscoveryResponse doLookupByVerifiedMobile(String loginHint,

   Auth.VerificationAction verificationAction) {

      String formattedSms = !String.isBlank(loginHint) ? getFormattedSms(loginHint) : null;

      if (String.isBlank(formattedSms)) {

       return new Auth.HeadlessUserDiscoveryResponse(null, 'Invalid phone number sent as

   loginHint: ' + loginHint);

      }

      // Search for an user account by phone

      List<User> users = [SELECT Id FROM User WHERE MobilePhone = :loginHint AND IsActive =

    TRUE];

      if (!users.isEmpty() && users.size() == 1) {

       Id userId = users[0].Id;

       // Check if the user has a verified phone

       List<TwoFactorMethodsInfo> verifiedInfo = [SELECT HasUserVerifiedMobileNumber FROM

   TwoFactorMethodsInfo WHERE UserId = :userId];

       if (!verifiedInfo.isEmpty() && verifiedInfo[0].HasUserVerifiedMobileNumber == true)

    {

        // Prepare and return HeadlessUserDiscoveryResponse with userId

        return new Auth.HeadlessUserDiscoveryResponse(new Set<Id>{userId}, null);

       } else {

        // Return HeadlessUserDiscoveryResponse with error message

        return new Auth.HeadlessUserDiscoveryResponse(null, ' ' + loginHint + ' not verified

    for the given user account');

       }

      } else {

       if (users.isEmpty()) {

        return new Auth.HeadlessUserDiscoveryResponse(null, 'No user identified for the

   phone number: ' + loginHint);

       } else {

        return new Auth.HeadlessUserDiscoveryResponse(null, 'Multiple users identified for

    the phone number: ' + loginHint);

       }

      }

     }

     private boolean isValidEmail(String identifier) {

      String emailRegex =

   '^[a-zA-Z0-9._|\\\\%#~`=?&/$^*!}{+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$';

      // source: http://www.regular-expressions.info/email.html

      Pattern EmailPattern = Pattern.compile(emailRegex);

```


### Apex Reference Guide HeadlessUserDiscoveryResponse Class

```
      Matcher EmailMatcher = EmailPattern.matcher(identifier);

      if (EmailMatcher.matches()) { return true; }

      else { return false; }

     }

     private String getFormattedSms(String identifier) {

      // Accept SMS input formats with 1 or 2 digits country code, 3 digits area code and 7

    digits number

      // You can customize the SMS regex to allow different formats

     String smsRegex = '^(\\+?\\d{1,2}?[\\s-])?(\\(?\\d{3}\\)?[\\s-]?\\d{3}[\\s-]?\\d{4})$';

      Pattern smsPattern = Pattern.compile(smsRegex);

      Matcher smsMatcher = SmsPattern.matcher(identifier);

      if (smsMatcher.matches()) {

       try {

        // Format user input into the verified SMS format '+xx xxxxxxxxxx' before DB lookup

        // Append US country code +1 by default if no country code is provided

        String countryCode = smsMatcher.group(1) == null ? '+1' : smsMatcher.group(1);

        return System.UserManagement.formatPhoneNumber(countryCode, smsMatcher.group(2));

       } catch(System.InvalidParameterValueException e) {

        return null;

       }

      } else { return null; }

     }

### HeadlessUserDiscoveryResponse Class

```

Contains methods to describe the result of headless user discovery using a handler that implements the
`Auth.HeadlessUserDiscoveryHandler` interface during headless login, passwordless login, and forgot password flows.

Namespace

Auth

Usage

Use this class to return a user ID if headless user discovery was successful, or return custom error messages if not.

IN THIS SECTION:

#### HeadlessUserDiscoveryResponse Constructors

HeadlessUserDiscoveryResponse Properties

#### HeadlessUserDiscoveryResponse Constructors

### The following are constructors for HeadlessUserDiscoveryResponse .


Apex Reference Guide HeadlessUserDiscoveryResponse Class

IN THIS SECTION:

##### HeadlessUserDiscoveryResponse(userIds, customErrorMessage)

Creates an instance of the `Auth.HeadlessUserDiscoveryResponse` class to describe the result of headless user discovery
based on data passed into the `login_hint` during headless login, passwordless login, and forgot password flows.

##### **`HeadlessUserDiscoveryResponse(userIds, customErrorMessage)`**

Creates an instance of the `Auth.HeadlessUserDiscoveryResponse` class to describe the result of headless user discovery
based on data passed into the `login_hint` during headless login, passwordless login, and forgot password flows.

Signature

```
   public HeadlessUserDiscoveryResponse(Set<Id> userIds, String customErrorMessage)

```

Parameters

```
   userIds
```

[Type: Set<Id>](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_set.htm)

The user ID that's associated with the data passed in the `login_hint` parameter. If there are multiple users associated with the
data, it can return multiple IDs, but headless user discovery fails.

##### _`customErrorMessage`_

Type: String

A custom error message that's returned if headless user discovery fails.

#### HeadlessUserDiscoveryResponse Properties

##### The following are properties for HeadlessUserDiscoveryResponse .

IN THIS SECTION:

##### customErrorMessage

A custom error message that's returned if headless user discovery fails. For example, write custom logic in your headless user discovery
handler to see if the user's email address is verified. Then return a custom error message for when it isn't verified.

userIds
The user ID for the external user that's associated with the data passed into the `login_hint` parameter. If there are multiple
users associated with the data, it can return multiple IDs, but headless user discovery fails.

##### **`customErrorMessage`**

A custom error message that's returned if headless user discovery fails. For example, write custom logic in your headless user discovery
handler to see if the user's email address is verified. Then return a custom error message for when it isn't verified.

Signature

```
   public String customErrorMessage {get; set;}

```


### Apex Reference Guide HttpCalloutMockUtil Class

Property Value

Type: String

##### **`userIds`**

The user ID for the external user that's associated with the data passed into the `login_hint` parameter. If there are multiple users
associated with the data, it can return multiple IDs, but headless user discovery fails.

Signature

```
   public Set<Id> userIds {get; set;}

```

Property Value

[Type: Set<Id>](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_set.htm)

### HttpCalloutMockUtil Class

Contains a method to send fake HTTP callouts for classes in the `Auth` namespace.

Namespace

Auth

Usage

Use the `setHttpMock` method in this class to test HTTP callouts when implementing the `Auth.JWTBearerTokenExchange`
and `Auth.JWTUtil` classes.

For the `Auth.JWTBearerTokenExchange` class, mock callouts to the OAuth token endpoint when using the
`JWTBearerTokenExchange` method.

For the `Auth.JWTUtil` class, mock callouts to the identity provider’s JSON Web Key Set (JWKS) endpoint when using the
`validateJWTWithKeysEndpoint` method.

[For more information on mocking HTTP callouts, see Testing HTTP Callouts by Implementing the HttpCalloutMock Interface.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_restful_http_testing_httpcalloutmock.htm)

IN THIS SECTION:

#### HttpCalloutMockUtil Methods HttpCalloutMockUtil Methods

### The following are methods for HttpCalloutMockUtil .

IN THIS SECTION:

setHttpMock(mock)
Mocks an HTTP callout using an implementation of the `System.HttpCalloutMock` interface.


### Apex Reference Guide IntegratingAppType Enum

##### **`setHttpMock(mock)`**

Mocks an HTTP callout using an implementation of the `System.HttpCalloutMock` interface.

Signature

```
   public static void setHttpMock(System.HttpCalloutMock mock)

```

Parameters

```
   mock
```

[Type: System.HttpCalloutMock](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_httpcalloutmock.htm)

[A class that implements the System.HttpCalloutMock interface to return a fake HTTP response for a given request to the OAuth token](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_httpcalloutmock.htm)
endpoint or a JWKS endpoint on an external identity provider, depending on your use case.

Return Value

Type: void

### IntegratingAppType Enum

Specifies whether you’re integrating your app as a connected app or as an external client app in methods used in your customized Apex
token exchange handler, which extends the `Auth.Oauth2TokenExchangeHandler` class.

Usage

[See Token Exchange Handler Validation and Subject Mapping.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/token_exchange_handler.htm)

Enum Values

The following are the values of the `Auth.IntegratingAppType` enum.

**Value** **Description**

`CA` Indicates a Salesforce connected app.

`ECA` Indicates a Salesforce external client app.

### InvocationContext Enum

The context in which the connected app is invoked, such as the protocol flow used and the token type issued, if any. Developers can
use the context information to write code that is unique to the type of invocation.

Enum Values

The following are the values of the `Auth.InvocationContext` enum.


### Apex Reference Guide JsonValueOutput Class

**Value** **Description**

`ASSET_TOKEN` Reserved for future use.

`OAUTH1` Context used when authentication is through an OAuth 1.0A flow.

`OAUTH2_JWT_BEARER_TOKEN` Context used when authentication is through a JSON-based Web Token (JWT)
bearer token flow.

`OAUTH2_SAML_ASSERTION` Context used when authentication is through an OAuth 2.0 SAML assertion flow.

`OAUTH2_SAML_BEARER_ASSERTION` Context used when authentication is through an OAuth 2.0 SAML bearer assertion
flow.

`OAUTH2_USERNAME_PASSWORD` Context used when authentication is through an OAuth 2.0 username-password
flow.

`OAUTH2_USER_AGENT_ID_TOKEN` Context used when issuing an ID token through an OAuth 2.0 user-agent flow.

`OAUTH2_USER_AGENT_TOKEN` Context used when authentication is through an OAuth 2.0 user agent flow.

`OAUTH2_WEB_SERVER` Context used when authentication is through a web server authentication flow.

`OPENIDCONNECT` Context used when authentication is through an OpenID Connect authentication
flow.

`REFRESH_TOKEN` Context used when renewing tokens issued by a web server or user-agent flow.

`SAML_ASSERTION` Context used when authentication is through a SAML assertion flow.

`UNKNOWN` Context is unknown.

`USERID_ENDPOINT` Context used when issuing an access token through a UserInfo endpoint.

SEE ALSO:

[Salesforce Help: Authenticating Apps with OAuth](https://help.salesforce.com/apex/HTViewHelpDoc?id=remoteaccess_authenticate.htm&language=en_US)

### JsonValueOutput Class

Stores the output of the Get User Data from JSON String invocable action, which you can access in Flow Builder..

Namespace

Auth

Usage

To implement single sign-on (SSO) with the authentication provider framework, you must set up a registration handler that creates and
updates users who log in via the identity provider. To create and update users, the registration handler uses user information from the
identity provider. Some identity providers return user information in an ID token or in a user info response. The ID token and user info
response are formatted as JSON objects that can be deeply nested, which makes them difficult to parse. If you use Flow Builder for your
registration handler, the Get User Data from JSON String invocable action makes it easier to get user information from these JSON objects.
Use this action to retrieve a specific attribute value from the ID token or user info response.


Apex Reference Guide JsonValueOutput Class

The action takes two input values. The first input value is the ID token or user info response from the identity provider. This input value
must be a JSON object that has been serialized into a string. The second input value is the JSON key that corresponds to the attribute
value that you want to retrieve. Using these input values, the action parses the ID token or user info response. It outputs the attribute
value and stores it in an instance of the `Auth.JsonValueOutput` class. Each instance of this class stores a single attribute. The
attribute is stored in a property that corresponds to its data type in the identity provider response, such as `integerValue` for an
integer.

For more information about this action and how you can use it, see these resources in Salesforce Help.

**•** [Flow Core Action: Get User Data from JSON String](http://platform.flow_ref_elements_actions_generate_user_data.htm)

**•** [Example: Authentication Provider Registration Handler Flow](https://help.salesforce.com/s/articleView?id=xcloud.sso_flow_registration_handler_example.htm&language=en_US)

IN THIS SECTION:

#### JsonValueOutput Constructors

JsonValueOutput Properties

#### JsonValueOutput Constructors The following are constructors for JsonValueOutput .

IN THIS SECTION:

##### JsonValueOutput(stringValue, booleanValue, integerValue, doubleValue, jsonStringValue, jsonArrayValue)

The Get User Data from JSON String action in Flow Builder uses this constructor to create an instance of the
`Auth.JsonValueOutput` class.

##### **`JsonValueOutput(stringValue, booleanValue, integerValue, doubleValue,`**

```
  jsonStringValue, jsonArrayValue)

```

The Get User Data from JSON String action in Flow Builder uses this constructor to create an instance of the `Auth.JsonValueOutput`
class.

Signature

```
   public JsonValueOutput(String stringValue, Boolean booleanValue, Integer integerValue,

   Double doubleValue, String jsonStringValue, String jsonArrayValue)

```

Parameters

```
   stringValue
```

Type: String

If the attribute returned by the action is a string, it's stored in this parameter.

```
   booleanValue
```

Type: Boolean

If the attribute returned by the action is a boolean value, it's stored in this parameter.

```
   integerValue
```

Type: Integer


Apex Reference Guide JsonValueOutput Class

If the attribute returned by the action is an integer value, it's stored in this parameter.

##### _`doubleValue`_

Type: Double

If the attribute returned by the action is a Double value, it's stored in this parameter.

```
   jsonStringValue
```

Type: String

If the attribute returned by the action is a JSON string, it's stored in this parameter.

```
   jsonArrayValue
```

Type: String

If the attribute returned by the action is a JSON array, it's formatted as a string and stored in this parameter.

#### JsonValueOutput Properties The following are properties for JsonValueOutput .

IN THIS SECTION:

##### booleanValue

If the attribute returned by the action is a boolean value, it's stored in this property.

##### doubleValue

If the attribute returned by the action is a Double value, it's stored in this property.

integerValue
If the attribute returned by the action is an integer, it's stored in this property.

jsonArrayValue
If the attribute returned by the action is a JSON array, it's formatted as a string and stored in this property.

jsonStringValue
If the attribute returned by the action is a JSON string, it's stored in this property.

stringValue
If the attribute returned by the action is a string, it's stored in this property.

##### **`booleanValue`**

If the attribute returned by the action is a boolean value, it's stored in this property.

Signature

```
   public Boolean booleanValue {get; set;}

```

Property Value

Type: Boolean

##### **`doubleValue`**

If the attribute returned by the action is a Double value, it's stored in this property.


Apex Reference Guide JsonValueOutput Class

Signature

```
   public Double doubleValue {get; set;}

```

Property Value

Type: Double

##### **`integerValue`**

If the attribute returned by the action is an integer, it's stored in this property.

Signature

```
   public Integer integerValue {get; set;}

```

Property Value

Type: Integer

##### **`jsonArrayValue`**

If the attribute returned by the action is a JSON array, it's formatted as a string and stored in this property.

Signature

```
   public String jsonArrayValue {get; set;}

```

Property Value

Type: String

##### **`jsonStringValue`**

If the attribute returned by the action is a JSON string, it's stored in this property.

Signature

```
   public String jsonStringValue {get; set;}

```

Property Value

Type: String

##### **`stringValue`**

If the attribute returned by the action is a string, it's stored in this property.

Signature

```
   public String stringValue {get; set;}

```


### Apex Reference Guide JWS Class

Property Value

Type: String

### JWS Class

Contains methods that apply a digital signature to a JSON Web Token (JWT), using a JSON Web Signature (JWS) data structure. This class
creates the signed JWT bearer token, which can be used to request an OAuth access token in the OAuth 2.0 JWT bearer token flow.

Namespace

Auth

Usage

Use the methods in this class to sign the JWT bearer token with the X509 certificate.

IN THIS SECTION:

#### JWS Constructors

JWS Methods

#### JWS Constructors

### The following are constructors for JWS .

IN THIS SECTION:

##### JWS(jwt, certDevName)
### Creates an instance of the JWS class using the specified Auth.JWT payload and the certificate used for signing the JWT bearer

token.

JWS(payload, certDevName)
### Creates an instance of the JWS class using the specified payload and certificate used for signing the JWT bearer token.

##### JWS(jwt, certDevName)

### Creates an instance of the JWS class using the specified Auth.JWT payload and the certificate used for signing the JWT bearer token.

Signature

```
   public JWS(Auth.JWT jwt, String certDevName)

```

Parameters

```
   jwt
```

Type: Auth.JWT

The Base64-encoded JSON Claims Set in the JWT bearer token generated by `Auth.JWT` .


Apex Reference Guide JWS Class

```
   certDevName
```

Type: String

The `Unique Name` for a certificate stored in the Salesforce org’s Certificate and Key Management page to use for signing the
JWT bearer token.

Usage

Calls the `toJSONString()` method in `Auth.JWT` and sets the resulting string as the payload of the JWT bearer token. Alternatively,
##### you can specify the payload directly using JWS(payload, certDevName) . JWS(payload, certDevName) Creates an instance of the JWS class using the specified payload and certificate used for signing the JWT bearer token.

Signature

```
   public JWS(String payload, String certDevName)

```

Parameters

```
   payload
```

Type: String

The Base64-encoded JSON Claims Set in the JWT bearer token.

```
   certDevName
```

Type: String

The `Unique Name` for a certificate stored in the Salesforce org’s Certificate and Key Management page to use for signing the
JWT bearer token.

Usage

Sets the _`payload`_ string as the payload of the JWT bearer token. Alternatively, if you generate the payload using `Auth.JWT`, you
can use `JWS(jwt, certDevName)` instead.

#### JWS Methods

##### The following are methods for JWS . All are instance methods.

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the JWS object.

getCompactSerialization()
Returns the compact serialization representation of the JWS as a concatenated string, with the encoded JWS header, encoded JWS
payload, and encoded JWS signature strings separated by period ('.') characters.

##### clone()

Makes a duplicate copy of the JWS object.


### Apex Reference Guide JWT Class

Signature

```
   public Object clone()

```

Return Value

Type: JWS

##### getCompactSerialization()

Returns the compact serialization representation of the JWS as a concatenated string, with the encoded JWS header, encoded JWS
payload, and encoded JWS signature strings separated by period ('.') characters.

Signature

```
   public String getCompactSerialization()

```

Return Value

Type: String

### JWT Class

Generates the JSON Claims Set in a JSON Web Token (JWT). The resulting Base64-encoded payload can be passed as an argument to
create an instance of the `Auth.JWS` class.

Namespace

Auth

Usage

Use the methods in this class to generate the payload in a JWT bearer token for the OAuth 2.0 JWT bearer token flow. For more information
[and a full code sample, see JWTBearerTokenExchange Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_JWTBearerTokenExchange.htm)

IN THIS SECTION:

#### JWT Methods JWT Methods

### The following are methods for JWT . All are instance methods.

IN THIS SECTION:

clone()
Makes a duplicate copy of the JWT object.

getAdditionalClaims()
Returns a map of additional claims in the JWT, where the key string contains the name of the claim, and the value contains the value
of the claim.


Apex Reference Guide JWT Class

getAud()
Returns the audience ( `aud` ) claim that identifies the intended recipients of the JWT.

getIss()
Returns the issuer ( `iss` ) claim that identifies the issuer of the JWT.

getNbfClockSkew()
Returns the not before ( `nbf` ) claim that identifies the time before which the JWT must not be accepted for processing, while allowing
some leeway for clock skew. This method returns a `NoAccess` exception for JWTs generated using methods in the
`Auth.JWTUtil` class. To return the `nbf` claim for these JWTs, use the `getAdditionalClaims` method instead.

getSub()
Returns the subject ( `sub` ) claim that identifies the current user of the JWT.

getValidityLength()
Returns the length of time (in seconds) that the JWT is valid, which affects the expiration ( `exp` ) claim. This method returns a
`NoAccess` exception for JWTs generated using methods in the `Auth.JWTUtil` class. To return the validity length for these
JWTs, use the `getAdditionalClaims` method instead.

setAdditionalClaims(additionalClaims)
Sets the additional claims in the JWT. Returned by the `getAdditionalClaims` method.

setAud(aud)
Sets the audience ( `aud` ) claim in the JWT. Returned by the `getAud` method.

setIss(iss)
Sets the issuer ( `iss` ) claim in the JWT. Returned by the `getIss` method.

setNbfClockSkew(nbfClockSkew)
Sets the not before ( `nbf` ) claim in the JWT. Returned by the `getNbfClockSkew` method. This method returns a `NoAccess`
exception for JWTs generated using methods in the `Auth.JWTUtil` class. For these JWTs, the incoming JWT determines the
`nbf` claim.

setSub(sub)
Sets the subject ( `sub` ) claim in the JWT. Returned by the `getSub` method.

setValidityLength(validityLength)
Sets the length of time (in seconds) that the JWT is valid, which affects the expiration ( `exp` ) claim. Returned by the
`getValidityLength` method. This method returns a `NoAccess` exception for JWTs generated using methods in the
`Auth.JWTUtil` class. For these JWTs, the incoming JWT determines the validity length.

toJSONString()
Generates the JSON object representation of the Claims Set as an encoded JWT payload.

##### clone()

Makes a duplicate copy of the JWT object.

Signature

```
   public Object clone()

```

Return Value

Type: JWT


Apex Reference Guide JWT Class

##### getAdditionalClaims()

Returns a map of additional claims in the JWT, where the key string contains the name of the claim, and the value contains the value of
the claim.

Signature

```
   public Map<String,Object> getAdditionalClaims()

```

Return Value

Type: Map<String,Object>

The claims returned depend on how the JWT was generated.

If the JWT was generated using other methods in the `Auth.JWT` class, this method returns the claims that were set using the
`setAdditionalClaims` method.

##### For JWTs generated using methods in the Auth.JWTUtil class, the getAdditionalClaims method returns all claims except

for these three.

##### • aud (audience)—Use the getAud method instead. • iss (issuer)—Use the getIss method instead.

**•** `sub` (subject)—Use the `getSub` method instead.

For these JWTs, when the incoming JWT has a claim that stores an inner JSON list, the claim value is returned as a string.

##### getAud()

Returns the audience ( `aud` ) claim that identifies the intended recipients of the JWT.

Signature

```
   public String getAud()

```

Return Value

Type: String

##### getIss()

Returns the issuer ( `iss` ) claim that identifies the issuer of the JWT.

Signature

```
   public String getIss()

```

Return Value

Type: String


Apex Reference Guide JWT Class

##### getNbfClockSkew()

Returns the not before ( `nbf` ) claim that identifies the time before which the JWT must not be accepted for processing, while allowing
some leeway for clock skew. This method returns a `NoAccess` exception for JWTs generated using methods in the `Auth.JWTUtil`
class. To return the `nbf` claim for these JWTs, use the `getAdditionalClaims` method instead.

Signature

```
   public Integer getNbfClockSkew()

```

Return Value

Type: Integer

##### getSub()

Returns the subject ( `sub` ) claim that identifies the current user of the JWT.

Signature

```
   public String getSub()

```

Return Value

Type: String

##### getValidityLength()

Returns the length of time (in seconds) that the JWT is valid, which affects the expiration ( `exp` ) claim. This method returns a `NoAccess`
exception for JWTs generated using methods in the `Auth.JWTUtil` class. To return the validity length for these JWTs, use the
`getAdditionalClaims` method instead.

Signature

```
   public Integer getValidityLength()

```

Return Value

Type: Integer

##### setAdditionalClaims(additionalClaims)

Sets the additional claims in the JWT. Returned by the `getAdditionalClaims` method.

Signature

```
   public void setAdditionalClaims(Map<String,Object> additionalClaims)

```


Apex Reference Guide JWT Class

Parameters

```
   additionalClaims
```

Type: Map<String,Object>

Return Value

Type: void

Usage

Additional claims must not include any standard claims.

##### setAud(aud)

Sets the audience ( `aud` ) claim in the JWT. Returned by the `getAud` method.

Signature

```
   public void setAud(String aud)

```

Parameters

```
   aud
```

Type: String

Return Value

Type: void

##### setIss(iss)

Sets the issuer ( `iss` ) claim in the JWT. Returned by the `getIss` method.

Signature

```
   public void setIss(String iss)

```

Parameters

```
   iss
```

Type: String

Return Value

Type: void


Apex Reference Guide JWT Class

##### setNbfClockSkew(nbfClockSkew)

Sets the not before ( `nbf` ) claim in the JWT. Returned by the `getNbfClockSkew` method. This method returns a `NoAccess`
exception for JWTs generated using methods in the `Auth.JWTUtil` class. For these JWTs, the incoming JWT determines the `nbf`
claim.

Signature

```
   public void setNbfClockSkew(Integer nbfClockSkew)

```

Parameters

```
   nbfClockSkew
```

Type: Integer

Return Value

Type: void

##### setSub(sub)

Sets the subject ( `sub` ) claim in the JWT. Returned by the `getSub` method.

Signature

```
   public void setSub(String sub)

```

Parameters

```
   sub
```

Type: String

Return Value

Type: void

##### setValidityLength(validityLength)

Sets the length of time (in seconds) that the JWT is valid, which affects the expiration ( `exp` ) claim. Returned by the
`getValidityLength` method. This method returns a `NoAccess` exception for JWTs generated using methods in the
`Auth.JWTUtil` class. For these JWTs, the incoming JWT determines the validity length.

Signature

```
   public void setValidityLength(Integer validityLength)

```

Parameters

```
   validityLength
```

Type: Integer


### Apex Reference Guide JWTBearerTokenExchange Class

Return Value

Type: void

##### toJSONString()

Generates the JSON object representation of the Claims Set as an encoded JWT payload.

Signature

```
   public String toJSONString()

```

Return Value

Type: String

### JWTBearerTokenExchange Class

Contains methods that POST the signed JWT bearer token to a token endpoint to request an access token, in the OAuth 2.0 JWT bearer
token flow.

Namespace

Auth

Usage

Use the methods in this class to post a signed JWT bearer token to the OAuth token endpoint, in exchange for an access token.

To test HTTP callouts to the token endpoint, use the `Auth.HttpCalloutMockUtil` class.

Example

In the following example application, the Apex controller:

**1.** Creates the JSON Claims Set.

**2.** Specifies the scope of the request with additional claims.

**3.** Creates the signed JWT.

**4.** Specifies the token endpoint and POSTs to it.

**5.** Gets the access token from the HTTP response.

```
   public class MyController{

      public MyController() {

        Auth.JWT jwt = new Auth.JWT();

        jwt.setSub('user@salesforce.com');

        jwt.setAud('https://login.salesforce.com');

        jwt.setIss('3MVG99OxTyEMCQ3gNp2PjkqeZKxnmAiG1xV4oHh9AKL_rSK.BoSVPGZHQ

   ukXnVjzRgSuQqGn75NL7yfkQcyy7');

```


Apex Reference Guide JWTBearerTokenExchange Class

```
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

IN THIS SECTION:

#### JWTBearerTokenExchange Constructors

JWTBearerTokenExchange Methods

#### JWTBearerTokenExchange Constructors The following are constructors for JWTBearerTokenExchange .

IN THIS SECTION:

##### JWTBearerTokenExchange(tokenEndpoint, jws)
#### Creates an instance of the JWTBearerTokenExchange class using the specified token endpoint and the signed JWT bearer

token.

JWTBearerTokenExchange()
Creates an instance of the `Auth.JWTBearerTokenExchange` class.

##### JWTBearerTokenExchange(tokenEndpoint, jws)

#### Creates an instance of the JWTBearerTokenExchange class using the specified token endpoint and the signed JWT bearer token.

Signature

```
   public JWTBearerTokenExchange(String tokenEndpoint, Auth.JWS jws)

```


Apex Reference Guide JWTBearerTokenExchange Class

Parameters

```
   tokenEndpoint
```

Type: String

The token endpoint that the signed JWT bearer token is POSTed to.

```
   jws
```

Type: Auth.JWS

The signed JWT bearer token.

##### JWTBearerTokenExchange()

Creates an instance of the `Auth.JWTBearerTokenExchange` class.

Signature

```
   public JWTBearerTokenExchange()

#### JWTBearerTokenExchange Methods

##### The following are methods for JWTBearerTokenExchange . All are instance methods.

```

IN THIS SECTION:

clone()
Makes a duplicate copy of the JWTBearerTokenExchange object.

getAccessToken()
Returns the `access_token` in the token response to the JWT bearer token request.

getGrantType()
Returns the grant type specified in the JWT bearer token request. The grant type value defaults to
`urn:ietf:params:oauth:grant-type:jwt-bearer` .

getHttpResponse()
Returns the full `System.HttpResponse` token response to the JWT bearer token request.

getJWS()
Returns the JWS specified in the JWT bearer token request.

getTokenEndpoint()
Returns the token endpoint that the JWT bearer token request is POSTed to.

setGrantType(grantType)
Sets the grant type in the JWT bearer token request. Returned by the `getGrantType()` method.

setJWS(jws)
Sets the JWS in the JWT bearer token request. Returned by the `getJWS()` method.

setTokenEndpoint(tokenEndpoint)
Sets the token endpoint that the JWT bearer token request is POSTed to. Returned by the `getTokenEndpoint()` method.


Apex Reference Guide JWTBearerTokenExchange Class

##### clone()

Makes a duplicate copy of the JWTBearerTokenExchange object.

Signature

```
   public Object clone()

```

Return Value

Type: JWTBearerTokenExchange

##### getAccessToken()

Returns the `access_token` in the token response to the JWT bearer token request.

Signature

```
   public String getAccessToken()

```

Return Value

Type: String

Usage

This method extracts the `access_token` from the token response. If the token response issues the access token in a different
parameter, the request fails.

##### If you want the full HTTP token response returned, use getHttpResponse instead. getGrantType()

Returns the grant type specified in the JWT bearer token request. The grant type value defaults to
`urn:ietf:params:oauth:grant-type:jwt-bearer` .

Signature

```
   public String getGrantType()

```

Return Value

Type: String

##### getHttpResponse()

Returns the full `System.HttpResponse` token response to the JWT bearer token request.

Signature

```
   public System.HttpResponse getHttpResponse()

```


Apex Reference Guide JWTBearerTokenExchange Class

Return Value

Type: System.HttpResponse

Usage

You can get the access token from the full `System.HttpResponse` . If you want only the `access_token` from the token
response, you can use `getAccessToken` instead.

##### getJWS()

Returns the JWS specified in the JWT bearer token request.

Signature

```
   public Auth.JWS getJWS()

```

Return Value

Type: Auth.JWS

##### getTokenEndpoint()

Returns the token endpoint that the JWT bearer token request is POSTed to.

Signature

```
   public String getTokenEndpoint()

```

Return Value

Type: String

##### setGrantType(grantType)

Sets the grant type in the JWT bearer token request. Returned by the `getGrantType()` method.

Signature

```
   public void setGrantType(String grantType)

```

Parameters

```
   grantType
```

Type: String

Return Value

Type: void


### Apex Reference Guide JWTUtil Class

##### setJWS(jws)

Sets the JWS in the JWT bearer token request. Returned by the `getJWS()` method.

Signature

```
   public void setJWS(Auth.JWS jws)

```

Parameters

```
   jws
```

Type: Auth.JWS

Return Value

Type: void

##### setTokenEndpoint(tokenEndpoint)

Sets the token endpoint that the JWT bearer token request is POSTed to. Returned by the `getTokenEndpoint()` method.

Signature

```
   public void setTokenEndpoint(String tokenEndpoint)

```

Parameters

```
   tokenEndpoint
```

Type: String

Return Value

Type: void

### JWTUtil Class

Contains methods for validating a JSON Web Token (JWT) from an external identity provider as part of the OAuth 2.0 token exchange
flow. Use these methods as part of the `validateIncomingToken` method in the `Auth.Oauth2TokenExchangeHandler`
class.

Namespace

Auth

Usage

[See Token Exchange Handler Validation and Subject Mapping.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/token_exchange_handler.htm)

If the methods in this class fail, Salesforce returns an `Auth.JWTValidationException` exception.


Apex Reference Guide JWTUtil Class

IN THIS SECTION:

#### JWTUtil Methods JWTUtil Methods The following are methods for JWTUtil .

IN THIS SECTION:

##### parseJWTFromStringWithoutValidation(incomingJWT)

Parses a JWT from an encoded string into a header, payload, and signature. Use this method to decode the JWT without validating
it.

##### validateJWTWithCert(incomingJWT, certDeveloperName)

Parses and validates the JWT using a certificate saved in Salesforce. The certificate can be self-signed or signed by a certificate
authority.

validateJWTWithKey(incomingJWT, publicKey)
Parses and validates the JWT using a public key from the external identity provider.

validateJWTWithKeysEndpoint(incomingJWT, keysEndpoint, shouldUseCache)
Parses and validates the JWT using a remote JSON Web Key Set (JWKS) endpoint on your external identity provider.

##### **`parseJWTFromStringWithoutValidation(incomingJWT)`**

Parses a JWT from an encoded string into a header, payload, and signature. Use this method to decode the JWT without validating it.

Signature

```
   public static Auth.JWT parseJWTFromStringWithoutValidation(String incomingJWT)

```

Parameters

```
   incomingJWT
```

Type: String

The JWT from your identity provider.

Return Value

[Type:Auth.JWT](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_JWT.htm)

##### **`validateJWTWithCert(incomingJWT, certDeveloperName)`**

Parses and validates the JWT using a certificate saved in Salesforce. The certificate can be self-signed or signed by a certificate authority.

Signature

```
   public static Auth.JWT validateJWTWithCert(String incomingJWT, String certDeveloperName)

```


Apex Reference Guide JWTUtil Class

Parameters

```
   incomingJWT
```

Type: String

The JWT from your identity provider.

```
   certDeveloperName
```

Type: String

A certificate saved in the Certificate and Key Management page in Setup.

Return Value

[Type: Auth.JWT](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_JWT.htm)

##### **`validateJWTWithKey(incomingJWT, publicKey)`**

Parses and validates the JWT using a public key from the external identity provider.

Signature

```
   public static Auth.JWT validateJWTWithKey(String incomingJWT, String publicKey)

```

Parameters

```
   incomingJWT
```

Type: String

The JWT from your identity provider.

```
   publicKey
```

Type: String

The public key from your identity provider.

Return Value

[Type: Auth.JWT](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_JWT.htm)

##### **`validateJWTWithKeysEndpoint(incomingJWT, keysEndpoint, shouldUseCache)`**

Parses and validates the JWT using a remote JSON Web Key Set (JWKS) endpoint on your external identity provider.

Signature

```
   public static Auth.JWT validateJWTWithKeysEndpoint(String incomingJWT, String

   keysEndpoint, Boolean shouldUseCache)

```

Parameters

```
   incomingJWT
```

Type: String

The JWT from your identity provider.


### Apex Reference Guide LightningLoginEligibility Enum

```
   keysEndpoint
```

Type: String

A URL pointing to a valid JSON Web Key Set (JWKS) endpoint on your identity provider. The JWKS returned by the endpoint must
[conform to the specification defined in RFC 7517: JSON Web Key (JWK).](https://datatracker.ietf.org/doc/html/rfc7517)

To test HTTP callouts to the JWKS endpoint, use the `Auth.HttpCalloutMockUtil` class.

```
   shouldUseCache
```

Type: Boolean

Indicates whether the cache is overwritten with the JWKS after validation. If `false`, the cache is overwritten with the JWKS after
each successful JWT validation. If `true`, the JWKS is cached only if there is no existing JWKS in the cache; if there is a cached JWKS,
it isn't overwritten.

Return Value

[Type: Auth.JWT](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_JWT.htm)

### LightningLoginEligibility Enum

Contains a Lightning Login eligibility value used by the `Auth.SessionManagement.getLightningLoginEligibility`
method.

Usage

If you use the Discovery page type, users can verify themselves with Lightning Login. Lightning Login lets internal users log in with
Salesforce Authenticator instead of a password. Certain conditions must be met for Lightning Login to succeed.

Call `Auth.SessionManagement.getLightningLoginEligibility` before or after a login attempt to get the eligibility
status. You can call after a login attempt to determine why the login attempt failed.

Enum Values

The following are the values of the `Auth.LightningLoginEligibility` enum.

**Value** **Description**

`ELIGIBLE` All eligibility conditions are met. The admin has enabled Salesforce Authenticator
and Lightning Login, assigned the user Lightning Login user permission, and selected

**Allow only for users with the Lightning Login User permission** from the Session
Settings Setup page. The user has set up Salesforce Authenticator and enrolled in
Lightning Login.

`ORG_AUTHENTICATOR_NOT_ENABLED` The admin hasn’t enabled Salesforce Authenticator.

`ORG_PREF_NOT_ENABLED` The admin hasn’t enabled Lightning Login. The Admin must select **Allow Lightning**
**Login** from the Session Settings Setup page.

`USER_AUTHENTICATOR_NOT_CONNECTED` The user hasn’t set up Salesforce Authenticator.

`USER_NOT_ALLOWED` The admin hasn’t granted the user AllowLightningLogin user permission. Allowing
Lightning Login to certain users requires the OnlyLLPermUserAllowed org preference.


### Apex Reference Guide LoginDiscoveryHandler Interface

**Value** **Description**

Admins must select **Allow only for users with the Lightning Login User**
**permission** from the Session Settings Setup page.

`USER_NOT_ENROLLED` The user hasn’t enrolled in Lightning Login.

`USER_PERM_NOT_ENABLED` The admin hasn’t granted the user the Lightning Login Eligible user permission.

### LoginDiscoveryHandler Interface

Salesforce gives you the ability to log in users based on other verification methods than username and password. For example, it can
prompt users to log in with their email, phone number, or another identifier like a Federation ID or device identifier. Login Discovery is
available to these licenses: Customer Community, Customer Community Plus, External Identity, Partner Community, and Partner
Community Plus.

Namespace

Auth

Usage

Implement a `Auth.LoginDiscoveryHandler` for an interview-based log in. The handler looks up a user from the identifier
entered, and can call `Site.passwordlessLogin` to determine which credential to use, such as email or SMS. Or the handler can
redirect a user to a third-party identity provider for login. With this handler, the login page doesn't show a password field. However, you
can use `Site.passwordlessLogin` to then prompt for a password.

From the user perspective, the user enters an identifier at the log in prompt. Then the user completes the login by entering a PIN or
password. Or, if SSO-enabled, the user bypasses login.

[For an example, see LoginDiscoveryHandler Example Implementation. For more details, see Salesforce Customer Identity in](https://help.salesforce.com/articleView?id=identity_about_customers_partners.htm&language=en_US) _Salesforce_
_Help_ .

IN THIS SECTION:

#### LoginDiscoveryHandler Method

LoginDiscoveryHandler Example Implementation

#### LoginDiscoveryHandler Method

### Here’s the method for LoginDiscoveryHandler .

IN THIS SECTION:

login(identifier, startUrl, requestAttributes)
Log in the customer or partner given the specified identifier, such as email or phone number. If successful, redirect the user to the
Experience Cloud site page specified by the start URL.


Apex Reference Guide LoginDiscoveryHandler Interface

##### login(identifier, startUrl, requestAttributes)

Log in the customer or partner given the specified identifier, such as email or phone number. If successful, redirect the user to the
Experience Cloud site page specified by the start URL.

Signature

```
   public System.PageReference login(String identifier, String startUrl,

   Map<String,String>requestAttributes)

```

Parameters

```
   identifier
```

Type: String

Identifier the customer or partner entered at the login prompt, for example, an email address or phone number.

```
   startUrl
```

Type: String

Path to the Experience Cloud site page requested by the customer or partner. The user is redirected to this location after successful
login.

```
   requestAttributes
```

Type: Map<String,String>

Information about the login request based on the user’s browser state when accessing the login page. `requestAttributes`
passes in the CommunityUrl, IpAddress, UserAgent, Platform, Application, City, Country, and Subdivision values. The City, Country,
and Subdivision values come from IP geolocation.

Return Value

Type: System.PageReference

The URL of the page where the user is redirected.

Example

Here’s a sample `requestAttributes` response.

```
   CommunityUrl=http://my-developer-edition.mycompany.com:5555/discover

   IpAddress=55.555.0.0

   UserAgent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML,

   like Gecko) Version/11.1 Safari/605.1.15

   Platform=Mac OSX

   Application=Browser

   City=San Mateo

   Country=United States

   Subdivision=California

#### LoginDiscoveryHandler Example Implementation

```

This Apex code example implements the `Auth.LoginDiscoveryHandler` interface. It checks whether the user who is logging
in has a verified email or phone number, depending on which identifier was supplied on the login page. If verified, with
`Auth.VerificationMethod.EMAIL` or `Auth.VerificationMethod.SMS`, we send a challenge to the identifier, either


Apex Reference Guide LoginDiscoveryHandler Interface

the user’s email address or mobile device. If the user enters the code correctly on the verify page, the user is redirected to the Experience
Cloud site’s page specified by the start URL. If the user isn’t verified, the user must enter a password to log in. The handler also checks
that the email and phone number are unique with this code: `users.size()==1` .

Note: Passwordless login works only with verified methods. You can check the verification status on the User object, for example,
with User list view, a report, or the API. Make sure that your solution handles the case where the user doesn’t have a verification
method. This code example falls back to a password.

The default discoverable login handler checks whether the user entered a valid email address or phone number before redirecting
the user to the verification page. If an invalid entry is made, the handler returns an error. Because this behavior is vulnerable to
user enumeration attack, make sure that your solution prevents this attack. For example, you can create a dummy page similar to
the verification page and redirect the user to the dummy page when invalid user identifier is entered. Also, use generic error
messages to avoid providing additional information.

The `discoveryResult` function calls the `Site.passwordlessLogin` method to log the user in with the specified verification
method. The `getSsoRedirect` function looks up whether the user logs in with SAML or an Auth Provider. Add the
implementation-specific logic to handle the lookup.

```
   global class AutocreatedDiscLoginHandler1535377170343 implements Auth.LoginDiscoveryHandler

    {

   global PageReference login(String identifier, String startUrl, Map<String, String>

   requestAttributes) {

      if (identifier != null && isValidEmail(identifier)) {

        // Search for user by email.

        List<User> users = [SELECT Id FROM User WHERE Email = :identifier AND IsActive =

   TRUE];

        if (!users.isEmpty() && users.size() == 1) {

           // User must have a verified email before using this verification method.

           // We cannot send messages to unverified emails.

           // You can check if the user's email verified bit set and add the

           // password verification method as fallback.

          List<TwoFactorMethodsInfo> verifiedInfo = [SELECT HasUserVerifiedEmailAddress

    FROM TwoFactorMethodsInfo WHERE UserId = :users[0].Id];

          if (!verifiedInfo.isEmpty() && verifiedInfo[0].HasUserVerifiedEmailAddress ==

    true) {

             // Use email verification method if the user's email is verified.

             return discoveryResult(users[0], Auth.VerificationMethod.EMAIL, startUrl,

    requestAttributes);

           } else {

             // Use password verification method as fallback

             // if the user's email is unverified.

            return discoveryResult(users[0], Auth.VerificationMethod.PASSWORD, startUrl,

    requestAttributes);

           }

        } else {

          throw new Auth.LoginDiscoveryException('No unique user found. User count=' +

   users.size());

        }

      }

      if (identifier != null) {

        String formattedSms = getFormattedSms(identifier);

        if (formattedSms != null) {

           // Search for user by SMS.

          List<User> users = [SELECT Id FROM User WHERE MobilePhone = :formattedSms AND

```


Apex Reference Guide LoginDiscoveryHandler Interface

```
    IsActive = TRUE];

           if (!users.isEmpty() && users.size() == 1) {

             // User must have a verified SMS before using this verification method.

             // We cannot send messages to unverified mobile numbers.

             // You can check if the user's mobile verified bit is set or add

             // the password verification method as fallback.

            List<TwoFactorMethodsInfo> verifiedInfo = [SELECT HasUserVerifiedMobileNumber

    FROM TwoFactorMethodsInfo WHERE UserId = :users[0].Id];

            if (!verifiedInfo.isEmpty() && verifiedInfo[0].HasUserVerifiedMobileNumber

    == true) {

               // Use SMS verification method if the user's mobile number is verified.

              return discoveryResult(users[0], Auth.VerificationMethod.SMS, startUrl,

    requestAttributes);

             } else {

               // Use password verification method as fallback if the user's

               // mobile number is unverified.

               return discoveryResult(users[0], Auth.VerificationMethod.PASSWORD,

   startUrl, requestAttributes);

             }

           } else {

            throw new Auth.LoginDiscoveryException('No unique user found. User count='

    + users.size());

           }

        }

      }

      if (identifier != null) {

        // You can customize the code to find user via other attributes,

        // such as SSN or Federation ID.

      }

      throw new Auth.LoginDiscoveryException('Invalid Identifier');

   }

   private boolean isValidEmail(String identifier) {

      String emailRegex =

   '^[a-zA-Z0-9._|\\\\%#~`=?&/$^*!}{+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$';

      // source: https://www.regular-expressions.info/email.html

      Pattern EmailPattern = Pattern.compile(emailRegex);

      Matcher EmailMatcher = EmailPattern.matcher(identifier);

      if (EmailMatcher.matches()) { return true; }

      else { return false; }

   }

   private String getFormattedSms(String identifier) {

      // Accept SMS input formats with 1- or 2-digit country code,

      // 3-digit area code, and 7-digit number.

      // You can customize the SMS regex to allow different formats.

     String smsRegex = '^(\\+?\\d{1,2}?[\\s-])?(\\(?\\d{3}\\)?[\\s-]?\\d{3}[\\s-]?\\d{4})$';

      Pattern smsPattern = Pattern.compile(smsRegex);

      Matcher smsMatcher = SmsPattern.matcher(identifier);

      if (smsMatcher.matches()) {

        try {

           // Format user input into the verified SMS format '+xx xxxxxxxxxx'

           // before DB lookup. If no country code is provided, append

           // US country code +1 for the default.

```


Apex Reference Guide LoginDiscoveryHandler Interface

```
          String countryCode = smsMatcher.group(1) == null ? '+1' : smsMatcher.group(1);

         return System.UserManagement.formatPhoneNumber(countryCode, smsMatcher.group(2));

        } catch(System.InvalidParameterValueException e) {

           return null;

        }

      } else { return null; }

   }

   private PageReference getSsoRedirect(User user, String startUrl, Map<String, String>

   requestAttributes) {

      // You can look up to check whether the user should log in with

      // SAML or an Auth Provider and return the URL to initialize SSO.

      return null;

   }

   private PageReference discoveryResult(User user, Auth.VerificationMethod method, String

   startUrl, Map<String, String> requestAttributes) {

      // Only users with an External Identity or community license can log in

      // using Site.passwordlessLogin. Use getSsoRedirect to let your org employees

      // log in to an Experience Cloud site.

      PageReference ssoRedirect = getSsoRedirect(user, startUrl, requestAttributes);

      if (ssoRedirect != null) {

        return ssoRedirect;

      } else {

        if (method != null) {

           List<Auth.VerificationMethod> methods = new List<Auth.VerificationMethod>();

           methods.add(method);

           PageReference pwdlessRedirect = Site.passwordlessLogin(user.Id, methods,

   startUrl);

           if (pwdlessRedirect != null) {

             return pwdlessRedirect;

           } else {

            throw new Auth.LoginDiscoveryException('No Passwordless Login redirect URL

    returned for verification method: ' + method);

           }

        } else {

           throw new Auth.LoginDiscoveryException('No method found');

        }

      }

   }

   }

```

Code Example: Filter Login Discovery Users by Profile

Your production org can have multiple users with the same verified email address and mobile number. But your customers must have
unique ones. To address this problem, you can add a few lines of code that filters users by profile to ensure uniqueness. This code example
handles users with the External Identity User profile, but can be adapted to support other use cases. For example, you can modify the
first line of code to address users with other user licenses or criteria.

Login Discovery is available with the following user licenses: Customer Community, Customer Community Plus, External Identity, Partner
Community, and Partner Community Plus. It depends on which profiles have access to your Experience Cloud site.

```
   global class AutocreatedDiscLoginHandler1551301979709 implements Auth.LoginDiscoveryHandler

    {

```


Apex Reference Guide LoginDiscoveryHandler Interface

```
   global PageReference login(String identifier, String startUrl, Map<String, String>

   requestAttributes) {

      if (identifier != null && isValidEmail(identifier)) {

        // Ensure uniqueness by profile

        Profile p = [SELECT id FROM profile WHERE name = 'External Identity User'];

        List<User> users = [SELECT Id FROM User WHERE Email = :identifier AND IsActive =

   TRUE AND profileId=:p.id];

        if (!users.isEmpty() && users.size() == 1) {

           // User must have verified email before using this verification method. We

   cannot send messages to unverified emails.

           // You can check if the user has email verified bit on and add the password

   verification method as fallback.

          List<TwoFactorMethodsInfo> verifiedInfo = [SELECT HasUserVerifiedEmailAddress

    FROM TwoFactorMethodsInfo WHERE UserId = :users[0].Id];

          if (!verifiedInfo.isEmpty() && verifiedInfo[0].HasUserVerifiedEmailAddress ==

    true) {

             // Use email verification method if the user's email is verified.

             return discoveryResult(users[0], Auth.VerificationMethod.EMAIL, startUrl,

    requestAttributes);

           } else {

             // Use password verification method as fallback if the user's email is

   unverified.

            return discoveryResult(users[0], Auth.VerificationMethod.PASSWORD, startUrl,

    requestAttributes);

           }

        } else {

          throw new Auth.LoginDiscoveryException('No unique user found. User count=' +

   users.size());

        }

      }

      if (identifier != null) {

        String formattedSms = getFormattedSms(identifier);

        if (formattedSms != null) {

           // Ensure uniqueness by profile

           Profile p = [SELECT id FROM profile WHERE name = 'External Identity User'];

          List<User> users = [SELECT Id FROM User WHERE MobilePhone = :formattedSms AND

    IsActive = TRUE AND profileId=:p.id];

           if (!users.isEmpty() && users.size() == 1) {

             // User must have verified SMS before using this verification method. We

   cannot send messages to unverified mobile numbers.

            // You can check if the user has mobile verified bit on or add the password

    verification method as fallback.

            List<TwoFactorMethodsInfo> verifiedInfo = [SELECT HasUserVerifiedMobileNumber

    FROM TwoFactorMethodsInfo WHERE UserId = :users[0].Id];

            if (!verifiedInfo.isEmpty() && verifiedInfo[0].HasUserVerifiedMobileNumber

    == true) {

               // Use SMS verification method if the user's mobile number is verified.

              return discoveryResult(users[0], Auth.VerificationMethod.SMS, startUrl,

    requestAttributes);

             } else {

               // Use password verification method as fallback if the user's mobile

   number is unverified.

```


Apex Reference Guide LoginDiscoveryHandler Interface

```
               return discoveryResult(users[0], Auth.VerificationMethod.PASSWORD,

   startUrl, requestAttributes);

             }

           } else {

            throw new Auth.LoginDiscoveryException('No unique user found. User count='

    + users.size());

           }

        }

      }

      if (identifier != null) {

        // You can customize the code to find user via other attributes, such as SSN or

   Federation ID

      }

      throw new Auth.LoginDiscoveryException('Invalid Identifier');

   }

   private boolean isValidEmail(String identifier) {

      String emailRegex =

   '^[a-zA-Z0-9._|\\\\%#~`=?&/$^*!}{+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$';

      // source: https://www.regular-expressions.info/email.html

      Pattern EmailPattern = Pattern.compile(emailRegex);

      Matcher EmailMatcher = EmailPattern.matcher(identifier);

      if (EmailMatcher.matches()) { return true; }

      else { return false; }

   }

   private String getFormattedSms(String identifier) {

      // Accept SMS input formats with 1 or 2 digits country code, 3 digits area code and 7

    digits number

      // You can customize the SMS regex to allow different formats

     String smsRegex = '^(\\+?\\d{1,2}?[\\s-])?(\\(?\\d{3}\\)?[\\s-]?\\d{3}[\\s-]?\\d{4})$';

      Pattern smsPattern = Pattern.compile(smsRegex);

      Matcher smsMatcher = SmsPattern.matcher(identifier);

      if (smsMatcher.matches()) {

        try {

           // Format user input into the verified SMS format '+xx xxxxxxxxxx' before DB

   lookup

           // Append US country code +1 by default if no country code is provided

          String countryCode = smsMatcher.group(1) == null ? '+1' : smsMatcher.group(1);

         return System.UserManagement.formatPhoneNumber(countryCode, smsMatcher.group(2));

        } catch(System.InvalidParameterValueException e) {

           return null;

        }

      } else { return null; }

   }

   private PageReference getSsoRedirect(User user, String startUrl, Map<String, String>

   requestAttributes) {

      // You can look up if the user should log in with SAML or an Auth Provider and return

    the URL to initialize SSO.

      return null;

```


### Apex Reference Guide LoginDiscoveryMethod Enum

```
   }

   private PageReference discoveryResult(User user, Auth.VerificationMethod method, String

   startUrl, Map<String, String> requestAttributes) {

      //Only users with an External Identity or community license can login using

   Site.passwordlessLogin

      //Use getSsoRedirect to enable your org employees to log in to an Experience Cloud

   site

      PageReference ssoRedirect = getSsoRedirect(user, startUrl, requestAttributes);

      if (ssoRedirect != null) {

        return ssoRedirect;

      } else {

        if (method != null) {

           List<Auth.VerificationMethod> methods = new List<Auth.VerificationMethod>();

           methods.add(method);

           PageReference pwdlessRedirect = Site.passwordlessLogin(user.Id, methods,

   startUrl);

           if (pwdlessRedirect != null) {

             return pwdlessRedirect;

           } else {

            throw new Auth.LoginDiscoveryException('No Passwordless Login redirect URL

    returned for verification method: ' + method);

           }

        } else {

           throw new Auth.LoginDiscoveryException('No method found');

        }

      }

   }

   }

### LoginDiscoveryMethod Enum

```

Contains methods used to verify the user’s identity when the My Domain login process uses Login Discovery.

Usage

Specifies the verification method used to authenticate internal users when My Domain is set up for Login Discovery.

Enum Values

`Auth.LoginDiscoveryMethod` enum has the following values.

**Value** **Description**

`LIGHTNING_LOGIN` Verify identity by Lightning Login, which lets internal users log in with Salesforce
Authenticator.

`PASSWORD` Verify identity by entering a password.


### Apex Reference Guide MyDomainLoginDiscoveryHandler Interface MyDomainLoginDiscoveryHandler Interface

The handler used to implement the My Domain Login Discovery page, which is an interview-based (two-step) login process. First the
user is prompted for a unique identifier such as an email address or phone number. Then the handler determines (discovers) how to
authenticate the user. Either the user enters a password or is directed to an identity provider’s login page.

Namespace

Auth

Usage

### Implement MyDomainLoginDiscoveryHandler to let My Domain users log in with something other than their username and

password. This handler contains the logic to look up the user based on the identifier value entered on the login page. The
`Auth.MyDomainLoginDiscoveryHandler.login` method is invoked when the identifier page is submitted and finds the
user that corresponds to the submitted identifier. The `Auth.SessionManagement.finishLoginDiscovery` method
sends the user to the authentication mechanism and then logs in the user.

Register the handler from the My Domain Setup page. Under Authentication Configuration, select the **Discovery** Login Page Type. For
Login Discovery Handler, select this handler from the list of Apex classes.

For an example, see MyDomainLoginDiscoveryHandler Example Implementation. For more details, search for My Domain Login Discovery
in _Salesforce Help_ .

IN THIS SECTION:

#### MyDomainLoginDiscoveryHandler Method

MyDomainLoginDiscoveryHandler Example Implementation

#### MyDomainLoginDiscoveryHandler Method

### MyDomainLoginDiscoveryHandler has the following method.

IN THIS SECTION:

##### login(identifier, startUrl, requestAttributes)

Log in a Salesforce user given the specified identifier, such as email or phone number. If successful, redirect the user to the page
specified by the start URL.

##### login(identifier, startUrl, requestAttributes)

Log in a Salesforce user given the specified identifier, such as email or phone number. If successful, redirect the user to the page specified
by the start URL.

Signature

```
   public System.PageReference login(String identifier, String startUrl, Map<String,String>

   requestAttributes)

```


Apex Reference Guide MyDomainLoginDiscoveryHandler Interface

Parameters

```
   identifier
```

Type: String

Identifier the Salesforce user entered at the login prompt, for example, an email address or phone number.

```
   startUrl
```

Type: String

The page users see after successfully logging in to the My Domain subdomain.

```
   requestAttributes
```

Type: Map <String, String>

Information about the login request based on the user’s browser state when accessing the login page. `requestAttributes`
passes in the MyDomainUrl, IpAddress, UserAgent, Platform, Application, City, Country, and Subdivision values. The City, Country,
and Subdivision values come from IP address geolocation.

Return Value

Type: System.PageReference

The URL of the page where the user is redirected to complete authentication.

Example

Here’s a sample `requestAttributes` response.

```
   CommunityUrl=http://my-dev-ed.my.salesforce.com:5555/discover

   IpAddress=55.255.0.0

   UserAgent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML,

   like Gecko) Version/11.1 Safari/605.1.15

   Platform=Mac OSX

   Application=Browser

   City=San Mateo

   Country=United States

   Subdivision=California

#### MyDomainLoginDiscoveryHandler Example Implementation

```

Here's an example of the `Auth.MyDomainLoginDiscoveryHandler` interface. This sample class contains the default logic
for My Domain login discovery using password authentication. You can customize the code to ensure it meets your needs. The
requestAttributes parameter provides additional information that you can use in the discovery logic. Attributes include MyDomainUrl,
IpAddress, UserAgent, and location information (such as Country and City). Use `Auth.DiscoveryCustomErrorException`
to throw custom errors to display on the login page.

To implement this interface, the My Domain login page type must be set to Discovery.

```
   // This sample class contains the default logic for My Domain login discovery by password.

   // You can customize the code to ensure it meets your needs. The requestAttributes parameter

   // provides additional information you can use in the discovery logic. Attributes include MyDomainUrl,

   // IpAddress, UserAgent, and location information (such as Country and City).

   // Use Auth.DiscoveryCustomErrorException to throw custom errors which will be shown on login page.

    global class MyDomainDiscLoginDefaultHandler implements Auth.MyDomainLoginDiscoveryHandler {

    global PageReference login(String identifier, String startUrl, Map<String, String> requestAttributes)

   {

```


Apex Reference Guide MyDomainLoginDiscoveryHandler Interface

```
     if (identifier != null) {

        // Search for user by email

       List<User> users = [SELECT Id FROM User WHERE Email = :identifier AND IsActive = TRUE];

        if (!users.isEmpty() && users.size() == 1) {

           return discoveryResult(users[0], startUrl, requestAttributes);

        } else {

         throw new Auth.LoginDiscoveryException('No unique user found. User count=' + users.size());

        }

      }

      throw new Auth.LoginDiscoveryException('Invalid Identifier');

     }

   private PageReference getSsoRedirect(User user, String startUrl, Map<String, String> requestAttributes) {

     // You can look up if the user should log in with SAML or an Auth Provider and return the URL to initialize SSO. For example:

     // SamlSsoConfig SSO = [select Id from SamlSsoConfig where DeveloperName='SamlTest' limit 1];

      // To get the URL for a My Domain subdomain, you can pass null in the communityURL

   parameter.

      // String ssoUrl = Auth.AuthConfiguration.getSamlSsoUrl(null, startUrl, SSO.Id);

      // return new PageReference(ssoUrl);

      return null;

     }

   private PageReference discoveryResult(User user, String startUrl, Map<String, String> requestAttributes)

      {

      PageReference ssoRedirect = getSsoRedirect(user, startUrl, requestAttributes);

       if (ssoRedirect != null) {

        return ssoRedirect;

       }

       else {

       return Auth.SessionManagement.finishLoginDiscovery(Auth.LoginDiscoveryMethod.password, user.Id);

       }

     }

   }

```

Test Class for MyDomainDiscLoginDefaultHandler Class

The following is the test class for MyDomainDiscoveryLoginHandler. For the test to work, your org must have the My Domain login page
type set to Discovery.

```
   // Test class for MyDomainDiscLoginDefaultHandler

   @isTest

   class MyDomainDiscLoginDefaultHandlerTest {

      /* Test Discoverable handler login.

        Create a user with specific email identifier and invoke login.

        Expected : User should be discovered and pagereference should be returned.

      */

      @isTest static void testLogin() {

        // Create user

        String identifierEmail = getUniqueName() + '@test.org';

        createTestUser(identifierEmail);

        Map<String, String> requestAttributes = new Map<String, String>();

        String startUrl = '';

```


Apex Reference Guide MyDomainLoginDiscoveryHandler Interface

```
       MyDomainDiscLoginDefaultHandler myDomainDiscLoginDefaultHandler = new MyDomainDiscLoginDefaultHandler();

        // Invoke login method from handler with the email of user created

      PageReference pageReference = myDomainDiscLoginDefaultHandler.login(identifierEmail, startUrl, requestAttributes);

        // Asser page reference is returned

        System.assertNotEquals(null, pageReference, 'Page reference was not returned');

      }

      /* Test Discoverable handler login with invalid (non-existing) user.

        Expected : Auth.LoginDiscoveryException

      */

      @isTest static void testLoginWithInvalidUser() {

        try {

           Map<String, String> requestAttributes = new Map<String, String>();

           String startUrl = '';

           String uniqueName = getUniqueName();

           String email = uniqueName + '@test.org';

        MyDomainDiscLoginDefaultHandler myDomainDiscLoginDefaultHandler = new MyDomainDiscLoginDefaultHandler();

           // Invoke login method from handler with non-existing user

           myDomainDiscLoginDefaultHandler.login(email, startUrl, requestAttributes);

        }catch (Auth.LoginDiscoveryException loginDiscoveryException) {

           // Assert exception message

       System.assert(loginDiscoveryException.getMessage().contains('Nouniqueuserfound'),'message='+loginDiscoveryException.getMessage());

        }

      }

      /*

        Generate a random name

      */

      private static String getUniqueName() {

        String orgId = UserInfo.getOrganizationId();

       String dateString = String.valueof(Datetime.now()).replace(' ','').replace(':','').replace('-','');

        Integer randomInt = Integer.valueOf(math.rint(math.random()*1000000));

        String uniqueName = orgId + dateString + randomInt;

        return uniqueName;

      }

      /*

       Create user with given email.

      */

      private static void createTestUser(String identifierEmail)

      {

        String uniqueName = getUniqueName();

        Profile pf = [SELECT Id FROM Profile WHERE Name='Standard User'];

        String profileID = pf.Id;

        String fName = 'fname';

        String lName = uniqueName + '-lname';

        User tuser = new User( firstname = fName,

                       lastName = lName,

                       email = identifierEmail,

                       Username = uniqueName + '@test.org',

                       EmailEncodingKey = 'ISO-8859-1',

                       Alias = uniqueName.substring(18, 23),

                       TimeZoneSidKey = 'America/Los_Angeles',

                       LocaleSidKey = 'en_US',

                       LanguageLocaleKey = 'en_US',

                       ProfileId = profileID);

        insert tuser;

```


### Apex Reference Guide Oauth2TokenExchangeHandler Class

```
      }

   }

### Oauth2TokenExchangeHandler Class

```

Use this class to create a token exchange handler that validates tokens from an external identity provider and maps the token’s subject
to a Salesforce user during the OAuth 2.0 token exchange flow. The handler can also be used to create users by setting up a new User
object and returning it to Salesforce for automatic insertion.

Namespace

Auth

Usage

[See Token Exchange Handler Validation and Subject Mapping.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/token_exchange_handler.htm)

IN THIS SECTION:

#### Oauth2TokenExchangeHandler Methods Oauth2TokenExchangeHandler Methods

### The following are methods for Oauth2TokenExchangeHandler .

IN THIS SECTION:

##### getUserForTokenSubject(networkId, result, canCreateUser, appDeveloperName, appType)

Finds the subject defined in the external identity provider’s token so that it can be mapped to a Salesforce subject.

validateIncomingToken(appDeveloperName, appType, incomingToken, tokenType)
Validates an access token, refresh token, ID token, SAML 2.0 assertion, or JWT passed from an external identity provider during the
OAuth 2.0 token exchange flow.

##### **`getUserForTokenSubject(networkId, result, canCreateUser, appDeveloperName,`**

```
  appType)

```

Finds the subject defined in the external identity provider’s token so that it can be mapped to a Salesforce subject.

Signature

```
   public User getUserForTokenSubject(Id networkId, Auth.TokenValidationResult result,

   Boolean canCreateUser, String appDeveloperName, Auth.IntegratingAppType appType)

```

Parameters

```
   networkId
```

Type: Id

The identifier for the Salesforce user, if one exists.


Apex Reference Guide Oauth2TokenExchangeHandler Class

```
   result
```

[Type: Auth.TokenValidationResult](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_TokenValidationResult.htm)

##### The result of the token validation performed by the validateIncomingToken method in the

[Auth.Oauth2TokenExchangeHandler class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_Oauth2TokenExchangeHandler.htm)

```
   canCreateUser
```

Type: Boolean

Specifies whether the handler can set up a User object if no user exists. Salesforce automatically inserts the user into this object.

```
   appDeveloperName
```

Type: String

The developer name of the Salesforce connected app or external client app that’s being used to integrate your app with Salesforce.

```
   appType
```

[Type: Auth.IntegratingAppType](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_Auth_IntegratingAppType.htm)

Specifies whether your app is integrated with Salesforce as a connected app or as an external client app.

Return Value

[Type: User](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_user.htm)

Returns a User object with the user information obtained from the token, from Salesforce, and from callouts to the identity provider, if
applicable. The User object can be an existing user record or a new user that hasn’t been inserted in the database. If it’s a new user,
Salesforce automatically inserts the user on behalf of the token exchange handler.

##### **`validateIncomingToken(appDeveloperName, appType, incomingToken, tokenType)`**

Validates an access token, refresh token, ID token, SAML 2.0 assertion, or JWT passed from an external identity provider during the OAuth
2.0 token exchange flow.

Signature

```
   public Auth.TokenValidationResult validateIncomingToken(String appDeveloperName,

   Auth.IntegratingAppType appType, String incomingToken, Auth.OAuth2TokenExchangeType

   tokenType)

```

Parameters

```
   appDeveloperName
```

Type: String

The developer name of the Salesforce connected app or external client app that’s being used to integrate your app with Salesforce.

```
   appType
```

[Type: Auth.IntegratingAppType](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_Auth_IntegratingAppType.htm)

Specifies whether your app is integrated with Salesforce as a connected app or as an external client app.

```
   incomingToken
```

Type: String

The token from the external identity provider.

```
   tokenType
```

[Type: Auth.OAuth2TokenExchangeType](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)


### Apex Reference Guide OAuth2TokenExchangeType Enum

The type of token from the external identity provider. It can be an access token, a refresh token, an ID token, a SAML 2.0 assertion,
or any token that’s formatted as a JSON Web Token (JWT).

Return Value

[Type: Auth.TokenValidationResult](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_TokenValidationResult.htm)

Returns information about whether the token is valid, data extracted from the token, the token itself, and the token type. It can also
return a custom error message if the validation failed.

### OAuth2TokenExchangeType Enum

Used during the OAuth 2.0 token exchange flow to specify the type of token that’s being exchanged for a Salesforce token.

Usage

During the token exchange flow, your app requests a token from Salesforce by sending a POST request with a token from an external
identity provider. The request includes a `subject_token_type` parameter to specify the type of token. The values specified in
this enum must correspond to the `subject_token_type` in the token request.

Enum Values

The following are the values of the `Auth.OAuth2TokenExchangeType` enum.

**Value** **Description**

```
ACCESS_TOKEN

ID_TOKEN

JWT

REFRESH_TOKEN

SAML_2

### OAuthRefreshResult Class

```

An access token from the identity provider. The corresponding
`subject_token_type` is
`urn:ietf:params:oauth:token-type:access_token` .

An ID token from the identity provider. The corresponding
`subject_token_type` is
`urn:ietf:params:oauth:token-type:id_token` .

A token from the identity provider that’s formatted as a JSON Web Token (JWT).
The corresponding `subject_token_type` is
`urn:ietf:params:oauth:token-type:JWT` .

A refresh token from the identity provider. The corresponding
`subject_token_type` is
`urn:ietf:params:oauth:token-type:refresh_token` .

A SAML 2.0 assertion from the identity provider. The corresponding
`subject_token_type` is
`urn:ietf:params:oauth:token-type:saml2` .

Stores the result of an `AuthProviderPluginClass` refresh method. OAuth authentication flow provides a refresh token that
can be used to get a new access token. Access tokens have a limited lifetime as specified by the session timeout value. When an access
token expires, use a refresh token to get a new access token.


Apex Reference Guide OAuthRefreshResult Class

Namespace

Auth

Usage

#### The OAuthRefreshResult class contains the parameters, accessToken, refreshToken, and error, all of which are of

type `string` . For a code example, see .

IN THIS SECTION:

#### OAuthRefreshResult Constructors

OAuthRefreshResult Properties

#### OAuthRefreshResult Constructors The following are constructors for OAuthRefreshResult .

IN THIS SECTION:

##### OAuthRefreshResult(accessToken, refreshToken, error)
#### Creates an instance of the OAuthRefreshResult class using the specified access token, refresh token, and error for a custom

authentication provider plug-in.

OAuthRefreshResult(accessToken, refreshToken)
#### Creates an instance of the OAuthRefreshResult class using the specified access token and refresh token for a custom

authentication provider plug-in. Use this method when you know that the refresh was successful.

##### OAuthRefreshResult(accessToken, refreshToken, error)

#### Creates an instance of the OAuthRefreshResult class using the specified access token, refresh token, and error for a custom

authentication provider plug-in.

Signature

```
   public OAuthRefreshResult(String accessToken, String refreshToken, String error)

```

Parameters

```
   accessToken
```

Type: String

OAuth access token for the user who is currently logged in.

```
   refreshToken
```

Type: String

OAuth refresh token for the user who is currently logged in.

```
   error
```

Type: String

Error that occurred when a user attempted to authenticate with the custom authentication provider.


Apex Reference Guide OAuthRefreshResult Class

##### OAuthRefreshResult(accessToken, refreshToken) Creates an instance of the OAuthRefreshResult class using the specified access token and refresh token for a custom authentication

provider plug-in. Use this method when you know that the refresh was successful.

Signature

```
   public OAuthRefreshResult(String accessToken, String refreshToken)

```

Parameters

##### _`accessToken`_

Type: String

The OAuth access token for the user who is logged in.

```
   refreshToken
```

Type: String

The OAuth refresh token for the user who is logged in.

#### OAuthRefreshResult Properties

##### The following are properties for OAuthRefreshResult .

IN THIS SECTION:

##### accessToken

The OAuth access token for the user who is currently logged in.

##### error

Error that occurs when a user unsuccessfully attempts to authenticate with the custom authentication provider.

refreshToken
The OAuth refresh token for the user who is currently logged in.

##### accessToken

The OAuth access token for the user who is currently logged in.

Signature

```
   public String accessToken {get; set;}

```

Property Value

Type: String

##### error

Error that occurs when a user unsuccessfully attempts to authenticate with the custom authentication provider.


### Apex Reference Guide OauthToken Class

Signature

```
   public String error {get; set;}

```

Property Value

Type: String

##### refreshToken

The OAuth refresh token for the user who is currently logged in.

Signature

```
   public String refreshToken {get; set;}

```

Property Value

Type: String

### OauthToken Class

Contains a method to revoke OAuth access tokens and refresh tokens. This method supports opaque tokens and JSON Web Token
(JWT)-based access tokens, including guest and named user JWT-based access tokens.

Namespace

Auth

Usage

When a client completes an authorization flow and is authorized to access Salesforce data, they’re issued an access token, which the
client can use to make authenticated requests for protected Salesforce resources. The client can also use refresh tokens to get more
access tokens. If you don’t want the client to access Salesforce data anymore, revoke its Salesforce tokens.

This class is distinct from the `[Auth.AuthToken](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_AuthToken.htm)` class, which contains a method to revoke tokens issued by a third-party provider
instead of Salesforce tokens.

IN THIS SECTION:

#### OauthToken Methods OauthToken Methods

### The following are methods for OauthToken .

IN THIS SECTION:

revokeToken(type, authToken)
Revokes Salesforce-issued OAuth tokens.


### Apex Reference Guide OauthTokenType Enum

##### **`revokeToken(type, authToken)`**

Revokes Salesforce-issued OAuth tokens.

Signature

```
   public static Boolean revokeToken(Auth.OauthTokenType type, String authToken)

```

Parameters

```
   type
```

[Type: Auth.OauthTokenType](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_OauthToken.htm)

Specifies the type of token to be revoked. To revoke an opaque access token, use the `ACCESS_TOKEN` value. To revoke a refresh
token and any associated access tokens, use the `REFRESH_TOKEN` value. To revoke a refresh token and associated access tokens,
use the `DELETE_TOKEN` value. To revoke a JSON Web Token (JWT)-based access token, use the `ORG_JWT` value.

```
   authToken
```

Type: String

The access token (opaque or JWT-based), refresh token, or delete token issued by Salesforce.

Return Value

Type: Boolean

The method returns `true` if successful, and `false` if not. For invalid or expired tokens, the method returns a
`[NoDataFoundException](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)` exception.

### OauthTokenType Enum

Specifies the type of Salesforce-issued OAuth 2.0 token being revoked in the `OauthToken.revokeToken` method.

Enum Values

The following are the values of the `Auth.OauthTokenType` enum.

**Value** **Description**

`ACCESS_TOKEN` An opaque access token, which Salesforce grants to a client when it successfully
completes an authorization flow. Salesforce grants opaque access tokens by default.

`DELETE_TOKEN` A delete token, which can be queried and used to revoke refresh tokens and
associated access tokens.

`REFRESH_TOKEN` A refresh token, which Salesforce grants to a client as a result of the refresh token
flow. Refresh tokens are used to get more access tokens.

```
ORG_JWT

```

A JSON Web Token (JWT)-based access token, which Salesforce grants to a client
when it successfully completes an authorization flow. Salesforce grants JWT-based
access tokens if you enable them for a connected app or external client app.


### Apex Reference Guide RegistrationHandler Interface RegistrationHandler Interface

Salesforce provides the ability to use an authentication provider, such as Facebook [©] or Janrain [©], for single sign-on into Salesforce.

Namespace

Auth

Usage

To set up single sign-on, you must create a class that implements `Auth.RegistrationHandler` . Classes implementing the
`Auth.RegistrationHandler` interface are specified as the `Registration Handler` in authentication provider definitions,
and enable single sign-on into Salesforce portals and organizations from third-party services such as Facebook. Using information from
the authentication providers, your class must perform the logic of creating and updating user data as appropriate, including any associated
account and contact records.

Note: During the user update process, you can use the `confirmUser()` method to ensure that users are correctly mapped
between Salesforce and the third party. For more information, see the ConfirmUserRegistrationHandler Interface.

IN THIS SECTION:

#### RegistrationHandler Methods

Storing User Information and Getting Access Tokens

Auth.RegistrationHandler Example Implementation

Auth.RegistrationHandler Error Example
This example implements the `Auth.RegistrationHandler` interface and shows how to use a custom exception to display
an error message in the URL of the page. If you don’t use a custom exception, the error code and description appear in the URL and
the error description appears on the page.

#### RegistrationHandler Methods

### The following are methods for RegistrationHandler .

IN THIS SECTION:

##### createUser(portalId, userData)

Returns a User object using the specified portal ID and user information from the third party, such as the username and email address.
The User object corresponds to the third party’s user information. It can be a new user that hasn’t been inserted in your org’s database,
or it can represent an existing user record in the database. If it’s a new User object, Salesforce inserts a user record for you.

updateUser(userId, portalId, userData)
Updates the specified user’s information. This method is called if the user has logged in before with the authentication provider and
then logs in again.

##### createUser(portalId, userData)

Returns a User object using the specified portal ID and user information from the third party, such as the username and email address.
The User object corresponds to the third party’s user information. It can be a new user that hasn’t been inserted in your org’s database,
or it can represent an existing user record in the database. If it’s a new User object, Salesforce inserts a user record for you.


Apex Reference Guide RegistrationHandler Interface

Signature

```
   public User createUser(ID portalId, Auth.UserData userData)

```

Parameters

```
   portalId
```

Type: ID

```
   userData
```

Type: Auth.UserData

Return Value

Type: User

Usage

The _`portalID`_ value can be null or an empty key if there’s no portal configured with this provider.

##### updateUser(userId, portalId, userData)

Updates the specified user’s information. This method is called if the user has logged in before with the authentication provider and
then logs in again.

Signature

```
   public Void updateUser(ID userId, ID portalId, Auth.UserData userData)

```

Parameters

```
   userId
```

Type: ID

```
   portalId
```

Type: ID

```
   userData
```

Type: Auth.UserData

Return Value

Type: Void

Usage

The _`portalID`_ value can be null or an empty key if there's no portal configured with this provider.

#### Storing User Information and Getting Access Tokens

The `Auth.UserData` class is used to store user information for `Auth.RegistrationHandler` . The third-party identity
provider can send back a large collection of data about the user, including their username, email address, locale, and more. The Salesforce


Apex Reference Guide RegistrationHandler Interface

authentication provider framework converts this data into a common format with the `Auth.UserData` class and then sendsit to
the registration handler.

[Note: If you use a predefined Salesforce authentication provider, Salesforce constructs the](https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.sso_predefined_authentication_provider_parent.htm) `Auth.UserData` object for you.
[If you use a custom authentication provider plug-in, it's up to you to determine how you store information in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/authproviderplugin.htm) `Auth.UserData`
object.

If the registration handler wants to use the rest of the data, the `Auth.UserData` class has an `attributeMap` variable. The
attribute map is a map of strings ( `Map<String, String>` ) for the raw values of all the data from the third party. Because the map
is `<String, String>`, values that the third party returns that aren't strings (like an array of URLs or a map) are converted into an
appropriate string representation. The map includes everything returned by the third-party authentication provider, including the items
automatically converted into the common format.

To learn about `Auth.UserData` properties, see Auth.UserData Class.

Note: You can only perform DML operations on additional sObjects in the same transaction with User objects under certain
[circumstances. For more information, see sObjects That Cannot Be Used Together in DML Operations.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dml_non_mix_sobjects.htm)

For all authentication providers except Janrain, after a user is authenticated using a provider, the access token associated with that
provider for this user can be obtained in Apex using the `Auth.AuthToken` Apex class. `Auth.AuthToken` provides two methods
to retrieve access tokens. One is `getAccessToken`, which obtains a single access token. Use this method if the user ID is mapped
to a single third-party user. If the user ID is mapped to multiple third-party users, use `getAccessTokenMap`, which returns a map
[of access tokens for each third-party user. For more information about authentication providers, see Authentication Providers in](https://help.salesforce.com/s/articleView?id=experience.sso_authentication_providers.htm&type=5&language=en_US) _Salesforce_
_Help_ .

When using Janrain as an authentication provider, you must use the Janrain `accessCredentials` dictionary values to retrieve the
access token or its equivalent. Only some providers supported by Janrain provide an access token, while other providers use other fields.
The Janrain `accessCredentials` fields are returned in the `attributeMap` variable of the `Auth.UserData` class. See the
Janrain `[auth_info](http://developers.janrain.com/documentation/api/auth_info/)` documentation for more information on `accessCredentials` .

Note: Not all Janrain account types return `accessCredentials` . Sometimes you must change your account type to receive
the information.

To learn about the `Auth.AuthToken` methods, see Auth.AuthToken Class.

User Information in the ID Token and User Info Response

Some identity providers send additional user information in an ID token or in a user info response. To extract user information from these
responses, there are some extra steps.

An ID token is formatted as a JWT and includes information about the authenticated user. If the identity provider sends an ID token,
Salesforce stores the full encoded JWT in the `idToken` property. Salesforce also stores the decoded JWT payload of the ID token in
the `idTokenJSONString` property.

Salesforce doesn't validate the ID token. To validate it, use methods in the `[Auth.JWTUtil](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_JWTUtil.htm)` class and pass in the encoded JWT stored
in the `idToken` property. The methods in the `Auth.JWTUtil` class all return an instance of the `Auth.JWT` object.

Once you validate the JWT, you can use methods in the `[Auth.JWT](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_JWT.htm)` class to access specific claims. For example, the Apex code in this
snippet validates the ID token using a public keys endpoint from the identity provider and then retrieves the value of an `email` claim
stored in the token.

```
   Auth.JWT jwt = Auth.JWTUtil.validateJWTWithKeysEndpoint(userdata.idToken, keysEndpoint,

   true);

   // Retrieve email claim from id token

```


Apex Reference Guide RegistrationHandler Interface

```
   String email = (String) jwt.getAdditionalClaims().get('email');

   System.debug(email);

```

Alternatively, to access specific claims in the `idTokenJSONString` property, you can deserialize the JSON string and then write
code to retrieve the claim you want. To deserialize the `idTokenJSONString`, use the `[JSON.deserialize (jsonString,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Json.htm#apex_System_Json_deserialize)`
`[apexType)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Json.htm#apex_System_Json_deserialize)` method in the `System.JSON` class.

The user info response, if returned by the identity provider, is also a JSON object that has been serialized into a string. The user info
response is stored in the `userInfoJSONString` property. You can use the `[JSON.deserialize (jsonString,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Json.htm#apex_System_Json_deserialize)`
`[apexType)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Json.htm#apex_System_Json_deserialize)` method to deserialize the user info response so that you can retrieve specific information.

This example snippet creates a custom class to store the user info response. It then deserializes the user info response in the
`userInfoJSONString` into this custom class structure.

```
   public class UserInfoResponse {

      public String preferred_username;

      public String email;

      public Boolean email_verified;

      public String given_name;

      public String family_name;

      public String locale;

   }

   UserInfoResponse userInfo =

   (UserInfoResponse)System.JSON.deserialize(userData.userInfoJSONString,

   UserInfoResponse.class);

   System.debug(userInfo.email);

#### Auth.RegistrationHandler Example Implementation This example implements the Auth.RegistrationHandler interface that creates as well as updates a standard user based on
```

data provided by the authentication provider. Error checking has been omitted to keep the example simple.

```
   global class StandardUserRegistrationHandler implements Auth.RegistrationHandler{

      global User createUser(Id portalId, Auth.UserData data) {

        User u = new User();

        Profile p = [SELECT Id FROM profile WHERE name='Standard User'];

        u.Username = data.username + '@salesforce.com';

        u.Email = data.email;

        u.LastName = data.lastName;

        u.FirstName = data.firstName;

        String alias = data.username;

        if(alias.length() > 8) {

           alias = alias.substring(0, 8);

        }

        u.Alias = alias;

        u.LanguageLocaleKey = data.attributeMap.get('language');

        u.LocaleSidKey = data.locale;

        u.EmailEncodingKey = 'UTF-8';

        u.TimeZoneSidKey = 'America/Los_Angeles';

        u.ProfileId = p.Id;

        return u;

      }

      global void updateUser(Id userId, Id portalId, Auth.UserData data) {

```


Apex Reference Guide RegistrationHandler Interface

```
        User u = new User(id=userId);

        u.Username = data.username + '@salesforce.com';

        u.Email = data.email;

        u.LastName = data.lastName;

        u.FirstName = data.firstName;

        String alias = data.username;

        if(alias.length() > 8) {

           alias = alias.substring(0, 8);

        }

        u.Alias = alias;

        u.LanguageLocaleKey = data.attributeMap.get('language');

        u.LocaleSidKey = data.locale;

        update(u);

      }

   }

```

The following example tests the above code.

```
   @isTest

   private class StandardUserRegistrationHandlerTest {

   static testMethod void testCreateAndUpdateUser() {

      StandardUserRegistrationHandler handler = new StandardUserRegistrationHandler();

      Auth.UserData sampleData = new Auth.UserData('testId', 'testFirst', 'testLast',

        'testFirst testLast', 'testuser@example.org', null, 'testuserlong', 'en_US',

   'facebook',

        null, new Map<String, String>{'language' => 'en_US'});

      User u = handler.createUser(null, sampleData);

      System.assertEquals('testuserlong@salesforce.com', u.username);

      System.assertEquals('testuser@example.org', u.email);

      System.assertEquals('testLast', u.lastName);

      System.assertEquals('testFirst', u.firstName);

      System.assertEquals('testuser', u.alias);

      insert(u);

      String uid = u.id;

      sampleData = new Auth.UserData('testNewId', 'testNewFirst', 'testNewLast',

        'testNewFirst testNewLast', 'testnewuser@example.org', null, 'testnewuserlong',

   'en_US', 'facebook',

        null, new Map<String, String>{'language' => 'en_US'});

      handler.updateUser(uid, null, sampleData);

      User updatedUser = [SELECT username, email, firstName, lastName, alias FROM user WHERE

    id=:uid];

      System.assertEquals('testnewuserlong@salesforce.com', updatedUser.username);

      System.assertEquals('testnewuser@example.org', updatedUser.email);

      System.assertEquals('testNewLast', updatedUser.lastName);

      System.assertEquals('testNewFirst', updatedUser.firstName);

      System.assertEquals('testnewu', updatedUser.alias);

   }

   }

```


### Apex Reference Guide SamlJitHandler Interface

#### Auth.RegistrationHandler Error Example This example implements the Auth.RegistrationHandler interface and shows how to use a custom exception to display an

error message in the URL of the page. If you don’t use a custom exception, the error code and description appear in the URL and the
error description appears on the page.

To limit this example to the custom exception, some code was omitted.

```
   global class RegHandler implements Auth.RegistrationHandler {

      class RegHandlerException extends Exception {}

        global User createUser(Id portalId, Auth.UserData data){

          List<Profile> profiles = [SELECT Id, Name, UserType FROM Profile WHERE Name =

    'Power User'];

           Profile profile = profiles.isEmpty() ? null : profiles[0];

           if(profile==null)

            throw new RegHandlerException('Cannot find the profile. For help, contact

   your administrator.');

   ...

        }

        global void updateUser(Id userId, Id portalId, Auth.UserData data){

           User u = new User(id=userId);

           u.lastName = data.lastName;

           u.firstName = data.firstName;

           update(u);

        }

   }

### SamlJitHandler Interface

```

Use this interface to control and customize Just-in-Time user provisioning logic during SAML single sign-on.

Namespace

#### Auth

Usage

To use custom logic for user provisioning during SAML single sign-on, you must create a class that implements
`Auth.SamlJitHandler` . This allows you to incorporate organization-specific logic (such as populating custom fields) when users
log in to Salesforce with single sign-on. Keep in mind that your class must perform the logic of creating and updating user data as
appropriate, including any associated account and contact records.

In Salesforce, you specify your class that implements this interface in the `SAML JIT Handler` field in SAML Single Sign-On Settings.
Make sure that the user you specify to run the class has “Manage Users” permission.

IN THIS SECTION:

SamlJitHandler Methods

SamlJitHandler Example Implementation


Apex Reference Guide SamlJitHandler Interface

#### SamlJitHandler Methods The following are methods for SamlJitHandler .

IN THIS SECTION:

##### createUser(samlSsoProviderId, communityId, portalId, federationId, attributes, assertion)

Returns a User object using the specified Federation ID. The User object corresponds to the user information. This object can be a
new user that hasn’t been inserted in the database or an existing user record in the database.

updateUser(userId, samlSsoProviderId, communityId, portalId, federationId, attributes, assertion)
Updates the specified user’s information. This method is called if the user has logged in before with SAML single sign-on and then
logs in again, or if your application is using the `Existing User Linking URL` .

##### createUser(samlSsoProviderId, communityId, portalId, federationId, attributes, assertion)

Returns a User object using the specified Federation ID. The User object corresponds to the user information. This object can be a new
user that hasn’t been inserted in the database or an existing user record in the database.

Signature

```
   public User createUser(Id samlSsoProviderId, Id communityId, Id portalId, String

   federationId, Map<String,String> attributes, String assertion)

```

Parameters

```
   samlSsoProviderId
```

Type: Id

The ID of the SamlSsoConfig standard object.

```
   communityId
```

Type: Id

The ID of the Experience Cloud site. This parameter can be `null` if you’re not creating an Experience Cloud user.

```
   portalId
```

Type: Id

The ID of the portal. This parameter can be `null` if you’re not creating a portal user.

```
   federationId
```

Type: String

The ID Salesforce expects to be used for this user.

```
   attributes
```

Type: Map<String,String>

All attributes in the SAML assertion that were added to the default assertion; for example, custom attributes. Attributes are
case-sensitive.

If the assertion is encrypted, the attribute map contains a decrypted assertion stored as a value with the key
`Sfdc.SamlAssertion` .

```
   assertion
```

Type: String


Apex Reference Guide SamlJitHandler Interface

The default SAML assertion, base-64 encoded.

If the assertion is encrypted, this parameter is also encrypted. To access the decrypted assertion, see the `Sfdc.SamlAssertion`
key in the attribute map.

Return Value

Type: User

A User sObject.

Usage

The _`communityId`_ and _`portalId`_ parameter values can be `null` or the associated keys can be empty if there’s no Experience
Cloud site or portal configured with this organization.

##### updateUser(userId, samlSsoProviderId, communityId, portalId, federationId, attributes, assertion)

Updates the specified user’s information. This method is called if the user has logged in before with SAML single sign-on and then logs
in again, or if your application is using the `Existing User Linking URL` .

Signature

```
   public void updateUser(Id userId, Id samlSsoProviderId, Id communityId, Id portalId,

   String federationId, Map<String,String> attributes, String assertion)

```

Parameters

```
   userId
```

Type: Id

The ID of the Salesforce user.

```
   samlSsoProviderId
```

Type: Id

The ID of the SamlSsoConfig object.

```
   communityId
```

Type: Id

The ID of the Experience Cloud site. This type can be `null` if you’re not updating an Experience Cloud user.

```
   portalId
```

Type: Id

The ID of the portal. This type can be `null` if you’re not updating a portal user.

```
   federationId
```

Type: String

The ID Salesforce expects to be used for this user.

```
   attributes
```

Type: Map<String,String>

All attributes in the SAML assertion that were added to the default assertion; for example, custom attributes. Attributes are
case-sensitive.


Apex Reference Guide SamlJitHandler Interface

If the assertion is encrypted, the attribute map also contains a decrypted assertion stored as a value with the key
`Sfdc.SamlAssertion` .

```
   assertion
```

Type: String

The default SAML assertion, base-64 encoded.

If the assertion is encrypted, this parameter is also encrypted. To access the decrypted assertion, see the `Sfdc.SamlAssertion`
key in the attribute map.

Return Value

Type: void

#### SamlJitHandler Example Implementation

This is an example implementation of the `Auth.SamlJitHandler` interface. This code uses private methods to handle accounts
and contacts (handleContact() and handleAccount()), which aren’t included in this example.

```
   global class StandardUserHandler implements Auth.SamlJitHandler {

      private class JitException extends Exception{}

      private void handleUser(boolean create, User u, Map<String, String> attributes,

        String federationIdentifier, boolean isStandard) {

        if(create && attributes.containsKey('User.Username')) {

           u.Username = attributes.get('User.Username');

        }

        if(create) {

           if(attributes.containsKey('User.FederationIdentifier')) {

             u.FederationIdentifier = attributes.get('User.FederationIdentifier');

           } else {

             u.FederationIdentifier = federationIdentifier;

           }

        }

        if(attributes.containsKey('User.ProfileId')) {

           String profileId = attributes.get('User.ProfileId');

           Profile p = [SELECT Id FROM Profile WHERE Id=:profileId];

           u.ProfileId = p.Id;

        }

        if(attributes.containsKey('User.UserRoleId')) {

           String userRole = attributes.get('User.UserRoleId');

           UserRole r = [SELECT Id FROM UserRole WHERE Id=:userRole];

           u.UserRoleId = r.Id;

        }

        if(attributes.containsKey('User.Phone')) {

           u.Phone = attributes.get('User.Phone');

        }

        if(attributes.containsKey('User.Email')) {

           u.Email = attributes.get('User.Email');

        }

    //More attributes here - removed for length

        //Handle custom fields here

```


### Apex Reference Guide SessionManagement Class

```
        if(!create) {

           update(u);

        }

      }

      private void handleJit(boolean create, User u, Id samlSsoProviderId, Id communityId,

   Id portalId,

        String federationIdentifier, Map<String, String> attributes, String assertion) {

        if(communityId != null || portalId != null) {

           String account = handleAccount(create, u, attributes);

           handleContact(create, account, u, attributes);

           handleUser(create, u, attributes, federationIdentifier, false);

        } else {

           handleUser(create, u, attributes, federationIdentifier, true);

        }

      }

      global User createUser(Id samlSsoProviderId, Id communityId, Id portalId,

        String federationIdentifier, Map<String, String> attributes, String assertion) {

        User u = new User();

        handleJit(true, u, samlSsoProviderId, communityId, portalId,

           federationIdentifier, attributes, assertion);

        return u;

      }

      global void updateUser(Id userId, Id samlSsoProviderId, Id communityId, Id portalId,

        String federationIdentifier, Map<String, String> attributes, String assertion) {

        User u = [SELECT Id FROM User WHERE Id=:userId];

        handleJit(false, u, samlSsoProviderId, communityId, portalId,

           federationIdentifier, attributes, assertion);

      }

   }

### SessionManagement Class

```

Contains methods for verifying users’ identity, creating custom login flows, customizing security levels, and defining trusted IP ranges
for a current session.

Namespace

Auth

IN THIS SECTION:

#### SessionManagement Methods SessionManagement Methods

### The following are methods for SessionManagement . All methods are static. Use these methods to customize your user identity

verification flows, manage the use of time-based one-time password (TOTP) apps like Google Authenticator, or create custom login
flows. Other methods validate a user’s incoming IP address against trusted IP range settings for an organization or profile.


Apex Reference Guide SessionManagement Class

IN THIS SECTION:

finishLoginDiscovery(method, userId)
Finishes the My Domain Login Discovery login process.

finishLoginFlow()
Finish the Visualforce Page login flow process, and redirect the user to the default home page.

finishLoginFlow(startUrl)
Finish the Visualforce Page login flow process, and redirect the user to the specified start URL.

generateVerificationUrl(policy, description, destinationUrl)
Initiates a user identity verification flow with the verification method that the user registered with, and returns a URL to the identity
verification screen. For example, if you have a custom Visualforce page that displays sensitive account details, you can prompt the
user to verify identity before viewing it.

getCurrentSession()
Returns a map of attributes for the current session.

getLightningLoginEligibility(userId)
Returns the eligibility status for a user who’s logging in with Lightning Login when you set up your org with My Domain and use
the Login Discovery page type. Use this method to redirect the user to a custom login flow. For example, use after a login attempt
to redirect the user to password flow if the user is ineligible for Lightning Login.

getQrCode()
Returns a map containing a URL to a quick response (QR) code and a time-based one-time password (TOTP) shared secret to configure
authenticator apps or devices for multi-factor authentication (MFA).

getRequiredSessionLevelForProfile(profileId)
Indicates the required login security session level for the given profile.

ignoreForConcurrentSessionLimit(sessions)
This method is reserved for internal Salesforce use.

inOrgNetworkRange(ipAddress)
Indicates whether the given IP address is within the organization's trusted IP range according to the organization's Network Access
settings.

isIpAllowedForProfile(profileId, ipAddress)
Indicates whether the given IP address is within the trusted IP range for the given profile.

setSessionLevel(level)
Sets the user's current session security level.

validateTotpTokenForKey(sharedKey, totpCode)
Deprecated. Use `validateTotpTokenForKey(totpSharedKey, totpCode, description)` instead.

validateTotpTokenForKey(totpSharedKey, totpCode, description)
Indicates whether a time-based one-time password (TOTP) code (token) is valid for the given shared key.

validateTotpTokenForUser(totpCode)
Deprecated. Use `validateTotpTokenForUser(totpCode, description)` instead.

validateTotpTokenForUser(totpCode, description)
Indicates whether a time-based one-time password (TOTP) code (token) is valid for the current user.

verifyDeviceFlow(userCode, startUrl)
Verifies the user code entered during the device authentication flow and redirects users to the OAuth approval page. If users aren’t
logged in, they must log in. After successful login, users are prompted to allow the device to access Salesforce data.


Apex Reference Guide SessionManagement Class

##### finishLoginDiscovery(method, userId)

Finishes the My Domain Login Discovery login process.

Signature

```
   public static System.PageReference finishLoginDiscovery(Auth.LoginDiscoveryMethod

   method, Id userId)

```

Parameters

```
   method
```

Type: Auth.LoginDiscoveryMethod LoginDiscoveryMethod Enum

Verification method used with My Domain Login Discovery.

```
   userId
```

Type: Id

ID used to log in the user. The user must be active.

Return Value

Type: System.PageReference

Usage

Include this method when implementing the `MyDomainLoginDiscoveryHandler` interface to direct users to an authentication
mechanism, and then log them in. If users enter a username in the login page, they are sent to the password page for authentication.
If users are enrolled in Lightning Login, they are directed to the Salesforce Authenticator to authenticate. If users are SSO-enabled, they
are sent to the suitable identity provider (IdP) to authenticate.

The calling user requires Manage Users permission. If the user passed in is frozen or inactive, the method throws an exception.

After implementing the `MyDomainLoginDiscoveryHandler` interface, register the Login Discovery handler from the My
Domain Setup page. Under Authentication Configuration, select this handler from the list of Apex classes.

##### finishLoginFlow()

Finish the Visualforce Page login flow process, and redirect the user to the default home page.

Signature

```
   public static System.PageReference finishLoginFlow()

```

Return Value

Type: System.PageReference

Usage

Include this method in the Apex controller of the Visualforce Page login flow when creating login flows programmatically. This method
indicates that the login flow is finished and redirects the user to the Experience Cloud site’s default home page. The login process runs


Apex Reference Guide SessionManagement Class

in a restricted session until users complete the process. Calling this method indicates that the login flow is complete, lifts the restriction,
and gives users full access to the Experience Cloud site.

##### finishLoginFlow(startUrl)

Finish the Visualforce Page login flow process, and redirect the user to the specified start URL.

Signature

```
   public static System.PageReference finishLoginFlow(String startUrl)

```

Parameters

```
   startUrl
```

Type: String

Path to the page that users see when they access the Experience Cloud site.

Return Value

Type: System.PageReference

Usage

Include this method in the Apex controller of the Visualforce Page login flow when creating login flows programmatically. This method
indicates that the login flow is finished and redirects the user to the specified location in the Experience Cloud site. The login process
runs in a restricted session until users complete the process. Calling this method indicates that the login flow is complete, lifts the
restriction, and gives users full access to the Experience Cloud site.

##### generateVerificationUrl(policy, description, destinationUrl)

Initiates a user identity verification flow with the verification method that the user registered with, and returns a URL to the identity
verification screen. For example, if you have a custom Visualforce page that displays sensitive account details, you can prompt the user
to verify identity before viewing it.

Signature

```
   public static String generateVerificationUrl(Auth.VerificationPolicy policy, String

   description, String destinationUrl)

```

Parameters

```
   policy
```

Type: Auth.VerificationPolicy

The session security policy required to initiate identity verification for the user’s session. For example, if the policy is set to High
Assurance level of session security, and the user’s current session has the standard level of session security, the user’s session is raised
to high assurance after successful verification of identity. In the Setup user interface, this value is shown in the Triggered By column
of Identity Verification History.

```
   description
```

Type: String


Apex Reference Guide SessionManagement Class

The custom description that describes the activity requiring identity verification; for example, “Complete purchase and check out”.
This text appears to users when they verify their identity in Salesforce and, if they use Salesforce Authenticator version 2 or later, in
the Salesforce Authenticator mobile app. In addition, in the Setup user interface, this text is shown in the Activity Message column
of Identity Verification History.

```
   destinationUrl
```

Type: String

The relative or absolute Salesforce URL that you want to redirect the user to after identity verification—for example, `/apex/mypage` .
The user is redirected to _`destinationUrl`_ when the identity verification flow is complete, regardless of success. For example,
if a user chooses to not respond to the identity challenge and cancels it, the user is still redirected to _`destinationUrl`_ . As a
best practice, ensure that your code for this page manually checks that the security policy was satisfied (and the user didn’t just
manually type the URL in the browser). For example, if the _`policy`_ is High Assurance, the target page checks that the user's session
is high assurance before allowing access.

Return Value

Type: String

The URL where the user is redirected to verify identity.

Usage

**•** If the user is already registered to confirm identity using a time-based one-time password (TOTP), then the user is redirected to the
one-time password identity verification flow and asked to provide a code.

**•** If the user isn’t registered with any verification method (such as one-time password or Salesforce Authenticator version 2 or later),
the user is prompted to download and verify identity using Salesforce Authenticator. The user can also choose a different verification
method.

##### getCurrentSession()

Returns a map of attributes for the current session.

Signature

```
   public static Map<String, String> getCurrentSession()

```

Return Value

Type: Map<String, String>

Usage

The map includes a `ParentId` value, which is the 18-character ID for the parent session, if one exists (for example, if the current
session is for a canvas app). If the current session doesn’t have a parent, this value is null. The map also includes the `LogoutUrl`
assigned to the current session.

If you create an Apex test method that calls this method, the test fails with an error such as, “Unexpected Exception: Current session
unavailable." An error occurs because there isn’t a session in the context through which the test is being run.

When a session is reused, Salesforce updates the `LoginHistoryId` with the value from the most recent login.


Apex Reference Guide SessionManagement Class

Example

The following example shows the name-value pairs in a map returned by `getCurrentSession()` . Note that `UsersId` includes
an “s” in the name to match the name of the corresponding field in the AuthSession object.

```
   {

   SessionId=0Ak###############,

   UserType=Standard,

   ParentId=0Ak###############,

   NumSecondsValid=7200,

   LoginType=SAML Idp Initiated SSO,

   LoginDomain=null,

   LoginHistoryId=0Ya###############,

   Username=user@domain.com,

   CreatedDate=Wed Jul 30 19:09:29 GMT 2014,

   SessionType=Visualforce,

   LastModifiedDate=Wed Jul 30 19:09:16 GMT 2014,

   LogoutUrl=https://google.com,

   SessionSecurityLevel=STANDARD,

   UsersId=005###############,

   SourceIp=1.1.1.1

   }

##### getLightningLoginEligibility(userId)

```

Returns the eligibility status for a user who’s logging in with Lightning Login when you set up your org with My Domain and use the
Login Discovery page type. Use this method to redirect the user to a custom login flow. For example, use after a login attempt to redirect
the user to password flow if the user is ineligible for Lightning Login.

Signature

```
   public static Auth.LightningLoginEligibility getLightningLoginEligibility(Id userId)

```

Parameters

```
   userId
```

Type: Id

ID of the user who is logging in.

Return Value

Type: Auth.LightningLoginEligibility

Returns the current eligibility status.

Example

```
   Auth.LightningLoginEligibility eligibility =

      Auth.SessionManagement.getLightningLoginEligibility(id);

   if (eligibility == Auth.LightningLoginEligibility.ELIGIBLE) {

      // success

   }

```


Apex Reference Guide SessionManagement Class

##### getQrCode()

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


Apex Reference Guide SessionManagement Class

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


Apex Reference Guide SessionManagement Class

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


Apex Reference Guide SessionManagement Class

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

##### validateTotpTokenForKey(sharedKey, totpCode)

```

Deprecated. Use `validateTotpTokenForKey(totpSharedKey, totpCode, description)` instead.

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


Apex Reference Guide SessionManagement Class

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

##### validateTotpTokenForUser(totpCode)

Deprecated. Use `validateTotpTokenForUser(totpCode, description)` instead.

Signature

```
   public static Boolean validateTotpTokenForUser( String totpCode )

```


Apex Reference Guide SessionManagement Class

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


### Apex Reference Guide SessionLevel Enum

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


### Apex Reference Guide TokenValidationResult Class

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

Usage

### For a full example implementation that shows how to get information from the TokenValidationResult class, see OAuth 2.0

[Token Exchange Handler Examples.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/token_exchange_handler.htm)

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

```


Apex Reference Guide TokenValidationResult Class

```
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


Apex Reference Guide TokenValidationResult Class

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

[Type: Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_UserData.htm)

Stores information about a Salesforce user.

```
   token
```

Type: String

The token from the external identity provider.

```
   tokenType
```

[Type: Auth.OAuth2TokenExchangeType](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)

The type of token from the external identity provider.

```
   customErrorMsg
```

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

customErrorMsg
A custom error message that’s returned if token validation fails.


Apex Reference Guide TokenValidationResult Class

##### data

Contains information about the user that isn’t stored in the `Auth.UserData` class, such as information obtained via callouts to
the external identity provider.

##### isValid

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


Apex Reference Guide TokenValidationResult Class

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

Signature

```
   public Auth.OAuth2TokenExchangeType tokenType {get; set;}

```

Property Value

[Type: Auth.OAuth2TokenExchangeType](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)

##### **`userData`**

Information about the user that’s obtained from the identity provider’s token.

Signature

```
   public Auth.UserData userData {get; set;}

```

Property Value

[Type: Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_UserData.htm)

#### TokenValidationResult Methods The following are methods for TokenValidationResult .

IN THIS SECTION:

getCustomErrorMessage()
Retrieves the `CustomErrorMsg` that’s returned when token validation fails.

getData()
##### Retrieves data from the identity provider token. This data can include custom data that isn’t stored in the userData property.


Apex Reference Guide TokenValidationResult Class

##### getToken()

Retrieves the token that was passed from the external identity provider.

##### getTokenType()

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


### Apex Reference Guide UserData Class

Signature

```
   public Auth.OAuth2TokenExchangeType getTokenType()

```

Return Value

[Type: Auth.OAuth2TokenExchangeType](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)

##### **`getUserData()`**

Retrieves information about the user. The user information can be obtained from the identity provider’s token or from callouts to the
identity provider, if applicable.

Signature

```
   public Auth.UserData getUserData()

```

Return Value

[Type: Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_UserData.htm)

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

For more information about using this class with the `Auth.RegistrationHandler` [interface, see Storing User Information and](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_auth_plugin.htm#apex_auth_plugin_part2)
[Getting Access Tokens in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_auth_plugin.htm#apex_auth_plugin_part2) `RegistrationHandler` Interface documentation.

[For more information about using this class as an Apex-defined variable in a user registration flow, see Example: Authentication Provider](https://help.salesforce.com/s/articleView?id=xcloud.sso_flow_registration_handler_example.htm&language=en_US)
[Registration Handler Flow in Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.sso_flow_registration_handler_example.htm&language=en_US)


Apex Reference Guide UserData Class

IN THIS SECTION:

#### UserData Constructors

UserData Properties

#### UserData Constructors The following are constructors for UserData .

IN THIS SECTION:

##### UserData(identifier, firstName, lastName, fullName, email, link, userName, locale, provider, siteLoginUrl, attributeMap)

Creates a new instance of the `Auth.UserData` class using the specified arguments.

UserData(identifier, firstName, lastName, fullName, email, link, username, locale, provider, siteLoginUrl, attributeMap, idToken,
userInfoJSONString)
Creates an instance of the Auth.UserData class that includes the ID token and user info response from the identity provider, if returned
during single sign-on.

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


Apex Reference Guide UserData Class

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


Apex Reference Guide UserData Class

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


Apex Reference Guide UserData Class

IN THIS SECTION:

##### identifier

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


Apex Reference Guide UserData Class

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


Apex Reference Guide UserData Class

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


Apex Reference Guide UserData Class

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


### Apex Reference Guide VerificationAction Enum

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
`System.UserManagement.deregisterVerificationMethod` on page 4292 methods. The value indicates the method
used to verify a user’s identity.

Enum Values

The following are the values of the `Auth.VerificationMethod` enum.

**Value** **Description**

`BUILT_IN_AUTHENTICATOR` Identity verified with a built-in authenticator.

`EMAIL` Identity verified with a verification code sent in an email message.

`PASSWORD` Identity verified with a password.


### Apex Reference Guide VerificationPolicy Enum

**Value** **Description**

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


Apex Reference Guide VerificationResult Class

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

#### VerificationResult Constructor

VerificationResult Properties

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


Apex Reference Guide VerificationResult Class

Indicates whether verification succeeded.

##### _`message`_

Type: String

Message that displays as a result of a verification challenge.

#### VerificationResult Properties The following are properties for VerificationResult .

IN THIS SECTION:

##### message

Message that displays as a result of a verification challenge. `Token is valid` if the identity verification is successful. Other
values are `FAILURE`, `PENDING`, `RATE_LIMITED`, or `FAILURE_REPORT` .

##### redirect

Where the user is directed after entering the verification code successfully, for example, the Experience Cloud site’s home page or
location specified by the start URL.

success
The verification challenge is successful.

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


### Apex Reference Guide Auth Exceptions

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

```

Throw this exception to indicate that an error occurred when using the auth provider plug-in.
Use to display a custom error message to the user. To get the error message and write it to
debug log, use the `String getMessage()` .

Throw this exception to indicate that an error occurred while running the custom behavior for
a connected app. To get the error message and write it to debug log, use the `String`

`getMessage()` .


Apex Reference Guide Auth Exceptions

**Exception** **Description**

```
Auth.DiscoveryCustomErrorException

Auth.JWTBearerTokenExchange.

JWTBearerTokenExchangeException

```

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

`Auth.JWTValidationException` Throws this exception to indicate failure to validate a JWT using methods in the `JWTUtil`
class. This exception occurs during the OAuth 2.0 token exchange flow in these scenarios.

**•** Can’t parse the JWT

**•** Can’t validate the JWT using a certificate, a public key, or the remote keys endpoint,
depending on which method you use

```
Auth.LoginDiscoveryException

Auth.VerificationException

```

Throw this exception to indicate that an error occurred when executing the Login Discovery
handler. For an example, see LoginDiscoveryHandler Example Implementation. To get the error
message and write it to debug log, use the `String getMessage()` .

Throw this exception to trigger verification based on the passed-in policy. You can throw this
exception in an Apex trigger or Visualforce controller. The system automatically sends you to
the verification endpoint, if possible.

Note: You can’t catch this exception. The exception immediately triggers the verification.


## Apex Reference Guide Cache Namespace

Examples

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

        throw new Auth.VerificationException(

           Auth.VerificationPolicy.HIGH_ASSURANCE, 'Insert Account');

      }

   }

## Cache Namespace The Cache namespace contains methods for managing the platform cache. The following are the classes in the Cache namespace.

```

IN THIS SECTION:

CacheBuilder Interface
An interface for safely retrieving and removing values from a session or org cache. Use the interface to generate a value that you
want to store in the cache. The interface checks for cache misses, which means you no longer need to check for null cache values
yourself.


### Apex Reference Guide CacheBuilder Interface

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
### The Cache namespace contains exception classes.

Visibility Enum
Use the `Cache.Visibility` enumeration in the `Cache.Session` or `Cache.Org` methods to indicate whether a cached
value is visible only in the value’s namespace or in all namespaces.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

### CacheBuilder Interface

An interface for safely retrieving and removing values from a session or org cache. Use the interface to generate a value that you want
to store in the cache. The interface checks for cache misses, which means you no longer need to check for null cache values yourself.

Namespace

### Cache

IN THIS SECTION:

#### CacheBuilder Methods

CacheBuilder Example Implementation

SEE ALSO:

_Apex Developer Guide_ [: Safely Cache Values with the CacheBuilder Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_platform_cache_builder.htm)

#### CacheBuilder Methods

### The following are methods for CacheBuilder .


### Apex Reference Guide Org Class

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


Apex Reference Guide Org Class

Namespace

Cache

Usage

**Cache Key Format**

This table lists the format of the key parameter that some methods in this class take, such as `put`, `get`, and `contains` .

Note:

**•** If no default partition is specified in the org, calling a cache method without fully qualifying the key name causes a
`Cache.Org.OrgCacheException` to be thrown.

**•** The `local` prefix in an installed managed package refers to the namespace of the subscriber org and not the package’s
namespace. The cache `put` calls aren’t allowed in a partition that the invoking class doesn’t own.

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

```


Apex Reference Guide Org Class

```
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

```


Apex Reference Guide Org Class

```
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

```


Apex Reference Guide Org Class

```
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

Org Constants
The Org class provides a constant that you can use when setting the time-to-live (TTL) value.


Apex Reference Guide Org Class

#### Org Methods

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

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


Apex Reference Guide Org Class

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


Apex Reference Guide Org Class

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


Apex Reference Guide Org Class

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


Apex Reference Guide Org Class

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


Apex Reference Guide Org Class

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

##### getAvgGetSize()

```

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


Apex Reference Guide Org Class

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


Apex Reference Guide Org Class

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

Signature

```
   public static Long getMaxGetSize()

```

Return Value

Type: Long

Example

In this example the following keys and their corresponding value sizes are inserted. The code fetches the keys: key 1, key 2 and key 4
and returns the maximum key value size from the fetched keys.


Apex Reference Guide Org Class

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


Apex Reference Guide Org Class

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


Apex Reference Guide Org Class

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


Apex Reference Guide Org Class

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


### Apex Reference Guide OrgPartition Class

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

### OrgPartition Class

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
[See Platform Cache Considerations in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_platform_cache_limitations.htm) _Apex Developer Guide_ .

Org cache operations are atomic transactions. If the Apex request that the cache operations run in fails, then all cache operations in that
[request are rolled back. See Platform Cache Internals in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_platform_cache_internals.htm) _Apex Developer Guide_ .


Apex Reference Guide OrgPartition Class

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

```


Apex Reference Guide OrgPartition Class

```
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

```


### Apex Reference Guide Partition Class

```
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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

### Partition Class

Base class of `Cache.OrgPartition` and `Cache.SessionPartition` . Use the subclasses to manage the cache partition
for org caches and session caches.

Namespace

Cache


Apex Reference Guide Partition Class

Cache Key Format for Partition Methods

After you obtain the partition object (an instance of `Cache.OrgPartition` or `Cache.SessionPartition` ), the methods
to add, retrieve, and manage the cache values in a partition take the key name. The key name that you supply to these methods ( `get()`,
`put()`, `remove()`, and `contains()` ) doesn’t include the `namespace.partition` prefix.

IN THIS SECTION:

#### Partition Methods

SEE ALSO:

OrgPartition Class

SessionPartition Class

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

#### Partition Methods The following are methods for Partition .

IN THIS SECTION:

contains(key)
Returns `true` if the cache partition contains a cached value corresponding to the specified key.

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


Apex Reference Guide Partition Class

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


Apex Reference Guide Partition Class

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


Apex Reference Guide Partition Class

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


Apex Reference Guide Partition Class

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


Apex Reference Guide Partition Class

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


Apex Reference Guide Partition Class

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


Apex Reference Guide Partition Class

Return Value

Type: Long

##### getCapacity()

Returns the percentage of cache used of the total capacity for this partition.

Signature

```
   public Double getCapacity()

```

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


Apex Reference Guide Partition Class

Return Value

Type: Long

##### getMaxValueSize()

**Deprecated and available only in API versions 49.0 and earlier.** Returns the maximum item size for keys in the partition, in bytes.

Signature

```
   public Long getMaxValueSize()

```

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


Apex Reference Guide Partition Class

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


Apex Reference Guide Partition Class

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


Apex Reference Guide Partition Class

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


Apex Reference Guide Partition Class

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


Apex Reference Guide Partition Class

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


### Apex Reference Guide Session Class

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


Apex Reference Guide Session Class

Note:

**•** If no default partition is specified in the org, calling a cache method without fully qualifying the key name causes a
`Cache.Session.SessionCacheException` to be thrown.

**•** The `local` prefix in an installed managed package refers to the namespace of the subscriber org and not the package’s
namespace. The cache `put` calls are not allowed in a partition that the invoking class doesn’t own.

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

```


Apex Reference Guide Session Class

```
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

```


Apex Reference Guide Session Class

```
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

```


Apex Reference Guide Session Class

```
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

Session Methods

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

#### Session Constants

The Session class provides a constant that you can use when setting the time-to-live (TTL) value.

**Constant** **Description**

`MAX_TTL_SECS` Represents the maximum amount of time, in seconds, to keep the cached value in the
session cache.


Apex Reference Guide Session Class

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


Apex Reference Guide Session Class

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


Apex Reference Guide Session Class

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


Apex Reference Guide Session Class

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


Apex Reference Guide Session Class

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

```


Apex Reference Guide Session Class

##### getAvgGetSize()

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


Apex Reference Guide Session Class

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


Apex Reference Guide Session Class

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


Apex Reference Guide Session Class

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

##### isAvailable()

```

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


Apex Reference Guide Session Class

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


Apex Reference Guide Session Class

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


Apex Reference Guide Session Class

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


### Apex Reference Guide SessionPartition Class SessionPartition Class

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

```


Apex Reference Guide SessionPartition Class

```
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

```


Apex Reference Guide SessionPartition Class

```
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

```


### Apex Reference Guide Cache Exceptions

```
   </apex:page>

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)_ : Platform Cache

### Cache Exceptions The Cache namespace contains exception classes.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions on page 3784 in the _Apex Developer Guide_ .

### The Cache namespace contains these exceptions.

**Exception** **Thrown when**

`Cache.Session.SessionCacheException` An error occurred while adding or retrieving a value in the session
cache.

`Cache.Session.SessionCacheNoSessionException` An attempt is made to access the cache when the session cache
isn’t available.

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


### Apex Reference Guide Visibility Enum

**Exception** **Thrown when**

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

ApplicationContext Interface
Use this interface to retrieve application context information, such as the application version or URL.

CanvasLifecycleHandler Interface
Implement this interface to control context information and add custom behavior during the application render phase.

ContextTypeEnum Enum
Describes context data that can be excluded from canvas app context data. You specify which context types to exclude in the
`excludeContextTypes()` method in your `CanvasLifecycleHandler` implementation.

EnvironmentContext Interface
Use this interface to retrieve environment context information, such as the app display location or the configuration parameters.


### Apex Reference Guide ApplicationContext Interface

RenderContext Interface
A wrapper interface that is used to retrieve application and environment context information.

Test Class
Contains methods for automated testing of your Canvas classes.

Canvas Exceptions
The `Canvas` namespace contains exception classes.

SEE ALSO:

[Canvas Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/canvas_framework_intro.htm)

### ApplicationContext Interface

Use this interface to retrieve application context information, such as the application version or URL.

Namespace

Canvas

Usage

### The ApplicationContext interface provides methods to retrieve application information about the canvas app that’s being

rendered. Most of the methods are read-only. For this interface, you don’t need to create an implementation. Use the default
implementation that Salesforce provides.

IN THIS SECTION:

#### ApplicationContext Methods ApplicationContext Methods

### The following are methods for ApplicationContext .

IN THIS SECTION:

getCanvasUrl()
Retrieves the fully qualified URL of the canvas app.

getDeveloperName()
Retrieves the internal API name of the canvas app.

getName()
Retrieves the name of the canvas app.

getNamespace()
Retrieves the namespace prefix of the canvas app.

getVersion()
Retrieves the current version of the canvas app.


Apex Reference Guide ApplicationContext Interface

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


Apex Reference Guide ApplicationContext Interface

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


### Apex Reference Guide CanvasLifecycleHandler Interface

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

### CanvasLifecycleHandler Interface

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


Apex Reference Guide CanvasLifecycleHandler Interface

IN THIS SECTION:

#### CanvasLifecycleHandler Methods

SEE ALSO:

_Canvas Developer Guide_ [: Customizing Your App Lifecycle](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/canvas_customizing_app_lifecycle.htm)

#### CanvasLifecycleHandler Methods The following are methods for CanvasLifecycleHandler .

IN THIS SECTION:

##### excludeContextTypes()

Lets the implementation exclude parts of the CanvasRequest context, if the application does not need it.

onRender(renderContext)
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

See the _[Canvas Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/)_ for more information on context information in the Context object that’s provided in the CanvasRequest.


Apex Reference Guide CanvasLifecycleHandler Interface

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

_Canvas Developer Guide_ [: Filtering CanvasRequest Context Data](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/canvas_filtering_context_data.htm)

##### onRender(renderContext)

Invoked when a canvas app is rendered. Provides the ability to set and retrieve canvas application and environment context information
during the application render phase.

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

This method is called whenever signed request or context information is retrieved by the client. See the _[Canvas Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/)_ for more
information on signed request authentication.

Example

This example implementation prints ‘Canvas lifecycle called.’ to the debug log when the canvas app is rendered.

```
   public void onRender(Canvas.RenderContext renderContext) {

      System.debug('Canvas lifecycle called.');

   }

```

SEE ALSO:

_Canvas Developer Guide_ [: Controlling App Behavior](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/canvas_controlling_app_behavior.htm)


### Apex Reference Guide ContextTypeEnum Enum ContextTypeEnum Enum

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


Apex Reference Guide EnvironmentContext Interface

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
[an object (placed on the page layout, for example), you can specify fields to be returned from the related object. See the Canvas Developer](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/)
[Guide for more information on the Record object.](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/)

Use `addEntityField()` to add a field to the list of object fields that are returned in the signed request Record object. By default
the list of fields includes ID. You can add fields by name or add all fields that the user has permission to view by calling
`addEntityField('*')` .

You can inspect the configured list of fields by using Canvas.EnvironmentContext. `getEntityFields()` .


Apex Reference Guide EnvironmentContext Interface

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
an object (placed on the page layout, for example), you can specify fields to be returned from the related object. See the _[Canvas Developer](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/)_
_[Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/)_ for more information on the Record object.

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

```


Apex Reference Guide EnvironmentContext Interface

```
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
an object (placed on the page layout, for example), you can specify fields to be returned from the related object. See the _[Canvas Developer](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/)_
_[Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/)_ for more information on the Record object.


Apex Reference Guide EnvironmentContext Interface

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

##### getLocationUrl()

```

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


Apex Reference Guide EnvironmentContext Interface

Usage

Use this method to get the current custom parameters for the canvas app. The parameters are returned in a JSON string that can be
de-serialized by using the System.JSON. `deserializeUntyped(jsonString)` method.

##### Custom parameters can be modified by using the Canvas.EnvironmentContext. setParametersAsJSON(jsonString) string.

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


### Apex Reference Guide RenderContext Interface

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


Apex Reference Guide RenderContext Interface

IN THIS SECTION:

#### RenderContext Methods RenderContext Methods The following are methods for RenderContext .

IN THIS SECTION:

##### getApplicationContext()

Retrieves the application context information.

getEnvironmentContext()
Retrieves the environment context information.

##### getApplicationContext()

Retrieves the application context information.

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

```


### Apex Reference Guide Test Class

```
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


Apex Reference Guide Test Class

Namespace

Canvas

Usage

Use this class to test your implementation of Canvas.CanvasLifecycleHandler with mock test data. You can create a test
Canvas.RenderContext with mock application and environment context data and use this data to verify that your CanvasLifecycleHandler
is being invoked correctly.

IN THIS SECTION:

#### Test Constants

The Test class provides constants that are used as keys when you set mock application and environment context data.

#### Test Methods

The Test class provides methods for creating test contexts and invoking your CanvasLifecycleHandler with mock data.

SEE ALSO:

_Canvas Developer Guide_ [: Testing Your CanvasLifecycleHandler Implementation](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/canvas_testing_your_canvaslifecyclehandler.htm)

#### Test Constants

The Test class provides constants that are used as keys when you set mock application and environment context data.

When you call Canvas.Test. `mockRenderContext(applicationContextTestValues,`
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


Apex Reference Guide Test Class

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
Canvas.Test. `testCanvasLifecycle(lifecycleHandler, mockRenderContext)` for testing
Canvas.CanvasLifecycleHandler implementations.

Example

The following example creates maps to represent mock application and environment context data and generates a test
Canvas.RenderContext. This test RenderContext can be used in a call to
Canvas.Test. `testCanvasLifecycle(lifecycleHandler, mockRenderContext)` .

```
   Map<String,String> appValues = new Map<String,String>();

   appValues.put(Canvas.Test.KEY_NAMESPACE,'alternateNamespace');

   appValues.put(Canvas.Test.KEY_VERSION,'3.0');

   Map<String,String> envValues = new Map<String,String>();

   envValues.put(Canvas.Test.KEY_DISPLAY_LOCATION,'Chatter');

   envValues.put(Canvas.Test.KEY_LOCATION_URL,'https:// MyDomainName .my.salesforce.com/_ui/core/chatter/ui/ChatterPage');

```


Apex Reference Guide Test Class

```
   Canvas.RenderContext mock = Canvas.Test.mockRenderContext(appValues,envValues);

```

SEE ALSO:

_Canvas Developer Guide_ [: Testing Your CanvasLifecycleHandler Implementation](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/canvas_testing_your_canvaslifecyclehandler.htm)

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

```


### Apex Reference Guide Canvas Exceptions

```
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

    }

   }

```

SEE ALSO:

_Canvas Developer Guide_ [: Testing Your CanvasLifecycleHandler Implementation](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/canvas_testing_your_canvaslifecyclehandler.htm)

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


## Apex Reference Guide ChatterAnswers Namespace

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

See the _[Canvas Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_connect.meta/platform_connect/)_ for additional examples that use CanvasRenderException.

## ChatterAnswers Namespace The ChatterAnswers namespace provides an interface for creating Account records. The following is the interface in the ChatterAnswers namespace.

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


Apex Reference Guide AccountCreator Interface

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

#### AccountCreator Methods The following are methods for AccountCreator .

IN THIS SECTION:

##### createAccount(firstName, lastName, siteAdminId)

Accepts basic user information and creates an Account record. The implementation of this method returns the account ID.

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


## Apex Reference Guide CommerceBuyGrp Namespace

#### AccountCreator Example Implementation

This is an example implementation of the `ChatterAnswers.AccountCreator` interface. The `createAccount` method
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

BuyerGroupEvaluationService Class
The `BuyerGroupEvaluationService` class allows you define and execute custom business logic for dynamically assigning
users to buyer groups. Unlike out-of-the-box configurations limited to account, market, or data segment-based buyer groups, this
service supports extensibility and empowers you to implement tailored buyer group evaluation strategies. It supports both guest
and logged-in user scenarios, enabling highly customizable and context-specific buyer group determination.

BuyerGroupRequest Class
Contains methods to retrieve account and store details used to identify the buyer groups associated with a user.


### Apex Reference Guide BuyerGroupEvaluationService Class

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

CommerceBuyGrp

Consideration

### When implementing the BuyerGroupEvaluationService, remember these key points:

**•** [The number of buyer groups that can be assigned to a user is determined by the limit set in your Salesforce org. See Shopper Buyer](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-data-model-shopper-buyer-groups-accounts-limits.html)
[Groups and Accounts Data Limits Groups.](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-data-model-shopper-buyer-groups-accounts-limits.html)

**•** Supported for B2B stores and D2C stores with custom checkout enabled. It isn't available for stores using managed checkout. See
[Configure Custom Checkout for a B2B or D2C Store.](https://help.salesforce.com/s/articleView?id=commerce.comm_custom_checkout.htm&language=en_US)

**•** Buyer group assignments may not take effect immediately if caching is enabled. To make sure the buyer group extensibility service
functions properly and to avoid caching-related issues, disable both the Salesforce Content Delivery Network (CDN) and Salesforce
Edge Network.

Test these changes in your sandbox org before applying them in production. Go to **My Domain Settings** and disable both options
for enhanced domains.

[See Considerations for the Salesforce CDN and Considerations for Salesforce Edge Network.](https://help.salesforce.com/s/articleView?id=platform.community_builder_cdn_considerations.htm&language=en_US)

Usage

### Use the BuyerGroupEvaluationService to implement custom logic for assigning users to buyer groups. By integrating your

logic with this service, you can evaluate and assign buyer groups in real time based on criteria specific to your organization.

**•** Define Custom Logic—Create your own business rules to evaluate and assign users to appropriate Buyer Groups.

### • Integration with the Service—Integrate your custom logic into the BuyerGroupEvaluationService to dynamically

determine buyer group membership at runtime.

**•** Test and Validate—Test your implementation to ensure it behaves as expected and doesn’t introduce errors or inconsistencies in
group assignments.

Example

For an example implementation of the `CommerceBuyGrp.BuyerGroupEvaluationService` [class, see Commerce Extensibility.](https://github.com/forcedotcom/commerce-extensibility/blob/main/commerce/domain/buyergroup/service/classes/BuyerGroupEvaluationServiceSample.cls)


### Apex Reference Guide BuyerGroupRequest Class

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


Apex Reference Guide BuyerGroupRequest Class

IN THIS SECTION:

##### getAccountId()

Returns the account ID of a user.

##### getStoreId()

Returns the ID of the web store.

##### getRequestContextParameters()

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


### Apex Reference Guide BuyerGroupResponse Class

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

#### BuyerGroupResponse Constructors

BuyerGroupResponse Methods

#### BuyerGroupResponse Constructors

### The following are constructors for BuyerGroupResponse .

IN THIS SECTION:

##### BuyerGroupResponse(buyerGroupIds)

Creates a new instance of the `CommerceBuyGrp.BuyerGroupResponse` class using the specified `buyerGroupIds`
payload parameter.

BuyerGroupResponse()
Creates a new instance of the `CommerceBuyGrp.BuyerGroupResponse` class.

##### **`BuyerGroupResponse(buyerGroupIds)`**

Creates a new instance of the `CommerceBuyGrp.BuyerGroupResponse` class using the specified `buyerGroupIds` payload
parameter.

Signature

```
   public BuyerGroupResponse(Set<String> buyerGroupIds)

```


Apex Reference Guide BuyerGroupResponse Class

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

#### BuyerGroupResponse Methods

##### The following are methods for BuyerGroupResponse .

```

IN THIS SECTION:

##### getBuyerGroupIds()

Retrieves a list of evaluated buyer group IDs assigned to a user.

##### setBuyerGroupIds(buyerGroupIds)

Sets a list of evaluated buyer group IDs assigned to a user.

setError(errorMessage, localizedErrorMessage)
Sets the error message to be returned when the evaluation of buyer group IDs fails.

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


## Apex Reference Guide CommerceExtension Namespace

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

## CommerceExtension Namespace Use the CommerceExtension namespace to define resolution strategies for registered Commerce extensions. The following are the classes in the CommerceExtension namespace.

IN THIS SECTION:

ExtensionInfo Class
Contains static methods to expose extension-related context information.

Resolution Class
Resolution of a resolution strategy, which conditionally invokes default domain logic, logic provided by an extension provider, or no
logic.

ResolutionException Class
Exception indicating a problem with the execution of a resolution strategy.

ResolutionStates Enum
Potential resolution states for a resolution strategy.


### Apex Reference Guide ExtensionInfo Class

ResolutionStrategy Interface
Interface for a resolution strategy.

### ExtensionInfo Class

Contains static methods to expose extension-related context information.

Namespace

CommerceExtension on page 306

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

        }

```

IN THIS SECTION:

#### ExtensionInfo Methods ExtensionInfo Methods

### The following are methods for ExtensionInfo .

IN THIS SECTION:

getClientApiVersion()
Returns the version number of the Client API for the extension context.

getCustomParameterField(fieldName)
Returns a custom parameter field value, if available, for the extension context.


Apex Reference Guide ExtensionInfo Class

##### getLocaleString()

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


### Apex Reference Guide Resolution Class

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

CommerceExtension on page 306

Example

```
   public class TaxServiceExtensionResolverSample extends commercestoretax.TaxService implements

    CommerceExtension.ResolutionStrategy {

      public CommerceExtension.Resolution resolve() {

        // The Sample Extension Provider registered with developer name as

   'tax_extension_provider_for_us' will be selected for execution for en_US locale

        if(CommerceExtension.ExtensionInfo.getLocaleString() == 'en_US') {

           return new CommerceExtension.Resolution('tax_extension_provider_for_us');

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


Apex Reference Guide Resolution Class

IN THIS SECTION:

#### Resolution Constructors

Resolution Methods

#### Resolution Constructors The following are constructors for Resolution .

IN THIS SECTION:

##### Resolution(resolutionState)

Constructor that takes a CommerceExtension.ResolutionStates object as an argument.

##### Resolution(providerName)

Constructor that takes the name of an extension provider as an argument.

##### Resolution()

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


### Apex Reference Guide ResolutionException Class

Signature

```
   public Resolution()

#### Resolution Methods The following are methods for Resolution .

```

IN THIS SECTION:

##### getProviderName()

Returns the name of an extension provider.

##### getResolutionState()

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

CommerceExtension on page 306


Apex Reference Guide ResolutionException Class

IN THIS SECTION:

#### ResolutionException Constructors

ResolutionException Methods

#### ResolutionException Constructors The following are constructors for ResolutionException .

IN THIS SECTION:

##### ResolutionException(errorMessage, exception)

Constructor that takes two arguments: an error message and an exception.

##### ResolutionException(exception)

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

Parameters

```
   errorMessage
```

Type: String

Error message.

```
   exception
```

[Type: Exception](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

Exception.

##### **`ResolutionException(exception)`**

Constructor that takes an exception as an argument,

Signature

```
   public ResolutionException(Exception exception)

```


Apex Reference Guide ResolutionException Class

Parameters

```
   exception
```

[Type: Exception](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

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


### Apex Reference Guide ResolutionStates Enum ResolutionStates Enum

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

CommerceExtension on page 306

Usage

When you implement this interface, you can register your apex class just like an extension provider class. Your class can then conditionally
decide how to handle each extension invocation. You can delegate to a specific extension provider, you can execute default domain
logic, or you can execute no logic at all.

IN THIS SECTION:

#### ResolutionStrategy Methods

ResolutionStrategy Example Implementation

#### ResolutionStrategy Methods

### The following are methods for ResolutionStrategy .

IN THIS SECTION:

resolve()
Returns a resolution object, which indicates how the resolution strategy was resolved. The resolution indicates whether default logic,
extension provider logic, or no logic is executed.


Apex Reference Guide ResolutionStrategy Interface

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

```


## Apex Reference Guide CommerceOrders Namespace

```
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

[See CommerceOrders namespace for more information about the available classes and methods.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_commerceorders.htm)

## CommercePayments Namespace Use the CommercePayments namespace to provide a safe and customizable platform for managing customer payments and

refunds.

## To review CommercePayments use cases and walkthroughs, go to Use Cases for the CommercePayments Namespace. The following are the classes in the CommercePayments namespace.

IN THIS SECTION:

AbstractResponse Class
Contains the normalized response fields from payment gateways that are common to all the other gateway responses.

AbstractTransactionResponse Class
Abstract class for storing normalized information sent from payment gateways about a payment transaction. Holds the common
response fields sent from payment gateways for authorization, sale, capture, and refund transactions.


Apex Reference Guide CommercePayments Namespace

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


Apex Reference Guide CommercePayments Namespace

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

GatewayErrorResponse Class
Use to respond with an error indication following errors from the `PaymentGateway` adapter, such as request-forbidden responses,
custom validation errors, or expired API tokens.

GatewayNotificationResponse Class
When the payment gateway sends a notification to the payments platform, the platform responds with a
`GatewayNotificationResponse` indicating whether the platform succeeded or failed at receiving the notification.

GatewayResponse Interface
Generic payment gateway response interface. This class extends the `CaptureResponse` on page 397,
`AbstractTransactionResponse` on page 324, and `AbstractResponse` on page 320 classes and inherits all their
properties. It has no unique methods or parameters.

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


Apex Reference Guide CommercePayments Namespace

PaymentGatewayNotificationContext Class
Wraps the information related to a gateway notification.

PaymentGatewayNotificationRequest Class
Contains the notification request data from the gateway.

PaymentMethodDetailsResponse Class
This class contains the details about the payment method.

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


### Apex Reference Guide AbstractResponse Class

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

Usage

You must specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes
no arguments. For example:

```
   CommercePayments.AbstractResponse abr = new CommercePayments.AbstractResponse();

```

This class can’t be instantiated on its own. This class implements the GatewayResponse class. Other GatewayResponse classes extend
this class to inherit common properties.

IN THIS SECTION:

#### AbstractResponse Methods AbstractResponse Methods

### The following are methods for AbstractResponse .


Apex Reference Guide AbstractResponse Class

IN THIS SECTION:

##### setGatewayAvsCode(gatewayAvsCode)

Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

##### setGatewayDate(gatewayDate)

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


Apex Reference Guide AbstractResponse Class

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


Apex Reference Guide AbstractResponse Class

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

Type: commercepayments.SalesforceResultCodeInfo on page 502

Description of the Salesforce result code value.

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


### Apex Reference Guide AbstractTransactionResponse Class

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

Usage

Specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes no arguments.
For example:

```
   CommercePayments.AbstractTransactionResponse atr = new

   CommercePayments.AbstractTransactionResponse();

```

IN THIS SECTION:

#### AbstractTransactionResponse Methods AbstractTransactionResponse Methods

### The following are methods for AbstractTransactionResponse .


Apex Reference Guide AbstractTransactionResponse Class

IN THIS SECTION:

##### setAmount(amount)

Sets the transaction amount. Must be a non-negative value.

##### setGatewayAvsCode(gatewayAvsCode)

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


Apex Reference Guide AbstractTransactionResponse Class

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


Apex Reference Guide AbstractTransactionResponse Class

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


### Apex Reference Guide AccountType Enum

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

Type: commercepayments.SalesforceResultCodeInfo on page 502

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

```


### Apex Reference Guide AccountHolderType Enum

**Value** **Description**

```
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

```
   CommercePayments.AddressRequest adr = new CommercePayments.AddressRequest();

```

IN THIS SECTION:

#### AddressRequest Constructors

AddressRequest Properties

AddressRequest Methods

#### AddressRequest Constructors

### The following are constructors for AddressRequest .


Apex Reference Guide AddressRequest Class

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

#### AddressRequest Properties

##### The following are properties for AddressRequest .

IN THIS SECTION:

city
City of the payment method address.

companyName
Company name of the payment method address.

country
Country for the payment method address.


Apex Reference Guide AddressRequest Class

##### postalCode

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


Apex Reference Guide AddressRequest Class

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

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type AddressRequest by determining the equality of external objects in a list. This method

is dynamic and is based on the equals method in Java.

hashCode()
#### Maintains the integrity of lists of type AddressRequest .

toString()
Converts a date to a string.

##### equals(obj)

#### Maintains the integrity of lists of type AddressRequest by determining the equality of external objects in a list. This method is

dynamic and is based on the equals method in Java.

Signature

```
   global Boolean equals(Object obj)

```


### Apex Reference Guide AlternativePaymentMethodRequest Class

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

```


Apex Reference Guide AlternativePaymentMethodRequest Class

```
   String gatewayTokenDetails = (String)alternativePaymentMethod.gatewayTokenDetails;

   String name = (String)alternativePaymentMethod.name;

   String accountId = (String)alternativePaymentMethod.accountId;

   String email = (String)alternativePaymentMethod.email;

```

IN THIS SECTION:

#### AlternativePaymentMethodRequest Constructors AlternativePaymentMethodRequest Properties

AlternativePaymentMethodRequest Methods

#### AlternativePaymentMethodRequest Constructors The following are constructors for AlternativePaymentMethodRequest .

IN THIS SECTION:

##### AlternativePaymentMethodRequest(gatewayToken)

Creates a new instance of the `CommercePayments.AlternativePaymentMethodRequest` class.

##### **`AlternativePaymentMethodRequest(gatewayToken)`**

Creates a new instance of the `CommercePayments.AlternativePaymentMethodRequest` class.

Signature

```
   public AlternativePaymentMethodRequest(String gatewayToken)

```

Parameters

```
   gatewayToken
```

Type: String

A unique, alphanumeric ID, called a token, that a payment gateway generates when it first processes a payment. The token replaces
the actual payment data so that the data is kept secure. This token is stored as encrypted text, and can be used for recurring payments.

#### AlternativePaymentMethodRequest Properties The following are properties for AlternativePaymentMethodRequest .

IN THIS SECTION:

accountId
Salesforce account ID to which this payment method is linked.

email
Email address of the card holder.

gatewayToken
A unique, alphanumeric ID, that a payment gateway generates when it first processes a payment.


Apex Reference Guide AlternativePaymentMethodRequest Class

##### gatewayTokenDetails

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


Apex Reference Guide AlternativePaymentMethodRequest Class

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

##### equals(obj)
#### Maintains the integrity of lists of type AlternativePaymentMethodRequest by determining the equality of external

objects in a list. This method is dynamic and based on the equals method in Java.

hashCode()
#### Maintains the integrity of lists of type AlternativePaymentMethodRequest by determining the uniqueness of the external

object records in a list.

toString()
Converts a date to a string.

##### **`equals(obj)`**

#### Maintains the integrity of lists of type AlternativePaymentMethodRequest by determining the equality of external objects

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


### Apex Reference Guide AlternativePaymentMethodResponse Class

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

#### AlternativePaymentMethodResponse Methods AlternativePaymentMethodResponse Methods

### The following are methods for AlternativePaymentMethodResponse .


Apex Reference Guide AlternativePaymentMethodResponse Class

IN THIS SECTION:

##### setAccountId(accountId)

Sets the ID of the Salesforce payments account to which the payment method is linked.

##### setComments(comments)

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


Apex Reference Guide AlternativePaymentMethodResponse Class

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


### Apex Reference Guide AuditParamsRequest

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

### AuditParamsRequest AuditParamsRequest is used for audit parameters in a transaction request. This is an abstract request class that is extended by

the `BaseRequest` class.

Namespace

CommercePayments

Usage

### AuditParamsRequest is an abstract class that holds attributes related to audit parameters such as email, IP address, MAC address,

and phone number. This class can't be instantiated on its own. All `CommercePayments` request classes extend this class.

IN THIS SECTION:

### AuditParamsRequest Constructors AuditParamsRequest Properties


#### Apex Reference Guide AuditParamsRequest AuditParamsRequest Constructors The following are constructors for AuditParamsRequest .

IN THIS SECTION:

##### AuditParamsRequest(email, macAddress, ipAddress, phone)

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

##### AuditParamsRequest(email, macAddress, ipAddress, phone)

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Signature

```
   AuditParamsRequest(String email, String macAddress, String ipAddress, String phone)

```

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

```
   phone
```

Type: String

Phone number of the client that initiated the request.

#### AuditParamsRequest Properties The following are properties for AuditParamsRequest .

IN THIS SECTION:

email
Email of the client that initiated the request.

ipAddress
The customer’s IP address. Gateways often use this data in risk checks.

macAddress
Mac address of the customer’s device. Gateways often use this data in risk checks.

phone
Phone number of the client that initiated the request.


### Apex Reference Guide AuthApiPaymentMethodRequest Class

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

AuthApiPaymentMethodRequest Constructors

AuthApiPaymentMethodRequest Properties


Apex Reference Guide AuthApiPaymentMethodRequest Class

#### AuthApiPaymentMethodRequest Constructors The following are constructors for AuthApiPaymentMethodRequest .

IN THIS SECTION:

##### AuthApiPaymentMethodRequest(cardPaymentMethodRequest) Constructs a sample cardPaymentMethodRequest . This constructor is intended for test usage and throws an exception if

used outside of the Apex test context.

##### AuthApiPaymentMethodRequest()
#### Constructor for AuthApiPaymentMethodRequest .

##### AuthApiPaymentMethodRequest(cardPaymentMethodRequest) Constructs a sample cardPaymentMethodRequest . This constructor is intended for test usage and throws an exception if used

outside of the Apex test context.

Signature

```
   global AuthApiPaymentMethodRequest(commercepayments.CardPaymentMethodRequest

##### `cardPaymentMethodRequest)`

```

Parameters

##### _`cardPaymentMethodRequest`_

Type: commercepayments.CardPaymentMethodRequest on page 403

Contains information about the card payment method. Used to send information to a gateway adapter during a service call.

##### AuthApiPaymentMethodRequest()

#### Constructor for AuthApiPaymentMethodRequest .

Signature

```
   global AuthApiPaymentMethodRequest()

#### AuthApiPaymentMethodRequest Properties The following are properties for AuthApiPaymentMethodRequest .

```

IN THIS SECTION:

##### cardPaymentMethod

The card payment method object used in a payment method request.

##### cardPaymentMethod

The card payment method object used in a payment method request.


### Apex Reference Guide AuthorizationRequest Class

Signature

```
   global commercepayments.CardPaymentMethodRequest cardPaymentMethod {get; set;}

```

Property Value

Type: commercepayments.CardPaymentMethodRequest on page 403

### AuthorizationRequest Class

Sends information about an authorization request to a gateway adapter during a service call. This class extends the `BaseRequest`
class and inherits all its methods.

Namespace

CommercePayments

Usage

This class contains information about a transaction authorization request. The gateway adapter reads fields from this class while
constructing an authorization JSON request to send to the payment gateway. An object of this class is available by calling
`getPaymentRequest()` in the `PaymentGatewayContext Class` .

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

```


Apex Reference Guide AuthorizationRequest Class

```
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


Apex Reference Guide AuthorizationRequest Class

IN THIS SECTION:

#### AuthorizationRequest Constructors AuthorizationRequest Properties

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

Parameters

```
   amount
```

Type: Double

The amount of the authorization.

#### AuthorizationRequest Properties The following are properties for AuthorizationRequest .

IN THIS SECTION:

accountId
The customer account where the authorization is performed.

amount
The total amount of the authorization. Can be positive or negative.

comments
Comments about the authorization. Users can enter comments to provide additional information.

currencyIsoCode
The ISO currency code for the authorization request.

paymentMethod
The payment method used to process the authorization in the authorization request.


Apex Reference Guide AuthorizationRequest Class

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


Apex Reference Guide AuthorizationRequest Class

Signature

```
   global AuthApiPaymentMethodRequest paymentMethod {get; set;}

```

Property Value

Type: AuthApiPaymentMethodRequest on page 342

#### AuthorizationRequest Methods The following are methods for AuthorizationRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type AuthorizationRequest by determining the equality of external objects in a list. This

method is dynamic and based on the equals method in Java.

##### hashCode()
#### Maintains the integrity of lists of type AuthorizationRequest by determining the uniqueness of the external object in a list.

toString()
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


### Apex Reference Guide AuthorizationResponse Class

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

```


Apex Reference Guide AuthorizationResponse Class

```
            authResponse.setGatewayAuthCode((String)mapOfResponseValues.get('authCode'));

             authResponse.setSalesforceResultCodeInfo(new

   commercepayments.SalesforceResultCodeInfo(commercepayments.SalesforceResultCode.Success));

           } else {

             //Sample returns 200 with refused status in some cases

             system.debug('status - refused');

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


Apex Reference Guide AuthorizationResponse Class

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the authorization occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the authorization request. Maximum length of 255 characters.

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


Apex Reference Guide AuthorizationResponse Class

Parameters

```
   async
```

Type: Boolean

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


Apex Reference Guide AuthorizationResponse Class

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


Apex Reference Guide AuthorizationResponse Class

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


Apex Reference Guide AuthorizationResponse Class

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

PaymentMethodTokenizationResponse on page 442

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


### Apex Reference Guide AuthorizationReversalRequest Class

Parameters

```
   salesforceResultCodeInfo
```

Type: SalesforceResultCodeInfo on page 502

Description of the Salesforce result code value.

Return Value

Type: void

### AuthorizationReversalRequest Class

Sends information about an authorization reversal request to a gateway adapter during a service call.

Namespace

CommercePayments on page 316

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

```


Apex Reference Guide AuthorizationReversalRequest Class

```
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

IN THIS SECTION:

#### AuthorizationReversalRequest Constructors

AuthorizationReversalRequest Properties

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


Apex Reference Guide AuthorizationReversalRequest Class

#### AuthorizationReversalRequest Properties The following are properties for AuthorizationReversalRequest .

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


Apex Reference Guide AuthorizationReversalRequest Class

#### AuthorizationReversalRequest Methods The following are methods for AuthorizationReversalRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type AuthorizationReversalRequest by determining the equality of external objects

in a list. This method is dynamic and based on the equals method in Java.

##### hashCode()
#### Maintains the integrity of lists of type AuthorizationReversalRequest by determining the uniqueness of the external

object in a list.

toString()
Converts a date to a string.

##### equals(obj)

#### Maintains the integrity of lists of type AuthorizationReversalRequest by determining the equality of external objects in a

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

#### Maintains the integrity of lists of type AuthorizationReversalRequest by determining the uniqueness of the external object

in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer


### Apex Reference Guide AuthorizationReversalResponse Class

##### toString()

Converts a date to a string.

Signature

```
   global String toString()

```

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

```


Apex Reference Guide AuthorizationReversalResponse Class

```
        authReversalResponse.setGatewayResultCode('00');

        authReversalResponse.setGatewayResultCodeDescription('Transaction Normal');

        authReversalResponse.setGatewayReferenceNumber('SF'+getRandomNumber(6));

   authReversalResponse.setSalesforceResultCodeInfo(SUCCESS_SALESFORCE_RESULT_CODE_INFO);

        return authReversalResponse;

      }

```

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


Apex Reference Guide AuthorizationReversalResponse Class

Parameters

```
   amount
```

Type: Double

Return Value

Type: void

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


Apex Reference Guide AuthorizationReversalResponse Class

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


Apex Reference Guide AuthorizationReversalResponse Class

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


### Apex Reference Guide BankType Enum

Description of the Salesforce result code value.

Return Value

Type: void

### BankType Enum

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

CommercePayments on page 316

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

```


Apex Reference Guide BankPaymentMethodRequest Class

```
      JSONGenerator jsonGeneratorInstance = JSON.createGenerator(true);

      jsonGeneratorInstance.writeStartObject();

      // Basic fields

      jsonGeneratorInstance.writeStringField('merchantAccount', '{!$Credential.Username}');

      jsonGeneratorInstance.writeStringField('reference', 'Tokenize_' +

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

```


Apex Reference Guide BankPaymentMethodRequest Class

```
   bankPaymentMethod.accountHolderName);

        } else {

           //Add support for other banks if required in future.

        }

        jsonGeneratorInstance.writeEndObject();

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


Apex Reference Guide BankPaymentMethodRequest Class

accountHolderLastName
The last name of the account holder for the bank payment method.

accountHolderName
The name of the account holder for the bank payment method.

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


Apex Reference Guide BankPaymentMethodRequest Class

##### **`accountHolderLastName`**

The last name of the account holder for the bank payment method.

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


Apex Reference Guide BankPaymentMethodRequest Class

Signature

```
   public String accountNumber {get; set;}

```

Property Value

Type: String

##### **`accountType`**

The type for the bank account.

Signature

```
   public commercepayments.AccountType accountType {get; set;}

```

Property Value

Type: commercepayments.AccountType on page 328

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


Apex Reference Guide BankPaymentMethodRequest Class

Signature

```
   public commercepayments.BankType bankType {get; set;}

```

Property Value

Type: commercepayments.BankType on page 365

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


Apex Reference Guide BankPaymentMethodRequest Class

Property Value

Type: String

##### **`standardEntryClassCode`**

The three-letter code that identifies the type of electronic payment transaction being processed within the Automated Clearing House
(ACH) network.

Signature

```
   public commercepayments.StandardEntryClassCode standardEntryClassCode {get; set;}

```

Property Value

Type: commercepayments.StandardEntryClassCode on page 503

#### BankPaymentMethodRequest Methods The following are methods for BankPaymentMethodRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type BankPaymentMethodRequest by determining the equality of external objects in a list.

This method is dynamic and based on the equals method in Java.

hashCode()
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


### Apex Reference Guide BankPaymentMethodResponse Class

##### **`hashCode()`**

Maintains the integrity of lists of type `BankPaymentMethodRequest` .

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

CommercePayments on page 316

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


Apex Reference Guide BankPaymentMethodResponse Class

setBankCode(bankCode)
Sets the unique nine-digit code that identifies the bank code for the bank payment method.

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


Apex Reference Guide BankPaymentMethodResponse Class

Signature

```
   public void setAccountId(String accountId)

```

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

Type: commercepayments.AccountType on page 328

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


Apex Reference Guide BankPaymentMethodResponse Class

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

Type: commercepayments.BankType on page 365

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


Apex Reference Guide BankPaymentMethodResponse Class

Signature

```
   public void setEmail(String email)

```

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


Apex Reference Guide BankPaymentMethodResponse Class

Signature

```
   public void setLast4(String lastFour)

```

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

Type: commercepayments.StandardEntryClassCode on page 503

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

Type: commercepayments.SalesforceResultCodeInfo on page 502

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

Type: commercepayments.NotificationStatus on page 426

Shows whether the payments platform successfully received the notification from the gateway.

Return Value

Type: void

### BasePaymentMethodRequest Class

Abstract class for storing information about payment methods.

Namespace

CommercePayments

Usage

### The BasePaymentMethodRequest class contains fields common to CardPaymentMethodRequest on page 403

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

Type: commercepayments.SalesforceResultCodeInfo on page 502

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

Type: NotificationStatus on page 426

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Return Value

Type: void


### Apex Reference Guide CaptureRequest Class CaptureRequest Class

Represents a capture request. This class extends the `BaseRequest` class and inherits all its methods.

Namespace

CommercePayments on page 316

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

CommercePayments on page 316

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

CommercePayments on page 316

Enum Values

The following are the values of the `commercepayments.CardCategory` enum.

**Value** **Description**

`CreditCard` Shows that the payment method is a credit card.

`DebitCard` Shows that the payment method is a debit card.


### Apex Reference Guide CardPaymentMethodRequest Class CardPaymentMethodRequest Class

Sends data related to a card payment method to a gateway adapter during a service call.

Namespace

CommercePayments on page 316

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

Type: CardCategory on page 402

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

Type: CardCategory on page 402

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


### Apex Reference Guide GatewayErrorResponse Class

Namespace

CommercePayments on page 316

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

### GatewayErrorResponse Class

Use to respond with an error indication following errors from the `PaymentGateway` adapter, such as request-forbidden responses,
custom validation errors, or expired API tokens.

Namespace

CommercePayments on page 316


Apex Reference Guide GatewayErrorResponse Class

Usage

#### Use GatewayErrorResponse to create an object that stores information about error responses sent by the payment gateway

adapter.

Example

#### If GatewayResponse receives an exception rather than a valid request, it calls GatewayErrorResponse to create an error

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

        }

      }

```

IN THIS SECTION:

#### GatewayErrorResponse Constructors GatewayErrorResponse Constructors The following are constructors for GatewayErrorResponse .

IN THIS SECTION:

GatewayErrorResponse(errorCode, errorMessage)
Constructor to create a GatewayErrorResponse object that accepts `errorCode` and `errorMessage` .


### Apex Reference Guide GatewayNotificationResponse Class

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

Namespace

CommercePayments on page 316

Usage

You must specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes
no arguments. For example:

```
   CommercePayments.GatewayNotificationResponse gnr = new

   CommercePayments.GatewayNotificationResponse();

```

When an asynchronous payment gateway sends a notification, the gateway requires the platform to acknowledge that it has either
succeeded or failed in receiving the notification. Payment gateway adapters use this class to construct the acknowledgment response,
### which gateways expect for a notification. GatewayNotificationResponse is the return type of the processNotification

method.


Apex Reference Guide GatewayNotificationResponse Class

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

```


### Apex Reference Guide GatewayResponse Interface

```
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

Return Value

Type: void

### GatewayResponse Interface

Generic payment gateway response interface. This class extends the `CaptureResponse` on page 397,
`AbstractTransactionResponse` on page 324, and `AbstractResponse` on page 320 classes and inherits all their properties.
It has no unique methods or parameters.

Namespace

CommercePayments on page 316


### Apex Reference Guide NotificationClient Class

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


Apex Reference Guide NotificationClient Class

Namespace

CommercePayments on page 316

Usage

Specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes no arguments.
For example:

```
   CommercePayments.NotificationClient ntc = new CommercePayments.NotificationClient();

```

This class is used in asynchronous payment gateway adapters. The notification client contains API for communicating with the payments
##### platform regarding the gateway’s notification. When the gateway sends a notification, the gateway adapter invokes the record
#### method in NotificationClient to request that the platform updates notification details.

Example

The `NotificationSaveResult` class creates a saveResult object to store the result of the save request made to the payment
gateway.

```
   commercepayments.NotificationSaveResult saveResult =

   commercepayments.NotificationClient.record(notification);

```

IN THIS SECTION:

#### NotificationClient Methods NotificationClient Methods The following are methods for NotificationClient .

IN THIS SECTION:

##### record(notification)

Stores the results of a notification request.

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

Type: BaseNotification on page 382


### Apex Reference Guide NotificationSaveResult Class

Return Value

Type: NotificationSaveResult on page 425

### NotificationSaveResult Class

Contains the result of the payment platform’s attempt to record data from the gateway’s notification.

Namespace

CommercePayments on page 316

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

IN THIS SECTION:

##### getErrorMessage()

Gets the error message, if any, from the payment platform regarding its attempt to save the notification sent from the payment
gateway.

getStatusCode()
Gets the status code from the payment platform’s attempt to save the notification sent from the payment gateway.

isSuccess()
Gets the status of whether the payment platform successfully saved the notification sent from the payment gateway.

##### getErrorMessage()

Gets the error message, if any, from the payment platform regarding its attempt to save the notification sent from the payment gateway.


### Apex Reference Guide NotificationStatus Enum

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

Usage

When the gateway sends a notification for a payment request, the payments platform delegates the notification request to the gateway
adapter. First, the adapter evaluates the signature from the notification request. If the signature is valid, the adapter builds a notification
### object to store information about the notification. During this process, the adapter sets the NotificationStatus to Failed

or `Success` based on information from the notification request.

Enum Values

The following are the values of the `commercepayments.NotificationStatus` enum.

**Value** **Description**

`Failed` The payments platform couldn’t receive the notification due to an error.


### Apex Reference Guide PaymentGatewayAdapter Interface

**Value** **Description**

`Success` The payments platform received the notification.

### PaymentGatewayAdapter Interface

`PaymentGatewayAdapters` can implement this interface in order to process requests.

Namespace

CommercePayments on page 316

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

Parameters

```
   var1
```

[Type: commercepayments.PaymentGatewayContext](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_PaymentGatewayContext.htm#apex_class_commerce_payments_PaymentGatewayContext)

You can retrieve the request type and the request from the Context object.

Return Value

Type: commercepayments.GatewayResponse

The response from the payment gateway.

### PaymentGatewayAsyncAdapter Interface

Implement the interface to allow customers to process payments asynchronously.


Apex Reference Guide PaymentGatewayAsyncAdapter Interface

Namespace

CommercePayments on page 316

Usage

##### Implementing an asynchronous adapter also requires the processNotification method from the GatewayNotificationResponse

on page 420 class.

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

#### PaymentGatewayAsyncAdapter Methods

PaymentGatewayAsyncAdapter Example Implementation

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


Apex Reference Guide PaymentGatewayAsyncAdapter Interface

Parameters

```
   paymentGatewayNotificationContext
```

Type: PaymentGatewayNotificationContext on page 432

The `PaymentGatewayNotificationContext` object wraps all the information related to a gateway notification.

Return Value

Type: GatewayNotificationResponse on page 420

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

```


Apex Reference Guide PaymentGatewayAsyncAdapter Interface

```
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

```


### Apex Reference Guide PaymentGatewayContext Class PaymentGatewayContext Class

Wraps the information related to a payment request.

Namespace

CommercePayments on page 316

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

#### PaymentGatewayContext Constructors

PaymentGatewayContext Methods

#### PaymentGatewayContext Constructors

### The following are constructors for PaymentGatewayContext .

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


### Apex Reference Guide PaymentGatewayNotificationContext Class

Parameters

```
   request
```

Type: commercepayments.PaymentGatewayRequest

Raw payload. Sensitive attributes are masked to ensure PCI compliance.

```
   requestType
```

[Type: commercepayments.RequestType Enum](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_commercepayments_RequestType.htm)

Defines the type of request made to the gateway

#### PaymentGatewayContext Methods The following are methods for PaymentGatewayContext .

IN THIS SECTION:

##### getPaymentRequest()

Returns the payment request object.

##### getPaymentRequestType()

Returns the payment request type.

##### getPaymentRequest()

Returns the payment request object.

Signature

```
   global commercepayments.PaymentGatewayRequest getPaymentRequest()

```

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


Apex Reference Guide PaymentGatewayNotificationContext Class

Namespace

CommercePayments on page 316

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

#### PaymentGatewayNotificationContext Methods PaymentGatewayNotificationContext Methods The following are methods for PaymentGatewayNotificationContext .

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

Type: PaymentGatewayNotificationRequest on page 434


### Apex Reference Guide PaymentGatewayNotificationRequest Class PaymentGatewayNotificationRequest Class

Contains the notification request data from the gateway.

Namespace

CommercePayments on page 316

Usage

When the payment gateway sends a notification for a payment request, the payments platform sends the notification request to the
gateway adapter. If the notification payload contains an `eventCode` of `CAPTURE`, the adapter constructs a
`CaptureNotification` . If the notification payload contains an `eventCode` of `REFUND`, the adapter constructs a
`ReferencedRefundNotification` . If the notification payload contains `eventCode` of `AUTHORISATION`, the adapter
constructs a `GatewayNotificationResponse` .

You can obtain a notification request from `PaymentGatewayNotificationContext` on page 432 by invoking its
`getPaymentGatewayNotificationRequest` method.

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

#### PaymentGatewayNotificationRequest Properties

PaymentGatewayNotificationRequest Methods

#### PaymentGatewayNotificationRequest Properties

### The following are properties for PaymentGatewayNotificationRequest .

IN THIS SECTION:

##### requestBody

Body of the notification request sent by the payment gateway.

##### requestBody

Body of the notification request sent by the payment gateway.

Signature

```
   global Blob requestBody {get; set;}

```


### Apex Reference Guide PaymentMethodDetailsResponse Class

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


Apex Reference Guide PaymentMethodDetailsResponse Class

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

#### PaymentMethodDetailsResponse Methods PaymentMethodDetailsResponse Methods The following are methods for PaymentMethodDetailsResponse .

IN THIS SECTION:

##### setAlternativePaymentMethod(alternativePaymentMethod)

Sets the alternative payment method details.

##### setCardPaymentMethod(cardPaymentMethod)

Sets the details about the card payment method.

##### **`setAlternativePaymentMethod(alternativePaymentMethod)`**

Sets the alternative payment method details.

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


### Apex Reference Guide PaymentMethodIdType Enum

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

CommercePayments on page 316

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.PaymentMethodTokenizationRequest pmtr = new

   CommercePayments.PaymentMethodTokenizationRequest();

```

This class holds all the required details about the tokenize request. Gateway adapters read the information in this class while constructing
a tokenization JSON request, which is sent to the payment gateway.


Apex Reference Guide PaymentMethodTokenizationRequest Class

Example

The following code is used within your payment gateway adapter Apex class.

Use the `GatewayResponse` class's `processRequest` method to build responses based on the request type that it receives
from an instance of `PaymentGatewayContext on page 431` . If the request type is Tokenize, `GatewayResponse on`
`page 422` calls the `createTokenizeResponse` method and passes an instance of the
`PaymentMethodTokenizationRequest` class. The passed `PaymentMethodTokenizationRequest` object contains
the address and cardPaymentMethod information that the payment gateway needs to manage the tokenization process. For example:

```
   global commercepayments.GatewayResponse processRequest(commercepayments.paymentGatewayContext

    gatewayContext) {

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

```

Configure the `createTokenizeResponse` method to accept an instance of `PaymentMethodTokenizationRequest` .
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


Apex Reference Guide PaymentMethodTokenizationRequest Class

IN THIS SECTION:

#### PaymentMethodTokenizationRequest Constructors PaymentMethodTokenizationRequest Properties

PaymentMethodTokenizationRequest Methods

#### PaymentMethodTokenizationRequest Constructors The following are constructors for PaymentMethodTokenizationRequest .

IN THIS SECTION:

##### PaymentMethodTokenizationRequest(paymentGatewayId)

Payment gateway ID constructor used with `paymentMethodTokenizationRequest` . This constructor is intended for test
usage and throws an exception if used outside of the Apex test context.

##### PaymentMethodTokenizationRequest()
#### The following are constructors for PaymentMethodTokenizationRequest .

##### PaymentMethodTokenizationRequest(paymentGatewayId)

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

##### PaymentMethodTokenizationRequest()

#### The following are constructors for PaymentMethodTokenizationRequest .

Signature

```
   global PaymentMethodTokenizationRequest()

#### PaymentMethodTokenizationRequest Properties The following are properties for PaymentMethodTokenizationRequest .

```

IN THIS SECTION:

address
The card payment method address to be tokenized.


Apex Reference Guide PaymentMethodTokenizationRequest Class

##### bankPaymentMethod

The bank payment method containing data to be tokenized.

##### cardPaymentMethod

The card payment method containing data to be tokenized.

##### savedByMerchant

Indicates whether the payment method to be tokenized is saved by the marchant ( `true` ) or not ( `false` ).

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

Type: commercepayments.BankPaymentMethodRequest on page 365

##### cardPaymentMethod

The card payment method containing data to be tokenized.

Signature

```
   global commercepayments.CardPaymentMethodRequest cardPaymentMethod {get; set;}

```

Property Value

Type: CardPaymentMethodRequest on page 403

##### **`savedByMerchant`**

Indicates whether the payment method to be tokenized is saved by the marchant ( `true` ) or not ( `false` ).

Signature

```
   public Boolean savedByMerchant {get; set;}

```


Apex Reference Guide PaymentMethodTokenizationRequest Class

Property Value

Type: Boolean

#### PaymentMethodTokenizationRequest Methods The following are methods for PaymentMethodTokenizationRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type PaymentMethodTokenizationRequest by determining the equality of external

objects in a list. This method is dynamic and is based on the equals method in Java.

##### hashCode()
#### Maintains the integrity of lists of type PaymentMethodTokenizationRequest by determining the uniquness of the

external object records in a list.

toString()
Converts a date to a string.

##### equals(obj)

#### Maintains the integrity of lists of type PaymentMethodTokenizationRequest by determining the equality of external objects

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

#### Maintains the integrity of lists of type PaymentMethodTokenizationRequest by determining the uniquness of the external

object records in a list.

Signature

```
   global Integer hashCode()

```


### Apex Reference Guide PaymentMethodTokenizationResponse Class

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

### PaymentMethodTokenizationResponse Class

Gateway response sent by payment gateway adapters for the payment method tokenization request. The response includes the payment
method’s token ID value.

Namespace

CommercePayments on page 316

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

[uses Salesforce encryption to set an encrypted token value for a payment method. The](https://developer.salesforce.com/docs/atlas.en-us.260.0.securityImplGuide.meta/securityImplGuide/fields_about_encrypted_fields.htm) `setGatewayTokenEncrypted` method
is available in Salesforce API v52.0 and later. We recommend using it to ensure your tokenized payment method values are encrypted


Apex Reference Guide PaymentMethodTokenizationResponse Class

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

```


Apex Reference Guide PaymentMethodTokenizationResponse Class

```
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


Apex Reference Guide PaymentMethodTokenizationResponse Class

IN THIS SECTION:

##### setAmount(amount)

Sets the amount for payment tokenization. Can be positive, negative, or zero.

setAsync(async)
Indicates whether the gateway response is received asynchronously ( `true` ) or not ( `false` ). When set to `true`, the saved payment
method remains in a pending state until the async notification is received.

setBankName(bankName)
Sets the bank name for payment tokenization.

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


Apex Reference Guide PaymentMethodTokenizationResponse Class

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


Apex Reference Guide PaymentMethodTokenizationResponse Class

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


Apex Reference Guide PaymentMethodTokenizationResponse Class

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


Apex Reference Guide PaymentMethodTokenizationResponse Class

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


Apex Reference Guide PaymentMethodTokenizationResponse Class

Return Value

Type: void

##### setGatewayToken(gatewayToken)

Sets the gateway token value that the gateway returned.

Signature

```
   global void setGatewayToken(String gatewayToken)

```

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


### Apex Reference Guide PaymentsHttp Class

Parameters

```
   gatewayTokenEncrypted
```

Type: String

[The gateway token that the payment gateway sends following a tokenization request. Salesforce Payments uses Salesforce encryption](https://developer.salesforce.com/docs/atlas.en-us.260.0.securityImplGuide.meta/securityImplGuide/fields_about_encrypted_fields.htm)
to encrypt the token value.

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

Type: SalesforceResultCodeInfo on page 502

Description of the Salesforce result code value.

Return Value

Type: void

### PaymentsHttp Class

Makes an HTTP request to start the interaction with the payment gateway.

Namespace

CommercePayments on page 316

Usage

You must specify the `CommercePayments` namespace when creating an instance of this class. The constructor of this class takes
no arguments. For example:

```
   CommercePayments.PaymentsHttp payhttp = new CommercePayments.PaymentsHttp();

```

IN THIS SECTION:

PaymentsHttp Methods

PaymentsHttp Constructors


### Apex Reference Guide PostAuthApiPaymentMethodRequest Class

#### PaymentsHttp Methods The following are methods for PaymentsHttp . All methods are instance methods.

IN THIS SECTION:

##### send(Request)

Sends an HttpRequest and returns the response.

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

[Type: System.HttpRequest](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_http_httprequest.htm#apex_classes_restful_http_httprequest)

Return Value

[Type: System.HttpResponse](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_http_httpresponse.htm#apex_classes_restful_http_httpresponse)

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


Apex Reference Guide PostAuthApiPaymentMethodRequest Class

Usage

Contains information about the payment method that is used for a postauthorization request. It contains all available payment methods
as fields, but populates only one field for each request. The gateway adapter uses this class when constructing a postauthorization
request. An object of this class is available through the `paymentMethod` field on the `PostAuthorizationRequest Class`
object.

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

PostAuthApiPaymentMethodRequest(AlternativePaymentMethodRequest)
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

Type: commercepayments.CardPaymentMethodRequest on page 403

Contains information about the card payment method. Used to send information to a gateway adapter during a service call.


Apex Reference Guide PostAuthApiPaymentMethodRequest Class

##### **`PostAuthApiPaymentMethodRequest(AlternativePaymentMethodRequest)`**

Constructs a sample `alternativePaymentMethodRequest` . This constructor is intended for test usage and throws an exception
if used outside of the Apex test context.

Signature

```
   global

   PostAuthApiPaymentMethodRequest(commercepayments.AlternativePaymentMethodRequestPaymentMethodRequest)

```

Parameters

```
   alternativePaymentMethodRequest
```

Type: commercepayments.AlternativePaymentMethodRequest on page 403

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

alternativePaymentMethod
The alternative payment method object used in a postauthorizaiton payment method request.

##### **`cardPaymentMethod`**

The card payment method object used in a postauthorizaiton payment method request.

Signature

```
   global commercepayments.CardPaymentMethodRequest cardPaymentMethod {get; set;}

```

Property Value

Type: commercepayments.CardPaymentMethodRequest on page 403


### Apex Reference Guide PostAuthorizationRequest Class

##### **`alternativePaymentMethod`**

The alternative payment method object used in a postauthorizaiton payment method request.

Signature

```
   global commercepayments.AlternativePaymentMethodRequest PaymentMethod {get; set;}

```

Property Value

Type: commercepayments.alternativePaymentMethodRequest

### PostAuthorizationRequest Class

Sends information about a postauthorization request to a gateway adapter during a service call.

Namespace

CommercePayments

Usage

This class extends `[BaseRequest](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_BaseRequest.htm)` and contains information about a transaction postauthorization request. The gateway adapter reads
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

PostAuthorizationRequest(amount)
Constructor for building the amount in a postauthorization request. This constructor is intended for test usage and throws an
exception if used outside of the Apex test context.


Apex Reference Guide PostAuthorizationRequest Class

##### **`PostAuthorizationRequest(amount)`**

Constructor for building the amount in a postauthorization request. This constructor is intended for test usage and throws an exception
if used outside of the Apex test context.

Signature

```
   global PostAuthorizationRequest(Double amount)

```

Parameters

##### _`amount`_

Type: Double

The amount of the authorization.

#### PostAuthorizationRequest Properties

Lists properties for a postauthorizaiton request.

##### The following are properties for a PostAuthorizationRequest .

IN THIS SECTION:

##### accountId

The customer account that is settled when the postauthorization is performed.

##### amount

The total amount of the postauthorization request.

comments
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


### Apex Reference Guide PostAuthorizationResponse Class

Signature

```
   global Double amount {get; set;}

```

Property Value

Type: Double

##### **`comments`**

Comments about the postauthorization. Users can enter comments to provide additional information.

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

Type: AuthApiPaymentMethodRequest on page 342

### PostAuthorizationResponse Class

Response sent by the payment gateway adapter for a postauthorization service.

Namespace

CommercePayments


Apex Reference Guide PostAuthorizationResponse Class

Usage

[This class extends AbstractTransactionResponse. The constructor of this class takes no arguments. For example:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_AbstractTransactionResponse.htm)

```
   CommercePayments.PostAuthorizationResponse authr = new

   CommercePayments.PostAuthorizationResponse();

```

Contains information about the payment gateway’s response following an authorization transaction. The gateway adapter uses the
#### payment gateway’s response to populate the PostAuthorizationResponse fields. The payments platform uses the information

from this class to settle the transaction.

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


Apex Reference Guide PostAuthorizationResponse Class

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

setPaymentMethodDetails(paymentMethodDetails)
Sets details about the payment method.

setPaymentMethodTokenizationResponse(paymentMethodTokenizationResponse)
Sets information from the gateway about the tokenized payment method.

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


Apex Reference Guide PostAuthorizationResponse Class

##### **`setAsync(async)`**

Sets whether the payment capture or authorization is asynchronous ( `True` ) or synchronous ( `False` ). If `True`, then the payment or
payment authorization record created has a status of `Pending` .

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


Apex Reference Guide PostAuthorizationResponse Class

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


Apex Reference Guide PostAuthorizationResponse Class

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

Return Value

Type: void

##### **`setGatewayResultCode(gatewayResultCode)`**

Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

Signature

```
   public void setGatewayResultCode(String gatewayResultCode)

```


Apex Reference Guide PostAuthorizationResponse Class

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


### Apex Reference Guide ReferencedRefundNotification Class

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

PaymentMethodTokenizationResponse on page 442

Gateway response sent by payment gateway adapters for the payment method tokenization request.

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

Type: commercepayments.SalesforceResultCodeInfo on page 502

Description of the Salesforce result code value.

Return Value

Type: void

### ReferencedRefundNotification Class

When a payment gateway sends a notification for a refund transaction, the payment gateway adapter creates the
### ReferencedRefundNotification object to store information about notification.

Namespace

CommercePayments on page 316

Usage

This class is used with asynchronous payments. When a payment gateway sends a notification for a refund transcation, the gateway
### adapter creates an object of type ReferencedRefundNotification to populate the respective values.


Apex Reference Guide ReferencedRefundNotification Class

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

setAmount(amount)
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


Apex Reference Guide ReferencedRefundNotification Class

setId(id)
Sets the ID of a notification sent by the payment gateway.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets Salesforce result code information.

setStatus(status)
Sets the notification status value on the notification object.

##### setAmount(amount)

Sets the transaction amount. Can be positive, negative, or zero.

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


Apex Reference Guide ReferencedRefundNotification Class

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


Apex Reference Guide ReferencedRefundNotification Class

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


Apex Reference Guide ReferencedRefundNotification Class

Return Value

Type: void

##### setId(id)

Sets the ID of a notification sent by the payment gateway.

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

Type: SalesforceResultCodeInfo on page 502

Description of the Salesforce result code value.

Return Value

Type: void

##### setStatus(status)

Sets the notification status value on the notification object.

Signature

```
   global void setStatus(commercepayments.NotificationStatus status)

```


### Apex Reference Guide ReferencedRefundRequest

Parameters

```
   status
```

Type: NotificationStatus on page 426

Indicates whether the payments platform successfully received the notification from the payment gateway.

Return Value

Type: void

### ReferencedRefundRequest

Access information about the referenced refund requests. Extends the `RefundRequest` class.

Namespace

CommercePayments on page 316

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

### ReferencedRefundRequest Constructors ReferencedRefundRequest Properties ReferencedRefundRequest Methods ReferencedRefundRequest Constructors The following are constructors for ReferencedRefundRequest .

IN THIS SECTION:

### ReferencedRefundRequest(amount, paymentId)

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

### ReferencedRefundRequest(amount, paymentId)

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.


#### Apex Reference Guide ReferencedRefundRequest

Parameters

##### _`amount`_

Type: Double

The amount to be debited or captured.

```
   paymentId
```

Type: String

The payment record.

#### ReferencedRefundRequest Properties The following are properties for ReferencedRefundRequest .

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


### Apex Reference Guide ReferencedRefundResponse Class

#### ReferencedRefundRequest Methods The following are methods for ReferencedRefundRequest .

### ReferencedRefundResponse Class

#### The payment gateway adapter sends this response for the ReferencedRefund request type.

Namespace

CommercePayments on page 316

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.ReferencedRefundResponse refr = new

   CommercePayments.ReferencedRefundResponse();

```

IN THIS SECTION:

#### ReferencedRefundResponse Methods ReferencedRefundResponse Methods

### The following are methods for ReferencedRefundResponse .

IN THIS SECTION:

setAmount(amount)
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


Apex Reference Guide ReferencedRefundResponse Class

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


Apex Reference Guide ReferencedRefundResponse Class

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


Apex Reference Guide ReferencedRefundResponse Class

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


### Apex Reference Guide RefundRequest Class

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

Type: commercepayments.SalesforceResultCodeInfo on page 502

Describes the Salesforce result code value.

Return Value

Type: void

### RefundRequest Class

Sends data related to a refund to the payment gateway adapter.

Namespace

CommercePayments on page 476

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.RefundRequest rrq = new CommercePayments.RefundRequest();

```


Apex Reference Guide RefundRequest Class

Example

```
   commercepayments.ReferencedRefundRequest refundRequest = new

   commercepayments.ReferencedRefundRequest(80, pmt.id);

```

IN THIS SECTION:

#### RefundRequest Methods RefundRequest Methods The following are methods for RefundRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type RefundRequest by determining the equality of external objects in a list. This method is

dynamic and is based on the equals method in Java.

##### hashCode()
#### Maintains the integrity of lists of type RefundRequest by determining the uniqueness of the external object records in a list.

##### equals(obj)

#### Maintains the integrity of lists of type RefundRequest by determining the equality of external objects in a list. This method is

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

#### Maintains the integrity of lists of type RefundRequest by determining the uniqueness of the external object records in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer


### Apex Reference Guide RequestType Enum RequestType Enum

Defines the type of payment transaction request made to the payment gateway.

Enum Values

The following are the values of the `commercepayments.RequestType` enum.

**Value** **Description**

`Authorize` Payment authorization request

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


### Apex Reference Guide RetryDecision Enum

**Value** **Description**

`Unknown` The payment gateway error code isn't recognized or isn't mapped to a specific
category.

### RetryDecision Enum

Specifies the retry decision.

Enum Values

The following are the values of the `commercepayments.RetryDecision` enum.

**Value** **Description**

`NonRetriable` The payment operation cannot be retried.

`Retriable` The payment operation can be retried.

### SaleApiPaymentMethodRequest Class

Sends data related to a card payment method to a gateway adapter during a sale service call.

Namespace

CommercePayments on page 316

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


Apex Reference Guide SaleApiPaymentMethodRequest Class

IN THIS SECTION:

##### SaleApiPaymentMethodRequest(cardPaymentMethodRequest)

Sends data related to a card payment method to a gateway adapter during a sale service call.

##### SaleApiPaymentMethodRequest()

Constructor for building a sale payment method request. This constructor is intended for test usage and throws an exception if used
outside of the Apex test context.

##### SaleApiPaymentMethodRequest(cardPaymentMethodRequest)

Sends data related to a card payment method to a gateway adapter during a sale service call.

Signature

```
   global SaleApiPaymentMethodRequest(commercepayments.CardPaymentMethodRequest

##### `cardPaymentMethodRequest)`

```

Parameters

##### _`cardPaymentMethodRequest`_

Type: CardPaymentMethodRequest on page 403

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

standardEntryClassCode
Contains details of the standard entry class code used in a payment method.

##### cardPaymentMethod

Contains details of the card used in a payment method.

Signature

```
   global commercepayments.CardPaymentMethodRequest cardPaymentMethod {get; set;}

```


Apex Reference Guide SaleApiPaymentMethodRequest Class

Property Value

Type: CardPaymentMethodRequest on page 403

##### **`standardEntryClassCode`**

Contains details of the standard entry class code used in a payment method.

Signature

```
   public commercepayments.StandardEntryClassCode standardEntryClassCode {get; set;}

```

Property Value

Type: commercepayments.StandardEntryClassCode on page 503

#### SaleApiPaymentMethodRequest Methods The following are methods for SaleApiPaymentMethodRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type SaleApiPaymentMethodRequest by determining the equality of external objects in

a list. This method is dynamic and is based on the equals method in Java.

hashCode()
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


### Apex Reference Guide SaleNotification Class

##### hashCode()

Maintains the integrity of lists of type `SaleApiPaymentMethodRequest` by determining the uniqueness of the external object
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

### SaleNotification Class When a payment gateway sends a notification for a sale payment, the payment gateway adapter creates the SaleNotification

object to store information about notification.

Namespace

CommercePayments on page 316

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

```


Apex Reference Guide SaleNotification Class

```
      AdyenNotificationRequest notificationRequest =

   AdyenNotificationRequest.parse(request.toString().replace('currency', 'currencyCode'));

      List < AdyenNotificationRequest.NotificationItems > notificationItems =

   notificationRequest.notificationItems;

      AdyenNotificationRequest.NotificationRequestItem notificationRequestItem =

   notificationItems[0].NotificationRequestItem;

      Boolean success = Boolean.valueOf(notificationRequestItem.success);

      String pspReference = notificationRequestItem.pspReference;

      String eventCode = notificationRequestItem.eventCode;

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


Apex Reference Guide SaleNotification Class

IN THIS SECTION:

#### SaleNotification Methods SaleNotification Methods The following are methods for SaleNotification .

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
