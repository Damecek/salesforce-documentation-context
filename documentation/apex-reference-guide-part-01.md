# Apex Reference Guide

> Source: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/salesforce_apex_reference_guide.pdf
> Fetched: 2026-06-02T08:10:56Z
Apex Reference Guide

Version 67.0, Summer ’26

Last updated: May 28, 2026

© Copyright 2000–2026 Salesforce, Inc. All rights reserved. Salesforce is a registered trademark of Salesforce, Inc., as are other
names and marks. Other marks appearing herein may be trademarks of their respective owners.

CONTENTS

Apex Reference Guide **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**

Release Notes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6**
Apex DML Operations **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6**

Apex DML Statements **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6**
ApexPages Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10**

Action Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11**
Component Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12**
IdeaStandardController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14**
IdeaStandardSetController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16**
KnowledgeArticleVersionStandardController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . 20**
Message Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23**
StandardController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27**
StandardSetController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32**
AppLauncher Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43**

AppMenu Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44**
ChangePasswordController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45**
CommunityLogoController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
EmployeeLoginLinkController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
ForgotPasswordController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
IdentityHeaderController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
LoginFormController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
SelfRegisterController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
SocialLoginController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47**
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
AuthToken Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95**
CommunitiesUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100**
ConfigurableSelfRegHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101**

**Contents**

ConfirmUserRegistrationHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106**
ConnectedAppPlugin Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109**
CustomOneTimePasswordDeliveryHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . 116**
CustomOneTimePasswordDeliveryResult Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118**
ExternalClientAppOauthHandler Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118**
GeneratedUserData Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121**
HeadlessSelfRegistrationHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126**
HeadlessUserDiscoveryHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129**
HeadlessUserDiscoveryResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134**
HttpCalloutMockUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136**
IntegratingAppType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137**
InvocationContext Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137**
JsonValueOutput Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138**
JWS Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141**
JWT Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144**
JWTBearerTokenExchange Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150**
JWTUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155**
LightningLoginEligibility Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158**
LoginDiscoveryHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158**
LoginDiscoveryMethod Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166**
MyDomainLoginDiscoveryHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166**
Oauth2TokenExchangeHandler Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170**
OAuth2TokenExchangeType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172**
OAuthRefreshResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173**
OauthToken Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176**
OauthTokenType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177**
RegistrationHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177**
SamlJitHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183**
SessionManagement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187**
SessionLevel Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199**
TokenValidationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199**
UserData Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206**
VerificationAction Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213**
VerificationMethod Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214**
VerificationPolicy Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214**
VerificationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215**
Auth Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218**
Cache Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220**

CacheBuilder Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220**
Org Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222**
OrgPartition Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240**
Partition Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243**
Session Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258**
SessionPartition Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274**

**Contents**

Cache Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277**
Visibility Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278**
Canvas Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279**

ApplicationContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279**
CanvasLifecycleHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283**
ContextTypeEnum Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285**
EnvironmentContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286**
RenderContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 292**
Test Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294**
Canvas Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 298**
ChatterAnswers Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299**

AccountCreator Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299**
CommerceBuyGrp Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301**

BuyerGroupEvaluationService Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301**
BuyerGroupRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303**
BuyerGroupResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304**
CommerceExtension Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 307**

ExtensionInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 307**
Resolution Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309**
ResolutionException Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312**
ResolutionStates Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314**
ResolutionStrategy Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314**
CommerceOrders Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316**
CommercePayments Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317**

AbstractResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 320**
AbstractTransactionResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324**
AccountType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329**
AccountHolderType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329**
AddressRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329**
AlternativePaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 334**
AlternativePaymentMethodResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337**
AuditParamsRequest **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341**
AuthApiPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343**
AuthorizationRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 344**
AuthorizationResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 350**
AuthorizationReversalRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 357**
AuthorizationReversalResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 361**
BankType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 366**
BankPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 366**
BankPaymentMethodResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374**
BaseApiPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 380**
BaseNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383**
BasePaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 389**
BaseRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 390**

**Contents**

CaptureNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 391**
CaptureRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 397**
CaptureResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398**
CardCategory Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 403**
CardPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 404**
CardPaymentMethodResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 410**
CardType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 418**
CustomMetadataTypeInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 418**
EnhancedPaymentDataInput Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 419**
GatewayErrorResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425**
GatewayNotificationResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 426**
GatewayResponse Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429**
NotificationClient Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 430**
NotificationSaveResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 431**
NotificationStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432**
PaymentGatewayAdapter Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 433**
PaymentGatewayAsyncAdapter Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434**
PaymentGatewayContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437**
PaymentGatewayNotificationContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 439**
PaymentGatewayNotificationRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440**
PaymentMethodDetailsResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 442**
LineItemInput Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 443**
PaymentMethodIdType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 450**
PaymentMethodTokenizationRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 450**
PaymentMethodTokenizationResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455**
PaymentsHttp Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 464**
PostAuthApiPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 465**
PostAuthorizationRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468**
PostAuthorizationResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 470**
ReferencedRefundNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 477**
ReferencedRefundRequest **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 482**
ReferencedRefundResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484**
RefundRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489**
RequestType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 490**
RetryCategory Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 491**
RetryDecision Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 491**
SaleApiPaymentMethodRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 492**
SaleNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495**
SaleRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 502**
SaleResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 511**
SalesforceResultCode Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 518**
SalesforceResultCodeInfo **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 519**
StandardEntryClassCode Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 520**
TokenizeNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 520**

**Contents**

CommerceTax Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 528**

AbstractTransactionResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 529**
AddressesResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 535**
AddressResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 538**
AmountDetailsResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 539**
CalculateTaxRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 541**
CalculateTaxResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 546**
CalculateTaxType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 553**
CustomTaxAttributesResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 554**
ErrorResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 555**
HeaderTaxAddressesRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 557**
ImpositionResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 561**
JurisdictionResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 563**
LineItemResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 567**
LineTaxAddressesRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 573**
RequestType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 577**
ResultCode Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 577**
RuleDetailsResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 577**
TaxAddressesRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 580**
TaxAddressRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 584**
TaxApiException Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 590**
TaxCustomerDetailsRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 591**
TaxDetailsResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 595**
TaxEngineAdapter Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 602**
TaxEngineContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 628**
TaxLineItemRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 630**
TaxSellerDetailsRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 637**
TaxTransactionRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 639**
TaxTransactionStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 646**
TaxTransactionType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 646**
ComplianceMgmt Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 647**
Compression Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 647**

Level Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 648**
Method Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 648**
ZipEntry Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 648**
ZipReader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 654**
ZipWriter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 657**
Compression Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 663**
ConnectApi Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 663**

ActionLinks Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 669**
Announcements Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 677**
BotVersionActivation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 683**
CdpActivation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 685**
CdpActivationExternalPlatform Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 689**

**Contents**

CdpActivationTarget Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 691**
CdpAudienceDMO Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 694**
CdpCalculatedInsight Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 695**
CdpConnection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 701**
CdpDataSpace Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 702**
CdpDataStreams Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 703**
CdpIdentityResolution Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 704**
CdpMachineLearning Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 708**
CdpQuery Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 709**
CdpSegment Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 767**
Chatter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 778**
ChatterFavorites Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 783**
ChatterFeeds Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 805**
ChatterGroups Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1208**
ChatterMessages Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1253**
ChatterUsers Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1277**
Clm Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1313**
CommerceBuyerExperience Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1314**
CommerceCart Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1372**
CommerceCatalog Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1425**
CommerceCatalogManagement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1453**
CommercePromotions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1456**
CommerceQuotes Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1458**
CommerceSearch Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1462**
CommerceSearchConnectFamily Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1469**
CommerceSearchSettings Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1473**
CommerceStorePricing Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1476**
CommerceWishlist Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1482**
Communities Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1500**
CommunityModeration Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1503**
ContentHub Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1532**
ConversationApplicationDefinition Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1607**
Datacloud Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1608**
EinsteinLLM Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1613**
EmailMergeFieldService Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1617**
EmployeeProfiles Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1617**
Exchanges Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1626**
ExtendedCommerceDelivery Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1628**
ExternalEmailServices Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1629**
ExternalManagedAccount Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1630**
FieldService Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1633**
FlowApprovalProcesses Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1635**
FulfillmentOrder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1636**
IBusinessObjectivesAndRecsFamily Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1641**

**Contents**

Knowledge Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1646**
LightningScheduler Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1651**
ManagedContent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1656**
ManagedContentChannels Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1688**
ManagedContentDelivery Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1692**
ManagedContentSpaces Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1717**
ManagedTopics Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1722**
MarketingIntegration Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1736**
Mentions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1738**
Missions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1744**
NamedCredentials Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1749**
NavigationMenu Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1767**
NextBestAction Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1771**
OmnichannelInventoryService Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1777**
OMSAnalytics Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1785**
OptimizationFiles Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1790**
Orchestration Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1792**
OrderPaymentSummary Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1794**
OrderSummary Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1795**
OrderSummaryCreation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1808**
Organization Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1809**
PardotBusinessUnitContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1810**
Payments Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1811**
Personalization Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1817**
PickTicket Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1829**
QuestionAndAnswers Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1830**
Recommendations Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1834**
RecordFilterCriteriaFamily Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1894**
Records Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1895**
RecordUi Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1897**
RegisterGuestBuyer Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1898**
Repricing Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1899**
ReturnOrder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1902**
Routing Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1904**
SalesforceInbox Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1909**
Search Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1910**
Sites Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1921**
SmartDataDiscovery Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1922**
SocialEngagement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1922**
Surveys Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1933**
TaxPlatform Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1934**
Topics Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1935**
UserProfiles Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1973**
Zones Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1983**

**Contents**

ConnectApi Input Classes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1993**
ConnectApi Output Classes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2192**
ConnectApi Enums **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2643**
ConnectApi Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2687**
ConnectApi Utilities **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2688**
ConnectApi Release Notes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2688**
Context Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2689**
Database Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2689**

Batchable Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2690**
BatchableContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2692**
Cursor Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2693**
CursorFetchResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2696**
DeletedRecord Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2697**
DeleteResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2698**
DMLOptions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2700**
DmlOptions.AssignmentRuleHeader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2703**
DMLOptions.DuplicateRuleHeader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2705**
DmlOptions.EmailHeader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2707**
DuplicateError Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2709**
EmptyRecycleBinResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2711**
Error Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2713**
GetDeletedResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2714**
GetUpdatedResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2716**
LeadConvert Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2717**
LeadConvertResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2728**
MergeResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2730**
PaginationCursor Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2732**
QueryLocator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2734**
QueryLocatorIterator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2735**
SaveResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2737**
UndeleteResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2739**
UpsertResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2741**
Datacloud Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2742**

AdditionalInformationMap Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2743**
DuplicateResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2744**
FieldDiff Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2749**
FindDuplicates Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2750**
FindDuplicatesByIds Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2753**
FindDuplicatesResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2755**
MatchRecord Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2758**
MatchResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2760**
DataRetrieval Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2762**
DataSource Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2763**

AsyncDeleteCallback Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2765**

**Contents**

AsyncSaveCallback Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2766**
AuthenticationCapability Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2767**
AuthenticationProtocol Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2767**
Capability Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2768**
Column Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2769**
ColumnSelection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2792**
Connection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2794**
ConnectionParams Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2799**
DataSourceUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2803**
DataType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2804**
DeleteContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2805**
DeleteResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2806**
Filter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2809**
FilterType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2811**
IdentityType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2812**
Order Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2812**
OrderDirection Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2815**
Provider Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2815**
QueryAggregation Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2817**
QueryContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2817**
QueryUtils Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2819**
ReadContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2822**
SearchContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2823**
SearchUtils Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2825**
Table Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2826**
TableResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2830**
TableSelection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2836**
UpsertContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2838**
UpsertResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2839**
DataSource Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2842**
DataWeave Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2842**

Result Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2843**
Script Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2844**
Dom Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2846**

Document Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2847**
XmlNode Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2849**
XmlNodeType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2860**
embeddedai Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2860**

ApexMap Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2860**
RecordApexRepresentation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2863**
EventBus Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2866**

ChangeEventHeader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2867**
EventPublishFailureCallback Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2872**
EventPublishSuccessCallback Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2874**

**Contents**

FailureResult Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2875**
SuccessResult Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2875**
TestBroker Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2876**
TriggerContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2878**
ExternalService Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2881**
Flow Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2881**

Interview Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2881**
Flowtesting Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2886**
flowuiruntime Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2886**

ComplexObjectFieldDetails Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2886**
PropertyTypeDetails Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2886**
ToastLink Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2887**
FormulaEval Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2887**

FormulaBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2887**
FormulaGlobal Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2892**
FormulaInstance Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2893**
FormulaReturnType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2895**
fsccashflow Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2895**

FSCCashFlowUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2896**
Functions Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2906**

Function Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2907**
FunctionCallback Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2911**
FunctionErrorType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2912**
FunctionInvocation Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2913**
FunctionInvocationError Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2915**
FunctionInvocationStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2917**
FunctionInvokeMock Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2917**
MockFunctionInvocationFactory Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2920**
ise_bots_apex Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2922**

DynamicMenuItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2922**
IssueCreditMemo Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2926**
ind_mfg_sample_mgmt_apex Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2926**
industriesNlpSvc **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2927**

NlpResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2927**
NlpSummarizationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2928**
IndustriesDigitalLending Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2929**
Invocable Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2929**

Action Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2930**
Action.AdditionalAttribute Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2937**
Action.DescribeResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2942**
Action.Error Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2949**
Action.GenericType Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2951**
Action.InputParameter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2952**
Action.OutputParameter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2958**

**Contents**

Action.PicklistValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2962**
Action.Result Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2964**
InvoiceWriteOff Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2967**
IsvPartners Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2967**

AppAnalytics Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2967**
KbManagement Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2969**

PublishingService Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2969**
LxScheduler Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2981**

GetAppointmentCandidatesInput Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2982**
GetAppointmentCandidatesInputBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . 2984**
GetAppointmentSlotsInput Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2991**
GetAppointmentSlotsInputBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2994**
SchedulerResources Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3001**
SkillRequirement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3006**
SkillRequirementBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3006**
WorkType Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3007**
WorkTypeBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3008**
ServiceResourceScheduleHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3012**
ServiceAppointmentRequestInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3015**
ServiceResourceInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3019**
ServiceResourceSchedule Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3022**
UnavailableTimeslot Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3023**
Messaging Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3025**

AttachmentRetrievalOption Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3027**
ActionableNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3027**
ActionableNotification.Builder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3030**
ActionError Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3033**
ActionResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3033**
ActionResult.Builder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3035**
CustomNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3037**
Email Class (Base Email Methods) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3044**
EmailFileAttachment Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3047**
InboundEmail Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3050**
InboundEmail.AuthenticationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3056**
InboundEmail.AuthenticationResultField Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 3058**
InboundEmail.BinaryAttachment Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3059**
InboundEmail.TextAttachment Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3061**
InboundEmailResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3064**
InboundEnvelope Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3065**
MassEmailMessage Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3066**
InboundEmail.Header Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3069**
PushNotification Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3070**
PushNotificationPayload Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3073**
NotificationActionHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3076**

**Contents**

RenderEmailTemplateBodyResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3079**
RenderEmailTemplateError Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3081**
SendEmailError Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3082**
SendEmailResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3084**
SingleEmailMessage Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3085**
Metadata Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3102**

AnalyticsCloudComponentLayoutItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3105**
ConsoleComponent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3109**
Container Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3111**
CustomConsoleComponents Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3114**
CustomMetadata Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3115**
CustomMetadataValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3118**
DeployCallback Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3120**
DeployCallbackContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3121**
DeployContainer Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3123**
DeployDetails Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3125**
DeployMessage Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3127**
DeployProblemType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3132**
DeployResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3132**
DeployStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3140**
FeedItemTypeEnum Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3141**
FeedLayout Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3142**
FeedLayoutComponent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3146**
FeedLayoutComponentType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3148**
FeedLayoutFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3148**
FeedLayoutFilterPosition Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3150**
FeedLayoutFilterType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3151**
Layout Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3151**
LayoutColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3159**
LayoutHeader Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3160**
LayoutItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3160**
LayoutSection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3165**
LayoutSectionStyle Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3168**
Metadata Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3168**
MetadataType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3170**
MetadataValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3170**
MiniLayout Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3171**
Operations Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3172**
PlatformActionList Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3176**
PlatformActionListContextEnum Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3178**
PlatformActionListItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3179**
PlatformActionTypeEnum Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3181**
PrimaryTabComponents Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3181**
QuickActionList Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3183**

**Contents**

QuickActionListItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3184**
RelatedContent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3185**
RelatedContentItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3187**
RelatedList Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3188**
RelatedListItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3189**
ReportChartComponentLayoutItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3192**
ReportChartComponentSize Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3196**
SidebarComponent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3196**
SortOrder Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3201**
StatusCode Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3201**
SubtabComponents Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3201**
SummaryLayoutStyleEnum Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3203**
SummaryLayout Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3203**
SummaryLayoutItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3206**
UiBehavior Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3209**
PlaceQuote Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3209**
Pref_center Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3209**

LoadFormData Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3210**
LoadParameters Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3216**
PreferenceCenterApexHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3217**
SubmitFormData Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3218**
SubmitParameters Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3222**
TokenType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3223**
TokenUtility Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3223**
ValidationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3226**
Process Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3226**

Plugin Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3227**
PluginDescribeResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3229**
PluginDescribeResult.InputParameter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3232**
PluginDescribeResult.OutputParameter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 3235**
PluginDescribeResult.ParameterType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3238**
PluginRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3239**
PluginResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3239**
QuickAction Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3240**

DescribeAvailableQuickActionResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3241**
DescribeLayoutComponent Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3243**
DescribeLayoutItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3244**
DescribeLayoutRow Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3247**
DescribeLayoutSection Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3248**
DescribeQuickActionDefaultValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3251**
DescribeQuickActionParameter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3252**
DescribeQuickActionResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3255**
QuickActionDefaults Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3272**
QuickActionDefaultsHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3274**

**Contents**

QuickActionRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3279**
QuickActionResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3282**
SendEmailQuickActionDefaults Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3284**
renew_assets_summary Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3286**
Reports Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3287**

AggregateColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3290**
BucketField Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3292**
BucketFieldValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3299**
BucketType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3302**
ColumnDataType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3303**
ColumnSortOrder Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3304**
CrossFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3304**
CsfGroupType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3309**
DateGranularity Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3310**
DetailColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3310**
Dimension Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3312**
EvaluatedCondition Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3312**
EvaluatedConditionOperator Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3316**
FilterOperator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3316**
FilterValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3317**
FormulaType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3318**
GroupingColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3319**
GroupingInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3320**
GroupingValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3322**
NotificationAction Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3324**
NotificationActionContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3325**
ReportCsf Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3327**
ReportCurrency Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3336**
ReportDataCell Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3337**
ReportDescribeResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3338**
ReportDetailRow Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3339**
ReportDivisionInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3339**
ReportExtendedMetadata Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3340**
ReportFact Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3342**
ReportFactWithDetails Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3343**
ReportFactWithSummaries Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3344**
ReportFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3345**
ReportFormat Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3351**
ReportFilterType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3352**
ReportInstance Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3352**
ReportManager Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3355**
ReportMetadata Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3360**
ReportResults Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3379**
ReportScopeInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3382**

**Contents**

ReportScopeValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3383**
ReportType Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3384**
ReportTypeColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3385**
ReportTypeColumnCategory Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3387**
ReportTypeMetadata Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3389**
SortColumn Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3390**
StandardDateFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3392**
StandardDateFilterDuration Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3395**
StandardDateFilterDurationGroup Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3397**
StandardFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3398**
StandardFilterInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3400**
StandardFilterInfoPicklist Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3401**
StandardFilterType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3402**
SummaryValue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3403**
ThresholdInformation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3404**
TopRows Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3405**
Reports Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3408**
RevSignaling Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3409**
RevSalesTrxn Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3409**
RichMessaging Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3409**

AbstractTiming Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3411**
AddressableContact Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3411**
AuthRequestHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3414**
AuthRequestResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3417**
AuthRequestResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3419**
AuthRequestResultStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3421**
DeferredTiming Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3421**
MessageDefinitionInputParameter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3423**
PaymentItemStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3427**
PaymentLineItem Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3427**
PaymentMethod Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3433**
PostalAddress Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3434**
ProcessFormHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3438**
ProcessPaymentHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3439**
ProcessPaymentRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3441**
ProcessPaymentResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3444**
ProcessPaymentResultStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3446**
RecurringTiming Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3446**
ShippingMethod Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3450**
TimeSlotOption Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3455**
TimingIntervalUnit Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3458**
TimingType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3458**
RulesAppln Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3458**
runtime_industries_cpq Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3459**

**Contents**

runtime_industries_insurance Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3459**
Schema Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3459**

ChildRelationship Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3460**
DataCategory Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3462**
DataCategoryGroupSobjectTypePair Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3464**
DescribeColorResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3466**
DescribeDataCategoryGroupResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3468**
DescribeDataCategoryGroupStructureResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . 3470**
DescribeFieldResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3472**
DescribeIconResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3489**
DescribeSObjectResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3492**
DescribeTabResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3514**
DescribeTabSetResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3517**
DisplayType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3521**
FieldDescribeOptions Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3522**
FieldSet Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3522**
FieldSetMember Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3526**
PicklistEntry Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3529**
RecordTypeInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3530**
SOAPType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3533**
SObjectDescribeOptions Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3534**
SObjectField Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3535**
SObjectType Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3536**
Search Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3540**

KnowledgeSuggestionFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3540**
QuestionSuggestionFilter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3545**
SearchResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3548**
SearchResults Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3550**
SuggestionOption Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3551**
SuggestionResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3553**
SuggestionResults Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3553**
setup_flow_performance Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3554**

FlowPerformanceSetupDetails Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3555**
Sfc Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3555**

ContentDownloadContext Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3555**
ContentDownloadHandler Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3556**
ContentDownloadHandlerFactory Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3557**
Sfdc_Checkout Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3559**

AsyncCartProcessor Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3559**
B2BCheckoutController Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3560**
IntegrationInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3561**
IntegrationStatus Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3563**
IntegrationStatus.Status Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3563**
Sfdc_Enablement Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3564**

**Contents**

LearningEvaluation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3564**
LearningEvaluationResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3566**
LearningItemEvaluationHandler Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3568**
LearningItemProgressStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3570**
LearningItemSerializeDeserializer Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3571**
sfdc_surveys Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3574**

SurveyInvitationLinkShortener Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3574**
Example Implementation to Associate SurveySubjects with SurveyInvitation and
SurveyResponses **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3576**
Site Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3577**

UrlRewriter Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3578**
Site Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3579**
Slack Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3579**
Support Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3581**

EmailTemplateSelector Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3581**
MilestoneTriggerTimeCalculator Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3583**
System Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3585**

AccessLevel Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3593**
AccessType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3596**
Address Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3596**
Answers Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3602**
ApexPages Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3603**
Approval Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3606**
Assert Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3618**
AsyncInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3631**
AsyncOptions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3632**
Blob Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3634**
Boolean Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3636**
BusinessHours Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3638**
CallbackStatus Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3641**
Callable Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3642**
Cases Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3644**
Collator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3648**
Comparable Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3650**
Comparator Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3652**
Continuation Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3655**
Cookie Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3659**
Crypto Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3666**
Custom Metadata Type Methods **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3692**
Custom Settings Methods **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3696**
Database Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3706**
Date Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3804**
Datetime Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3815**
Decimal Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3838**

**Contents**

Domain Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3852**
DomainCreator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3854**
DomainParser Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3859**
DomainType Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3860**
Double Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3861**
EmailMessages Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3865**
EncodingUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3868**
Enum Methods **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3872**
EventBus Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3873**
Exception Class and Built-In Exceptions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3882**
ExternalServiceTest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3887**
FeatureManagement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3888**
Finalizer Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3893**
FinalizerContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3895**
FlexQueue Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3896**
Formula Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3899**
FormulaRecalcFieldError Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3901**
FormulaRecalcResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3902**
Http Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3904**
HttpCalloutMock Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3905**
HttpRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3906**
HttpResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3915**
Id Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3922**
Ideas Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3928**
InstallHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3933**
Integer Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3936**
IntegrationTest Class (Developer Preview) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3939**
JSON Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3940**
JSONGenerator Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3947**
JSONParser Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3960**
JSONToken Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3973**
Label Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3973**
Limits Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3976**
List Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3992**
Location Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4007**
LoggingLevel Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4011**
Long Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4011**
Map Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4013**
Matcher Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4026**
Math Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4038**
Messaging Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4063**
MultiStaticResourceCalloutMock Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4072**
Network Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4074**
Object Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4080**

**Contents**

OrgLimit Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4082**
OrgLimits Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4084**
PageReference Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4086**
Packaging Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4098**
Pattern Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4099**
ParentJobResult Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4103**
Queueable Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4103**
QueueableContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4106**
QueueableDuplicateSignature Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4106**
QueueableDuplicateSignature.Builder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4107**
QuickAction Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4111**
Quiddity Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4115**
RemoteObjectController **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4116**
Request Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4120**
ResetPasswordResult Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4121**
RestContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4122**
RestRequest Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4123**
RestResponse Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4129**
SandboxPostCopy Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4133**
Schedulable Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4135**
SchedulableContext Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4136**
Schema Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4137**
Search Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4142**
Security Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4147**
SelectOption Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4151**
Set Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4157**
Site Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4168**
SObject Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4190**
SObjectAccessDecision Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4217**
SoqlStubProvider Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4220**
StaticResourceCalloutMock Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4223**
String Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4226**
StubProvider Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4303**
System Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4305**
Test Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4333**
Time Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4355**
TimeZone Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4359**
Trigger Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4363**
TriggerOperation Enum **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4366**
Type Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4366**
UninstallHandler Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4374**
URL Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4376**
UserInfo Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4387**
UserManagement Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4396**

**Contents**

UUID Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4416**
Version Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4418**
WebServiceCallout Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4422**
WebServiceMock Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4423**
XmlStreamReader Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4425**
XmlStreamWriter Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4439**
TerritoryMgmt Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4446**

OpportunityTerritory2AssignmentFilter Global Interface **. . . . . . . . . . . . . . . . . . . . . . 4446**
TxnSecurity Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4450**

Event Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4450**
EventCondition Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4454**
AsyncCondition Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4456**
PolicyCondition Interface **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4457**
UserProvisioning Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4459**

ConnectorTestUtil Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4459**
UserProvisioningLog Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4461**
UserProvisioningPlugin Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4463**
VisualEditor Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4467**

DataRow Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4468**
DesignTimePageContext Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4471**
DynamicPickList Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4473**
DynamicPickListRows Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4476**
Wave Namespace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4481**

QueryBuilder Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4481**
QueryNode Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4485**
ProjectionNode Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4489**
Templates Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4492**
TemplatesSearchOptions Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4495**
Appendices **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4497**

Apex Versioned Behavior Changes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4498**
Shipping Invoice Example **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4508**
Reserved Keywords **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4519**
Documentation Typographical Conventions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4521**

APEX REFERENCE GUIDE

Apex is a strongly typed, object-oriented programming language that allows developers to execute flow and transaction control
statements on the Salesforce Platform server, in conjunction with calls to the API. This reference guide includes built-in Apex classes,
interfaces, enums, and exceptions, grouped by namespace. It also includes Apex DML statements to insert, update, merge, delete, and
restore data in Salesforce.

[For information on the Apex development process, see Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dev_guide.htm)

Note: In API version 51.0 and earlier, Apex Reference information was included in the Apex Developer Guide in the "Apex Language
Reference" section.

Keep these guidelines in mind regarding API version usage:

**•** Salesforce strongly recommends that you use the latest available API version.

**•** If you can't upgrade to the latest version yet, use API versions released in the past three years, for improved performance, security,
and compatibility.

**•** To reduce complexity, consolidate your Apex codebase to use the minimal number of API versions, ideally, just one API version.

For a non-exhaustive list of major Apex behavior changes across API versions, organized by version number, see Apex Versioned Behavior
Changes on page 4498.

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


Apex Reference Guide

CommerceBuyGrp Namespace
The `CommerceBuyGrp` namespace provides classes and methods for retrieving information about the buyer groups associated
with a user.

CommerceExtension Namespace
Use the `CommerceExtension` namespace to define resolution strategies for registered Commerce extensions.

CommerceOrders Namespace
The `CommerceOrders` namespace provides classes and methods to place orders with integrated pricing, configuration, and
validation.

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


Apex Reference Guide

EventBus Namespace
The `EventBus` namespace provides classes and methods for platform events and Change Data Capture events.

ExternalService Namespace
The `ExternalService` namespace provides dynamically generated Apex service interfaces and Apex classes for complex
object data types.

Flow Namespace
The `Flow` namespace provides a class for advanced access to flows from Apex such as from Visualforce controllers and asynchronous
Apex.

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

IssueCreditMemo Namespace
The IssueCreditMemo namespace provides classes to create and apply credit memos against invoices or invoice lines based on
dispute adjustments.

ind_mfg_sample_mgmt_apex Namespace
The ind_mfg_sample_mgmt_apex namespace provides classes and properties to manage the lifecycle and documentation of
product requirements in manufacturing. Create, update, or version Product Requirement Specification records to ensure sample
data remains consistent and compliant with production standards.

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


Apex Reference Guide

IsvPartners Namespace
The `IsvPartners` namespace provides a class associated with Salesforce ISV partner use cases, such as optimizing code, providing
great customer trial experiences, and driving feature adoption.

KbManagement Namespace
The `KbManagement` namespace provides a class for managing knowledge articles.

LxScheduler Namespace
The `LxScheduler` namespace provides an interface and classes for integrating Salesforce Scheduler with external calendars.

Messaging Namespace
The `Messaging` namespace provides classes and methods for Salesforce notifications and email functionality.

Metadata Namespace
The `Metadata` namespace provides classes and methods for working with custom metadata in Salesforce

PlaceQuote Namespace
The `PlaceQuote` namespace provides classes and methods to create or update quotes with pricing preferences and configuration
options.

Pref_center Namespace
The Pref_center namespace provides an interface, classes, and methods to create and retrieve data in forms in Preference Manager.
Preference Manager, previously called Preference Center, is a feature within the Privacy Center app.

Process Namespace
The `Process` namespace provides an interface and classes for passing data between your organization and a flow.

QuickAction Namespace
The `QuickAction` namespace provides classes and methods for quick actions.

renew_assets_summary Namespace
The renew_assets_summary namespace provides classes that retrieve details about renewable assets to create renewal opportunities.

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

runtime_industries_cpq Namespace
The runtime_industries_cpq namespace provides classes and methods to search products or to manage products, catalogs, and
categories.


Apex Reference Guide

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

Wave Namespace
The classes in the `Wave` namespace are part of the CRM Analytics Analytics SDK, designed to facilitate querying CRM Analytics data
from Apex code.

Appendices


Apex Reference Guide Apex Release Notes

Apex Release Notes

Use the Salesforce Release Notes to learn about the most recent updates and changes to Apex.

[For Apex updates and changes that impact the Salesforce Platform, see the Apex Release Notes.](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex.htm&language=en_US)

[For new and changed Apex classes, methods, exceptions and interfaces, see Apex: New and Changed Items in the Salesforce Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_nc.htm&language=en_US)
Notes.

## Apex DML Operations

You can perform DML operations using the Apex DML statements or the methods of the `Database` class. For lead conversion, use
the `convertLead` method of the `Database` class. There is no DML counterpart for it.

SEE ALSO:

_Apex Developer Guide_ [: Working with Data in Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_data_intro.htm)

Database Class

### Apex DML Statements

Use Data Manipulation Language (DML) statements to insert, update, merge, delete, and restore data in Salesforce.

The following Apex DML statements are available:

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

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)


Apex Reference Guide Apex DML Statements

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

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)

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
[attribute set. To check a field’s attribute, see the Object Reference for Salesforce.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/)

[Also, you can use foreign keys to upsert sObject records if they have been set as reference fields. For more information, see Field Types](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/field_types.htm)
in the _Object Reference for Salesforce._

The optional field parameter, _`opt_field`_, is a field token (of type `Schema.SObjectField` ). For example, to specify the
MyExternalID custom field, the statement is:

```
   upsert sObjectList Account.Fields.MyExternalId__c;

```


Apex Reference Guide Apex DML Statements

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


Apex Reference Guide Apex DML Statements

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

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)

#### Undelete Statement

The `undelete` DML operation restores one or more existing sObject records, such as individual accounts or contacts, from your
organization’s Recycle Bin. `undelete` is analogous to the UNDELETE statement in SQL.

Syntax

```
   undelete sObject | ID

   undelete sObject[] | ID[]

```

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

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)

#### Merge Statement

The `merge` statement merges up to three records of the same sObject type into one of the records, deleting the others, and re-parenting
any related records.

Note: This DML operation does not have a matching Database system method.

Syntax

```
   merge sObject sObject

   merge sObject sObject[]

```


## Apex Reference Guide ApexPages Namespace

```
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

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)

## ApexPages Namespace The ApexPages namespace provides classes used in Visualforce controllers. The following are the classes in the ApexPages namespace.

IN THIS SECTION:

Action Class
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


### Apex Reference Guide Action Class

StandardController Class
Use a StandardController when defining an extension for a standard controller.

StandardSetController Class

`StandardSetController` objects allow you to create list controllers similar to, or as extensions of, the pre-built Visualforce
list controllers provided by Salesforce.

### Action Class

You can use `ApexPages.Action` to create an action method that you can use in a Visualforce custom controller or controller
extension.

Namespace

ApexPages

Usage

For example, you could create a `saveOver` method on a controller extension that performs a custom save.

Instantiation

The following code snippet illustrates how to instantiate a new `ApexPages.Action` object that uses the save action:

```
   ApexPages.Action saveAction = new ApexPages.Action('{!save}');

```

IN THIS SECTION:

#### Action Constructors

Action Methods

#### Action Constructors

### The following are constructors for Action .

IN THIS SECTION:

##### Action(action)

Creates a new instance of the `ApexPages.Action` class using the specified action.

##### Action(action)

Creates a new instance of the `ApexPages.Action` class using the specified action.

Signature

```
   public Action(String action)

```


### Apex Reference Guide Component Class

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

##### invoke()

Invokes the action.

##### getExpression()

Returns the expression that is evaluated when the action is invoked.

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


Apex Reference Guide Component Class

#### Dynamic Component Properties

The following are properties for `Component` .

IN THIS SECTION:

##### childComponents

Returns a reference to the child components for the component.

##### expressions

Sets the content of an attribute using the expression language notation. The notation for this is
##### expressions . name_of_attribute .

facets
Sets the content of a facet to a dynamic component. The notation is `facet` . _`name_of_facet`_ .

##### childComponents

Returns a reference to the child components for the component.

Signature

```
   public List <ApexPages.Component> childComponents {get; set;}

```

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


### Apex Reference Guide IdeaStandardController Class

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


Apex Reference Guide IdeaStandardController Class

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


### Apex Reference Guide IdeaStandardSetController Class

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


Apex Reference Guide IdeaStandardSetController Class

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


Apex Reference Guide IdeaStandardSetController Class

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

```


Apex Reference Guide IdeaStandardSetController Class

```
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


### Apex Reference Guide KnowledgeArticleVersionStandardController Class

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

Namespace

ApexPages

Usage

### In addition to the method listed above, the KnowledgeArticleVersionStandardController class inherits all the methods

associated with `StandardController` .

Note: Though inherited, the `edit`, `delete`, and `save` methods don't serve a function when used with the
### KnowledgeArticleVersionStandardController class.

Example

### The following example shows how a KnowledgeArticleVersionStandardController object can be used to create a

custom extension controller. In this example, you create a class named `AgentContributionArticleController` that allows
customer-support agents to see pre-populated fields on the draft articles they create while closing cases.

Prerequisites:

**1.** Create an article type called _`FAQ`_ . For instructions, see “Create Article Types” in the Salesforce online help.

**2.** Create a text custom field called `Details` . For instructions, see “Add Custom Fields to Article Types” in the Salesforce online help.

**3.** Create a category group called _`Geography`_ and assign it to a category called _`USA`_ . For instructions, see “Create and Modify
Category Groups” and “Add Data Categories to Category Groups” in the Salesforce online help.


Apex Reference Guide KnowledgeArticleVersionStandardController Class

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

```


Apex Reference Guide KnowledgeArticleVersionStandardController Class

```
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

#### KnowledgeArticleVersionStandardController Constructors

KnowledgeArticleVersionStandardController Methods

SEE ALSO:

StandardController Class

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


### Apex Reference Guide Message Class

#### KnowledgeArticleVersionStandardController Methods The following are instance methods for KnowledgeArticleVersionStandardController .

IN THIS SECTION:

##### getSourceId()

Returns the ID for the source object record when creating a new article from another object.

##### setDataCategory(categoryGroup, category)

Specifies a default data category for the specified data category group when creating a new article.

##### getSourceId()

Returns the ID for the source object record when creating a new article from another object.

Signature

```
   public String getSourceId()

```

Return Value

Type: String

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


Apex Reference Guide Message Class

Usage

When using a standard controller, all validation errors, both custom and standard, that occur when the user saves the page are automatically
added to the page error collections. If an `inputField` component is bound to the field with an error, the message is added to the
[component’s error collection. All messages are added to the page’s error collection. For more information, see Validation Rules and](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_std.htm#validation_rules_and_standard_controllers)
[Standard Controllers in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_std.htm#validation_rules_and_standard_controllers) _Visualforce Developer's Guide_ .

If your application uses a custom controller or extension, you must use the `message` class for collecting errors.

Instantiation

In a custom controller or controller extension, you can instantiate a Message in one of these ways:

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

Message(severity, summary)
Creates a new instance of the `ApexPages.Message` class using the specified message severity and summary.


Apex Reference Guide Message Class

##### Message(severity, summary, detail)

Creates a new instance of the `ApexPages.Message` class using the specified message severity, summary, and message detail.

##### Message(severity, summary, detail, id)

Creates a new instance of the `ApexPages.Message` class using the specified severity, summary, detail, and component ID.

##### Message(severity, summary)

Creates a new instance of the `ApexPages.Message` class using the specified message severity and summary.

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


Apex Reference Guide Message Class

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

getDetail()
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


### Apex Reference Guide StandardController Class

##### getDetail()

Returns the value of the detail parameter used to create the message. If no detail String was specified, this method returns `null` .

Signature

```
   public String getDetail()

```

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


Apex Reference Guide StandardController Class

Instantiation

You can instantiate a StandardController in the following way:

```
   ApexPages.StandardController sc = new ApexPages.StandardController(sObject);

```

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


Apex Reference Guide StandardController Class

Signature

```
   public StandardController(SObject controllerSObject)

```

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


Apex Reference Guide StandardController Class

Signature

```
   public Void addFields(List<String> fieldNames)

```

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


Apex Reference Guide StandardController Class

Signature

```
   public System.PageReference edit()

```

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


### Apex Reference Guide StandardSetController Class

Signature

```
   public Void reset()

```

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


Apex Reference Guide StandardSetController Class

are applied to every record in the set controller's collection. This is useful for writing pages that perform mass updates (applying identical
changes to fields within a collection of objects).

Note: Fields that are required in other Salesforce objects will keep the same requiredness when used by the prototype object.

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

```


Apex Reference Guide StandardSetController Class

```
           <apex:column value="{!o.CloseDate}"/>

        </apex:pageBlockTable>

      </apex:pageBlock>

   </apex:page>

```

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

Type: List on page 3992<sObject on page 4190>

A List of standard or custom objects.


Apex Reference Guide StandardSetController Class

Example

```
   List<account> accountList = [SELECT Name FROM Account LIMIT 20];

   ApexPages.StandardSetController ssc = new ApexPages.StandardSetController(accountList);

#### StandardSetController Methods The following are methods for StandardSetController . All are instance methods.

```

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


Apex Reference Guide StandardSetController Class

previous()
Changes the set of records that the controller returns to the previous page of records.

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

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_actions.htm)

##### **`first()`**

Changes the set of records that the controller returns to the first page of records.

Signature

```
   public Void first()

```

Return Value

Type: Void

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_actions.htm)


Apex Reference Guide StandardSetController Class

##### getCompleteResult()

Indicates whether there are more records in the set than the maximum record limit. If this is false, there are more records than you can
process using the list controller. The maximum record limit is 10,000 records.

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

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_actions.htm)

_Visualforce Developer Guide_ [: List Views with Standard List Controllers](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_list_views.htm)

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


Apex Reference Guide StandardSetController Class

Signature

```
   public Boolean getHasPrevious()

```

Return Value

Type: Boolean

##### getListViewOptions()

Returns a list of the listviews available to the current user.

Signature

```
   public System.SelectOption getListViewOptions()

```

Return Value

Type: System.SelectOption[]

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_actions.htm)

_Visualforce Developer Guide_ [: List Views with Standard List Controllers](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_list_views.htm)

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


Apex Reference Guide StandardSetController Class

##### getRecord()

Returns the sObject that represents the changes to the selected records. This retrieves the prototype object contained within the class,
and is used for performing mass updates.

Signature

```
   public sObject getRecord()

```

Return Value

Type: sObject

SEE ALSO:

_Visualforce Developer Guide_ [: Building a Custom List Controller](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_custom_list_controller.htm)

##### getRecords()

Returns the list of sObjects in the current page set. This list is immutable, i.e. you can't call `clear` () on it.

Signature

```
   public sObject[] getRecords()

```

Return Value

Type: sObject[]

SEE ALSO:

_Visualforce Developer Guide_ [: Building a Custom List Controller](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_custom_list_controller.htm)

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


Apex Reference Guide StandardSetController Class

Return Value

Type: sObject[]

##### **`last()`**

Changes the set of records that the controller returns to the last page of records.

Signature

```
   public Void last()

```

Return Value

Type: Void

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_actions.htm)

##### **`next()`**

Changes the set of records that the controller returns to the next page of records.

Signature

```
   public Void next()

```

Return Value

Type: Void

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_actions.htm)

##### **`previous()`**

Changes the set of records that the controller returns to the previous page of records.

Signature

```
   public Void previous()

```

Return Value

Type: Void

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_actions.htm)


Apex Reference Guide StandardSetController Class

##### save()

Inserts new records or updates existing records that have been changed. After this operation is finished, it returns a PageReference to
the original page, if known, or the home page.

Signature

```
   public System.PageReference save()

```

Return Value

Type: System.PageReference

SEE ALSO:

_Visualforce Developer Guide_ [: Standard List Controller Actions](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_actions.htm)

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


Apex Reference Guide StandardSetController Class

##### setPageSize(pageSize)

Sets the number of records in each page set.

Signature

```
   public Void setPageSize(Integer pageSize)

```

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

```


## Apex Reference Guide AppLauncher Namespace

```
        </apex:pageBlockTable>

      </apex:pageBlock>

   </apex:page>

   // MyControllerExtension.cls

   public with sharing class MyControllerExtension {

      private ApexPages.StandardSetController setController;

      public MyControllerExtension(ApexPages.StandardSetController setController) {

        this.setController = setController;

        Account [] records = [SELECT Id, Name FROM Account LIMIT 30];

        setController.setSelected(records);

      }

   }

```

SEE ALSO:

_Visualforce Developer Guide_ [: Accessing Data with List Controllers](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_sosc_access_data.htm)

## AppLauncher Namespace The AppLauncher namespace provides methods for managing the appearance of apps in the App Launcher, including their visibility

and sort order.

## The following class is in the AppLauncher namespace.

IN THIS SECTION:

AppMenu Class
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


### Apex Reference Guide AppMenu Class

SocialLoginController Class
This class and its methods are for internal use only.

### AppMenu Class

Contains methods to set the appearance of apps in the App Launcher.

Namespace

AppLauncher

IN THIS SECTION:

#### AppMenu Methods AppMenu Methods

### The following are methods for AppMenu .

IN THIS SECTION:

##### setAppVisibility(appMenuItemId, isVisible)

Shows or hides specific apps in the App Launcher.

setOrgSortOrder(appIds)
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

The 15-character application ID value for an app. For more information, see the `ApplicationId` [field for AppMenuItem or the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_appmenuitem.htm)
`AppMenuItemId` [field for UserAppMenuItem in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_userappmenuitem.htm) _Salesforce Object Reference_

```
   isVisible
```

Type: Boolean

If `true`, the app is visible.


### Apex Reference Guide ChangePasswordController Class

Return Value

Type: void

##### setOrgSortOrder(appIds)

Sets the organization-wide default sort order for the App Launcher based on a List of app menu item IDs in the desired order.

Signature

```
   public static void setOrgSortOrder(List<Id> appIds)

```

Parameters

```
   appIds
```

Type: List<Id>

A list of application ID values. For more information, see the `ApplicationId` [field for AppMenuItem in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_appmenuitem.htm) _Salesforce Object_
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

A list of application ID values. For more information, see the `AppMenuItemId` [field for UserAppMenuItem in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_userappmenuitem.htm) _Salesforce Object_
_Reference_ .

Return Value

Type: void

### ChangePasswordController Class

This class and its methods are for internal use only.

Namespace

AppLauncher


### Apex Reference Guide CommunityLogoController Class CommunityLogoController Class

This class and its methods are for internal use only.

Namespace

AppLauncher

### EmployeeLoginLinkController Class

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


### Apex Reference Guide SocialLoginController Class SocialLoginController Class

This class and its methods are for internal use only.

Namespace

AppLauncher

## Approval Namespace The Approval namespace provides classes and methods for approval processes. The following are the classes in the Approval namespace.

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


Apex Reference Guide LockResult Class

Example

The following example obtains and iterates through the returned Approval.LockResult objects. It locks some queried accounts using
`Approval.lock` with a `false` second parameter to allow partial processing of records on failure. Next, it iterates through the
results to determine whether the operation was successful for each record. It writes the ID of every record that was processed successfully
to the debug log, or writes error messages and failed fields of the failed records.

```
   // Query the accounts to lock

   Account[] accts = [SELECT Id from Account WHERE Name LIKE 'Acme%'];

   // Lock the accounts

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

getErrors()
If an error occurred, returns an array of one or more database error objects, providing the error code and description.

getId()
Returns the ID of the sObject you are trying to lock.

isSuccess()
A Boolean value that is set to `true` if the lock operation is successful for this object, or `false` otherwise.


### Apex Reference Guide ProcessRequest Class

##### getErrors()

If an error occurred, returns an array of one or more database error objects, providing the error code and description.

Signature

```
   public List<Database.Error> getErrors()

```

Return Value

Type: List<Database.Error>

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


Apex Reference Guide ProcessRequest Class

Usage

The request must be instantiated via the child classes, `ProcessSubmitRequest` and `ProcessWorkItemRequest` .

#### ProcessRequest Methods The following are methods for ProcessRequest . All are instance methods.

IN THIS SECTION:

##### getComments()

Returns the comments that have been added previously to the approval request.

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


### Apex Reference Guide ProcessResult Class

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


Apex Reference Guide ProcessResult Class

IN THIS SECTION:

##### getEntityId()

The ID of the record being processed.

##### getErrors()

If an error occurred, returns an array of one or more database error objects including the error code and description.

##### getInstanceId()

The ID of the approval process that has been submitted for approval.

getInstanceStatus()
The status of the current approval process. Valid values are: Approved, Rejected, Removed or Pending.

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


### Apex Reference Guide ProcessSubmitRequest Class

Return Value

Type: String

##### getInstanceStatus()

The status of the current approval process. Valid values are: Approved, Rejected, Removed or Pending.

Signature

```
   public String getInstanceStatus()

```

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


Apex Reference Guide ProcessSubmitRequest Class

Usage

You must specify the Approval namespace when creating an instance of this class. The constructor for this class takes no arguments.
For example:

```
   Approval.ProcessSubmitRequest psr = new Approval.ProcessSubmitRequest();

```

Inherited Methods

#### In addition to the methods listed, the ProcessSubmitRequest class has access to all the methods in its parent class, ProcessRequest

Class.

**•** getComments()

**•** getNextApproverIds()

**•** setComments(comments)

**•** setNextApproverIds(nextApproverIds)

Example

[To view sample code, refer to Approval Processing Example.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_process_example.htm)

#### ProcessSubmitRequest Methods The following are methods for ProcessSubmitRequest . All are instance methods.

IN THIS SECTION:

getObjectId()
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


Apex Reference Guide ProcessSubmitRequest Class

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


Apex Reference Guide ProcessSubmitRequest Class

Signature

```
   public String getSubmitterId()

```

Return Value

Type: String

##### setObjectId(recordId)

Sets the ID of the record to be submitted for approval. For example, it can specify an account, contact, or custom object record.

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


### Apex Reference Guide ProcessWorkitemRequest Class

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


Apex Reference Guide ProcessWorkitemRequest Class

Usage

You must specify the Approval namespace when creating an instance of this class. The constructor for this class takes no arguments.
For example:

```
   Approval.ProcessWorkitemRequest pwr = new Approval.ProcessWorkitemRequest();

```

Inherited Methods

#### In addition to the methods listed, the ProcessWorkitemRequest class has access to all the methods in its parent class,

ProcessRequest Class:

**•** getComments()

**•** getNextApproverIds()

**•** setComments(comments)

**•** setNextApproverIds(nextApproverIds)

#### ProcessWorkitemRequest Methods The following are methods for ProcessWorkitemRequest . All are instance methods.

IN THIS SECTION:

##### getAction()

Returns the type of action already associated with the approval request. Valid values are: Approve, Reject, or Removed.

##### getWorkitemId()

Returns the ID of the approval request that is in the process of being approved, rejected, or removed.

setAction(actionType)
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


### Apex Reference Guide UnlockResult Class

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


Apex Reference Guide UnlockResult Class

Usage

The `System.Approval.unlock()` methods return Approval.UnlockResult objects. Each element in an UnlockResult array
corresponds to an element in the ID or sObject array passed as a parameter to an `unlock` method. The first element in the UnlockResult
array corresponds to the first element in the ID or sObject array, the second element corresponds to the second element, and so on. If
only one ID or sObject is passed in, the UnlockResult array contains a single element.

Example

The following example shows how to obtain and iterate through the returned Approval.UnlockResult objects. It locks some queried
accounts using `Approval.unlock` with a `false` second parameter to allow partial processing of records on failure. Next, it
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


Apex Reference Guide UnlockResult Class

IN THIS SECTION:

#### UnlockResult Methods

SEE ALSO:

Approval Class

#### UnlockResult Methods The following are methods for UnlockResult .

IN THIS SECTION:

##### getErrors()

If an error occurred, returns an array of one or more database error objects, providing the error code and description.

##### getId()

Returns the ID of the sObject you are trying to unlock.

isSuccess()
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


## Apex Reference Guide Auth Namespace

##### isSuccess()

A Boolean value that is set to `true` if the unlock operation is successful for this object, or `false` otherwise.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

## Auth Namespace The Auth namespace provides an interface and classes for single sign-on into Salesforce and session security management. The following is the interface in the Auth namespace.

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


Apex Reference Guide Auth Namespace

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


Apex Reference Guide Auth Namespace

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


### Apex Reference Guide AuthConfiguration Class

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


Apex Reference Guide AuthConfiguration Class

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

#### AuthConfiguration Constructors The following are constructors for AuthConfiguration .

```

Note: The `AuthConfiguration (networkId, startUrl)` constructor is deprecated in API version 56.0 and later.

##### AuthConfiguration(communityOrCustomUrl, startUrl)

#### Creates an instance of the AuthConfiguration class using the specified URL for an Experience Cloud site or a My Domain subdomain

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

#### AuthConfiguration Methods The following are methods for AuthConfiguration . Use these methods to manage and customize authentication for a Salesforce

community.


Apex Reference Guide AuthConfiguration Class

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


Apex Reference Guide AuthConfiguration Class

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


Apex Reference Guide AuthConfiguration Class

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

Note: For better performance, we recommend using this method instead of `getAuthProviderSsoUrl` . If the authentication
provider has `User Subdomain for Callback` enabled, changing the single sign-on URL also changes the callback URL
to use the Experience Cloud site subdomain. Before switching to this method, update the callback URL in your third-party applications
to avoid getting an invalid callback URL error during single sign-on.

Signature

```
   public static String getAuthProviderSsoDomainUrl(String communityUrl, String startUrl,

   String developerName)

```


Apex Reference Guide AuthConfiguration Class

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


Apex Reference Guide AuthConfiguration Class

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


Apex Reference Guide AuthConfiguration Class

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


Apex Reference Guide AuthConfiguration Class

Return Value

Type: Boolean

##### **`getHeadlessFrgtPswEnabled()`**

This method will be deprecated in a future release. Use the `getHeadlessForgotPasswordEnabled()` method in this class
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


Apex Reference Guide AuthConfiguration Class

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


Apex Reference Guide AuthConfiguration Class

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


### Apex Reference Guide AuthProviderCallbackState Class

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


Apex Reference Guide AuthProviderCallbackState Class

IN THIS SECTION:

##### AuthProviderCallbackState(headers, body, queryParameters) Creates an instance of the AuthProviderCallbackState class using the specified HTTP headers, body, and query parameters

of the authentication request.

##### AuthProviderCallbackState(headers, body, queryParameters) Creates an instance of the AuthProviderCallbackState class using the specified HTTP headers, body, and query parameters

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

##### _`body`_

Type: String

The HTTP body of the authentication request.

```
   queryParameters
```

Type: Map<String,String>

The HTTP query parameters of the authentication request.

#### AuthProviderCallbackState Properties

##### The following are properties for AuthProviderCallbackState .

IN THIS SECTION:

##### body

The HTTP body of the authentication request.

headers
The HTTP headers of the authentication request.

queryParameters
The HTTP query parameters of the authentication request.

##### body

The HTTP body of the authentication request.

Signature

```
   public String body {get; set;}

```


### Apex Reference Guide AuthProviderPlugin Interface

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

AuthProviderPlugin Methods

AuthProviderPlugin Example Implementation


Apex Reference Guide AuthProviderPlugin Interface

#### AuthProviderPlugin Methods The following methods are for AuthProviderPlugin, which, as of API version 39.0, is deprecated. Use themethods in

`AuthProviderPluginClass` instead.

IN THIS SECTION:

##### getCustomMetadataType()

Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

##### getUserInfo(authProviderConfiguration, response)

Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

handleCallback(authProviderConfiguration, callbackState)
Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

initiate(authProviderConfiguration, stateToPropagate)
Deprecated as of API version 39.0. Use the corresponding method in `Auth.AuthProviderPluginClass` .

SEE ALSO:

[Salesforce Help: Create a Custom External Authentication Provider](https://help.salesforce.com/HTViewHelpDoc?id=sso_provider_plugin_custom.htm&language=en_US)

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


Apex Reference Guide AuthProviderPlugin Interface

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


### Apex Reference Guide AuthProviderPluginClass Class

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


Apex Reference Guide AuthProviderPluginClass Class

Usage

To create a custom authentication provider for single sign-on, create a class that extends `Auth.AuthProviderPluginClass` .
This class allows you to store the custom configuration for your authentication provider and handle authentication protocols when users
log in to Salesforce with their login credentials for an external service provider. In Salesforce, the class that implements this interface
appears in the `Provider Type` drop-down list in Auth. Providers in Setup. Make sure that the user you specify to run the class has
“Customize Application” and “Manage Auth. Providers” permissions.

#### As of API version 39.0, use the abstract class AuthProviderPluginClass to create a custom external authentication provider. This class replaces the AuthProviderPlugin interface. If you’ve already implemented a custom authentication provider plug-in using the interface, it still works. However, use AuthProviderPluginClass to extend your plug-in. If you haven’t created an

[interface, create a custom authentication provider plug-in by extending this abstract class. For more information, see Create a Custom](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/authproviderplugin.htm)
[Authentication Provider Plug-in.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/authproviderplugin.htm)

IN THIS SECTION:

#### AuthProviderPluginClass Methods

AuthProviderPluginClass Code Example

#### AuthProviderPluginClass Methods The AuthProviderPluginClass methods don’t support DML options.

[This class doesn't include a method for single logout. You can easily configure single logout in Setup. For steps, see Configure OpenID](https://help.salesforce.com/s/articleView?id=xcloud.security_auth_slo_oidc_rp_configuring.htm&language=en_US)
[Connect Single Logout with Salesforce as the Relying Party in](https://help.salesforce.com/s/articleView?id=xcloud.security_auth_slo_oidc_rp_configuring.htm&language=en_US) _Salesforce Help_ . Alternatively, create custom methods for single logout.

IN THIS SECTION:

##### getCustomMetadataType()

Returns the custom metadata type API name for a custom OAuth-based authentication provider for single sign-on to Salesforce.

getUserInfo(authProviderConfiguration, response)
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


Apex Reference Guide AuthProviderPluginClass Class

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


Apex Reference Guide AuthProviderPluginClass Class

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


Apex Reference Guide AuthProviderPluginClass Class

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

```


Apex Reference Guide AuthProviderPluginClass Class

```
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

```


Apex Reference Guide AuthProviderPluginClass Class

```
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

```


Apex Reference Guide AuthProviderPluginClass Class

```
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

```


Apex Reference Guide AuthProviderPluginClass Class

```
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

```


Apex Reference Guide AuthProviderPluginClass Class

```
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

```


### Apex Reference Guide AuthProviderTokenResponse Class

```
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


Apex Reference Guide AuthProviderTokenResponse Class

IN THIS SECTION:

##### AuthProviderTokenResponse(provider, oauthToken, oauthSecretOrRefreshToken, state) Creates an instance of the AuthProviderTokenResponse class for a custom authentication provider plug-in using the

specified arguments.

##### AuthProviderTokenResponse(provider, oauthToken, oauthSecretOrRefreshToken, state, idToken)

Creates an instance of the AuthProviderTokenResponse class for a custom authentication provider plug-in using the specified
arguments. This constructor includes a parameter for the ID token.

##### AuthProviderTokenResponse(provider, oauthToken, oauthSecretOrRefreshToken, state) Creates an instance of the AuthProviderTokenResponse class for a custom authentication provider plug-in using the specified

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


Apex Reference Guide AuthProviderTokenResponse Class

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

##### _`oauthSecretOrRefreshToken`_

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

#### AuthProviderTokenResponse Properties The following are properties for AuthProviderTokenResponse .

IN THIS SECTION:

##### oauthSecretOrRefreshToken

The OAuth secret or refresh token for the currently logged-in user.

oauthToken
The OAuth access token.

provider
The authentication provider.

state
The state passed in to initiate the authentication request for the user.

idToken
The ID token from the third party in encoded JWT format.

##### oauthSecretOrRefreshToken

The OAuth secret or refresh token for the currently logged-in user.

Signature

```
   public String oauthSecretOrRefreshToken {get; set;}

```


Apex Reference Guide AuthProviderTokenResponse Class

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


### Apex Reference Guide AuthToken Class AuthToken Class

Contains methods for getting and revoking access and refresh tokens that are issued when a user logs in via a single sign-on (SSO) flow
that uses an authentication provider, such as Facebook.

Namespace

### Auth

Usage

To authenticate users via an authentication provider, you must create a class that implements the `[Auth.RegistrationHandler](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_auth_plugin.htm)`
[interface. When a user logs in to Salesforce via a provider such as Facebook, they’re issued an access token and in some cases, a refresh](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_auth_plugin.htm)
token. To retrieve and revoke these tokens, use the methods in the `Auth.AuthToken` class.

#### AuthToken Methods

### The following are methods for AuthToken . All methods are static.

IN THIS SECTION:

##### getAccessToken(authProviderId, providerName)

Returns an access token for the current user using the specified 18-character identifier of an AuthProvider definition in your org and
the proper name of the provider, such as Salesforce or Facebook.

getAccessTokenMap(authProviderId, providerName)
Returns a map from the provider’s identifier to the access token for the currently logged-in Salesforce user. The identifier value
depends on the provider. For example, for Salesforce, it’s the user ID, while for Facebook, it’s the user number.

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


Apex Reference Guide AuthToken Class

```
   providerName
```

Type: String

The proper name of the provider. Here are valid values for each provider type.

**•** Apple— `Apple`

**•** Custom—For a custom authentication provider, use the value in the `FriendlyName` [field on the AuthProvider object, such](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_authprovider.htm)
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


Apex Reference Guide AuthToken Class

**•** Custom—For a custom authentication provider, use the value in the `FriendlyName` [field on the AuthProvider object, such](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_authprovider.htm)
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

**•** Custom—For a custom authentication provider, use the value in the `FriendlyName` [field on the AuthProvider object, such](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_authprovider.htm)
as `MyProvider` .

**•** Facebook— `Facebook`

**•** GitHub— `GitHub`

**•** Google— `Google`


Apex Reference Guide AuthToken Class

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


Apex Reference Guide AuthToken Class

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
[AuthProvider object. For example, if the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_authprovider.htm) `FriendlyName` is `MyProvider`, use `myprovider` .

**•** Facebook— `facebook`

**•** GitHub— `github`

**•** Google— `google`

**•** Janrain—Use a lowercase version of the name of the third party, such as `yahoo!` .

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


### Apex Reference Guide CommunitiesUtil Class

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

      return new PageReference(LOGIN_URL);

   if (Auth.CommunitiesUtil.isInternalUser())

      // Redirect to the home page if user is an internal user

      return new PageReference(HOME_URL);

#### CommunitiesUtil Methods

### The following are methods for CommunitiesUtil . All methods are static.

```

IN THIS SECTION:

##### getLogoutUrl()

Returns the page to display after the current Experience Cloud user logs out.

getUserDisplayName()
Returns the current user’s Experience Cloud display name.

isGuestUser()
Indicates whether the current user isn’t logged in to the Experience Cloud site. Redirect the user to log in, if necessary.

isInternalUser()
Indicates whether the current user is logged in as a member of the parent Salesforce organization, such as an employee.

##### getLogoutUrl()

Returns the page to display after the current Experience Cloud user logs out.


### Apex Reference Guide ConfigurableSelfRegHandler Interface

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


Apex Reference Guide ConfigurableSelfRegHandler Interface

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

#### The generated ConfigurableSelfRegHandler is located on the Setup Apex Classes page, and begins with

`AutocreatedConfigSelfReg`, for example, `AutocreatedConfigSelfReg1532475901849` .

[For an example, see ConfigurableSelfRegHandler Example Implementation. For more details, see Salesforce Customer Identity in](https://help.salesforce.com/articleView?id=identity_about_customers_partners.htm&language=en_US) _Salesforce_
_Help_ .

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


Apex Reference Guide ConfigurableSelfRegHandler Interface

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


Apex Reference Guide ConfigurableSelfRegHandler Interface

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

```


Apex Reference Guide ConfigurableSelfRegHandler Interface

```
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

```


### Apex Reference Guide ConfirmUserRegistrationHandler Interface

```
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

### ConfirmUserRegistrationHandler Interface

```

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


Apex Reference Guide ConfirmUserRegistrationHandler Interface

that the incoming user data is consistent with the user's third-party identifier. If not, you can identify which user is supposed to be logged
in.

You can also use the `Auth.ConfirmUserRegistrationHandler` interface to switch context for users with multiple records.
For example, a user has two records—an admin user and a standard user. When the user logs in, the third-party identity provider confirms
[the account used to log in and sends the response to Salesforce via the UserInfo endpoint. You can then use this information to determine](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_using_userinfo_endpoint.htm&type=5&language=en_US)
whether to log in the user as an admin or standard user.

IN THIS SECTION:

#### ConfirmUserRegistrationHandler Methods

ConfirmUserRegistrationHandler Example Implementation

#### ConfirmUserRegistrationHandler Methods The following are methods for ConfirmUserRegistrationHandler .

IN THIS SECTION:

##### confirmUser(userId, tpalId, portalId, userdata)

Returns the ID of the user to be logged in based on their mapping to a third-party identifier. This method is called before calling the
`[updateUser()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_auth_plugin.htm#apex_Auth_RegistrationHandler_updateUser)` method. It's called only if the incoming user has previously logged in and has a third-party account link to a
Salesforce user.

##### **`confirmUser(userId, tpalId, portalId, userdata)`**

Returns the ID of the user to be logged in based on their mapping to a third-party identifier. This method is called before calling the
`[updateUser()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_auth_plugin.htm#apex_Auth_RegistrationHandler_updateUser)` method. It's called only if the incoming user has previously logged in and has a third-party account link to a Salesforce
user.

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

[Type: Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_UserData.htm#apex_class_Auth_UserData)

Contains user information from the third-party identity provider.


Apex Reference Guide ConfirmUserRegistrationHandler Interface

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

```


### Apex Reference Guide ConnectedAppPlugin Class

```
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

Namespace

Auth

Usage

When you create a connected app, you specify general information about the app and settings for OAuth, web apps, mobile apps, and
### canvas apps. To customize how the app is invoked, create a connected app handler with this ConnectedAppPlugin Apex class.

For example, use this class to support new authentication protocols or respond to user attributes in a way that benefits a business process.

### When you create a connected app handler, you also configure the ConnectedAppPlugin class to run as an execution user. The

execution user authorizes access for the connected app. For example, when you use the `authorize` method, the execution user
authorizes the connected app to access data.

If you don't specify an execution user, the plug-in runs as an Automated Process User, which is a system user that executes tasks behind
### the scenes. Most ConnectedAppPlugin methods require that you specify an execution user, with the exception of the

`customAttributes` [method. For more information, see Create a Custom Connected App Handler.](https://help.salesforce.com/articleView?id=xcloud.connected_app_create_custom_handler.htm&type=5&language=en_US)


Apex Reference Guide ConnectedAppPlugin Class

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

```


Apex Reference Guide ConnectedAppPlugin Class

```
        return formulaDefinedAttributes;

      }

   }

```

IN THIS SECTION:

#### ConnectedAppPlugin Methods ConnectedAppPlugin Methods The following are methods for ConnectedAppPlugin .

IN THIS SECTION:

##### authorize(userId, connectedAppId, isAdminApproved) Deprecated and available only in API versions 35.0 and 36.0. As of version 37.0, use authorize(userId, connectedAppId,

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


Apex Reference Guide ConnectedAppPlugin Class

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


Apex Reference Guide ConnectedAppPlugin Class

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


Apex Reference Guide ConnectedAppPlugin Class

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


Apex Reference Guide ConnectedAppPlugin Class

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


### Apex Reference Guide CustomOneTimePasswordDeliveryHandler Interface CustomOneTimePasswordDeliveryHandler Interface

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

##### sendOneTimePassword(userId, phoneNumber, oneTimePassword, networkId, defaultText, expId)

Calls out to an external SMS messaging provider to send a Salesforce one-time password to an external user for identity verification.
Returns an `Auth.CustomOneTimePasswordDeliveryResult` indicating whether the provider sent the message.

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


Apex Reference Guide CustomOneTimePasswordDeliveryHandler Interface

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

```


### Apex Reference Guide CustomOneTimePasswordDeliveryResult Enum CustomOneTimePasswordDeliveryResult Enum

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


Apex Reference Guide ExternalClientAppOauthHandler Class

If you don't specify an execution user, the plug-in runs as an Automated Process User, which is a system user that executes tasks behind
#### the scenes. Most ExternalClientAppOauthHandler methods require that you specify an execution user, with the exception

of the `customAttributes` method.

IN THIS SECTION:

#### ExternalClientAppOauthHandler Methods ExternalClientAppOauthHandler Methods The following are methods for ExternalClientAppOauthHandler .

IN THIS SECTION:

##### authorize(userId, ecAppId, isAdminApproved, context)

Authorizes the specified user to access the external client app. If the external client app is set for users to self-authorize, this method
isn’t invoked.

customAttributes(userId, ecAppId, formulaDefinedAttributes, context)
Sets new attributes for the specified user. When the external client app gets the user’s attributes from the UserInfo endpoint, use
this method to update the attribute values.

refresh(userId, ecAppId, context)
Salesforce calls this method during a refresh token exchange.

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

Type: Auth.InvocationContext on page 137


Apex Reference Guide ExternalClientAppOauthHandler Class

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


### Apex Reference Guide GeneratedUserData Class

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

#### GeneratedUserData Constructors

### The following are constructors for GeneratedUserData .


Apex Reference Guide GeneratedUserData Class

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


Apex Reference Guide GeneratedUserData Class

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

emailEncodingKey
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


Apex Reference Guide GeneratedUserData Class

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


Apex Reference Guide GeneratedUserData Class

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


### Apex Reference Guide HeadlessSelfRegistrationHandler Interface

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

Namespace

Auth

Usage

The Headless Registration Flow allows you to control user registration experience in a third-party app while using Salesforce to authenticate
users and manage their data access. When you set up this flow, add users in the class that is implementing the
`Auth.HeadlessSelfRegistrationHandler` interface. This class runs after the user verifies their identity. For a detailed
[explanation of headless registration, see Headless Registration Flow for Private Clients or Headless Registration Flow for Public Clients,](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_headless_registration_private_clients.htm&type=5&language=en_US)
depending on your app type.

IN THIS SECTION:

HeadlessSelfRegistrationHandler Methods
### The following are methods for HeadlessSelfRegistrationHandler .


Apex Reference Guide HeadlessSelfRegistrationHandler Interface

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

```
   data
```

[Type: Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_UserData.htm)

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


Apex Reference Guide HeadlessSelfRegistrationHandler Interface

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

```


### Apex Reference Guide HeadlessUserDiscoveryHandler Interface

```
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


Apex Reference Guide HeadlessUserDiscoveryHandler Interface

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

#### HeadlessUserDiscoveryHandler Methods The following are methods for HeadlessUserDiscoveryHandler .

IN THIS SECTION:

##### discoverUserFromLoginHint(networkId, loginHint, verificationAction, customDataJson, requestAttributes)

Finds a user's Salesforce account based on user information, such as their email address, phone number, or other data, that's passed
to a Salesforce endpoint during headless login, passwordless login, and forgot password flows.

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


Apex Reference Guide HeadlessUserDiscoveryHandler Interface

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

[Type: Map<String,String>](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_map.htm#apex_methods_system_map)

Information about the login request that's based on the user’s browser state when accessing the login page. `requestAttributes`
passes in the CommunityUrl, IpAddress, UserAgent, Platform, Application, City, Country, and Subdivision values. The City, Country,
and Subdivision values come from IP geolocation.

Return Value

Type: Auth.HeadlessUserDiscoveryResponse on page 134

If the handler finds a user, it returns a user ID. If not, it returns an error message.

#### HeadlessUserDiscoveryHandler Example Implementation

Here's an example implementation of the `Auth.HeadlessUserDiscoveryHandler` interface. This example supports login
with email and login with SMS.

The `discoverUserFromLoginHint` method uses custom logic to search for a user account with a verified email address or
phone number that matches the data passed in the login hint. As a security best practice, Salesforce always recommends writing code
to determine if the user's email address or phone number is verified.

For users logging in with email, the custom logic first checks whether the email address passed in the login hint is in a valid format. Then,
[to look for a verified Salesforce email address that matches the email address passed in the login hint, it queries the TwoFactorMethodsInfo](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_twofactormethodsinfo.htm)
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

```


Apex Reference Guide HeadlessUserDiscoveryHandler Interface

```
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

```


Apex Reference Guide HeadlessUserDiscoveryHandler Interface

```
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

```


### Apex Reference Guide HeadlessUserDiscoveryResponse Class

```
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


Apex Reference Guide HeadlessUserDiscoveryResponse Class

Parameters

##### _`userIds`_

[Type: Set<Id>](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_set.htm)

The user ID that's associated with the data passed in the `login_hint` parameter. If there are multiple users associated with the
data, it can return multiple IDs, but headless user discovery fails.

##### _`customErrorMessage`_

Type: String

A custom error message that's returned if headless user discovery fails.

#### HeadlessUserDiscoveryResponse Properties The following are properties for HeadlessUserDiscoveryResponse .

IN THIS SECTION:

##### customErrorMessage

A custom error message that's returned if headless user discovery fails. For example, write custom logic in your headless user discovery
handler to see if the user's email address is verified. Then return a custom error message for when it isn't verified.

##### userIds

The user ID for the external user that's associated with the data passed into the `login_hint` parameter. If there are multiple
users associated with the data, it can return multiple IDs, but headless user discovery fails.

##### **`customErrorMessage`**

A custom error message that's returned if headless user discovery fails. For example, write custom logic in your headless user discovery
handler to see if the user's email address is verified. Then return a custom error message for when it isn't verified.

Signature

```
   public String customErrorMessage {get; set;}

```

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

[Type: Set<Id>](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_set.htm)


### Apex Reference Guide HttpCalloutMockUtil Class HttpCalloutMockUtil Class

Contains a method to send fake HTTP callouts for classes in the `Auth` namespace.

Namespace

Auth

Usage

##### Use the setHttpMock method in this class to test HTTP callouts when implementing the Auth.JWTBearerTokenExchange

and `Auth.JWTUtil` classes.

For the `Auth.JWTBearerTokenExchange` class, mock callouts to the OAuth token endpoint when using the
`JWTBearerTokenExchange` method.

For the `Auth.JWTUtil` class, mock callouts to the identity provider’s JSON Web Key Set (JWKS) endpoint when using the
`validateJWTWithKeysEndpoint` method.

[For more information on mocking HTTP callouts, see Testing HTTP Callouts by Implementing the HttpCalloutMock Interface.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_restful_http_testing_httpcalloutmock.htm)

IN THIS SECTION:

#### HttpCalloutMockUtil Methods HttpCalloutMockUtil Methods

### The following are methods for HttpCalloutMockUtil .

IN THIS SECTION:

##### setHttpMock(mock)

Mocks an HTTP callout using an implementation of the `System.HttpCalloutMock` interface.

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

[Type: System.HttpCalloutMock](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_httpcalloutmock.htm)

[A class that implements the System.HttpCalloutMock interface to return a fake HTTP response for a given request to the OAuth token](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_httpcalloutmock.htm)
endpoint or a JWKS endpoint on an external identity provider, depending on your use case.


### Apex Reference Guide IntegratingAppType Enum

Return Value

Type: void

### IntegratingAppType Enum

Specifies whether you’re integrating your app as a connected app or as an external client app in methods used in your customized Apex
token exchange handler, which extends the `Auth.Oauth2TokenExchangeHandler` class.

Usage

[See Token Exchange Handler Validation and Subject Mapping.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/token_exchange_handler.htm)

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


### Apex Reference Guide JsonValueOutput Class

**Value** **Description**

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

JsonValueOutput Constructors

JsonValueOutput Properties


Apex Reference Guide JsonValueOutput Class

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

If the attribute returned by the action is an integer value, it's stored in this parameter.

```
   doubleValue
```

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


Apex Reference Guide JsonValueOutput Class

IN THIS SECTION:

##### booleanValue

If the attribute returned by the action is a boolean value, it's stored in this property.

##### doubleValue

If the attribute returned by the action is a Double value, it's stored in this property.

##### integerValue

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


### Apex Reference Guide JWS Class

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

Property Value

Type: String

### JWS Class

Contains methods that apply a digital signature to a JSON Web Token (JWT), using a JSON Web Signature (JWS) data structure. This class
creates the signed JWT bearer token, which can be used to request an OAuth access token in the OAuth 2.0 JWT bearer token flow.

Namespace

Auth


Apex Reference Guide JWS Class

Usage

Use the methods in this class to sign the JWT bearer token with the X509 certificate.

IN THIS SECTION:

#### JWS Constructors

JWS Methods

#### JWS Constructors The following are constructors for JWS .

IN THIS SECTION:

##### JWS(jwt, certDevName)
#### Creates an instance of the JWS class using the specified Auth.JWT payload and the certificate used for signing the JWT bearer

token.

##### JWS(payload, certDevName)
#### Creates an instance of the JWS class using the specified payload and certificate used for signing the JWT bearer token.

##### JWS(jwt, certDevName)

#### Creates an instance of the JWS class using the specified Auth.JWT payload and the certificate used for signing the JWT bearer token.

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

```
   certDevName
```

Type: String

The `Unique Name` for a certificate stored in the Salesforce org’s Certificate and Key Management page to use for signing the
JWT bearer token.

Usage

Calls the `toJSONString()` method in `Auth.JWT` and sets the resulting string as the payload of the JWT bearer token. Alternatively,
##### you can specify the payload directly using JWS(payload, certDevName) . JWS(payload, certDevName)

#### Creates an instance of the JWS class using the specified payload and certificate used for signing the JWT bearer token.


Apex Reference Guide JWS Class

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

#### JWS Methods The following are methods for JWS . All are instance methods.

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the JWS object.

##### getCompactSerialization()

Returns the compact serialization representation of the JWS as a concatenated string, with the encoded JWS header, encoded JWS
payload, and encoded JWS signature strings separated by period ('.') characters.

##### clone()

Makes a duplicate copy of the JWS object.

Signature

```
   public Object clone()

```

Return Value

Type: JWS

##### getCompactSerialization()

Returns the compact serialization representation of the JWS as a concatenated string, with the encoded JWS header, encoded JWS
payload, and encoded JWS signature strings separated by period ('.') characters.


### Apex Reference Guide JWT Class

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
[and a full code sample, see JWTBearerTokenExchange Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWTBearerTokenExchange.htm)

IN THIS SECTION:

#### JWT Methods JWT Methods

### The following are methods for JWT . All are instance methods.

IN THIS SECTION:

clone()
Makes a duplicate copy of the JWT object.

getAdditionalClaims()
Returns a map of additional claims in the JWT, where the key string contains the name of the claim, and the value contains the value
of the claim.

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


Apex Reference Guide JWT Class

getValidityLength()
Returns the length of time (in seconds) that the JWT is valid, which affects the expiration ( `exp` ) claim. This method returns a
`NoAccess` exception for JWTs generated using methods in the `Auth.JWTUtil` class. To return the validity length for these
##### JWTs, use the getAdditionalClaims method instead.

setAdditionalClaims(additionalClaims)
##### Sets the additional claims in the JWT. Returned by the getAdditionalClaims method.

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

##### getAdditionalClaims()

Returns a map of additional claims in the JWT, where the key string contains the name of the claim, and the value contains the value of
the claim.

Signature

```
   public Map<String,Object> getAdditionalClaims()

```

Return Value

Type: Map<String,Object>


Apex Reference Guide JWT Class

The claims returned depend on how the JWT was generated.

If the JWT was generated using other methods in the `Auth.JWT` class, this method returns the claims that were set using the
`setAdditionalClaims` method.

For JWTs generated using methods in the `[Auth.JWTUtil](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWTUtil.htm)` class, the `getAdditionalClaims` method returns all claims except
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


Apex Reference Guide JWT Class

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


Apex Reference Guide JWT Class

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


Apex Reference Guide JWT Class

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


### Apex Reference Guide JWTBearerTokenExchange Class JWTBearerTokenExchange Class

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

```


Apex Reference Guide JWTBearerTokenExchange Class

```
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

##### JWTBearerTokenExchange()

Creates an instance of the `Auth.JWTBearerTokenExchange` class.

##### JWTBearerTokenExchange(tokenEndpoint, jws)

#### Creates an instance of the JWTBearerTokenExchange class using the specified token endpoint and the signed JWT bearer token.

Signature

```
   public JWTBearerTokenExchange(String tokenEndpoint, Auth.JWS jws)

```

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


Apex Reference Guide JWTBearerTokenExchange Class

Signature

```
   public JWTBearerTokenExchange()

#### JWTBearerTokenExchange Methods The following are methods for JWTBearerTokenExchange . All are instance methods.

```

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the JWTBearerTokenExchange object.

##### getAccessToken()

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


Apex Reference Guide JWTBearerTokenExchange Class

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


Apex Reference Guide JWTBearerTokenExchange Class

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


### Apex Reference Guide JWTUtil Class

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

[See Token Exchange Handler Validation and Subject Mapping.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/token_exchange_handler.htm)

If the methods in this class fail, Salesforce returns an `Auth.JWTValidationException` exception.

IN THIS SECTION:

#### JWTUtil Methods JWTUtil Methods

### The following are methods for JWTUtil .

IN THIS SECTION:

parseJWTFromStringWithoutValidation(incomingJWT)
Parses a JWT from an encoded string into a header, payload, and signature. Use this method to decode the JWT without validating
it.

validateJWTWithCert(incomingJWT, certDeveloperName)
Parses and validates the JWT using a certificate saved in Salesforce. The certificate can be self-signed or signed by a certificate
authority.


Apex Reference Guide JWTUtil Class

##### validateJWTWithKey(incomingJWT, publicKey)

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

[Type:Auth.JWT](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWT.htm)

##### **`validateJWTWithCert(incomingJWT, certDeveloperName)`**

Parses and validates the JWT using a certificate saved in Salesforce. The certificate can be self-signed or signed by a certificate authority.

Signature

```
   public static Auth.JWT validateJWTWithCert(String incomingJWT, String certDeveloperName)

```

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

[Type: Auth.JWT](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWT.htm)

##### **`validateJWTWithKey(incomingJWT, publicKey)`**

Parses and validates the JWT using a public key from the external identity provider.


Apex Reference Guide JWTUtil Class

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

[Type: Auth.JWT](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWT.htm)

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

[Type: Auth.JWT](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWT.htm)


### Apex Reference Guide LightningLoginEligibility Enum LightningLoginEligibility Enum

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
### Login from the Session Settings Setup page.

`USER_AUTHENTICATOR_NOT_CONNECTED` The user hasn’t set up Salesforce Authenticator.

`USER_NOT_ALLOWED` The admin hasn’t granted the user AllowLightningLogin user permission. Allowing
Lightning Login to certain users requires the OnlyLLPermUserAllowed org preference.

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


Apex Reference Guide LoginDiscoveryHandler Interface

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

#### LoginDiscoveryHandler Method Here’s the method for LoginDiscoveryHandler .

IN THIS SECTION:

##### login(identifier, startUrl, requestAttributes)

Log in the customer or partner given the specified identifier, such as email or phone number. If successful, redirect the user to the
Experience Cloud site page specified by the start URL.

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


Apex Reference Guide LoginDiscoveryHandler Interface

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

```


Apex Reference Guide LoginDiscoveryHandler Interface

```
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

```


Apex Reference Guide LoginDiscoveryHandler Interface

```
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

```


Apex Reference Guide LoginDiscoveryHandler Interface

```
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

```


Apex Reference Guide LoginDiscoveryHandler Interface

```
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

```


Apex Reference Guide LoginDiscoveryHandler Interface

```
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

```


### Apex Reference Guide LoginDiscoveryMethod Enum

```
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

### MyDomainLoginDiscoveryHandler Interface

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


Apex Reference Guide MyDomainLoginDiscoveryHandler Interface

IN THIS SECTION:

#### MyDomainLoginDiscoveryHandler Method

MyDomainLoginDiscoveryHandler Example Implementation

#### MyDomainLoginDiscoveryHandler Method MyDomainLoginDiscoveryHandler has the following method.

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


Apex Reference Guide MyDomainLoginDiscoveryHandler Interface

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

```


Apex Reference Guide MyDomainLoginDiscoveryHandler Interface

```
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

```


### Apex Reference Guide Oauth2TokenExchangeHandler Class

```
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

[See Token Exchange Handler Validation and Subject Mapping.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/token_exchange_handler.htm)

IN THIS SECTION:

Oauth2TokenExchangeHandler Methods


Apex Reference Guide Oauth2TokenExchangeHandler Class

#### Oauth2TokenExchangeHandler Methods The following are methods for Oauth2TokenExchangeHandler .

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

```
   result
```

[Type: Auth.TokenValidationResult](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_TokenValidationResult.htm)

The result of the token validation performed by the `validateIncomingToken` method in the
[Auth.Oauth2TokenExchangeHandler class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_Oauth2TokenExchangeHandler.htm)

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

[Type: Auth.IntegratingAppType](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Auth_IntegratingAppType.htm)

Specifies whether your app is integrated with Salesforce as a connected app or as an external client app.

Return Value

[Type: User](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_user.htm)


### Apex Reference Guide OAuth2TokenExchangeType Enum

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

[Type: Auth.IntegratingAppType](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Auth_IntegratingAppType.htm)

Specifies whether your app is integrated with Salesforce as a connected app or as an external client app.

```
   incomingToken
```

Type: String

The token from the external identity provider.

```
   tokenType
```

[Type: Auth.OAuth2TokenExchangeType](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)

The type of token from the external identity provider. It can be an access token, a refresh token, an ID token, a SAML 2.0 assertion,
or any token that’s formatted as a JSON Web Token (JWT).

Return Value

[Type: Auth.TokenValidationResult](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_TokenValidationResult.htm)

Returns information about whether the token is valid, data extracted from the token, the token itself, and the token type. It can also
return a custom error message if the validation failed.

### OAuth2TokenExchangeType Enum

Used during the OAuth 2.0 token exchange flow to specify the type of token that’s being exchanged for a Salesforce token.

Usage

During the token exchange flow, your app requests a token from Salesforce by sending a POST request with a token from an external
identity provider. The request includes a `subject_token_type` parameter to specify the type of token. The values specified in
this enum must correspond to the `subject_token_type` in the token request.


### Apex Reference Guide OAuthRefreshResult Class

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

Namespace

Auth

Usage

### The OAuthRefreshResult class contains the parameters, accessToken, refreshToken, and error, all of which are of

type `string` . For a code example, see .

IN THIS SECTION:

#### OAuthRefreshResult Constructors

OAuthRefreshResult Properties

#### OAuthRefreshResult Constructors

### The following are constructors for OAuthRefreshResult .


Apex Reference Guide OAuthRefreshResult Class

IN THIS SECTION:

##### OAuthRefreshResult(accessToken, refreshToken, error) Creates an instance of the OAuthRefreshResult class using the specified access token, refresh token, and error for a custom

authentication provider plug-in.

##### OAuthRefreshResult(accessToken, refreshToken) Creates an instance of the OAuthRefreshResult class using the specified access token and refresh token for a custom

authentication provider plug-in. Use this method when you know that the refresh was successful.

##### OAuthRefreshResult(accessToken, refreshToken, error) Creates an instance of the OAuthRefreshResult class using the specified access token, refresh token, and error for a custom

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

##### OAuthRefreshResult(accessToken, refreshToken) Creates an instance of the OAuthRefreshResult class using the specified access token and refresh token for a custom authentication

provider plug-in. Use this method when you know that the refresh was successful.

Signature

```
   public OAuthRefreshResult(String accessToken, String refreshToken)

```

Parameters

```
   accessToken
```

Type: String

The OAuth access token for the user who is logged in.

```
   refreshToken
```

Type: String

The OAuth refresh token for the user who is logged in.


Apex Reference Guide OAuthRefreshResult Class

#### OAuthRefreshResult Properties The following are properties for OAuthRefreshResult .

IN THIS SECTION:

##### accessToken

The OAuth access token for the user who is currently logged in.

##### error

Error that occurs when a user unsuccessfully attempts to authenticate with the custom authentication provider.

##### refreshToken

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


### Apex Reference Guide OauthToken Class OauthToken Class

Contains a method to revoke OAuth access tokens and refresh tokens. This method supports opaque tokens and JSON Web Token
(JWT)-based access tokens, including guest and named user JWT-based access tokens.

Namespace

Auth

Usage

When a client completes an authorization flow and is authorized to access Salesforce data, they’re issued an access token, which the
client can use to make authenticated requests for protected Salesforce resources. The client can also use refresh tokens to get more
access tokens. If you don’t want the client to access Salesforce data anymore, revoke its Salesforce tokens.

This class is distinct from the `[Auth.AuthToken](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_AuthToken.htm)` class, which contains a method to revoke tokens issued by a third-party provider
instead of Salesforce tokens.

IN THIS SECTION:

#### OauthToken Methods OauthToken Methods

### The following are methods for OauthToken .

IN THIS SECTION:

##### revokeToken(type, authToken)

Revokes Salesforce-issued OAuth tokens.

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

[Type: Auth.OauthTokenType](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_OauthToken.htm)

Specifies the type of token to be revoked. To revoke an opaque access token, use the `ACCESS_TOKEN` value. To revoke a refresh
token and any associated access tokens, use the `REFRESH_TOKEN` value. To revoke a refresh token and associated access tokens,
use the `DELETE_TOKEN` value. To revoke a JSON Web Token (JWT)-based access token, use the `ORG_JWT` value.

```
   authToken
```

Type: String

The access token (opaque or JWT-based), refresh token, or delete token issued by Salesforce.


### Apex Reference Guide OauthTokenType Enum

Return Value

Type: Boolean

The method returns `true` if successful, and `false` if not. For invalid or expired tokens, the method returns a
`[NoDataFoundException](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)` exception.

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

### RegistrationHandler Interface

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


Apex Reference Guide RegistrationHandler Interface

IN THIS SECTION:

#### RegistrationHandler Methods

Storing User Information and Getting Access Tokens

Auth.RegistrationHandler Example Implementation

Auth.RegistrationHandler Error Example
This example implements the `Auth.RegistrationHandler` interface and shows how to use a custom exception to display
an error message in the URL of the page. If you don’t use a custom exception, the error code and description appear in the URL and
the error description appears on the page.

#### RegistrationHandler Methods The following are methods for RegistrationHandler .

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


Apex Reference Guide RegistrationHandler Interface

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
authentication provider framework converts this data into a common format with the `Auth.UserData` class and then sendsit to
the registration handler.

[Note: If you use a predefined Salesforce authentication provider, Salesforce constructs the](https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.sso_predefined_authentication_provider_parent.htm) `Auth.UserData` object for you.
[If you use a custom authentication provider plug-in, it's up to you to determine how you store information in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/authproviderplugin.htm) `Auth.UserData`
object.

If the registration handler wants to use the rest of the data, the `Auth.UserData` class has an `attributeMap` variable. The
attribute map is a map of strings ( `Map<String, String>` ) for the raw values of all the data from the third party. Because the map
is `<String, String>`, values that the third party returns that aren't strings (like an array of URLs or a map) are converted into an
appropriate string representation. The map includes everything returned by the third-party authentication provider, including the items
automatically converted into the common format.

To learn about `Auth.UserData` properties, see Auth.UserData Class.

Note: You can only perform DML operations on additional sObjects in the same transaction with User objects under certain
[circumstances. For more information, see sObjects That Cannot Be Used Together in DML Operations.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_non_mix_sobjects.htm)

For all authentication providers except Janrain, after a user is authenticated using a provider, the access token associated with that
provider for this user can be obtained in Apex using the `Auth.AuthToken` Apex class. `Auth.AuthToken` provides two methods
to retrieve access tokens. One is `getAccessToken`, which obtains a single access token. Use this method if the user ID is mapped
to a single third-party user. If the user ID is mapped to multiple third-party users, use `getAccessTokenMap`, which returns a map


Apex Reference Guide RegistrationHandler Interface

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

Salesforce doesn't validate the ID token. To validate it, use methods in the `[Auth.JWTUtil](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWTUtil.htm)` class and pass in the encoded JWT stored
in the `idToken` property. The methods in the `Auth.JWTUtil` class all return an instance of the `Auth.JWT` object.

Once you validate the JWT, you can use methods in the `[Auth.JWT](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWT.htm)` class to access specific claims. For example, the Apex code in this
snippet validates the ID token using a public keys endpoint from the identity provider and then retrieves the value of an `email` claim
stored in the token.

```
   Auth.JWT jwt = Auth.JWTUtil.validateJWTWithKeysEndpoint(userdata.idToken, keysEndpoint,

   true);

   // Retrieve email claim from id token

   String email = (String) jwt.getAdditionalClaims().get('email');

   System.debug(email);

```

Alternatively, to access specific claims in the `idTokenJSONString` property, you can deserialize the JSON string and then write
code to retrieve the claim you want. To deserialize the `idTokenJSONString`, use the `[JSON.deserialize (jsonString,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Json.htm#apex_System_Json_deserialize)`
`[apexType)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Json.htm#apex_System_Json_deserialize)` method in the `System.JSON` class.

The user info response, if returned by the identity provider, is also a JSON object that has been serialized into a string. The user info
response is stored in the `userInfoJSONString` property. You can use the `[JSON.deserialize (jsonString,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Json.htm#apex_System_Json_deserialize)`
`[apexType)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Json.htm#apex_System_Json_deserialize)` method to deserialize the user info response so that you can retrieve specific information.

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

```


Apex Reference Guide RegistrationHandler Interface

```
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

```


Apex Reference Guide RegistrationHandler Interface

```
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

#### Auth.RegistrationHandler Error Example This example implements the Auth.RegistrationHandler interface and shows how to use a custom exception to display an
```

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

```


### Apex Reference Guide SamlJitHandler Interface

```
           update(u);

        }

   }

### SamlJitHandler Interface

```

Use this interface to control and customize Just-in-Time user provisioning logic during SAML single sign-on.

Namespace

Auth

Usage

To use custom logic for user provisioning during SAML single sign-on, you must create a class that implements
`Auth.SamlJitHandler` . This allows you to incorporate organization-specific logic (such as populating custom fields) when users
log in to Salesforce with single sign-on. Keep in mind that your class must perform the logic of creating and updating user data as
appropriate, including any associated account and contact records.

In Salesforce, you specify your class that implements this interface in the `SAML JIT Handler` field in SAML Single Sign-On Settings.
Make sure that the user you specify to run the class has “Manage Users” permission.

IN THIS SECTION:

#### SamlJitHandler Methods

SamlJitHandler Example Implementation

#### SamlJitHandler Methods

### The following are methods for SamlJitHandler .

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


Apex Reference Guide SamlJitHandler Interface

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


Apex Reference Guide SamlJitHandler Interface

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

```


Apex Reference Guide SamlJitHandler Interface

```
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

```


### Apex Reference Guide SessionManagement Class

```
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


Apex Reference Guide SessionManagement Class

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


Apex Reference Guide SessionManagement Class

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


Apex Reference Guide SessionManagement Class

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


Apex Reference Guide SessionManagement Class

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

Example

##### The following example shows the name-value pairs in a map returned by getCurrentSession() . Note that UsersId includes

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

```


Apex Reference Guide SessionManagement Class

##### getLightningLoginEligibility(userId)

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

