setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

setStatus(status)
Sets the notification status value on the notification object.

##### **`setAmount(amount)`**

Sets the amount for the sale payment.


Apex Reference Guide SaleNotification Class

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


Apex Reference Guide SaleNotification Class

##### **`setGatewayMessage(gatewayMessage)`**

Sets error messages that the gateway returned for the sale request. Maximum length of 255 characters.

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


Apex Reference Guide SaleNotification Class

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


Apex Reference Guide SaleNotification Class

##### **`setRetryCategory(retryCategory)`**

Sets the retry category returned by the payment gateway for the failed payment.

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

Type: commercepayments.SalesforceResultCodeInfo on page 501


### Apex Reference Guide SaleRequest Class

Return Value

Type: void

##### **`setStatus(status)`**

Sets the notification status value on the notification object.

Signature

```
   public void setStatus(commercepayments.NotificationStatus status)

```

Parameters

```
   status
```

Type: commercepayments.NotificationStatus on page 426

Return Value

Type: void

### SaleRequest Class

Stores information about a sales request.

Namespace

CommercePayments on page 316

Usage

This class holds all the required details about a sale request. Gateway adapters read the fields of this class object while constructing a
sale JSON request thatis sent to the payment gateway. The object of this class is made available through
`commercepayments.paymentGatewayContext` by calling `getPaymentRequest()` .

Example

```
   private String buildSaleRequest(commercepayments.SaleRequest saleRequest) {

        String currencyIso = saleRequest.currencyIsoCode;

        commercepayments.SaleApiPaymentMethodRequest paymentMethod =

   saleRequest.paymentMethod;

        if (currencyIso == null) {

           currencyIso = UserInfo.getDefaultCurrency();

        }

        JSONGenerator jsonGeneratorInstance = JSON.createGenerator(true);

        jsonGeneratorInstance.writeStartObject();

       jsonGeneratorInstance.writeStringField('merchantAccount', '{!$Credential.Username}');

        jsonGeneratorInstance.writeStringField('reference',

```


Apex Reference Guide SaleRequest Class

```
   String.valueOf(Datetime.now().getTime()) + String.valueOf(Math.random()).substring(2, 8));

        jsonGeneratorInstance.writeFieldName('amount');

        jsonGeneratorInstance.writeStartObject();

        jsonGeneratorInstance.writeStringField('value', String.ValueOf((saleRequest.amount

    * 100.0).intValue()));

        jsonGeneratorInstance.writeStringField('currency', currencyIso);

        jsonGeneratorInstance.writeEndObject();

        jsonGeneratorInstance.writeFieldName('paymentMethod');

        jsonGeneratorInstance.writeStartObject();

        String shopperReference;

        String type = 'scheme';

        if (saleRequest.paymentMethodData != null) {

           String token = saleRequest.paymentMethodData.get('gatewayToken');

           String paymentMethodType =

   saleRequest.paymentMethodData.get('paymentMethodType');

           shopperReference = saleRequest.paymentMethodData.get('gatewayReference');

           if ('us_bank_account'.equals(paymentMethodType)) {

             type = 'ach';

           } else if ('sepa_debit'.equals(paymentMethodType)) {

             type = 'sepadirectdebit';

           } else if ('au_becs_debit'.equals(paymentMethodType)) {

             type = 'directdebit_AU';

           } else if ('bacs_debit'.equals(paymentMethodType)) {

             type = 'directdebit_GB';

           }

           jsonGeneratorInstance.writeStringField('type', type);

           jsonGeneratorInstance.writeStringField('storedPaymentMethodId', token);

        }

        jsonGeneratorInstance.writeEndObject();

        jsonGeneratorInstance.writeStringField('shopperInteraction', 'ContAuth');

        jsonGeneratorInstance.writeStringField('recurringProcessingModel',

   'UnscheduledCardOnFile');

        jsonGeneratorInstance.writeStringField('shopperReference', shopperReference);

        jsonGeneratorInstance.writeNumberField('captureDelayHours', 0);

        jsonGeneratorInstance.writeEndObject();

        return jsonGeneratorInstance.getAsString();

```

IN THIS SECTION:

SaleRequest Constructors

SaleRequest Properties

SaleRequest Methods


Apex Reference Guide SaleRequest Class

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

IN THIS SECTION:

accountId
Customer account ID for the sale request.

amount
Amount of the sale request. Can be positive only.

comments
Additional information about the sale request.

currencyIsoCode
Currency code for the sale request.

paymentMethod
Payment method used in the sale request.

paymentMethodData
Payment method data used in the sale request.

submittedByMerchant
Indicates whether the sale request is submitted by the marchant ( `true` ) or not ( `false` ).


Apex Reference Guide SaleRequest Class

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

##### paymentMethod

Payment method used in the sale request.


Apex Reference Guide SaleRequest Class

Signature

```
   global commercepayments.SaleApiPaymentMethodRequest paymentMethod {get; set;}

```

Property Value

Type: SaleApiPaymentMethodRequest on page 479

##### **`paymentMethodData`**

Payment method data used in the sale request.

##### This field is populated when SaleInput specifies a saved payment method. Accessible using paymentMethodData on
#### SaleRequest . The map contains these fields from SavedPaymentMethod : GatewayToken, Type, GatewayReference,

and `StandardEntryCode` for direct gateway interaction without querying the database.

Signature

```
   public Map<String,String> paymentMethodData {get; set;}

```

Property Value

Type: Map<String,String>

##### **`submittedByMerchant`**

Indicates whether the sale request is submitted by the marchant ( `true` ) or not ( `false` ).

Signature

```
   public Boolean submittedByMerchant {get; set;}

```

Property Value

Type: Boolean

#### SaleRequest Methods The following are methods for SaleRequest .

IN THIS SECTION:

equals(obj)
Compares this object with the specified object and returns `true` if both objects are equal; otherwise, returns `false` .

hashCode()
#### Maintains the integrity of lists of type SaleRequest by determining the uniqueness of the external object records in a list.

toString()
Converts a date to a string.


### Apex Reference Guide SaleResponse Class

##### equals(obj)

Compares this object with the specified object and returns `true` if both objects are equal; otherwise, returns `false` .

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

Maintains the integrity of lists of type `SaleRequest` by determining the uniqueness of the external object records in a list.

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

### SaleResponse Class

Response sent by payment gateway adapters for a sales service.

Namespace

CommercePayments on page 316


Apex Reference Guide SaleResponse Class

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.SaleResponse slr CommercePayments.SaleResponse();

```

This class contains details about a customer card that was used as a payment method for Authorization, Sale, or Tokenization request.
The gateway adapter reads the fields of this class while constructing a transaction JSON request, which it then sends to the payment
gateway. The object of this class is made available by the `cardPaymentMethod` field in `SaleApiPaymentMethodRequest`

`on page 479` and `AuthApiPaymentMethodRequest on page 342` .

Example

#### This code sample builds a SaleResponse object.

```
   commercepayments.SaleResponse saleResponse = new commercepayments.SaleResponse();

   saleResponse.setGatewayReferenceDetails("refDetailString");

   saleResponse.setGatewayResultCode("res_code");

   saleResponse.setGatewayResultCodeDescription("");

   saleResponse.setGatewayReferenceNumber("");

   saleResponse.setSalesforceResultCodeInfo(getSalesforceResultCodeInfo(commercepayments.SalesforceResultCode.SUCCESS.name()));

```

IN THIS SECTION:

#### SaleResponse Methods SaleResponse Methods The following are methods for SaleResponse .

IN THIS SECTION:

setAmount(amount)
Sets the transaction amount. Must be a non-negative value.

setAsync(async)
Indicates whether the gateway response is received asynchronously ( `true` ) or not ( `false` ). When set to `true`, the sale payment
record remains in a pending state until the async notification is received.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the sale occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the sale request. Maximum length of 255 characters.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets additional data that you can use for subsequent sales. You can use any data that isn’t normalized in financial entities. This field
has a maximum length of 1000 characters and can store data as JSON or XML.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the unique gateway reference number for the transaction that the gateway returned. Maximum length of 255 characters.


Apex Reference Guide SaleResponse Class

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

setPaymentMethodTokenizationResponse(paymentMethodTokenizationResponse)
Sets information from the gateway about the tokenized payment method.

setRetryCategory(retryCategory)
Sets the retry category returned by the payment gateway for the failed payment for a batch flow.

setRetryDecision(retryDecision)
Sets the retry decision.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

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

##### **`setAsync(async)`**

Indicates whether the gateway response is received asynchronously ( `true` ) or not ( `false` ). When set to `true`, the sale payment
record remains in a pending state until the async notification is received.

Signature

```
   public void setAsync(Boolean async)

```

Parameters

```
   async
```

Type: Boolean


Apex Reference Guide SaleResponse Class

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

Sets the date that the sale occurred. Some gateways don’t send this value.

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

Sets error messages that the gateway returned for the sale request. Maximum length of 255 characters.

Signature

```
   global void setGatewayMessage(String gatewayMessage)

```


Apex Reference Guide SaleResponse Class

Parameters

```
   gatewayMessage
```

Type: String

Return Value

Type: void

##### setGatewayReferenceDetails(gatewayReferenceDetails)

Sets additional data that you can use for subsequent sales. You can use any data that isn’t normalized in financial entities. This field has
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

Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.


Apex Reference Guide SaleResponse Class

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

Type: PaymentMethodTokenizationResponse on page 442

Gateway response sent by payment gateway adapters for the payment method tokenization request. The response includes the
payment method’s token ID value.


Apex Reference Guide SaleResponse Class

Return Value

Type: void

##### **`setRetryCategory(retryCategory)`**

Sets the retry category returned by the payment gateway for the failed payment for a batch flow.

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

##### setSalesforceResultCodeInfo(salesforceResultCodeInfo)

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce uses
the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Signature

```
   global void setSalesforceResultCodeInfo(commercepayments.SalesforceResultCodeInfo

   salesforceResultCodeInfo)

```


### Apex Reference Guide SalesforceResultCode Enum

Parameters

```
   salesforceResultCodeInfo
```

Type: SalesforceResultCodeInfo on page 502

Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

Return Value

Type: void

### SalesforceResultCode Enum

Defines the gateway call status values in Salesforce based on the call status values that the payment gateway returned.

Usage

Payment gateways can return many different responses. Salesforce maps these responses into one of seven possible Salesforce response
values.

Enum Values

The following are the values of the `commercepayments.SalesforceResultCode` enum.

**Value** **Description**

```
Decline

```

The gateway call failed, but it may still work if you try again. For example, the
customer had insufficient funds or briefly lost their connection to the internet. This
is also known as a “soft decline.”

`Indeterminate` The gateway didn't respond to the call and the user has to check the transaction
request’s status. Indeterminate responses often occur following server timeouts,

system failure, or any action that interrupts the gateway’s ability to process the
payment.

`PermanentFail` The customer’s bank recognized the payment account as closed, terminated, or
fraudulent. The gateway won’t further calls from the payment method associate

with the transaction. After a permanent fail response, the transaction changes its
gateway status to Permanent Fail.

`RequiresReview` The gateway call initially failed, but the payment method may still work after further
evaluation. This response often happens when the customer bank requires more

information about the payment request. In this case, the bank provides an
authorization code manually when the payment manager calls the processor.

`Success` The gateway processed the transaction successfully.

`SystemError` Salesforce ended the payment request call before receiving a gateway response.
System error responses often occur due to gateway server errors, invalid customer

credentials, or anytime the request times out before receiving a gateway response.
The failure occurs before the request reaches the gateway, so there’s no risk of an


### Apex Reference Guide SalesforceResultCodeInfo

**Value** **Description**

unaccounted payment remaining in the gateway. You can continue with the
transaction by manually creating a payment.

`ValidationError` The gateway received incorrect customer payment information, such as misspelled
credit card names or a CVV with missing numbers.

### SalesforceResultCodeInfo

Stores Salesforce result code information from payment gateway adapters.

Namespace

CommercePayments on page 316

Usage

The constructor of this class takes no arguments. For example:

```
   CommercePayments.SalesforceResultCodeInfo srci = new

   CommercePayments.SalesforceResultCodeInfo();

### Gateways can return the transaction result as either CustomMetadata or SalesforceResultCode .

```

IN THIS SECTION:

### SalesforceResultCodeInfo Constructors SalesforceResultCodeInfo Constructors The following are constructors for SalesforceResultCodeInfo .

IN THIS SECTION:

### SalesforceResultCodeInfo(customMetadataTypeInfo)

Constructor for providing the `customMetadataTypeInfo` for the result of the transaction.

### SalesforceResultCodeInfo(salesforceResultCode)

Constructor that provides the `salesforceResultCode` for the transaction result.

### SalesforceResultCodeInfo(customMetadataTypeInfo)

Constructor for providing the `customMetadataTypeInfo` for the result of the transaction.

Signature

```
   global SalesforceResultCodeInfo(commercepayments.CustomMetadataTypeInfo

   customMetadataTypeInfo)

```


### Apex Reference Guide StandardEntryClassCode Enum

Parameters

```
   customMetadataTypeInfo
```

Type: CustomMetadataTypeInfo on page 417

Information about the metadata type.

##### SalesforceResultCodeInfo(salesforceResultCode)

Constructor that provides the `salesforceResultCode` for the transaction result.

Signature

```
   global SalesforceResultCodeInfo(commercepayments.SalesforceResultCode

   salesforceResultCode)

```

Parameters

```
   salesforceResultCode
```

Type: SalesforceResultCode on page 501

The enum value for the result code.

### StandardEntryClassCode Enum

Specifies the three-letter code that identifies the type of electronic payment transaction being processed within the Automated Clearing
House (ACH) network.

Enum Values

The following are the values of the `commercepayments.StandardEntryClassCode` enum.

**Value** **Description**

`Ccd` —Corporate Credit or Debit

`Ppd` —Prearranged Payment and Deposit

`Tel` —Telephone-Initiated Entry

`Web` —Internet Initiated/Mobile

### TokenizeNotification Class

When a payment gateway sends a notification for a payment method tokenization, the payment gateway adapter creates the
### TokenizeNotification object to store information about notification.

Namespace

CommercePayments on page 316


Apex Reference Guide TokenizeNotification Class

Usage

`TokenizeNotification` is used in asynchronous payment gateway adapters. Specify the `CommercePayments` namespace
when creating an instance of this class. The constructor of this class takes no arguments. For example:

```
   commercePayments.TokenizeNotification Notification = new

   commercepayments.TokenizeNotification();

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

      if ('RECURRING_CONTRACT'.equals(eventCode)) {

        // NOTE: if you are consuming RECURRING_CONTRACT instead of AUTHORISATION for token

    webhook, use originalReference instead of pspReference

        commercepayments.TokenizeNotification tokenizeNotification = new

   commercepayments.TokenizeNotification();

        String gatewayToken = pspReference;

        tokenizeNotification.setGatewayTokenEncrypted(gatewayToken);

        notification = tokenizeNotification;

        String originalReference = notificationRequestItem.originalReference;

        notification.setGatewayReferenceNumber(originalReference);

      } else {

        system.debug('handling unknown event : ' + eventCode);

        commercepayments.GatewayNotificationResponse unknownEventResponse = new

   commercepayments.GatewayNotificationResponse();

        unknownEventResponse.setStatusCode(200);

```


Apex Reference Guide TokenizeNotification Class

```
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

#### TokenizeNotification Methods TokenizeNotification Methods The following are methods for TokenizeNotification .

IN THIS SECTION:

setAmount(amount)
Sets the amount.

setGatewayAvsCode(gatewayAvsCode)
Sets the AVS (address verification system) result code information that the gateway returned. Maximum length of 64 characters.

setGatewayDate(gatewayDate)
Sets the date that the sale occurred. Some gateways don’t send this value.

setGatewayMessage(gatewayMessage)
Sets error messages that the gateway returned for the sale request. Maximum length of 255 characters.

setGatewayReferenceDetails(gatewayReferenceDetails)
Sets additional data that you can use for payment tokenization. You can use any data that isn’t normalized in financial entities. This
field has a maximum length of 1000 characters and can store data as JSON or XML.

setGatewayReferenceNumber(gatewayReferenceNumber)
Sets the unique gateway reference number for the transaction that the gateway returned. Maximum length of 255 characters.

setGatewayResultCode(gatewayResultCode)
Sets a gateway-specific result code. The code may be mapped to a Salesforce-specific result code. Maximum length of 64 characters.


Apex Reference Guide TokenizeNotification Class

setGatewayResultCodeDescription(gatewayResultCodeDescription)
Sets a description of the gateway-specific result code that a payment gateway returned. Maximum length of 1000 characters.

setGatewayToken(gatewayToken)
Sets the gateway token that the gateway returned.

setGatewayTokenEncrypted(gatewayTokenEncrypted)
Sets an unencrypted unique token ID generated by the payment gateway to represent the saved payment method. Set the value
of the `gatewayTokenEncrypted` field on a SavedPaymentMethod object.

setId(id)
Sets the ID of a notification sent by the payment gateway.

setSalesforceResultCodeInfo(salesforceResultCodeInfo)
Sets the Salesforce-specific result code information. Payment gateways have many response codes for payment calls. Salesforce
uses the result code information to map payment gateway codes to a predefined set of standard Salesforce result codes.

setStatus(status)
Sets the notification status value on the notification object.

##### **`setAmount(amount)`**

Sets the amount.

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


Apex Reference Guide TokenizeNotification Class

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

Parameters

```
   gatewayMessage
```

Type: String

Return Value

Type: void

##### **`setGatewayReferenceDetails(gatewayReferenceDetails)`**

Sets additional data that you can use for payment tokenization. You can use any data that isn’t normalized in financial entities. This field
has a maximum length of 1000 characters and can store data as JSON or XML.

Signature

```
   public void setGatewayReferenceDetails(String gatewayReferenceDetails)

```

Parameters

```
   gatewayReferenceDetails
```

Type: String


Apex Reference Guide TokenizeNotification Class

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


Apex Reference Guide TokenizeNotification Class

Return Value

Type: void

##### **`setGatewayToken(gatewayToken)`**

Sets the gateway token that the gateway returned.

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

##### **`setGatewayTokenEncrypted(gatewayTokenEncrypted)`**

Sets an unencrypted unique token ID generated by the payment gateway to represent the saved payment method. Set the value of the
`gatewayTokenEncrypted` field on a SavedPaymentMethod object.

Signature

```
   public void setGatewayTokenEncrypted(String gatewayTokenEncrypted)

```

Parameters

```
   gatewayTokenEncrypted
```

Type: String

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


## Apex Reference Guide CommerceTax Namespace

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

Type: commercepayments.SalesforceResultCodeInfo on page 501

Return Value

Type: void

##### **`setStatus(status)`**

Sets the notification status value on the notification object.

Signature

```
   public void setStatus(commercepayments.NotificationStatus status)

```

Parameters

```
   status
```

Type: commercepayments.NotificationStatus on page 426

Return Value

Type: void

## CommerceTax Namespace

Manage the communication between Salesforce and an external tax engine.

## The CommerceTax namespace includes these classes.

IN THIS SECTION:

AbstractTransactionResponse Class
Abstract class that contains methods for setting tax fields based on the external tax provider's response. Response classes that extend
`AbstractTransactionResponse` inherit these methods.


Apex Reference Guide CommerceTax Namespace

AddressesResponse Class
Sets the tax address fields based on a response from the external tax engine. Contains setter methods for the Ship From, Ship To,
and Sold To addresses.

AddressResponse Class
Contains a location code sent from the external tax engine.

AmountDetailsResponse Class
Sets tax amount fields based on a response from the external tax engine.

CalculateTaxRequest Class
Represents a request to an external tax engine to calculate tax. Extends the TaxTransactionRequest class and is the top-level request
class.

CalculateTaxResponse Class
Sets the values of the tax transaction following a response from the external tax engine. Extends the AbstractTransactionResponse
class and is the top-level response class.

CalculateTaxType Enum
Shows whether a tax calculation request is for estimated or actual tax.

CustomTaxAttributesResponse Class
Sets additional data or custom attributes in the tax response.

ErrorResponse Class
[Use to respond with an error after receiving errors from the PaymentGatewayAdapter methods of the CommercePayments namespace,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_commercepayments.htm)
such as request-forbidden responses, custom validation errors, or expired API tokens.

HeaderTaxAddressesRequest Class
Captures the address values that are applicable for the quote or order transaction.

ImpositionResponse Class
Stores details of tax impositions from the external tax engine.

JurisdictionResponse Class
Stores details from the external tax engine about the tax jurisdiction used in the tax calculation process. A tax jurisdiction represents
a government entity that collects tax.

LineItemResponse Class
Response class that stores details of a list of one or more line items on which the tax engine has calculated tax.

LineTaxAddressesRequest Class
Stores details of the addresses applied per line item in a tax calculation request.

RequestType Enum
Shows the type of tax request made to the tax engine.

ResultCode Enum
Code that represents the results of a tax request made to the tax engine.

RuleDetailsResponse Class
Contains details about the tax rules used for tax calculation.

TaxAddressesRequest Class
Contains methods to get and set tax address values.

TaxAddressRequest Class
Contains address details used for tax calculation.


### Apex Reference Guide AbstractTransactionResponse Class

TaxApiException Class
Contains details about any exceptions during the tax calculation process. Extends the `ApexBaseException` class.

TaxCustomerDetailsRequest Class
Contains customer details used in tax calculation.

TaxDetailsResponse Class
Stores details of the tax values that an external tax engine calculates in response to a tax calculation request.

TaxEngineAdapter Interface
Retrieves information from the tax engine and evaluates the information to define tax details.

TaxEngineContext Class
Wrapper class that stores details about the type of a tax calculation request.

TaxLineItemRequest Class
Contains line item details of a tax request.

TaxSellerDetailsRequest Class
Contains tax code details used in the tax calculation request.

TaxTransactionRequest Class
Abstract class for storing customer details used in tax calculation and estimation requests.

TaxTransactionStatus Enum
Shows whether the tax transaction has been committed or uncommitted.

TaxTransactionType Enum
Shows whether the tax transaction is for a credit or debit transaction.

### AbstractTransactionResponse Class

Abstract class that contains methods for setting tax fields based on the external tax provider's response. Response classes that extend
### AbstractTransactionResponse inherit these methods.

Namespace

CommerceTax

IN THIS SECTION:

#### AbstractTransactionResponse Methods

Learn more about the methods for AbstractTransactionResponse class.

#### AbstractTransactionResponse Methods

Learn more about the methods for AbstractTransactionResponse class.

### The AbstractTransactionResponse class includes these methods.

IN THIS SECTION:

setAddresses(addresses)
Uses an instance of `AddressesResponse` to set the values of tax address fields.


Apex Reference Guide AbstractTransactionResponse Class

setAmountDetails(amountDetails)
Uses an instance of `AmountDetailsResponse` to set tax amount fields such as exemption amount and tax amount.

setCurrencyIsoCode(currencyIsoCode)
Sets the currencyIsoCode field.

setCustomTaxAttributes(customTaxAttributes)
Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax response at the header
level.

setDescription(dscptn)
Sets the Description field.

setDocumentCode(documentCode)
Sets the DocumentCode field. Document codes are often used to reference tax documents that the external tax engine uses in the
tax calculation process. Document code acts as a unique link to chain-related transactions, such as amendment or refunds.

setEffectiveDate(effectiveDate)
Sets the EffectiveDate field. Effective Date fields are optional fields that store the date that a transaction takes effect. We provide
these fields only for recordkeeping purposes – for example, if you must report an effective date to an external general ledger system.
Salesforce doesn't use them to calculate any tax or payment values.

setLineItems(lineItems)
Uses an instance of the `LineItemResponse` class to set a list of line items. Each line item represents an item sent to an external
tax engine for tax calculation.

setReferenceDocumentCode(referenceDocumentCode)
Sets the ReferenceDocumentCode field. Use this field to store the code of an additional document used in the tax calculation process.
For example, use this field in case of a refund for a previously taxed purchase.

setReferenceEntityId(referenceEntityId)
Sets the ID of a reference entity. In Commerce Tax, a reference entity represents a record related to the items sent to the external
tax engine for tax calculation. For example, if you sent order items for tax calculation, you could define the parent order as the
reference entity.

setTaxTransactionId(taxTrxnId)
Sets the TaxTransactionId field using the ID of a tax transaction record. In Commerce Tax, a tax transaction record stores information
about a specific tax calculation process.

setTransactionDate(transactionDate)
Sets the TransactionDate field.

##### **`setAddresses(addresses)`**

Uses an instance of `AddressesResponse` to set the values of tax address fields.

Signature

```
   global void setAddresses(commercetax.AddressesResponse addresses)

```

Parameters

```
   addresses
```

Type: AddressesResponse

Class that contains methods to set the Ship To, Ship From, and Sold To address information.


Apex Reference Guide AbstractTransactionResponse Class

Return Value

Type: void

##### **`setAmountDetails(amountDetails)`**

Uses an instance of `AmountDetailsResponse` to set tax amount fields such as exemption amount and tax amount.

Signature

```
   global void setAmountDetails(commercetax.AmountDetailsResponse amountDetails)

```

Parameters

```
   amountDetails
```

Type: AmountDetailsResponse

Class that contains methods to set the tax exemption amount, tax amount, total amount, and total amount with tax.

Return Value

Type: void

##### **`setCurrencyIsoCode(currencyIsoCode)`**

Sets the currencyIsoCode field.

Signature

```
   global void setCurrencyIsoCode(String currencyIsoCode)

```

Parameters

```
   currencyIsoCode
```

Type: String

Three-letter ISO 4217 currency code associated with a tax object.

Return Value

Type: void

##### **`setCustomTaxAttributes(customTaxAttributes)`**

Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax response at the header
level.

Signature

```
   global void setCustomTaxAttributes(commercetax.CustomTaxAttributesResponse

   customTaxAttributes)

```


Apex Reference Guide AbstractTransactionResponse Class

Parameters

```
   customTaxAttributes
```

Type: CustomTaxAttributesResponse

Additional data or custom attributes to include in the tax response.

Return Value

Type: void

##### **`setDescription(dscptn)`**

Sets the Description field.

Signature

```
   global void setDescription(String dscptn)

```

Parameters

```
   dscptn
```

Type: String

Optional field for providing additional information about a record.

Return Value

Type: void

##### **`setDocumentCode(documentCode)`**

Sets the DocumentCode field. Document codes are often used to reference tax documents that the external tax engine uses in the tax
calculation process. Document code acts as a unique link to chain-related transactions, such as amendment or refunds.

Signature

```
   global void setDocumentCode(String documentCode)

```

Parameters

```
   documentCode
```

Type: String

Code for a tax document used in the tax calculation process.

Return Value

Type: void


Apex Reference Guide AbstractTransactionResponse Class

##### **`setEffectiveDate(effectiveDate)`**

Sets the EffectiveDate field. Effective Date fields are optional fields that store the date that a transaction takes effect. We provide these
fields only for recordkeeping purposes – for example, if you must report an effective date to an external general ledger system. Salesforce
doesn't use them to calculate any tax or payment values.

Signature

```
   global void setEffectiveDate(Datetime effectiveDate)

```

Parameters

```
   effectiveDate
```

Type: Datetime

Optional field that stores the date that a transaction takes effect.

Return Value

Type: void

##### **`setLineItems(lineItems)`**

Uses an instance of the `LineItemResponse` class to set a list of line items. Each line item represents an item sent to an external
tax engine for tax calculation.

Signature

```
   global void setLineItems(List<commercetax.LineItemResponse> lineItems)

```

Parameters

```
   lineItems
```

Type: List<LineItemResponse>

A list of line items sent to an external tax engine for tax calculation.

Return Value

Type: void

##### **`setReferenceDocumentCode(referenceDocumentCode)`**

Sets the ReferenceDocumentCode field. Use this field to store the code of an additional document used in the tax calculation process.
For example, use this field in case of a refund for a previously taxed purchase.

Signature

```
   global void setReferenceDocumentCode(String referenceDocumentCode)

```


Apex Reference Guide AbstractTransactionResponse Class

Parameters

```
   referenceDocumentCode
```

Type: String

The code for a document used in the tax calculation process.

Return Value

Type: void

##### **`setReferenceEntityId(referenceEntityId)`**

Sets the ID of a reference entity. In Commerce Tax, a reference entity represents a record related to the items sent to the external tax
engine for tax calculation. For example, if you sent order items for tax calculation, you could define the parent order as the reference
entity.

Signature

```
   global void setReferenceEntityId(String referenceEntityId)

```

Parameters

```
   referenceEntityId
```

Type: String

ID of a record related to the items sent for tax calculation.

Return Value

Type: void

##### **`setTaxTransactionId(taxTrxnId)`**

Sets the TaxTransactionId field using the ID of a tax transaction record. In Commerce Tax, a tax transaction record stores information
about a specific tax calculation process.

Signature

```
   global void setTaxTransactionId(String taxTrxnId)

```

Parameters

```
   taxTrxnId
```

Type: String

The ID of a tax transaction record in Commerce Tax.

Return Value

Type: void


### Apex Reference Guide AddressesResponse Class

##### **`setTransactionDate(transactionDate)`**

Sets the TransactionDate field.

Signature

```
   global void setTransactionDate(Datetime transactionDate)

```

Parameters

```
   transactionDate
```

Type: Datetime

Date that a tax transaction occurred.

Return Value

Type: void

### AddressesResponse Class

Sets the tax address fields based on a response from the external tax engine. Contains setter methods for the Ship From, Ship To, and
Sold To addresses.

Namespace

CommerceTax

Usage

### Because AddressesResponse contains multiple addresses, we recommend using multiple instances of AddressResponse

to set unique values for each address.

Example

This code sample represents a portion of the code used in a mock tax adapter. In this example, you create three `AddressResponse`
classes, set their location codes, and pass them to the `Ship To`, `Ship From`, and `Sold To` setter methods in
### AddressesResponse . In an actual implementation, your AddressResponse classes already have a location code based on

the response from the external tax engine.

```
   commercetax.AddressesResponse addressesRes = new commercetax.AddressesResponse();

   //AddressResponse containing ShipTo information

   commercetax.AddressResponse shipToAddress = new commercetax.AddressResponse();

   shipToAddress.setLocationCode('1234567');

   //AddressResponse containing ShipFrom information

   commercetax.AddressResponse shipFromAddress = new commercetax.AddressResponse();

   shipFromAddress.setLocationCode('84720385');

   //AddressResponse containing Sold To information

```


Apex Reference Guide AddressesResponse Class

```
   commercetax.AddressResponse soldToAddress = new commercetax.AddressResponse();

   soldToAddress.setLocationCode('92381749');

   //set values of addressesRes

   addressesRes.setShipFrom(shipFromAddress);

   addressesRes.setShipTo(shipToAddress);

   addressesRes.setSoldTo(soldToAddress);

```

IN THIS SECTION:

#### AddressesResponse Methods

Learn more about the methods for AddressesResponse class.

#### AddressesResponse Methods

Learn more about the methods for AddressesResponse class.

#### The AddressesResponse class includes these methods.

IN THIS SECTION:

##### setShipFrom(shipFrom)

Sets the value of a ShipFrom address field.

setShipTo(shipTo)
Sets the value of a ShipTo address field.

setSoldTo(soldTo)
Sets the value of a SoldTo address field.

##### **`setShipFrom(shipFrom)`**

Sets the value of a ShipFrom address field.

Signature

```
   global void setShipFrom(commercetax.AddressResponse shipFrom)

```

Parameters

```
   shipFrom
```

Type: AddressResponse

A single address. Use this generic address parameter to store any type of address, such as Ship From, Ship To, and Sold To details.
#### Users set the specific address in an AddressResponse instance and then pass that instance to the AddressesResponse ’s

`setShipTo()`, `setShipFrom()`, and `setSoldTo()` methods as needed.

Return Value

Type: void


### Apex Reference Guide AddressResponse Class

##### **`setShipTo(shipTo)`**

Sets the value of a ShipTo address field.

Signature

```
   global void setShipTo(commercetax.AddressResponse shipTo)

```

Parameters

```
   shipTo
```

Type: AddressResponse

Stores a single address. This is a generic address parameter and can be used to store any type of address, such as Ship From, Ship
### To, and Sold To details. Users set the specific address in an AddressResponse instance and then pass that instance to the

`AddressesResponse` ’s `setShipTo()`, `setShipFrom()`, and `setSoldTo()` methods as needed.

Return Value

Type: void

##### **`setSoldTo(soldTo)`**

Sets the value of a SoldTo address field.

Signature

```
   global void setSoldTo(commercetax.AddressResponse soldTo)

```

Parameters

```
   soldTo
```

Type: AddressResponse

Stores a single address. This is a generic address parameter and can be used to store any type of address, such as Ship From, Ship
To, Sold To details. Users set the specific address in an AddressResponse instance and then pass that instance to the
`AddressesResponse` ’s `setShipTo()`, `setShipFrom()`, and `setSoldTo()` methods as needed.

Return Value

Type: void

### AddressResponse Class

Contains a location code sent from the external tax engine.

Namespace

CommerceTax


Apex Reference Guide AddressResponse Class

Usage

#### Use the AddressResponse class to set unique values for each address.

```
   commercetax.AddressesResponse addressesRes = new commercetax.AddressesResponse();

   //AddressResponse containing ShipTo information

   commercetax.AddressResponse shipToAddress = new commercetax.AddressResponse();

   shipToAddress.setLocationCode('1234567');

   //AddressResponse containing ShipFrom information

   commercetax.AddressResponse shipFromAddress = new commercetax.AddressResponse();

   shipFromAddress.setLocationCode('84720385');

   //AddressResponse containing Sold To information

   commercetax.AddressResponse soldToAddress = new commercetax.AddressResponse();

   soldToAddress.setLocationCode('92381749');

   //set values of addressesRes

   addressesRes.setShipFrom(shipFromAddress);

   addressesRes.setShipTo(shipToAddress);

   addressesRes.setSoldTo(soldToAddress);

```

IN THIS SECTION:

#### AddressResponse Methods Learn more about the available methods with the AddressResponse class. AddressResponse Methods Learn more about the available methods with the AddressResponse class. The AddressResponse class includes these methods.

IN THIS SECTION:

##### setLocationCode(locationCode)

Sets the value of a LocationCode field.

##### **`setLocationCode(locationCode)`**

Sets the value of a LocationCode field.

Signature

```
   global void setLocationCode(String locationCode)

```

Parameters

```
   locationCode
```

Type: String


### Apex Reference Guide AmountDetailsResponse Class

A code that contains address information. This value can be passed to a method that sets the value of an address field.

Return Value

Type: void

### AmountDetailsResponse Class

Sets tax amount fields based on a response from the external tax engine.

Namespace

CommerceTax

Example

### In this example, an instance of AmountDetailsResponse class in a mock adapter calculates several tax amount fields. The

`totalTax` and `totalAmount` parameters were defined in an instance of `LineItemResponse` class. The adapter then assigns
the instance to `lineItemResponse` .

```
   commercetax.AmountDetailsResponse amountResponse = new commercetax.AmountDetailsResponse();

   amountResponse.setTotalAmountWithTax(totalTax+totalAmount);

   amountResponse.setExemptAmount(0);

   amountResponse.setTotalAmount(totalAmount);

   amountResponse.setTaxAmount(totalTax);

   lineItemResponse.setAmountDetails(amountResponse);

```

IN THIS SECTION:

#### AmountDetailsResponse Methods
### Learn more about the methods available from the AmountDetailsResponse class.

#### AmountDetailsResponse Methods

### Learn more about the methods available from the AmountDetailsResponse class. The following are methods for AmountDetailsResponse .

IN THIS SECTION:

setExemptAmount(exemptAmount)
Sets the value of the ExemptAmount field.

setTaxAmount(taxAmount)
Sets the value of the TaxAmount field.

setTotalAmount(totalAmount)
Sets the value of the TotalAmount field.

setTotalAmountWithTax(totalAmtWithTax)
Sets the value of the TotalAmountWithTax field.


Apex Reference Guide AmountDetailsResponse Class

##### **`setExemptAmount(exemptAmount)`**

Sets the value of the ExemptAmount field.

Signature

```
   global void setExemptAmount(Double exemptAmount)

```

Parameters

```
   exemptAmount
```

Type: Double

The amount of a line item's total amount that's exempt from tax calculation.

Return Value

Type: void

##### **`setTaxAmount(taxAmount)`**

Sets the value of the TaxAmount field.

Signature

```
   global void setTaxAmount(Double taxAmount)

```

Parameters

```
   taxAmount
```

Type: Double

The calculated amount of tax for a line item.

Return Value

Type: void

##### **`setTotalAmount(totalAmount)`**

Sets the value of the TotalAmount field.

Signature

```
   global void setTotalAmount(Double totalAmount)

```

Parameters

```
   totalAmount
```

Type: Double

The total amount of a line item, excluding tax.


### Apex Reference Guide CalculateTaxRequest Class

Return Value

Type: void

##### **`setTotalAmountWithTax(totalAmtWithTax)`**

Sets the value of the TotalAmountWithTax field.

Signature

```
   global void setTotalAmountWithTax(Double totalAmtWithTax)

```

Parameters

```
   totalAmtWithTax
```

Type: Double

The total amount of a line item combined with the calculated tax for that line item.

Return Value

Type: void

### CalculateTaxRequest Class

Represents a request to an external tax engine to calculate tax. Extends the TaxTransactionRequest class and is the top-level request
class.

Namespace

CommerceTax

Usage

Keep these considerations in mind when you use this class.

**•** If the `shouldVoidTax` property value is set to `true`, then the operation returns a response with `documentCode` property
value updated to `referenceDocumentCode` property value that was originally sent in the request payload. The response also
includes the `taxTransactionType` property value as `Void` . This indicates that the document specified in the
`referenceDocumentCode` property value is voided.

**•** If document is locked or you can't void the tax transaction for any reason, then you can use the Tax Calculation request to perform
another transaction such as a Credit Tax request. In this scenario, the response includes the `documentCode` property value that
was sent in the request payload.

**•** If the document that's mentioned in the `referenceDocumentCode` property value isn't available in the tax engine, then an
error response occurs with ResultCode on page 559 value as `ReferenceDocumentCodeMissing` .

Example

### See TaxEngineAdapter Example Implementation for more details on how to access information from the CalculateTaxRequest

class.


Apex Reference Guide CalculateTaxRequest Class

IN THIS SECTION:

#### CalculateTaxRequest Constructors Learn more about the constructors that are available with the CalculateTaxRequest class. This constructor is intended for

test usage and throws an exception if used outside of the Apex test context.

#### CalculateTaxRequest Properties Learn more about the available properties with the CalculateTaxRequest class.

CalculateTaxRequest Methods
#### Learn more about the available methods with the CalculateTaxRequest class. CalculateTaxRequest Constructors Learn more about the constructors that are available with the CalculateTaxRequest class. This constructor is intended for test

usage and throws an exception if used outside of the Apex test context.

#### The CalculateTaxRequest class includes these constructors.

IN THIS SECTION:

##### CalculateTaxRequest(taxType)

This constructor is intended for test usage only and throws an exception if used outside of the Apex test context.

##### **`CalculateTaxRequest(taxType)`**

This constructor is intended for test usage only and throws an exception if used outside of the Apex test context.

Signature

```
   global CalculateTaxRequest(commercetax.CalculateTaxType taxType)

```

Parameters

```
   taxType
```

Type: CalculateTaxType

Indicates whether the tax calculation is for estimated tax or actual tax.

#### CalculateTaxRequest Properties Learn more about the available properties with the CalculateTaxRequest class. The CalculateTaxRequest class includes these properties.

IN THIS SECTION:

isCommit
Indicates whether the tax calculation has to be committed or reported to government authorities.

isHeaderTaxRequested
Indicates whether header tax is enabled in the tax engine ( `true` ) or not ( `false` ).


Apex Reference Guide CalculateTaxRequest Class

##### shouldVoidTax

Indicates whether to void the tax transaction associated with a document that's mentioned in the `referenceDocumentCode`
##### property value with taxType property value set to Actual and isCommit property value set to true . taxTransactionType

Shows whether the tax transaction is for a credit or debit transaction.

taxType
Shows whether the tax calculation is for estimated or actual tax wherein only actual tax can be submitted.

##### **`isCommit`**

Indicates whether the tax calculation has to be committed or reported to government authorities.

Signature

```
   global Boolean isCommit {get; set;}

```

Property Value

Type: Boolean

##### **`isHeaderTaxRequested`**

Indicates whether header tax is enabled in the tax engine ( `true` ) or not ( `false` ).

Signature

```
   global Boolean isHeaderTaxRequested {get; set;}

```

Property Value

Type: Boolean

##### **`shouldVoidTax`**

Indicates whether to void the tax transaction associated with a document that's mentioned in the `referenceDocumentCode`
##### property value with taxType property value set to Actual and isCommit property value set to true .

Signature

```
   global commercetax.CalculateTaxType shouldVoidTax {get; set;}

```

Property Value

Type: Boolean

##### **`taxTransactionType`**

Shows whether the tax transaction is for a credit or debit transaction.


Apex Reference Guide CalculateTaxRequest Class

Signature

```
   global commercetax.TaxTransactionType taxTransactionType {get; set;}

```

Property Value

Type: TaxTransactionType

##### **`taxType`**

Shows whether the tax calculation is for estimated or actual tax wherein only actual tax can be submitted.

Signature

```
   global commercetax.CalculateTaxType taxType {get; set;}

```

Property Value

Type: CalculateTaxType

#### CalculateTaxRequest Methods Learn more about the available methods with the CalculateTaxRequest class. The CalculateTaxRequest class includes these methods.

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type CalculateTaxRequest by determining the equality of external objects in a list. This

method is dynamic and is based on the `equals()` method in Java.

hashCode()
#### Maintains the integrity of lists of type CalculateTaxRequest by determining the uniqueness of the external object records

in a list.

toString()
Converts a value to a string.

##### **`equals(obj)`**

#### Maintains the integrity of lists of type CalculateTaxRequest by determining the equality of external objects in a list. This method

is dynamic and is based on the `equals()` method in Java.

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object


### Apex Reference Guide CalculateTaxResponse Class

External object whose key is to be validated.

Return Value

Type: Boolean

##### **`hashCode()`**

Maintains the integrity of lists of type `CalculateTaxRequest` by determining the uniqueness of the external object records in a
list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a value to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### CalculateTaxResponse Class

Sets the values of the tax transaction following a response from the external tax engine. Extends the AbstractTransactionResponse class
and is the top-level response class.

Namespace

CommerceTax

Example

```
   if(requestType == commercetax.RequestType.CalculateTax){

           commercetax.calculatetaxtype type = request.taxtype;

           String docCode='';

           if(request.DocumentCode == 'simulateEmptyDocumentCode')

              docCode = '';

           else if(request.DocumentCode != null)

              docCode =request.DocumentCode;

          else if(request.ReferenceEntityId != null) docCode = request.ReferenceEntityId;

```


Apex Reference Guide CalculateTaxResponse Class

```
           else docCode = String.valueOf(getRandomInteger(0,2147483647));

           commercetax.CalculateTaxResponse response = new

   commercetax.CalculateTaxResponse();

           if(request.isCommit == true) {

              response.setStatus(commercetax.TaxTransactionStatus.Committed);

           } else {

              response.setStatus(commercetax.TaxTransactionStatus.Uncommitted);

           }

           response.setDocumentCode(docCode);

           response.setReferenceDocumentCode(request.referenceDocumentCode);

           response.setTaxType(type);

           response.setStatusDescription('statusDescription');

           if(request.sellerDetails.code == 'testSellerCode') {

              response.setDescription('SellerCode fetched from TaxEngine entity');

           }

           else {

              response.setDescription('description');

           }

           response.setEffectiveDate(system.now());

           if(request.transactionDate == null) {

            response.setTransactionDate(system.now());

           } else {

            response.setTransactionDate(request.transactionDate);

           }

           if(request.taxTransactionType == null) {

             response.setTaxTransactionType(commercetax.TaxTransactionType.Debit);

           } else {

             response.setTaxTransactionType(request.taxTransactionType);

           }

           if(request.currencyIsoCode == null || request.currencyIsoCode == '') {

             response.setCurrencyIsoCode('USD');

           } else {

             response.setCurrencyIsoCode(request.currencyIsoCode);

           }

           response.setReferenceEntityId(request.ReferenceEntityId);

   }

```

IN THIS SECTION:

#### CalculateTaxResponse Methods Learn more about the available methods with the CalculateTaxResponse class. CalculateTaxResponse Methods Learn more about the available methods with the CalculateTaxResponse class. The CalculateTaxResponse class includes these methods.

IN THIS SECTION:

setAddresses(addresses)
Sets the value of the Addresses field using the addresses contained in an instance of the AddressesResponse class.


Apex Reference Guide CalculateTaxResponse Class

setAmountDetails(amountDetails)
Sets the value of the AmountDetails field using an instance of `AmountDetailsResponse` .

setCurrencyIsoCode(currencyIsoCode)
Sets the value of the CurrencyIsoCode field of the `CalculateTaxResponse` object.

setDescription(dscptn)
Sets the value of the Description field of the `CalculateTaxResponse` object.

setDocumentCode(documentCode)
Sets the value of the DocumentCode field of the `CalculateTaxResponse` object.

setEffectiveDate(effectiveDate)
Sets the value of the EffectiveDate field of the `CalculateTaxResponse` object.

setLineItems(lineItems)
Sets the value of the LineItems field of the `CalculateTaxResponse` object.

setReferenceDocumentCode(referenceDocumentCode)
Sets the value of the ReferenceDocumentCode field of the `CalculateTaxResponse` object.

setReferenceEntityId(referenceEntityId)
Sets the value of the ReferenceEntityId field of the `CalculateTaxResponse` object.

setStatus(status)
Sets the value of the Status field of the `CalculateTaxResponse` object.

setStatusDescription(statusDescription)
Sets the value of the StatusDescription field of the `CalculateTaxResponse` object.

setTaxTransactionId(taxTrxnId)
Sets the value of the TaxTransactionId field of the `CalculateTaxResponse` object.

setTaxTransactionType(taxTransactionType)
Sets the value of the TaxTransactionType field of the `CalculateTaxResponse` object.

setTaxType(taxType)
Sets the value of the TaxType field of the `CalculateTaxResponse` object.

setTransactionDate(transactionDate)
Sets the value of the TransactionDate field of the `CalculateTaxResponse` object.

##### **`setAddresses(addresses)`**

Sets the value of the Addresses field using the addresses contained in an instance of the AddressesResponse class.

Signature

```
   global void setAddresses(commercetax.AddressesResponse addresses)

```

Parameters

```
   addresses
```

Type: AddressesResponse

Contains Ship To, Ship From, and Sold To addresses.


Apex Reference Guide CalculateTaxResponse Class

Return Value

Type: void

##### **`setAmountDetails(amountDetails)`**

Sets the value of the AmountDetails field using an instance of `AmountDetailsResponse` .

Signature

```
   global void setAmountDetails(commercetax.AmountDetailsResponse amountDetails)

```

Parameters

```
   amountDetails
```

Type: AmountDetailsResponse

The tax amount details for a line item on which tax was calculated.

Return Value

Type: void

##### **`setCurrencyIsoCode(currencyIsoCode)`**

Sets the value of the CurrencyIsoCode field of the `CalculateTaxResponse` object.

Signature

```
   global void setCurrencyIsoCode(String currencyIsoCode)

```

Parameters

```
   currencyIsoCode
```

Type: String

Three-letter ISO 4217 currency code associated with a tax object.

Return Value

Type: void

##### **`setDescription(dscptn)`**

Sets the value of the Description field of the `CalculateTaxResponse` object.

Signature

```
   global void setDescription(String dscptn)

```


Apex Reference Guide CalculateTaxResponse Class

Parameters

```
   dscptn
```

Type: String

Optional description for providing more information about the calculate tax response.

Return Value

Type: void

##### **`setDocumentCode(documentCode)`**

Sets the value of the DocumentCode field of the `CalculateTaxResponse` object.

Signature

```
   global void setDocumentCode(String documentCode)

```

Parameters

```
   documentCode
```

Type: String

Code for a tax document that’s created by the tax engine for the calculation process.

Return Value

Type: void

##### **`setEffectiveDate(effectiveDate)`**

Sets the value of the EffectiveDate field of the `CalculateTaxResponse` object.

Signature

```
   global void setEffectiveDate(Datetime effectiveDate)

```

Parameters

```
   effectiveDate
```

Type: Datetime

The date a tax calculation action takes effect. This parameter is optional and is provided only for recordkeeping purpose. Additionally,
this parameter is used to determine the tax rates or rules and overrides the transaction date. For example, if the tax calculation
request is placed on January 3 and the transaction date is January 1, you can set the effective date as January 1.

Return Value

Type: void


Apex Reference Guide CalculateTaxResponse Class

##### **`setLineItems(lineItems)`**

Sets the value of the LineItems field of the `CalculateTaxResponse` object.

Signature

```
   global void setLineItems(List<commercetax.LineItemResponse> lineItems)

```

Parameters

```
   lineItems
```

Type: List<LineItemResponse>

Response object that the tax adapter populates from the response of the external tax engine.

Return Value

Type: void

##### **`setReferenceDocumentCode(referenceDocumentCode)`**

Sets the value of the ReferenceDocumentCode field of the `CalculateTaxResponse` object.

Signature

```
   global void setReferenceDocumentCode(String referenceDocumentCode)

```

Parameters

```
   referenceDocumentCode
```

Type: String

Code for a reference document used in the tax calculation process.

Return Value

Type: void

##### **`setReferenceEntityId(referenceEntityId)`**

Sets the value of the ReferenceEntityId field of the `CalculateTaxResponse` object.

Signature

```
   global void setReferenceEntityId(String referenceEntityId)

```

Parameters

```
   referenceEntityId
```

Type: String

ID of an entity related to the line items submitted for tax calculation. For example, if order items were sent for tax calculation, you
could use the ID of their parent order.


Apex Reference Guide CalculateTaxResponse Class

Return Value

Type: void

##### **`setStatus(status)`**

Sets the value of the Status field of the `CalculateTaxResponse` object.

Signature

```
   global void setStatus(commercetax.TaxTransactionStatus status)

```

Parameters

```
   status
```

Type: TaxTransactionStatus

Indicates whether a tax transaction has been committed.

Return Value

Type: void

##### **`setStatusDescription(statusDescription)`**

Sets the value of the StatusDescription field of the `CalculateTaxResponse` object.

Signature

```
   global void setStatusDescription(String statusDescription)

```

Parameters

```
   statusDescription
```

Type: String

Optional value for providing more information about a tax transaction's status.

Return Value

Type: void

##### **`setTaxTransactionId(taxTrxnId)`**

Sets the value of the TaxTransactionId field of the `CalculateTaxResponse` object.

Signature

```
   public void setTaxTransactionId(String taxTrxnId)

```


Apex Reference Guide CalculateTaxResponse Class

Parameters

```
   taxTrxnId
```

Type: String

The ID of the Salesforce tax transaction entity that stores information about the tax calculation transaction.

Return Value

Type: void

##### **`setTaxTransactionType(taxTransactionType)`**

Sets the value of the TaxTransactionType field of the `CalculateTaxResponse` object.

Signature

```
   global void setTaxTransactionType(commercetax.TaxTransactionType taxTransactionType)

```

Parameters

```
   taxTransactionType
```

Type: TaxTransactionType

Whether the tax transaction was for a credit, debit, or voided transaction.

Return Value

Type: void

##### **`setTaxType(taxType)`**

Sets the value of the TaxType field of the `CalculateTaxResponse` object.

Signature

```
   global void setTaxType(commercetax.CalculateTaxType taxType)

```

Parameters

```
   taxType
```

Type: CalculateTaxType

Indicates whether a tax calculation request is for estimated or actual tax.

Return Value

Type: void

##### **`setTransactionDate(transactionDate)`**

Sets the value of the TransactionDate field of the `CalculateTaxResponse` object.


### Apex Reference Guide CalculateTaxType Enum

Signature

```
   global void setTransactionDate(Datetime transactionDate)

```

Parameters

```
   transactionDate
```

Type: Datetime

The date that the tax transaction occurred.

Return Value

Type: void

### CalculateTaxType Enum

Shows whether a tax calculation request is for estimated or actual tax.

Usage

Used by the CalculateTaxRequest and CalculateTaxResponse class methods.

Enum Values

The `commercetax.CalculateTaxType` enum includes these values.

**Value** **Description**

`Actual` Specifies that the tax calculation service should calculate the finalized (actual) tax
for the requested line items.

`Estimated` Specifies that the tax calculation service should estimate the tax for the requested
line items.

### CustomTaxAttributesResponse Class

Sets additional data or custom attributes in the tax response.

Namespace

CommerceTax

IN THIS SECTION:

CustomTaxAttributesResponse Constructors
### Learn more about the available constructors with the CustomTaxAttributesResponse class.

CustomTaxAttributesResponse Methods
### Learn more about the available methods with the CustomTaxAttributesResponse class.


Apex Reference Guide CustomTaxAttributesResponse Class

#### CustomTaxAttributesResponse Constructors Learn more about the available constructors with the CustomTaxAttributesResponse class. The CustomTaxAttributesResponse class includes these constructors.

IN THIS SECTION:

##### CustomTaxAttributesResponse()

Constructor to set additional data or custom attributes in the tax response.

##### **`CustomTaxAttributesResponse()`**

Constructor to set additional data or custom attributes in the tax response.

Signature

```
   global CustomTaxAttributesResponse()

#### CustomTaxAttributesResponse Methods Learn more about the available methods with the CustomTaxAttributesResponse class. The CustomTaxAttributesResponse class includes these methods.

```

IN THIS SECTION:

##### setData(data)

Sets additional data or custom attributes in the tax response.

##### **`setData(data)`**

Sets additional data or custom attributes in the tax response.

Signature

```
   global void setData(Map<String, Object> data)

```

Parameters

```
   data
```

Type: Map<String, Object>

Additional data or custom attributes to be included in the tax response.

Return Value

Type: void


### Apex Reference Guide ErrorResponse Class ErrorResponse Class

[Use to respond with an error after receiving errors from the PaymentGatewayAdapter methods of the CommercePayments namespace,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_commercepayments.htm)
such as request-forbidden responses, custom validation errors, or expired API tokens.

Namespace

CommerceTax

Example

This example snippet of a mock tax adapter shows a hypothetical scenario to demo an error response. The adapter receives request
information from `TaxEngineContext` and stores it in an instance of `CalculateTaxRequest` . If the request's `documentCode`
property is null or indicates an error, the adapter returns an error response with information about the error.

```
   global virtual class MockAdapter implements commercetax.TaxEngineAdapter {

      global commercetax.TaxEngineResponse processRequest(commercetax.TaxEngineContext

   taxEngineContext) {

         commercetax.RequestType requestType = taxEngineContext.getRequestType();

         commercetax.CalculateTaxRequest request =

   (commercetax.CalculateTaxRequest)taxEngineContext.getRequest();

   if(request.documentCode == null) {

           return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError,

   '404', 'documentCode is mandatory');

         }

         if(request.documentCode == 'TaxEngineError') {

           return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError,

   '504', 'documentCode - not supported');

         }

         if(request.documentCode == 'simulateValidationFailureInAdapter') {

           return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError,

   '400', 'validations for documentCode failed in adapter');

         }

         if(request.documentCode == 'simulateMalformedErrorInAdapter') {

                return new

   commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, null, 'malformed adapter

    error response');

         }

         if(request.documentCode == 'simulateTaxEngineProcessFailure') {

           return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError,

   '500', 'Tax Engine couldnt process your request');

         }

```

IN THIS SECTION:

ErrorResponse Constructors
### Learn more about the available constructors with the ErrorResponse class.


### Apex Reference Guide HeaderTaxAddressesRequest Class

#### ErrorResponse Constructors Learn more about the available constructors with the ErrorResponse class. The ErrorResponse class includes these constructors.

IN THIS SECTION:

##### ErrorResponse(resultCode, errorCode, errorMessage)
#### Constructor to initialize an ErrorResponse object from the result code, error code, and error message sent from the tax engine.

##### **`ErrorResponse(resultCode, errorCode, errorMessage)`**

#### Constructor to initialize an ErrorResponse object from the result code, error code, and error message sent from the tax engine.

Signature

```
   global ErrorResponse(commercetax.ResultCode resultCode, String errorCode, String

   errorMessage)

```

Parameters

```
   resultCode
```

Type: ResultCode

Code for the type of result sent by the tax engine.

```
   errorCode
```

Type: String

Code for the type of error sent by the tax engine.

Codes must match the HTTP status codes to be returned to the user. Here are a few examples:

**•** If the status code is for a bad request, set `errorCode` to `400` .

**•** If the status code is for a forbidden request, set `errorCode` to `403` .

**•** If `errorCode` isn't a valid HTTP status code, a 500 internal server error is returned.

```
   errorMessage
```

Type: String

The error message sent by the tax engine.

### HeaderTaxAddressesRequest Class

Captures the address values that are applicable for the quote or order transaction.

Namespace

CommerceTax


Apex Reference Guide HeaderTaxAddressesRequest Class

IN THIS SECTION:

#### HeaderTaxAddressesRequest Constructors Learn more about the constructors available with the HeaderTaxAddressesRequest class.

HeaderTaxAddressesRequest Properties
#### Learn more about the available properties with the HeaderTaxAddressesRequest class.

HeaderTaxAddressesRequest Methods
#### Learn more about the available methods with the HeaderTaxAddressesRequest class. HeaderTaxAddressesRequest Constructors Learn more about the constructors available with the HeaderTaxAddressesRequest class. The HeaderTaxAddressesRequest class includes these constructors.

IN THIS SECTION:

##### HeaderTaxAddressesRequest(shipFrom, shipTo, soldTo, billTo, taxEngineAddress)

Constructor for initializing the required addresses of the tax addresses request such as the ship from, ship to, sold to, and bill to
addresses. This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

##### **`HeaderTaxAddressesRequest(shipFrom, shipTo, soldTo, billTo, taxEngineAddress)`**

Constructor for initializing the required addresses of the tax addresses request such as the ship from, ship to, sold to, and bill to addresses.
This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Signature

```
   global HeaderTaxAddressesRequest(commercetax.TaxAddressRequest shipFrom,

   commercetax.TaxAddressRequest shipTo, commercetax.TaxAddressRequest soldTo,

   commercetax.TaxAddressRequest billTo, commercetax.TaxAddressRequest taxEngineAddress)

```

Parameters

```
   shipFrom
```

Type: TaxAddressRequest

Address where a line item was shipped from.

```
   shipTo
```

Type: TaxAddressRequest

Address where a line item was shipped to.

```
   soldTo
```

Type: TaxAddressRequest

Address of the line item's buyer.

```
   billTo
```

Type: TaxAddressRequest

Person or group who was billed for the line item.


Apex Reference Guide HeaderTaxAddressesRequest Class

```
   taxEngineAddress
```

Type: TaxAddressRequest

Address that the tax engine uses to calculate tax.

#### HeaderTaxAddressesRequest Properties Learn more about the available properties with the HeaderTaxAddressesRequest class. The HeaderTaxAddressesRequest class includes these properties.

IN THIS SECTION:

##### billTo

Specifies the billTo address for a line item on which tax was calculated.

##### shipFrom

Specifies the shipFrom address for a line item on which tax was calculated.

shipTo
Specifies the shipTo address for a line item on which tax was calculated.

soldTo
Specifies the soldTo address for a line item on which tax was calculated.

taxEngineAddress
Address used by the tax engine when calculating tax for a line item.

##### **`billTo`**

Specifies the billTo address for a line item on which tax was calculated.

Signature

```
   global commercetax.TaxAddressRequest billTo {get; set;}

```

Property Value

Type: TaxAddressRequest

##### **`shipFrom`**

Specifies the shipFrom address for a line item on which tax was calculated.

Signature

```
   global commercetax.TaxAddressRequest shipFrom {get; set;}

```

Property Value

Type: TaxAddressRequest


Apex Reference Guide HeaderTaxAddressesRequest Class

##### **`shipTo`**

Specifies the shipTo address for a line item on which tax was calculated.

Signature

```
   global commercetax.TaxAddressRequest shipTo {get; set;}

```

Property Value

Type: TaxAddressRequest

##### **`soldTo`**

Specifies the soldTo address for a line item on which tax was calculated.

Signature

```
   global commercetax.TaxAddressRequest soldTo {get; set;}

```

Property Value

Type: TaxAddressRequest

##### **`taxEngineAddress`**

Address used by the tax engine when calculating tax for a line item.

Signature

```
   global commercetax.TaxAddressRequest taxEngineAddress {get; set;}

```

Property Value

Type: TaxAddressRequest

#### HeaderTaxAddressesRequest Methods Learn more about the available methods with the HeaderTaxAddressesRequest class. The HeaderTaxAddressesRequest class includes these methods.

IN THIS SECTION:

equals(obj)
#### Maintains the integrity of lists of type HeaderTaxAddressesRequest by determining the equality of external objects in a

list. This method is dynamic and is based on the `equals()` method in Java.

hashCode()
Maintains the integrity of lists of type `TaxAddressesRequest` by determining the uniqueness of the external objects in a list.

toString()
Converts a value to a string.


### Apex Reference Guide ImpositionResponse Class

##### **`equals(obj)`**

Maintains the integrity of lists of type `HeaderTaxAddressesRequest` by determining the equality of external objects in a list.
This method is dynamic and is based on the `equals()` method in Java.

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

##### **`hashCode()`**

Maintains the integrity of lists of type `TaxAddressesRequest` by determining the uniqueness of the external objects in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a value to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### ImpositionResponse Class

Stores details of tax impositions from the external tax engine.

Namespace

CommerceTax


Apex Reference Guide ImpositionResponse Class

Example

In this mock adapter example, the adapter sets the `TaxDetailsResponse.setImposition()` method parameter to null if
the request's document code indicates that the tax calculation didn't require any exceptions. Otherwise, it creates an instance of
#### ImpositionResponse and sets its SubType and Type values, and then assigns it to TaxDetailsResponse .

```
   if(request.DocumentCode == 'SetsNullForResponseWithoutException'){

     taxDetailsResponse.setImposition(null);

                }else{

                  commercetax.ImpositionResponse imposition = new

   commercetax.ImpositionResponse();

                  imposition.setSubType('subtype');

                  imposition.setType('type');

                  taxDetailsResponse.setImposition(imposition);

               }

```

IN THIS SECTION:

#### ImpositionResponse Methods Learn more about the available methods with the ImpositionResponse class. ImpositionResponse Methods Learn more about the available methods with the ImpositionResponse class. The ImpositionResponse class includes these methods.

IN THIS SECTION:

##### setId(id)
#### Sets the ID field of the ImpositionResponse class.

setName(name)
#### Sets the Name field of the ImpositionResponse class.

setSubType(subType)
#### Sets the SubType field of the ImpositionResponse class.

setType(type)
#### Sets the Type field of the ImpositionResponse class.

##### **`setId(id)`**

#### Sets the ID field of the ImpositionResponse class.

Signature

```
   global void setId(String id)

```

Parameters

```
   id
```

Type: String


Apex Reference Guide ImpositionResponse Class

User-defined ID value used for referencing the tax imposition.

Return Value

Type: void

##### **`setName(name)`**

Sets the Name field of the `ImpositionResponse` class.

Signature

```
   global void setName(String name)

```

Parameters

```
   name
```

Type: String

Optional user-defined name for the tax imposition response.

Return Value

Type: void

##### **`setSubType(subType)`**

Sets the SubType field of the `ImpositionResponse` class.

Signature

```
   global void setSubType(String subType)

```

Parameters

```
   subType
```

Type: String

Many tax calculation organizations use types and subtypes to categorize their tax imposition procedures. If the tax engine you use
follows this process, set the subtype with this parameter.

Return Value

Type: void

##### **`setType(type)`**

Sets the Type field of the `ImpositionResponse` class.

Signature

```
   public void setType(String type)

```


### Apex Reference Guide JurisdictionResponse Class

Parameters

```
   type
```

Type: String

Many tax calculation organizations use types and subtypes to categorize their tax imposition procedures. If the tax engine you use
follows this process, set the type with this parameter.

Return Value

Type: void

### JurisdictionResponse Class

Stores details from the external tax engine about the tax jurisdiction used in the tax calculation process. A tax jurisdiction represents a
government entity that collects tax.

Namespace

CommerceTax

Example

In this mock adapter example, the adapter sets the `TaxDetailsResponse.setJurisdiction()` method parameter to null
if the request's document code indicates that the tax calculation didn't require any exceptions. Otherwise, it creates an instance of
### JurisdictionResponse and sets its address values. Because this code represents a mock adapter, the example defines the

address parameters directly. In a standard implementation, the jurisdiction's setters receive values passed from the eternal tax engine.

```
   if(request.DocumentCode == 'SetsNullForResponseWithoutException'){

                  taxDetailsResponse.setJurisdiction(null);

                }else{

                  commercetax.JurisdictionResponse jurisdiction = new

   commercetax.JurisdictionResponse();

                  jurisdiction.setCountry('country');

                  jurisdiction.setRegion('region');

                  jurisdiction.setName('name');

                  jurisdiction.setStateAssignedNumber('stateAssignedNo');

                  jurisdiction.setId('id');

                  jurisdiction.setLevel('level');

                  taxDetailsResponse.setJurisdiction(jurisdiction);

   }

```

IN THIS SECTION:

#### JurisdictionResponse Methods
### Learn more about the available methods with the JurisdictionResponse class.

#### JurisdictionResponse Methods

### Learn more about the available methods with the JurisdictionResponse class.


Apex Reference Guide JurisdictionResponse Class

The `JurisdictionResponse` class includes these methods.

IN THIS SECTION:

##### setCountry(country)

Sets the Country field of the `JurisdictionResponse` class.

##### setId(id)

Sets the ID field of the `JurisdictionResponse` class.

setLevel(level)
Sets the Level field of the `JurisdictionResponse` class.

setName(name)
Sets the Name field of the `JurisdictionResponse` class.

setRegion(region)
Sets the Region value of the `JurisdictionResponse` class.

setStateAssignedNumber(stateAssignedNo)
Sets the StateAssignedNumber field of the `JurisdictionResponse` class.

##### **`setCountry(country)`**

Sets the Country field of the `JurisdictionResponse` class.

Signature

```
   global void setCountry(String country)

```

Parameters

```
   country
```

Type: String

The country of the tax jurisdiction entity's address.

Return Value

Type: void

##### **`setId(id)`**

Sets the ID field of the `JurisdictionResponse` class.

Signature

```
   global void setId(String id)

```

Parameters

```
   id
```

Type: String


Apex Reference Guide JurisdictionResponse Class

User-defined Id value used to reference the jurisdiction response.

Return Value

Type: void

##### **`setLevel(level)`**

Sets the Level field of the `JurisdictionResponse` class.

Signature

```
   global void setLevel(String level)

```

Parameters

```
   level
```

Type: String

Level value used in the jurisdiction entity's address.

Return Value

Type: void

##### **`setName(name)`**

Sets the Name field of the `JurisdictionResponse` class.

Signature

```
   global void setName(String name)

```

Parameters

```
   name
```

Type: String

Optional user-defined name field for referencing the jurisdiction response.

Return Value

Type: void

##### **`setRegion(region)`**

Sets the Region value of the `JurisdictionResponse` class.

Signature

```
   global void setRegion(String region)

```


### Apex Reference Guide LineItemResponse Class

Parameters

```
   region
```

Type: String

Region value used in the tax jurisdiction entity's address.

Return Value

Type: void

##### **`setStateAssignedNumber(stateAssignedNo)`**

Sets the StateAssignedNumber field of the `JurisdictionResponse` class.

Signature

```
   global void setStateAssignedNumber(String stateAssignedNo)

```

Parameters

```
   stateAssignedNo
```

Type: String

State assigned number value of the tax jurisdiction entity's address.

Return Value

Type: void

### LineItemResponse Class

Response class that stores details of a list of one or more line items on which the tax engine has calculated tax.

Namespace

CommerceTax

Example

### This example uses a LineItemResponse list to store information about each line item that was processed as part of the request.

For simplicity, the sample code uses a static value of 1 for the tax rate. However, most integrations typically have a more complex process
for determining a tax rate. Most integrations also build a `TaxDetailsResponse` list to store the actual tax value information that
### they assign to each line item in the LineItemResponse list.

```
   Double totalTax = 0.0;

           Double totalAmount = 0.0;

           List<commercetax.LineItemResponse> lineItemResponses = new

   List<commercetax.LineItemResponse>();

           for(Commercetax.TaxLineItemRequest lineItem : request.lineItems){

              commercetax.AddressesResponse addressesRes = new

   commercetax.AddressesResponse();

```


Apex Reference Guide LineItemResponse Class

```
              if(request.DocumentCode == 'SetsNullForResponseWithoutException'){

                addressesRes.setShipFrom(null);

                addressesRes.setShipTO(null);

                addressesRes.setSoldTo(null);

              }else{

              commercetax.AddressResponse addRes = new commercetax.AddressResponse();

                addRes.setLocationCode('locationCode');

                addressesRes.setShipFrom(addRes);

                addressesRes.setShipTO(addRes);

                addressesRes.setSoldTo(addRes);

              }

              commercetax.LineItemResponse lineItemResponse = new

   commercetax.LineItemResponse();

              Double totalLineTax = 0;

              List<commercetax.TaxDetailsResponse> taxDetailsResponses = new

   List<commercetax.TaxDetailsResponse>();

              for(integer i =0;i<1;i++){

                Integer rate = 1;

                Double taxableAmount = lineItem.amount;

                commercetax.TaxDetailsResponse taxDetailsResponse = new

   commercetax.TaxDetailsResponse();

                taxDetailsResponse.setRate(Double.valueOf(rate));

                taxDetailsResponse.setTaxableAmount(taxableAmount);

                Double tax = taxableAmount*rate;

                totalLineTax+=tax;

                taxDetailsResponse.setTax(taxableAmount*rate);

                taxDetailsResponse.setExemptAmount(0);

                taxDetailsResponse.setExemptReason('exemptReason');

                taxDetailsResponse.setTaxRegionId('taxRegionId');

   taxDetailsResponse.setTaxId(String.valueOf(getRandomInteger(0,2323233)));

                taxDetailsResponse.setSerCode('serCode');

                taxDetailsResponse.setTaxAuthorityTypeId('taxAuthorityTypeId');

                if(request.DocumentCode == 'SetsNullForResponseWithoutException'){

                  taxDetailsResponse.setImposition(null);

                }else{

                  commercetax.ImpositionResponse imposition = new

   commercetax.ImpositionResponse();

                  imposition.setSubType('subtype');

                  imposition.setType('type');

                  taxDetailsResponse.setImposition(imposition);

                }

                if(request.DocumentCode == 'SetsNullForResponseWithoutException'){

                  taxDetailsResponse.setJurisdiction(null);

                }else{

                  commercetax.JurisdictionResponse jurisdiction = new

   commercetax.JurisdictionResponse();

                  jurisdiction.setCountry('country');

                  jurisdiction.setRegion('region');

                  jurisdiction.setName('name');

                  jurisdiction.setStateAssignedNumber('stateAssignedNo');

                  jurisdiction.setId('id');

```


Apex Reference Guide LineItemResponse Class

```
                  jurisdiction.setLevel('level');

                  taxDetailsResponse.setJurisdiction(jurisdiction);

                }

                taxDetailsResponses.add(taxDetailsResponse);

              }

              lineItemResponse.setTaxes(taxDetailsResponses);

              totalTax +=totalLineTax;

              totalAmount+=lineItem.amount;

```

IN THIS SECTION:

#### LineItemResponse Methods Learn more about the available methods with the LineItemResponse class. LineItemResponse Methods Learn more about the available methods with the LineItemResponse class. The LineItemResponse class includes these methods.

IN THIS SECTION:

setAddresses(addresses)
#### Sets the Addresses field on the LineItemResponse using an instance of AddressesResponse class.

setAmountDetails(amountDetails)
#### Sets the Amount Details field on the LineItemResponse using an instance of AmountDetails .

setCustomTaxAttributes(customTaxAttributes)
Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax response at line item
level.

setEffectiveDate(effectiveDate)
#### Sets the EffectiveDate field on the LineItemResponse class. Effective Date fields are optional fields that store the date that a

transaction takes effect. We provide these fields only for recordkeeping purposes – for example, if you must report an effective date
to an external general ledger system. Salesforce doesn't use them to calculate any tax or payment values.

setIsTaxable(isTaxable)
#### Sets the IsTaxable field on the LineItemResponse class.

setLineNumber(lineNumber)
#### Sets the LineNumber field on the LineItemResponse class.

setProductCode(productCode)
#### Sets the ProductCode field on the LineItemResponse class.

setQuantity(quantity)
#### Sets the Quantity field on the LineItemResponse class.

setTaxCode(taxCode)
#### Sets the TaxCode field on the LineItemResponse .

setTaxes(taxes)
#### Sets the Taxes field on a LineItemResponse .


Apex Reference Guide LineItemResponse Class

##### **`setAddresses(addresses)`**

Sets the Addresses field on the `LineItemResponse` using an instance of `AddressesResponse` class.

Signature

```
   global void setAddresses(commercetax.AddressesResponse addresses)

```

Parameters

```
   addresses
```

Type: AddressesResponse

Class that contains methods to set the Ship To, Ship From, and Sold To address information.

Return Value

Type: void

##### **`setAmountDetails(amountDetails)`**

Sets the Amount Details field on the `LineItemResponse` using an instance of `AmountDetails` .

Signature

```
   global void setAmountDetails(commercetax.AmountDetailsResponse amountDetails)

```

Parameters

```
   amountDetails
```

Type: AmountDetailsResponse

Class that contains methods to set the tax amount, total amount with tax, total amount, and exempt amount.

Return Value

Type: void

##### **`setCustomTaxAttributes(customTaxAttributes)`**

Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax response at line item level.

Signature

```
   global void setCustomTaxAttributes(commercetax.CustomTaxAttributesResponse

   customTaxAttributes)

```

Parameters

```
   customTaxAttributes
```

Type: CustomTaxAttributesResponse

Additional data or custom attributes to include in the tax response.


Apex Reference Guide LineItemResponse Class

Return Value

Type: void

##### **`setEffectiveDate(effectiveDate)`**

Sets the EffectiveDate field on the `LineItemResponse` class. Effective Date fields are optional fields that store the date that a
transaction takes effect. We provide these fields only for recordkeeping purposes – for example, if you must report an effective date to
an external general ledger system. Salesforce doesn't use them to calculate any tax or payment values.

Signature

```
   global void setEffectiveDate(Datetime effectiveDate)

```

Parameters

```
   effectiveDate
```

Type: Datetime

Optional field that stores the date that a transaction takes effect.

Return Value

Type: void

##### **`setIsTaxable(isTaxable)`**

Sets the IsTaxable field on the `LineItemResponse` class.

Signature

```
   global void setIsTaxable(Boolean isTaxable)

```

Parameters

```
   isTaxable
```

Type: Boolean

Whether line items were taxed as part of the tax calculation request.

Return Value

Type: void

##### **`setLineNumber(lineNumber)`**

Sets the LineNumber field on the `LineItemResponse` class.

Signature

```
   global void setLineNumber(String lineNumber)

```


Apex Reference Guide LineItemResponse Class

Parameters

```
   lineNumber
```

Type: String

User-defined number used to identify a line item.

Return Value

Type: void

##### **`setProductCode(productCode)`**

Sets the ProductCode field on the `LineItemResponse` class.

Signature

```
   global void setProductCode(String productCode)

```

Parameters

```
   productCode
```

Type: String

Code for the product that a line item represents.

Return Value

Type: void

##### **`setQuantity(quantity)`**

Sets the Quantity field on the `LineItemResponse` class.

Signature

```
   global void setQuantity(Double quantity)

```

Parameters

```
   quantity
```

Type: Double

Quantity of a line item.

Return Value

Type: void

##### **`setTaxCode(taxCode)`**

Sets the TaxCode field on the `LineItemResponse` .


### Apex Reference Guide LineTaxAddressesRequest Class

Signature

```
   global void setTaxCode(String taxCode)

```

Parameters

```
   taxCode
```

Type: String

Federal code that an individual or business uses to pay their taxes to a federal or state government. The tax engine uses this code
during the tax calculation process.

Return Value

Type: void

##### **`setTaxes(taxes)`**

Sets the Taxes field on a `LineItemResponse` .

Signature

```
   global void setTaxes(List<commercetax.TaxDetailsResponse> taxes)

```

Parameters

```
   taxes
```

Type: List<TaxDetailsResponse>

Tax values applied to a line item in the `LineItemResponse` list. This information is stored in a list of `TaxDetailsResponses`,
which contains values such as tax, taxable amount, and tax rate.

Return Value

Type: void

### LineTaxAddressesRequest Class

Stores details of the addresses applied per line item in a tax calculation request.

Namespace

CommerceTax

IN THIS SECTION:

LineTaxAddressesRequest Constructors
### Learn more about the constructors available with the LineTaxAddressesRequest class.

LineTaxAddressesRequest Properties
### Learn more about the available properties with the LineTaxAddressesRequest class.


Apex Reference Guide LineTaxAddressesRequest Class

LineTaxAddressesRequest Methods
#### Learn more about the available methods with the LineTaxAddressesRequest class. LineTaxAddressesRequest Constructors Learn more about the constructors available with the LineTaxAddressesRequest class. The LineTaxAddressesRequest class includes these constructors.

IN THIS SECTION:

##### LineTaxAddressesRequest(shipFrom, shipTo, soldTo, billTo, taxEngineAddress)

Constructor for initializing the required addresses for a line item of the tax addresses request such as the ship to, ship from, and bill
to addresses. This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

##### **`LineTaxAddressesRequest(shipFrom, shipTo, soldTo, billTo, taxEngineAddress)`**

Constructor for initializing the required addresses for a line item of the tax addresses request such as the ship to, ship from, and bill to
addresses. This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Signature

```
   global LineTaxAddressesRequest(commercetax.TaxAddressRequest shipFrom,

   commercetax.TaxAddressRequest shipTo, commercetax.TaxAddressRequest soldTo,

   commercetax.TaxAddressRequest billTo, commercetax.TaxAddressRequest taxEngineAddress)

```

Parameters

```
   shipFrom
```

TaxAddressRequest

Address where a line item was shipped from.

```
   shipTo
```

TaxAddressRequest

Address where a line item is shipped to.

```
   soldTo
```

TaxAddressRequest

Address of the line item's buyer.

```
   billTo
```

TaxAddressRequest

Person or group who was billed for the line item.

```
   taxEngineAddress
```

TaxAddressRequest

Address that the tax engine uses to calculate tax.

#### LineTaxAddressesRequest Properties Learn more about the available properties with the LineTaxAddressesRequest class.


Apex Reference Guide LineTaxAddressesRequest Class

The `LineTaxAddressesRequest` class includes these properties.

IN THIS SECTION:

##### billTo

The Bill To address for a line item.

##### shipFrom

The Ship From address for a line item.

##### shipTo

The Ship To address for a line item.

soldTo
The Sold To address for a line item.

##### **`billTo`**

The Bill To address for a line item.

Signature

```
   global commercetax.TaxAddressRequest billTo {get; set;}

```

Property Value

Type: TaxAddressRequest

##### **`shipFrom`**

The Ship From address for a line item.

Signature

```
   global commercetax.TaxAddressRequest shipFrom {get; set;}

```

Property Value

Type: TaxAddressRequest

##### **`shipTo`**

The Ship To address for a line item.

Signature

```
   global commercetax.TaxAddressRequest shipTo {get; set;}

```

Property Value

Type: TaxAddressRequest


Apex Reference Guide LineTaxAddressesRequest Class

##### **`soldTo`**

The Sold To address for a line item.

Signature

```
   global commercetax.TaxAddressRequest soldTo {get; set;}

```

Property Value

Type: TaxAddressRequest

#### LineTaxAddressesRequest Methods Learn more about the available methods with the LineTaxAddressesRequest class. The LineTaxAddressesRequest class includes these methods.

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type LineTaxAddressesRequest by determining the equality of external objects in a list.

This method is dynamic and is based on the `equals()` method in Java.

hashCode()
#### Maintains the integrity of lists of type LineTaxAddressesRequest by determining the uniquness of the external object

records in a list.

toString()
Converts a value to a string.

##### **`equals(obj)`**

#### Maintains the integrity of lists of type LineTaxAddressesRequest by determining the equality of external objects in a list. This

method is dynamic and is based on the `equals()` method in Java.

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


### Apex Reference Guide RequestType Enum

##### **`hashCode()`**

Maintains the integrity of lists of type `LineTaxAddressesRequest` by determining the uniquness of the external object records
in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a value to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### RequestType Enum

Shows the type of tax request made to the tax engine.

Usage

Used by the TaxEngineContext class method.

Enum Values

The `commercetax.RequestType` enum includes these values.

**Value** **Description**

`CalculateTax` Represents a request to calculate tax on a list of taxable line items.

### ResultCode Enum

Code that represents the results of a tax request made to the tax engine.

Usage

Used by the ErrorResponse class method.


### Apex Reference Guide RuleDetailsResponse Class

Enum Values

The `commercetax.ResultCode` enum includes these values.

**Value** **Description**

`TaxEngineError` Represents an error that occurred during the tax request process.

`ReferenceDocumentCodeMissing` Specifies if the document mentioned as a `referenceDocumentCode` value
isn't available in the tax engine.

### RuleDetailsResponse Class

Contains details about the tax rules used for tax calculation.

Namespace

CommerceTax

IN THIS SECTION:

#### RuleDetailsResponse Methods
### Learn more about the available methods with the RuleDetailsResponse class.

#### RuleDetailsResponse Methods

### Learn more about the available methods with the RuleDetailsResponse class. The RuleDetailsResponse includes these methods.

IN THIS SECTION:

##### RuleDetailsResponse()

Contains information about the tax rules used when calculating tax for line items.

setNonTaxableRuleId(nonTaxableRuleId)
### Sets the NonTaxableRuleId field of the RuleDetailsResponse .

setNonTaxableType(nonTaxableType)
### Sets the NonTaxableType field of the RuleDetailsResponse .

setRateRuleId(rateRuleId)
### Sets the RateRuleId field of the RuleDetailsResponse .

setRateSourceId(rateSourceId)
### Sets the RateSourceId field on the RuleDetailsResponse .

##### **`RuleDetailsResponse()`**

Contains information about the tax rules used when calculating tax for line items.


Apex Reference Guide RuleDetailsResponse Class

Signature

```
   global void RuleDetailsResponse()

```

Return Value

Type: void

##### **`setNonTaxableRuleId(nonTaxableRuleId)`**

Sets the NonTaxableRuleId field of the `RuleDetailsResponse` .

Signature

```
   global void setNonTaxableRuleId(String nonTaxableRuleId)

```

Parameters

```
   nonTaxableRuleId
```

Type: String

ID of the tax rule applied to non-taxable line items.

Return Value

Type: void

##### **`setNonTaxableType(nonTaxableType)`**

Sets the NonTaxableType field of the `RuleDetailsResponse` .

Signature

```
   global void setNonTaxableType(String nonTaxableType)

```

Parameters

```
   nonTaxableType
```

Type: String

Reason (from several possible types) that a line item is non-taxable.

Return Value

Type: void

##### **`setRateRuleId(rateRuleId)`**

Sets the RateRuleId field of the `RuleDetailsResponse` .

Signature

```
   global void setRateRuleId(String rateRuleId)

```


### Apex Reference Guide TaxAddressesRequest Class

Parameters

```
   rateRuleId
```

Type: String

ID of the tax rule used to determine a tax rate.

Return Value

Type: void

##### **`setRateSourceId(rateSourceId)`**

Sets the RateSourceId field on the `RuleDetailsResponse` .

Signature

```
   global void setRateSourceId(String rateSourceId)

```

Parameters

```
   rateSourceId
```

Type: String

ID of the source object used for calculating tax rate.

Return Value

Type: void

### TaxAddressesRequest Class

Contains methods to get and set tax address values.

Namespace

CommerceTax

IN THIS SECTION:

#### TaxAddressesRequest Constructors
### Learn more about the available constructors with the TaxAddressesRequest class.

TaxAddressesRequest Properties
### Learn more about the available properties with the TaxAddressesRequest class.

TaxAddressesRequest Methods
### Learn more about the available methods with the TaxAddressesRequest class.

#### TaxAddressesRequest Constructors

### Learn more about the available constructors with the TaxAddressesRequest class.


Apex Reference Guide TaxAddressesRequest Class

##### The TaxAddressesRequest class includes these constructors.

IN THIS SECTION:

##### TaxAddressesRequest(shipFrom, shipTo, soldTo, billTo, taxEngineAddress)

Constructor for defining addresses for the tax addresses request. This constructor is intended for test usage and throws an exception
if used outside of the Apex test context.

##### **`TaxAddressesRequest(shipFrom, shipTo, soldTo, billTo, taxEngineAddress)`**

Constructor for defining addresses for the tax addresses request. This constructor is intended for test usage and throws an exception if
used outside of the Apex test context.

Signature

```
   global TaxAddressesRequest(commercetax.TaxAddressRequest shipFrom,

   commercetax.TaxAddressRequest shipTo, commercetax.TaxAddressRequest soldTo,

   commercetax.TaxAddressRequest billTo, commercetax.TaxAddressRequest taxEngineAddress)

```

Parameters

```
   shipFrom
```

TaxAddressRequest

The address where a line item was shipped from.

```
   shipTo
```

TaxAddressRequest

The address where a line item is shipped to.

```
   soldTo
```

TaxAddressRequest

The address of the line item's buyer.

```
   billTo
```

TaxAddressRequest

The person or group who was billed for the line item.

```
   taxEngineAddress
```

TaxAddressRequest

The address that the tax engine uses to calculate tax.

#### TaxAddressesRequest Properties

##### Learn more about the available properties with the TaxAddressesRequest class. The TaxAddressesRequest class includes these properties.

IN THIS SECTION:

billTo
The Bill To address for a line item.


Apex Reference Guide TaxAddressesRequest Class

##### shipFrom

The Ship From address for a line item.

##### shipTo

The Ship To address for a line item.

##### soldTo

The Sold To address for a line item.

taxEngineAddress
The Tax Engine Address for a line item.

##### **`billTo`**

The Bill To address for a line item.

Signature

```
   global commercetax.TaxAddressRequest billTo {get; set;}

```

Property Value

TaxAddressRequest

##### **`shipFrom`**

The Ship From address for a line item.

Signature

```
   global commercetax.TaxAddressRequest shipFrom {get; set;}

```

Property Value

TaxAddressRequest

##### **`shipTo`**

The Ship To address for a line item.

Signature

```
   public commercetax.TaxAddressRequest shipTo {get; set;}

```

Property Value

TaxAddressRequest

##### **`soldTo`**

The Sold To address for a line item.


Apex Reference Guide TaxAddressesRequest Class

Signature

```
   global commercetax.TaxAddressRequest soldTo {get; set;}

```

Property Value

TaxAddressRequest

##### **`taxEngineAddress`**

The Tax Engine Address for a line item.

Signature

```
   global commercetax.TaxAddressRequest taxEngineAddress {get; set;}

```

Property Value

TaxAddressRequest

#### TaxAddressesRequest Methods Learn more about the available methods with the TaxAddressesRequest class. The TaxAddressesRequest class includes these methods.

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type TaxAddressesRequest by determining the equality of external objects in a list. This

method is dynamic and is based on the `equals()` method in Java.

hashCode()
#### Maintains the integrity of lists of type TaxAddressesRequest by determining the uniqueness of the external object records

in a list.

toString()
Converts a value to a string.

##### **`equals(obj)`**

#### Maintains the integrity of lists of type TaxAddressesRequest by determining the equality of external objects in a list. This method

is dynamic and is based on the `equals()` method in Java.

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object


### Apex Reference Guide TaxAddressRequest Class

External object whose key is to be validated.

Return Value

Type: Boolean

##### **`hashCode()`**

Maintains the integrity of lists of type `TaxAddressesRequest` by determining the uniqueness of the external object records in a
list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a value to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### TaxAddressRequest Class

Contains address details used for tax calculation.

Namespace

CommerceTax

IN THIS SECTION:

TaxAddressRequest Constructors
### Learn more about the available constructors with the TaxAddressRequest class.

TaxAddressRequest Properties
### Learn more about the available properties with the TaxAddressRequest class.

TaxAddressRequest Methods
### Learn more about the available methods with the TaxAddressRequest class.


Apex Reference Guide TaxAddressRequest Class

#### TaxAddressRequest Constructors Learn more about the available constructors with the TaxAddressRequest class. The TaxAddressRequest class includes these constructors.

IN THIS SECTION:

##### TaxAddressRequest(city, country, latitude, longitude, postalCode, state, street, locationCode)
#### Initializes the TaxAddressRequest object using address details. This constructor is intended for test usage and throws an

exception if used outside of the Apex test context.

##### **`TaxAddressRequest(city, country, latitude, longitude, postalCode, state,`**

```
  street, locationCode)

#### Initializes the TaxAddressRequest object using address details. This constructor is intended for test usage and throws an exception
```

if used outside of the Apex test context.

Signature

```
   global TaxAddressRequest(String city, String country, Double latitude, Double longitude,

   String postalCode, String state, String street, String locationCode)

```

Parameters

```
   city
```

Type: String

City used in an address, which is required for tax calculation.

```
   country
```

Type: String

Country used in an address, which is required for tax calculation.

```
   latitude
```

Type: Double

Latitude used in an address, which is required for tax calculation.

```
   longitude
```

Type: Double

Longitude used in an address, which is required for tax calculation.

```
   postalCode
```

Type: String

Postal code used in an address, which is required for tax calculation.

```
   state
```

Type: String

State used in an address, which is required for tax calculation.

```
   street
```

Type: String

Street used in an address, which is required for tax calculation.


Apex Reference Guide TaxAddressRequest Class

```
   locationCode
```

Type: String

Location code used in an address, which is required for tax calculation.

#### TaxAddressRequest Properties Learn more about the available properties with the TaxAddressRequest class. The TaxAddressRequest class includes these properties.

IN THIS SECTION:

##### city

City used in an address, which is required for tax calculation.

country
Country used in an address, which is required for tax calculation.

countryCode
Country code used in an address, which is required for tax calculation.

latitude
Latitude used in an address, which is required for tax calculation.

locationCode
Location code used in an address, which is required for tax calculation.

longitude
Longitude used in an address, which is required for tax calculation.

postalCode
Postal code used in an address, which is required for tax calculation.

state
State used in an address, which is required for tax calculation.

stateCode
State code used in an address, which is required for tax calculation.

street
Street used in an address, which is required for tax calculation.

##### **`city`**

City used in an address, which is required for tax calculation.

Signature

```
   global String city {get; set;}

```

Property Value

Type: String


Apex Reference Guide TaxAddressRequest Class

##### **`country`**

Country used in an address, which is required for tax calculation.

Signature

```
   global String country {get; set;}

```

Property Value

Type: String

##### **`countryCode`**

Country code used in an address, which is required for tax calculation.

Signature

```
   global String countryCode {get; set;}

```

Property Value

Type: String

##### **`latitude`**

Latitude used in an address, which is required for tax calculation.

Signature

```
   global Double latitude {get; set;}

```

Property Value

Type: Double

##### **`locationCode`**

Location code used in an address, which is required for tax calculation.

Signature

```
   global String locationCode {get; set;}

```

Property Value

Type: String

##### **`longitude`**

Longitude used in an address, which is required for tax calculation.


Apex Reference Guide TaxAddressRequest Class

Signature

```
   global Double longitude {get; set;}

```

Property Value

Type: Double

##### **`postalCode`**

Postal code used in an address, which is required for tax calculation.

Signature

```
   global String postalCode {get; set;}

```

Property Value

Type: String

##### **`state`**

State used in an address, which is required for tax calculation.

Signature

```
   global String state {get; set;}

```

Property Value

Type: String

##### **`stateCode`**

State code used in an address, which is required for tax calculation.

Signature

```
   global String stateCode {get; set;}

```

Property Value

Type: String

##### **`street`**

Street used in an address, which is required for tax calculation.

Signature

```
   global String street {get; set;}

```


Apex Reference Guide TaxAddressRequest Class

Property Value

Type: String

#### TaxAddressRequest Methods Learn more about the available methods with the TaxAddressRequest class. The TaxAddressRequest class includes these methods.

IN THIS SECTION:

##### equals(obj)

Maintains the integrity of lists of type TaxAddressRequest by determining the equality of external objects in a list. This method is
dynamic and based on the `equals()` method in Java.

##### hashCode()
#### Maintains the integrity of lists of type TaxAddressRequest by determining the uniqueness of the external object in a list.

toString()
Converts a date to a string.

##### **`equals(obj)`**

Maintains the integrity of lists of type TaxAddressRequest by determining the equality of external objects in a list. This method is dynamic
and based on the `equals()` method in Java.

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

##### **`hashCode()`**

#### Maintains the integrity of lists of type TaxAddressRequest by determining the uniqueness of the external object in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer


### Apex Reference Guide TaxApiException Class

##### **`toString()`**

Converts a date to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### TaxApiException Class

Contains details about any exceptions during the tax calculation process. Extends the `ApexBaseException` class.

Namespace

CommerceTax

IN THIS SECTION:

#### TaxApiException Constructors
### Learn more about the available constructors with the TaxApiException class.

#### TaxApiException Constructors

### Learn more about the available constructors with the TaxApiException class. The TaxApiException class includes these constructors.

IN THIS SECTION:

##### TaxApiException(var1, var2)
### Initializes the TaxApiException class using an Exception and a string to provide more details about the exception. This

constructor is intended for test usage and throws an exception if used outside of the Apex test context.

TaxApiException(var1)
### Initializes the TaxApiException class using an Exception . This constructor is intended for test usage and throws an

exception if used outside of the Apex test context.

TaxApiException()
### Initializes the TaxApiException class without any initialized parameters. This constructor is intended for test usage and throws

an exception if used outside of the Apex test context.

##### **`TaxApiException(var1, var2)`**

### Initializes the TaxApiException class using an Exception and a string to provide more details about the exception. This

constructor is intended for test usage and throws an exception if used outside of the Apex test context.


### Apex Reference Guide TaxCustomerDetailsRequest Class

Signature

```
   global TaxApiException(String var1, Exception var2)

```

Parameters

```
   var1
```

Type: String

Text that provides more information about the returned exception.

```
   var2
```

[Type: Exception](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

An exception denotes an error that disrupts the normal flow of code execution. You can use Apex built-in exceptions or create
custom exceptions. All exceptions have common methods.

##### **`TaxApiException(var1)`** Initializes the TaxApiException class using an Exception . This constructor is intended for test usage and throws an exception

if used outside of the Apex test context.

Signature

```
   global TaxApiException(Exception var1)

```

Parameters

```
   var1
```

[Type: Exception](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

An exception denotes an error that disrupts the normal flow of code execution. You can use Apex built-in exceptions or create
custom exceptions. All exceptions have common methods.

##### **`TaxApiException()`** Initializes the TaxApiException class without any initialized parameters. This constructor is intended for test usage and throws an

exception if used outside of the Apex test context.

Signature

```
   global TaxApiException()

### TaxCustomerDetailsRequest Class

```

Contains customer details used in tax calculation.

Namespace

CommerceTax


Apex Reference Guide TaxCustomerDetailsRequest Class

IN THIS SECTION:

#### TaxCustomerDetailsRequest Constructors Learn more about the available constructors with the TaxCustomerDetailsRequest class.

TaxCustomerDetailsRequest Properties
#### Learn more about the available properties with the TaxCustomerDetailsRequest class.

TaxCustomerDetailsRequest Methods
#### Learn more about the available methods with the TaxCustomerDetailsRequest class. TaxCustomerDetailsRequest Constructors Learn more about the available constructors with the TaxCustomerDetailsRequest class. The TaxCustomerDetailsRequest class includes these constructors.

IN THIS SECTION:

##### TaxCustomerDetailsRequest(accountId, code, exemptionNo, exemptionReason)
#### Initializes the TaxCustomerDetailsRequest object. This constructor is intended for test usage and throws an exception if

used outside of the Apex test context.

##### **`TaxCustomerDetailsRequest(accountId, code, exemptionNo, exemptionReason)`**

#### Initializes the TaxCustomerDetailsRequest object. This constructor is intended for test usage and throws an exception if used

outside of the Apex test context.

Signature

```
   global TaxCustomerDetailsRequest(String accountId, String code, String exemptionNo,

   String exemptionReason)

```

Parameters

```
   accountId
```

Type: String

The customer account ID for the line items sent for tax calculation.

```
   code
```

Type: String

The tax code used during tax calculation.

```
   exemptionNo
```

Type: String

The exemption number applied to any tax exempt line items.

```
   exemptionReason
```

Type: String

The reason that certain line items are tax exempt.


Apex Reference Guide TaxCustomerDetailsRequest Class

#### TaxCustomerDetailsRequest Properties Learn more about the available properties with the TaxCustomerDetailsRequest class. The TaxCustomerDetailsRequest class includes these properties.

IN THIS SECTION:

##### accountId

Customer account that contains the line items sent for tax calculation.

##### code

Tax code used during tax calculation.

##### exemptionNo

Number used to qualify a line item for tax exemption.

exemptionReason
Reason why a line item qualifies for tax exemption.

taxCertificateId
ID of a tax certificate used for tax calculation.

##### **`accountId`**

Customer account that contains the line items sent for tax calculation.

Signature

```
   global String accountId {get; set;}

```

Property Value

Type: String

##### **`code`**

Tax code used during tax calculation.

Signature

```
   global String code {get; set;}

```

Property Value

Type: String

##### **`exemptionNo`**

Number used to qualify a line item for tax exemption.


Apex Reference Guide TaxCustomerDetailsRequest Class

Signature

```
   global String exemptionNo {get; set;}

```

Property Value

Type: String

##### **`exemptionReason`**

Reason why a line item qualifies for tax exemption.

Signature

```
   global String exemptionReason {get; set;}

```

Property Value

Type: String

##### **`taxCertificateId`**

ID of a tax certificate used for tax calculation.

Signature

```
   global String taxCertificateId {get; set;}

```

Property Value

Type: String

#### TaxCustomerDetailsRequest Methods Learn more about the available methods with the TaxCustomerDetailsRequest class. The TaxCustomerDetailsRequest class includes these methods.

IN THIS SECTION:

equals(obj)
#### Maintains the integrity of lists of type TaxCustomerDetailsRequest by determining the equality of external objects in a

list. This method is dynamic and based on the `equals()` method in Java.

hashCode()
#### Maintains the integrity of lists of type TaxCustomerDetailsRequest by determining the uniqueness of the external objects

in a list.

toString()
Converts a value to a string.


### Apex Reference Guide TaxDetailsResponse Class

##### **`equals(obj)`**

Maintains the integrity of lists of type `TaxCustomerDetailsRequest` by determining the equality of external objects in a list.
This method is dynamic and based on the `equals()` method in Java.

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

##### **`hashCode()`**

Maintains the integrity of lists of type `TaxCustomerDetailsRequest` by determining the uniqueness of the external objects in
a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a value to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### TaxDetailsResponse Class

Stores details of the tax values that an external tax engine calculates in response to a tax calculation request.


Apex Reference Guide TaxDetailsResponse Class

Namespace

CommerceTax

Usage

If your tax calculation request contains multiple line items, we recommend building your adapter using a list of `TaxDetailsResponse`
instances. Each instance represents the tax details calculated for a given line item.

Example

```
   List<commercetax.TaxDetailsResponse> taxDetailsResponses = new

   List<commercetax.TaxDetailsResponse>();

              for(integer i =0;i<1;i++){

                Integer rate = 1;

                Double taxableAmount = lineItem.amount;

                commercetax.TaxDetailsResponse taxDetailsResponse = new

   commercetax.TaxDetailsResponse();

                taxDetailsResponse.setRate(Double.valueOf(rate));

                taxDetailsResponse.setTaxableAmount(taxableAmount);

                Double tax = taxableAmount*rate;

                totalLineTax+=tax;

                taxDetailsResponse.setTax(taxableAmount*rate);

                taxDetailsResponse.setExemptAmount(0);

                taxDetailsResponse.setExemptReason('exemptReason');

                taxDetailsResponse.setTaxRegionId('taxRegionId');

   taxDetailsResponse.setTaxId(String.valueOf(getRandomInteger(0,2323233)));

                taxDetailsResponse.setSerCode('serCode');

                taxDetailsResponse.setTaxAuthorityTypeId('taxAuthorityTypeId');

                if(request.DocumentCode == 'SetsNullForResponseWithoutException'){

                  taxDetailsResponse.setImposition(null);

                }else{

                  commercetax.ImpositionResponse imposition = new

   commercetax.ImpositionResponse();

                  imposition.setSubType('subtype');

                  imposition.setType('type');

                  taxDetailsResponse.setImposition(imposition);

                }

                if(request.DocumentCode == 'SetsNullForResponseWithoutException'){

                  taxDetailsResponse.setJurisdiction(null);

                }else{

                  commercetax.JurisdictionResponse jurisdiction = new

   commercetax.JurisdictionResponse();

                  jurisdiction.setCountry('country');

                  jurisdiction.setRegion('region');

                  jurisdiction.setName('name');

                  jurisdiction.setStateAssignedNumber('stateAssignedNo');

                  jurisdiction.setId('id');

                  jurisdiction.setLevel('level');

                  taxDetailsResponse.setJurisdiction(jurisdiction);

                }

```


Apex Reference Guide TaxDetailsResponse Class

```
                taxDetailsResponses.add(taxDetailsResponse);

              }

              lineItemResponse.setTaxes(taxDetailsResponses);

              totalTax +=totalLineTax;

              totalAmount+=lineItem.amount;

```

IN THIS SECTION:

#### TaxDetailsResponse Methods Learn more about the available methods with the TaxDetailsResponse class. TaxDetailsResponse Methods Learn more about the available methods with the TaxDetailsResponse class. The TaxDetailsResponse class includes these methods.

IN THIS SECTION:

setCustomTaxAttributes(customTaxAttributes)
Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax response at the tax
line item level.

setExemptAmount(exemptAmount)
#### Sets the ExemptAmount field of the TaxDetailsResponse class.

setExemptReason(reason)
#### Sets the ExemptReason field of the TaxDetailsResponse class.

setImposition(imposition)
#### Sets the Imposition field of the TaxDetailsResponse class using an instance of the ImpositionResponse class.

setJurisdiction(jurisdiction)
#### Sets the Jurisdiction field of the TaxDetailsResponse using an instance of the JurisdictionResponse class.

setRate(rate)
#### Sets the Rate field of the TaxDetailsResponse class.

setSerCode(serCode)
#### Sets the Service Code field of the TaxDetailsResponse class.

setTax(tax)
#### Sets the Tax field of the TaxDetailsResponse class.

setTaxAuthorityTypeId(taxAuthorityTypeId)
#### Sets the TaxAuthorityTypeId field of the TaxDetailsResponse class.

setTaxId(taxId)
#### Sets the TaxId field of the TaxDetailsResponse class.

setTaxRegionId(taxRegionId)
#### Sets the TaxRegionId field on the TaxDetailsResponse class.

setTaxRuleDetails(taxRuleDetails)
#### Sets the TaxRuleDetails field of the TaxDetailsResponse class.


Apex Reference Guide TaxDetailsResponse Class

setTaxableAmount(taxableAmount)
Sets the TaxableAmount field of the `TaxDetailsResponse class` .

##### **`setCustomTaxAttributes(customTaxAttributes)`**

Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax response at the tax line
item level.

Signature

```
   global void setCustomTaxAttributes(commercetax.CustomTaxAttributesResponse

   customTaxAttributes)

```

Parameters

```
   customTaxAttributes
```

Type: CustomTaxAttributesResponse

Additional data or custom attributes to include in the tax response.

Return Value

Type: void

##### **`setExemptAmount(exemptAmount)`**

Sets the ExemptAmount field of the `TaxDetailsResponse` class.

Signature

```
   global void setExemptAmount(Double exemptAmount)

```

Parameters

```
   exemptAmount
```

Type: Double

Amount of tax on a line item that is exempt from tax calculation.

Return Value

Type: void

##### **`setExemptReason(reason)`**

Sets the ExemptReason field of the `TaxDetailsResponse` class.

Signature

```
   global void setExemptReason(String reason)

```


Apex Reference Guide TaxDetailsResponse Class

Parameters

```
   reason
```

Type: String

Optional user-defined information on why a tax exemption applies to a line item.

Return Value

Type: void

##### **`setImposition(imposition)`**

Sets the Imposition field of the `TaxDetailsResponse` class using an instance of the `ImpositionResponse` class.

Signature

```
   global void setImposition(commercetax.ImpositionResponse imposition)

```

Parameters

```
   imposition
```

Type: ImpositionResponse

Contains information about why tax was imposed on a line item.

Return Value

Type: void

##### **`setJurisdiction(jurisdiction)`**

Sets the Jurisdiction field of the `TaxDetailsResponse` using an instance of the `JurisdictionResponse` class.

Signature

```
   global void setJurisdiction(commercetax.JurisdictionResponse jurisdiction)

```

Parameters

```
   jurisdiction
```

Type: JurisdictionResponse

Contains address information about the tax jurisdiction used in the tax calculation process.

Return Value

Type: void

##### **`setRate(rate)`**

Sets the Rate field of the `TaxDetailsResponse` class.


Apex Reference Guide TaxDetailsResponse Class

Signature

```
   global void setRate(Double rate)

```

Parameters

```
   rate
```

Type: Double

Tax used during tax calculation. This value is often a decimal amount, such as 0.1 or 0.06, based on the applied tax percentage.

Return Value

Type: void

##### **`setSerCode(serCode)`**

Sets the Service Code field of the `TaxDetailsResponse` class.

Signature

```
   global void setSerCode(String serCode)

```

Parameters

```
   serCode
```

Type: String

Service code used in tax calculation.

Return Value

Type: void

##### **`setTax(tax)`**

Sets the Tax field of the `TaxDetailsResponse` class.

Signature

```
   global void setTax(Double tax)

```

Parameters

```
   tax
```

Type: Double

Amount of tax for a line item.

Return Value

Type: void


Apex Reference Guide TaxDetailsResponse Class

##### **`setTaxAuthorityTypeId(taxAuthorityTypeId)`**

Sets the TaxAuthorityTypeId field of the `TaxDetailsResponse` class.

Signature

```
   global void setTaxAuthorityTypeId(String taxAuthorityTypeId)

```

Parameters

```
   taxAuthorityTypeId
```

Type: String

ID of the organization that oversees tax collection.

Return Value

Type: void

##### **`setTaxId(taxId)`**

Sets the TaxId field of the `TaxDetailsResponse` class.

Signature

```
   global void setTaxId(String taxId)

```

Parameters

```
   taxId
```

Type: String

ID value used to determine the tax for an individual or business.

Return Value

Type: void

##### **`setTaxRegionId(taxRegionId)`**

Sets the TaxRegionId field on the `TaxDetailsResponse` class.

Signature

```
   global void setTaxRegionId(String taxRegionId)

```

Parameters

```
   taxRegionId
```

Type: String

ID of the tax region used in tax calculation. A tax region represents a geographical area where tax is applied.


### Apex Reference Guide TaxEngineAdapter Interface

Return Value

Type: void

##### **`setTaxRuleDetails(taxRuleDetails)`**

Sets the TaxRuleDetails field of the `TaxDetailsResponse` class.

Signature

```
   global void setTaxRuleDetails(commercetax.RuleDetailsResponse taxRuleDetails)

```

Parameters

```
   taxRuleDetails
```

Type: RuleDetailsResponse

Information about the Salesforce tax rules used during tax calculation.

Return Value

Type: void

##### **`setTaxableAmount(taxableAmount)`**

Sets the TaxableAmount field of the `TaxDetailsResponse class` .

Signature

```
   global void setTaxableAmount(Double taxableAmount)

```

Parameters

```
   taxableAmount
```

Type: Double

Amount that can be taxed on a line item.

Return Value

Type: void

### TaxEngineAdapter Interface

Retrieves information from the tax engine and evaluates the information to define tax details.

Namespace

CommerceTax


Apex Reference Guide TaxEngineAdapter Interface

IN THIS SECTION:

#### TaxEngineAdapter Methods Learn more about the available methods with the TaxEngineAdapter class. TaxEngineAdapter Example Implementation Refer to the example implementation of the TaxEngineAdapter interface to accept information from a tax engine and evaluate

the information to define tax details.

#### TaxEngineAdapter Methods Learn more about the available methods with the TaxEngineAdapter class. The TaxEngineAdapter class includes these methods.

IN THIS SECTION:

##### processRequest(requestType) The processRequest method takes an instance of TaxEngineContext class and returns a response with the calculated

tax details through the `TaxDetailsResponse` class or an error response through the `ErrorResponse` class.

##### **`processRequest(requestType)`** The processRequest method takes an instance of TaxEngineContext class and returns a response with the calculated tax

details through the `TaxDetailsResponse` class or an error response through the `ErrorResponse` class.

Signature

```
   global commercetax.TaxEngineResponse processRequest(commercetax.TaxEngineContext var1)

```

Parameters

```
   var1
```

Type: TaxEngineContext

Wrapper class that stores information about the type of a tax calculation request.

Return Value

Type: TaxEngineResponse

Generic interface representing a response from a tax engine.

#### TaxEngineAdapter Example Implementation Refer to the example implementation of the TaxEngineAdapter interface to accept information from a tax engine and evaluate

the information to define tax details.

Namespace

commercetax


Apex Reference Guide TaxEngineAdapter Interface

Usage

The `TaxEngineAdapter` interface accepts information from the tax engine through the `TaxEngineContext` class. The
interface evaluates the information to define tax in the response with details, such as tax amount and addresses. The response is used
to update and create entities in the Salesforce org.

Use these steps to build a sample tax adapter implementation. Each tax adapter implementation varies based on your implementation
requirements. Customize this example to suit your business requirements.

Example:

**•** The custom adapter class implements the `TaxEngineAdapter` interface. The `processRequest` method takes an
instance of `TaxEngineContext` class and returns a response with the calculated tax details through the
`TaxDetailsResponse` class or an error response through the `ErrorResponse` class.

```
       global virtual class AvalaraAdapter implements commercetax.TaxEngineAdapter {

         global commercetax.TaxEngineResponse processRequest(commercetax.TaxEngineContext

        taxEngineContext) {

            commercetax.RequestType requestType = taxEngineContext.getRequestType();

            if(requestType == commercetax.RequestType.CalculateTax){

               return CalculateTaxService.getTax(taxEngineContext);

            }

            else

               return null;

          }

       }

```

**•** This example shows the `CalculateTaxService` class.

```
       global class CalculateTaxService {

         // ============================================================================

          // CONSTANT

         // ============================================================================

          private static final String AVALARA_ENDPOINT_URL_SANDBOX =

       'https://sandbox-rest.avatax.com/api/v2';

          // Avalara Endpoint URL Production

          private static final String AVALARA_ENDPOINT_URL_PRODUCTION =

       'https://rest.avatax.com/api/v2';

         private static final String TEST_REQUEST_BODY = '{ "id": -1, "code": "00000131",

        "companyId": -1, "date": "2017-02-03T00:00:00", "taxDate": "2017-02-03T00:00:00",

        "status": "Temporary", "type": "SalesOrder", "reconciled": false, "totalAmount":

        4000, "totalExempt": 0, "totalTax": 290, "totalTaxable": 4000,

       "totalTaxCalculated": 290, "adjustmentReason": "NotAdjusted", "locked": false,

       "version": 1, "modifiedDate": "2017-02-03T12:18:18.7347388Z", "modifiedUserId":

       53894, "lines": [ { "id": -1, "transactionId": -1, "lineNumber":

        "80241000000jNDCAA2", "discountAmount": 0, "exemptAmount": 0,

       "exemptCertId": 0, "isItemTaxable": true, "lineAmount": 1000,

       "reportingDate": "2017-02-03T00:00:00", "tax": 72.5, "taxableAmount":

       1000, "taxCalculated": 72.5, "taxCode": "P0000000", "taxDate":

       "2017-02-03T00:00:00", "taxIncluded": false, "details": [ {

          "id": -1, "transactionLineId": -1, "transactionId": -1,

          "country": "US", "region": "CA", "exemptAmount": 0,

        "jurisCode": "06", "jurisName": "CALIFORNIA", "stateAssignedNo":

```


Apex Reference Guide TaxEngineAdapter Interface

```
        "", "jurisType": "STA", "nonTaxableAmount": 0, "rate":

        0.06, "tax": 60, "taxableAmount": 1000, "taxType":

       "Sales", "taxName": "CA STATE TAX", "taxAuthorityTypeId": 45,

            "taxCalculated": 60, "rateType": "General" }, {

          "id": -1, "transactionLineId": -1, "transactionId": -1,

           "country": "US", "region": "CA", "exemptAmount": 0,

         "jurisCode": "075", "jurisName": "SAN FRANCISCO",

       "stateAssignedNo": "", "jurisType": "CTY", "nonTaxableAmount": 0,

             "rate": 0.0025, "tax": 2.5, "taxableAmount": 1000,

           "taxType": "Sales", "taxName": "CA COUNTY TAX",

       "taxAuthorityTypeId": 45, "taxCalculated": 2.5, "rateType":

       "General" }, { "id": -1, "transactionLineId": -1,

             "transactionId": -1, "country": "US", "region": "CA",

            "exemptAmount": 0, "jurisCode": "EMTV0", "jurisName": "SAN

        FRANCISCO CO LOCAL TAX SL", "stateAssignedNo": "38", "jurisType":

        "STJ", "nonTaxableAmount": 0, "rate": 0.01, "tax": 10,

             "taxableAmount": 1000, "taxType": "Sales", "taxName":

       "CA SPECIAL TAX", "taxAuthorityTypeId": 45, "taxCalculated": 10,

             "rateType": "General" } ] } ]}';

          private static String getTestResponseString(){

          List<String> jsonResponse = new List<String> {

                             '"id": 0',

                             '"code": "testDocCode1231245984"',

                             '"companyId": 468039',

                             '"date": "2020-07-15"',

                             '"paymentDate": "2020-07-15"',

                             '"status": "Temporary"',

                             '"type": "SalesOrder"',

                             '"customerVendorCode": "testDocCode1234"',

                             '"customerCode": "testDocCode1234"',

                             '"reconciled": false',

                             '"totalAmount": 232',

                             '"totalExempt": 0',

                             '"totalDiscount": 0',

                             '"totalTax": 23.43',

                             '"totalTaxable": 232',

                             '"totalTaxCalculated": 23.43',

                             '"adjustmentReason": "NotAdjusted"',

                             '"locked": false',

                             '"version": 1',

                             '"exchangeRateEffectiveDate": "2020-07-15"',

                             '"exchangeRate": 1',

                           '"modifiedDate": "2020-08-13T11:19:20.4836636Z"',

                             '"modifiedUserId": 53894',

                             '"taxDate": "2020-07-15T00:00:00"',

                             '"lines": [{"id": 0,"transactionId":

       0,"lineNumber": "1","discountAmount": 0,"exemptAmount": 0,"exemptCertId":

       0,"isItemTaxable": true,"itemCode": "","lineAmount": 232,"quantity":

       1,"reportingDate": "2020-07-15","tax": 23.43,"taxableAmount": 232,"taxCalculated":

        23.43,"taxCode": "P0000000","taxCodeId": 8087,"taxDate":

       "2020-07-15","taxOverrideType": "None","taxOverrideAmount": 0,"taxIncluded":

```


Apex Reference Guide TaxEngineAdapter Interface

```
       false,"details": [{"id": 0,"transactionLineId": 0,"transactionId": 0,"country":

       "US","region": "WA","exemptAmount": 0,"jurisCode": "53","jurisName":

       "WASHINGTON","stateAssignedNo": "","jurisType": "STA","jurisdictionType":

       "State","nonTaxableAmount": 0,"rate": 0.065,"tax": 15.08,"taxableAmount":

       232,"taxType": "Sales","taxSubTypeId": "S","taxName": "WA STATE

       TAX","taxAuthorityTypeId": 45,"taxCalculated": 15.08,"rateType":

       "General","rateTypeCode": "G","unitOfBasis": "PerCurrencyUnit","isNonPassThru":

       false,"isFee": false},{"id": 0,"transactionLineId": 0,"transactionId": 0,"country":

        "US","region": "WA","exemptAmount": 0,"jurisCode": "033","jurisName":

       "KING","stateAssignedNo": "1700","jurisType": "CTY","jurisdictionType":

       "County","nonTaxableAmount": 0,"rate": 0,"tax": 0,"taxableAmount": 232,"taxType":

       "Sales","taxSubTypeId": "S","taxName": "WA COUNTY TAX","taxAuthorityTypeId":

       45,"taxCalculated": 0,"rateType": "General","rateTypeCode": "G","unitOfBasis":

       "PerCurrencyUnit","isNonPassThru": false,"isFee": false}],"nonPassthroughDetails":

        [],"hsCode": "","costInsuranceFreight": 0,"vatCode": "","vatNumberTypeId": 0}]',

                             '"addresses": [{"id": 0,"transactionId":

       0,"boundaryLevel": "Address","line1": "255 S. King Street","line2": "","line3":

       "","city": "Seattle","region": "WA","postalCode": "98104","country":

       "US","taxRegionId": 2109700,"latitude": "47.59821","longitude": "-122.33108"}]',

                             '"summary": [{"country": "US","region":

       "WA","jurisType": "State","jurisCode": "53","jurisName":

       "WASHINGTON","taxAuthorityType": 45,"stateAssignedNo": "","taxType":

       "Sales","taxSubType": "S","taxName": "WA STATE TAX","rateType": "General","taxable":

        232,"rate": 0.065,"tax": 15.08,"taxCalculated": 15.08,"nonTaxable": 0,"exemption":

        0},{"country": "US","region": "WA","jurisType": "County","jurisCode":

       "033","jurisName": "KING","taxAuthorityType": 45,"stateAssignedNo": "1700","taxType":

        "Sales","taxSubType": "S","taxName": "WA COUNTY TAX","rateType": "General","taxable":

        232,"rate": 0,"tax": 0,"taxCalculated": 0,"nonTaxable": 0,"exemption": 0}]'

                           };

               return '{' + String.join(jsonResponse, ',') + '}';

            }

         public static commercetax.TaxEngineResponse getTax(commercetax.TaxEngineContext

        taxEngineContext)

          {

            commercetax.CalculateTaxRequest request =

       (commercetax.CalculateTaxRequest)taxEngineContext.getRequest();

            commercetax.calculatetaxtype requestType = request.taxtype;

            string referenceEntity = request.ReferenceEntityId;

            try{

               List<commercetax.TaxLineItemRequest> listOfLines = request.lineItems;

               if(!listOfLines.isEmpty()){

                 HttpService sendHttpRequest = new HttpService();

                 sendHttpRequest.addHeader('Content-type', 'application/json');

                 String requestBody =

       AvalaraJSONBuilder.getInstance().frameJsonForGetTaxOrderItem(request);

                 sendHttpRequest.post('/transactions/create',requestBody);

                 //system.debug('Request '+requestBody);

                 String responseString = '';

                 if(Test.isRunningTest()){

                   responseString = getTestResponseString();

                 } else{

                   responseString = sendHttpRequest.getResponse().getBody();

                 }

```


Apex Reference Guide TaxEngineAdapter Interface

```
                 //system.debug(sendHttpRequest.getResponse());

                 //system.debug('response'+responseString);

                 //responseString = TEST_REQUEST_BODY;

                 system.debug('Heap size used ' +Limits.getHeapSize());

                 if(!responseString.contains('error'))

                 {

                   commercetax.CalculateTaxResponse response = new

       commercetax.CalculateTaxResponse();

                   JsonSuccessParser jsonSuccessParserClass =

       JsonSuccessParser.parse(responseString);

                   response.setTaxTransactionType(request.taxTransactionType);

                   response.setDocumentCode(jsonSuccessParserClass.code);

       response.setReferenceDocumentCode(jsonSuccessParserClass.referenceCode);

                   if(jsonSuccessParserClass.status == 'Temporary') {

       response.setStatus(commercetax.TaxTransactionStatus.Uncommitted);

                   }

                   if(jsonSuccessParserClass.status == 'Committed') {

       response.setStatus(commercetax.TaxTransactionStatus.Committed);

                   }

                   response.setTaxType(requestType);

                   commercetax.AmountDetailsResponse headerAmountResponse = new

       commercetax.AmountDetailsResponse();

       headerAmountResponse.setTotalAmountWithTax(jsonSuccessParserClass.totalAmount +

       jsonSuccessParserClass.totaltax);

       headerAmountResponse.setExemptAmount(jsonSuccessParserClass.totalExempt);

       headerAmountResponse.setTotalAmount(jsonSuccessParserClass.totalAmount);

       headerAmountResponse.setTaxAmount(jsonSuccessParserClass.totalTax);

                   response.setAmountDetails(headerAmountResponse);

       response.setStatusDescription(jsonSuccessParserClass.adjustmentReason);

       response.setEffectiveDate(date.valueof(jsonSuccessParserClass.taxDate));

       response.setTransactionDate(date.valueof(jsonSuccessParserClass.transactionDate));

                   response.setReferenceEntityId(referenceEntity);

                   response.setTaxTransactionId(jsonSuccessParserClass.id);

                   response.setCurrencyIsoCode(request.currencyIsoCode);

                   List<commercetax.LineItemResponse> lineItemResponses = new

       List<commercetax.LineItemResponse>();

                   for(JsonSuccessParser.Lines linesToProcess:

       jsonSuccessParserClass.lines)

                   {

                      commercetax.LineItemResponse lineItemResponse = new

       commercetax.LineItemResponse();

                      Double rateCalculated = 0.0;

                      List<commercetax.TaxDetailsResponse> taxDetailsResponses =

```


Apex Reference Guide TaxEngineAdapter Interface

```
        new List<commercetax.TaxDetailsResponse>();

                      for(JsonSuccessParser.details linesDetails :

       linesToProcess.details)

                      {

                        commercetax.TaxDetailsResponse taxDetailsResponse = new

        commercetax.TaxDetailsResponse();

                        if(linesDetails.exemptAmount != 0){

       taxDetailsResponse.setExemptAmount(linesDetails.exemptAmount);

                           taxDetailsResponse.setExemptReason('Some reason we

        dont know');

                        }

                           commercetax.ImpositionResponse imposition = new

       commercetax.ImpositionResponse();

                             imposition.setSubType(linesDetails.taxName);

                             imposition.setType(linesDetails.ratetype);

                             imposition.setSubType(linesDetails.taxName);

                             taxDetailsResponse.setImposition(imposition);

                          commercetax.JurisdictionResponse jurisdiction = new

        commercetax.JurisdictionResponse();

                             jurisdiction.setCountry(linesDetails.country);

                             jurisdiction.setRegion(linesDetails.region);

                             jurisdiction.setName(linesDetails.jurisName);

       jurisdiction.setStateAssignedNumber(linesDetails.stateAssignedNo);

                             jurisdiction.setId(linesDetails.jurisCode);

                             jurisdiction.setLevel(linesDetails.jurisType);

                           taxDetailsResponse.setJurisdiction(jurisdiction);

                             rateCalculated += linesDetails.rate;

                           taxDetailsResponse.setRate(rateCalculated);

                        taxDetailsResponse.setTax(linesDetails.taxCalculated);

       taxDetailsResponse.setTaxableAmount(linesDetails.taxableAmount);

       taxDetailsResponse.setTaxAuthorityTypeId(String.valueOf(linesDetails.taxAuthorityTypeId));

                           taxDetailsResponse.setTaxId(linesDetails.id);

       taxDetailsResponse.setTaxRegionId(linesDetails.region);

                           taxDetailsResponses.add(taxDetailsResponse);

                      }

                        lineItemResponse.setTaxes(taxDetailsResponses);

       lineItemResponse.setEffectiveDate(date.valueof(linesToProcess.taxDate));

                        lineItemResponse.setIsTaxable(true);

                           commercetax.AmountDetailsResponse amountResponse =

        new commercetax.AmountDetailsResponse();

       amountResponse.setTaxAmount(linesToProcess.taxCalculated);

       amountResponse.setTotalAmount(linesToProcess.lineAmount);

```


Apex Reference Guide TaxEngineAdapter Interface

```
       amountResponse.setTotalAmountWithTax(linesToProcess.lineAmount+linesToProcess.taxCalculated);

       amountResponse.setExemptAmount(linesToProcess.exemptAmount);

                           lineItemResponse.setAmountDetails(amountResponse);

       lineItemResponse.setIsTaxable(linesToProcess.isItemTaxable);

                      lineItemResponse.setProductCode(linesToProcess.itemCode);

                        lineItemResponse.setTaxCode(linesToProcess.taxCode);

                      lineItemResponse.setLineNumber(linesToProcess.lineNumber);

                        lineItemResponse.setQuantity(linesToProcess.quantity);

                        lineItemResponses.add(lineItemResponse);

                   }

                   response.setLineItems(lineItemResponses);

                   return response;

                 }

                 else

                 {

                   JsonErrorParser jsonErrorParserClass =

       JsonErrorParser.parse(responseString);

                   String message = null;

                   if(String.isNotBlank(jsonErrorParserClass.error.message))

                   {

                     message=jsonErrorParserClass.error.message;

                   }else{

                        String errorMessage = '';

                        for(JsonErrorParser.cls_details messageString :

       jsonErrorParserClass.error.details)

                        {

                           if(String.isNotBlank(messageString.message) )

                           {

                             errorMessage = messageString.message;

                           }

                        }

                        message = errorMessage;

                      }

                    return new

       commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, '501', message);

                 }

               }else return null;

            }

            catch (Exception e)

            {

               throw e;

            }

          }

       }

```


Apex Reference Guide TaxEngineAdapter Interface

**•** In the `HttpService` class, replace the `test` value in the endpoint variable with the name of the
`TaxTypedNamedCredential` record. This class contains the credentials that are required to access your Avalara account
through Salesforce.

```
       public with sharing class HttpService

       {

          // Attribute to implement singleton pattern for Order Product Service class

          private static HttpService httpServiceInstance;

          // VARIABLES

          private HttpResponse httpResponse;

          private Map<String,String> mapOfHeaderParameter = new Map<String,String>();

          private enum Method {GET, POST}

          /**

          * @name getInstance

          * @description get an Instance of Service class

          * @params NA

          * @return Http Service Class Instance

          */

          public static HttpService getInstance()

          {

            if (NULL == httpServiceInstance)

            {

               httpServiceInstance = new HttpService();

            }

            return httpServiceInstance;

          }

          /**

          * @name get

          * @description Get Method to get a HTTP request

          */

          public void get(String endPoint)

          {

            send(newRequest(Method.GET, endPoint));

          }

          /**

          * @name post

          * @description Post Method to Post a HTTP request

          */

          public void post(String path, String requestBody)

          {

            String endPoint = 'callout:commerce.tax.TaxTypedNamedCredential:test'+path;

            send(newRequest(Method.POST, endPoint, requestBody));

          }

          /**

          * @name addHeader

          * @description addHeader Methods to add all the defualt Header's required fo

       rthe request

```


Apex Reference Guide TaxEngineAdapter Interface

```
          */

          public void addHeader(String name, String value)

          {

            mapOfHeaderParameter.put(name, value);

          }

          /**

          * @name setHeader

          * @description setHeader Methods to set setHeader for the request

          */

          private void setHeader(HttpRequest request)

          {

            for(String headerValue : mapOfHeaderParameter.keySet())

            {

               request.setHeader(headerValue, mapOfHeaderParameter.get(headerValue));

            }

          }

          /**

          * @name newRequest

          * @description newRequest Methods to make a new request

          */

          private HttpRequest newRequest(Method method, String endPoint)

          {

            return newRequest(method, endPoint, NULL);

          }

          /**

          * @name newRequest

          * @description newRequest Methods to make a new request

          */

         private HttpRequest newRequest(Method method, String endPoint, String requestBody)

          {

            HttpRequest request = new HttpRequest();

            request.setMethod(Method.name());

            setHeader(request);

            request.setEndpoint(endPoint);

            if (String.isNotBlank(requestBody))

            {

               request.setBody(requestBody);

            }

            request.setTimeout(120000);

            return request;

          }

          /**

          * @name send

          * @description send Methods to send a request

          */

          private void send(HttpRequest request)

          {

            try

            {

               Http http = new Http();

```


Apex Reference Guide TaxEngineAdapter Interface

```
               httpResponse = http.send(request);

            }

            catch(System.CalloutException e)

            {

               system.debug('callout exception happened' + e.getMessage());

            }

            catch(Exception e)

            {

               system.debug('callout did not happen' + e.getMessage());

            }

          }

          /**

          * @name getResponse

          * @description getResponse Method to get the Response

          */

          public HttpResponse getResponse()

          {

            return httpResponse;

          }

          /**

          * @name getResponseToString

          * @description getResponse Method to get the Responses

          */

          public String getResponseToString()

          {

            return getResponse().toString();

          }

       }

```

**•** Parse the `JsonSuccessParser` response object by using the `AvalaraJSONBuilder` class to build the response
for your adapter.

This example shows the `JsonSuccessParser` class.

```
       global with sharing class JsonSuccessParser

       {

         public static void consumeObject(JSONParser parser)

         {

          Integer depth = 0;

          do {

           JSONToken curr = parser.getCurrentToken();

           if (curr == JSONToken.START_OBJECT ||

            curr == JSONToken.START_ARRAY) {

            depth++;

           } else if (curr == JSONToken.END_OBJECT ||

            curr == JSONToken.END_ARRAY) {

            depth--;

           }

          } while (depth > 0 && parser.nextToken() != null);

         }

          public class Addresses {

            public String id {get;set;}

```


Apex Reference Guide TaxEngineAdapter Interface

```
            public String transactionId {get;set;}

            public String boundaryLevel {get;set;}

            public String line1 {get;set;}

            public String city {get;set;}

            public String region {get;set;}

            public String postalCode {get;set;}

            public String country {get;set;}

            public Integer taxRegionId {get;set;}

            public Addresses(JSONParser parser) {

               while (parser.nextToken() != JSONToken.END_OBJECT) {

                 if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {

                   String text = parser.getText();

                   if (parser.nextToken() != JSONToken.VALUE_NULL) {

                      if (text == 'id') {

                        id = parser.getText();

                      } else if (text == 'transactionId') {

                        transactionId = parser.getText();

                      } else if (text == 'boundaryLevel') {

                        boundaryLevel = parser.getText();

                      } else if (text == 'line1') {

                        line1 = parser.getText();

                      } else if (text == 'city') {

                        city = parser.getText();

                      } else if (text == 'region') {

                        region = parser.getText();

                      } else if (text == 'postalCode') {

                        postalCode = parser.getText();

                      } else if (text == 'country') {

                        country = parser.getText();

                      } else if (text == 'taxRegionId') {

                        taxRegionId = parser.getIntegerValue();

                      } else {

                        consumeObject(parser);

                      }

                   }

                 }

               }

            }

          }

          public class Details {

            public String id {get;set;}

            public String transactionLineId {get;set;}

            public String transactionId {get;set;}

            public String country {get;set;}

            public String region {get;set;}

            public Integer exemptAmount {get;set;}

            public String jurisCode {get;set;}

            public String jurisName {get;set;}

            public String stateAssignedNo {get;set;}

            public String jurisType {get;set;}

            public Integer nonTaxableAmount {get;set;}

            public Double rate {get;set;}

```


Apex Reference Guide TaxEngineAdapter Interface

```
            public Double tax {get;set;}

            public Integer taxableAmount {get;set;}

            public String taxType {get;set;}

            public String taxName {get;set;}

            public Integer taxAuthorityTypeId {get;set;}

            public Double taxCalculated {get;set;}

            public String rateType {get;set;}

            public Details(JSONParser parser) {

               while (parser.nextToken() != JSONToken.END_OBJECT) {

                 if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {

                   String text = parser.getText();

                   if (parser.nextToken() != JSONToken.VALUE_NULL) {

                      if (text == 'id') {

                        id = parser.getText();

                      } else if (text == 'transactionLineId') {

                        transactionLineId = parser.getText();

                      } else if (text == 'transactionId') {

                        transactionId = parser.getText();

                      } else if (text == 'country') {

                        country = parser.getText();

                      } else if (text == 'region') {

                        region = parser.getText();

                      } else if (text == 'exemptAmount') {

                        exemptAmount = parser.getIntegerValue();

                      } else if (text == 'jurisCode') {

                        jurisCode = parser.getText();

                      } else if (text == 'jurisName') {

                        jurisName = parser.getText();

                      } else if (text == 'stateAssignedNo') {

                        stateAssignedNo = parser.getText();

                      } else if (text == 'jurisType') {

                        jurisType = parser.getText();

                      } else if (text == 'nonTaxableAmount') {

                        nonTaxableAmount = parser.getIntegerValue();

                      } else if (text == 'rate') {

                        rate = parser.getDoubleValue();

                      } else if (text == 'tax') {

                        tax = parser.getDoubleValue();

                      } else if (text == 'taxableAmount') {

                        taxableAmount = parser.getIntegerValue();

                      } else if (text == 'taxType') {

                        taxType = parser.getText();

                      } else if (text == 'taxName') {

                        taxName = parser.getText();

                      } else if (text == 'taxAuthorityTypeId') {

                        taxAuthorityTypeId = parser.getIntegerValue();

                      } else if (text == 'taxCalculated') {

                        taxCalculated = parser.getDoubleValue();

                      } else if (text == 'rateType') {

                        rateType = parser.getText();

                      } else {

                        consumeObject(parser);

                      }

```


Apex Reference Guide TaxEngineAdapter Interface

```
                   }

                 }

               }

            }

          }

          public class Messages {

            public String summary {get;set;}

            public String details {get;set;}

            public String refersTo {get;set;}

            public String severity {get;set;}

            public String source {get;set;}

            public Messages(JSONParser parser) {

               while (parser.nextToken() != JSONToken.END_OBJECT) {

                 if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {

                   String text = parser.getText();

                   if (parser.nextToken() != JSONToken.VALUE_NULL) {

                      if (text == 'summary') {

                        summary = parser.getText();

                      } else if (text == 'details') {

                        details = parser.getText();

                      } else if (text == 'refersTo') {

                        refersTo = parser.getText();

                      } else if (text == 'severity') {

                        severity = parser.getText();

                      } else if (text == 'source') {

                        source = parser.getText();

                      } else {

                        consumeObject(parser);

                      }

                   }

                 }

               }

            }

          }

          public String id {get;set;}

          public String code {get;set;}

          public String referenceCode {get;set;}

          public Integer companyId {get;set;}

          public String taxDate {get;set;}

          public String transactionDate {get;set;}

          public String status {get;set;}

          public String type_Z {get;set;} // in json: type

          public Boolean reconciled {get;set;}

          public Integer totalAmount {get;set;}

          public Integer totalExempt {get;set;}

          public Double totalTax {get;set;}

          public Integer totalTaxable {get;set;}

          public Double totalTaxCalculated {get;set;}

          public String adjustmentReason {get;set;}

          public Boolean locked {get;set;}

          public Integer version {get;set;}

```


Apex Reference Guide TaxEngineAdapter Interface

```
          public String modifiedDate {get;set;}

          public Integer modifiedUserId {get;set;}

          public List<Lines> lines {get;set;}

          public List<Addresses> addresses {get;set;}

          public List<Summary> summary {get;set;}

          public List<Messages> messages {get;set;}

          public JsonSuccessParser(JSONParser parser) {

            while (parser.nextToken() != JSONToken.END_OBJECT) {

               if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {

                 String text = parser.getText();

                 if (parser.nextToken() != JSONToken.VALUE_NULL) {

                   if (text == 'id') {

                      id = parser.getText();

                   } else if (text == 'code') {

                      code = parser.getText();

                   } else if (text == 'referenceCode'){

                      referenceCode = parser.getText();

                   } else if (text == 'companyId') {

                      companyId = parser.getIntegerValue();

                   } else if (text == 'taxDate') {

                      taxDate = parser.getText();

                   } else if (text == 'date') {

                      transactionDate = parser.getText();

                   } else if (text == 'status') {

                      status = parser.getText();

                   } else if (text == 'type') {

                      type_Z = parser.getText();

                   } else if (text == 'reconciled') {

                      reconciled = parser.getBooleanValue();

                   } else if (text == 'totalAmount') {

                      totalAmount = parser.getIntegerValue();

                   } else if (text == 'totalExempt') {

                      totalExempt = parser.getIntegerValue();

                   } else if (text == 'totalTax') {

                      totalTax = parser.getDoubleValue();

                   } else if (text == 'totalTaxable') {

                      totalTaxable = parser.getIntegerValue();

                   } else if (text == 'totalTaxCalculated') {

                      totalTaxCalculated = parser.getDoubleValue();

                   } else if (text == 'adjustmentReason') {

                      adjustmentReason = parser.getText();

                   } else if (text == 'locked') {

                      locked = parser.getBooleanValue();

                   } else if (text == 'version') {

                      version = parser.getIntegerValue();

                   } else if (text == 'modifiedDate') {

                      modifiedDate = parser.getText();

                   } else if (text == 'modifiedUserId') {

                      modifiedUserId = parser.getIntegerValue();

                   } else if (text == 'lines') {

                      lines = new List<Lines>();

                      while (parser.nextToken() != JSONToken.END_ARRAY) {

                        lines.add(new Lines(parser));

```


Apex Reference Guide TaxEngineAdapter Interface

```
                      }

                   } else if (text == 'addresses') {

                      addresses = new List<Addresses>();

                      while (parser.nextToken() != JSONToken.END_ARRAY) {

                        addresses.add(new Addresses(parser));

                      }

                   } else if (text == 'summary') {

                      summary = new List<Summary>();

                      while (parser.nextToken() != JSONToken.END_ARRAY) {

                        summary.add(new Summary(parser));

                      }

                   } else if (text == 'messages') {

                      messages = new List<Messages>();

                      while (parser.nextToken() != JSONToken.END_ARRAY) {

                        messages.add(new Messages(parser));

                      }

                   } else {

                      consumeObject(parser);

                   }

                 }

               }

            }

          }

          public class Summary {

            public String country {get;set;}

            public String region {get;set;}

            public String jurisType {get;set;}

            public String jurisCode {get;set;}

            public String jurisName {get;set;}

            public Integer taxAuthorityType {get;set;}

            public String stateAssignedNo {get;set;}

            public String taxType {get;set;}

            public String taxName {get;set;}

            public String taxGroup {get;set;}

            public String rateType {get;set;}

            public Integer taxable {get;set;}

            public Double rate {get;set;}

            public Double tax {get;set;}

            public Double taxCalculated {get;set;}

            public Integer nonTaxable {get;set;}

            public Integer exemption {get;set;}

            public Summary(JSONParser parser) {

               while (parser.nextToken() != JSONToken.END_OBJECT) {

                 if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {

                   String text = parser.getText();

                   if (parser.nextToken() != JSONToken.VALUE_NULL) {

                      if (text == 'country') {

                        country = parser.getText();

                      } else if (text == 'region') {

                        region = parser.getText();

                      } else if (text == 'jurisType') {

                        jurisType = parser.getText();

```


Apex Reference Guide TaxEngineAdapter Interface

```
                      } else if (text == 'jurisCode') {

                        jurisCode = parser.getText();

                      } else if (text == 'jurisName') {

                        jurisName = parser.getText();

                      } else if (text == 'taxAuthorityType') {

                        taxAuthorityType = parser.getIntegerValue();

                      } else if (text == 'stateAssignedNo') {

                        stateAssignedNo = parser.getText();

                      } else if (text == 'taxType') {

                        taxType = parser.getText();

                      } else if (text == 'taxName') {

                        taxName = parser.getText();

                      } else if (text == 'taxGroup') {

                        taxGroup = parser.getText();

                      } else if (text == 'rateType') {

                        rateType = parser.getText();

                      } else if (text == 'taxable') {

                        taxable = parser.getIntegerValue();

                      } else if (text == 'rate') {

                        rate = parser.getDoubleValue();

                      } else if (text == 'tax') {

                        tax = parser.getDoubleValue();

                      } else if (text == 'taxCalculated') {

                        taxCalculated = parser.getDoubleValue();

                      } else if (text == 'nonTaxable') {

                        nonTaxable = parser.getIntegerValue();

                      } else if (text == 'exemption') {

                        exemption = parser.getIntegerValue();

                      } else {

                        consumeObject(parser);

                      }

                   }

                 }

               }

            }

          }

          public class Lines {

            public String id {get;set;}

            public String transactionId {get;set;}

            public String lineNumber {get;set;}

            public Integer discountAmount {get;set;}

            public Integer exemptAmount {get;set;}

            public Integer exemptCertId {get;set;}

            public Boolean isItemTaxable {get;set;}

            public Integer lineAmount {get;set;}

            public Double quantity {get;set;}

            public String reportingDate {get;set;}

            public Double tax {get;set;}

            public Integer taxableAmount {get;set;}

            public Double taxCalculated {get;set;}

            public String taxCode {get;set;}

            public String taxDate {get;set;}

            public Boolean taxIncluded {get;set;}

```


Apex Reference Guide TaxEngineAdapter Interface

```
            public List<Details> details {get;set;}

            public String itemCode {get;set;}

            public Lines(JSONParser parser) {

               while (parser.nextToken() != JSONToken.END_OBJECT) {

                 if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {

                   String text = parser.getText();

                   if (parser.nextToken() != JSONToken.VALUE_NULL) {

                      if (text == 'id') {

                        id = parser.getText();

                      } else if (text == 'transactionId') {

                        transactionId = parser.getText();

                      }else if (text == 'itemCode') {

                        itemCode = parser.getText();

                      }else if (text == 'lineNumber') {

                        lineNumber = parser.getText();

                      } else if (text == 'discountAmount') {

                        discountAmount = parser.getIntegerValue();

                      } else if (text == 'exemptAmount') {

                        exemptAmount = parser.getIntegerValue();

                      } else if (text == 'exemptCertId') {

                        exemptCertId = parser.getIntegerValue();

                      } else if (text == 'isItemTaxable') {

                        isItemTaxable = parser.getBooleanValue();

                      } else if (text == 'lineAmount') {

                        lineAmount = parser.getIntegerValue();

                      } else if (text == 'quantity') {

                        quantity = parser.getDoubleValue();

                      } else if (text == 'reportingDate') {

                        reportingDate = parser.getText();

                      } else if (text == 'tax') {

                        tax = parser.getDoubleValue();

                      } else if (text == 'taxableAmount') {

                        taxableAmount = parser.getIntegerValue();

                      } else if (text == 'taxCalculated') {

                        taxCalculated = parser.getDoubleValue();

                      } else if (text == 'taxCode') {

                        taxCode = parser.getText();

                      } else if (text == 'taxDate') {

                        taxDate = parser.getText();

                      } else if (text == 'taxIncluded') {

                        taxIncluded = parser.getBooleanValue();

                      } else if (text == 'details') {

                        details = new List<Details>();

                        while (parser.nextToken() != JSONToken.END_ARRAY) {

                           details.add(new Details(parser));

                        }

                      } else {

                        consumeObject(parser);

                      }

                   }

                 }

               }

            }

          }

```


Apex Reference Guide TaxEngineAdapter Interface

```
          public static JsonSuccessParser parse(String json)

          {

            return new JsonSuccessParser(System.JSON.createParser(json));

          }

       }

```

Prepare your JSON request to call the Avalara endpoint by using the `AvalaraJSONBuilder` class.

```
       public with sharing class AvalaraJSONBuilder

       {

          private static AvalaraJSONBuilder avalaraJSONBuilderInstance;

          public static AvalaraJSONBuilder getInstance()

          {

            if (NULL == avalaraJSONBuilderInstance)

            {

               avalaraJSONBuilderInstance = new AvalaraJSONBuilder();

            }

            return avalaraJSONBuilderInstance;

          }

          public String frameJsonForGetTaxOrderItem(commercetax.CalculateTaxRequest

       calculateTaxRequest)

          {

            try

            {

               Id accountid = null;

               if(calculateTaxRequest.CustomerDetails.AccountId != null &&

       calculateTaxRequest.CustomerDetails.AccountId != '')

               accountid = Id.valueof(calculateTaxRequest.CustomerDetails.AccountId);

               JSONGenerator jsonGeneratorInstance = JSON.createGenerator(true);

               jsonGeneratorInstance.writeStartObject();

               String type = null;

               if(calculateTaxRequest.taxtype == commercetax.CalculateTaxType.Actual)

                 type ='SalesInvoice';

                 else type = 'SalesOrder';

               jsonGeneratorInstance.writeStringField('type', type);

               if(calculateTaxRequest.SellerDetails != null)

                 jsonGeneratorInstance.writeStringField('companyCode',

       calculateTaxRequest.SellerDetails.code);

               else

                 jsonGeneratorInstance.writeStringField('companyCode', 'billing2');

               if(calculateTaxRequest.isCommit != null) {

                 jsonGeneratorInstance.writeBooleanField('commit',

       calculateTaxRequest.isCommit);

               }

               if(calculateTaxRequest.documentcode != null){

                 jsonGeneratorInstance.writeStringField('code',

       calculateTaxRequest.documentcode);

               }else if(calculateTaxRequest.referenceEntityId != null) {

                 jsonGeneratorInstance.writeStringField('code',

       calculateTaxRequest.referenceEntityId);

```


Apex Reference Guide TaxEngineAdapter Interface

```
               }

              if(calculateTaxRequest.CustomerDetails.code == null && accountid !=null)

        {

                 Account acc = [select id, name from account where id=:accountid];

                 jsonGeneratorInstance.writeStringField('customerCode', acc.name);

               } else {

                 jsonGeneratorInstance.writeStringField('customerCode',

       calculateTaxRequest.CustomerDetails.code);

               }

               if(calculateTaxRequest.EffectiveDate == null)

                 jsonGeneratorInstance.writeDateField('date', system.today());

               else

                 jsonGeneratorInstance.writeDateTimeField('date',

       calculateTaxRequest.EffectiveDate);

               jsonGeneratorInstance.writeFieldName('lines');

               jsonGeneratorInstance.writeStartArray();

               for(integer i=0;i<1;i++){

                 for(Commercetax.TaxLineItemRequest lineItem :

       calculateTaxRequest.LineItems)

                 {

                   jsonGeneratorInstance.writeStartObject();

                   if(lineItem.linenumber != null){

                      jsonGeneratorInstance.writeStringField('number',

       lineItem.linenumber);

                   }

                   jsonGeneratorInstance.writeNumberField('quantity',

       lineItem.Quantity);

                   jsonGeneratorInstance.writeNumberField('amount',

       (lineItem.Amount));

       jsonGeneratorInstance.writeStringField('taxCode',lineItem.taxCode);

                   jsonGeneratorInstance.writeFieldName('addresses');

                   jsonGeneratorInstance.writeStartObject();

                   jsonGeneratorInstance.writeFieldName('ShipFrom');

                   jsonGeneratorInstance.writeStartObject();

                   jsonGeneratorInstance.writeStringField('line1',

       lineItem.addresses.shipfrom.street);

                   jsonGeneratorInstance.writeStringField('line2',

       lineItem.addresses.shipfrom.street);

                   jsonGeneratorInstance.writeStringField('city',

       lineItem.addresses.shipfrom.city);

                   jsonGeneratorInstance.writeStringField('region',

       lineItem.addresses.shipfrom.state);

                   jsonGeneratorInstance.writeStringField('country',

       lineItem.addresses.shipfrom.country);

       jsonGeneratorInstance.writeStringField('postalCode',lineItem.addresses.shipfrom.postalcode);

                   jsonGeneratorInstance.writeEndObject();

                   jsonGeneratorInstance.writeFieldName('ShipTo');

                   jsonGeneratorInstance.writeStartObject();

```


Apex Reference Guide TaxEngineAdapter Interface

```
                   jsonGeneratorInstance.writeStringField('line1',

       lineItem.addresses.shipto.street);

                   jsonGeneratorInstance.writeStringField('line2',

       lineItem.addresses.shipto.street);

                   jsonGeneratorInstance.writeStringField('city',

       lineItem.addresses.shipto.city);

                   jsonGeneratorInstance.writeStringField('region',

       lineItem.addresses.shipto.state);

                   jsonGeneratorInstance.writeStringField('country',

       lineItem.addresses.shipto.country);

       jsonGeneratorInstance.writeStringField('postalCode',lineItem.addresses.shipto.postalcode);

                   jsonGeneratorInstance.writeEndObject();

                   jsonGeneratorInstance.writeFieldName('pointOfOrderOrigin');

                   jsonGeneratorInstance.writeStartObject();

                   jsonGeneratorInstance.writeStringField('line1',

       lineItem.addresses.soldto.street);

                   jsonGeneratorInstance.writeStringField('line2',

       lineItem.addresses.soldto.street);

                   jsonGeneratorInstance.writeStringField('city',

       lineItem.addresses.soldto.city);

                   jsonGeneratorInstance.writeStringField('region',

       lineItem.addresses.soldto.state);

                   jsonGeneratorInstance.writeStringField('country',

       lineItem.addresses.soldto.country);

       jsonGeneratorInstance.writeStringField('postalCode',lineItem.addresses.soldto.postalcode);

                   jsonGeneratorInstance.writeEndObject();

                   if(lineItem.effectiveDate != null)

                   {

                      jsonGeneratorInstance.writeFieldName('taxOverride');

                      jsonGeneratorInstance.writeStartObject();

                      jsonGeneratorInstance.writeDateTimeField('taxDate',

       lineItem.effectiveDate);

                      jsonGeneratorInstance.writeEndObject();

                   }

                   jsonGeneratorInstance.writeEndObject();

                   jsonGeneratorInstance.writeEndObject();

                 }

               }

                 jsonGeneratorInstance.writeEndArray();

               jsonGeneratorInstance.writeEndObject();

               return jsonGeneratorInstance.getAsString();

            }

            catch (Exception e)

            {

               throw e;

            }

```


### Apex Reference Guide TaxEngineContext Class

```
          }

       }

```

**•** Use the `JsonErrorParser` class to extract the error details, if any.

```
       global with sharing class JsonErrorParser

       {

          public cls_error error;

          public class cls_error

          {

            public String code;

            public String message;

            public String target;

            public cls_details[] details;

          }

          public class cls_details

          {

            public String code;

            public String message;

            public String description;

            public String faultCode;

            public String helpLink;

            public String severity;

          }

          public static JsonErrorParser parse(String json)

          {

           return (JsonErrorParser) System.JSON.deserialize(json, JsonErrorParser.class);

          }

       }

### TaxEngineContext Class

```

Wrapper class that stores details about the type of a tax calculation request.

Namespace

CommerceTax

Example

### At the beginning of a tax adapter, use TaxEngineContext class to pass the value of a request type to an instance of RequestType .

```
   global virtual class MockAdapter implements commercetax.TaxEngineAdapter {

      global commercetax.TaxEngineResponse processRequest(commercetax.TaxEngineContext

   taxEngineContext) {

         commercetax.RequestType requestType = taxEngineContext.getRequestType();

         commercetax.CalculateTaxRequest request =

   (commercetax.CalculateTaxRequest)taxEngineContext.getRequest();

```


Apex Reference Guide TaxEngineContext Class

#### Build the rest of your adapter based on the type of request that you got from TaxEngineContext class.

```
   if(requestType == commercetax.RequestType.CalculateTax){

           commercetax.calculatetaxtype type = request.taxtype;

           String docCode='';

           if(request.DocumentCode == 'simulateEmptyDocumentCode')

              docCode = '';

           else if(request.DocumentCode != null)

              docCode =request.DocumentCode;

          else if(request.ReferenceEntityId != null) docCode = request.ReferenceEntityId;

           else docCode = String.valueOf(getRandomInteger(0,2147483647));

           commercetax.CalculateTaxResponse response = new

   commercetax.CalculateTaxResponse();

           if(request.isCommit == true) {

              response.setStatus(commercetax.TaxTransactionStatus.Committed);

           } else {

              response.setStatus(commercetax.TaxTransactionStatus.Uncommitted);

           }

   }

```

IN THIS SECTION:

#### TaxEngineContext Constructors Learn more about the available constructors with the TaxEngineContext class.

TaxEngineContext Methods
#### Learn more about the available methods with the TaxEngineContext class. TaxEngineContext Constructors Learn more about the available constructors with the TaxEngineContext class. The TaxEngineContext class includes these constructors.

IN THIS SECTION:

##### TaxEngineContext(request, requestType, namedUri)
#### Initializes the TaxEngineContext object. This constructor is intended for test usage and throws an exception if used outside

of the Apex test context.

##### **`TaxEngineContext(request, requestType, namedUri)`**

#### Initializes the TaxEngineContext object. This constructor is intended for test usage and throws an exception if used outside of

the Apex test context.

Signature

```
   TaxEngineContext(commercetax.TaxEngineRequest request, commercetax.RequestType

   requestType, String namedUri)

```


Apex Reference Guide TaxEngineContext Class

Parameters

```
   request
```

Type: TaxEngineRequest

Information about the request.

```
   requestType
```

Type: RequestType

Whether the tax request is to calculate or estimate tax.

```
   namedUri
```

Type: String

URI that was called as part of the tax calculation request.

#### TaxEngineContext Methods Learn more about the available methods with the TaxEngineContext class. The TaxEngineContext class includes these methods.

IN THIS SECTION:

##### getNamedUri()
#### Retrieves the value of the NamedUri field of the TaxEngineContext class.

##### getRequest()
#### Gets the value of the TaxEngineContext 's Request field.

getRequestType()
#### Gets the value of the RequestType field of the TaxEngineContext class.

##### **`getNamedUri()`**

#### Retrieves the value of the NamedUri field of the TaxEngineContext class.

Signature

```
   global String getNamedUri()

```

Return Value

Type: String

##### **`getRequest()`**

#### Gets the value of the TaxEngineContext 's Request field.

Signature

```
   global commercetax.TaxEngineRequest getRequest()

```


### Apex Reference Guide TaxLineItemRequest Class

Return Value

Type: TaxEngineRequest

An implemented instance of an external tax engine's interface for processing requests. We've provided the `TaxEngineRequest`
interface for you to test within mock adapters with classes that implement it, such as CalculateTaxRequest. However, don’t use it outside
of a testing context.

##### **`getRequestType()`**

Gets the value of the RequestType field of the `TaxEngineContext` class.

Signature

```
   global commercetax.RequestType getRequestType()

```

Return Value

Type: RequestType

Indicates whether the calculation request was for actual or calculated tax.

### TaxLineItemRequest Class

Contains line item details of a tax request.

Namespace

CommerceTax

IN THIS SECTION:

#### TaxLineItemRequest Constructors
### Learn more about the constructors available with the TaxLineItemRequest class.

TaxLineItemRequest Properties
### Learn more about the available properties with the TaxLineItemRequest class.

TaxLineItemRequest Methods
### Learn more about the available methods with the TaxLineItemRequest class.

#### TaxLineItemRequest Constructors

### Learn more about the constructors available with the TaxLineItemRequest class. The TaxLineItemRequest class includes these constructors.

IN THIS SECTION:

TaxLineItemRequest(addresses, amount, description, productCode, quantity, lineNumber, taxCode, effectiveDate)
Initializes the request for the tax line item. This constructor is intended for test usage and throws an exception if used outside of the
Apex test context.


Apex Reference Guide TaxLineItemRequest Class

##### **`TaxLineItemRequest(addresses, amount, description, productCode, quantity,`**

```
  lineNumber, taxCode, effectiveDate)

```

Initializes the request for the tax line item. This constructor is intended for test usage and throws an exception if used outside of the
Apex test context.

Signature

```
   global TaxLineItemRequest(commercetax.LineTaxAddressesRequest addresses, Double amount,

   String description, String productCode, Double quantity, String lineNumber, String

   taxCode, Datetime effectiveDate)

   commercetax.TaxLineItemRequest, newinstance, [commercetax.LineTaxAddressesRequest, Double,

    String, String, Double, String, String, Datetime], commercetax.TaxLineItemRequest

```

Parameters

```
   addresses
```

Type: LineTaxAddressesRequest

Information about the addresses applied to each line item in a tax calculation request.

```
   amount
```

Type: Double

Total amount (in a given currency) represented by a line item sent for tax calculation.

```
   description
```

Type: String

User-defined description for a tax line item.

```
   productCode
```

Type: String

Catalog code for the product represented by the tax line item.

```
   quantity
```

Type: Double

Number of units of a given product that the tax line item represents.

```
   lineNumber
```

Type: String

Unique number used to identify a tax line item.

```
   taxCode
```

Type: String

Code used to identify how tax is calculated for a tax line item.

```
   effectiveDate
```

Type: Datetime

This is a user-defined date used for reporting only. For negative invoice lines, this parameter represents the invoice date from the
original invoice. In other cases, it represents the date when the tax transaction takes effect on the line item. The previous tax transaction
type is always `Debit` for negative invoice lines.


Apex Reference Guide TaxLineItemRequest Class

#### TaxLineItemRequest Properties Learn more about the available properties with the TaxLineItemRequest class. The TaxLineItemRequest class includes these properties.

IN THIS SECTION:

##### addresses

Contains the list of addresses of a line item.

amount
Total amount (in a given currency) represented by a line item sent for tax calculation.

customTaxAttributes
Customised tax contract to include additional attributes at the line item level.

description
User-defined description for a tax line item.

effectiveDate
The date that a tax transaction takes effect on a line item. This is a user-defined date used for reporting only.

lineNumber
Unique number used to identify a tax line item.

productCode
Catalog code for the product represented by the tax line item.

productSKU
Unique identifier of a product that can be used to identify products that are exempted from tax.

quantity
Number of units of a given product that the tax line item represents.

referenceDocumentCode
Identifier that combines the original invoice ID, previous tax transaction type, and tax engine ID, used in tax calculations for negative
invoice lines.

taxCode
Code used to identify how tax is calculated for a tax line item.

##### **`addresses`**

Contains the list of addresses of a line item.

Signature

```
   public commercetax.LineTaxAddressesRequest addresses {get; set;}

```

Property Value

Type: commercetax.LineTaxAddressesRequest


Apex Reference Guide TaxLineItemRequest Class

##### **`amount`**

Total amount (in a given currency) represented by a line item sent for tax calculation.

Signature

```
   global Double amount {get; set;}

```

Property Value

Type: Double

##### **`customTaxAttributes`**

Customised tax contract to include additional attributes at the line item level.

Signature

```
   global commercetax.TaxLineItemRequest customTaxAttributes {get; set;}

```

Property Value

Type: Map<String, Object>

##### **`description`**

User-defined description for a tax line item.

Signature

```
   global String description {get; set;}

```

Property Value

Type: String

##### **`effectiveDate`**

The date that a tax transaction takes effect on a line item. This is a user-defined date used for reporting only.

Signature

```
   global Datetime effectiveDate {get; set;}

```

Property Value

Type: Datetime

##### **`lineNumber`**

Unique number used to identify a tax line item.


Apex Reference Guide TaxLineItemRequest Class

Signature

```
   global String lineNumber {get; set;}

```

Property Value

Type: String

##### **`productCode`**

Catalog code for the product represented by the tax line item.

Signature

```
   global String productCode {get; set;}

```

Property Value

Type: String

##### **`productSKU`**

Unique identifier of a product that can be used to identify products that are exempted from tax.

Signature

```
   global String productSKU {get; set;}

```

Property Value

Type: String

##### **`quantity`**

Number of units of a given product that the tax line item represents.

Signature

```
   global Double quantity {get; set;}

```

Property Value

Type: Double

##### **`referenceDocumentCode`**

Identifier that combines the original invoice ID, previous tax transaction type, and tax engine ID, used in tax calculations for negative
invoice lines.

For example, a referenceDocumentCode parameter value `3ttxx00000004Bh_Debit-4wAxx0000000001EAA` indicates
`3ttxx00000004Bh` is the original invoice ID and `4wAxx0000000001EAA` is the tax engine ID. The previous tax transaction
type is always `Debit` for negative invoice lines.


Apex Reference Guide TaxLineItemRequest Class

Signature

```
   global String referenceDocumentCode {get; set;}

```

Property Value

Type: String

##### **`taxCode`**

Code used to identify how tax is calculated for a tax line item.

Signature

```
   global String taxCode {get; set;}

```

Property Value

Type: String

#### TaxLineItemRequest Methods Learn more about the available methods with the TaxLineItemRequest class. The TaxLineItemRequest class includes these methods.

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type TaxLineItemRequest by determining the equality of external objects in a list. This

method is dynamic and is based on the `equals()` method in Java.

hashCode()
#### Maintains the integrity of lists of type TaxLineItemRequest by determining the uniqueness of the external object records in

a list.

toString()
Converts a value to a string.

##### **`equals(obj)`**

#### Maintains the integrity of lists of type TaxLineItemRequest by determining the equality of external objects in a list. This method

is dynamic and is based on the `equals()` method in Java.

Signature

```
   global Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object


### Apex Reference Guide TaxSellerDetailsRequest Class

External object whose key is to be validated.

Return Value

Type: Boolean

##### **`hashCode()`**

Maintains the integrity of lists of type `TaxLineItemRequest` by determining the uniqueness of the external object records in a
list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a value to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### TaxSellerDetailsRequest Class

Contains tax code details used in the tax calculation request.

Namespace

CommerceTax

IN THIS SECTION:

TaxSellerDetailsRequest Constructors
### Learn more about the available constructors with the TaxSellerDetailsRequest class.

TaxSellerDetailsRequest Properties
### Learn more about the available properties with the TaxSellerDetailsRequest class.

TaxSellerDetailsRequest Methods
### Learn more about the available methods with the TaxSellerDetailsRequest class.


Apex Reference Guide TaxSellerDetailsRequest Class

#### TaxSellerDetailsRequest Constructors Learn more about the available constructors with the TaxSellerDetailsRequest class. The TaxSellerDetailsRequest class includes these constructors.

IN THIS SECTION:

##### TaxSellerDetailsRequest(code)

Initializes the request for the tax seller details. This constructor is intended for test usage and throws an exception if used outside of
the Apex test context

##### **`TaxSellerDetailsRequest(code)`**

Initializes the request for the tax seller details. This constructor is intended for test usage and throws an exception if used outside of the
Apex test context

Signature

```
   global TaxSellerDetailsRequest(String code)

```

Parameters

##### _`code`_

Type: String

Tax code used for tax calculation.

#### TaxSellerDetailsRequest Properties Learn more about the available properties with the TaxSellerDetailsRequest class. The TaxSellerDetailsRequest class includes these properties.

IN THIS SECTION:

##### code

Tax code used for tax calculation.

##### **`code`**

Tax code used for tax calculation.

Signature

```
   global String code {get; set;}

```

Property Value

Type: String


Apex Reference Guide TaxSellerDetailsRequest Class

#### TaxSellerDetailsRequest Methods Learn more about the available methods with the TaxSellerDetailsRequest class. The TaxSellerDetailsRequest class includes these methods.

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type TaxSellerDetailsRequest by determining the equality of the external objects in a

list. This method is dynamic and based on the `equals()` method in Java.

##### hashCode()
#### Maintains the integrity of lists of type TaxSellerDetailsRequest by determining the uniqueness of the external objects

in a list.

toString()
Converts a value to a string.

##### **`equals(obj)`**

#### Maintains the integrity of lists of type TaxSellerDetailsRequest by determining the equality of the external objects in a list.

This method is dynamic and based on the `equals()` method in Java.

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

##### **`hashCode()`**

#### Maintains the integrity of lists of type TaxSellerDetailsRequest by determining the uniqueness of the external objects in a

list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer


### Apex Reference Guide TaxTransactionRequest Class

##### **`toString()`**

Converts a value to a string.

Signature

```
   global String toString()

```

Return Value

Type: String

### TaxTransactionRequest Class

Abstract class for storing customer details used in tax calculation and estimation requests.

Namespace

CommerceTax

Usage

Specify the `CommerceTax` namespace when creating an instance of this class. The constructor of this class takes no arguments. For
### example, let's say you create an instance of CalculateTaxRequest class, which extends the TaxTransactionRequest

class.

IN THIS SECTION:

#### TaxTransactionRequest Constructors
### Learn more about the available constructors with the TaxTransactionRequest class.

TaxTransactionRequest Properties
### Learn more about the available properties with the TaxTransactionRequest class.

TaxTransactionRequest Methods

#### TaxTransactionRequest Constructors

### Learn more about the available constructors with the TaxTransactionRequest class. The TaxTransactionRequest class includes these constructors.

IN THIS SECTION:

TaxTransactionRequest(addresses, currencyIsoCode, customerDetails, description, documentCode, referenceDocumentCode,
transactionDate, effectiveDate, lineItems, referenceEntityId, sellerDetails, customTaxAttributes)
Initializes the request for the tax transaction. This constructor is intended for test usage and throws an exception if used outside of
the Apex test context.


Apex Reference Guide TaxTransactionRequest Class

##### **`TaxTransactionRequest(addresses, currencyIsoCode, customerDetails,`**

```
  description, documentCode, referenceDocumentCode, transactionDate,

  effectiveDate, lineItems, referenceEntityId, sellerDetails,

  customTaxAttributes)

```

Initializes the request for the tax transaction. This constructor is intended for test usage and throws an exception if used outside of the
Apex test context.

Signature

```
   global TaxTransactionRequest(commercetax.HeaderTaxAddressesRequest addresses, String

   currencyIsoCode, commercetax.TaxCustomerDetailsRequest customerDetails, String

   description, String documentCode, String referenceDocumentCode, Datetime transactionDate,

   Datetime effectiveDate, List<commercetax.TaxLineItemRequest> lineItems, String

   referenceEntityId, commercetax.TaxSellerDetailsRequest sellerDetails,Map<String,Object>

   customTaxAttributes)

```

Parameters

```
   addresses
```

Type: HeaderTaxAddressesRequest

Tax addresses, such as Ship To and Bill From.

```
   currencyIsoCode
```

Type: String

##### Three-letter ISO 4217 currency code associated with the TaxTransactionRequest .

```
   customerDetails
```

Type: TaxCustomerDetailsRequest

Customer information used in tax calculation.

```
   description
```

Type: String

Optional user-defined description for providing more information about the tax transaction request.

```
   documentCode
```

Type: String

Code for documents that are used to provide more information in the tax calculation process.

```
   referenceDocumentCode
```

Type: String

Identifier that combines the original invoice ID, previous tax transaction type, and tax engine ID, used in tax calculations for negative
invoice lines. For example, a referenceDocumentCode parameter value `3ttxx00000004Bh_Debit-4wAxx0000000001EAA`
indicates `3ttxx00000004Bh` is the original invoice ID and `4wAxx0000000001EAA` is the tax engine ID.

```
   transactionDate
```

Type: Datetime

The date that the tax transaction occurred.

```
   effectiveDate
```

Type: Datetime


Apex Reference Guide TaxTransactionRequest Class

The date that the tax transaction takes effect. User-defined and used only for reporting purposes.

```
   lineItems
```

Type: List<TaxLineItemRequest>

A list of line items on which tax is calculated.

```
   referenceEntityId
```

Type: String

ID of an object related to the line items sent for tax calculation.

```
   sellerDetails
```

Type: TaxSellerDetailsRequest

Contains tax code information used in a tax calculation request.

```
   customTaxAttributes
```

Type: Map<String, Object>

Customised tax contract to include additional attributes at the header level.

#### TaxTransactionRequest Properties Learn more about the available properties with the TaxTransactionRequest class. The TaxTransactionRequest class includes these properties.

IN THIS SECTION:

addresses
A list of addresses (such as Ship To and Sold To) used as part of the tax transaction.

currencyIsoCode
#### Three-letter ISO 4217 currency code associated with the TaxTransactionRequest .

customerDetails
Customer information used in tax calculation.

customTaxAttributes
Customised tax contract to include additional attributes at the header level.

description
Optional user-defined description for providing more information about the tax transaction request.

documentCode
Code for documents used to provide more information in the tax calculation process.

effectiveDate
The date that the tax transaction takes effect. User-defined and used only for reporting purposes.

lineItems
A list of line items on which tax will be calculated.

referenceDocumentCode
Identifier that combines the original invoice ID, previous tax transaction type, and tax engine ID, used in tax calculations for negative
invoice lines.

referenceEntityId
ID of an object related to the line items sent for tax calculation.


Apex Reference Guide TaxTransactionRequest Class

sellerDetails
Contains tax code information used in a tax calculation request.

transactionDate
The date that the tax transaction occurred.

##### **`addresses`**

A list of addresses (such as Ship To and Sold To) used as part of the tax transaction.

Signature

```
   global commercetax.HeaderTaxAddressesRequest addresses {get; set;}

```

Property Value

Type: HeaderTaxAddressesRequest

##### **`currencyIsoCode`**

Three-letter ISO 4217 currency code associated with the `TaxTransactionRequest` .

Signature

```
   global String currencyIsoCode {get; set;}

```

Property Value

Type: String

##### **`customerDetails`**

Customer information used in tax calculation.

Signature

```
   global CommerceTax.TaxCustomerDetailsRequest customerDetails {get; set;}

```

Property Value

Type: TaxCustomerDetailsRequest

##### **`customTaxAttributes`**

Customised tax contract to include additional attributes at the header level.

Signature

```
   global commercetax.TaxTransactionRequest customTaxAttributes {get; set;}

```


Apex Reference Guide TaxTransactionRequest Class

Property Value

Type: Map<String, Object>

##### **`description`**

Optional user-defined description for providing more information about the tax transaction request.

Signature

```
   global String description {get; set;}

```

Property Value

Type: String

##### **`documentCode`**

Code for documents used to provide more information in the tax calculation process.

Signature

```
   global String documentCode {get; set;}

```

Property Value

Type: String

##### **`effectiveDate`**

The date that the tax transaction takes effect. User-defined and used only for reporting purposes.

Signature

```
   global Datetime effectiveDate {get; set;}

```

Property Value

Type: Datetime

##### **`lineItems`**

A list of line items on which tax will be calculated.

Signature

```
   global List<CommerceTax.TaxLineItemRequest> lineItems {get; set;}

```

Property Value

Type: List<TaxLineItemRequest>


Apex Reference Guide TaxTransactionRequest Class

##### **`referenceDocumentCode`**

Identifier that combines the original invoice ID, previous tax transaction type, and tax engine ID, used in tax calculations for negative
invoice lines.

For example, a referenceDocumentCode parameter value `3ttxx00000004Bh_Debit-4wAxx0000000001EAA` indicates
`3ttxx00000004Bh` is the original invoice ID and `4wAxx0000000001EAA` is the tax engine ID.

Signature

```
   global String referenceDocumentCode {get; set;}

```

Property Value

Type: String

##### **`referenceEntityId`**

ID of an object related to the line items sent for tax calculation.

Signature

```
   global String referenceEntityId {get; set;}

```

Property Value

Type: String

##### **`sellerDetails`**

Contains tax code information used in a tax calculation request.

Signature

```
   global commercetax.TaxSellerDetailsRequest sellerDetails {get; set;}

```

Property Value

Type: TaxSellerDetailsRequest

##### **`transactionDate`**

The date that the tax transaction occurred.

Signature

```
   global Datetime transactionDate {get; set;}

```

Property Value

Type: Datetime


Apex Reference Guide TaxTransactionRequest Class

#### TaxTransactionRequest Methods The following are methods for TaxTransactionRequest .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type TaxTransactionRequest by determining the equality of external objects in a list. This

method is dynamic and based on the `equals()` method in Java.

##### hashCode()
#### Maintains the integrity of lists of type TaxTransactionRequest by determining the uniqueness of the external object records

in a list.

##### toString()

Converts a value to a string.

##### **`equals(obj)`**

#### Maintains the integrity of lists of type TaxTransactionRequest by determining the equality of external objects in a list. This

method is dynamic and based on the `equals()` method in Java.

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

##### **`hashCode()`**

#### Maintains the integrity of lists of type TaxTransactionRequest by determining the uniqueness of the external object records

in a list.

Signature

```
   global Integer hashCode()

```

Return Value

Type: Integer

##### **`toString()`**

Converts a value to a string.


### Apex Reference Guide TaxTransactionStatus Enum

Signature

```
   global String toString()

```

Return Value

Type: String

### TaxTransactionStatus Enum

Shows whether the tax transaction has been committed or uncommitted.

Usage

Used by the CalculateTaxResponse class method.

Enum Values

The `commercetax.TaxTransactionStatus` enum includes these values.

**Value** **Description**

`Committed` Tax has been calculated and committed.

`Uncommitted` Tax has been calculated but hasn't been committed.

### TaxTransactionType Enum

Shows whether the tax transaction is for a credit or debit transaction.

Usage

Used by the CalculateTaxResponse and CalculateTaxRequest class methods.

Enum Values

The `commercetax.TaxTransactionType` enum includes these values.

**Value** **Description**

`Credit` Represents a credit transaction.

`Debit` Represents a debit transaction.

`Void` Specifies that the tax engine has voided the document that's mentioned in the
`referenceDocumentCode` property value.


## Apex Reference Guide ComplianceMgmt Namespace ComplianceMgmt Namespace The ComplianceMgmt namespace provides classes and methods to implement rule processors for compliance control. The ComplianceMgmt namespace includes these classes.

**•** [ComplianceEvaluation Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_interface_ComplianceMgmt_ComplianceEvaluation.htm)

**•** [ControlEvaluationInput Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_ComplianceMgmt_ControlEvaluationInput)

**•** [ControlInput Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_ComplianceMgmt_ControlInput.htm)

**•** [ComplianceEvaluationResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_ComplianceMgmt_ComplianceEvaluationResponse.htm)

**•** [EvaluationResult Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_ComplianceMgmt_EvaluationResult.htm)

**•** [ComplianceControlLog Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_ComplianceMgmt_ComplianceControlLog.htm)

## Compression Namespace

The Compression namespace provides classes and methods to create and extract zip files.

## The following are the classes and enums in the Compression namespace.

IN THIS SECTION:

### Level Enum

Specifies the compression level for creating a zip file.

Method Enum
Specifies the compression method for the zip entries.

ZipEntry Class
Contains methods to get and set information about a zip file entry.

ZipReader Class
Contains methods to get information about zip entries and to extract content for specified zip entries from the zip file.

ZipWriter Class
Contains methods to add zip entries, generate a zipped archive, and return the result as an Apex blob.

Compression Exceptions
## The Compression namespace contains exception classes.

### Level Enum

Specifies the compression level for creating a zip file.

Usage

### Use Level enum with the getLevel() and setLevel(value) methods in the ZipWriter class.

Enum Values

The following are the values of the `Compression.Level` enum.


### Apex Reference Guide Method Enum

**Value** **Description**

`BEST_COMPRESSION` Compression level for best compression.

`BEST_SPEED` Compression level for fastest compression.

`DEFAULT_LEVEL` Default compression level.

`NO_COMPRESSION` Compression level for no compression.

### Method Enum

Specifies the compression method for the zip entries.

Usage

### Use the Method enum with the getMethod() and setMethod(method) methods in the ZipEntry and ZipWriter

classes.

Enum Values

The following are the values of the `Compression.Method` enum.

**Value** **Description**

`DEFLATED` Deflated compression method for compressed entries.

`STORED` No compression method for zip entries.

### ZipEntry Class

Contains methods to get and set information about a zip file entry.

Namespace

Compression

IN THIS SECTION:

#### ZipEntry Methods ZipEntry Methods

### The following are methods for ZipEntry .

IN THIS SECTION:

equals(obj)
Compares this object with the specified object and returns `true` if both objects are equal; otherwise, returns `false` .


Apex Reference Guide ZipEntry Class

hashcode()
Returns the hash code value for the zip entry.

getComment()
Gets the comment string for the zip entry.

getCompressedSize()
Gets the size in bytes of the compressed zip entry.

getContent()
Gets the content of the zip entry. This method doesn’t work with the `ZipReader` class.

getCrc()
Gets the cyclic redundancy check (CRC) value for the zip entry.

getLastModifiedTime()
Gets the last modification timestamp of the zip entry.

getMethod()
Gets the compression method of the zip entry.

getName()
Gets the name of the zip entry.

getUncompressedSize()
Gets the uncompressed size in bytes of the zip entry content.

setComment(comment)
Sets the comment string for the zip entry that’s written to the Zip archive. This method doesn’t work with the `ZipReader` class.

setContent(blob)
Sets the content of the zip entry that’s written to the Zip archive. This method doesn’t work with the `ZipReader` class.

setLastModifiedTime(modTime)
Sets the last modification time of the zip entry that’s written to the Zip archive. This method doesn’t work with the `ZipReader`
class.

setMethod(method)
Sets the compression method for the zip entry that’s written to the zip archive. This method doesn’t work with the `ZipReader`
class.

toString()
Returns a string representation of the zip entry.

##### **`equals(obj)`**

Compares this object with the specified object and returns `true` if both objects are equal; otherwise, returns `false` .

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object


Apex Reference Guide ZipEntry Class

Return Value

Type: Boolean

##### **`hashcode()`**

Returns the hash code value for the zip entry.

Signature

```
   public Integer hashcode()

```

Return Value

Type: Integer

##### **`getComment()`**

Gets the comment string for the zip entry.

Signature

```
   public string getComment()

```

Return Value

Type: string

##### **`getCompressedSize()`**

Gets the size in bytes of the compressed zip entry.

Signature

```
   public long getCompressedSize()

```

Return Value

Type: long

##### **`getContent()`**

Gets the content of the zip entry. This method doesn’t work with the `ZipReader` class.

Signature

```
   public blob getContent()

```

Return Value

Type: blob


Apex Reference Guide ZipEntry Class

##### **`getCrc()`**

Gets the cyclic redundancy check (CRC) value for the zip entry.

Signature

```
   public long getCrc()

```

Return Value

Type: long

##### **`getLastModifiedTime()`**

Gets the last modification timestamp of the zip entry.

Signature

```
   public Datetime getLastModifiedTime()

```

Return Value

Type: Datetime

##### **`getMethod()`**

Gets the compression method of the zip entry.

Signature

```
   public Compression.Method getMethod()

```

Return Value

Type: Compression.Method

Uses values from the `Method` enum and indicates whether the zip entry has _`DEFLATED`_ or _`STORED`_ method.

##### **`getName()`**

Gets the name of the zip entry.

Signature

```
   public string getName()

```

Return Value

Type: string


Apex Reference Guide ZipEntry Class

##### **`getUncompressedSize()`**

Gets the uncompressed size in bytes of the zip entry content.

Signature

```
   public long getUncompressedSize()

```

Return Value

Type: long

##### **`setComment(comment)`**

Sets the comment string for the zip entry that’s written to the Zip archive. This method doesn’t work with the `ZipReader` class.

Signature

```
   public Compression.ZipEntry setComment(String comment)

```

Parameters

```
   comment
```

Type: String

Return Value

Type: Compression.ZipEntry

##### **`setContent(blob)`**

Sets the content of the zip entry that’s written to the Zip archive. This method doesn’t work with the `ZipReader` class.

Signature

```
   public Compression.ZipEntry setContent(Blob blob)

```

Parameters

```
   blob
```

Type: Blob

Return Value

Type: Compression.ZipEntry

##### **`setLastModifiedTime(modTime)`**

Sets the last modification time of the zip entry that’s written to the Zip archive. This method doesn’t work with the `ZipReader` class.


### Apex Reference Guide ZipReader Class

Signature

```
   public Compression.ZipEntry setLastModifiedTime(Datetime modTime)

```

Parameters

```
   modTime
```

Type: Datetime

Return Value

Type: Compression.ZipEntry

##### **`setMethod(method)`**

### Sets the compression method for the zip entry that’s written to the zip archive. This method doesn’t work with the ZipReader class.

Signature

```
   public Compression.ZipEntry setMethod(Compression.Method method)

```

Parameters

```
   method
```

Type: Compression.Method

Uses the `Method` enum values and sets the compression method as `DEFLATED` or `STORED` .

Return Value

Type: Compression.ZipEntry

##### **`toString()`**

Returns a string representation of the zip entry.

Signature

```
   public string toString()

```

Return Value

Type: string

### ZipReader Class

Contains methods to get information about zip entries and to extract content for specified zip entries from the zip file.

Namespace

Compression


Apex Reference Guide ZipReader Class

IN THIS SECTION:

#### ZipReader Constructors ZipReader Methods ZipReader Constructors The following are constructors for ZipReader .

IN THIS SECTION:

##### ZipReader(data)
#### Creates a new instance of the ZipReader class using the specified blob data.

##### **`ZipReader(data)`**

#### Creates a new instance of the ZipReader class using the specified blob data.

Signature

```
   global ZipReader(Blob data)

```

Parameters

```
   data
```

Type: Blob

Apex blob that contains the compressed content.

#### ZipReader Methods The following are methods for ZipReader .

IN THIS SECTION:

extract(name)
Extracts the bytes for the specified zip entry name and decompresses the content.

extract(entry)
Extracts the bytes for the specified zip entry and decompresses the content.

getEntries()
Gets a list of all the entries from the zip file.

getEntriesMap()
Gets a map of names and the corresponding zip entries from the zip file.

getEntry(name)
Gets a zip entry for the specified name from the zip file.

getEntryNames()
Gets a list of all the zip entry names from the zip file.


Apex Reference Guide ZipReader Class

##### **`extract(name)`**

Extracts the bytes for the specified zip entry name and decompresses the content.

Signature

```
   public blob extract(string name)

```

Parameters

```
   name
```

Type: string

Species the zip entry name to extract and decompress.

Return Value

Type: blob

Apex blob that contains the decompressed content.

##### **`extract(entry)`**

Extracts the bytes for the specified zip entry and decompresses the content.

Signature

```
   public blob extract(Compression.ZipEntry entry)

```

Parameters

```
   entry
```

Type: Compression.ZipEntry

Species the zip entry to extract and decompress.

Return Value

Type: blob

Apex blob that contains the decompressed content.

##### **`getEntries()`**

Gets a list of all the entries from the zip file.

Signature

```
   public List<compression.ZipEntry> getEntries()

```

Return Value

Type: List<Compression.ZipEntry>


### Apex Reference Guide ZipWriter Class

##### **`getEntriesMap()`**

Gets a map of names and the corresponding zip entries from the zip file.

Signature

```
   public Map<String,Compression.ZipEntry> getEntriesMap()

```

Return Value

Type: Map<string,Compression.ZipEntry>

##### **`getEntry(name)`**

Gets a zip entry for the specified name from the zip file.

Signature

```
   public compression.ZipEntry getEntry(string name)

```

Parameters

```
   name
```

Type: string

Name of the zip entry.

Return Value

Type: Compression.ZipEntry

Throws a `ZipException` if the specified name isn’t found.

##### **`getEntryNames()`**

Gets a list of all the zip entry names from the zip file.

Signature

```
   public List<String> getEntryNames()

```

Return Value

Type: List<String>

### ZipWriter Class

Contains methods to add zip entries, generate a zipped archive, and return the result as an Apex blob.

Namespace

Compression


Apex Reference Guide ZipWriter Class

Example

This sample code compresses email attachments into a single file.

```
   Compression.ZipWriter writer = new Compression.ZipWriter();

   List<id> contentDocumentIds = new List<id>();

   // Add IDs of documents to be compressed to contentDocumentIds

   for ( ContentVersion cv : [SELECT PathOnClient, Versiondata

                    FROM ContentVersion

                    WHERE ContentDocumentId IN :contentDocumentIds])

   {

       writer.addEntry(cv.PathOnClient, cv.versiondata);

   }

   blob zipAttachment = writer.getArchive();

   Messaging.EmailFileAttachment efa = new Messaging.EmailFileAttachment();

   efa.setFileName('attachments.zip');

   efa.setBody(zipAttachment);

   List<Messaging.EmailFileAttachment> fileAttachments = new

   List<Messaging.EmailFileAttachment>();

   fileAttachments.add(efa);

   Messaging.SingleEmailMessage email = new Messaging.SingleEmailMessage();

   // Set all the other email fields, such as addresses, subject, and body

   email.setFileAttachments(fileAttachments);

   Messaging.sendEmail(new Messaging.SingleEmailMessage[] { email });

```

IN THIS SECTION:

#### ZipWriter Constructors

ZipWriter Methods

#### ZipWriter Constructors The following are constructors for ZipWriter .

IN THIS SECTION:

##### ZipWriter()
#### Creates a new instance of the ZipWriter class.

##### **`ZipWriter()`**

#### Creates a new instance of the ZipWriter class.


Apex Reference Guide ZipWriter Class

Signature

```
   global ZipWriter()

#### ZipWriter Methods The following are methods for ZipWriter .

```

IN THIS SECTION:

##### addEntry(name, data)

Adds an entry to the zip file with the specified name and content.

addEntry(prototype)
Adds a copy of the specified prototype entry to the zip file and includes details such as the zip entry name, comment, last modification
time, and content.

addEntry(name, comment, modTime, method, data)
Adds an entry to the zip file with the specified name, comment, last modification time, compression method, and content.

getArchive()
Compresses the zip entries and generates a ZIP archive.

getEntries()
Gets a list of all the entries in the zip file.

getEntry(name)
Gets the entry with the specified name from the zip file.

getEntryNames()
Gets a set of all the zip entry names in the zip file.

getLevel()
Gets the compression level of the zip file.

getMethod()
Gets the compression method of the zip file.

removeEntry(name)
Removes the entry with the specified name from the zip file.

setLevel(level)
Sets the compression level of the zip file.

setMethod(method)
Sets the compression method for the zip file.

##### **`addEntry(name, data)`**

Adds an entry to the zip file with the specified name and content.

Signature

```
   public Compression.ZipEntry addEntry(string name, blob data)

```


Apex Reference Guide ZipWriter Class

Parameters

```
   name
```

Type: string

The name of the zip entry.

```
   data
```

Type: blob

The content of the zip entry.

Return Value

Type: Compression.ZipEntry

Zip entry added to the zip file.

##### **`addEntry(prototype)`**

Adds a copy of the specified prototype entry to the zip file and includes details such as the zip entry name, comment, last modification
time, and content.

Signature

```
   public Compression.ZipEntry addEntry(compression.ZipEntry prototype)

```

Parameters

```
   prototype
```

Type: Compression.ZipEntry

Details of the entry to be added to the zip file.

Return Value

Type: Compression.ZipEntry

##### **`addEntry(name, comment, modTime, method, data)`**

Adds an entry to the zip file with the specified name, comment, last modification time, compression method, and content.

Signature

```
   public Compression.ZipEntry addEntry(String name, String comment, Datetime modTime,

   Compression.Method method, Blob data)

```

Parameters

```
   name
```

Type: String

The name of the zip entry.

```
   comment
```

Type: String


Apex Reference Guide ZipWriter Class

The comment about the zip entry.

```
   modTime
```

Type: Datetime

The last modification timestamp of the zip entry.

```
   method
```

Type: Compression.Method

The compression method of the zip entry, which is either `DEFLATED` or `STORED` .

```
   data
```

Type: Blob

The content of the zip entry.

Return Value

Type: Compression.ZipEntry

Zip entry added to the zip file.

##### **`getArchive()`**

Compresses the zip entries and generates a ZIP archive.

Signature

```
   public blob getArchive()

```

Return Value

Type: blob

Apex blob that contains the bytes of the compression operation.

##### **`getEntries()`**

Gets a list of all the entries in the zip file.

Signature

```
   public List<Compression.ZipEntry> getEntries()

```

Return Value

Type: List<Compression.ZipEntry>

##### **`getEntry(name)`**

Gets the entry with the specified name from the zip file.

Signature

```
   public compression.ZipEntry getEntry(string name)

```


Apex Reference Guide ZipWriter Class

Parameters

```
   name
```

Type: string

Name of the zip entry to be retrieved.

Return Value

Type: Compression.ZipEntry

##### **`getEntryNames()`**

Gets a set of all the zip entry names in the zip file.

Signature

```
   public Set<String> getEntryNames()

```

Return Value

Type: Set<String> on page 4038

##### **`getLevel()`**

Gets the compression level of the zip file.

Signature

```
   public Compression.Level getLevel()

```

Return Value

Type: Compression.Level

Uses the `Level` enum values to indicate the compression level as `BEST_COMPRESSION`, `BEST_SPEED`, `DEFAULT_LEVEL`,
or `NO_COMPRESSION` .

##### **`getMethod()`**

Gets the compression method of the zip file.

Signature

```
   public Compression.Method getMethod()

```

Return Value

Type: Compression.Method

Uses the `Method` enum values to indicate the compression method as `DEFLATED` or `STORED` .


Apex Reference Guide ZipWriter Class

##### **`removeEntry(name)`**

Removes the entry with the specified name from the zip file.

Signature

```
   public Void removeEntry(string name)

```

Parameters

```
   name
```

Type: string

Name of the zip entry to be removed. If an entry with this name isn’t found, the method throws a `ZipException` exception.

Return Value

Type: Void

##### **`setLevel(level)`**

Sets the compression level of the zip file.

Signature

```
   public Compression.ZipWriter setLevel(compression.Level value)

```

Parameters

```
   value
```

Type: Compression.Level

Uses the `Level` enum to set the compression level.

Return Value

Type: Compression.ZipWriter

Returns the zip file set with the specified compression level.

##### **`setMethod(method)`**

Sets the compression method for the zip file.

Signature

```
   public Compression.ZipWriter setMethod(compression.Method value)

```

Parameters

```
   value
```

Type: Compression.Method

Uses the `Method` enum to set the compression method.


### Apex Reference Guide Compression Exceptions

Return Value

Type: Compression.ZipWriter

Returns the zip file set with the specified compression method.

### Compression Exceptions The Compression namespace contains exception classes.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions.

### The Compression namespace contains this exception:

**Exception** **Description**

`Compression.ZipException` Any problem with the zip operations, such as a zip entry name isn’t found.

## ConnectApi Namespace The ConnectApi namespace (also called Connect in Apex) provides classes for accessing the same data available in Connect REST

API. Use Connect in Apex to create custom experiences in Salesforce.

## For information about working with the ConnectApi classes, see Connect in Apex.

IN THIS SECTION:

ActionLinks Class
Create, delete, and get information about an action link group definition; get information about an action link group; get action link
diagnostic information.

Announcements Class
Access information about announcements and post announcements.

BotVersionActivation Class
Access and update activation information of a bot version.

CdpActivation Class
Get, create, update, and delete Data 360 activations.

CdpActivationTarget Class
Get, create, and update Data 360 activation targets.

CdpAudienceDMO Class
Get activation records from Data 360 Audience Data Model Objects (DMOs).

CdpCalculatedInsight Class
Create, delete, get, run, and update Data 360 calculated insights.

CdpConnection Class
Get database schemas for a Data 360 connection.

CdpDataSpace Class
Get Data 360 data spaces.


Apex Reference Guide ConnectApi Namespace

CdpDataStreams Class
Run Data 360 data streams.

CdpIdentityResolution Class
Create, delete, get, run, and update Data 360 identity resolution rulesets.

CdpMachineLearning Class
Make a machine-learning prediction with Data 360.

CdpQuery Class
Get Data 360 metadata and query data.

CdpSegment Class
Create, delete, get, publish, and update Data 360 segments.

Chatter Class
Access information about followers and subscriptions for records.

ChatterFavorites Class
Chatter favorites give you easy access to topics, list views, and feed searches.

ChatterFeeds Class
Get, post, and delete feed elements, likes, comments, and bookmarks. You can also search feed elements, share feed elements, and
vote on polls.

ChatterGroups Class
Information about groups, such as the group’s members, photo, and the groups the specified user is a member of. Add members
to a group, remove members, and change the group photo.

ChatterMessages Class
Get, send, search, and reply to private messages. You can also get and search private conversations, mark conversations as read, and
get a count of unread private messages.

ChatterUsers Class
Access information about users, such as activity, followers, subscriptions, files, and groups.

Clm Class
Create and update Contract Lifecycle Management (CLM) contracts using object ID.

CommerceBuyerExperience Class
Create, delete, or get commerce addresses. Get order delivery group, order item, order shipments, shipment items, and order
summaries. Get adjustments for order items and order summaries.

CommerceCart Class
Get, create, update, calculate, and delete carts. Get cart items, add items to carts, update and delete cart items.

CommerceCatalog Class
Get products, product categories, and product category paths.

CommerceCatalogManagement Class
Create or update a composite product. Create a variation product.

CommercePromotions Class
Evaluate promotions for Commerce orders. Get coupon code redemption usage.

CommerceSearch Class
Get sort rules for the live search index. Get product search suggestions. Search products.


Apex Reference Guide ConnectApi Namespace

CommerceSearchConnectFamily Class
Search products by search term or category in a webstore.

CommerceSearchSettings Class
Get indexes. Get index logs. Create an index of a product catalog.

CommerceStorePricing Class
Get product prices.

CommerceWishlist Class
Get, create, update, and delete wishlists. Add wishlists to carts. Get wishlist items, add items to wishlists, and delete wishlist items.

Communities Class
Get information about Experience Cloud sites in your org.

CommunityModeration Class
Get information about flagged feed items and comments in an Experience Cloud site. Add and remove flags from comments and
feed items.

ContentHub Class
Access Files Connect repositories and their files and folders.

ConversationApplicationDefinition Class
Access information about a conversation application definition.

Datacloud Class
Purchase Data.com contact or company records, and retrieve purchase information.

EinsteinLLM Class
Get a list of prompt templates and generate LLM responses for prompt templates.

EmailMergeFieldService Class
Extract a list of merge fields for an object. A merge field is a field you can put in an email template, mail merge template, custom
link, or formula to incorporate values from a record.

EmployeeProfiles Class
Get, set and crop, and delete employee banner photos and photos.

Exchanges Class
Preview and submit cart to exchange orders.

ExtendedCommerceDelivery Class
Access information about delivery estimation.

ExternalEmailServices Class
Access information about integration with external email services, such as sending email within Salesforce through an external email
account.

ExternalManagedAccount Class
Get externally managed accounts.

FieldService Class
Preview and create shifts from a pattern.

FlowApprovalProcesses Class
Get the status and available actions for flow approval processes.

FulfillmentOrder Class
Fulfill orders in Order Management.


Apex Reference Guide ConnectApi Namespace

IBusinessObjectivesAndRecsFamily Class
Get and patch business objectives, or goals. Get, create, patch, and update recommended actions for business objectives.

Knowledge Class
Get information about trending articles in Experience Cloud sites.

LightningScheduler Class
Create and update service appointments.

ManagedContent Class
Clone managed content. Create and get managed content. Create, delete, or update a digital asset management (DAM) provider
instance. Delete and replace variants. Get channels. Get a managed content space. Get DAM providers. Get targets that managed
content space folders can be shared with. Get and update targets that managed content space folders are shared with. Publish and
unpublish content.

ManagedContentChannels Class
Get managed content channels. Create, get, update, or delete a managed content channel.

ManagedContentDelivery Class
Get collection items. Get a managed content channel. Get managed content.

ManagedContentSpaces Class
Get channels in a managed content space. Add or remove channels from a managed content space.

ManagedTopics Class
Get managed topics in an Experience Cloud site. Create, delete, and reorder managed topics.

MarketingIntegration Class
Get, save, and submit a microsites marketing integration form for an Experience Cloud site.

Mentions Class
Access information about mentions. A mention is an “@” character followed by a user or group name. When a user or group is
mentioned, they receive a notification.

Missions Class
Export and purge mission activity for users. Get a user’s mission progress. Update mission activity counts for users.

NamedCredentials Class
Create, refresh, get, delete, replace, and update credentials. Create and get external credentials. Create and get named credentials.
Create, get, delete, and update external auth identity providers. Get the URL for the OAuth token flow for an external credential.

NavigationMenu Class
Get navigation menu items for an Experience Cloud site.

NextBestAction Class
Execute recommendation strategies, get recommendations, manage recommendation reactions.

OmnichannelInventoryService Class
Route orders to inventory locations in Order Management.

OMSAnalytics Class
Get products with return rates, get text classified into different classifications using text analysis, and capture the return reasons from
external sources based on the product ids.

Orchestration Class
Get orchestration instances.


Apex Reference Guide ConnectApi Namespace

OrderPaymentSummary Class
Work with payments in Order Management.

OrderSummary Class
Work with orders in Order Management.

OrderSummaryCreation Class
Create Order Summaries in Order Management.

Organization Class
Access information about an org.

PardotBusinessUnitContext Class
Get the Pardot business units the context user has access to.

Payments Class
Authorize a payment, capture an authorized payment, and refund an authorized payment.

Personalization Class
Get assigned personalization audiences that match the user context. Create, get, update, and delete an audience. Get personalization
targets that match the user context, based on the assigned audiences that include the user. Create and update targets. Get and
delete a target.

PickTicket Class
Create tickets to fulfill orders.

QuestionAndAnswers Class
Access question and answers suggestions.

Recommendations Class
Get and reject Chatter, custom, and static recommendations. Create, get, update, and delete custom recommendation audiences,
custom recommendation definitions, and scheduled custom recommendations.

RecordFilterCriteriaFamily Class
Filter records on recordset filter criteria.

Records Class
Access information about record motifs, which are small icons used to distinguish record types in the Salesforce UI.

RecordUi Class
Get picklist values by record type.

RegisterGuestBuyer Class
Register a guest buyer for a webstore using an account ID, enabling a guest buyer to order on behalf of another buyer.

Repricing Class
Perform functions related to repricing orders in Order Management.

ReturnOrder Class
Process ReturnOrders in Order Management, limited to 2,000 requests per hour.

Routing Class
Route orders to inventory locations in Order Management.

SalesforceInbox Class
Access information about Automated Activity Capture, which is available in Einstein and Salesforce Inbox.

Search Class
Search objects using keywords or a natural language query.


### Apex Reference Guide ActionLinks Class

Sites Class
Search an Experience Cloud site.

SmartDataDiscovery Class
Get predictions on Salesforce objects.

SocialEngagement Class
Manage information about social accounts or fan pages for social networks.

Surveys Class
Send survey invitations by email.

TaxPlatform Class
Apply or cancel tax.

Topics Class
Access information about topics, such as their descriptions, the number of people talking about them, related topics, and information
about groups contributing to the topic. Update a topic’s name or description, merge topics, and add and remove topics from records
and feed items.

UserProfiles Class
Access user profile data. The user profile data populates the profile page (also called the Chatter profile page). This data includes
user information (such as address, manager, and phone number), some user capabilities (permissions), and a set of subtab apps,
which are custom tabs on the profile page.

Zones Class
Access information about Chatter Answers zones in your organization. Zones organize questions into logical groups, with each zone
having its own focus and unique questions.

ConnectApi Input Classes
Some `ConnectApi` methods take arguments that are instances of `ConnectApi` input classes.

ConnectApi Output Classes
Most `ConnectApi` methods return instances of `ConnectApi` output classes.

ConnectApi Enums
Enums specific to the `ConnectApi` namespace.

ConnectApi Exceptions
The `ConnectApi` namespace contains exception classes.

ConnectApi Utilities
The `ConnectApi` namespace contains a utility class.

ConnectApi Release Notes
Use the Salesforce Release Notes to learn about the most recent updates and changes to the ConnectApi namespace in Apex.

### ActionLinks Class

Create, delete, and get information about an action link group definition; get information about an action link group; get action link
diagnostic information.

Namespace

ConnectApi


Apex Reference Guide ActionLinks Class

Usage

An action link is a button on a feed element. Clicking an action link can take a user to a Web page, initiate a file download, or invoke an
API call to Salesforce or to an external server. An action link includes a URL and an HTTP method, and can include a request body and
header information, such as an OAuth token for authentication. Use action links to integrate Salesforce and third-party services into the
feed so that users can drive productivity and accelerate innovation.

There are two views of an action link and an action link group: the definition, and the context user’s view. The definition includes potentially
sensitive information, such as authentication information. The context user’s view is filtered by visibility options and the values reflect
the state of the context user.

Action link definition can be sensitive to a third party (for example, OAuth bearer token headers). For this reason, only calls made from
the Apex namespace that created the action link definition can read, modify, or delete the definition. In addition, the user making the
call must have created the definition or have View All Data permission. Use these methods to operate on action link group definitions
(which contain action link definitions).

**•** createActionLinkGroupDefinition(communityId, actionLinkGroup)

**•** deleteActionLinkGroupDefinition(communityId, actionLinkGroupId)

**•** getActionLinkGroupDefinition(communityId, actionLinkGroupId)

Use these methods to operate on a context user’s view of an action link or an action link group.

**•** getActionLink(communityId, actionLinkId)

**•** getActionLinkGroup(communityId, actionLinkGroupId)

**•** getActionLinkDiagnosticInfo(communityId, actionLinkId)

[For information about how to use action links, see Working with Action Links.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_features_action_links.htm)

#### ActionLinks Methods These methods are for ActionLinks . All methods are static.

IN THIS SECTION:

createActionLinkGroupDefinition(communityId, actionLinkGroup)
Create an action link group definition. To associate an action link group with a feed element, first create an action link group definition.
Then post a feed element with an associated actions capability.

deleteActionLinkGroupDefinition(communityId, actionLinkGroupId)
Delete an action link group definition. Deleting an action link group definition removes all references to it from feed elements.

getActionLink(communityId, actionLinkId)
Get information about an action link, including state for the context user.

getActionLinkDiagnosticInfo(communityId, actionLinkId)
Get diagnostic information returned when an action link executes. Diagnostic information is given only for users who can access
the action link.

getActionLinkGroup(communityId, actionLinkGroupId)
Get information about an action link group including state for the context user.

getActionLinkGroupDefinition(communityId, actionLinkGroupId)
Get information about an action link group definition.


Apex Reference Guide ActionLinks Class

```
  createActionLinkGroupDefinition(communityId, actionLinkGroup)

```

Create an action link group definition. To associate an action link group with a feed element, first create an action link group definition.
Then post a feed element with an associated actions capability.

API Version

33.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ActionLinkGroupDefinition createActionLinkGroupDefinition(String

   communityId, ConnectApi.ActionLinkGroupDefinitionInput actionLinkGroup)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   actionLinkGroup
```

Type: `ConnectApi.ActionLinkGroupDefinitionInput`

A `ConnectApi.ActionLinkGroupDefinitionInput` object that defines the action link group.

Return Value

Type: `ConnectApi.ActionLinkGroupDefinition`

Usage

An action link is a button on a feed element. Clicking an action link can take a user to a Web page, initiate a file download, or invoke an
API call to Salesforce or to an external server. An action link includes a URL and an HTTP method, and can include a request body and
header information, such as an OAuth token for authentication. Use action links to integrate Salesforce and third-party services into the
feed so that users can drive productivity and accelerate innovation.

All action links must belong to a group. Action links in a group are mutually exclusive and share some properties. Define standalone
actions in their own action group.

Information in the action link group definition can be sensitive to a third party (for example, OAuth bearer token headers). For this reason,
only calls made from the Apex namespace that created the action link group definition can read, modify, or delete the definition. In
addition, the user making the call must have created the definition or have View All Data permission.

Note: Invoking `ApiAsync` action links from an app requires a call to set the status. However, there isn’t currently a way to set
[the status of an action link using Apex. To set the status, use Connect REST API. See the Action Link resource in the Connect REST](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/)
[API Developer Guidefor more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/)


Apex Reference Guide ActionLinks Class

Example for Defining an Action Link and Posting with a Feed Element

[For more information about this example, see Define an Action Link and Post with a Feed Element.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link.htm)

```
   ConnectApi.ActionLinkGroupDefinitionInput actionLinkGroupDefinitionInput = new

   ConnectApi.ActionLinkGroupDefinitionInput();

   ConnectApi.ActionLinkDefinitionInput actionLinkDefinitionInput = new

   ConnectApi.ActionLinkDefinitionInput();

   ConnectApi.RequestHeaderInput requestHeaderInput1 = new ConnectApi.RequestHeaderInput();

   ConnectApi.RequestHeaderInput requestHeaderInput2 = new ConnectApi.RequestHeaderInput();

   // Create the action link group definition.

   actionLinkGroupDefinitionInput.actionLinks = New

   List<ConnectApi.ActionLinkDefinitionInput>();

   actionLinkGroupDefinitionInput.executionsAllowed =

   ConnectApi.ActionLinkExecutionsAllowed.OncePerUser;

   actionLinkGroupDefinitionInput.category = ConnectApi.PlatformActionGroupCategory.Primary;

   // To Do : Verify that the date is in the future.

   // Action link groups are removed from feed elements on the expiration date.

   datetime myDate = datetime.newInstance(2016, 3, 1);

   actionLinkGroupDefinitionInput.expirationDate = myDate;

   // Create the action link definition.

   actionLinkDefinitionInput.actionType = ConnectApi.ActionLinkType.Api;

   actionLinkDefinitionInput.actionUrl = '/services/data/v33.0/chatter/feed-elements';

   actionLinkDefinitionInput.headers = new List<ConnectApi.RequestHeaderInput>();

   actionLinkDefinitionInput.labelKey = 'Post';

   actionLinkDefinitionInput.method = ConnectApi.HttpRequestMethod.HttpPost;

   actionLinkDefinitionInput.requestBody = '{\"subjectId\": \"me\",\"feedElementType\":

   \"FeedItem\",\"body\": {\"messageSegments\": [{\"type\": \"Text\",\"text\": \"This is a

   test post created via an API action link.\"}]}}';

   actionLinkDefinitionInput.requiresConfirmation = true;

   // To Do : Substitute an OAuth value for your Salesforce org.

   requestHeaderInput1.name = 'Authorization';

   requestHeaderInput1.value = 'OAuth

   00DD00000007WNP!ARsAQCwoeV0zzAV847FTl4zF.85w.EwsPbUgXR4SAjsp ';

   actionLinkDefinitionInput.headers.add(requestHeaderInput1);

   requestHeaderInput2.name = 'Content-Type';

   requestHeaderInput2.value = 'application/json';

   actionLinkDefinitionInput.headers.add(requestHeaderInput2);

   // Add the action link definition to the action link group definition.

   actionLinkGroupDefinitionInput.actionLinks.add(actionLinkDefinitionInput);

   // Instantiate the action link group definition.

   ConnectApi.ActionLinkGroupDefinition actionLinkGroupDefinition =

   ConnectApi.ActionLinks.createActionLinkGroupDefinition(Network.getNetworkId(),

   actionLinkGroupDefinitionInput);

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   ConnectApi.AssociatedActionsCapabilityInput associatedActionsCapabilityInput = new

```


Apex Reference Guide ActionLinks Class

```
   ConnectApi.AssociatedActionsCapabilityInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   // Set the properties of the feedItemInput object.

   feedItemInput.body = messageBodyInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   feedItemInput.subjectId = 'me';

   // Create the text for the post.

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   textSegmentInput.text = 'Click to post a feed item.';

   messageBodyInput.messageSegments.add(textSegmentInput);

   // The feedElementCapabilitiesInput object holds the capabilities of the feed item.

   // Define an associated actions capability to hold the action link group.

   // The action link group ID is returned from the call to create the action link group

   definition.

   feedElementCapabilitiesInput.associatedActions = associatedActionsCapabilityInput;

   associatedActionsCapabilityInput.actionLinkGroupIds = new List<String>();

   associatedActionsCapabilityInput.actionLinkGroupIds.add(actionLinkGroupDefinition.id);

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

```

Example for Defining an Action Link in a Template and Posting with a Feed Element

[For more information about this example, see Define an Action Link in a Template and Post with a Feed Element.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link_template.htm)

```
   // Get the action link group template Id.

   ActionLinkGroupTemplate template = [SELECT Id FROM ActionLinkGroupTemplate WHERE

   DeveloperName='Doc_Example'];

   // Add binding name-value pairs to a map.

   // The names are defined in the action link template(s) associated with the action link

   group template.

   // Get them from Setup UI or SOQL.

   Map<String, String> bindingMap = new Map<String, String>();

   bindingMap.put('ApiVersion', 'v33.0');

   bindingMap.put('Text', 'This post was created by an API action link.');

   bindingMap.put('SubjectId', 'me');

   // Create ActionLinkTemplateBindingInput objects from the map elements.

   List<ConnectApi.ActionLinkTemplateBindingInput> bindingInputs = new

   List<ConnectApi.ActionLinkTemplateBindingInput>();

   for (String key : bindingMap.keySet()) {

      ConnectApi.ActionLinkTemplateBindingInput bindingInput = new

   ConnectApi.ActionLinkTemplateBindingInput();

      bindingInput.key = key;

      bindingInput.value = bindingMap.get(key);

      bindingInputs.add(bindingInput);

```


Apex Reference Guide ActionLinks Class

```
   }

   // Set the template Id and template binding values in the action link group definition.

   ConnectApi.ActionLinkGroupDefinitionInput actionLinkGroupDefinitionInput = new

   ConnectApi.ActionLinkGroupDefinitionInput();

   actionLinkGroupDefinitionInput.templateId = template.id;

   actionLinkGroupDefinitionInput.templateBindings = bindingInputs;

   // Instantiate the action link group definition.

   ConnectApi.ActionLinkGroupDefinition actionLinkGroupDefinition =

    ConnectApi.ActionLinks.createActionLinkGroupDefinition(Network.getNetworkId(),

   actionLinkGroupDefinitionInput);

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   ConnectApi.AssociatedActionsCapabilityInput associatedActionsCapabilityInput = new

   ConnectApi.AssociatedActionsCapabilityInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   // Define the FeedItemInput object to pass to postFeedElement

   feedItemInput.body = messageBodyInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   feedItemInput.subjectId = 'me';

   // The MessageBodyInput object holds the text in the post

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   textSegmentInput.text = 'Click to post a feed item.';

   messageBodyInput.messageSegments.add(textSegmentInput);

   // The FeedElementCapabilitiesInput object holds the capabilities of the feed item.

   // For this feed item, we define an associated actions capability to hold the action link

    group.

   // The action link group ID is returned from the call to create the action link group

   definition.

   feedElementCapabilitiesInput.associatedActions = associatedActionsCapabilityInput;

   associatedActionsCapabilityInput.actionLinkGroupIds = new List<String>();

   associatedActionsCapabilityInput.actionLinkGroupIds.add(actionLinkGroupDefinition.id);

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

##### **`deleteActionLinkGroupDefinition(communityId, actionLinkGroupId)`**

```

Delete an action link group definition. Deleting an action link group definition removes all references to it from feed elements.

API Version

33.0


Apex Reference Guide ActionLinks Class

Requires Chatter

No

Signature

```
   public static void deleteActionLinkGroupDefinition(String communityId, String

   actionLinkGroupId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   actionLinkGroupId
```

Type: String

The ID of the action link group.

Return Value

Type: Void

Usage

Information in the action link group definition can be sensitive to a third party (for example, OAuth bearer token headers). For this reason,
only calls made from the Apex namespace that created the action link group definition can read, modify, or delete the definition. In
addition, the user making the call must have created the definition or have View All Data permission.

##### **`getActionLink(communityId, actionLinkId)`**

Get information about an action link, including state for the context user.

API Version

33.0

Requires Chatter

No

Signature

```
   public static ConnectApi.PlatformAction getActionLink(String communityId, String

   actionLinkId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ActionLinks Class

```
   actionLinkId
```

Type: String

The ID of the action link.

Return Value

Type: `ConnectApi.PlatformAction`

##### **`getActionLinkDiagnosticInfo(communityId, actionLinkId)`**

Get diagnostic information returned when an action link executes. Diagnostic information is given only for users who can access the
action link.

API Version

33.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ActionLinkDiagnosticInfo getActionLinkDiagnosticInfo(String

   communityId, String actionLinkId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   actionLinkId
```

Type: String

The ID of the action link.

Return Value

Type: `ConnectApi.ActionLinkDiagnosticInfo`

##### **`getActionLinkGroup(communityId, actionLinkGroupId)`**

Get information about an action link group including state for the context user.

API Version

33.0


Apex Reference Guide ActionLinks Class

Requires Chatter

No

Signature

```
   public static ConnectApi.PlatformActionGroup getActionLinkGroup(String communityId,

   String actionLinkGroupId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   actionLinkGroupId
```

Type: String

The ID of the action link group.

Return Value

Type: `ConnectApi.PlatformActionGroup`

Usage

All action links must belong to a group. Action links in a group are mutually exclusive and share some properties. Action link groups are
accessible by clients, unlike action link group definitions.

##### **`getActionLinkGroupDefinition(communityId, actionLinkGroupId)`**

Get information about an action link group definition.

API Version

33.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ActionLinkGroupDefinition getActionLinkGroupDefinition(String

   communityId, String actionLinkGroupId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


### Apex Reference Guide Announcements Class

```
   actionLinkGroupId
```

Type: String

The ID of the action link group.

Return Value

Type: `ConnectApi.ActionLinkGroupDefinition`

Usage

Information in the action link group definition can be sensitive to a third party (for example, OAuth bearer token headers). For this reason,
only calls made from the Apex namespace that created the action link group definition can read, modify, or delete the definition. In
addition, the user making the call must have created the definition or have View All Data permission.

### Announcements Class

Access information about announcements and post announcements.

Namespace

ConnectApi

Usage

Use the `ConnectApi.Announcements` class to get, create, update, and delete announcements. Use an announcement to
highlight information. Users can discuss, like, and post comments on announcements. Deleting the feed post deletes the announcement.

This image shows an announcement displayed in a group. Creating an announcement also creates a feed item with the announcement
text.


Apex Reference Guide Announcements Class

An announcement displays in a designated location in the Salesforce UI until 11:59 p.m. on its expiration date, unless it’s deleted or
replaced by another announcement.

#### Announcements Methods These methods are for Announcements . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

##### deleteAnnouncement(communityId, announcementId)

Delete an announcement.

getAnnouncement(communityId, announcementId)
Get an announcement.

getAnnouncements(communityId, parentId)
Get the first page of announcements.

getAnnouncements(communityId, parentId, pageParam, pageSize)
Get a page of announcements.

postAnnouncement(communityId, announcement)
Post an announcement.

updateAnnouncement(communityId, announcementId, expirationDate)
Update the expiration date of an announcement.

##### **`deleteAnnouncement(communityId, announcementId)`**

Delete an announcement.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static void deleteAnnouncement(String communityId, String announcementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   announcementId
```

Type: String


Apex Reference Guide Announcements Class

An announcement ID, which has a prefix of 0BT.

Return Value

Type: Void

Usage

To get a list of announcements in a group, call `getAnnouncements(communityId, parentId)` or

`getAnnouncements(communityId, parentId, pageParam, pageSize)` .

To post an announcement to a group, call `postAnnouncement(communityId, announcement)` .

##### **`getAnnouncement(communityId, announcementId)`**

Get an announcement.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Announcement getAnnouncement(String communityId, String

   announcementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   announcementId
```

Type: String

An announcement ID, which has a prefix of 0BT.

Return Value

Type: `ConnectApi.Announcement`

Usage

To get a list of announcements in a group, call `getAnnouncements(communityId, parentId)` or

`getAnnouncements(communityId, parentId, pageParam, pageSize)` .

To post an announcement to a group, call `postAnnouncement(communityId, announcement)` .


Apex Reference Guide Announcements Class

##### **`getAnnouncements(communityId, parentId)`**

Get the first page of announcements.

API Version

36.0

Available to Guest Users

38.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.AnnouncementPage getAnnouncements(String communityId, String

   parentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   parentId
```

Type: String

ID of the parent entity for the announcement, that is, a group ID when the announcement appears in a group.

Return Value

Type: `ConnectApi.AnnouncementPage`

##### **`getAnnouncements(communityId, parentId, pageParam, pageSize)`**

Get a page of announcements.

API Version

36.0

Available to Guest Users

38.0

Requires Chatter

Yes


Apex Reference Guide Announcements Class

Signature

```
   public static ConnectApi.AnnouncementPage getAnnouncements(String communityId, String

   parentId, Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   parentId
```

Type: String

ID of the parent entity for the announcement, that is, a group ID when the announcement appears in a group.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of announcements per page.

Return Value

Type: `ConnectApi.AnnouncementPage`

##### **`postAnnouncement(communityId, announcement)`**

Post an announcement.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Announcement postAnnouncement(String communityId,

   ConnectApi.AnnouncementInput announcement)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   announcement
```

Type: `ConnectApi.AnnouncementInput`


Apex Reference Guide Announcements Class

A `ConnectApi.AnnouncementInput` object.

Return Value

Type: `ConnectApi.Announcement`

##### **`updateAnnouncement(communityId, announcementId, expirationDate)`**

Update the expiration date of an announcement.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Announcement updateAnnouncement(String communityId, String

   announcementId, Datetime expirationDate)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   announcementId
```

Type: String

An announcement ID, which has a prefix of 0BT.

```
   expirationDate
```

Type: Datetime

The Salesforce UI displays an announcement until 11:59 p.m. on this date unless another announcement is posted first. The Salesforce
UI ignores the time value in the `expirationDate` . However, you can use the time value to create your own display logic in your
own UI.

Return Value

Type: `ConnectApi.Announcement`

Usage

To get a list of announcements in a group, call `getAnnouncements(communityId, parentId)` or

`getAnnouncements(communityId, parentId, pageParam, pageSize)` .

To post an announcement to a group, call `postAnnouncement(communityId, announcement)` .


### Apex Reference Guide BotVersionActivation Class BotVersionActivation Class

Access and update activation information of a bot version.

Namespace

ConnectApi

#### BotVersionActivation Methods

### These methods are for BotVersionActivation . All methods are static.

IN THIS SECTION:

##### getVersionActivationInfo(botVersionId)

Get the active or inactive status of the bot version.

updateVersionStatus(botVersionId, status, postBody)
Update the status of the specified bot version.

##### **`getVersionActivationInfo(botVersionId)`**

Get the active or inactive status of the bot version.

API Version

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BotVersionActivationInfo getVersionActivationInfo(String

   botVersionId)

```

Parameters

```
   botVersionId
```

Type: String

ID of the bot version.

Return Value

Type: `ConnectApi.BotVersionActivationInfo`


Apex Reference Guide BotVersionActivation Class

Usage

To access this method, enable the bot feature, and the user must be an admin or have the Manage Bots or Manage Bots Training Data
user permissions.

##### **`updateVersionStatus(botVersionId, status, postBody)`**

Update the status of the specified bot version.

API Version

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BotVersionActivationInfo updateVersionStatus(String

   botVersionId, ConnectApi.BotVersionActivationStatus status,

   ConnectApi.BotVersionActivationInput postBody)

```

Parameters

```
   botVersionId
```

Type: String

ID of the bot version.

```
   status
```

Type: `ConnectApi.BotVersionActivationStatus`

Activation status of the bot version. Values are:

**•** `Active`

**•** `Inactive`

Activation status must be specified in the _`status`_ or _`postBody`_ parameter.

```
   postBody
```

Type: `ConnectApi.BotVersionActivationInput`

Parameters to update for the bot version. Activation status must be specified in the _`status`_ or _`postBody`_ parameter.

Return Value

Type: `ConnectApi.BotVersionActivationInfo`

Usage

To access this method, enable the bot feature, and the user must be an admin or have the Manage Bots or Manage Bots Training Data
user permissions.


### Apex Reference Guide CdpActivation Class CdpActivation Class

Get, create, update, and delete Data 360 activations.

Namespace

ConnectApi

#### CdpActivation Methods

### These methods are for CdpActivation . All methods are static.

IN THIS SECTION:

##### getActivations()

Get activations.

getActivationsPaginated(batchSize, offset, orderBy, filters)
Get a paginated list of activations.

createActivation(input)
Create an activation.

deleteActivation(activationId)
Delete an activation.

getActivation(activationId)
Get an activation by ID.

updateActivation(activationId, input)
Update an activation by ID.

##### **`getActivations()`**

Get activations.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ActivationCollection getActivations()

```

Return Value

Type: `ConnectApi.ActivationCollection`


Apex Reference Guide CdpActivation Class

##### **`getActivationsPaginated(batchSize, offset, orderBy, filters)`**

Get a paginated list of activations.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ActivationCollection getActivationsPaginated(Integer batchSize,

   Integer offset, String orderBy, String filters)

```

Parameters

```
   batchSize
```

Type: Integer

Number of results to return. Values are from `1` through `200` . If unspecified, the default value is `20` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. Must be greater than or equal to `0` . If unspecified, no rows are skipped.

```
   orderBy
```

Type: String

Specify `createdDate` to sort results by creation date. If unspecified, items are returned by ID in ascending order.

```
   filters
```

Type: String

Filter the result set to a more narrow scope or specific type. These filters are supported:

**•** name (field name: name; description: name of the activation)

**•** marketSegmentId (field name: segmentId; description: segment ID of the activation)

**•** activationTargetId (field name: activationTarget.id; description: activation target ID of the activation)

**•** activationRefreshType (field name: refreshType; description: refresh type of the activation; example: incremental)

**•** activationStatus (field name: status; description: status of the activation, which accepts only the values in the status response
field; example: active)

Return Value

Type: `ConnectApi.ActivationCollection`

##### **`createActivation(input)`**

Create an activation.


Apex Reference Guide CdpActivation Class

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Activation createActivation(ConnectApi.ActivationDefinitionInput

   input)

```

Parameters

```
   input
```

Type: `ConnectApi.ActivationDefinitionInput`

Input representation for an activation.

Return Value

Type: `ConnectApi.Activation`

##### **`deleteActivation(activationId)`**

Delete an activation.

Note: Before deleting an activation, ensure there are no downstream systems that expect data from it. After you delete an
activation, Data 360 stops sending data to any downstream systems that are associated with the deleted activation. To identify
the downstream system (activation target) that's associated with the activation, use the getActivation(activationId) resource. It
provides the activation target details needed to evaluate the impact before deleting the activation.

API Version

60.0

Requires Chatter

No

Signature

```
   public static Void deleteActivation(String activationId)

```

Parameters

```
   activationId
```

Type: String

The unique identifier (ID) or developer name of a specific activation target.


Apex Reference Guide CdpActivation Class

Return Value

Type: Void

##### **`getActivation(activationId)`**

Get an activation by ID.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Activation getActivation(String activationId)

```

Parameters

```
   activationId
```

Type: String

The unique identifier (ID) or developer name of a specific activation target.

Return Value

Type: `ConnectApi.Activation`

##### **`updateActivation(activationId, input)`**

Update an activation by ID.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Activation updateActivation(String activationId,

   ConnectApi.ActivationDefinitionInput input)

```

Parameters

```
   activationId
```

Type: String


### Apex Reference Guide CdpActivationTarget Class

The unique identifier (ID) or developer name of a specific activation target.

```
   input
```

Type: `ConnectApi.ActivationDefinitionInput`

Input representation for an activation.

Return Value

Type: `ConnectApi.Activation`

### CdpActivationTarget Class

Get, create, and update Data 360 activation targets.

Namespace

ConnectApi

#### CdpActivationTarget Methods

### These methods are for CdpActivationTarget . All methods are static.

IN THIS SECTION:

##### createActivationTarget(input)

Create an activation target.

getActivationTarget(activationTargetId)
Get an activation target by ID.

getActivationTargets()
Get a list of activation targets.

getActivationTargetsPaginated(batchSize, offset, orderBy, filters)
Get a paginated list of activation targets.

updateActivationTarget(activationTargetId, input)
Update an activation target.

##### **`createActivationTarget(input)`**

Create an activation target.

API Version

60.0

Requires Chatter

No


Apex Reference Guide CdpActivationTarget Class

Signature

```
   public static ConnectApi.ActivationTarget

   createActivationTarget(ConnectApi.ActivationTargetInput input)

```

Parameters

```
   input
```

Type: `ConnectApi.ActivationTargetInput`

Input details for the activation target.

Return Value

Type: `ConnectApi.ActivationTarget`

##### **`getActivationTarget(activationTargetId)`**

Get an activation target by ID.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ActivationTarget getActivationTarget(String activationTargetId)

```

Parameters

```
   activationTargetId
```

Type: String

ID of the activation target.

Return Value

Type: `ConnectApi.ActivationTarget`

##### **`getActivationTargets()`**

Get a list of activation targets.

API Version

60.0


Apex Reference Guide CdpActivationTarget Class

Requires Chatter

No

Signature

```
   public static ConnectApi.ActivationTargetCollection getActivationTargets()

```

Return Value

Type: `ConnectApi.ActivationTargetCollection`

##### **`getActivationTargetsPaginated(batchSize, offset, orderBy, filters)`**

Get a paginated list of activation targets.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ActivationTargetCollection getActivationTargetsPaginated(Integer

   batchSize, Integer offset, String orderBy, String filters)

```

Parameters

```
   batchSize
```

Type: Integer

Number of results to return. Values are from `1` through `200` . For example, specify `20` to return 20 results.

```
   offset
```

Type: Integer

Number of rows to skip before returning results. Must be greater than or equal to `0` . For example, specify `0` to skip no rows.

```
   orderBy
```

Type: String

Sort order for the result set. Results are ordered by creation date. Specify `createddate` to order results in ascending order. Specify
`createddate desc` to order results in descending order.

```
   filters
```

Type: String

Filter the result set to a more narrow scope or specific type. These filters are supported:

**•** `masterLabel`     - Matches the field `name`, which is a string that identifies the name of the activation target.

**•** `targetStatus`     - Matches the field `status`, which is an enum that indicates the status of the activation target. Values must
match those listed in the `status` response field.


### Apex Reference Guide CdpAudienceDMO Class

**•** `connectionType`     - Matches the field `platformType`, which is an enum that indicates the platform type of the activation
target. Values must match those listed in the `platformType` response field.

**•** `platformName`     - Matches the field `platformName`, which is a string that indentifies the platform name of the activation
target.

These are examples of filter specifications:

**•** `masterLabel in Target002`

**•** `targetStatus in active`

**•** `platformName in Customer Data Platform`

**•** `targetStatus in active AND platformName in Amazon S3`

Return Value

Type: `ConnectApi.ActivationTargetCollection`

##### **`updateActivationTarget(activationTargetId, input)`**

Update an activation target.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ActivationTarget updateActivationTarget(String

   activationTargetId, ConnectApi.ActivationTargetInput input)

```

Parameters

```
   activationTargetId
```

Type: String

ID of the activation target.

```
   input
```

Type: `ConnectApi.ActivationTargetInput`

Input details for the activation target.

Return Value

Type: `ConnectApi.ActivationTarget`

### CdpAudienceDMO Class

Get activation records from Data 360 Audience Data Model Objects (DMOs).


### Apex Reference Guide CdpCalculatedInsight Class

Namespace

ConnectApi

#### CdpAudienceDMO Methods These methods are for CdpAudienceDMO . All methods are static.

IN THIS SECTION:

##### getActivationData(activationId)

Get a list of all activation records from Audience Data Model Objects (DMOs).

##### **`getActivationData(activationId)`**

Get a list of all activation records from Audience Data Model Objects (DMOs).

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.AudienceDMOCollection getActivationData(String activationId)

```

Parameters

```
   activationId
```

Type: String

The unique identifier (ID) or developer name of a specific activation target.

Return Value

Type: `ConnectApi.AudienceDMOCollection`

### CdpCalculatedInsight Class

Create, delete, get, run, and update Data 360 calculated insights.

Namespace

ConnectApi


Apex Reference Guide CdpCalculatedInsight Class

#### CdpCalculatedInsight Methods These methods are for CdpCalculatedInsight . All methods are static.

IN THIS SECTION:

##### createCalculatedInsight(input)

Create a calculated insight.

deleteCalculatedInsight(apiName)
Delete a calculated insight.

getCalculatedInsight(apiName)
Get a calculated insight.

getCalculatedInsights(definitionType, batchSize, offset, orderby, dataspace)
Get calculated insights.

getCalculatedInsights(definitionType, batchSize, offset, orderby, dataspace, pageToken)
Get a page of calculated insights.

runCalculatedInsight(apiName)
Run a calculated insight.

updateCalculatedInsight(apiName, input)
Update a calculated insight.

##### **`createCalculatedInsight(input)`**

Create a calculated insight.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpCalculatedInsightOutput

   createCalculatedInsight(ConnectApi.CdpCalculatedInsightInput input)

```

Parameters

```
   input
```

Type: `ConnectApi.CdpCalculatedInsightInput`

Input representation for a calculated insight.

Return Value

Type: `ConnectApi.CdpCalculatedInsightOutput`


Apex Reference Guide CdpCalculatedInsight Class

##### **`deleteCalculatedInsight(apiName)`**

Delete a calculated insight.

API Version

57.0

Requires Chatter

No

Signature

```
   public static Void deleteCalculatedInsight(String apiName)

```

Parameters

```
   apiName
```

Type: String

API name of the calculated insight to delete.

Return Value

Type: Void

##### **`getCalculatedInsight(apiName)`**

Get a calculated insight.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpCalculatedInsightOutput getCalculatedInsight(String apiName)

```

Parameters

```
   apiName
```

Type: String

API name of the calculated insight to get.

Return Value

Type: `ConnectApi.CdpCalculatedInsightOutput`


Apex Reference Guide CdpCalculatedInsight Class

##### **`getCalculatedInsights(definitionType, batchSize, offset, orderby, dataspace)`**

Get calculated insights.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpCalculatedInsightPage getCalculatedInsights(String

   definitionType, Integer batchSize, Integer offset, String orderby, String dataspace)

```

Parameters

```
   definitionType
```

Type: String

Definition type of the calculated insight. Values are:

**•** `CALCULATED_METRIC`

**•** `CALCULATED_METRIC`

**•** `CALCULATED_METRIC`

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–200. If unspecified, the default value is `25` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. If unspecified, no rows are skipped.

```
   orderby
```

Type: String

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.

```
   dataspace
```

Type: String

Name of the data space.

Return Value

Type: `ConnectApi.CdpCalculatedInsightPage`


Apex Reference Guide CdpCalculatedInsight Class

##### **`getCalculatedInsights(definitionType, batchSize, offset, orderby, dataspace,`**

```
  pageToken)

```

Get a page of calculated insights.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpCalculatedInsightPage getCalculatedInsights(String

   definitionType, Integer batchSize, Integer offset, String orderby, String dataspace,

   String pageToken)

```

Parameters

```
   definitionType
```

Type: String

Definition type of the calculated insight. Values are:

**•** `CALCULATED_METRIC`

**•** `CALCULATED_METRIC`

**•** `CALCULATED_METRIC`

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–200. If unspecified, the default value is `25` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. If unspecified, no rows are skipped.

```
   orderby
```

Type: String

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.

```
   dataspace
```

Type: String

Name of the data space.

```
   pageToken
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.


Apex Reference Guide CdpCalculatedInsight Class

Return Value

Type: `ConnectApi.CdpCalculatedInsightPage`

##### **`runCalculatedInsight(apiName)`**

Run a calculated insight.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpCalculatedInsightStandardActionesponseRepresentation

   runCalculatedInsight(String apiName)

```

Parameters

```
   apiName
```

Type: String

API name of the calculated insight to run.

Return Value

Type: `ConnectApi.CdpCalculatedInsightStandardActionResponseRepresentation`

##### **`updateCalculatedInsight(apiName, input)`**

Update a calculated insight.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpCalculatedInsightOutput updateCalculatedInsight(String

   apiName, ConnectApi.CdpCalculatedInsightInput input)

```


### Apex Reference Guide CdpConnection Class

Parameters

```
   apiName
```

Type: String

API name of the calculated insight to update.

```
   input
```

Type: `ConnectApi.CdpCalculatedInsightInput`

Input representation for a calculated insight.

Return Value

Type: `ConnectApi.CdpCalculatedInsightOutput`

### CdpConnection Class

Get database schemas for a Data 360 connection.

Namespace

ConnectApi

#### CdpConnection Methods

### These methods are for CdpConnection . All methods are static.

IN THIS SECTION:

##### getDatabaseSchemas(connectionId, getDatabaseSchemasInput)

Get a list of database schemas for a connection.

##### **`getDatabaseSchemas(connectionId, getDatabaseSchemasInput)`**

Get a list of database schemas for a connection.

API Version

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ConnectionDbSchemaCollection getDatabaseSchemas(String

   connectionId, ConnectApi.ConnectionDbSchemaCollectionInputRepresentation

   getDatabaseSchemasInput)

```


### Apex Reference Guide CdpDataSpace Class

Parameters

```
   connectionId
```

Type: String

ID for the connection.

```
   getDatabaseSchemasInput
```

Type: `ConnectApi.ConnectionDbSchemaCollectionInputRepresentation`

Input representation for a database schema collection.

Return Value

Type: `ConnectApi.ConnectionDbSchemaCollection`

### CdpDataSpace Class

Get Data 360 data spaces.

Namespace

ConnectApi

#### CdpDataSpace Methods

### These methods are for CdpDataSpace . All methods are static.

IN THIS SECTION:

##### getAllDataSpaces(batchSize, offset, orderBy)

Get a collection of all data spaces that a user is assigned to.

getDataSpace(idOrName)
Get a data space by ID or API name.

##### **`getAllDataSpaces(batchSize, offset, orderBy)`**

Get a collection of all data spaces that a user is assigned to.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.DataSpaceCollectionRepresentation getAllDataSpaces(Integer

   batchSize, Integer offset, String orderBy)

```


### Apex Reference Guide CdpDataStreams Class

Parameters

```
   batchSize
```

Type: Integer

Number of results to return in each response. Values are from `1` through `4999` . For example, specify `50` to return 50 results.

```
   offset
```

Type: Integer

Number of rows to skip before returning results. Must be greater than or equal to `0` . For example, specify `0` to skip no rows.

```
   orderBy
```

Type: String

Sort order for the result set. Results are ordered by ID. Specify `id` to order results in ascending order. Specify `id desc` to order
results in descending order.

Return Value

Type: `ConnectApi.DataSpaceCollectionRepresentation`

##### **`getDataSpace(idOrName)`**

Get a data space by ID or API name.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.DataSpaceInfoRepresentation getDataSpace(String idOrName)

```

Parameters

```
   idOrName
```

Type: String

ID or API name of the data space.

Return Value

Type: `ConnectApi.DataSpaceInfoRepresentation`

### CdpDataStreams Class

Run Data 360 data streams.


### Apex Reference Guide CdpIdentityResolution Class

Namespace

ConnectApi

#### CdpDataStreams Methods These methods are for CdpDataStreams . All methods are static.

IN THIS SECTION:

##### runDataStream(recordIdOrDeveloperName, interactive)

Start a data stream run to read from a source and update a data lake object.

##### **`runDataStream(recordIdOrDeveloperName, interactive)`**

Start a data stream run to read from a source and update a data lake object.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.DataStreamActionResponse runDataStream(String

   recordIdOrDeveloperName, Boolean interactive)

```

Parameters

```
   recordIdOrDeveloperName
```

Type: String

Record ID or developer name of the data stream.

```
   interactive
```

Type: Boolean

Indicates whether to perform fast format conversion for the data stream ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.DataStreamActionResponseOutput`

### CdpIdentityResolution Class

Create, delete, get, run, and update Data 360 identity resolution rulesets.


Apex Reference Guide CdpIdentityResolution Class

Namespace

ConnectApi

#### CdpIdentityResolution Methods These methods are for CdpIdentityResolution . All methods are static.

IN THIS SECTION:

##### createIdentityResolution(input)

Create an identity resolution ruleset.

deleteIdentityResolution(identityResolution)
Delete an identity resolution ruleset.

getIdentityResolution(identityResolution)
Get an identity resolution ruleset.

getIdentityResolutions()
Get identity resolution rulesets.

runIdentityResolutionNow(identityResolution, input)
Trigger an immediate identity resolution ruleset job run.

updateIdentityResolution(identityResolution, input)
Update an identity resolution ruleset.

##### **`createIdentityResolution(input)`**

Create an identity resolution ruleset.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpIdentityResolutionOutput

   createIdentityResolution(ConnectApi.CdpIdentityResolutionConfigInput input)

```

Parameters

```
   input
```

Type: `ConnectApi.CdpIdentityResolutionConfigInput`

Input representation for creating an identity resolution ruleset.


Apex Reference Guide CdpIdentityResolution Class

Return Value

Type: `ConnectApi.CdpIdentityResolutionOutput`

##### **`deleteIdentityResolution(identityResolution)`**

Delete an identity resolution ruleset.

API Version

57.0

Requires Chatter

No

Signature

```
   public static Void deleteIdentityResolution(String identityResolution)

```

Parameters

```
   identityResolution
```

Type: String

Developer name or ID of the ruleset.

Return Value

Type: Void

##### **`getIdentityResolution(identityResolution)`**

Get an identity resolution ruleset.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpIdentityResolutionOutput getIdentityResolution(String

   identityResolution)

```

Parameters

```
   identityResolution
```

Type: String


Apex Reference Guide CdpIdentityResolution Class

Developer name or ID of the ruleset.

Return Value

Type: `ConnectApi.CdpIdentityResolutionOutput`

##### **`getIdentityResolutions()`**

Get identity resolution rulesets.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpIdentityResolutionsOutput getIdentityResolutions()

```

Return Value

Type: `ConnectApi.CdpIdentityResolutionsOutput`

##### **`runIdentityResolutionNow(identityResolution, input)`**

Trigger an immediate identity resolution ruleset job run.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpIdentityResolutionRunNowOutput

   runIdentityResolutionNow(String identityResolution,

   ConnectApi.CdpIdentityResolutionRunNowInput input)

```

Parameters

```
   identityResolution
```

Type: String

Developer name of the ruleset.


### Apex Reference Guide CdpMachineLearning Class

```
   input
```

Type: `ConnectApi.CdpIdentityResolutionRunNowInput`

Input representation for running an identity resolution ruleset job on demand.

Return Value

Type: `ConnectApi.CdpIdentityResolutionRunNowOutput`

##### **`updateIdentityResolution(identityResolution, input)`**

Update an identity resolution ruleset.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpIdentityResolutionOutput updateIdentityResolution(String

   identityResolution, ConnectApi.CdpIdentityResolutionConfigPatchInput input)

```

Parameters

```
   identityResolution
```

Type: String

Developer name or ID of the ruleset.

```
   input
```

Type: `ConnectApi.CdpIdentityResolutionConfigPatchInput`

Input representation for updating an identity resolution ruleset.

Return Value

Type: `ConnectApi.CdpIdentityResolutionOutput`

### CdpMachineLearning Class

Make a machine-learning prediction with Data 360.

Namespace

ConnectApi


### Apex Reference Guide CdpQuery Class

#### CdpMachineLearning Methods These methods are for CdpMachineLearning . All methods are static.

IN THIS SECTION:

##### predict(predict)

Make a prediction using a specified model and parameters. This request is synchronous.

##### **`predict(predict)`**

Make a prediction using a specified model and parameters. This request is synchronous.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpMlPredictResult predict(ConnectApi.CdpMlBasePredictInput

   predict)

```

Parameters

##### _`predict`_

Type: `ConnectApi.CdpMlBasePredictInput`

Input representation for a prediction.

Return Value

Type: `ConnectApi.CdpMlPredictResult`

### CdpQuery Class

Get Data 360 metadata and query data.

Namespace

ConnectApi

#### CdpQuery Methods

### These methods are for CdpQuery . All methods are static.


Apex Reference Guide CdpQuery Class

IN THIS SECTION:

getAllMetadata()
Get all metadata, including Calculated Insights, Engagement, Profile, and other objects, as well as their relationships to other objects.

getAllMetadata(entityType, entityCategory, entityName)
Get all metadata, filtering for entity type, category, and name.

getAllMetadata(entityType, entityCategory, entityName, dataspace)
Get all metadata, filtering for entity type, category, name, and data space.

getDataGraphData(dataGraphEntityName, id)
Query a data graph in the default data space. For real-time data graphs, the method attempts to retrieve data from the real-time
data graph but falls back to the standard data graph if the real-time data graph is unavailable.

getDataGraphData(dataGraphEntityName, id, dataspace)
Query a data graph in a specified data space. For real-time data graphs, the method attempts to retrieve data from the real-time
data graph but falls back to the standard data graph if the real-time data graph is unavailable.

getDataGraphData(dataGraphEntityName, id, live)
Query a data graph by performing a live lookup in the default data space. For real-time data graphs, the method attempts to retrieve
data from the real-time data graph but falls back to the standard data graph if the real-time data graph is unavailable.

getDataGraphData(dataGraphEntityName, id, dataspace, live)
Query a data graph by performing a live lookup in a specified data space. For real-time data graphs, the method attempts to retrieve
data from the real-time data graph but falls back to the standard data graph if the real-time data graph is unavailable.

getDataGraphDataWithLookupKeys(dataGraphEntityName, lookupKeys)
Query a data graph by the primary key of either the primary Data Model Object (DMO) or the Individual linked DMO. Get the data
from the default data space. For real-time data graphs, the method attempts to retrieve data from the real-time data graph but falls
back to the standard data graph if the real-time data graph is unavailable.

getDataGraphDataWithLookupKeys(dataGraphEntityName, lookupKeys, dataspace)
Query a data graph by the primary key of either the primary Data Model Object (DMO) or the Individual linked DMO. Get the data
from a specified data space. For real-time data graphs, the method attempts to retrieve data from the real-time data graph but falls
back to the standard data graph if the real-time data graph is unavailable.

getDataGraphDataWithLookupKeys(dataGraphEntityName, lookupKeys, dataspace, noCache)
Query a data graph by the primary key of either the primary Data Model Object (DMO) or the Individual linked DMO. Get the data
from a specified data space. Get data from a standard or real-time data graph. For real-time data graphs, the method attempts to
retrieve data from the real-time data graph but falls back to the standard data graph if the real-time data graph is unavailable.

getDataGraphMetadata()
Retrieve metadata from all data graphs in the default data space. Retrieves data from both standard and real-time data graphs.

getDataGraphMetadata(dataGraphEntityName)
Retrieve metadata from a specified data graph in the default data space. Retrieves data from both standard and real-time data graphs.

getDataGraphMetadata(dataGraphEntityName, dataspace)
Retrieve metadata from a specified data graph in a specified data space. Retrieves data from both standard and real-time data graphs.

getInsightsMetadata()
Get Insight metadata, including Calculated Insight objects, their dimensions and measures.

getInsightsMetadata(ciName)
Get metadata for a Calculated Insight object. Metadata includes dimensions and measures.


Apex Reference Guide CdpQuery Class

getInsightsMetadata(ciName, dataspace)
Get metadata for a Calculated Insight object and specify the data space. Metadata includes dimensions and measures.

getProfileMetadata()
Get metadata for data model objects in the profile category, including Individual, Contact Point Email, Unified Individual, and Contact
Point Address objects. Metadata includes the objects, their fields, and category.

getProfileMetadata(dataModelName)
Get metadata for a data model object in the profile category, such as Individual, Contact Point Email, Unified Individual, and Contact
Point Address. Metadata includes the list of fields, data types, and indexes available for lookup.

getProfileMetadata(dataModelName, dataspace)
Get metadata for a data model object in the profile category, such as Individual, Contact Point Email, Unified Individual, and Contact
Point Address. Also, specify the data space. Metadata includes the list of fields, data types, and indexes available for lookup.

queryANSISql(input)
Synchronously query data across data model, lake, unified, and linked objects. This query returns up to 49,999 rows.

queryANSISql(input, batchSize, offset, orderby)
Synchronously query data across data model, lake, unified, and linked objects. Specify batch size, offset, and order of the results. This
query returns up to 49,999 rows.

queryANSISql(input, batchSize, offset, orderby, dataspace)
Synchronously query data across data model, lake, unified, and linked objects. Specify batch size, offset, order of the results, and data
space. This query returns up to 49,999 rows.

queryAnsiSqlV2(input)
Query data across data model, lake, unified, and linked objects.

queryAnsiSqlV2(input, dataspace)
Query data across data model, lake, unified, and linked objects. Also, specify the data space.

nextBatchAnsiSqlV2(nextBatchId)
Get the next batch of data across data model, lake, unified, and linked objects.

nextBatchAnsiSqlV2(nextBatchId, dataspace)
Get the next batch of data across data model, lake, unified, and linked objects. Also, specify the data space.

querySql(input)
Submit an SQL query request for execution and retrieve the first chunk of data.

querySql(input, dataspace)
Submit an SQL query request for execution and specify the data space.

querySql(input, workloadName, dataspace)
Submit an SQL query request for execution and specify the workload name and data space.

querySqlRows(queryId, offset, rowLimit)
Get additional query results that weren't returned in the initial request. Paginate through existing query results by specifying the
offset and row limit. Results are available for up to 24 hours.

querySqlRows(queryId, offset, rowLimit, omitSchema)
Get additional query results that weren't returned in the initial request. Paginate through existing query results by specifying the
offset and row limit. Also, specify whether to include metadata in the response or not. Results are available for up to 24 hours.

querySqlRows(queryId, offset, rowLimit, dataspace)
Get additional query results that weren’t returned in the initial request. Paginate through existing query results by specifying the
offset and row limit. Also, specify the data space. Results are available for up to 24 hours.


Apex Reference Guide CdpQuery Class

querySqlRows(queryId, offset, rowLimit, omitSchema, dataspace)
Get additional query results that weren't returned in the initial request. Paginate through existing query results by specifying the
offset and row limit. Also, specify the data space and whether or not to exclude metadata from the response. Results are available
for up to 24 hours.

querySqlRows(queryId, offset, rowLimit, workloadName, dataspace)
Get additional query results that weren't returned in the initial request. Paginate through existing query results by specifying the
offset and row limit. Also, specify the workload name and data space. Results are available for up to 24 hours.

querySqlRows(queryId, offset, rowLimit, omitSchema, workloadName, dataspace)
Get additional query results that weren't returned in the initial request. Paginate through existing query results by specifying the
offset and row limit. Also, specify the workload name, data space, and whether or not to exclude metadata from the response. Results
are available for up to 24 hours.

cancelQuerySql(queryId)
Delete the specified query and terminate long-running queries that are no longer needed to manage resource consumption.

cancelQuerySql(queryId, dataspace)
Delete the specified query and terminate long-running queries that are no longer needed to manage resource consumption. Specify
the data space.

cancelQuerySql(queryId, workloadName, dataspace)
Delete the specified query and terminate long-running queries that are no longer needed to manage resource consumption. Specify
the data space and workload name.

querySqlStatus(queryId)
Get the status of an SQL query request. Results are available for up to 24 hours.

querySqlStatus(queryId, waitTimeMs)
Get the status of an SQL query request and specify the time to wait before returning the response. Results are available for up to 24
hours.

querySqlStatus(queryId, dataspace)
Get the status of an SQL query request and specify the data space. Results are available for up to 24 hours.

querySqlStatus(queryId, dataspace, waitTimeMs)
Get the status of an SQL query request. Specify the data space and time to wait before returning the response. Results are available
for up to 24 hours.

querySqlStatus(queryId, workloadName, dataspace)
Get the status of an SQL query request. Specify the workload name and data space. Results are available for up to 24 hours.

querySqlStatus(queryId, workloadName, dataspace, waitTimeMs)
Get the status of an SQL query request. Specify the workload name, data space, and time to wait before returning the response.
Results are available for up to 24 hours.

queryCalculatedInsights(ciName, dimensions, measures, orderby, filters, batchSize, offset)
Query a Calculated Insight object.

queryCalculatedInsights(ciName, dimensions, measures, orderby, filters, batchSize, offset, timeGranularity)
Query a Calculated Insight object within a specified time range.

queryCalculatedInsights(ciName, dimensions, measures, orderby, filters, batchSize, offset, timeGranularity, dataspace)
Query a Calculated Insight object within a specified time range and specify the data space.

queryProfileApi(dataModelName, filters, fields, batchSize, offset, orderby)
Query a Profile data model object using filters.


Apex Reference Guide CdpQuery Class

queryProfileApi(dataModelName, id, searchKey, filters, fields, batchSize, offset, orderby)
Query a Profile data model object using filters and a search key.

queryProfileApi(dataModelName, id, childDataModelName, searchKey, filters, fields, batchSize, offset, orderby)
Query a Profile data model object and a child object using filters and a search key.

queryProfileApi(dataModelName, id, ciName, searchKey, dimensions, measures, filters, fields, batchSize, offset, orderby)
Query a Profile data model object and a Calculated Insight object using filters and a search key.

queryProfileApi(dataModelName, id, ciName, searchKey, dimensions, measures, filters, fields, batchSize, offset, orderby, timeGranularity)
Query a Profile data model object and a Calculated Insight object using filters, a search key, and a time range.

queryProfileApi(dataModelName, id, ciName, searchKey, dimensions, measures, filters, fields, batchSize, offset, orderby, timeGranularity,
dataspace)
Query a Profile data model object and a Calculated Insight object using filters, a search key, a time range, and a data space.

universalIdLookupBySourceId(entityName, dataSourceId, dataSourceObjectId, sourceRecordId)
Look up objects by source ID.

universalIdLookupBySourceId(entityName, dataSourceId, dataSourceObjectId, sourceRecordId, dataspace)
Look up objects by source ID and specify the data space.

##### **`getAllMetadata()`**

Get all metadata, including Calculated Insights, Engagement, Profile, and other objects, as well as their relationships to other objects.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryMetadataOutput getAllMetadata()

```

Return Value

Type: `ConnectApi.CdpQueryMetadataOutput`

##### **`getAllMetadata(entityType, entityCategory, entityName)`**

Get all metadata, filtering for entity type, category, and name.

API Version

54.0

Requires Chatter

No


Apex Reference Guide CdpQuery Class

Signature

```
   public static ConnectApi.CdpQueryMetadataOutput getAllMetadata(String entityType, String

   entityCategory, String entityName)

```

Parameters

```
   entityType
```

Type: String

Type of metadata entity requested. Valid values are `DataLakeObject`, `DataModelObject`, and `CalculatedInsight` .
If unspecified, all types are returned.

```
   entityCategory
```

Type: String

Category of the metadata entity. Valid values are `Profile`, `Engagement`, and `Related` . If unspecified, all category entities
are returned.

```
   entityName
```

Type: String

Metadata name of the entity, for example `UnifiedIndividual__dlm` . If unspecified, a complete list of entities is returned.

Return Value

Type: `ConnectApi.CdpQueryMetadataOutput`

##### **`getAllMetadata(entityType, entityCategory, entityName, dataspace)`**

Get all metadata, filtering for entity type, category, name, and data space.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryMetadataOutput getAllMetadata(String entityType, String

   entityCategory, String entityName, String dataspace)

```

Parameters

```
   entityType
```

Type: String

Type of metadata entity requested. Valid values are `DataLakeObject`, `DataModelObject`, and `CalculatedInsight` .
If unspecified, all types are returned.

```
   entityCategory
```

Type: String


Apex Reference Guide CdpQuery Class

Category of the metadata entity. Valid values are `Profile`, `Engagement`, and `Related` . If unspecified, all category entities
are returned.

```
   entityName
```

Type: String

Metadata name of the entity, for example `UnifiedIndividual__dlm` . If unspecified, a complete list of entities is returned.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.CdpQueryMetadataOutput`

##### **`getDataGraphData(dataGraphEntityName, id)`**

Query a data graph in the default data space. For real-time data graphs, the method attempts to retrieve data from the real-time data
graph but falls back to the standard data graph if the real-time data graph is unavailable.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput getDataGraphData(String dataGraphEntityName,

   String id)

```

Parameters

```
   dataGraphEntityName
```

Type: String

API name of the data graph to query.

```
   id
```

Type: String

Record ID to query for. The ID is matched against the primary key field of the primary Data Model Object (DMO) in the data graph.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`getDataGraphData(dataGraphEntityName, id, dataspace)`**

Query a data graph in a specified data space. For real-time data graphs, the method attempts to retrieve data from the real-time data
graph but falls back to the standard data graph if the real-time data graph is unavailable.


Apex Reference Guide CdpQuery Class

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput getDataGraphData(String dataGraphEntityName,

   String id, String dataspace)

```

Parameters

```
   dataGraphEntityName
```

Type: String

API name of the data graph to query.

```
   id
```

Type: String

Record ID to query for. The ID is matched against the primary key field of the primary Data Model Object (DMO) in the data graph.

```
   dataspace
```

Type: String

Name of the data space in which to query the data graph.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`getDataGraphData(dataGraphEntityName, id, live)`**

Query a data graph by performing a live lookup in the default data space. For real-time data graphs, the method attempts to retrieve
data from the real-time data graph but falls back to the standard data graph if the real-time data graph is unavailable.

API Version

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput getDataGraphData(String dataGraphEntityName,

   String id, Boolean live)

```


Apex Reference Guide CdpQuery Class

Parameters

```
   dataGraphEntityName
```

Type: String

API name of the data graph to query.

```
   id
```

Type: String

Record ID to query for. The ID is matched against the primary key field of the primary Data Model Object (DMO) in the data graph.

```
   live
```

Type: Boolean

Indicates whether live lookup for the data graph is enabled ( `true` ) or not ( `false` ). With live lookup, the Query Service does not
query the data graph itself. It instead queries the data graph's metadata to return data that is guaranteed to be fresh. The response
mimics the structure of the regular JSON-formatted response for the data graph. You can use live lookup on any data graph, regardless
of the complexity of its structure.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`getDataGraphData(dataGraphEntityName, id, dataspace, live)`**

Query a data graph by performing a live lookup in a specified data space. For real-time data graphs, the method attempts to retrieve
data from the real-time data graph but falls back to the standard data graph if the real-time data graph is unavailable.

API Version

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput getDataGraphData(String dataGraphEntityName,

   String id, String dataspace, Boolean live)

```

Parameters

```
   dataGraphEntityName
```

Type: String

API name of the data graph to query.

```
   id
```

Type: String

Record ID to query for. The ID is matched against the primary key field of the primary Data Model Object (DMO) in the data graph.

```
   dataspace
```

Type: String


Apex Reference Guide CdpQuery Class

Name of the data space in which to query the data graph.

```
   live
```

Type: Boolean

Indicates whether live lookup for the data graph is enabled ( `true` ) or not ( `false` ). With live lookup, the Query Service does not
query the data graph itself. It instead queries the data graph's metadata to return data that is guaranteed to be fresh. The response
mimics the structure of the regular JSON-formatted response for the data graph. You can use live lookup on any data graph, regardless
of the complexity of its structure.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`getDataGraphDataWithLookupKeys(dataGraphEntityName, lookupKeys)`**

Query a data graph by the primary key of either the primary Data Model Object (DMO) or the Individual linked DMO. Get the data from
the default data space. For real-time data graphs, the method attempts to retrieve data from the real-time data graph but falls back to
the standard data graph if the real-time data graph is unavailable.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput getDataGraphDataWithLookupKeys(String

   dataGraphEntityName, String lookupKeys)

```

Parameters

```
   dataGraphEntityName
```

Type: String

API name of the data graph to query.

```
   lookupKeys
```

Type: String

Lookup key and value to search on. Specify one of these key-value pairs:

**•** The primary key of the primary DMO, for example, `lookupKeys=[id__c=def]`

**•** The primary key of the Individual linked DMO, for example,

```
      lookupKeys=[IndividualLink__dlm.SourceRecordId__c=1111111]

```

Return Value

Type: `ConnectApi.CdpQueryOutput`


Apex Reference Guide CdpQuery Class

##### **`getDataGraphDataWithLookupKeys(dataGraphEntityName, lookupKeys, dataspace)`**

Query a data graph by the primary key of either the primary Data Model Object (DMO) or the Individual linked DMO. Get the data from
a specified data space. For real-time data graphs, the method attempts to retrieve data from the real-time data graph but falls back to
the standard data graph if the real-time data graph is unavailable.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput getDataGraphDataWithLookupKeys(String

   dataGraphEntityName, String lookupKeys, String dataspace)

```

Parameters

```
   dataGraphEntityName
```

Type: String

API name of the data graph to query.

```
   lookupKeys
```

Type: String

Lookup key and value to search on. Specify one of these key-value pairs:

**•** The primary key of the primary DMO, for example, `lookupKeys=[id__c=def]`

**•** The primary key of the Individual linked DMO, for example,

```
      lookupKeys=[IndividualLink__dlm.SourceRecordId__c=1111111]

   dataspace
```

Type: String

Name of the data space in which to query the data graph.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`getDataGraphDataWithLookupKeys(dataGraphEntityName, lookupKeys, dataspace,`**

```
  noCache)

```

Query a data graph by the primary key of either the primary Data Model Object (DMO) or the Individual linked DMO. Get the data from
a specified data space. Get data from a standard or real-time data graph. For real-time data graphs, the method attempts to retrieve data
from the real-time data graph but falls back to the standard data graph if the real-time data graph is unavailable.

API Version

64.0


Apex Reference Guide CdpQuery Class

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput getDataGraphDataWithLookupKeys(String

   dataGraphEntityName, String lookupKeys, String dataspace, Boolean noCache)

```

Parameters

```
   dataGraphEntityName
```

Type: String

API name of the data graph to query.

```
   lookupKeys
```

Type: String

Lookup key and value to search on. Specify one of these key-value pairs:

**•** The primary key of the primary DMO, for example, `lookupKeys=[id__c=def]`

**•** The primary key of the Individual linked DMO, for example,

```
      lookupKeys=[IndividualLink__dlm.SourceRecordId__c=1111111]

   dataspace
```

Type: String

Name of the data space in which to query the data graph.

```
   noCache
```

Type: Boolean

Indicates whether to read data from the standard, non-real-time data graph ( `true` ) or the real-time data graph ( `false` ).

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`getDataGraphMetadata()`**

Retrieve metadata from all data graphs in the default data space. Retrieves data from both standard and real-time data graphs.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpDgMetadata getDataGraphMetadata()

```


Apex Reference Guide CdpQuery Class

Return Value

Type: `ConnectApi.CdpDgMetadata`

##### **`getDataGraphMetadata(dataGraphEntityName)`**

Retrieve metadata from a specified data graph in the default data space. Retrieves data from both standard and real-time data graphs.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpDgMetadata getDataGraphMetadata(String dataGraphEntityName)

```

Parameters

```
   dataGraphEntityName
```

Type: String

API name of the data graph to query.

Return Value

Type: `ConnectApi.CdpDgMetadata`

##### **`getDataGraphMetadata(dataGraphEntityName, dataspace)`**

Retrieve metadata from a specified data graph in a specified data space. Retrieves data from both standard and real-time data graphs.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpDgMetadata getDataGraphMetadata(String dataGraphEntityName,

   String dataspace)

```

Parameters

```
   dataGraphEntityName
```

Type: String


Apex Reference Guide CdpQuery Class

API name of the data graph to query.

```
   dataspace
```

Type: String

Name of the data space in which to query the data graph.

Return Value

Type: `ConnectApi.CdpDgMetadata`

##### **`getInsightsMetadata()`**

Get Insight metadata, including Calculated Insight objects, their dimensions and measures.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryMetadataOutput getInsightsMetadata()

```

Return Value

Type: `ConnectApi.CdpQueryMetadataOutput`

##### **`getInsightsMetadata(ciName)`**

Get metadata for a Calculated Insight object. Metadata includes dimensions and measures.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryMetadataOutput getInsightsMetadata(String ciName)

```

Parameters

```
   ciName
```

Type: String

Name of the Calculated Insight object, for example, `IndividualChildrenCount__cio` .


Apex Reference Guide CdpQuery Class

Return Value

Type: `ConnectApi.CdpQueryMetadataOutput`

##### **`getInsightsMetadata(ciName, dataspace)`**

Get metadata for a Calculated Insight object and specify the data space. Metadata includes dimensions and measures.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryMetadataOutput getInsightsMetadata(String ciName,

   String dataspace)

```

Parameters

```
   ciName
```

Type: String

Name of the Calculated Insight object, for example, `IndividualChildrenCount__cio` .

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.CdpQueryMetadataOutput`

##### **`getProfileMetadata()`**

Get metadata for data model objects in the profile category, including Individual, Contact Point Email, Unified Individual, and Contact
Point Address objects. Metadata includes the objects, their fields, and category.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryMetadataOutput getProfileMetadata()

```


Apex Reference Guide CdpQuery Class

Return Value

Type: `ConnectApi.CdpQueryMetadataOutput`

##### **`getProfileMetadata(dataModelName)`**

Get metadata for a data model object in the profile category, such as Individual, Contact Point Email, Unified Individual, and Contact
Point Address. Metadata includes the list of fields, data types, and indexes available for lookup.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryMetadataOutput getProfileMetadata(String dataModelName)

```

Parameters

```
   dataModelName
```

Type: String

Name of the data model object, for example, `UnifiedIndividual__dlm` .

Return Value

Type: `ConnectApi.CdpQueryMetadataOutput`

##### **`getProfileMetadata(dataModelName, dataspace)`**

Get metadata for a data model object in the profile category, such as Individual, Contact Point Email, Unified Individual, and Contact
Point Address. Also, specify the data space. Metadata includes the list of fields, data types, and indexes available for lookup.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryMetadataOutput getProfileMetadata(String dataModelName,

   String dataspace)

```


Apex Reference Guide CdpQuery Class

Parameters

```
   dataModelName
```

Type: String

Name of the data model object, for example, `UnifiedIndividual__dlm` .

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.CdpQueryMetadataOutput`

##### **`queryANSISql(input)`**

Synchronously query data across data model, lake, unified, and linked objects. This query returns up to 49,999 rows.

Note: A newer version of the Query API is available. We recommend using `queryAnsiSqlV2(input)` and
`nextBatchAnsiSqlV2(nextBatchId)` to take advantage of subsequent requests and larger response sizes.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput queryANSISql(ConnectApi.CdpQueryInput input)

```

Parameters

```
   input
```

Type: `ConnectApi.CdpQueryInput`

A `ConnectApi.CdpQueryInput` body with the SQL query.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`queryANSISql(input, batchSize, offset, orderby)`**

Synchronously query data across data model, lake, unified, and linked objects. Specify batch size, offset, and order of the results. This
query returns up to 49,999 rows.

Note: A newer version of the Query API is available. We recommend using `queryAnsiSqlV2(input)` and
`nextBatchAnsiSqlV2(nextBatchId)` to take advantage of subsequent requests and larger response sizes.


Apex Reference Guide CdpQuery Class

API Version

53.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput queryANSISql(ConnectApi.CdpQueryInput input,

   Integer batchSize, Integer offset, String orderby)

```

Parameters

```
   input
```

Type: `ConnectApi.CdpQueryInput`

A `ConnectApi.CdpQueryInput` body with the SQL query.

```
   batchSize
```

Type: Integer

Number of records to return. Values are from `1`      - `49999` . The default value is `49999` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. The sum of _`offset`_ and _`batchSize`_ must be less than `2147483647` . The
default value is `0` .

```
   orderby
```

Type: String

Comma-separated values to sort the results in ascending or descending order, for example, `GenderId__c`
`ASC,Occupation__c DESC` .

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`queryANSISql(input, batchSize, offset, orderby, dataspace)`**

Synchronously query data across data model, lake, unified, and linked objects. Specify batch size, offset, order of the results, and data
space. This query returns up to 49,999 rows.

Note: A newer version of the Query API is available. We recommend using `queryAnsiSqlV2(input)` and
`nextBatchAnsiSqlV2(nextBatchId)` to take advantage of subsequent requests and larger response sizes.

API Version

57.0

Requires Chatter

No


Apex Reference Guide CdpQuery Class

Signature

```
   public static ConnectApi.CdpQueryOutput queryANSISql(ConnectApi.CdpQueryInput input,

   Integer batchSize, Integer offset, String orderby, String dataspace)

```

Parameters

```
   input
```

Type: `ConnectApi.CdpQueryInput`

A `ConnectApi.CdpQueryInput` body with the SQL query.

```
   batchSize
```

Type: Integer

Number of records to return. Values are from `1`      - `49999` . The default value is `49999` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. The sum of _`offset`_ and _`batchSize`_ must be less than `2147483647` . The
default value is `0` .

```
   orderby
```

Type: String

Comma-separated values to sort the results in ascending or descending order, for example, `GenderId__c`
`ASC,Occupation__c DESC` .

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`queryAnsiSqlV2(input)`**

Query data across data model, lake, unified, and linked objects.

API Version

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutputV2 queryAnsiSqlV2(ConnectApi.CdpQueryInput input)

```


Apex Reference Guide CdpQuery Class

Parameters

```
   input
```

Type: `ConnectApi.CdpQueryInput`

A `ConnectApi.CdpQueryInput` body with the SQL query.

Return Value

Type: `ConnectApi.CdpQueryOutputV2`

Usage

Use the `nextBatchId` in the `ConnectApi.CdpQueryOutputV2` output class as the _`nextBatchId`_ parameter in the

`nextBatchAnsiSqlV2(nextBatchId)` method to continue getting batches of data for up to an hour.

##### **`queryAnsiSqlV2(input, dataspace)`**

Query data across data model, lake, unified, and linked objects. Also, specify the data space.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutputV2 queryAnsiSqlV2(ConnectApi.CdpQueryInput input,

   String dataspace)

```

Parameters

```
   input
```

Type: `ConnectApi.CdpQueryInput`

A `ConnectApi.CdpQueryInput` body with the SQL query.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.CdpQueryOutputV2`

Usage

Use the `nextBatchId` in the `ConnectApi.CdpQueryOutputV2` output class as the _`nextBatchId`_ parameter in the

`nextBatchAnsiSqlV2(nextBatchId)` method to continue getting batches of data for up to an hour.


Apex Reference Guide CdpQuery Class

##### **`nextBatchAnsiSqlV2(nextBatchId)`**

Get the next batch of data across data model, lake, unified, and linked objects.

API Version

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutputV2 nextBatchAnsiSqlV2(String nextBatchId)

```

Parameters

```
   nextBatchId
```

Type: String

ID of the next batch. See the Usage section for more information.

Return Value

Type: `ConnectApi.CdpQueryOutputV2`

Usage

Initially, use the `queryAnsiSqlV2(input)` method to query up to 8 MB of data. Use the `nextBatchId` from the
`ConnectApi.CdpQueryOutputV2` output class as the _`nextBatchId`_ parameter in this method to get the next batch of
data. You can continue using subsequent next batch IDs for up to an hour.

##### **`nextBatchAnsiSqlV2(nextBatchId, dataspace)`**

Get the next batch of data across data model, lake, unified, and linked objects. Also, specify the data space.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutputV2 nextBatchAnsiSqlV2(String nextBatchId, String

   dataspace)

```


Apex Reference Guide CdpQuery Class

Parameters

```
   nextBatchId
```

Type: String

ID of the next batch. See the Usage section for more information.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.CdpQueryOutputV2`

Usage

Initially, use the `queryAnsiSqlV2(input)` method to query up to 8 MB of data. Use the `nextBatchId` from the
`ConnectApi.CdpQueryOutputV2` output class as the _`nextBatchId`_ parameter in this method to get the next batch of
data. You can continue using subsequent next batch IDs for up to an hour.

##### **`querySql(input)`**

Submit an SQL query request for execution and retrieve the first chunk of data.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlOutput querySql(ConnectApi.QuerySqlInput input)

```

Parameters

```
   input
```

Type: `ConnectApi.QuerySqlInput`

Input representation for an SQL query.

Return Value

Type: `ConnectApi.QuerySqlOutput`

Usage

[To get started with writing queries, see Write a Simple Query. For more information about creating SQL statements, see Data 360 SQL](https://developer.salesforce.com/docs/data/data-cloud-query-guide/guide/write-simple-query.html)
[Syntax.](https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/dc-sql-reference/syntax.html)


Apex Reference Guide CdpQuery Class

Example

Submit a query, check its status, then retrieve and process data in chunks until all results are fetched:

```
   ConnectApi.QuerySqlInput query = new ConnectApi.QuerySqlInput();

   query.sql = 'SELECT street_address__c FROM test__dll limit 200000';

   Integer numProcessed = 0;

   Long startTime = System.currentTimeMillis();

   System.debug('Query execution started at: ' + startTime);

   ConnectApi.QuerySqlOutput queryOutput = ConnectApi.CdpQuery.querySql(query,

   'sample_workload', 'default');

   ConnectApi.QuerySqlStatus status = queryOutput.status;

   // Process chunks as they become available

   while(status.completionStatus != ConnectApi.QuerySqlStatusEnum.FINISHED || numProcessed <

    status.rowCount) {

      // If we have unprocessed rows available, fetch and process them

      if (status.rowCount > numProcessed) {

        ConnectApi.QuerySqlPageOutput pageOutput =

   ConnectApi.CdpQuery.querySqlRows(status.queryId, numProcessed, 10000, 'sample_workload',

   'default');

        // Process this chunk - inline max length calculation

        Integer maxLength = 0;

        for (ConnectApi.QuerySqlRow rowObj : pageOutput.dataRows) {

           String streetAddress = (String) rowObj.row[0];

           if (streetAddress.length() > maxLength) {

             maxLength = streetAddress.length();

           }

        }

        System.debug('Chunk - Rows: ' + pageOutput.dataRows.size() + ', Max street_address

    length: ' + maxLength);

        numProcessed += pageOutput.dataRows.size();

      } else if (status.completionStatus != ConnectApi.QuerySqlStatusEnum.FINISHED) {

        // No new rows available yet, wait a bit before checking status again

        System.debug('Query in progress. Total rows available: ' + status.rowCount + ',

   Processed: ' + numProcessed);

        // Small delay to avoid excessive polling (adjust as needed)

        // Note: In Apex, we can't use Thread.sleep(), so we'll just continue to next

   iteration

      }

      // Update status if query is still running

      if (status.completionStatus != ConnectApi.QuerySqlStatusEnum.FINISHED) {

        status = ConnectApi.CdpQuery.querySqlStatus(status.queryId, 'sample_workload',

   'default');

      }

   }

```


Apex Reference Guide CdpQuery Class

```
   Long completionTime = System.currentTimeMillis();

   System.debug('Query and processing completed at: ' + completionTime + ', Total time: ' +

   (completionTime - startTime) + ' ms');

   System.debug('Total rows processed: ' + numProcessed + ' out of ' + status.rowCount + '

   total rows');

##### **`querySql(input, dataspace)`**

```

Submit an SQL query request for execution and specify the data space.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlOutput querySql(ConnectApi.QuerySqlInput input, String

   dataspace)

```

Parameters

```
   input
```

Type: `ConnectApi.QuerySqlInput`

Input representation for an SQL query.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.QuerySqlOutput`

Usage

[To get started with writing queries, see Write a Simple Query. For more information about creating SQL statements, see Data 360 SQL](https://developer.salesforce.com/docs/data/data-cloud-query-guide/guide/write-simple-query.html)
[Syntax.](https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/dc-sql-reference/syntax.html)

Example

Submit a query with a data space:

```
   ConnectApi.QuerySqlInput input = new ConnectApi.QuerySqlInput();

   input.sql = 'select * from "passenger2__dll"';

   ConnectApi.QuerySqlOutput output = ConnectApi.CdpQuery.querySql(input, 'default');

   System.debug(output);

```


Apex Reference Guide CdpQuery Class

```
   System.debug(output.dataRows);

   System.debug(output.metadata);

   System.debug(output.status);

   System.debug(output.returnedRows);

##### **`querySql(input, workloadName, dataspace)`**

```

Submit an SQL query request for execution and specify the workload name and data space.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlOutput querySql(ConnectApi.QuerySqlInput input, String

   workloadName, String dataspace)

```

Parameters

```
   input
```

Type: `ConnectApi.QuerySqlInput`

Input representation for an SQL query.

```
   workloadName
```

Type: String

Description of the scenario, task, or application name that your query handles. Set this value to help Salesforce Customer Support
assist you with debugging issues.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.QuerySqlOutput`

Usage

[To get started with writing queries, see Write a Simple Query. For more information about creating SQL statements, see Data 360 SQL](https://developer.salesforce.com/docs/data/data-cloud-query-guide/guide/write-simple-query.html)
[Syntax.](https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/dc-sql-reference/syntax.html)


Apex Reference Guide CdpQuery Class

Example

Submit a query with a data space and workload name:

```
   ConnectApi.QuerySqlInput input = new ConnectApi.QuerySqlInput();

   input.sql = 'select * from "passenger2__dll"';

   ConnectApi.QuerySqlOutput output = ConnectApi.CdpQuery.querySql(input, 'workloadName',

   'default');

   System.debug(output);

   System.debug(output.dataRows);

   System.debug(output.metadata);

   System.debug(output.status);

   System.debug(output.returnedRows);

##### **`querySqlRows(queryId, offset, rowLimit)`**

```

Get additional query results that weren't returned in the initial request. Paginate through existing query results by specifying the offset
and row limit. Results are available for up to 24 hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlPageOutput querySqlRows(String queryId, Long offset,

   Long rowLimit)

```

Parameters

```
   queryId
```

Type: String

ID from the initial query to retrieve more results, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

```
   offset
```

Type: Long

Row number to start with when retrieving the next chunk of query results. Value must be less than the total number of available
rows. If unspecified, no rows are skipped.

```
   rowLimit
```

Type: Long

Maximum number of rows to include in the response. The actual number of rows returned may be lower than the requested value
if fewer are available or if the result set exceeds internal system size limits. Value must be greater than `0` .


Apex Reference Guide CdpQuery Class

Return Value

Type: `ConnectApi.QuerySqlPageOutput`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Query additional rows with an offset and row limit:

```
   ConnectApi.QuerySqlPageOutput pageOutput =

   ConnectApi.CdpQuery.querySqlRows(output.status.queryId, 100, 200);

   System.debug(pageOutput);

   System.debug(pageOutput.dataRows);

   System.debug(pageOutput.metadata);

   System.debug(pageOutput.returnedRows);

##### **`querySqlRows(queryId, offset, rowLimit, omitSchema)`**

```

Get additional query results that weren't returned in the initial request. Paginate through existing query results by specifying the offset
and row limit. Also, specify whether to include metadata in the response or not. Results are available for up to 24 hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlPageOutput querySqlRows(String queryId, Long offset,

   Long rowLimit, Boolean omitSchema)

```

Parameters

```
   queryId
```

Type: String

ID from the initial query to retrieve more results, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

```
   offset
```

Type: Long

Row number to start with when retrieving the next chunk of query results. Value must be less than the total number of available
rows. If unspecified, no rows are skipped.


Apex Reference Guide CdpQuery Class

```
   rowLimit
```

Type: Long

Maximum number of rows to include in the response. The actual number of rows returned may be lower than the requested value
if fewer are available or if the result set exceeds internal system size limits. Value must be greater than `0` .

```
   omitSchema
```

Type: Boolean

Indicates whether to exclude metadata from the response ( `true` ) or not ( `false` ). Omitting the schema reduces the amount of
data returned and improves performance.

Return Value

Type: `ConnectApi.QuerySqlPageOutput`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Query additional rows with an offset, a row limit, and omitting the schema:

```
   ConnectApi.QuerySqlPageOutput pageOutput =

   ConnectApi.CdpQuery.querySqlRows(output.status.queryId, 100, 200, true);

   System.debug(pageOutput);

   System.debug(pageOutput.dataRows);

   System.debug(pageOutput.metadata);

   System.debug(pageOutput.returnedRows);

##### **`querySqlRows(queryId, offset, rowLimit, dataspace)`**

```

Get additional query results that weren’t returned in the initial request. Paginate through existing query results by specifying the offset
and row limit. Also, specify the data space. Results are available for up to 24 hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlPageOutput querySqlRows(String queryId, Long offset,

   Long rowLimit, String dataspace)

```


Apex Reference Guide CdpQuery Class

Parameters

```
   queryId
```

Type: String

ID from the initial query to retrieve more results, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

```
   offset
```

Type: Long

Row number to start with when retrieving the next chunk of query results. Value must be less than the total number of available
rows. If unspecified, no rows are skipped.

```
   rowLimit
```

Type: Long

Maximum number of rows to include in the response. The actual number of rows returned may be lower than the requested value
if fewer are available or if the result set exceeds internal system size limits. Value must be greater than `0` .

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.QuerySqlPageOutput`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Query additional rows with an offset, row limit, and data space:

```
   ConnectApi.QuerySqlPageOutput pageOutput =

   ConnectApi.CdpQuery.querySqlRows(output.status.queryId, 100, 200, 'default');

   System.debug(pageOutput);

   System.debug(pageOutput.dataRows);

   System.debug(pageOutput.metadata);

   System.debug(pageOutput.returnedRows);

##### **`querySqlRows(queryId, offset, rowLimit, omitSchema, dataspace)`**

```

Get additional query results that weren't returned in the initial request. Paginate through existing query results by specifying the offset
and row limit. Also, specify the data space and whether or not to exclude metadata from the response. Results are available for up to 24
hours.

API Version

62.0


Apex Reference Guide CdpQuery Class

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlPageOutput querySqlRows(String queryId, Long offset,

   Long rowLimit, Boolean omitSchema, String dataspace)

```

Parameters

```
   queryId
```

Type: String

ID from the initial query to retrieve more results, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
`querySql` response.

```
   offset
```

Type: Long

Row number to start with when retrieving the next chunk of query results. Value must be less than the total number of available
rows. If unspecified, no rows are skipped.

```
   rowLimit
```

Type: Long

Maximum number of rows to include in the response. The actual number of rows returned may be lower than the requested value
if fewer are available or if the result set exceeds internal system size limits. Value must be greater than `0` .

```
   omitSchema
```

Type: Boolean

Indicates whether to exclude metadata from the response ( `true` ) or not ( `false` ). Omitting the schema reduces the amount of
data returned and improves performance.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.QuerySqlPageOutput`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Query additional rows with an offset, row limit, data space, and omitting the schema:

```
   ConnectApi.QuerySqlPageOutput pageOutput =

   ConnectApi.CdpQuery.querySqlRows(output.status.queryId, 100, 200, true, 'default');

   System.debug(pageOutput);

```


Apex Reference Guide CdpQuery Class

```
   System.debug(pageOutput.dataRows);

   System.debug(pageOutput.metadata);

   System.debug(pageOutput.returnedRows);

##### **`querySqlRows(queryId, offset, rowLimit, workloadName, dataspace)`**

```

Get additional query results that weren't returned in the initial request. Paginate through existing query results by specifying the offset
and row limit. Also, specify the workload name and data space. Results are available for up to 24 hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlPageOutput querySqlRows(String queryId, Long offset,

   Long rowLimit, String workloadName, String dataspace)

```

Parameters

```
   queryId
```

Type: String

ID from the initial query to retrieve more results, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

```
   offset
```

Type: Long

Row number to start with when retrieving the next chunk of query results. Value must be less than the total number of available
rows. If unspecified, no rows are skipped.

```
   rowLimit
```

Type: Long

Maximum number of rows to include in the response. The actual number of rows returned may be lower than the requested value
if fewer are available or if the result set exceeds internal system size limits. Value must be greater than `0` .

```
   workloadName
```

Type: String

Description of the scenario, task, or application name that your query handles. Set this value to help Salesforce Customer Support
assist you with debugging issues.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.


Apex Reference Guide CdpQuery Class

Return Value

Type: `ConnectApi.QuerySqlPageOutput`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Query additional rows with an offset, row limit, workload name, and data space:

```
   ConnectApi.QuerySqlPageOutput pageOutput =

   ConnectApi.CdpQuery.querySqlRows(output.status.queryId, 100, 200, 'workloadName', 'default');

   System.debug(pageOutput);

   System.debug(pageOutput.dataRows);

   System.debug(pageOutput.metadata);

   System.debug(pageOutput.returnedRows);

##### **`querySqlRows(queryId, offset, rowLimit, omitSchema, workloadName, dataspace)`**

```

Get additional query results that weren't returned in the initial request. Paginate through existing query results by specifying the offset
and row limit. Also, specify the workload name, data space, and whether or not to exclude metadata from the response. Results are
available for up to 24 hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlPageOutput querySqlRows(String queryId, Long offset,

   Long rowLimit, Boolean omitSchema, String workloadName, String dataspace)

```

Parameters

```
   queryId
```

Type: String

ID from the initial query to retrieve more results, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

```
   offset
```

Type: Long

Row number to start with when retrieving the next chunk of query results. Value must be less than the total number of available
rows. If unspecified, no rows are skipped.


Apex Reference Guide CdpQuery Class

```
   rowLimit
```

Type: Long

Maximum number of rows to include in the response. The actual number of rows returned may be lower than the requested value
if fewer are available or if the result set exceeds internal system size limits. Value must be greater than `0` .

```
   omitSchema
```

Type: Boolean

Indicates whether to exclude metadata from the response ( `true` ) or not ( `false` ). Omitting the schema reduces the amount of
data returned and improves performance.

```
   workloadName
```

Type: String

Description of the scenario, task, or application name that your query handles. Set this value to help Salesforce Customer Support
assist you with debugging issues.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.QuerySqlPageOutput`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Query additional rows with an offset, row limit, workload name, data space, and omitting the schema:

```
   ConnectApi.QuerySqlPageOutput pageOutput =

   ConnectApi.CdpQuery.querySqlRows(output.status.queryId, 100, 200, true, 'workloadName',

   'default');

   System.debug(pageOutput);

   System.debug(pageOutput.dataRows);

   System.debug(pageOutput.metadata);

   System.debug(pageOutput.returnedRows);

##### **`cancelQuerySql(queryId)`**

```

Delete the specified query and terminate long-running queries that are no longer needed to manage resource consumption.

API Version

62.0

Requires Chatter

No


Apex Reference Guide CdpQuery Class

Signature

```
   public static Void cancelQuerySql(String queryId)

```

Parameters

```
   queryId
```

Type: String

ID of the query to cancel, for example `MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` .
The query ID is returned in the `querySql` response.

Return Value

Type: Void

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Cancel a query:

```
   ConnectApi.CdpQuery.cancelQuerySql(output.status.queryId);

   System.debug('done');

##### **`cancelQuerySql(queryId, dataspace)`**

```

Delete the specified query and terminate long-running queries that are no longer needed to manage resource consumption. Specify
the data space.

API Version

62.0

Requires Chatter

No

Signature

```
   public static Void cancelQuerySql(String queryId, String dataspace)

```

Parameters

```
   queryId
```

Type: String

ID of the query to cancel, for example `MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` .
The query ID is returned in the `querySql` response.


Apex Reference Guide CdpQuery Class

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: Void

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Cancel a query with a data space:

```
   ConnectApi.CdpQuery.cancelQuerySql(output.status.queryId, 'default');

   System.debug('done');

##### **`cancelQuerySql(queryId, workloadName, dataspace)`**

```

Delete the specified query and terminate long-running queries that are no longer needed to manage resource consumption. Specify
the data space and workload name.

API Version

62.0

Requires Chatter

No

Signature

```
   public static Void cancelQuerySql(String queryId, String workloadName, String dataspace)

```

Parameters

```
   queryId
```

Type: String

ID of the query to cancel, for example `MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` .
The query ID is returned in the `querySql` response.

```
   workloadName
```

Type: String

Description of the scenario, task, or application name that your query handles. Set this value to help Salesforce Customer Support
assist you with debugging issues.

```
   dataspace
```

Type: String


Apex Reference Guide CdpQuery Class

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: Void

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Cancel a query with a workload name and data space:

```
   ConnectApi.CdpQuery.cancelQuerySql(output.status.queryId, 'workloadName', 'default');

   System.debug('done');

##### **`querySqlStatus(queryId)`**

```

Get the status of an SQL query request. Results are available for up to 24 hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlStatus querySqlStatus(String queryId)

```

Parameters

```
   queryId
```

Type: String

ID of the query to return the status for, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

Return Value

Type: `ConnectApi.QuerySqlStatus`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .


Apex Reference Guide CdpQuery Class

Example

Get the status of a query:

```
   ConnectApi.QuerySqlStatus statusOutput =

   ConnectApi.CdpQuery.querySqlStatus(output.status.queryId);

   System.debug(statusOutput);

##### **`querySqlStatus(queryId, waitTimeMs)`**

```

Get the status of an SQL query request and specify the time to wait before returning the response. Results are available for up to 24
hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlStatus querySqlStatus(String queryId, Integer

   waitTimeMs)

```

Parameters

```
   queryId
```

Type: String

ID of the query to return the status for, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

```
   waitTimeMs
```

Type: Integer

Maximum time (in milliseconds) to wait for the result. Configure a wait time up to 10 seconds before returning the status without
chunk information. If unspecified, the status is returned immediately. Use this to avoid resource limits by delaying requests.

Return Value

Type: `ConnectApi.QuerySqlStatus`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .


Apex Reference Guide CdpQuery Class

Example

Get the status of a query with wait time:

```
   ConnectApi.QuerySqlStatus statusOutput =

   ConnectApi.CdpQuery.querySqlStatus(output.status.queryId, 55);

   System.debug(statusOutput);

##### **`querySqlStatus(queryId, dataspace)`**

```

Get the status of an SQL query request and specify the data space. Results are available for up to 24 hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlStatus querySqlStatus(String queryId, String dataspace)

```

Parameters

```
   queryId
```

Type: String

ID of the query to return the status for, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.QuerySqlStatus`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Get the status of a query with a data space:

```
   ConnectApi.QuerySqlStatus statusOutput =

   ConnectApi.CdpQuery.querySqlStatus(output.status.queryId, 'default');

   System.debug(statusOutput);

```


Apex Reference Guide CdpQuery Class

##### **`querySqlStatus(queryId, dataspace, waitTimeMs)`**

Get the status of an SQL query request. Specify the data space and time to wait before returning the response. Results are available for
up to 24 hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlStatus querySqlStatus(String queryId, String dataspace,

   Integer waitTimeMs)

```

Parameters

```
   queryId
```

Type: String

ID of the query to return the status for, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

```
   waitTimeMs
```

Type: Integer

Maximum time (in milliseconds) to wait for the result. Configure a wait time up to 10 seconds before returning the status. If unspecified,
the status is returned immediately. Use this to avoid resource limits by delaying requests.

Return Value

Type: `ConnectApi.QuerySqlStatus`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Get the status of a query with a data space and wait time:

```
   ConnectApi.QuerySqlStatus statusOutput =

   ConnectApi.CdpQuery.querySqlStatus(output.status.queryId, 'default', 100);

   System.debug(statusOutput);

```


Apex Reference Guide CdpQuery Class

##### **`querySqlStatus(queryId, workloadName, dataspace)`**

Get the status of an SQL query request. Specify the workload name and data space. Results are available for up to 24 hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlStatus querySqlStatus(String queryId, String

   workloadName, String dataspace)

```

Parameters

```
   queryId
```

Type: String

ID of the query to return the status for, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

```
   workloadName
```

Type: String

Description of the scenario, task, or application name that your query handles. Set this value to help Salesforce Customer Support
assist you with debugging issues.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.QuerySqlStatus`

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Get the status of a query with a workload name and data space:

```
   ConnectApi.QuerySqlInput input = new ConnectApi.QuerySqlInput();

   input.sql = 'select * from "passenger2__dll"';

   ConnectApi.QuerySqlOutput output = ConnectApi.CdpQuery.querySql(input);

   System.debug(output);

```


Apex Reference Guide CdpQuery Class

```
   ConnectApi.QuerySqlStatus statusOutput =

   ConnectApi.CdpQuery.querySqlStatus(output.status.queryId, 'workloadName', 'default');

   System.debug(statusOutput);

##### **`querySqlStatus(queryId, workloadName, dataspace, waitTimeMs)`**

```

Get the status of an SQL query request. Specify the workload name, data space, and time to wait before returning the response. Results
are available for up to 24 hours.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.QuerySqlStatus querySqlStatus(String queryId, String

   workloadName, String dataspace, Integer waitTimeMs)

```

Parameters

```
   queryId
```

Type: String

ID of the query to return the status for, for example
`MTAuMjMuMTU2LjIwODo3NDg0_49169cf8-a6f4-738f-6544-c3a7ba2ff548` . The query ID is returned in the
##### querySql response.

```
   workloadName
```

Type: String

Description of the scenario, task, or application name that your query handles. Set this value to help Salesforce Customer Support
assist you with debugging issues.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

```
   waitTimeMs
```

Type: Integer

Maximum time (in milliseconds) to wait for the result. Configure a wait time up to 10 seconds before returning the status . If unspecified,
the status is returned immediately. Use this to avoid resource limits by delaying requests.

Return Value

Type: `ConnectApi.QuerySqlStatus`


Apex Reference Guide CdpQuery Class

Usage

Retrieve the _`queryId`_ from the initial query request. To submit an SQL query request for execution, call `querySql(input)`,

`querySql(input, dataspace)`, or `querySql(input, workloadName, dataspace)` .

Example

Get the status of a query with a workload name, data space, and wait time:

```
   ConnectApi.QuerySqlStatus statusOutput =

   ConnectApi.CdpQuery.querySqlStatus(output.status.queryId, 'workloadName', 'default', 100);

   System.debug(statusOutput);

##### **`queryCalculatedInsights(ciName, dimensions, measures, orderby, filters,`**

  batchSize, offset)

```

Query a Calculated Insight object.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput queryCalculatedInsights(String ciName, String

   dimensions, String measures, String orderby, String filters, Integer batchSize, Integer

   offset)

```

Parameters

```
   ciName
```

Type: String

Name of the Calculated Insight object, for example, `IndividualChildrenCount__cio` .

```
   dimensions
```

Type: String

Comma-separated list of up to 10 dimensions, such as `GenderId__c`, to project. If unspecified, this parameter includes all of the
available dimensions.

```
   measures
```

Type: String

Comma-separated list of up to 5 measures, such as `TotalSales__c`, to project. If unspecified, this parameter includes all of the
available measures.

```
   orderby
```

Type: String


Apex Reference Guide CdpQuery Class

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.

```
   filters
```

Type: String

Filter the result set to a more narrow scope or specific type, such as `[GenderId__c=Male,FirstName__c=Angel]` .

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–4,999. If unspecified, the default value is `4999` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. If unspecified, no rows are skipped.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`queryCalculatedInsights(ciName, dimensions, measures, orderby, filters,`**

```
  batchSize, offset, timeGranularity)

```

Query a Calculated Insight object within a specified time range.

API Version

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput queryCalculatedInsights(String ciName, String

   dimensions, String measures, String orderby, String filters, Integer batchSize, Integer

   offset, String timeGranularity)

```

Parameters

```
   ciName
```

Type: String

Name of the Calculated Insight object, for example, `IndividualChildrenCount__cio` .

```
   dimensions
```

Type: String

Comma-separated list of up to 10 dimensions, such as `GenderId__c`, to project. If unspecified, this parameter includes all of the
available dimensions.

```
   measures
```

Type: String


Apex Reference Guide CdpQuery Class

Comma-separated list of up to 5 measures, such as `TotalSales__c`, to project. If unspecified, this parameter includes all of the
available measures.

```
   orderby
```

Type: String

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.

```
   filters
```

Type: String

Filter the result set to a more narrow scope or specific type, such as `[GenderId__c=Male,FirstName__c=Angel]` .

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–4,999. If unspecified, the default value is `4999` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. If unspecified, no rows are skipped.

```
   timeGranularity
```

Type: String

Time range for the measures. Values are:

**•** `HOUR`

**•** `DAY`

**•** `MONTH`

**•** `QUARTER`

**•** `YEAR`

If unspecified, no time range is applied.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`queryCalculatedInsights(ciName, dimensions, measures, orderby, filters,`**

```
  batchSize, offset, timeGranularity, dataspace)

```

Query a Calculated Insight object within a specified time range and specify the data space.

API Version

57.0

Requires Chatter

No


Apex Reference Guide CdpQuery Class

Signature

```
   public static ConnectApi.CdpQueryOutput queryCalculatedInsights(String ciName, String

   dimensions, String measures, String orderby, String filters, Integer batchSize, Integer

   offset, String timeGranularity, String dataspace)

```

Parameters

```
   ciName
```

Type: String

Name of the Calculated Insight object, for example, `IndividualChildrenCount__cio` .

```
   dimensions
```

Type: String

Comma-separated list of up to 10 dimensions, such as `GenderId__c`, to project. If unspecified, this parameter includes all of the
available dimensions.

```
   measures
```

Type: String

Comma-separated list of up to 5 measures, such as `TotalSales__c`, to project. If unspecified, this parameter includes all of the
available measures.

```
   orderby
```

Type: String

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.

```
   filters
```

Type: String

Filter the result set to a more narrow scope or specific type, such as `[GenderId__c=Male,FirstName__c=Angel]` .

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–4,999. If unspecified, the default value is `4999` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. If unspecified, no rows are skipped.

```
   timeGranularity
```

Type: String

Time range for the measures. Values are:

**•** `HOUR`

**•** `DAY`

**•** `MONTH`

**•** `QUARTER`

**•** `YEAR`

If unspecified, no time range is applied.

```
   dataspace
```

Type: String


Apex Reference Guide CdpQuery Class

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`queryProfileApi(dataModelName, filters, fields, batchSize, offset, orderby)`**

Query a Profile data model object using filters.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput queryProfileApi(String dataModelName, String

   filters, String fields, Integer batchSize, Integer offset, String orderby)

```

Parameters

```
   dataModelName
```

Type: String

Name of the data model object, for example, `UnifiedIndividual__dlm` .

```
   filters
```

Type: String

Comma-separated list of equality expressions within square brackets, for example, `[FirstName__c=DON]` .

```
   fields
```

Type: String

Comma-separated list of up to 50 field names that you want to include in the result, for example, `Id__c,FirstName__c,`
`GenderId__c,Occupation__c` . If unspecified, `Id__c` is returned.

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–4,999. If unspecified, the default value is `100` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. If unspecified, no rows are skipped.

```
   orderby
```

Type: String

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.


Apex Reference Guide CdpQuery Class

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`queryProfileApi(dataModelName, id, searchKey, filters, fields, batchSize,`**

```
  offset, orderby)

```

Query a Profile data model object using filters and a search key.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput queryProfileApi(String dataModelName, String

   id, String searchKey, String filters, String fields, Integer batchSize, Integer offset,

   String orderby)

```

Parameters

```
   dataModelName
```

Type: String

Name of the data model object, for example, `UnifiedIndividual__dlm` .

```
   id
```

Type: String

Value of the primary or secondary key field, for example, `John` . If unspecified, defaults to the value of the primary key field.

```
   searchKey
```

Type: String

If a field other than the primary key is used, name of the key field, for example, `FirstName__c` .

```
   filters
```

Type: String

Comma-separated list of equality expressions within square brackets, for example, `[FirstName__c=DON]` .

```
   fields
```

Type: String

Comma-separated list of up to 50 field names that you want to include in the result, for example, `Id__c,FirstName__c,`
`GenderId__c,Occupation__c` . If unspecified, `Id__c` is returned.

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–4,999. If unspecified, the default value is `100` .

```
   offset
```

Type: Integer


Apex Reference Guide CdpQuery Class

Number of rows to skip before returning results. If unspecified, no rows are skipped.

```
   orderby
```

Type: String

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`queryProfileApi(dataModelName, id, childDataModelName, searchKey, filters,`**

```
  fields, batchSize, offset, orderby)

```

Query a Profile data model object and a child object using filters and a search key.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput queryProfileApi(String dataModelName, String

   id, String childDataModelName, String searchKey, String filters, String fields, Integer

   batchSize, Integer offset, String orderby)

```

Parameters

```
   dataModelName
```

Type: String

Name of the data model object, for example, `UnifiedIndividual__dlm` .

```
   id
```

Type: String

Value of the primary or secondary key field, for example, `John` . If unspecified, defaults to the value of the primary key field.

```
   childDataModelName
```

Type: String

Name of the child data model object, for example, `UnifiedContactPointEmail__dlm` .

```
   searchKey
```

Type: String

If a field other than the primary key is used, name of the key field, for example, `FirstName__c` .

```
   filters
```

Type: String


Apex Reference Guide CdpQuery Class

Comma-separated list of equality expressions within square brackets, for example, `[FirstName__c=DON]` . Filters are applied
to the parent object only.

```
   fields
```

Type: String

Comma-separated list of child object field names that you want to include in the result, for example, `Id__c,EmailAddress__c` .
If unspecified, the first 10 alphabetically sorted fields are returned.

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–4,999. If unspecified, the default value is `100` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. If unspecified, no rows are skipped.

```
   orderby
```

Type: String

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`queryProfileApi(dataModelName, id, ciName, searchKey, dimensions, measures,`**

```
  filters, fields, batchSize, offset, orderby)

```

Query a Profile data model object and a Calculated Insight object using filters and a search key.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput queryProfileApi(String dataModelName, String

   id, String ciName, String searchKey, String dimensions, String measures, String filters,

   String fields, Integer batchSize, Integer offset, String orderby)

```

Parameters

```
   dataModelName
```

Type: String

Name of the data model object, for example, `UnifiedIndividual__dlm` .


Apex Reference Guide CdpQuery Class

```
   id
```

Type: String

Value of the primary or secondary key field, for example, `John` . If unspecified, defaults to the value of the primary key field.

```
   ciName
```

Type: String

Name of the Calculated Insight object, for example, `IndividualChildrenCount__cio` .

```
   searchKey
```

Type: String

If a field other than the primary key is used, name of the key field, for example, `FirstName__c` .

```
   dimensions
```

Type: String

Comma-separated list of up to 10 dimensions, such as `GenderId__c`, to project. If unspecified, this parameter includes all of the
available dimensions.

```
   measures
```

Type: String

Comma-separated list of up to 5 measures, such as `TotalSales__c`, to project. If unspecified, this parameter includes all of the
available measures.

```
   filters
```

Type: String

Comma-separated list of equality expressions within square brackets, for example, `[FirstName__c=DON]` .

```
   fields
```

Type: String

Comma-separated list of up to 50 field names that you want to include in the result, for example, `Id__c,FirstName__c,`
`GenderId__c,Occupation__c` . If unspecified, `Id__c` is returned.

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–4,999. If unspecified, the default value is `100` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. If unspecified, no rows are skipped.

```
   orderby
```

Type: String

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.

Return Value

Type: `ConnectApi.CdpQueryOutput`


Apex Reference Guide CdpQuery Class

##### **`queryProfileApi(dataModelName, id, ciName, searchKey, dimensions, measures,`**

```
  filters, fields, batchSize, offset, orderby, timeGranularity)

```

Query a Profile data model object and a Calculated Insight object using filters, a search key, and a time range.

API Version

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput queryProfileApi(String dataModelName, String

   id, String ciName, String searchKey, String dimensions, String measures, String filters,

   String fields, Integer batchSize, Integer offset, String orderby, String timeGranularity)

```

Parameters

```
   dataModelName
```

Type: String

Name of the data model object, for example, `UnifiedIndividual__dlm` .

```
   id
```

Type: String

Value of the primary or secondary key field, for example, `John` . If unspecified, defaults to the value of the primary key field.

```
   ciName
```

Type: String

Name of the Calculated Insight object, for example, `IndividualChildrenCount__cio` .

```
   searchKey
```

Type: String

If a field other than the primary key is used, name of the key field, for example, `FirstName__c` .

```
   dimensions
```

Type: String

Comma-separated list of up to 10 dimensions, such as `GenderId__c`, to project. If unspecified, this parameter includes all of the
available dimensions.

```
   measures
```

Type: String

Comma-separated list of up to 5 measures, such as `TotalSales__c`, to project. If unspecified, this parameter includes all of the
available measures.

```
   filters
```

Type: String

Comma-separated list of equality expressions within square brackets, for example, `[FirstName__c=DON]` .


Apex Reference Guide CdpQuery Class

```
   fields
```

Type: String

Comma-separated list of up to 50 field names that you want to include in the result, for example, `Id__c,FirstName__c,`
`GenderId__c,Occupation__c` . If unspecified, `Id__c` is returned.

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–4,999. If unspecified, the default value is `100` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. If unspecified, no rows are skipped.

```
   orderby
```

Type: String

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.

```
   timeGranularity
```

Type: String

Time range for the measures. Values are:

**•** `HOUR`

**•** `DAY`

**•** `MONTH`

**•** `QUARTER`

**•** `YEAR`

If unspecified, no time range is applied.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`queryProfileApi(dataModelName, id, ciName, searchKey, dimensions, measures,`**

```
  filters, fields, batchSize, offset, orderby, timeGranularity, dataspace)

```

Query a Profile data model object and a Calculated Insight object using filters, a search key, a time range, and a data space.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryOutput queryProfileApi(String dataModelName, String

   id, String ciName, String searchKey, String dimensions, String measures, String filters,

```


Apex Reference Guide CdpQuery Class

```
   String fields, Integer batchSize, Integer offset, String orderby, String timeGranularity,

   String dataspace)

```

Parameters

```
   dataModelName
```

Type: String

Name of the data model object, for example, `UnifiedIndividual__dlm` .

```
   id
```

Type: String

Value of the primary or secondary key field, for example, `John` . If unspecified, defaults to the value of the primary key field.

```
   ciName
```

Type: String

Name of the Calculated Insight object, for example, `IndividualChildrenCount__cio` .

```
   searchKey
```

Type: String

If a field other than the primary key is used, name of the key field, for example, `FirstName__c` .

```
   dimensions
```

Type: String

Comma-separated list of up to 10 dimensions, such as `GenderId__c`, to project. If unspecified, this parameter includes all of the
available dimensions.

```
   measures
```

Type: String

Comma-separated list of up to 5 measures, such as `TotalSales__c`, to project. If unspecified, this parameter includes all of the
available measures.

```
   filters
```

Type: String

Comma-separated list of equality expressions within square brackets, for example, `[FirstName__c=DON]` .

```
   fields
```

Type: String

Comma-separated list of up to 50 field names that you want to include in the result, for example, `Id__c,FirstName__c,`
`GenderId__c,Occupation__c` . If unspecified, `Id__c` is returned.

```
   batchSize
```

Type: Integer

Number of items to return. Values are from 1–4,999. If unspecified, the default value is `100` .

```
   offset
```

Type: Integer

Number of rows to skip before returning results. If unspecified, no rows are skipped.

```
   orderby
```

Type: String

Sort order for the result set, such as `GenderId__c ASC,Occupation__c DESC` . If unspecified, items are returned in the
order they are retrieved.


Apex Reference Guide CdpQuery Class

```
   timeGranularity
```

Type: String

Time range for the measures. Values are:

**•** `HOUR`

**•** `DAY`

**•** `MONTH`

**•** `QUARTER`

**•** `YEAR`

If unspecified, no time range is applied.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.

Return Value

Type: `ConnectApi.CdpQueryOutput`

##### **`universalIdLookupBySourceId(entityName, dataSourceId, dataSourceObjectId,`**

```
  sourceRecordId)

```

Look up objects by source ID.

API Version

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryDataOutput universalIdLookupBySourceId(String

   entityName, String dataSourceId, String dataSourceObjectId, String sourceRecordId)

```

Parameters

```
   entityName
```

Type: String

Entity name.

```
   dataSourceId
```

Type: String

Data source ID.

```
   dataSourceObjectId
```

Type: String


Apex Reference Guide CdpQuery Class

Data source object ID.

```
   sourceRecordId
```

Type: String

Source record ID.

Return Value

Type: `ConnectApi.CdpQueryDataOutput`

##### **`universalIdLookupBySourceId(entityName, dataSourceId, dataSourceObjectId,`**

```
  sourceRecordId, dataspace)

```

Look up objects by source ID and specify the data space.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpQueryDataOutput universalIdLookupBySourceId(String

   entityName, String dataSourceId, String dataSourceObjectId, String sourceRecordId,

   String dataspace)

```

Parameters

```
   entityName
```

Type: String

Entity name.

```
   dataSourceId
```

Type: String

Data source ID.

```
   dataSourceObjectId
```

Type: String

Data source object ID.

```
   sourceRecordId
```

Type: String

Source record ID.

```
   dataspace
```

Type: String

Name of the data space to query. If unspecified, the `default` data space is used.


### Apex Reference Guide CdpSegment Class

Return Value

Type: `ConnectApi.CdpQueryDataOutput`

### CdpSegment Class

Create, delete, get, publish, and update Data 360 segments.

Namespace

ConnectApi

#### CdpSegment Methods

### These methods are for CdpSegment . All methods are static.

IN THIS SECTION:

createSegment(input)
Create a segment.

createSegment(input, dataspace)
Create a segment in a dataspace.

deactivateSegmentByApiName(segmentApiName)
Deactivate a segment by API name.

deactivateSegmentById(segmentId)
Deactivate a segment by ID.

deleteSegment(segmentApiName)
Delete a segment.

executePublishAdhoc(segmentId)
Publish a segment.

getSegment(segmentApiName)
Get a segment by API name.

getSegmentById(segmentId)
Get a segment by ID.

getSegments()
Get segments.

getSegmentsPaginated(batchSize, offset, orderBy)
Get an ordered batch of paginated segments.

getSegmentsPaginated(batchSize, offset, orderBy, dataspace)
Get an ordered batch of paginated segments in a dataspace.

getSegmentsFilteredPaginated(batchSize, offset, orderBy, filters)
Get an ordered and filtered batch of paginated segments.

getSegmentsFilteredPaginated(batchSize, offset, orderBy, dataspace, filters)
Get an ordered and filtered batch of paginated segments in a dataspace.


Apex Reference Guide CdpSegment Class

updateSegment(segmentApiName, input)
Update a segment.

##### **`createSegment(input)`**

Create a segment.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentOutput createSegment(ConnectApi.CdpSegmentInput

   input)

```

Parameters

```
   input
```

Type: `ConnectApi.CdpSegmentInput`

A `ConnectApi.CdpSegmentInput` class.

Return Value

Type: `ConnectApi.CdpSegmentOutput`

##### **`createSegment(input, dataspace)`**

Create a segment in a dataspace.

API Version

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentOutput createSegment(ConnectApi.CdpSegmentInput

   input, String dataspace)

```


Apex Reference Guide CdpSegment Class

Parameters

```
   input
```

Type: `ConnectApi.CdpSegmentInput`

A `ConnectApi.CdpSegmentInput` class.

```
   dataspace
```

Type: String

Name of the dataspace in which to perform the action. The user must have permission to the specified dataspace. Specify `default`
to use the default dataspace.

Return Value

Type: `ConnectApi.CdpSegmentOutput`

##### **`deactivateSegmentByApiName(segmentApiName)`**

Deactivate a segment by API name.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentActionOutput deactivateSegmentByApiName(String

   segmentApiName)

```

Parameters

```
   segmentApiName
```

Type: String

API name of the segment.

Return Value

Type: `ConnectApi.CdpSegmentActionOutput`

##### **`deactivateSegmentById(segmentId)`**

Deactivate a segment by ID.

API Version

59.0


Apex Reference Guide CdpSegment Class

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentActionOutput deactivateSegmentById(String segmentId)

```

Parameters

```
   segmentId
```

Type: String

ID of the segment.

Return Value

Type: `ConnectApi.CdpSegmentActionOutput`

##### **`deleteSegment(segmentApiName)`**

Delete a segment.

API Version

56.0

Requires Chatter

No

Signature

```
   public static Void deleteSegment(String segmentApiName)

```

Parameters

```
   segmentApiName
```

Type: String

API name of the segment.

Return Value

Type: Void

##### **`executePublishAdhoc(segmentId)`**

Publish a segment.

API Version

56.0


Apex Reference Guide CdpSegment Class

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentActionOutput executePublishAdhoc(String segmentId)

```

Parameters

```
   segmentId
```

Type: String

ID of the segment to publish.

Return Value

Type: `ConnectApi.CdpSegmentActionOutput`

##### **`getSegment(segmentApiName)`**

Get a segment by API name.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentContainerOutput getSegment(String segmentApiName)

```

Parameters

```
   segmentApiName
```

Type: String

API name of the segment.

Return Value

Type: `ConnectApi.CdpSegmentContainerOutput`

##### **`getSegmentById(segmentId)`**

Get a segment by ID.

API Version

65.0


Apex Reference Guide CdpSegment Class

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentContainerOutput getSegmentById(String segmentId)

```

Parameters

```
   segmentId
```

Type: String

ID of the segment.

Return Value

Type: `ConnectApi.CdpSegmentContainerOutput`

##### **`getSegments()`**

Get segments.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentContainerOutput getSegments()

```

Return Value

Type: `ConnectApi.CdpSegmentContainerOutput`

##### **`getSegmentsPaginated(batchSize, offset, orderBy)`**

Get an ordered batch of paginated segments.

API Version

56.0

Requires Chatter

No


Apex Reference Guide CdpSegment Class

Signature

```
   public static ConnectApi.CdpSegmentContainerOutput getSegmentsPaginated(Integer

   batchSize, Integer offset, String orderBy)

```

Parameters

```
   batchSize
```

Type: Integer

Number of segments to return at one time. Values are from `1` through `200` . For example, specify `20` to return 20 segments.

```
   offset
```

Type: Integer

Number of segments to skip before returning results. Specify `0` to skip no segments.

```
   orderBy
```

Type: String

Sort order for the result set. Specify a field value followed by an optional sort order, `ASC` or `DESC` . For example, `Name ASC` sorts
results by `Name` in ascending order, and `MarketSegmentType DESC` sorts results by `MarketSegmentType` in descending
order. Omit `ASC` and `DESC` to return results in ascending order by default.

Return Value

Type: `ConnectApi.CdpSegmentContainerOutput`

##### **`getSegmentsPaginated(batchSize, offset, orderBy, dataspace)`**

Get an ordered batch of paginated segments in a dataspace.

API Version

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentContainerOutput getSegmentsPaginated(Integer

   batchSize, Integer offset, String orderBy, String dataspace)

```

Parameters

```
   batchSize
```

Type: Integer

Number of segments to return at one time. Values are from `1` through `200` . For example, specify `20` to return 20 segments.

```
   offset
```

Type: Integer

Number of segments to skip before returning results. Specify `0` to skip no segments.


Apex Reference Guide CdpSegment Class

```
   orderBy
```

Type: String

Sort order for the result set. Specify a field value followed by an optional sort order, `ASC` or `DESC` . For example, `Name ASC` sorts
results by `Name` in ascending order, and `MarketSegmentType DESC` sorts results by `MarketSegmentType` in descending
order. Omit `ASC` and `DESC` to return results in ascending order by default.

```
   dataspace
```

Type: String

Name of the dataspace in which to perform the action. The user must have permission to the specified dataspace. Specify `default`
to use the default dataspace.

Return Value

Type: `ConnectApi.CdpSegmentContainerOutput`

##### **`getSegmentsFilteredPaginated(batchSize, offset, orderBy, filters)`**

Get an ordered and filtered batch of paginated segments.

API Version

65.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentContainerOutput getSegmentsFilteredPaginated(Integer

   batchSize, Integer offset, String orderBy, String filters)

```

Parameters

```
   batchSize
```

Type: Integer

Number of segments to return at one time. Values are from `1` through `200` . For example, specify `20` to return 20 segments.

```
   offset
```

Type: Integer

Number of segments to skip before returning results. Specify `0` to skip no segments.

```
   orderBy
```

Type: String

Sort order for the result set. Specify a field value followed by an optional sort order, `ASC` or `DESC` . For example, `Name ASC` sorts
results by `Name` in ascending order, and `MarketSegmentType DESC` sorts results by `MarketSegmentType` in descending
order. Omit `ASC` and `DESC` to return results in ascending order by default.

```
   filters
```

Type: String


Apex Reference Guide CdpSegment Class

Filter the result set to a more narrow scope based on segment attributes. Specify a maximum of 10 filters. Separate each filter by an
`AND` logical operator.

These values are supported:

**•** `LastPublishedEndDateTime`     - Not present in the output type. Indicates the end date and time when the segment was
last published. Use only the `!=` operator with this value.

**•** `MarketSegmentType`     - Matches field `segmentType` .

**•** `Name`     - Matches field `disaplyName` .

**•** `SegmentOn`     - Matches field `segmentOnApiName` .

**•** `SegmentStatus`     - Matches field `segmentStatus` .

These operators are supported:

**•** `contains`     - Search operator for identifying strings or substrings within a field.

**•** `eq`     - Equality operator for identifying values that match exactly.

**•** `in`     - Comparison operator for determining whether a field matches one or more specified values.

**•** `!=`     - Inequality operator for determining values that don't match.

These are examples of filter parameter specifications:

**•** `Name != NULL AND Name In Seg 01,seg 02 AND Name contains seg AND Name eq seg 01`

**•** `SegmentStatus != NULL AND SegmentStatus In Processing,Active AND SegmentStatus`

```
      contains ive AND SegmentStatus eq active

```

**•** `MarketSegmentType != NULL AND MarketSegmentType In UI,Dbt AND MarketSegmentType`

```
      contains i AND MarketSegmentType eq UI

```

**•** `SegmentOn != NULL AND SegmentOn In individual,account AND SegmentOn contains ual`

```
      AND SegmentOn eq Account

```

**•** `SegmentOn != NULL AND SegmentOn In individual,account AND SegmentOn contains nt`

```
      AND SegmentOn eq Account

```

**•** `LastPublishedEndDateTime != NULL`

Return Value

Type: `ConnectApi.CdpSegmentContainerOutput`

##### **`getSegmentsFilteredPaginated(batchSize, offset, orderBy, dataspace, filters)`**

Get an ordered and filtered batch of paginated segments in a dataspace.

API Version

65.0

Requires Chatter

No


Apex Reference Guide CdpSegment Class

Signature

```
   public static ConnectApi.CdpSegmentContainerOutput getSegmentsFilteredPaginated(Integer

   batchSize, Integer offset, String orderBy, String dataspace, String filters)

```

Parameters

```
   batchSize
```

Type: Integer

Number of segments to return at one time. Values are from `1` through `200` . For example, specify `20` to return 20 segments.

```
   offset
```

Type: Integer

Number of segments to skip before returning results. Specify `0` to skip no segments.

```
   orderBy
```

Type: String

Sort order for the result set. Specify a field value followed by an optional sort order, `ASC` or `DESC` . For example, `Name ASC` sorts
results by `Name` in ascending order, and `MarketSegmentType DESC` sorts results by `MarketSegmentType` in descending
order. Omit `ASC` and `DESC` to return results in ascending order by default.

```
   dataspace
```

Type: String

Name of the dataspace in which to perform the action. The user must have permission to the specified dataspace. Specify `default`
to use the default dataspace.

```
   filters
```

Type: String

Filter the result set to a more narrow scope based on segment attributes. Specify a maximum of 10 filters. Separate each filter by an
`AND` logical operator.

These values are supported:

**•** `LastPublishedEndDateTime`     - Not present in the output type. Indicates the end date and time when the segment was
last published. Use only the `!=` operator with this value.

**•** `MarketSegmentType`     - Matches field `segmentType` .

**•** `Name`     - Matches field `disaplyName` .

**•** `SegmentOn`     - Matches field `segmentOnApiName` .

**•** `SegmentStatus`     - Matches field `segmentStatus` .

These operators are supported:

**•** `contains`     - Search operator for identifying strings or substrings within a field.

**•** `eq`     - Equality operator for identifying values that match exactly.

**•** `in`     - Comparison operator for determining whether a field matches one or more specified values.

**•** `!=`     - Inequality operator for determining values that don't match.

These are examples of filter parameter specifications:

**•** `Name != NULL AND Name In Seg 01,seg 02 AND Name contains seg AND Name eq seg 01`

**•** `SegmentStatus != NULL AND SegmentStatus In Processing,Active AND SegmentStatus`

```
      contains ive AND SegmentStatus eq active

```


### Apex Reference Guide Chatter Class

**•** `MarketSegmentType != NULL AND MarketSegmentType In UI,Dbt AND MarketSegmentType`

```
      contains i AND MarketSegmentType eq UI

```

**•** `SegmentOn != NULL AND SegmentOn In individual,account AND SegmentOn contains ual`

```
      AND SegmentOn eq Account

```

**•** `SegmentOn != NULL AND SegmentOn In individual,account AND SegmentOn contains nt`

```
      AND SegmentOn eq Account

```

**•** `LastPublishedEndDateTime != NULL`

Return Value

Type: `ConnectApi.CdpSegmentContainerOutput`

##### **`updateSegment(segmentApiName, input)`**

Update a segment.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CdpSegmentOutput updateSegment(String segmentApiName,

   ConnectApi.CdpSegmentInput input)

```

Parameters

```
   segmentApiName
```

Type: String

API name of the segment.

```
   input
```

Type: `ConnectApi.CdpSegmentInput`

A `ConnectApi.CdpSegmentInput` class with the updates.

Return Value

Type: `ConnectApi.CdpSegmentOutput`

### Chatter Class

Access information about followers and subscriptions for records.


Apex Reference Guide Chatter Class

Namespace

ConnectApi

#### Chatter Methods These methods are for Chatter . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

##### deleteSubscription(communityId, subscriptionId)

Delete a subscription. Use this method to stop following a record, a user, or a file.

getFollowers(communityId, recordId)
Get the first page of followers for a record.

getFollowers(communityId, recordId, pageParam, pageSize)
Get a page of followers for a record.

getSubscription(communityId, subscriptionId)
Get information about a subscription.

submitDigestJob(period)
Submit a daily or weekly Chatter email digest job.

##### **`deleteSubscription(communityId, subscriptionId)`**

Delete a subscription. Use this method to stop following a record, a user, or a file.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static void deleteSubscription(String communityId, String subscriptionId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subscriptionId
```

Type: String

The ID for a subscription.


Apex Reference Guide Chatter Class

Return Value

Type: Void

Usage

“Following” a user, group, or record is the same as “subscribing” to a user, group, or record. A “follower” is the user who followed the
user, group, or record. A “subscription” is an object describing the relationship between the follower and the user, group, or record they
followed.

To leave a group, call `deleteMember(communityId, membershipId)` .

Example

When you follow a user, the call to `ConnectApi.ChatterUsers.follow` returns a `ConnectApi.Subscription` object.
To stop following the user, pass the `id` property of that object to this method.

```
   ConnectApi.Chatter.deleteSubscription(null, '0E8RR0000004CnK0AU');

```

SEE ALSO:

[Follow a Record](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_follow_record.htm)

follow(communityId, userId, subjectId)

##### **`getFollowers(communityId, recordId)`**

Get the first page of followers for a record.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FollowerPage getFollowers(String communityId, String recordId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

ID for a record or the keyword `me` .


Apex Reference Guide Chatter Class

Return Value

Type: `ConnectApi.FollowerPage`

Usage

“Following” a user, group, or record is the same as “subscribing” to a user, group, or record. A “follower” is the user who followed the
user, group, or record. A “subscription” is an object describing the relationship between the follower and the user, group, or record they
followed.

SEE ALSO:

[Follow a Record](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_follow_record.htm)

##### **`getFollowers(communityId, recordId, pageParam, pageSize)`**

Get a page of followers for a record.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FollowerPage getFollowers(String communityId, String recordId,

   Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

ID for a record or the keyword `me` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.FollowerPage`


Apex Reference Guide Chatter Class

Usage

“Following” a user, group, or record is the same as “subscribing” to a user, group, or record. A “follower” is the user who followed the
user, group, or record. A “subscription” is an object describing the relationship between the follower and the user, group, or record they
followed.

SEE ALSO:

[Follow a Record](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_follow_record.htm)

##### **`getSubscription(communityId, subscriptionId)`**

Get information about a subscription.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Subscription getSubscription(String communityId, String

   subscriptionId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subscriptionId
```

Type: String

The ID for a subscription.

Return Value

Type: `ConnectApi.Subscription`

Usage

“Following” a user, group, or record is the same as “subscribing” to a user, group, or record. A “follower” is the user who followed the
user, group, or record. A “subscription” is an object describing the relationship between the follower and the user, group, or record they
followed.

SEE ALSO:

[Follow a Record](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_follow_record.htm)


Apex Reference Guide Chatter Class

##### **`submitDigestJob(period)`**

Submit a daily or weekly Chatter email digest job.

API Version

37.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.DigestJobRepresentation submitDigestJob(ConnectApi.DigestPeriod

   period)

```

Parameters

```
   period
```

Type: `ConnectApi.DigestPeriod`

Time period that’s included in a Chatter email digest. Values are:

**•** `DailyDigest` —The email includes up to the 50 latest posts from the previous day.

**•** `WeeklyDigest` —The email includes up to the 50 latest posts from the previous week.

Return Value

Type: `ConnectApi.DigestJob`

Usage

The times when Chatter sends email digests are not configurable in the UI. To control when email digests are sent and to use this method,
contact Salesforce to enable API-only Chatter Digests.

Warning: Enabling API-only Chatter Digests disables the scheduled digests for your org. You must call the API for your users to
receive their digests.

We recommend scheduling digest jobs by implementing the Apex `Schedulable` interface with this method. To monitor your digest
jobs from Setup, enter _`Background Jobs`_ in the `Quick Find` box, then select **Background Jobs** .

Example

Schedule daily digests:

```
   global class ExampleDigestJob1 implements Schedulable {

     global void execute(SchedulableContext context) {

       ConnectApi.Chatter.submitDigestJob(ConnectApi.DigestPeriod.DailyDigest);

     }

   }

```


### Apex Reference Guide ChatterFavorites Class

Schedule weekly digests:

```
   global class ExampleDigestJob2 implements Schedulable {

     global void execute(SchedulableContext context) {

       ConnectApi.Chatter.submitDigestJob(ConnectApi.DigestPeriod.WeeklyDigest);

     }

   }

```

SEE ALSO:

[Apex Scheduler](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_scheduler.htm)

### ChatterFavorites Class

Chatter favorites give you easy access to topics, list views, and feed searches.

Namespace

ConnectApi

Usage

Use Connect in Apex to get and delete topics, list views, and feed searches that have been added as favorites. Add topics and feed
searches as favorites, and update the last view date of a feed search or list view feed to the current system time.

In this image of Salesforce, “Build Issues” is a topic, “All Accounts” is a list view, and “United” is a feed search.

#### ChatterFavorites Methods

### These methods are for ChatterFavorites . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.


Apex Reference Guide ChatterFavorites Class

IN THIS SECTION:

##### addFavorite(communityId, subjectId, searchText)

Add a feed search favorite for a user.

addRecordFavorite(communityId, subjectId, targetId)
Add a topic as a favorite.

deleteFavorite(communityId, subjectId, favoriteId)
Delete a favorite.

getFavorite(communityId, subjectId, favoriteId)
Get information about a favorite.

getFavorites(communityId, subjectId)
Get a list of favorites for a user.

getFeedElements(communityId, subjectId, favoriteId)
Get the first page of feed elements for a favorite.

getFeedElements(communityId, subjectId, favoriteId, pageParam, pageSize, sortParam)
Get a page of sorted feed elements for a favorite.

getFeedElements(communityId, subjectId, favoriteId, recentCommentCount, elementsPerBundle, pageParam, pageSize, sortParam)
Get a page of sorted feed elements for a favorite. Include no more than the specified number of comments per feed element.

updateFavorite(communityId, subjectId, favoriteId, updateLastViewDate)
Update the last view date of the saved search or list view feed to the current system time.

##### **`addFavorite(communityId, subjectId, searchText)`**

Add a feed search favorite for a user.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedFavorite addFavorite(String communityId, String subjectId,

   String searchText)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .


Apex Reference Guide ChatterFavorites Class

```
   searchText
```

Type: String

Specify the text of the search to be saved as a favorite. This method can only create a feed search favorite, not a list view favorite or
a topic.

Return Value

Type: `ConnectApi.FeedFavorite`

##### **`addRecordFavorite(communityId, subjectId, targetId)`**

Add a topic as a favorite.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedFavorite addRecordFavorite(String communityId, String

   subjectId, String targetId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   targetId
```

Type: String

The ID of the topic to add as a favorite.

Return Value

Type: `ConnectApi.FeedFavorite`

##### **`deleteFavorite(communityId, subjectId, favoriteId)`**

Delete a favorite.


Apex Reference Guide ChatterFavorites Class

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static Void deleteFavorite(String communityId, String subjectId, String

   favoriteId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

Return Value

Type: Void

##### **`getFavorite(communityId, subjectId, favoriteId)`**

Get information about a favorite.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedFavorite getFavorite(String communityId, String subjectId,

   String favoriteId)

```


Apex Reference Guide ChatterFavorites Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

Return Value

Type: `ConnectApi.FeedFavorite`

##### **`getFavorites(communityId, subjectId)`**

Get a list of favorites for a user.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedFavorites getFavorites(String communityId, String subjectId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

Return Value

Type: `ConnectApi.FeedFavorites`

##### **`getFeedElements(communityId, subjectId, favoriteId)`**

Get the first page of feed elements for a favorite.


Apex Reference Guide ChatterFavorites Class

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElements(String communityId, String

   subjectId, String favoriteId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElements(communityId, subjectId, favoriteId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElements(communityId, subjectId, favoriteId, pageParam, pageSize,`**

```
  sortParam)

```

Get a page of sorted feed elements for a favorite.

API Version

31.0


Apex Reference Guide ChatterFavorites Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElements(String communityId, String

   subjectId, String favoriteId, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFavorites Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElements(communityId, subjectId, favoriteId, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElements(communityId, subjectId, favoriteId, recentCommentCount,`**

```
  elementsPerBundle, pageParam, pageSize, sortParam)

```

Get a page of sorted feed elements for a favorite. Include no more than the specified number of comments per feed element.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElements(String communityId, String

   subjectId, String favoriteId, Integer recentCommentCount, Integer elementsPerBundle,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.


Apex Reference Guide ChatterFavorites Class

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElements(communityId, subjectId, favoriteId, recentCommentCount, elementsPerBundle, pageParam, pageSize,
sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`updateFavorite(communityId, subjectId, favoriteId, updateLastViewDate)`**

Update the last view date of the saved search or list view feed to the current system time.

API Version

28.0

Requires Chatter

Yes


Apex Reference Guide ChatterFavorites Class

Signature

```
   public static ConnectApi.FeedFavorite updateFavorite(String communityId, String

   subjectId, String favoriteId, Boolean updateLastViewDate)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

```
   updateLastViewDate
```

Type: Boolean

Specify whether to update the last view date of the specified favorite to the current system time ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.FeedFavorite`

#### ChatterFavorites Test Methods These test methods are for ChatterFavorites . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

IN THIS SECTION:

##### setTestGetFeedElements(communityId, subjectId, favoriteId, result)

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElements` is called with matching
parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElements(communityId, subjectId, favoriteId, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElements` is called with matching
parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElements(communityId, subjectId, favoriteId, recentCommentCount, elementsPerBundle, pageParam, pageSize,
sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElements` is called with matching
parameters in a test context. Use the method with the same parameters or the code throws an exception.

##### **`setTestGetFeedElements(communityId, subjectId, favoriteId, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElements` is called with matching
parameters in a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFavorites Class

API Version

31.0

Signature

```
   public static Void setTestGetFeedElements(String communityId, String subjectId, String

   favoriteId, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElements(communityId, subjectId, favoriteId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElements(communityId, subjectId, favoriteId, pageParam,`**

```
  pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElements` is called with matching
parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElements(String communityId, String subjectId, String

   favoriteId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedElementPage result)

```


Apex Reference Guide ChatterFavorites Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElements(communityId, subjectId, favoriteId, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFavorites Class

##### **`setTestGetFeedElements(communityId, subjectId, favoriteId, recentCommentCount,`**

```
  elementsPerBundle, pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElements` is called with matching
parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElements(String communityId, String subjectId, String

   favoriteId, Integer recentCommentCount, Integer elementsPerBundle, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:


Apex Reference Guide ChatterFavorites Class

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElements(communityId, subjectId, favoriteId, recentCommentCount, elementsPerBundle, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

#### Retired ChatterFavorites Methods

These methods for `ChatterFavorites` are retired.

IN THIS SECTION:

getFeedItems(communityId, subjectId, favoriteId)
Get the first page of feed items for a favorite.

getFeedItems(communityId, subjectId, favoriteId, pageParam, pageSize, sortParam)
Get a page of sorted feed items for a favorite.

getFeedItems(communityId, subjectId, favoriteId, recentCommentCount, pageParam, pageSize, sortParam)
Get a page of sorted feed items for a favorite. Include no more than the specified number of comments per feed item.

setTestGetFeedItems(communityId, subjectId, favoriteId, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItems` is called with matching parameters
in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedItems(communityId, subjectId, favoriteId, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItems` is called with matching parameters
in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedItems(communityId, subjectId, favoriteId, recentCommentCount, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItems` is called with matching parameters
in a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFavorites Class

##### **`getFeedItems(communityId, subjectId, favoriteId)`**

Get the first page of feed items for a favorite.

API Version

28.0–31.0

Important: In version 32.0 and later, use getFeedElements(communityId, subjectId, favoriteId).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItems(String communityId, String subjectId,

   String favoriteId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItems(communityId, subjectId, favoriteId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItems(communityId, subjectId, favoriteId, pageParam, pageSize,`**

```
  sortParam)

```

Get a page of sorted feed items for a favorite.


Apex Reference Guide ChatterFavorites Class

API Version

28.0–31.0

Important: In version 32.0 and later, use getFeedElements(communityId, subjectId, favoriteId, pageParam, pageSize, sortParam).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItems(String communityId, String subjectId,

   String favoriteId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.


Apex Reference Guide ChatterFavorites Class

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItems(communityId, subjectId, favoriteId, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItems(communityId, subjectId, favoriteId, recentCommentCount,`**

```
  pageParam, pageSize, sortParam)

```

Get a page of sorted feed items for a favorite. Include no more than the specified number of comments per feed item.

API Version

29.0–31.0

Important: In version 32.0 and later, use getFeedElements(communityId, subjectId, favoriteId, recentCommentCount,
elementsPerBundle, pageParam, pageSize, sortParam).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItems(String communityId, String subjectId,

   String favoriteId, Integer recentCommentCount, String pageParam, Integer pageSize,

   FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String


Apex Reference Guide ChatterFavorites Class

ID of a favorite.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

##### To test code that uses this method, use the matching set test method (prefix the method name with setTest ). Use the set test method

with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItems(communityId, subjectId, favoriteId, recentCommentCount, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItems(communityId, subjectId, favoriteId, result)`**

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItems` is called with matching parameters in
a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFavorites Class

API Version

28.0–31.0

Signature

```
   public static Void setTestGetFeedItems(String communityId, String subjectId, String

   favoriteId, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItems(communityId, subjectId, favoriteId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItems(communityId, subjectId, favoriteId, pageParam, pageSize,`**

```
  sortParam, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItems` is called with matching parameters in
a test context. Use the method with the same parameters or the code throws an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestGetFeedItems(String communityId, String subjectId, String

   favoriteId, String pageParam, Integer pageSize, FeedSortOrder sortParam,

   ConnectApi.FeedItemPage result)

```


Apex Reference Guide ChatterFavorites Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItems(communityId, subjectId, favoriteId, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFavorites Class

##### **`setTestGetFeedItems(communityId, subjectId, favoriteId, recentCommentCount,`**

```
  pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItems` is called with matching parameters in
a test context. Use the method with the same parameters or the code throws an exception.

API Version

29.0–31.0

Signature

```
   public static Void setTestGetFeedItems(String communityId, String subjectId, String

   favoriteId, Integer recentCommentCount, String pageParam, Integer pageSize, FeedSortOrder

   sortParam, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   favoriteId
```

Type: String

ID of a favorite.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.


### Apex Reference Guide ChatterFeeds Class

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItems(communityId, subjectId, favoriteId, recentCommentCount, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

### ChatterFeeds Class

Get, post, and delete feed elements, likes, comments, and bookmarks. You can also search feed elements, share feed elements, and vote
on polls.

Namespace

ConnectApi

Usage

The Chatter feed is a container of feed elements. The abstract class `ConnectApi.FeedElement` is a parent class to the
`ConnectApi.FeedItem` class, representing feed posts, and the `ConnectApi.GenericFeedElement` class, representing
[bundles and recommendations in the feed. For detailed information, see Working with Feeds and Feed Elements.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_features_feeds_feed_elements.htm)

Important: Feed item methods aren’t available in version 32.0. In version 32.0 and later, use feed element methods.

Message segments in a feed item are typed as `ConnectApi.MessageSegment` . Feed item capabilities are typed as
`ConnectApi.FeedItemCapability` . Record fields are typed as `ConnectApi.AbstractRecordField` . These classes
are all abstract and have several concrete subclasses. At runtime you can use `instanceof` to check the concrete types of these objects
and then safely proceed with the corresponding downcast. When you downcast, you must have a default case that handles unknown
subclasses.

Important: The composition of a feed can change between releases. Write your code to handle instances of unknown subclasses.

#### ChatterFeeds Methods

### These methods are for ChatterFeeds . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.


Apex Reference Guide ChatterFeeds Class

IN THIS SECTION:

createStream(communityId, streamInput)
Create a Chatter feed stream.

deleteComment(communityId, commentId)
Delete a comment.

deleteFeedElement(communityId, feedElementId)
Delete a feed element.

deleteLike(communityId, likeId)
Delete a like on a comment or post.

deleteStream(communityId, streamId)
Delete a Chatter feed stream.

getComment(communityId, commentId)
Get a comment.

getCommentBatch(communityId, commentIds)
Get a list of comments.

getCommentInContext(communityId, commentId, pageSize)
Get a threaded comment in the context of its parent comments and post.

getCommentsForFeedElement(communityId, feedElementId)
Get comments for a feed element.

getCommentsForFeedElement(communityId, feedElementId, threadedCommentsCollapsed)
Get comments in a threaded style for a feed element.

getCommentsForFeedElement(communityId, feedElementId, pageParam, pageSize)
Get a page of comments for a feed element.

getCommentsForFeedElement(communityId, feedElementId, pageParam, pageSize, threadedCommentsCollapsed)
Get a page of comments in a threaded style for a feed element.

getCommentsForFeedElement(communityId, feedElementId, threadedCommentsCollapsed, sortParam)
Get sorted comments in a threaded style for a feed element.

getCommentsForFeedElement(communityId, feedElementId, pageParam, pageSize, threadedCommentsCollapsed, sortParam)
Get a page of sorted comments in a threaded style for a feed element.

getCommentsForFeedElement(communityId, feedElementId, sortParam)
Get sorted comments for a feed element.

getCommentsForFeedElement(communityId, feedElementId, sortParam, threadedCommentsCollapsed)
Get sorted comments in a threaded style for a feed element.

getExtensions(communityId, pageParam, pageSize)
Get extensions.

getFeed(communityId, feedType)
Get a feed.

getFeed(communityId, feedType, sortParam)
Get a sorted feed.


Apex Reference Guide ChatterFeeds Class

getFeed(communityId, feedType, subjectId)
Get a feed for a record or user.

getFeed(communityId, feedType, subjectId, sortParam)
Get a sorted feed for a record or user.

getFeedDirectory(String)
Get a list of all feeds available to the context user.

getFeedElement(communityId, feedElementId)
Get a feed element.

getFeedElement(communityId, feedElementId, commentSort)
Get a feed element with sorted comments.

getFeedElement(communityId, feedElementId, threadedCommentsCollapsed)
Get a feed element and its comments in a threaded style.

getFeedElement(communityId, feedElementId, threadedCommentsCollapsed, commentSort)
Get a feed element and its sorted comments in a threaded style.

getFeedElement(communityId, feedElementId, recentCommentCount, elementsPerBundle)
Get a feed element with the specified number of elements per bundle including no more than the specified number of comments
per feed element.

getFeedElement(communityId, feedElementId, recentCommentCount, elementsPerBundle, threadedCommentsCollapsed)
Get a feed element with its comments in a threaded style with the specified number of elements per bundle and comments per
feed element.

getFeedElement(communityId, feedElementId, recentCommentCount, elementsPerBundle, threadedCommentsCollapsed,
commentSort)
Get a feed element with its sorted comments in a threaded style with the specified number of elements per bundle and comments
per feed element.

getFeedElement(communityId, feedElementId, recentCommentCount, elementsPerBundle, commentSort)
Get a feed element with the specified number of elements per bundle including no more than the specified number of sorted
comments per feed element.

getFeedElementBatch(communityId, feedElementIds)
Get a list of feed elements.

getFeedElementPoll(communityId, feedElementId)
Get the poll associated with a feed element.

getFeedElementsFromBundle(communityId, feedElementId)
Get feed elements from a bundle.

getFeedElementsFromBundle(communityId, feedElementId, pageParam, pageSize, elementsPerBundle, recentCommentCount)
Get a page of feed elements from a bundle. Specify the number of elements per bundle and include no more than the specified
number of comments per feed element.

getFeedElementsFromFeed(communityId, feedType)
Get feed elements from the `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` feeds.

getFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam)
Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`,
`Isolated`, `Moderation`, and `PendingReview` feeds.


Apex Reference Guide ChatterFeeds Class

getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam)
Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`,
`Isolated`, `Moderation`, and `PendingReview` feeds. Each feed element contains no more than the specified number of
comments.

getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter)
Get a page of sorted and filtered feed elements from the `Home` feed. Each feed element contains no more than the specified number
of comments.

getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
threadedCommentsCollapsed)
Get a page of filtered and sorted feed elements with comments in a threaded style from the `Home` feed. Each feed element contains
no more than the specified number of comments.

getFeedElementsFromFeed(communityId, feedType, subjectId)
Get feed elements from any feed other than `Company`, `DirectMessageModeration`, `DirectMessages`, `Filter`,
`Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` for a user or record.

getFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam)
Get a page of sorted feed elements from any feed other than `Company`, `DirectMessageModeration`, `DirectMessages`,
`Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam)
Get a page of sorted feed elements from any feed other than `Company`, `DirectMessageModeration`, `DirectMessages`,
`Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` . Each feed element includes no more than
the specified number of comments.

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
showInternalOnly)
Get a page of sorted feed elements from a record feed. Each feed element includes no more than the specified number of comments.
Specify whether to return feed elements posted by internal (non-Experience Cloud site) users only.

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
filter)
Get a page of sorted and filtered feed elements from the `UserProfile` feed.

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
filter, threadedCommentsCollapsed)
Get a page of feed elements with comments in a threaded style from the `UserProfile` feed.

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
customFilter)
Get a page of sorted and filtered feed elements from the case feed.

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly)
Get a page of sorted feed elements from a record feed. Specify the number of elements per bundle and include no more than the
specified number of comments per feed element. Specify whether to return feed elements posted by internal (non-Experience Cloud
site) users only.

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter)
Get a page of sorted and filtered feed elements from a record feed. Specify the number of elements per bundle and include no more
than the specified number of comments per feed element. Specify whether to return feed elements posted by internal (non-Experience
Cloud site) users only.


Apex Reference Guide ChatterFeeds Class

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, threadedCommentsCollapsed)
Get a page of sorted and filtered feed elements with comments in a threaded style for a record feed. Specify the number of elements
per bundle and include no more than the specified number of comments per feed element. Specify whether to return feed elements
posted by internal (non-Experience Cloud site) users only.

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter)
Get a page of sorted and filtered feed elements from a case feed.

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, threadedCommentsCollapsed)
Get a page of filtered and sorted feed elements with comments in a threaded style from a case feed.

getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix)
Get feed elements from a feed filtered by a key prefix for a user.

getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam)
Get a page of sorted feed elements from a feed filtered by a key prefix for a user.

getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam)
Get a page of sorted feed elements from a feed filtered by a key prefix for a user. Each feed element contains no more than the
specified number of comments.

getFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle,
density, pageParam, pageSize, updatedSince)
Get a page of feed elements from a feed filtered by a key prefix for a user. Include only feed elements that have been updated since
the time specified in the _`updatedSince`_ parameter.

getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince)
Get a page of feed elements from the `Company`, `DirectMessageModeration`, `Home`, and `Moderation` feeds. Include
only feed elements that have been updated since the time specified in the _`updatedSince`_ parameter. Each feed element contains
no more than the specified number of comments.

getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince, filter)
Get a page of filtered feed elements from the `Home` feed. Include only feed elements that have been updated since the time
specified in the _`updatedSince`_ parameter. Each feed element contains no more than the specified number of comments.

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince)
Get a page of feed elements from the `Files`, `Groups`, `News`, `People`, and `Record` feeds. Include only feed elements that
have been updated since the time specified in the _`updatedSince`_ parameter. Each feed element contains no more than the
specified number of comments.

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, updatedSince,
showInternalOnly)
Get a page of feed elements from a record feed. Include only feed elements that have been updated since the time specified in the
_`updatedSince`_ parameter. Specify whether to return feed elements posted by internal (non-Experience Cloud site) users only.

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, updatedSince, filter)
Get a page of filtered feed elements from a `UserProfile` feed. Include only feed elements that have been updated since the
time specified in the _`updatedSince`_ parameter.


Apex Reference Guide ChatterFeeds Class

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, updatedSince, customFilter)
Get a page of filtered feed elements from a case feed. Include only feed elements that have been updated since the time specified
in the _`updatedSince`_ parameter.

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, updatedSince, showInternalOnly)
Get a page of feed elements from a record feed. Include only feed elements that have been updated since the time specified in the
_`updatedSince`_ parameter. Specify the maximum number of feed elements in a bundle and whether to return feed elements
posted by internal (non-Experience Cloud site) users only.

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, updatedSince, showInternalOnly, filter)
Get a page of filtered feed elements from a record feed. Include only feed elements that have been updated since the time specified
in the _`updatedSince`_ parameter. Specify the maximum number of feed elements in a bundle and whether to return feed
elements posted by internal (non-Experience Cloud site) users only.

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, updatedSince, showInternalOnly, customFilter)
Get a page of filtered feed elements from a case feed. Include only feed elements that have been updated since the time specified
in the _`updatedSince`_ parameter.

getFeedWithFeedElements(communityId, feedType, pageSize)
Get information about a feed and a page of feed elements from the feed.

getFeedWithFeedElements(communityId, feedType, pageSize, recentCommentCount)
Get a page of information about the feed and the feed elements with the specified number of comments per feed element from
the feed.

getFilterFeed(communityId, subjectId, keyPrefix)
Get a feed filtered by a key prefix for a user.

getFilterFeed(communityId, subjectId, keyPrefix, sortParam)
Get a sorted feed filtered by a key prefix for a user.

getFilterFeedDirectory(communityId, subjectId)
Get a feed directory of filter feeds available to the context user.

getLike(communityId, likeId)
Get a like on a post or comment.

getLikesForComment(communityId, commentId)
Get likes for a comment.

getLikesForComment(communityId, commentId, pageParam, pageSize)
Get a page of likes for a comment.

getLikesForFeedElement(communityId, feedElementId)
Get likes for a feed element.

getLikesForFeedElement(communityId, feedElementId, pageParam, pageSize)
Get a page of likes for a feed element.

getLinkMetadata(communityId, urls)
Get link metadata for URLs.


Apex Reference Guide ChatterFeeds Class

getPinnedFeedElementsFromFeed(communityId, feedType, subjectId)
Get pinned feed elements from a group or topic feed.

getReadByForFeedElement(communityId, feedElementId)
Get information about who read a feed element and when.

getReadByForFeedElement(communityId, feedElementId, pageParam, pageSize)
Get a page of information about who read a feed element and when.

getRelatedPosts(communityId, feedElementId, filter, maxResults)
Get posts related to the context feed element.

getStream(communityId, streamId)
Get information about a Chatter feed stream.

getStream(communityId, streamId, globalScope)
Get information about a Chatter feed stream, regardless of Experience Cloud site.

getStreams(communityId)
Get the Chatter feed streams for the context user.

getStreams(communityId, sortParam)
Get and sort the Chatter feed streams for the context user.

getStreams(communityId, pageParam, pageSize)
Get a page of Chatter feed streams for the context user.

getStreams(communityId, pageParam, pageSize, sortParam)
Get a sorted page of Chatter feed streams for the context user.

getStreams(communityId, pageParam, pageSize, sortParam, globalScope)
Get a sorted page of Chatter feed streams from all Enterprise Cloud sites for the context user.

getSupportedEmojis()
Get supported emojis for the org.

getThreadsForFeedComment(communityId, commentId)
Get threaded comments for a comment.

getThreadsForFeedComment(communityId, commentId, pageParam, pageSize)
Get a page of threaded comments for a comment.

getThreadsForFeedComment(communityId, commentId, threadedCommentsCollapsed)
Access the comments capability for a comment.

getTopUnansweredQuestions(communityId) (Pilot)
Get top unanswered questions for the context user in aExperience Cloud site.

getTopUnansweredQuestions(communityId, filter) (Pilot)
Get filtered top unanswered questions for the context user in an Experience Cloud site.

getTopUnansweredQuestions(communityId, pageSize) (Pilot)
Get a page of top unanswered questions for the context user in an Experience Cloud site.

getTopUnansweredQuestions(communityId, filter, pageSize) (Pilot)
Get a page of filtered top unanswered questions for the context user in an Experience Cloud site.

getVotesForComment(communityId, commentId, vote)
Get the first page of users who upvoted or downvoted a comment.


Apex Reference Guide ChatterFeeds Class

getVotesForComment(communityId, commentId, vote, pageParam, pageSize)
Get a page of users who upvoted or downvoted a comment.

getVotesForFeedElement(communityId, feedElementId, vote)
Get the first page of users who upvoted or downvoted a feed element.

getVotesForFeedElement(communityId, feedElementId, vote, pageParam, pageSize)
Get a page of users who upvoted or downvoted a feed element.

isCommentEditableByMe(communityId, commentId)
Discover whether the context user can edit a comment.

isFeedElementEditableByMe(communityId, feedElementId)
Discover whether the context user can edit a feed element.

isModified(communityId, feedType, subjectId, since)
Discover whether a news feed has been updated or changed. Use this method to poll a news feed for updates.

likeComment(communityId, commentId)
Like a comment for the context user.

likeFeedElement(communityId, feedElementId)
Like a feed element.

postCommentToFeedElement(communityId, feedElementId, text)
Post a plain-text comment to a feed element.

postCommentToFeedElement(communityId, feedElementId, comment, feedElementFileUpload)
Post a rich-text comment to a feed element. Use this method to include mentions and to attach a file.

postFeedElement(communityId, subjectId, feedElementType, text)
Post a plain-text feed element.

postFeedElement(communityId, feedElement)
Post a rich-text feed element. Include mentions and hashtag topics, attach already uploaded files to a feed element, and associate
action link groups with a feed element. You can also use this method to share a feed element and add a comment.

postFeedElementBatch(communityId, feedElements)
Post a list of feed elements.

publishDraftFeedElement(communityId, feedElementId, feedElement)
Publish a draft feed element.

searchFeedElements(communityId, q)
Get the first page of feed elements that match the search criteria.

searchFeedElements(communityId, q, sortParam)
Get the first page of sorted feed elements that match the search criteria.

searchFeedElements(communityId, q, threadedCommentsCollapsed)
Get the feed elements and comments that match the search criteria.

searchFeedElements(communityId, q, pageParam, pageSize)
Get a page of feed elements that match the search criteria.

searchFeedElements(communityId, q, pageParam, pageSize, sortParam)
Get a page of sorted feed elements that match the search criteria.

searchFeedElements(communityId, q, pageParam, pageSize, threadedCommentsCollapsed)
Get a page of feed elements with comments in a threaded style that match the search criteria.


Apex Reference Guide ChatterFeeds Class

searchFeedElements(communityId, q, recentCommentCount, pageParam, pageSize, sortParam)
Get a page of sorted feed elements that match the search criteria. Each feed element includes no more than the specified number
of comments.

searchFeedElementsInFeed(communityId, feedType, q)
Get the feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` feeds that match the search criteria.

searchFeedElementsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q)
Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`,
and `PendingReview` feeds that match the search criteria.

searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q)
Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`,
and `PendingReview` feeds that match the search criteria. Each feed element includes no more than the specified number of
comments.

searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q, filter)
Get a page of sorted and filtered feed elements from the `Home` feed that match the search criteria. Each feed element includes no
more than the specified number of comments.

searchFeedElementsInFeed(communityId, feedType, subjectId, q)
Search up to 5,000 of the most recent feed elements in a feed for a subject ID that match the search string. Feed elements are
returned in order of most recent activity.

searchFeedElementsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q)
Get a page of sorted feed elements from a feed for a record or user that match the search criteria.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
q)
Get a page of sorted feed elements from a feed that match the search criteria. Each feed element includes no more than the specified
number of comments.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
filter)
Get a page of sorted and filtered feed elements from a `UserProfile` feed that match the search criteria.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
customFilter)
Get a page of sorted and filtered feed elements from a case feed that match the search criteria.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly)
Get a page of sorted feed elements from a feed for a record or user that match the search criteria. Each feed element includes no
more than the specified number of comments. Specify whether to return feed elements posted by internal (non-Experience Cloud
site) users only.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly, filter)
Get a page of sorted and filtered feed elements from a feed for a record or user that match the search criteria. Each feed element
includes no more than the specified number of comments. Specify whether to return feed elements posted by internal (non-Experience
Cloud site) users only.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly, customFilter)
Get a page of sorted and filtered feed elements from a case feed that match the search criteria.


Apex Reference Guide ChatterFeeds Class

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q)
Get the feed elements from a feed filtered by a key prefix that match the search criteria.

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q)
Get a page of sorted feed elements from a feed filtered by a key prefix that match the search criteria.

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize, sortParam,
q)
Get a page of sorted feed elements from a feed filtered by a key prefix that match the search criteria. Each feed element includes no
more than the specified number of comments.

searchStreams(communityId, q)
Search the Chatter feed streams for the context user.

searchStreams(communityId, q, sortParam)
Search and sort the Chatter feed streams for the context user.

searchStreams(communityId, q, pageParam, pageSize)
Search the Chatter feed streams for the context user and return a page of results.

searchStreams(communityId, q, pageParam, pageSize, sortParam)
Search the Chatter feed streams for the context user and return a sorted page of results.

searchStreams(communityId, q, pageParam, pageSize, sortParam, globalScope)
Search the Chatter feed streams from all Experience Cloud sites for the context user and return a sorted page of results.

setCommentIsVerified(communityId, commentId, isVerified)
Mark a comment as verified or unverified.

setCommentIsVerifiedByAnonymized(communityId, commentId, isVerified, isVerifiedByAnonymized)
Mark a comment as verified by an anonymous user.

setCommentVote(communityId, commentId, upDownVote)
Upvote or downvote a comment.

setFeedCommentStatus(communityId, commentId, status)
Set the status of a comment.

setFeedElementIsClosed(communityId, feedElementId, isClosed)
Set a feed element to closed.

setFeedElementVote(communityId, feedElementId, upDownVote)
Upvote or downvote a feed element.

setFeedEntityStatus(communityId, feedElementId, status)
Set the status of a feed post.

setIsMutedByMe(communityId, feedElementId, isMutedByMe)
Mute or unmute a feed element.

setIsReadByMe(communityId, feedElementId, readBy)
Mark a feed element as read for the context user using an input class.

setIsReadByMe(communityId, feedElementId, isReadByMe)
Mark a feed element as read for the context user.

updateComment(communityId, commentId, comment)
Edit a comment.


Apex Reference Guide ChatterFeeds Class

updateDirectMessage(communityId, feedElementId, directMessage)
Update the members of a direct message.

updateFeedElement(communityId, feedElementId, feedElement)
Edit a feed element.

updateFeedElementBookmarks(communityId, feedElementId, bookmarks)
Bookmark a feed element or remove a bookmark from a feed element using an input class.

updateFeedElementBookmarks(communityId, feedElementId, isBookmarkedByCurrentUser)
Bookmark a feed element or remove a bookmark from a feed element.

updateFeedElementReadByCapabilityBatch(communityId, feedElementIds, readBy)
Mark multiple feed elements as read by the context user at the same time using an input class.

updateFeedElementReadByCapabilityBatch(communityId, feedElementIds, isReadByMe)
Mark multiple feed elements as read by the context user at the same time.

updateLikeForComment(communityId, commentId, isLikedByCurrentUser)
Like or unlike a comment.

updateLikeForFeedElement(communityId, feedElementId, isLikedByCurrentUser)
Like or unlike a feed element.

updatePinnedFeedElements(communityId, feedType, subjectId, pin)
Pin or unpin feed elements to a group or topic feed.

updateStream(communityId, streamId, streamInput)
Update a Chatter feed stream.

voteOnFeedElementPoll(communityId, feedElementId, myChoiceId)
Vote on a poll or change your vote on a poll.

##### **`createStream(communityId, streamInput)`**

Create a Chatter feed stream.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStream createStream(String communityId,

   ConnectApi.ChatterStreamInput streamInput)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   streamInput
```

Type: `ConnectApi.ChatterStreamInput`

A `ConnectApi.ChatterStreamInput` body.

Return Value

Type: `ConnectApi.ChatterStream`

##### **`deleteComment(communityId, commentId)`**

Delete a comment.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static Void deleteComment(String communityId, String commentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

Return Value

Type: Void

##### **`deleteFeedElement(communityId, feedElementId)`**

Delete a feed element.

API Version

31.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static deleteFeedElement(String communityId, String feedElementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

Return Value

Type: Void

##### **`deleteLike(communityId, likeId)`**

Delete a like on a comment or post.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static Void deleteLike(String communityId, String likeId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   likeId
```

Type: String

ID for a like.

Return Value

Type: Void

##### **`deleteStream(communityId, streamId)`**

Delete a Chatter feed stream.


Apex Reference Guide ChatterFeeds Class

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static Void deleteStream(String communityId, String streamId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   streamId
```

Type: String

ID of the Chatter feed stream.

Return Value

Type: Void

##### **`getComment(communityId, commentId)`**

Get a comment.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Comment getComment(String communityId, String commentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   commentId
```

Type: String

ID for a comment.

Return Value

Type: `ConnectApi.Comment`

##### **`getCommentBatch(communityId, commentIds)`**

Get a list of comments.

API Version

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] getCommentBatch(String communityId, List<String>

   commentIds)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentIds
```

Type: List<String>

A list of up to 100 comment IDs.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.Comment` object and errors for comments
that didn’t load.

##### **`getCommentInContext(communityId, commentId, pageSize)`**

Get a threaded comment in the context of its parent comments and post.

API Version

44.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getCommentInContext(String communityId, String

   commentId, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you don’t specify a value, the default size is 25.

Return Value

Type: `ConnectApi.FeedElement`

If the comment doesn’t support the `comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId)`**

Get comments for a feed element.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedElement(String communityId,

   String feedElementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId,`**

```
  threadedCommentsCollapsed)

```

Get comments in a threaded style for a feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedElement(String communityId,

   String feedElementId, Boolean threadedCommentsCollapsed)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID of the feed element.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId, pageParam, pageSize)`**

Get a page of comments for a feed element.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedElement(String communityId,

   String feedElementId, String pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of comments per page. Valid values are from 1 through 100. If you pass `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId, pageParam, pageSize,`**

```
  threadedCommentsCollapsed)

```

Get a page of comments in a threaded style for a feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedElement(String communityId,

   String feedElementId, String pageParam, Integer pageSize, Boolean

   threadedCommentsCollapsed)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of comments per page. Valid values are from 1 through 100. If you pass `null`, the default size is 25.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId,`**

```
  threadedCommentsCollapsed, sortParam)

```

Get sorted comments in a threaded style for a feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentsCapability getCommentsForFeedElement(String communityId,

   String feedElementId, Boolean threadedCommentsCollapsed, ConnectApi.FeedCommentSortOrder

   sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   sortParam
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments. Values are:

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.


Apex Reference Guide ChatterFeeds Class

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId, pageParam, pageSize,`**

```
  threadedCommentsCollapsed, sortParam)

```

Get a page of sorted comments in a threaded style for a feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedElement(String communityId,

   String feedElementId, String pageParam, Integer pageSize, Boolean

   threadedCommentsCollapsed, ConnectApi.FeedCommentSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of comments per page. Valid values are from 1 through 100. If you pass `null`, the default size is 25.

```
   threadedCommentsCollapsed
```

Type: Boolean


Apex Reference Guide ChatterFeeds Class

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   sortParam
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments. Values are:

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId, sortParam)`**

Get sorted comments for a feed element.

API Version

41.0

Available to Guest Users

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentsCapability getCommentsForFeedElement(String communityId,

   String feedElementId, ConnectApi.FeedCommentSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   sortParam
```

Type: `ConnectApi.FeedCommentSortOrder`


Apex Reference Guide ChatterFeeds Class

Order of comments. Values are:

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.CommentsCapability`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId, sortParam,`**

```
  threadedCommentsCollapsed)

```

Get sorted comments in a threaded style for a feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentsCapability getCommentsForFeedElement(String communityId,

   String feedElementId, ConnectApi.FeedCommentSortOrder sortParam, Boolean

   threadedCommentsCollapsed)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   sortParam
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments. Values are:

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.


Apex Reference Guide ChatterFeeds Class

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

Sorting in descending order isn’t supported.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.CommentsCapability`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getExtensions(communityId, pageParam, pageSize)`**

Get extensions.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ExtensionDefinitions getExtensions(String communityId, String

   pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. The default size is 15.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.ExtensionDefinitions`

##### **`getFeed(communityId, feedType)`**

Get a feed.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeed(String communityId, ConnectApi.FeedType feedType)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

Return Value

Type: `ConnectApi.Feed`

##### **`getFeed(communityId, feedType, sortParam)`**

Get a sorted feed.

API Version

28.0

Available to Guest Users

32.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeed(String communityId, ConnectApi.FeedType feedType,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

If _`feedType`_ is `DirectMessages`, _`sortParam`_ must be `LastModifiedDateDesc` .

Return Value

Type: `ConnectApi.Feed`

##### **`getFeed(communityId, feedType, subjectId)`**

Get a feed for a record or user.

API Version

28.0

Available to Guest Users

32.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeed(String communityId, ConnectApi.FeedType feedType,

   String subjectId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

Return Value

Type: `ConnectApi.Feed`

##### **`getFeed(communityId, feedType, subjectId, sortParam)`**

Get a sorted feed for a record or user.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeed(String communityId, ConnectApi.FeedType feedType,

   String subjectId, ConnectApi.FeedSortOrder sortParam)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.Feed`

##### **`getFeedDirectory(String)`**

Get a list of all feeds available to the context user.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedDirectory getFeedDirectory(String communityId)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.FeedDirectory`

##### **`getFeedElement(communityId, feedElementId)`**

Get a feed element.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, commentSort)`**

Get a feed element with sorted comments.


Apex Reference Guide ChatterFeeds Class

API Version

41.0

Available to Guest Users

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, ConnectApi.FeedCommentSortOrder commentSort)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   commentSort
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments.

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

The default value is `CreatedDateLatestAsc` .

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, threadedCommentsCollapsed)`**

Get a feed element and its comments in a threaded style.

API Version

44.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Boolean threadedCommentsCollapsed)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, threadedCommentsCollapsed,`**

```
  commentSort)

```

Get a feed element and its sorted comments in a threaded style.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Boolean threadedCommentsCollapsed, ConnectApi.FeedCommentSortOrder

   commentSort)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   commentSort
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments.

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, recentCommentCount,`**

```
  elementsPerBundle)

```

Get a feed element with the specified number of elements per bundle including no more than the specified number of comments per
feed element.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Integer recentCommentCount, Integer elementsPerBundle)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, recentCommentCount,`**

```
  elementsPerBundle, threadedCommentsCollapsed)

```

Get a feed element with its comments in a threaded style with the specified number of elements per bundle and comments per feed
element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Integer recentCommentCount, Integer elementsPerBundle, Boolean

   threadedCommentsCollapsed)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, recentCommentCount,`**

```
  elementsPerBundle, threadedCommentsCollapsed, commentSort)

```

Get a feed element with its sorted comments in a threaded style with the specified number of elements per bundle and comments per
feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Integer recentCommentCount, Integer elementsPerBundle, Boolean

   threadedCommentsCollapsed, ConnectApi.FeedCommentSortOrder commentSort)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   commentSort
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments.

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, recentCommentCount,`**

```
  elementsPerBundle, commentSort)

```

Get a feed element with the specified number of elements per bundle including no more than the specified number of sorted comments
per feed element.

API Version

41.0

Available to Guest Users

41.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedCommentSortOrder commentSort)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   commentSort
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments.

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

The default value is `CreatedDateLatestAsc` .

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElementBatch(communityId, feedElementIds)`**

Get a list of feed elements.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] getFeedElementBatch(String communityId,

   List<String> feedElementIds)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementIds
```

Type: List<String>

A list of up to 500 feed element IDs.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.FeedElement` object and errors for
feed elements that didn’t load.

##### **`getFeedElementPoll(communityId, feedElementId)`**

Get the poll associated with a feed element.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.PollCapability getFeedElementPoll(String communityId, String

   feedElementId)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

Return Value

Type: `ConnectApi.PollCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Note: Triggers on FeedItem objects run before their attachment and capabilities information is saved, which means that
`ConnectApi.FeedItem.attachment` information and `ConnectApi.FeedElement.capabilities` information
may not be available in the trigger.

##### **`getFeedElementsFromBundle(communityId, feedElementId)`**

Get feed elements from a bundle.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromBundle(String communityId,

   String feedElementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsFromBundle(communityId, feedElementId, pageParam, pageSize,`**

```
  elementsPerBundle, recentCommentCount)

```

Get a page of feed elements from a bundle. Specify the number of elements per bundle and include no more than the specified number
of comments per feed element.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromBundle(String communityId,

   String feedElementId, String pageParam, Integer pageSize, Integer elementsPerBundle,

   Integer recentCommentCount)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsFromFeed(communityId, feedType)`**

Get feed elements from the `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`, `Moderation`,
and `PendingReview` feeds.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam)`**

Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` feeds.


Apex Reference Guide ChatterFeeds Class

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.


Apex Reference Guide ChatterFeeds Class

If _`feedType`_ is `DirectMessages`, _`sortParam`_ must be `LastModifiedDateDesc` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam)

```

Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` feeds. Each feed element contains no more than the specified number of comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .


Apex Reference Guide ChatterFeeds Class

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

If _`feedType`_ is `DirectMessages`, _`sortParam`_ must be `LastModifiedDateDesc` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam, filter)

```

Get a page of sorted and filtered feed elements from the `Home` feed. Each feed element contains no more than the specified number
of comments.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedFilter filter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. The only valid value is `Home` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.


Apex Reference Guide ChatterFeeds Class

When the _`sortParam`_ is `MostViewed`, you must pass in `null` for the _`pageParam`_ .

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

When the _`sortParam`_ is `MostViewed`, the _`pageSize`_ must be a value from 1 to 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam, filter, threadedCommentsCollapsed)

```

Get a page of filtered and sorted feed elements with comments in a threaded style from the `Home` feed. Each feed element contains
no more than the specified number of comments.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedFilter filter, Boolean threadedCommentsCollapsed)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. The only valid value is `Home` .


Apex Reference Guide ChatterFeeds Class

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

When the _`sortParam`_ is `MostViewed`, you must pass in `null` for the _`pageParam`_ .

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

When the _`sortParam`_ is `MostViewed`, the _`pageSize`_ must be a value from 1 to 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.


Apex Reference Guide ChatterFeeds Class

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId)`**

Get feed elements from any feed other than `Company`, `DirectMessageModeration`, `DirectMessages`, `Filter`, `Home`,
`Isolated`, `Landing`, `Moderation`, and `PendingReview` for a user or record.

API Version

31.0

Available to Guest Users

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example for Getting the Context User’s News Feed

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.News, 'me');

```

Example for Getting Another User’s Profile Feed

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.UserProfile, '005R0000000HwMA');

```


Apex Reference Guide ChatterFeeds Class

Example for Getting Another User’s Record Feed

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.Record, '005R0000000HwMA');

```

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize,`**

```
  sortParam)

```

Get a page of sorted feed elements from any feed other than `Company`, `DirectMessageModeration`, `DirectMessages`,
`Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .


Apex Reference Guide ChatterFeeds Class

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

The number of feed elements per page.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam)

```

Get a page of sorted feed elements from any feed other than `Company`, `DirectMessageModeration`, `DirectMessages`,
`Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` . Each feed element includes no more than the
specified number of comments.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, showInternalOnly)

```

Get a page of sorted feed elements from a record feed. Each feed element includes no more than the specified number of comments.
Specify whether to return feed elements posted by internal (non-Experience Cloud site) users only.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.


Apex Reference Guide ChatterFeeds Class

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, filter)

```

Get a page of sorted and filtered feed elements from the `UserProfile` feed.

API Version

35.0

Available to Guest Users

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedFilter filter)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.UserProfile` .

```
   subjectId
```

Type: String

ID of any user. To specify the context user, use the user ID or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Value must be `ConnectApi.FeedFilter.CommunityScoped` or `ConnectApi.FeedFilter.AuthoredBy` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example gets only community-specific feed elements.

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.UserProfile, 'me', 3, ConnectApi.FeedDensity.FewerUpdates, null, null,

    ConnectApi.FeedSortOrder.LastModifiedDateDesc, ConnectApi.FeedFilter.CommunityScoped );

```

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, filter, threadedCommentsCollapsed)

```

Get a page of feed elements with comments in a threaded style from the `UserProfile` feed.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedFilter filter, Boolean

   threadedCommentsCollapsed)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.UserProfile` .

```
   subjectId
```

Type: String

ID of any user. To specify the context user, use the user ID or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Value must be `ConnectApi.FeedFilter.CommunityScoped` or `ConnectApi.FeedFilter.AuthoredBy` .

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, filter, threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, customFilter)

```

Get a page of sorted and filtered feed elements from the case feed.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String customFilter)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly)

```

Get a page of sorted feed elements from a record feed. Specify the number of elements per bundle and include no more than the
specified number of comments per feed element. Specify whether to return feed elements posted by internal (non-Experience Cloud
site) users only.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .


Apex Reference Guide ChatterFeeds Class

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

  filter)

```

Get a page of sorted and filtered feed elements from a record feed. Specify the number of elements per bundle and include no more
than the specified number of comments per feed element. Specify whether to return feed elements posted by internal (non-Experience
Cloud site) users only.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, ConnectApi.FeedFilter

   filter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`


Apex Reference Guide ChatterFeeds Class

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

  filter, threadedCommentsCollapsed)

```

Get a page of sorted and filtered feed elements with comments in a threaded style for a record feed. Specify the number of elements
per bundle and include no more than the specified number of comments per feed element. Specify whether to return feed elements
posted by internal (non-Experience Cloud site) users only.


Apex Reference Guide ChatterFeeds Class

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, ConnectApi.FeedFilter

   filter, Boolean threadedCommentsCollapsed)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String


Apex Reference Guide ChatterFeeds Class

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.


Apex Reference Guide ChatterFeeds Class

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

  customFilter)

```

Get a page of sorted and filtered feed elements from a case feed.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, String customFilter)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.


Apex Reference Guide ChatterFeeds Class

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

  customFilter, threadedCommentsCollapsed)

```

Get a page of filtered and sorted feed elements with comments in a threaded style from a case feed.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, String customFilter,

   Boolean threadedCommentsCollapsed)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.


Apex Reference Guide ChatterFeeds Class

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix)`**

Get feed elements from a feed filtered by a key prefix for a user.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFilterFeed(String

   communityId, String subjectId, String keyPrefix)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam,`**

```
  pageSize, sortParam)

```

Get a page of sorted feed elements from a feed filtered by a key prefix for a user.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFilterFeed(String

   communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam)

```

Get a page of sorted feed elements from a feed filtered by a key prefix for a user. Each feed element contains no more than the specified
number of comments.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFilterFeed(String

   communityId, String subjectId, String keyPrefix, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.


Apex Reference Guide ChatterFeeds Class

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince)

```

Get a page of feed elements from a feed filtered by a key prefix for a user. Include only feed elements that have been updated since the
time specified in the _`updatedSince`_ parameter.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFilterFeedUpdatedSince(String

   communityId, String subjectId, String keyPrefix, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

```
   updatedSince
```

Type: String

Opaque token defining the modification timestamp of the feed and the sort order.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle,
density, pageParam, pageSize, updatedSince, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince)

```

Get a page of feed elements from the `Company`, `DirectMessageModeration`, `Home`, and `Moderation` feeds. Include only
feed elements that have been updated since the time specified in the _`updatedSince`_ parameter. Each feed element contains no
more than the specified number of comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, String updatedSince)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, and `Moderation` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince,
result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince, filter)

```

Get a page of filtered feed elements from the `Home` feed. Include only feed elements that have been updated since the time specified
in the _`updatedSince`_ parameter. Each feed element contains no more than the specified number of comments.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, String updatedSince, ConnectApi.FeedFilter filter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. The only valid value is `Home` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.


Apex Reference Guide ChatterFeeds Class

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince,
filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince)

```

Get a page of feed elements from the `Files`, `Groups`, `News`, `People`, and `Record` feeds. Include only feed elements that have
been updated since the time specified in the _`updatedSince`_ parameter. Each feed element contains no more than the specified
number of comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

One of these values:

**•** `Files`

**•** `Groups`

**•** `News`

**•** `People`


Apex Reference Guide ChatterFeeds Class

**•** `Record`

```
   subjectId
```

Type: String

If _`feedType`_ is `ConnectApi.Record`, _`subjectId`_ can be any record ID, including a group ID. Otherwise, it must be the
context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince,

  showInternalOnly)

```

Get a page of feed elements from a record feed. Include only feed elements that have been updated since the time specified in the
_`updatedSince`_ parameter. Specify whether to return feed elements posted by internal (non-Experience Cloud site) users only.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince,

   Boolean showInternalOnly)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.


Apex Reference Guide ChatterFeeds Class

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, filter)

```

Get a page of filtered feed elements from a `UserProfile` feed. Include only feed elements that have been updated since the time
specified in the _`updatedSince`_ parameter.

API Version

35.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, ConnectApi.FeedFilter filter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.UserProfile` .

```
   subjectId
```

Type: String

ID of any user. To specify the context user, use the user ID or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

Opaque token defining the modification timestamp of the feed and the sort order.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Value must be `ConnectApi.FeedFilter.CommunityScoped` . Filters the feed to include only feed elements that are
scoped to Experience Cloud sites. Feed elements that are always visible in all sites are filtered out.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, customFilter)

```

Get a page of filtered feed elements from a case feed. Include only feed elements that have been updated since the time specified in
the _`updatedSince`_ parameter.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

```


Apex Reference Guide ChatterFeeds Class

```
   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, String customFilter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

Opaque token defining the modification timestamp of the feed and the sort order.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, showInternalOnly)

```

Get a page of feed elements from a record feed. Include only feed elements that have been updated since the time specified in the
_`updatedSince`_ parameter. Specify the maximum number of feed elements in a bundle and whether to return feed elements posted
by internal (non-Experience Cloud site) users only.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, Boolean showInternalOnly)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .


Apex Reference Guide ChatterFeeds Class

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, showInternalOnly, filter)

```

Get a page of filtered feed elements from a record feed. Include only feed elements that have been updated since the time specified in
the _`updatedSince`_ parameter. Specify the maximum number of feed elements in a bundle and whether to return feed elements
posted by internal (non-Experience Cloud site) users only.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, Boolean showInternalOnly, ConnectApi.FeedFilter filter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.


Apex Reference Guide ChatterFeeds Class

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.


Apex Reference Guide ChatterFeeds Class

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, showInternalOnly, customFilter)

```

Get a page of filtered feed elements from a case feed. Include only feed elements that have been updated since the time specified in
the _`updatedSince`_ parameter.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, Boolean showInternalOnly, String customFilter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.


Apex Reference Guide ChatterFeeds Class

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedWithFeedElements(communityId, feedType, pageSize)`**

Get information about a feed and a page of feed elements from the feed.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeedWithFeedElements(String communityId,

   ConnectApi.FeedType feedType, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Landing`, `Moderation`, and `PendingReview` . `Landing` is valid only when _`communityId`_ is `internal` .

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in 0, feed elements aren’t returned
with the feed.

Return Value

Type: `ConnectApi.Feed`

##### **`getFeedWithFeedElements(communityId, feedType, pageSize, recentCommentCount)`**

Get a page of information about the feed and the feed elements with the specified number of comments per feed element from the
feed.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeedWithFeedElements(String communityId,

   ConnectApi.FeedType feedType, Integer pageSize, Integer recentCommentCount)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Landing`, `Moderation`, and `PendingReview` . `Landing` is valid only when _`communityId`_ is `internal` .

```
   pageSize
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in 0, feed elements aren’t returned
with the feed.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

Return Value

Type: `ConnectApi.Feed`

##### **`getFilterFeed(communityId, subjectId, keyPrefix)`**

Get a feed filtered by a key prefix for a user.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFilterFeed(String communityId, String subjectId, String

   keyPrefix)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A _key prefix_ is the first three characters of a record ID, which specifies the object type.

Return Value

Type: `ConnectApi.Feed`

##### **`getFilterFeed(communityId, subjectId, keyPrefix, sortParam)`**

Get a sorted feed filtered by a key prefix for a user.


Apex Reference Guide ChatterFeeds Class

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFilterFeed(String communityId, String subjectId, String

   keyPrefix, ConnectApi.FeedType sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   sortParam
```

Type: `ConnectApi.FeedType`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.Feed`

##### **`getFilterFeedDirectory(communityId, subjectId)`**

Get a feed directory of filter feeds available to the context user.


Apex Reference Guide ChatterFeeds Class

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedDirectory getFilterFeedDirectory(String communityId, String

   subjectId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

Return Value

Type: `ConnectApi.FeedDirectory`

This feed directory contains a list of filter feeds, which are the news feed filtered to include feed items whose parent is a specific entity
type.

Usage

Call this method to return a directory containing a list of `ConnectApi.FeedDirectoryItem` objects. Each object contains a
key prefix associated with an entity type the context user is following. A _key prefix_ is the first three characters of a record ID, which specifies
the object type.

Use key prefixes to filter the news feed so that it contains only feed items whose parent is the entity type associated with the key prefix.
For example, get all the feed items whose parent is an Account. To get the feed items, pass a key prefix to the
`ConnectApi.getFeedItemsFromFilterFeed` method.

The information about filter feeds never contains the key prefixes for users ( `005` ) or groups ( `0F9` ), but all users can use those key prefixes
as filters.

The `ConnectApi.FeedDirectory.favorites` property is always empty when returned by a call to
`getFilterFeedDirectory` because you can’t filter a news feed by favorites.

Example

This example calls `getFilterFeedDirectory` and loops through the returned `FeedDirectoryItem` objects to find the
key prefixes the context user can use to filter their news feed. It then copies each `keyPrefix` value to a list. Finally, it passes one of


Apex Reference Guide ChatterFeeds Class

the key prefixes from the list to the `getFeedItemsFromFilterFeed` method. The returned feed items include every feed item
from the news feed whose parent is the entity type specified by the passed key prefix.

```
   String communityId = null;

   String subjectId = 'me';

   // Create a list to populate with key prefixes.

   List<String> keyPrefixList = new List<String>();

   // Prepopulate with User and Group record types

   // which are available to all users.

   keyPrefixList.add('005');

   keyPrefixList.add('0F9');

   System.debug(keyPrefixList);

   // Get the key prefixes available to the context user.

   ConnectApi.FeedDirectory myFeedDirectory =

     ConnectApi.ChatterFeeds.getFilterFeedDirectory(null, 'me');

   // Loop through the returned feeds list.

   for (ConnectApi.FeedDirectoryItem i : myFeedDirectory.feeds) {

     // Grab each key prefix and add it to the list.

     keyPrefixList.add(i.keyPrefix);

   }

   System.debug(keyPrefixList);

   // Use a key prefix from the list to filter the feed items in the news feed.

   ConnectApi.FeedItemPage myFeedItemPage =

     ConnectApi.ChatterFeeds.getFeedItemsFromFilterFeed(communityId, subjectId,

   keyPrefixList[0]);

   System.debug(myFeedItemPage);

##### **`getLike(communityId, likeId)`**

```

Get a like on a post or comment.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLike getLike(String communityId, String likeId)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   likeId
```

Type: String

ID for a like.

Return Value

Type: `ConnectApi.ChatterLike`

##### **`getLikesForComment(communityId, commentId)`**

Get likes for a comment.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage getLikesForComment(String communityId, String

   commentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

Return Value

Type: `ConnectApi.ChatterLikePage`


Apex Reference Guide ChatterFeeds Class

##### **`getLikesForComment(communityId, commentId, pageParam, pageSize)`**

Get a page of likes for a comment.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage getLikesForComment(String communityId, String

   commentId, Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ChatterLikePage`

##### **`getLikesForFeedElement(communityId, feedElementId)`**

Get likes for a feed element.

API Version

32.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage getLikesForFeedElement(String communityId,

   String feedElementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

Return Value

Type: `ConnectApi.ChatterLikePage`

If the feed element doesn’t support the `ChatterLikes` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getLikesForFeedElement(communityId, feedElementId, pageParam, pageSize)`**

Get a page of likes for a feed element.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage getLikesForFeedElement(String communityId,

   String feedElementId, Integer pageParam, Integer pageSize)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ChatterLikePage`

If the feed element doesn’t support the `ChatterLikes` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getLinkMetadata(communityId, urls)`**

Get link metadata for URLs.

API Version

42.0

Available to Guest Users

42.0

Requires Chatter

No

Signature

```
   public static ConnectApi.LinkMetadataCollection getLinkMetadata(String communityId,

   String urls)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   urls
```

Type: String

Comma-separated list of URL-encoded URLs.

Return Value

Type: `ConnectApi.LinkMetadataCollection`

##### **`getPinnedFeedElementsFromFeed(communityId, feedType, subjectId)`**

Get pinned feed elements from a group or topic feed.

API Version

41.0

Available to Guest Users

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.PinnedFeedElements getPinnedFeedElementsFromFeed(String

   communityId, ConnectApi.FeedType feedType, String subjectId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. Valid values are `Record` and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ must be a group ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID.

Return Value

Type: `ConnectApi.PinnedFeedElements`

If the feed doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .


Apex Reference Guide ChatterFeeds Class

Usage

In the UI, pinned feed elements don’t show all auxiliary information, such as comments, likes, interaction counts, or read by information.
As a result, the `ConnectApi.PinnedFeedElements` output class doesn’t include all the information for these capabilities.

##### **`getReadByForFeedElement(communityId, feedElementId)`**

Get information about who read a feed element and when.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ReadByPage getReadByForFeedElement(String communityId, String

   feedElementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

Return Value

Type: `ConnectApi.ReadByPage`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`getReadByForFeedElement(communityId, feedElementId, pageParam, pageSize)`**

Get a page of information about who read a feed element and when.

API Version

40.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.ReadByPage getReadByForFeedElement(String communityId, String

   feedElementId, Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ReadByPage`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`getRelatedPosts(communityId, feedElementId, filter, maxResults)`**

Get posts related to the context feed element.

API Version

37.0

Available to Guest Users

37.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RelatedFeedPosts getRelatedPosts(String communityId, String

   feedElementId, ConnectApi.RelatedFeedPostType filter, Integer maxResults)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element. The feed element must be a question.

```
   filter
```

Type: `ConnectApi.RelatedFeedPostType`

Specifies the type of related post. Values are:

**•** `Answered` —Related questions that have at least one answer.

**•** `BestAnswer` —Related questions that have a best answer.

**•** `Generic` —All types of related questions, including answered, with a best answer, and unanswered.

**•** `Unanswered` —Related questions that don’t have answers.

`Generic` is the default value.

```
   maxResults
```

Type: Integer

The maximum number of results to return. You can return up to 25 results; 5 is the default.

Return Value

Type: `ConnectApi.RelatedFeedPosts`

In version 37.0 and later, related feed posts are questions.

Each related feed post has a score indicating how closely it’s related to the context feed post. We return related feed posts sorted by
score, with the highest score first.

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

##### **`getStream(communityId, streamId)`**

Get information about a Chatter feed stream.

API Version

39.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.ChatterStream getStream(String communityId, String streamId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   streamId
```

Type: String

ID of the Chatter feed stream.

Return Value

Type: `ConnectApi.ChatterStream`

##### **`getStream(communityId, streamId, globalScope)`**

Get information about a Chatter feed stream, regardless of Experience Cloud site.

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStream getStream(String communityId, String streamId,

   Boolean globalScope)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   streamId
```

Type: String

ID of the Chatter feed stream.

```
   globalScope
```

Type: Boolean

Specifies whether to get streams from all the context user’s Experience Cloud sites, regardless of the _`communityId`_ value.

Tip: If you know the _`communityId`_ for the stream, we recommend setting _`globalScope`_ to `false` .


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.ChatterStream`

##### **`getStreams(communityId)`**

Get the Chatter feed streams for the context user.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage getStreams(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.ChatterStreamPage`

##### **`getStreams(communityId, sortParam)`**

Get and sort the Chatter feed streams for the context user.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage getStreams(String communityId,

   ConnectApi.SortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   sortParam
```

Type: `ConnectApi.SortOrder`

Specifies the sort order. Values are:

**•** `Ascending` —Items are in ascending alphabetical order (A-Z).

**•** `Descending` —Items are in descending alphabetical order (Z-A).

**•** `MostRecentlyViewed` —Items are in descending chronological order by view. This sort order is valid only for Chatter feed
streams.

If not specified, default value is `Ascending` .

Return Value

Type: `ConnectApi.ChatterStreamPage`

##### **`getStreams(communityId, pageParam, pageSize)`**

Get a page of Chatter feed streams for the context user.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage getStreams(String communityId, Integer

   pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 to 250. The default size is 25.

Return Value

Type: `ConnectApi.ChatterStreamPage`


Apex Reference Guide ChatterFeeds Class

##### **`getStreams(communityId, pageParam, pageSize, sortParam)`**

Get a sorted page of Chatter feed streams for the context user.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage getStreams(String communityId, Integer

   pageParam, Integer pageSize, ConnectApi.SortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 to 250. The default size is 25.

```
   sortParam
```

Type: `ConnectApi.SortOrder`

Specifies the sort order. Values are:

**•** `Ascending` —Items are in ascending alphabetical order (A-Z).

**•** `Descending` —Items are in descending alphabetical order (Z-A).

**•** `MostRecentlyViewed` —Items are in descending chronological order by view. This sort order is valid only for Chatter feed
streams.

If not specified, default value is `Ascending` .

Return Value

Type: `ConnectApi.ChatterStreamPage`

##### **`getStreams(communityId, pageParam, pageSize, sortParam, globalScope)`**

Get a sorted page of Chatter feed streams from all Enterprise Cloud sites for the context user.


Apex Reference Guide ChatterFeeds Class

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage getStreams(String communityId, Integer

   pageParam, Integer pageSize, ConnectApi.SortOrder sortParam, Boolean globalScope)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 to 250. The default size is 25.

```
   sortParam
```

Type: `ConnectApi.SortOrder`

Specifies the sort order. Values are:

**•** `Ascending` —Items are in ascending alphabetical order (A-Z).

**•** `Descending` —Items are in descending alphabetical order (Z-A).

**•** `MostRecentlyViewed` —Items are in descending chronological order by view. This sort order is valid only for Chatter feed
streams.

If not specified, default value is `Ascending` .

```
   globalScope
```

Type: Boolean

Specifies whether to get streams from all the context user’s Experience Cloud sites, regardless of the _`communityId`_ value.

Tip: If you know the _`communityId`_ for the streams, we recommend setting _`globalScope`_ to `false` .

Return Value

Type: `ConnectApi.ChatterStreamPage`

##### **`getSupportedEmojis()`**

Get supported emojis for the org.


Apex Reference Guide ChatterFeeds Class

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.SupportedEmojis getSupportedEmojis()

```

Return Value

Type: `ConnectApi.SupportedEmojis`

Usage

To get the list, emojis must be enabled in your org.

##### **`getThreadsForFeedComment(communityId, commentId)`**

Get threaded comments for a comment.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getThreadsForFeedComment(String communityId, String

   commentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.CommentPage`

If the comment doesn’t support the `comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getThreadsForFeedComment(communityId, commentId, pageParam, pageSize)`**

Get a page of threaded comments for a comment.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getThreadsForFeedComment(String communityId, String

   commentId, String pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment.

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.CommentPage`

If the comment doesn’t support the `comments` capability, the return value is `ConnectApi.NotFoundException` .


Apex Reference Guide ChatterFeeds Class

##### **`getThreadsForFeedComment(communityId, commentId, threadedCommentsCollapsed)`**

Access the comments capability for a comment.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentsCapability getThreadsForFeedComment(String communityId,

   String commentId, Boolean threadedCommentsCollapsed)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.CommentsCapability`

If the comment doesn’t support the `comments` capability, the return value is `ConnectApi.NotFoundException` .

##### getTopUnansweredQuestions(communityId) (Pilot)

Get top unanswered questions for the context user in aExperience Cloud site.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getTopUnansweredQuestions(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopUnansweredQuestions(communityId, result) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### getTopUnansweredQuestions(communityId, filter) (Pilot)

Get filtered top unanswered questions for the context user in an Experience Cloud site.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getTopUnansweredQuestions(String communityId,

   ConnectApi.TopUnansweredQuestionsFilterType filter)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the filter for the feed. `UnansweredQuestionsWithCandidateAnswers` is the only valid value.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopUnansweredQuestions(communityId, filter, result) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### getTopUnansweredQuestions(communityId, pageSize) (Pilot)

Get a page of top unanswered questions for the context user in an Experience Cloud site.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getTopUnansweredQuestions(String communityId,

   Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   pageSize
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Specifies the number of items per page. Valid values are from 0 through 10. If you pass in `null`, the default size is 5.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopUnansweredQuestions(communityId, pageSize, result) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### getTopUnansweredQuestions(communityId, filter, pageSize) (Pilot)

Get a page of filtered top unanswered questions for the context user in an Experience Cloud site.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getTopUnansweredQuestions(String communityId,

   ConnectApi.FeedFilter filter, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the filter for the feed. `UnansweredQuestionsWithCandidateAnswers` is the only valid value.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 0 through 10. If you pass in `null`, the default size is 5.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopUnansweredQuestions(communityId, filter, pageSize, result) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getVotesForComment(communityId, commentId, vote)`**

Get the first page of users who upvoted or downvoted a comment.

API Version

42.0

Available to Guest Users

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VotePage getVotesForComment(String communityId, String

   commentId, ConnectApi.UpDownVoteValue vote)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment.

```
   vote
```

Type: `ConnectApi.UpDownVoteValue`

Specifies the value of the vote for the feed element. Values are:

**•** `Down`

**•** `Up`


Apex Reference Guide ChatterFeeds Class

You can’t specify `None` .

Return Value

Type: `ConnectApi.VotePage`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`getVotesForComment(communityId, commentId, vote, pageParam, pageSize)`**

Get a page of users who upvoted or downvoted a comment.

API Version

42.0

Available to Guest Users

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VotePage getVotesForComment(String communityId, String

   commentId, ConnectApi.UpDownVoteValue vote, Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment.

```
   vote
```

Type: `ConnectApi.UpDownVoteValue`

Specifies the value of the vote for the feed element. Values are:

**•** `Down`

**•** `Up`

You can’t specify `None` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.


Apex Reference Guide ChatterFeeds Class

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.VotePage`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`getVotesForFeedElement(communityId, feedElementId, vote)`**

Get the first page of users who upvoted or downvoted a feed element.

API Version

42.0

Available to Guest Users

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VotePage getVotesForFeedElement(String communityId, String

   feedElementId, ConnectApi.UpDownVoteValue vote)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   vote
```

Type: `ConnectApi.UpDownVoteValue`

Specifies the value of the vote for the feed element. Values are:

**•** `Down`

**•** `Up`

You can’t specify `None` .


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.VotePage`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`getVotesForFeedElement(communityId, feedElementId, vote, pageParam, pageSize)`**

Get a page of users who upvoted or downvoted a feed element.

API Version

42.0

Available to Guest Users

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VotePage getVotesForFeedElement(String communityId, String

   feedElementId, ConnectApi.UpDownVoteValue vote, Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   vote
```

Type: `ConnectApi.UpDownVoteValue`

Specifies the value of the vote for the feed element. Values are:

**•** `Down`

**•** `Up`

You can’t specify `None` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.VotePage`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`isCommentEditableByMe(communityId, commentId)`**

Discover whether the context user can edit a comment.

API Version

34.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedEntityIsEditable isCommentEditableByMe(String communityId,

   String commentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment.

Return Value

Type: `ConnectApi.FeedEntityIsEditable`

If the comment doesn’t support the `edit` capability, the return value is `ConnectApi.NotFoundException` .

SEE ALSO:

[Edit a Comment](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_comment.htm)

##### **`isFeedElementEditableByMe(communityId, feedElementId)`**

Discover whether the context user can edit a feed element.

API Version

34.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedEntityIsEditable isFeedElementEditableByMe(String

   communityId, String feedElementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element. Feed items are the only type of feed element that can be edited.

Return Value

Type: `ConnectApi.FeedEntityIsEditable`

If the feed element doesn’t support the `edit` capability, the return value is `ConnectApi.NotFoundException` .

SEE ALSO:

[Edit a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_feed_element.htm)

[Edit a Question Title and Post](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_question_title_post.htm)

##### **`isModified(communityId, feedType, subjectId, since)`**

Discover whether a news feed has been updated or changed. Use this method to poll a news feed for updates.

Important: This feature is available through a Feed Polling pilot program. This pilot program is closed and not accepting new
participants.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedModifiedInfo isModified(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String since)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Specifies the type of feed. The only supported type is `News`

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   since
```

Type: String

An opaque token containing information about the last modified date of the feed. Retrieve this token from the
`FeedElementPage.isModifiedToken` property.

Return Value

Type: `ConnectApi.FeedModifiedInfo`

##### **`likeComment(communityId, commentId)`**

Like a comment for the context user.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLike likeComment(String communityId, String commentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.ChatterLike`

If the context user has already liked the comment, this method is a non-operation and returns the existing like.

##### **`likeFeedElement(communityId, feedElementId)`**

Like a feed element.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLike likeFeedElement(String communityId, String

   feedElementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

Return Value

Type: `ConnectApi.ChatterLike`

If the feed element doesn’t support the `ChatterLikes` capability, the return value is `ConnectApi.NotFoundException` .

Example

```
   ConnectApi.ChatterLike chatterLike = ConnectApi.ChatterFeeds.likeFeedElement(null,

   '0D5D0000000KuGh');

##### **`postCommentToFeedElement(communityId, feedElementId, text)`**

```

Post a plain-text comment to a feed element.

API Version

32.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Comment postCommentToFeedElement(String communityId, String

   feedElementId, String text)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   text
```

Type: String

Text of the comment. A comment can contain up to 10,000 characters.

Return Value

Type: `ConnectApi.Comment`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

Example

```
   ConnectApi.Comment comment = ConnectApi.ChatterFeeds.postCommentToFeedElement(null,

   '0D5D0000000KuGh', 'I agree with the proposal.' );

##### **`postCommentToFeedElement(communityId, feedElementId, comment,`**

  feedElementFileUpload)

```

Post a rich-text comment to a feed element. Use this method to include mentions and to attach a file.

API Version

32.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.Comment postCommentToFeedElement(String communityId, String

   feedElementId, ConnectApi.CommentInput comment, ConnectApi.BinaryInput

   feedElementFileUpload)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   comment
```

Type: `ConnectApi.CommentInput`

The comment body, including text and mentions, and capabilities, such as information about an attached file. A comment can
contain up to 10,000 characters.

```
   feedElementFileUpload
```

Type: `ConnectApi.BinaryInput`

A new binary file to attach to the comment, or `null` . If you specify a binary file, specify the title and description of the file in the
_`comment`_ parameter.

Return Value

Type: `ConnectApi.Comment`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

Example for Posting a Comment with Mentions

[You can post comments with mentions two ways. Use the ConnectApiHelper repository on GitHub to write a single line of code, or use](https://github.com/forcedotcom/ConnectApiHelper)
this method example.

```
   String communityId = null;

   String feedElementId = '0D5D0000000KtW3';

   ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

   ConnectApi.MentionSegmentInput mentionSegmentInput = new ConnectApi.MentionSegmentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   textSegmentInput.text = 'Does anyone in this group have an idea? ';

   messageBodyInput.messageSegments.add(textSegmentInput);

   mentionSegmentInput.id = '005D00000000oOT';

   messageBodyInput.messageSegments.add(mentionSegmentInput);

```


Apex Reference Guide ChatterFeeds Class

```
   commentInput.body = messageBodyInput;

   ConnectApi.Comment commentRep = ConnectApi.ChatterFeeds.postCommentToFeedElement(communityId,

    feedElementId, commentInput, null);

```

Example for Posting a Comment with an Existing File

```
   String feedElementId = '0D5D0000000KtW3';

   ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'I attached this file from Salesforce Files.';

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   commentInput.body = messageBodyInput;

   ConnectApi.CommentCapabilitiesInput commentCapabilitiesInput = new

   ConnectApi.CommentCapabilitiesInput();

   ConnectApi.ContentCapabilityInput contentCapabilityInput = new

   ConnectApi.ContentCapabilityInput();

   commentCapabilitiesInput.content = contentCapabilityInput;

   contentCapabilityInput.contentDocumentId = '069D00000001rNJ';

   commentInput.capabilities = commentCapabilitiesInput;

   ConnectApi.Comment commentRep =

   ConnectApi.ChatterFeeds.postCommentToFeedElement(Network.getNetworkId(), feedElementId,

   commentInput, null);

```

Example for Posting a Comment with a New File

```
   String feedElementId = '0D5D0000000KtW3';

   ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Enjoy this new file.';

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   commentInput.body = messageBodyInput;

   ConnectApi.CommentCapabilitiesInput commentCapabilitiesInput = new

   ConnectApi.CommentCapabilitiesInput();

   ConnectApi.ContentCapabilityInput contentCapabilityInput = new

```


Apex Reference Guide ChatterFeeds Class

```
   ConnectApi.ContentCapabilityInput();

   commentCapabilitiesInput.content = contentCapabilityInput;

   contentCapabilityInput.title = 'Title';

   commentInput.capabilities = commentCapabilitiesInput;

   String text = 'These are the contents of the new file.';

   Blob myBlob = Blob.valueOf(text);

   ConnectApi.BinaryInput binInput = new ConnectApi.BinaryInput(myBlob, 'text/plain',

   'fileName');

   ConnectApi.Comment commentRep =

   ConnectApi.ChatterFeeds.postCommentToFeedElement(Network.getNetworkId(), feedElementId,

   commentInput, binInput);

```

Example for Posting a Rich-Text Comment with an Inline Image

[You can post rich-text comments with inline images and mentions two ways. Use the ConnectApiHelper repository on GitHub to write](https://github.com/forcedotcom/ConnectApiHelper)
a single line of code, or use this method example. In this example, the image file is existing content that has already been uploaded to
Salesforce.

```
   String communityId = null;

   String feedElementId = '0D5R0000000SBEr';

   String imageId = '069R00000000IgQ';

   String mentionedUserId = '005R0000000DiMz';

   ConnectApi.CommentInput input = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MentionSegmentInput mentionSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   ConnectApi.InlineImageSegmentInput inlineImageSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = 'Hello ';

   messageInput.messageSegments.add(textSegment);

   mentionSegment = new ConnectApi.MentionSegmentInput();

   mentionSegment.id = mentionedUserId;

   messageInput.messageSegments.add(mentionSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = '!';

   messageInput.messageSegments.add(textSegment);

```


Apex Reference Guide ChatterFeeds Class

```
   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupEndSegment);

   inlineImageSegment = new ConnectApi.InlineImageSegmentInput();

   inlineImageSegment.altText = 'image one';

   inlineImageSegment.fileId = imageId;

   messageInput.messageSegments.add(inlineImageSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postCommentToFeedElement(communityId, feedElementId, input, null);

```

Example for Posting a Rich-Text Comment with a Code Block

```
   String communityId = null;

   String feedElementId = '0D5R0000000SBEr';

   String codeSnippet = '<html>\n\t<body>\n\t\tHello, world!\n\t</body>\n</html>';

   ConnectApi.CommentInput input = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = codeSnippet;

   messageInput.messageSegments.add(textSegment);

   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupEndSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postCommentToFeedElement(communityId, feedElementId, input, null);

##### **`postFeedElement(communityId, subjectId, feedElementType, text)`**

```

Post a plain-text feed element.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement postFeedElement(String communityId, String

   subjectId, ConnectApi.FeedElementType feedElementType, String text)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

The ID of the parent this feed element is being posted to. This value can be the ID of a user, group, or record, or the string `me` to
indicate the context user.

```
   feedElementType
```

Type: `ConnectApi.FeedElementType`

The only possible value is `FeedItem` .

```
   text
```

Type: String

The text of the feed element. A feed element can contain up to 10,000 characters.

Return Value

Type: `ConnectApi.FeedElement`

Example

```
   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), '0F9d0000000TreH',

   ConnectApi.FeedElementType.FeedItem, 'On vacation this week.');

##### **`postFeedElement(communityId, feedElement)`**

```

Post a rich-text feed element. Include mentions and hashtag topics, attach already uploaded files to a feed element, and associate action
link groups with a feed element. You can also use this method to share a feed element and add a comment.

API Version

36.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElement postFeedElement(String communityId,

   ConnectApi.FeedElementInput feedElement)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElement
```

Type: `ConnectApi.FeedElementInput`

Specify rich text, including mentions. Optionally, specify a link, a poll, or up to 10 existing files.

Return Value

Type: `ConnectApi.FeedElement`

Example for Posting a Feed Element with a Mention

[You can post feed elements with mentions two ways. Use the ConnectApiHelper repository on GitHub to write a single line of code, or](https://github.com/forcedotcom/ConnectApiHelper)
use this method example.

```
   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   ConnectApi.MentionSegmentInput mentionSegmentInput = new ConnectApi.MentionSegmentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   mentionSegmentInput.id = '005RR000000Dme9';

   messageBodyInput.messageSegments.add(mentionSegmentInput);

   textSegmentInput.text = 'Could you take a look?';

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   feedItemInput.feedElementType = ConnectApi.FeedElementType.FeedItem;

   feedItemInput.subjectId = '0F9RR0000004CPw';

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

```

Example for Posting a Feed Element with Existing Content

```
   // Define the FeedItemInput object to pass to postFeedElement

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   feedItemInput.subjectId = 'me';

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Would you please review these docs?';

```


Apex Reference Guide ChatterFeeds Class

```
   // The MessageBodyInput object holds the text in the post

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   // The FeedElementCapabilitiesInput object holds the capabilities of the feed item.

   // For this feed item, we define a files capability to hold the file(s).

   List<String> fileIds = new List<String>();

   fileIds.add('069xx00000000QO');

   fileIds.add('069xx00000000QT');

   fileIds.add('069xx00000000Qn');

   fileIds.add('069xx00000000Qi');

   fileIds.add('069xx00000000Qd');

   ConnectApi.FilesCapabilityInput filesInput = new ConnectApi.FilesCapabilityInput();

   filesInput.items = new List<ConnectApi.FileIdInput>();

   for (String fileId : fileIds) {

      ConnectApi.FileIdInput idInput = new ConnectApi.FileIdInput();

      idInput.id = fileId;

      filesInput.items.add(idInput);

   }

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   feedElementCapabilitiesInput.files = filesInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

```

Example for Posting a Rich-Text Feed Element with an Inline Image

[You can post rich-text feed elements with inline images and mentions two ways. Use the ConnectApiHelper repository on GitHub to](https://github.com/forcedotcom/ConnectApiHelper)
write a single line of code, or use this method example. In this example, the image file is existing content that has already been uploaded
to Salesforce. The post also includes text and a mention.

```
   String communityId = null;

   String imageId = '069D00000001INA';

   String mentionedUserId = '005D0000001QNpr';

   String targetUserOrGroupOrRecordId = '005D0000001Gif0';

   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   input.subjectId = targetUserOrGroupOrRecordId;

   input.feedElementType = ConnectApi.FeedElementType.FeedItem;

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MentionSegmentInput mentionSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

```


Apex Reference Guide ChatterFeeds Class

```
   ConnectApi.InlineImageSegmentInput inlineImageSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = 'Hello ';

   messageInput.messageSegments.add(textSegment);

   mentionSegment = new ConnectApi.MentionSegmentInput();

   mentionSegment.id = mentionedUserId;

   messageInput.messageSegments.add(mentionSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = '!';

   messageInput.messageSegments.add(textSegment);

   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupEndSegment);

   inlineImageSegment = new ConnectApi.InlineImageSegmentInput();

   inlineImageSegment.altText = 'image one';

   inlineImageSegment.fileId = imageId;

   messageInput.messageSegments.add(inlineImageSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postFeedElement(communityId, input);

```

Example for Posting a Rich-Text Feed Element with a Code Block

```
   String communityId = null;

   String targetUserOrGroupOrRecordId = 'me';

   String codeSnippet = '<html>\n\t<body>\n\t\tHello, world!\n\t</body>\n</html>';

   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   input.subjectId = targetUserOrGroupOrRecordId;

   input.feedElementType = ConnectApi.FeedElementType.FeedItem;

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

```


Apex Reference Guide ChatterFeeds Class

```
   textSegment.text = codeSnippet;

   messageInput.messageSegments.add(textSegment);

   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupEndSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postFeedElement(communityId, input);

```

Example for Sharing a Feed Element (in Version 39.0 and Later)

```
   // Define the FeedItemInput object to pass to postFeedElement

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   feedItemInput.subjectId = 'me';

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Look at this post I'm sharing.';

   // The MessageBodyInput object holds the text in the post

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   ConnectApi.FeedEntityShareCapabilityInput shareInput = new

   ConnectApi.FeedEntityShareCapabilityInput();

   shareInput.feedEntityId = '0D5R0000000SEbc';

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   feedElementCapabilitiesInput.feedEntityShare = shareInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

```

Example for Sending a Direct Message

```
   // Define the FeedItemInput object to pass to postFeedElement

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Thanks for attending my presentation test run this morning. Send

    me any feedback.';

   // The MessageBodyInput object holds the text in the post

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   // The FeedElementCapabilitiesInput object holds the capabilities of the feed item.

   // For this feed item, we define a direct message capability to hold the member(s) and the

    subject.

```


Apex Reference Guide ChatterFeeds Class

```
   List<String> memberIds = new List<String>();

   memberIds.add('005B00000016OUQ');

   memberIds.add('005B0000001rIN6');

   ConnectApi.DirectMessageCapabilityInput dmInput = new

   ConnectApi.DirectMessageCapabilityInput();

   dmInput.subject = 'Thank you!';

   dmInput.membersToAdd = memberIds;

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   feedElementCapabilitiesInput.directMessage = dmInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

##### **`postFeedElementBatch(communityId, feedElements)`**

```

Post a list of feed elements.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] postFeedElementBatch(String communityId,

   List<ConnectApi.BatchInput> feedElements)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElements
```

Type: List< `ConnectApi.BatchInput`       

The list can contain up to 500 `ConnectApi.BatchInput` objects. In the `ConnectApi.BatchInput` constructor, the
input object must be a concrete instance of the abstract `ConnectApi.FeedElementInput` class.

Return Value

Type: `ConnectApi.BatchResult` []


Apex Reference Guide ChatterFeeds Class

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.FeedElement` object.

The returned objects correspond to each of the input objects and are returned in the same order as the input objects.

The method call fails only if an error occurs that affects the entire operation (such as a parsing failure). If an individual object causes an
error, the error is embedded within the `ConnectApi.BatchResult` list.

Usage

Use this method to post a list of feed elements efficiently. Create a list containing up to 500 objects and insert them all for the cost of
one DML statement.

In version 36.0 and later, you can attach only one already uploaded file to each post. The `ConnectApi.BatchInput` has three
constructors, but the `postFeedElementBatch` method supports only `ConnectApi.BatchInput(Object input)`
in version 35.0 and later. This constructor doesn’t support a binary input.

In version 32.0–35.0, this method supports both `ConnectApi.BatchInput(Object input)` and
`ConnectApi.BatchInput(Object input, ConnectApi.BinaryInput binary)` constructors. The
`ConnectApi.BatchInput(Object input, ConnectApi.BinaryInput binary)` constructor allows for a single
binary input.

In each constructor, the input object must be an instance of `ConnectApi.FeedElementInput` .

Example

This trigger bulk posts to the feeds of newly inserted accounts.

```
   trigger postFeedItemToAccount on Account (after insert) {

      Account[] accounts = Trigger.new;

      // Bulk post to the account feeds.

      List<ConnectApi.BatchInput> batchInputs = new List<ConnectApi.BatchInput>();

      for (Account a : accounts) {

        ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

        input.subjectId = a.id;

        ConnectApi.MessageBodyInput body = new ConnectApi.MessageBodyInput();

        body.messageSegments = new List<ConnectApi.MessageSegmentInput>();

        ConnectApi.TextSegmentInput textSegment = new ConnectApi.TextSegmentInput();

        textSegment.text = 'Let\'s win the ' + a.name + ' account.';

        body.messageSegments.add(textSegment);

        input.body = body;

        ConnectApi.BatchInput batchInput = new ConnectApi.BatchInput(input);

        batchInputs.add(batchInput);

      }

      ConnectApi.ChatterFeeds.postFeedElementBatch(Network.getNetworkId(), batchInputs);

   }

```


Apex Reference Guide ChatterFeeds Class

##### **`publishDraftFeedElement(communityId, feedElementId, feedElement)`**

Publish a draft feed element.

API Version

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement publishDraftFeedElement(String communityId, String

   feedElementId, ConnectApi.FeedElementInput feedElement)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element to publish.

```
   feedElement
```

Type: `ConnectApi.FeedElementInput`

Use this optional parameter to edit your draft before publishing.

Return Value

Type: `ConnectApi.FeedElement`

The published feed element has a new ID.

##### **`searchFeedElements(communityId, q)`**

Get the first page of feed elements that match the search criteria.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, sortParam)`**

Get the first page of sorted feed elements that match the search criteria.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, ConnectApi.FeedSortOrder sortParam)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, threadedCommentsCollapsed)`**

Get the feed elements and comments that match the search criteria.

API Version

44.0

Available to Guest Users

44.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, Boolean threadedCommentsCollapsed)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, pageParam, pageSize)`**

Get a page of feed elements that match the search criteria.

API Version

31.0

Available to Guest Users

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, String pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, pageParam, pageSize, sortParam)`**

Get a page of sorted feed elements that match the search criteria.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, pageParam, pageSize,`**

```
  threadedCommentsCollapsed)

```

Get a page of feed elements with comments in a threaded style that match the search criteria.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, String pageParam, Integer pageSize, Boolean threadedCommentsCollapsed)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, pageParam, pageSize, threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, recentCommentCount, pageParam, pageSize,`**

```
  sortParam)

```

Get a page of sorted feed elements that match the search criteria. Each feed element includes no more than the specified number of
comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, Integer recentCommentCount, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, recentCommentCount, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, q)`**

Get the feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` feeds that match the search criteria.


Apex Reference Guide ChatterFeeds Class

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchFeedElementsInFeed(communityId, feedType, pageParam, pageSize,`**

```
  sortParam, q)

```

Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`,
and `PendingReview` feeds that match the search criteria.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.


Apex Reference Guide ChatterFeeds Class

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam, q)

```

Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`,
and `PendingReview` feeds that match the search criteria. Each feed element includes no more than the specified number of
comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q,
result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam, q, filter)

```

Get a page of sorted and filtered feed elements from the `Home` feed that match the search criteria. Each feed element includes no more
than the specified number of comments.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q,

   ConnectApi.FeedFilter filter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. The only valid value is `Home` .


Apex Reference Guide ChatterFeeds Class

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

When the _`sortParam`_ is `MostViewed`, you must pass in `null` for the _`pageParam`_ .

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

When the _`sortParam`_ is `MostViewed`, the _`pageSize`_ must be a value from 1 to 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.


Apex Reference Guide ChatterFeeds Class

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q,
filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, q)`**

Search up to 5,000 of the most recent feed elements in a feed for a subject ID that match the search string. Feed elements are returned
in order of most recent activity.

API Version

31.0

Available to Guest Users

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, `Streams`, and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `UserProfile`,
_`subjectId`_ can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the
alias `me` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, pageParam,`**

```
  pageSize, sortParam, q)

```

Get a page of sorted feed elements from a feed for a record or user that match the search criteria.


Apex Reference Guide ChatterFeeds Class

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, `Streams`, and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `UserProfile`,
_`subjectId`_ can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the
alias `me` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Order of feed items in the feed.

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.


Apex Reference Guide ChatterFeeds Class

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Search term. Searches keywords in the user or group name. A minimum of one character is required. This parameter doesn’t support
wildcards. This parameter is required.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q)

```

Get a page of sorted feed elements from a feed that match the search criteria. Each feed element includes no more than the specified
number of comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, `Streams`, and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `UserProfile`,
_`subjectId`_ can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the
alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.


Apex Reference Guide ChatterFeeds Class

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, filter)

```

Get a page of sorted and filtered feed elements from a `UserProfile` feed that match the search criteria.

API Version

35.0

Available to Guest Users

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedFilter filter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.UserProfile` .

```
   subjectId
```

Type: String

ID of any user. To specify the context user, use the user ID or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

One or more keywords to search for in the feed elements visible to the context user. The search string can contain wildcards and
[must contain at least two characters that aren’t wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Value must be `ConnectApi.FeedFilter.CommunityScoped` . Filters the feed to include only feed elements that are
scoped to Experience Cloud sites. Feed elements that are always visible in all sites are filtered out.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, customFilter)

```

Get a page of sorted and filtered feed elements from a case feed that match the search criteria.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, String customFilter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`


Apex Reference Guide ChatterFeeds Class

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

One or more keywords to search for in the feed elements visible to the context user. The search string can contain wildcards and
[must contain at least two characters that aren’t wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, showInternalOnly)

```

Get a page of sorted feed elements from a feed for a record or user that match the search criteria. Each feed element includes no more
than the specified number of comments. Specify whether to return feed elements posted by internal (non-Experience Cloud site) users
only.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, Boolean showInternalOnly)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .


Apex Reference Guide ChatterFeeds Class

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, showInternalOnly, filter)

```

Get a page of sorted and filtered feed elements from a feed for a record or user that match the search criteria. Each feed element includes
no more than the specified number of comments. Specify whether to return feed elements posted by internal (non-Experience Cloud
site) users only.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, Boolean showInternalOnly,

   ConnectApi.FeedFilter filter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .


Apex Reference Guide ChatterFeeds Class

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, showInternalOnly, customFilter)

```

Get a page of sorted and filtered feed elements from a case feed that match the search criteria.

API Version

40.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, Boolean showInternalOnly, String

   customFilter)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   filter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q)`**

Get the feed elements from a feed filtered by a key prefix that match the search criteria.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFilterFeed(String

   communityId, String subjectId, String keyPrefix, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam,`**

```
  pageSize, sortParam, q)

```

Get a page of sorted feed elements from a feed filtered by a key prefix that match the search criteria.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFilterFeed(String

   communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q)

```

Get a page of sorted feed elements from a feed filtered by a key prefix that match the search criteria. Each feed element includes no
more than the specified number of comments.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFilterFeed(String

   communityId, String subjectId, String keyPrefix, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize,
sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchStreams(communityId, q)`**

Search the Chatter feed streams for the context user.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage searchStreams(String communityId, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterStreamPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchStreams(communityId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchStreams(communityId, q, sortParam)`**

Search and sort the Chatter feed streams for the context user.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage searchStreams(String communityId, String q,

   ConnectApi.SortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   sortParam
```

Type: `ConnectApi.SortOrder`

Specifies the sort order. Values are:

**•** `Ascending` —Items are in ascending alphabetical order (A-Z).

**•** `Descending` —Items are in descending alphabetical order (Z-A).

**•** `MostRecentlyViewed` —Items are in descending chronological order by view. This sort order is valid only for Chatter feed
streams.

If not specified, default value is `Ascending` .

Return Value

Type: `ConnectApi.ChatterStreamPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchStreams(communityId, q, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchStreams(communityId, q, pageParam, pageSize)`**

Search the Chatter feed streams for the context user and return a page of results.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage searchStreams(String communityId, String q,

   Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 to 250. The default size is 25.

Return Value

Type: `ConnectApi.ChatterStreamPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchStreams(communityId, q, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchStreams(communityId, q, pageParam, pageSize, sortParam)`**

Search the Chatter feed streams for the context user and return a sorted page of results.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage searchStreams(String communityId, String q,

   Integer pageParam, Integer pageSize, ConnectApi.SortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 to 250. The default size is 25.

```
   sortParam
```

Type: `ConnectApi.SortOrder`

Specifies the sort order. Values are:

**•** `Ascending` —Items are in ascending alphabetical order (A-Z).

**•** `Descending` —Items are in descending alphabetical order (Z-A).

**•** `MostRecentlyViewed` —Items are in descending chronological order by view. This sort order is valid only for Chatter feed
streams.

If not specified, default value is `Ascending` .

Return Value

Type: `ConnectApi.ChatterStreamPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchStreams(communityId, q, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchStreams(communityId, q, pageParam, pageSize, sortParam, globalScope)`**

Search the Chatter feed streams from all Experience Cloud sites for the context user and return a sorted page of results.

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage searchStreams(String communityId, String q,

   Integer pageParam, Integer pageSize, ConnectApi.SortOrder sortParam, Boolean globalScope)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 to 250. The default size is 25.

```
   sortParam
```

Type: `ConnectApi.SortOrder`

Specifies the sort order. Values are:

**•** `Ascending` —Items are in ascending alphabetical order (A-Z).

**•** `Descending` —Items are in descending alphabetical order (Z-A).


Apex Reference Guide ChatterFeeds Class

**•** `MostRecentlyViewed` —Items are in descending chronological order by view. This sort order is valid only for Chatter feed
streams.

If not specified, default value is `Ascending` .

```
   globalScope
```

Type: Boolean

Specifies whether to get streams from all the context user’s Experience Cloud sites, regardless of the _`communityId`_ value.

Tip: If you know the _`communityId`_ for the streams, we recommend setting _`globalScope`_ to `false` .

Return Value

Type: `ConnectApi.ChatterStreamPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

##### **`setCommentIsVerified(communityId, commentId, isVerified)`**

Mark a comment as verified or unverified.

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VerifiedCapability setCommentIsVerified(String communityId,

   String commentId, Boolean isVerified)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment on a question post. Only one comment on a question post can be marked as verified.

```
   isVerified
```

Type: Boolean

Specifies whether to mark the comment as verified ( `true` ) or unverified ( `false` ).

Only verified comments can be marked as unverified, and only unverified comments can be marked as verified.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.VerifiedCapability`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setCommentIsVerifiedByAnonymized(communityId, commentId, isVerified,`**

```
  isVerifiedByAnonymized)

```

Mark a comment as verified by an anonymous user.

API Version

43.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VerifiedCapability setCommentIsVerifiedByAnonymized(String

   communityId, String commentId, Boolean isVerified, Boolean isVerifiedByAnonymized)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment on a question post. Only one comment on a question post can be marked as verified.

```
   isVerified
```

Type: Boolean

Specifies whether to mark the comment as verified ( `true` ) or unverified ( `false` ).

Only verified comments can be marked as unverified, and only unverified comments can be marked as verified.

```
   isVerifiedByAnonymized
```

Type: Boolean

Specifies whether to mark the comment as verified by an anonymous user ( `true` ).

If a user previously verified a comment and then requested the activity to be deleted, use `isVerifiedByAnonymized` to
maintain the verification and anonymize the value of `lastVerifiedByUser` .

You can’t set `isVerified` and `isVerifiedByAnonymized` to `true` at the same time. `isVerifiedByAnonymized`
can be set to `true` only if `isVerified` is already set to `true` .

You can’t set `isVerifiedByAnonymized` to `false` . After `isVerifiedByAnonymized` is set to `true`, it can be
undone only when another user marks the comment as unverified and then reverifies the comment.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.VerifiedCapability`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setCommentVote(communityId, commentId, upDownVote)`**

Upvote or downvote a comment.

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UpDownVoteCapability setCommentVote(String communityId, String

   commentId, ConnectApi.UpDownVoteCapabilityInput upDownVote)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment.

```
   upDownVote
```

Type: `ConnectApi.UpDownVoteCapabilityInput`

A `ConnectApi.UpDownVoteCapabilityInput` object that includes your vote.

Return Value

Type: `ConnectApi.UpDownVoteCapability`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setFeedCommentStatus(communityId, commentId, status)`**

Set the status of a comment.

API Version

38.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.StatusCapability setFeedCommentStatus(String communityId,

   String commentId, ConnectApi.StatusCapabilityInput status)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment.

```
   status
```

Type: `ConnectApi.StatusCapabilityInput`

A `ConnectApi.StatusCapabilityInput` object that includes the status you want to set.

Return Value

Type: `ConnectApi.StatusCapability`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Usage

Only users with the Can Approve Feed Post and Comment permission can set the status of a feed post or comment.

##### **`setFeedElementIsClosed(communityId, feedElementId, isClosed)`**

Set a feed element to closed.

Users can’t edit (specifically the feed item body or title), comment on, or delete a closed feed element. If the closed feed element is a
poll, users can’t vote on it. Users can’t edit (specifically the comment body) or delete a comment on a closed feed element or select or
remove it as best answer.

Admins and moderators can edit and delete closed feed elements and comments on closed feed elements. Admins and moderators
can select or remove the best answer status on comments on closed feed elements.

API Version

43.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.CloseCapability setFeedElementIsClosed(String communityId,

   String feedElementId, Boolean isClosed)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   isClosed
```

Type: Boolean

Specifies whether to set the feed element to closed ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.CloseCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setFeedElementVote(communityId, feedElementId, upDownVote)`**

Upvote or downvote a feed element.

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UpDownVoteCapability setFeedElementVote(String communityId,

   String feedElementId, ConnectApi.UpDownVoteCapabilityInput upDownVote)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.


Apex Reference Guide ChatterFeeds Class

```
   upDownVote
```

Type: `ConnectApi.UpDownVoteCapabilityInput`

A `ConnectApi.UpDownVoteCapabilityInput` object that includes your vote.

Return Value

Type: `ConnectApi.UpDownVoteCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setFeedEntityStatus(communityId, feedElementId, status)`**

Set the status of a feed post.

API Version

37.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.StatusCapability setFeedEntityStatus(String communityId, String

   feedElementId, ConnectApi.StatusCapabilityInput status)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   status
```

Type: `ConnectApi.StatusCapabilityInput`

A `ConnectApi.StatusCapabilityInput` object that includes the status you want to set.

Return Value

Type: `ConnectApi.StatusCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Usage

Only users with the Can Approve Feed Post and Comment permission can set the status of a feed post or comment.


Apex Reference Guide ChatterFeeds Class

##### **`setIsMutedByMe(communityId, feedElementId, isMutedByMe)`**

Mute or unmute a feed element.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.MuteCapability setIsMutedByMe(String communityId, String

   feedElementId, Boolean isMutedByMe)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   isMutedByMe
```

Type: Boolean

Indicates whether the feed element is muted for the context user. Default value is `false` .

Return Value

Type: `ConnectApi.MuteCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setIsReadByMe(communityId, feedElementId, readBy)`**

Mark a feed element as read for the context user using an input class.

API Version

40.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.ReadByCapability setIsReadByMe(String communityId, String

   feedElementId, ConnectApi.ReadByCapabilityInput readBy)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element to mark as read.

```
   readBy
```

Type: `ConnectApi.ReadByCapabilityInput`

A `ConnectApi.ReadByCapabilityInput` body indicating to mark the feed elements as read.

Return Value

Type: `ConnectApi.ReadByCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setIsReadByMe(communityId, feedElementId, isReadByMe)`**

Mark a feed element as read for the context user.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ReadByCapability setIsReadByMe(String communityId, String

   feedElementId, Boolean isReadByMe)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element to mark as read.


Apex Reference Guide ChatterFeeds Class

```
   isReadByMe
```

Type: Boolean

Specifies to mark the feed element as read ( `true` ) for the context user.

Return Value

Type: `ConnectApi.ReadByCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`updateComment(communityId, commentId, comment)`**

Edit a comment.

API Version

34.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Comment updateComment(String communityId, String commentId,

   ConnectApi.CommentInput comment)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment to be edited.

```
   comment
```

Type: `ConnectApi.CommentInput`

Information about the comment to be edited.

Return Value

Type: `ConnectApi.Comment`

If the comment doesn’t support the `edit` capability, the return value is `ConnectApi.NotFoundException` .

Example

```
   String commentId;

   String communityId = Network.getNetworkId();

```


Apex Reference Guide ChatterFeeds Class

```
   // Get the last feed item created by the context user.

   List<FeedItem> feedItems = [SELECT Id FROM FeedItem WHERE CreatedById = :UserInfo.getUserId()

    ORDER BY CreatedDate DESC];

   if (feedItems.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   String feedElementId = feedItems[0].id;

   ConnectApi.CommentPage commentPage =

   ConnectApi.ChatterFeeds.getCommentsForFeedElement(communityId, feedElementId);

   if (commentPage.items.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   commentId = commentPage.items[0].id;

   ConnectApi.FeedEntityIsEditable isEditable =

   ConnectApi.ChatterFeeds.isCommentEditableByMe(communityId, commentId);

   if (isEditable.isEditableByMe == true){

      ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

      ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

      ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

      messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

      textSegmentInput.text = 'This is my edited comment.';

      messageBodyInput.messageSegments.add(textSegmentInput);

      commentInput.body = messageBodyInput;

      ConnectApi.Comment editedComment = ConnectApi.ChatterFeeds.updateComment(communityId,

    commentId, commentInput);

   }

##### **`updateDirectMessage(communityId, feedElementId, directMessage)`**

```

Update the members of a direct message.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.DirectMessageCapability updateDirectMessage(String communityId,

   String feedElementId, ConnectApi.DirectMessageCapabilityInput directMessage)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   directMessage
```

Type: `ConnectApi.DirectMessageCapabilityInput`

A `ConnectApi.DirectMessageCapabilityInput` body that includes the members to add and remove.

Return Value

Type: `ConnectApi.DirectMessageCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`updateFeedElement(communityId, feedElementId, feedElement)`**

Edit a feed element.

API Version

34.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement updateFeedElement(String communityId, String

   feedElementId, ConnectApi.FeedElementInput feedElement)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element to be edited. Feed items are the only type of feed element that can be edited.

```
   feedElement
```

Type: `ConnectApi.FeedElementInput`

Information about the feed item to be edited.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElement`

If the feed element doesn’t support the `edit` capability, the return value is `ConnectApi.NotFoundException` .

Example for Editing a Feed Post

```
   String communityId = Network.getNetworkId();

   // Get the last feed item created by the context user.

   List<FeedItem> feedItems = [SELECT Id FROM FeedItem WHERE CreatedById = :UserInfo.getUserId()

    ORDER BY CreatedDate DESC];

   if (feedItems.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   String feedElementId = feedItems[0].id;

   ConnectApi.FeedEntityIsEditable isEditable =

   ConnectApi.ChatterFeeds.isFeedElementEditableByMe(communityId, feedElementId);

   if (isEditable.isEditableByMe == true){

      ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

      ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

      ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

      messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

      textSegmentInput.text = 'This is my edited post.';

      messageBodyInput.messageSegments.add(textSegmentInput);

      feedItemInput.body = messageBodyInput;

      ConnectApi.FeedElement editedFeedElement =

   ConnectApi.ChatterFeeds.updateFeedElement(communityId, feedElementId, feedItemInput);

   }

```

Example for Editing a Question Title and Post

```
   String communityId = Network.getNetworkId();

   // Get the last feed item created by the context user.

   List<FeedItem> feedItems = [SELECT Id FROM FeedItem WHERE CreatedById = :UserInfo.getUserId()

    ORDER BY CreatedDate DESC];

   if (feedItems.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   String feedElementId = feedItems[0].id;

   ConnectApi.FeedEntityIsEditable isEditable =

   ConnectApi.ChatterFeeds.isFeedElementEditableByMe(communityId, feedElementId);

```


Apex Reference Guide ChatterFeeds Class

```
   if (isEditable.isEditableByMe == true){

      ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

      ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

      ConnectApi.QuestionAndAnswersCapabilityInput questionAndAnswersCapabilityInput = new

   ConnectApi.QuestionAndAnswersCapabilityInput();

      ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

      ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

      messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

      textSegmentInput.text = 'This is my edited question.';

      messageBodyInput.messageSegments.add(textSegmentInput);

      feedItemInput.body = messageBodyInput;

      feedItemInput.capabilities = feedElementCapabilitiesInput;

      feedElementCapabilitiesInput.questionAndAnswers = questionAndAnswersCapabilityInput;

      questionAndAnswersCapabilityInput.questionTitle = 'Where is my edited question?';

      ConnectApi.FeedElement editedFeedElement =

   ConnectApi.ChatterFeeds.updateFeedElement(communityId, feedElementId, feedItemInput);

   }

##### **`updateFeedElementBookmarks(communityId, feedElementId, bookmarks)`**

```

Bookmark a feed element or remove a bookmark from a feed element using an input class.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BookmarksCapability updateFeedElementBookmarks(String

   communityId, String feedElementId, ConnectApi.BookmarksCapabilityInput bookmarks)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.


Apex Reference Guide ChatterFeeds Class

```
   bookmarks
```

Type: `ConnectApi.BookmarksCapabilityInput`

Information about a bookmark.

Return Value

Type: ConnectApi.BookmarksCapability

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`updateFeedElementBookmarks(communityId, feedElementId,`**

```
  isBookmarkedByCurrentUser)

```

Bookmark a feed element or remove a bookmark from a feed element.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BookmarksCapability updateFeedElementBookmarks(String

   communityId, String feedElementId, Boolean isBookmarkedByCurrentUser)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   isBookmarkedByCurrentUser
```

Type: Boolean

Specify whether to bookmark the feed element ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.BookmarksCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .


Apex Reference Guide ChatterFeeds Class

Example

```
   ConnectApi.BookmarksCapability bookmark =

   ConnectApi.ChatterFeeds.updateFeedElementBookmarks(null, '0D5D0000000KuGh', true);

##### **`updateFeedElementReadByCapabilityBatch(communityId, feedElementIds, readBy)`**

```

Mark multiple feed elements as read by the context user at the same time using an input class.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] updateFeedElementReadByCapabilityBatch(String

   communityId, List<String> feedElementIds, ConnectApi.ReadByCapabilityInput readBy)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementIds
```

Type: List<String>

Up to 500 feed element IDs to mark as read.

```
   readBy
```

Type: `ConnectApi.ReadByCapabilityInput`

A `ConnectApi.ReadByCapabilityInput` body indicating to mark the feed elements as read.

Return Value

Type: `ConnectApi.BatchResult` []

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

The returned objects correspond to each of the input objects and are returned in the same order as the input objects.

The method call fails only if an error occurs that affects the entire operation (such as a parsing failure). If an individual object causes an
error, the error is embedded within the `ConnectApi.BatchResult` list.

##### **`updateFeedElementReadByCapabilityBatch(communityId, feedElementIds,`**

```
  isReadByMe)

```

Mark multiple feed elements as read by the context user at the same time.


Apex Reference Guide ChatterFeeds Class

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] updateFeedElementReadByCapabilityBatch(String

   communityId, List<String> feedElementIds, Boolean isReadByMe)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementIds
```

Type: List<String>

Up to 500 feed element IDs to mark as read.

```
   isReadByMe
```

Type: Boolean

Specifies to mark the feed element as read ( `true` ) for the context user.

Return Value

Type: `ConnectApi.BatchResult` []

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`updateLikeForComment(communityId, commentId, isLikedByCurrentUser)`**

Like or unlike a comment.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage updateLikeForComment(String communityId, String

   commentId, Boolean isLikedByCurrentUser)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID of the comment.

```
   isLikedByCurrentUser
```

Type: Boolean

Specifies if the context user likes ( `true` ) or unlikes ( `false` ) the comment.

Return Value

Type: `ConnectApi.ChatterLikePage`

##### **`updateLikeForFeedElement(communityId, feedElementId, isLikedByCurrentUser)`**

Like or unlike a feed element.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage updateLikeForFeedElement(String communityId,

   String feedElementId, Boolean isLikedByCurrentUser)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   isLikedByCurrentUser
```

Type: Boolean

Specifies if the context user likes ( `true` ) or unlikes ( `false` ) the feed element.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.ChatterLikePage`

If the feed element doesn’t support the `ChatterLikes` capability, the return value is `ConnectApi.NotFoundException` .

##### **`updatePinnedFeedElements(communityId, feedType, subjectId, pin)`**

Pin or unpin feed elements to a group or topic feed.

API Version

41.0

Available to Guest Users

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.PinCapability updatePinnedFeedElements(String communityId,

   ConnectApi.FeedType feedType, String subjectId, ConnectApi.PinCapabilityInput pin)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. Valid values are `Record` and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ must be a group ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID.

```
   pin
```

Type: `ConnectApi.PinCapabilityInput`

A `ConnectApi.PinCapabilityInput` object indicating the feed element to pin or unpin.

Return Value

Type: `ConnectApi.PinCapability`

If the feed doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .


Apex Reference Guide ChatterFeeds Class

##### **`updateStream(communityId, streamId, streamInput)`**

Update a Chatter feed stream.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStream updateStream(String communityId, String streamId,

   ConnectApi.ChatterStreamInput streamInput)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   streamId
```

Type: String

ID of the Chatter feed stream.

```
   streamInput
```

Type: `ConnectApi.ChatterStreamInput`

A `ConnectApi.ChatterStreamInput` object.

Return Value

Type: `ConnectApi.ChatterStream`

##### **`voteOnFeedElementPoll(communityId, feedElementId, myChoiceId)`**

Vote on a poll or change your vote on a poll.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.PollCapability voteOnFeedElementPoll(String communityId, String

   feedElementId, String myChoiceId)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   myChoiceId
```

Type: String

ID of the poll item you’re voting for. The key prefix for poll items is 09A.

Return Value

Type: `ConnectApi.PollCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Example

```
   ConnectApi.PollCapability poll = ConnectApi.ChatterFeeds.voteOnFeedElementPoll(null,

   '0D5D0000000XZaUKAW', '09AD000000000TKMAY');

#### ChatterFeeds Test Methods These test methods are for ChatterFeeds . All methods are static.

```

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

IN THIS SECTION:

setTestGetFeedElementsFromFeed(communityId, feedType, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFeeds Class

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, showInternalOnly, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, filter, threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFeeds Class

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, result)
a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElementsFromFilterFeed`
method is called in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElements`
`FromFilterFeed` method is called in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElements`
`FromFilterFeed` method is called in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle,
density, pageParam, pageSize, updatedSince, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the
`getFeedElementsFromFilterFeedUpdatedSince` method is called in a test context.

setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince,
result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince,
filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, showInternalOnly, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFeeds Class

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetRelatedPosts(communityId, feedElementId, filter, maxResults, result)
Register a `ConnectApi.RelatedFeedPosts` object to be returned when the matching
`ConnectApi.getRelatedPosts(communityId, feedElementId, filter, maxResults)` method is
called in a test context. Use the method with the same parameters or you receive an exception.

setTestGetTopUnansweredQuestions(communityId, result) (Pilot)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetTopUnansweredQuestions(communityId, filter, result) (Pilot)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetTopUnansweredQuestions(communityId, pageSize, result) (Pilot)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetTopUnansweredQuestions(communityId, filter, pageSize, result) (Pilot)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElements(communityId, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElements(communityId, q, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.


Apex Reference Guide ChatterFeeds Class

setTestSearchFeedElements(communityId, q, threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElements(communityId, q, pageParam, pageSize, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElements(communityId, q, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElements(communityId, q, pageParam, pageSize, threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElements(communityId, q, recentCommentCount, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q,
result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q,
filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.


Apex Reference Guide ChatterFeeds Class

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `searchFeedElementsInFeed` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.


Apex Reference Guide ChatterFeeds Class

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize,
sortParam, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.

setTestSearchStreams(communityId, q, result)
Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStream(communityId, q)` method is called in a test context. Use the method with the same
parameters or you receive an exception.

setTestSearchStreams(communityId, q, sortParam, result)
Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStream(communityId, q, sortParam)` method is called in a test context. Use the method
with the same parameters or you receive an exception.

setTestSearchStreams(communityId, q, pageParam, pageSize, result)
Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStreams(communityId, q, pageParam, pageSize)` method is called in a test context.
Use the method with the same parameters or you receive an exception.

setTestSearchStreams(communityId, q, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStreams(communityId, q, pageParam, pageSize, sortParam)` method is called
in a test context. Use the method with the same parameters or you receive an exception.

setTestSearchStreams(communityId, q, pageParam, pageSize, sortParam, globalScope, result)
Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching

```
    ConnectApi.searchStreams(communityId, q, pageParam, pageSize, sortParam, globalScope)
```

method is called in a test context. Use the method with the same parameters or you receive an exception.

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, pageParam, pageSize,`**

```
  sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The only valid value for this parameter is `Company` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.


Apex Reference Guide ChatterFeeds Class

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedElementPage result)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

32.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedFilter filter,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. The only valid value is `Home` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String


Apex Reference Guide ChatterFeeds Class

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, filter, threadedCommentsCollapsed,

  result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters or
you receive an exception.

API Version

44.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedFilter filter,

   Boolean threadedCommentsCollapsed, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. The only valid value is `Home` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.


Apex Reference Guide ChatterFeeds Class

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.


Apex Reference Guide ChatterFeeds Class

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
threadedCommentsCollapsed)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The feed type.

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, pageParam,`**

```
  pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, showInternalOnly,

  result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, Boolean

   showInternalOnly, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.


Apex Reference Guide ChatterFeeds Class

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFeeds Class

API Version

35.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedFilter filter, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.UserProfile` .

```
   subjectId
```

Type: String

ID of any user. To specify the context user, use the user ID or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.


Apex Reference Guide ChatterFeeds Class

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Value must be `ConnectApi.FeedFilter.CommunityScoped` . Filters the feed to include only feed elements that are
scoped to Experience Cloud sites. Feed elements that are always visible in all sites are filtered out. Currently, feed elements scoped
to sites have a User or a Group parent record. However, other parent record types could be scoped to sites in the future.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, filter,

  threadedCommentsCollapsed, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters or
you receive an exception.

API Version

44.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedFilter filter, Boolean threadedCommentsCollapsed,

   ConnectApi.FeedElementPage result)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.UserProfile` .

```
   subjectId
```

Type: String

ID of any user. To specify the context user, use the user ID or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Value must be `ConnectApi.FeedFilter.CommunityScoped` . Filters the feed to include only feed elements that are
scoped to Experience Cloud sites. Feed elements that are always visible in all sites are filtered out. Currently, feed elements scoped
to sites have a User or a Group parent record. However, other parent record types could be scoped to sites in the future.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
filter, threadedCommentsCollapsed)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, customFilter,

  result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

40.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String

   customFilter, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .


Apex Reference Guide ChatterFeeds Class

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
customFilter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, showInternalOnly, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, ConnectApi.FeedElementPage

   result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.


Apex Reference Guide ChatterFeeds Class

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, showInternalOnly, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

32.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, ConnectApi.FeedFilter

   filter, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String


Apex Reference Guide ChatterFeeds Class

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.


Apex Reference Guide ChatterFeeds Class

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, showInternalOnly, filter, threadedCommentsCollapsed, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

44.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, ConnectApi.FeedFilter

   filter, Boolean threadedCommentsCollapsed, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Maximum number of comments to return with each feed item. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.


Apex Reference Guide ChatterFeeds Class

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, threadedCommentsCollapsed)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, showInternalOnly, customFilter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

40.0


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, String customFilter,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:


Apex Reference Guide ChatterFeeds Class

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, showInternalOnly, customFilter, threadedCommentsCollapsed, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters or
you receive an exception.

API Version

44.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

```


Apex Reference Guide ChatterFeeds Class

```
   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, String customFilter,

   Boolean threadedCommentsCollapsed, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.


Apex Reference Guide ChatterFeeds Class

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, threadedCommentsCollapsed)

##### **`setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  result)

```

a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElementsFromFilterFeed`
method is called in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFilterFeed(String communityId, String

   subjectId, String keyPrefix, ConnectApi.FeedElementPage result)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElements`
`FromFilterFeed` method is called in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFilterFeed(String communityId, String

   subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElements`
`FromFilterFeed` method is called in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFilterFeed(String communityId, String

   subjectId, String keyPrefix, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String


Apex Reference Guide ChatterFeeds Class

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId,`**

```
  keyPrefix, recentCommentCount, elementsPerBundle, density, pageParam,

  pageSize, updatedSince, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the
`getFeedElementsFromFilterFeedUpdatedSince` method is called in a test context.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFilterFeedUpdatedSince(String communityId,

   String subjectId, String keyPrefix, Integer recentCommentCount, Integer

```


Apex Reference Guide ChatterFeeds Class

```
   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

Opaque token defining the modification timestamp of the feed and the sort order.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle,
density, pageParam, pageSize, updatedSince)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, String updatedSince, ConnectApi.FeedElementPage

   result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.


Apex Reference Guide ChatterFeeds Class

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

32.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, String updatedSince, ConnectApi.FeedFilter filter,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.


Apex Reference Guide ChatterFeeds Class

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

One of these values:

**•** `Files`


Apex Reference Guide ChatterFeeds Class

**•** `Groups`

**•** `News`

**•** `People`

**•** `Record`

```
   subjectId
```

Type: String

If _`feedType`_ is `ConnectApi.Record`, _`subjectId`_ can be any record ID, including a group ID. Otherwise, it must be the
context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince,

  showInternalOnly, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince,

   Boolean showInternalOnly, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, updatedSince,
showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

35.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, ConnectApi.FeedFilter filter, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.UserProfile` .

```
   subjectId
```

Type: String

ID of any user. To specify the context user, use the user ID or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

