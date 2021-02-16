# openapi-client# First Data Gateway
Payment Gateway API Specification.
- API version: 21.1.0

## Requirements

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install first_data_gateway
```
(you may need to run `pip` with root permission: `sudo pip install first_data_gateway`)

You can also install directly from Github:

```sh
pip install git+https://github.com/GBSEcom/Python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GBSEcom/Python.git`)

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## Getting Started

```python
from __future__ import print_function
import openapi_client
import simple
from simple import MerchantCredentials
from simple import Gateway
from openapi_client.rest import ApiException
from pprint import pprint

api_key = "Your API Key here"
api_secret = "Your API Secret here"

credentials = MerchantCredentials(api_key, api_secret)

gateway = Gateway.create(credentials)
api_client = openapi_client.ApiClient()

json_payload = 	"""{
					\"requestType\": \"PaymentCardSaleTransaction\",
					\"transactionAmount\": {
						\"total\": \"25.01\",
						"currency": "USD"
					},
					\"paymentMethod\": {
						\"paymentCard\": {
							\"number\": \"4012000033330026\",
							\"expiryDate\": {
								\"month\": \"12\",
								\"year\": \"25\"
							},
							\"securityCode\": \"977\"
						}
					}
				}"""

obj_name = "PaymentCardSaleTransaction"
obj_model = getattr(openapi_client, obj_name)
payload = api_client.build_object(json.loads(json_payload), obj_model)

result = gateway.primary_payment_transaction(payload)
pprint(result)

```

## Documentation for API Endpoints

All URIs are relative to *https://cert.api.firstdata.com/gateway/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**authentication_access_tokens_post**](docs/AuthenticationApi.md#authentication_access_tokens_post) | **POST** /authentication/access-tokens | Generate an access token for user authentication.
*CurrencyConversionApi* | [**get_exchange_rate**](docs/CurrencyConversionApi.md#get_exchange_rate) | **POST** /exchange-rates | Generate dynamic currency conversion transactions.
*FraudDetectApi* | [**fraud_client_registration_post**](docs/FraudDetectApi.md#fraud_client_registration_post) | **POST** /fraud/client-registration | Client registration for fraud detect transaction.
*FraudDetectApi* | [**fraud_payment_registration_post**](docs/FraudDetectApi.md#fraud_payment_registration_post) | **POST** /fraud/payment-registration | Payment registration for fraud detect transaction.
*FraudDetectApi* | [**score_only**](docs/FraudDetectApi.md#score_only) | **POST** /fraud/score-only | Score a transaction for fraud.
*InformationLookupApi* | [**card_info_lookup**](docs/InformationLookupApi.md#card_info_lookup) | **POST** /card-information | Card information lookup.
*InformationLookupApi* | [**lookup_account**](docs/InformationLookupApi.md#lookup_account) | **POST** /account-information | Account information lookup.
*OrderApi* | [**order_inquiry**](docs/OrderApi.md#order_inquiry) | **GET** /orders/{order-id} | Retrieve the state of an order.
*OrderApi* | [**submit_secondary_transaction_from_order**](docs/OrderApi.md#submit_secondary_transaction_from_order) | **POST** /orders/{order-id} | Perform return or postAuth secondary transactions.
*PaymentApi* | [**finalize_secure_transaction**](docs/PaymentApi.md#finalize_secure_transaction) | **PATCH** /payments/{transaction-id} | Update a 3DSecure or UnionPay payment and continue processing.
*PaymentApi* | [**submit_primary_transaction**](docs/PaymentApi.md#submit_primary_transaction) | **POST** /payments | Generate a primary transaction.
*PaymentApi* | [**submit_secondary_transaction**](docs/PaymentApi.md#submit_secondary_transaction) | **POST** /payments/{transaction-id} | Perform a secondary transaction.
*PaymentApi* | [**transaction_inquiry**](docs/PaymentApi.md#transaction_inquiry) | **GET** /payments/{transaction-id} | Retrieve the state of a transaction.
*PaymentSchedulesApi* | [**cancel_payment_schedule**](docs/PaymentSchedulesApi.md#cancel_payment_schedule) | **DELETE** /payment-schedules/{order-id} | Cancel a gateway payment schedule.
*PaymentSchedulesApi* | [**create_payment_schedule**](docs/PaymentSchedulesApi.md#create_payment_schedule) | **POST** /payment-schedules | Create gateway payment schedule.
*PaymentSchedulesApi* | [**inquiry_payment_schedule**](docs/PaymentSchedulesApi.md#inquiry_payment_schedule) | **GET** /payment-schedules/{order-id} | View a gateway payment schedule.
*PaymentSchedulesApi* | [**update_payment_schedule**](docs/PaymentSchedulesApi.md#update_payment_schedule) | **PATCH** /payment-schedules/{order-id} | Update a gateway payment schedule.
*PaymentTokenApi* | [**create_payment_token**](docs/PaymentTokenApi.md#create_payment_token) | **POST** /payment-tokens | Create a payment token from a payment card.
*PaymentTokenApi* | [**delete_payment_token**](docs/PaymentTokenApi.md#delete_payment_token) | **DELETE** /payment-tokens/{token-id} | Delete a payment token.
*PaymentTokenApi* | [**get_payment_token_details**](docs/PaymentTokenApi.md#get_payment_token_details) | **GET** /payment-tokens/{token-id} | Get payment card details associated with token.
*PaymentTokenApi* | [**update_payment_token**](docs/PaymentTokenApi.md#update_payment_token) | **PATCH** /payment-tokens | Update one or more payment tokens.
*PaymentURLApi* | [**create_payment_url**](docs/PaymentURLApi.md#create_payment_url) | **POST** /payment-url | Create a payment URL.
*PaymentURLApi* | [**delete_payment_url**](docs/PaymentURLApi.md#delete_payment_url) | **DELETE** /payment-url | Delete a payment URL.
*PaymentURLApi* | [**payment_url_detail**](docs/PaymentURLApi.md#payment_url_detail) | **GET** /payment-url | Retrieve the state of payment URL.
*VerificationApi* | [**verify_account**](docs/VerificationApi.md#verify_account) | **POST** /account-verification | Verify a payment card or payment token.
*VerificationApi* | [**verify_card**](docs/VerificationApi.md#verify_card) | **POST** /card-verification | Verify a payment card.


## Documentation For Models

 - [ACSResponse](docs/ACSResponse.md)
 - [AVSResponse](docs/AVSResponse.md)
 - [AccessTokenRequest](docs/AccessTokenRequest.md)
 - [AccessTokenResponse](docs/AccessTokenResponse.md)
 - [AccountInfoLookupRequest](docs/AccountInfoLookupRequest.md)
 - [AccountUpdaterResponse](docs/AccountUpdaterResponse.md)
 - [AccountVerificationRequest](docs/AccountVerificationRequest.md)
 - [AchCreditTransaction](docs/AchCreditTransaction.md)
 - [AchPostAuthTransaction](docs/AchPostAuthTransaction.md)
 - [AchPostAuthTransactionAllOf](docs/AchPostAuthTransactionAllOf.md)
 - [AchPreAuthTransaction](docs/AchPreAuthTransaction.md)
 - [AchPreAuthTransactionAllOf](docs/AchPreAuthTransactionAllOf.md)
 - [AchRecurringType](docs/AchRecurringType.md)
 - [AchResponse](docs/AchResponse.md)
 - [AchReturnTransaction](docs/AchReturnTransaction.md)
 - [AchSaleTransaction](docs/AchSaleTransaction.md)
 - [AchVoidTransaction](docs/AchVoidTransaction.md)
 - [AdditionalAmountRate](docs/AdditionalAmountRate.md)
 - [AdditionalDetails](docs/AdditionalDetails.md)
 - [AdditionalTransactionDetails](docs/AdditionalTransactionDetails.md)
 - [Address](docs/Address.md)
 - [Airline](docs/Airline.md)
 - [AirlineAncillaryServiceCategory](docs/AirlineAncillaryServiceCategory.md)
 - [AirlineTravelRoute](docs/AirlineTravelRoute.md)
 - [AliPay](docs/AliPay.md)
 - [AliPayPaymentMethod](docs/AliPayPaymentMethod.md)
 - [AliPayPaymentMethodAllOf](docs/AliPayPaymentMethodAllOf.md)
 - [AliPaySaleTransaction](docs/AliPaySaleTransaction.md)
 - [AliPaySaleTransactionAllOf](docs/AliPaySaleTransactionAllOf.md)
 - [Amount](docs/Amount.md)
 - [AmountComponents](docs/AmountComponents.md)
 - [AuthenticationRequest](docs/AuthenticationRequest.md)
 - [AuthenticationResult](docs/AuthenticationResult.md)
 - [AuthenticationUpdateRequest](docs/AuthenticationUpdateRequest.md)
 - [Background](docs/Background.md)
 - [BackgroundColor](docs/BackgroundColor.md)
 - [BancontactQR](docs/BancontactQR.md)
 - [BasicResponse](docs/BasicResponse.md)
 - [Billing](docs/Billing.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [BlockCard](docs/BlockCard.md)
 - [BlockDomain](docs/BlockDomain.md)
 - [BlockIPAddress](docs/BlockIPAddress.md)
 - [BlockName](docs/BlockName.md)
 - [BlockedCardNumber](docs/BlockedCardNumber.md)
 - [BlockedItems](docs/BlockedItems.md)
 - [Body](docs/Body.md)
 - [Borders](docs/Borders.md)
 - [BrandingStyleConfigurationRequest](docs/BrandingStyleConfigurationRequest.md)
 - [BrandingStyleConfigurationResponse](docs/BrandingStyleConfigurationResponse.md)
 - [BrandingStyleConfigurationResult](docs/BrandingStyleConfigurationResult.md)
 - [Button](docs/Button.md)
 - [CarRental](docs/CarRental.md)
 - [CarRentalExtraCharges](docs/CarRentalExtraCharges.md)
 - [Card](docs/Card.md)
 - [CardFunction](docs/CardFunction.md)
 - [CardInfo](docs/CardInfo.md)
 - [CardInfoLookupRequest](docs/CardInfoLookupRequest.md)
 - [CardInfoLookupResponse](docs/CardInfoLookupResponse.md)
 - [CardVerificationRequest](docs/CardVerificationRequest.md)
 - [ChinaDomestic](docs/ChinaDomestic.md)
 - [ChinaDomesticPaymentMethod](docs/ChinaDomesticPaymentMethod.md)
 - [ChinaDomesticPaymentMethodAllOf](docs/ChinaDomesticPaymentMethodAllOf.md)
 - [ChinaPnRSaleTransaction](docs/ChinaPnRSaleTransaction.md)
 - [ChinaPnRSaleTransactionAllOf](docs/ChinaPnRSaleTransactionAllOf.md)
 - [ClassicMode](docs/ClassicMode.md)
 - [ClearingDetails](docs/ClearingDetails.md)
 - [ClearingElement](docs/ClearingElement.md)
 - [ClientLocale](docs/ClientLocale.md)
 - [ClientRegistration](docs/ClientRegistration.md)
 - [CombinedMode](docs/CombinedMode.md)
 - [ConnectMode](docs/ConnectMode.md)
 - [Contact](docs/Contact.md)
 - [Content](docs/Content.md)
 - [CountryProfile](docs/CountryProfile.md)
 - [CreatePaymentToken](docs/CreatePaymentToken.md)
 - [CurrencyConversion](docs/CurrencyConversion.md)
 - [CurrencyConversionResponse](docs/CurrencyConversionResponse.md)
 - [Customer](docs/Customer.md)
 - [CustomerAddress](docs/CustomerAddress.md)
 - [DCCExchangeRateRequest](docs/DCCExchangeRateRequest.md)
 - [DCCExchangeRateRequestAllOf](docs/DCCExchangeRateRequestAllOf.md)
 - [Dcc](docs/Dcc.md)
 - [DccAllOf](docs/DccAllOf.md)
 - [DecryptedApplePay](docs/DecryptedApplePay.md)
 - [DecryptedApplePayWalletPaymentMethod](docs/DecryptedApplePayWalletPaymentMethod.md)
 - [DecryptedApplePayWalletPaymentMethodAllOf](docs/DecryptedApplePayWalletPaymentMethodAllOf.md)
 - [DecryptedGooglePay](docs/DecryptedGooglePay.md)
 - [DecryptedGooglePayWalletPaymentMethod](docs/DecryptedGooglePayWalletPaymentMethod.md)
 - [DecryptedGooglePayWalletPaymentMethodAllOf](docs/DecryptedGooglePayWalletPaymentMethodAllOf.md)
 - [DecryptedSamsungPay](docs/DecryptedSamsungPay.md)
 - [DecryptedSamsungPayWalletPaymentMethod](docs/DecryptedSamsungPayWalletPaymentMethod.md)
 - [DecryptedSamsungPayWalletPaymentMethodAllOf](docs/DecryptedSamsungPayWalletPaymentMethodAllOf.md)
 - [DeleteBrandingStyleConfigurationResponse](docs/DeleteBrandingStyleConfigurationResponse.md)
 - [Device](docs/Device.md)
 - [Disbursement](docs/Disbursement.md)
 - [DisbursementTransactionType](docs/DisbursementTransactionType.md)
 - [Document](docs/Document.md)
 - [DynamicPricing](docs/DynamicPricing.md)
 - [DynamicPricingAllOf](docs/DynamicPricingAllOf.md)
 - [DynamicPricingExchangeRateRequest](docs/DynamicPricingExchangeRateRequest.md)
 - [DynamicPricingExchangeRateRequestAllOf](docs/DynamicPricingExchangeRateRequestAllOf.md)
 - [EmailNotificationData](docs/EmailNotificationData.md)
 - [EncryptedApplePay](docs/EncryptedApplePay.md)
 - [EncryptedApplePayHeader](docs/EncryptedApplePayHeader.md)
 - [EncryptedApplePayWalletPaymentMethod](docs/EncryptedApplePayWalletPaymentMethod.md)
 - [EncryptedApplePayWalletPaymentMethodAllOf](docs/EncryptedApplePayWalletPaymentMethodAllOf.md)
 - [EncryptedGooglePay](docs/EncryptedGooglePay.md)
 - [EncryptedGooglePayData](docs/EncryptedGooglePayData.md)
 - [EncryptedGooglePayWalletPaymentMethod](docs/EncryptedGooglePayWalletPaymentMethod.md)
 - [EncryptedGooglePayWalletPaymentMethodAllOf](docs/EncryptedGooglePayWalletPaymentMethodAllOf.md)
 - [EncryptedSamsungPay](docs/EncryptedSamsungPay.md)
 - [EncryptedSamsungPayWalletPaymentMethod](docs/EncryptedSamsungPayWalletPaymentMethod.md)
 - [EncryptedSamsungPayWalletPaymentMethodAllOf](docs/EncryptedSamsungPayWalletPaymentMethodAllOf.md)
 - [EndpointResponse](docs/EndpointResponse.md)
 - [Error](docs/Error.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [ErrorMessage](docs/ErrorMessage.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExchangeRateDetails](docs/ExchangeRateDetails.md)
 - [ExchangeRateRequest](docs/ExchangeRateRequest.md)
 - [ExchangeRateResponse](docs/ExchangeRateResponse.md)
 - [Expiration](docs/Expiration.md)
 - [FontFace](docs/FontFace.md)
 - [FontProperties](docs/FontProperties.md)
 - [FontWeight](docs/FontWeight.md)
 - [Footer](docs/Footer.md)
 - [FraudAddress](docs/FraudAddress.md)
 - [FraudOrder](docs/FraudOrder.md)
 - [FraudOrderItems](docs/FraudOrderItems.md)
 - [FraudRegistration](docs/FraudRegistration.md)
 - [FraudRegistrationCard](docs/FraudRegistrationCard.md)
 - [FraudRegistrationDevice](docs/FraudRegistrationDevice.md)
 - [FraudRegistrationDeviceItems](docs/FraudRegistrationDeviceItems.md)
 - [FraudRegistrationError](docs/FraudRegistrationError.md)
 - [FraudRegistrationResponse](docs/FraudRegistrationResponse.md)
 - [FraudScore](docs/FraudScore.md)
 - [FraudSettings](docs/FraudSettings.md)
 - [FraudSettingsResponse](docs/FraudSettingsResponse.md)
 - [Frequency](docs/Frequency.md)
 - [FundingTransactionType](docs/FundingTransactionType.md)
 - [Header](docs/Header.md)
 - [Hover](docs/Hover.md)
 - [IdInfo](docs/IdInfo.md)
 - [IndustrySpecificExtensions](docs/IndustrySpecificExtensions.md)
 - [InitiateClearingResponse](docs/InitiateClearingResponse.md)
 - [InitiateClearingResponseAllOf](docs/InitiateClearingResponseAllOf.md)
 - [InstallmentOptions](docs/InstallmentOptions.md)
 - [IssuerResponse](docs/IssuerResponse.md)
 - [Items](docs/Items.md)
 - [Location](docs/Location.md)
 - [LockoutTime](docs/LockoutTime.md)
 - [Lodging](docs/Lodging.md)
 - [LodgingExtraCharges](docs/LodgingExtraCharges.md)
 - [Logo](docs/Logo.md)
 - [Loyalty](docs/Loyalty.md)
 - [MasterpassWalletPaymentMethod](docs/MasterpassWalletPaymentMethod.md)
 - [MasterpassWalletPaymentMethodAllOf](docs/MasterpassWalletPaymentMethodAllOf.md)
 - [MaximumPurchaseAmount](docs/MaximumPurchaseAmount.md)
 - [Mcc6012](docs/Mcc6012.md)
 - [Merchant](docs/Merchant.md)
 - [Method](docs/Method.md)
 - [Mobile](docs/Mobile.md)
 - [MobileHeaderArea](docs/MobileHeaderArea.md)
 - [Order](docs/Order.md)
 - [OrderErrorResponse](docs/OrderErrorResponse.md)
 - [OrderResponse](docs/OrderResponse.md)
 - [PayPal](docs/PayPal.md)
 - [PayPalPaymentMethod](docs/PayPalPaymentMethod.md)
 - [PayPalPaymentMethodAllOf](docs/PayPalPaymentMethodAllOf.md)
 - [Payment](docs/Payment.md)
 - [PaymentCard](docs/PaymentCard.md)
 - [PaymentCardCreditTransaction](docs/PaymentCardCreditTransaction.md)
 - [PaymentCardDisbursementTransaction](docs/PaymentCardDisbursementTransaction.md)
 - [PaymentCardDisbursementTransactionAllOf](docs/PaymentCardDisbursementTransactionAllOf.md)
 - [PaymentCardForcedTicketTransaction](docs/PaymentCardForcedTicketTransaction.md)
 - [PaymentCardForcedTicketTransactionAllOf](docs/PaymentCardForcedTicketTransactionAllOf.md)
 - [PaymentCardInfoLookupRequest](docs/PaymentCardInfoLookupRequest.md)
 - [PaymentCardInfoLookupRequestAllOf](docs/PaymentCardInfoLookupRequestAllOf.md)
 - [PaymentCardPayerAuthTransaction](docs/PaymentCardPayerAuthTransaction.md)
 - [PaymentCardPayerAuthTransactionAllOf](docs/PaymentCardPayerAuthTransactionAllOf.md)
 - [PaymentCardPaymentMethod](docs/PaymentCardPaymentMethod.md)
 - [PaymentCardPaymentMethodAllOf](docs/PaymentCardPaymentMethodAllOf.md)
 - [PaymentCardPaymentTokenUpdateRequest](docs/PaymentCardPaymentTokenUpdateRequest.md)
 - [PaymentCardPaymentTokenizationRequest](docs/PaymentCardPaymentTokenizationRequest.md)
 - [PaymentCardPaymentTokenizationRequestAllOf](docs/PaymentCardPaymentTokenizationRequestAllOf.md)
 - [PaymentCardPreAuthTransaction](docs/PaymentCardPreAuthTransaction.md)
 - [PaymentCardPreAuthTransactionAllOf](docs/PaymentCardPreAuthTransactionAllOf.md)
 - [PaymentCardSaleTransaction](docs/PaymentCardSaleTransaction.md)
 - [PaymentCardSaleTransactionAllOf](docs/PaymentCardSaleTransactionAllOf.md)
 - [PaymentCardVerificationRequest](docs/PaymentCardVerificationRequest.md)
 - [PaymentCardVerificationRequestAllOf](docs/PaymentCardVerificationRequestAllOf.md)
 - [PaymentDevice](docs/PaymentDevice.md)
 - [PaymentDeviceCreditTransaction](docs/PaymentDeviceCreditTransaction.md)
 - [PaymentDeviceCreditTransactionAllOf](docs/PaymentDeviceCreditTransactionAllOf.md)
 - [PaymentDeviceDisbursementTransaction](docs/PaymentDeviceDisbursementTransaction.md)
 - [PaymentDeviceDisbursementTransactionAllOf](docs/PaymentDeviceDisbursementTransactionAllOf.md)
 - [PaymentDevicePaymentMethod](docs/PaymentDevicePaymentMethod.md)
 - [PaymentDevicePaymentMethodAllOf](docs/PaymentDevicePaymentMethodAllOf.md)
 - [PaymentDevicePaymentTokenizationRequest](docs/PaymentDevicePaymentTokenizationRequest.md)
 - [PaymentDevicePaymentTokenizationRequestAllOf](docs/PaymentDevicePaymentTokenizationRequestAllOf.md)
 - [PaymentDevicePreAuthTransaction](docs/PaymentDevicePreAuthTransaction.md)
 - [PaymentDevicePreAuthTransactionAllOf](docs/PaymentDevicePreAuthTransactionAllOf.md)
 - [PaymentDeviceSaleTransaction](docs/PaymentDeviceSaleTransaction.md)
 - [PaymentDeviceSaleTransactionAllOf](docs/PaymentDeviceSaleTransactionAllOf.md)
 - [PaymentFacilitator](docs/PaymentFacilitator.md)
 - [PaymentMethodDetails](docs/PaymentMethodDetails.md)
 - [PaymentMethodPaymentSchedulesRequest](docs/PaymentMethodPaymentSchedulesRequest.md)
 - [PaymentMethodPaymentSchedulesRequestAllOf](docs/PaymentMethodPaymentSchedulesRequestAllOf.md)
 - [PaymentMethodType](docs/PaymentMethodType.md)
 - [PaymentRegistration](docs/PaymentRegistration.md)
 - [PaymentSchedulesErrorResponse](docs/PaymentSchedulesErrorResponse.md)
 - [PaymentSchedulesRequest](docs/PaymentSchedulesRequest.md)
 - [PaymentSchedulesResponse](docs/PaymentSchedulesResponse.md)
 - [PaymentTokenCreditTransaction](docs/PaymentTokenCreditTransaction.md)
 - [PaymentTokenCreditTransactionAllOf](docs/PaymentTokenCreditTransactionAllOf.md)
 - [PaymentTokenDetails](docs/PaymentTokenDetails.md)
 - [PaymentTokenDetailsAllOf](docs/PaymentTokenDetailsAllOf.md)
 - [PaymentTokenDisbursementTransaction](docs/PaymentTokenDisbursementTransaction.md)
 - [PaymentTokenDisbursementTransactionAllOf](docs/PaymentTokenDisbursementTransactionAllOf.md)
 - [PaymentTokenInfoLookupRequest](docs/PaymentTokenInfoLookupRequest.md)
 - [PaymentTokenInfoLookupRequestAllOf](docs/PaymentTokenInfoLookupRequestAllOf.md)
 - [PaymentTokenPaymentMethod](docs/PaymentTokenPaymentMethod.md)
 - [PaymentTokenPaymentMethodAllOf](docs/PaymentTokenPaymentMethodAllOf.md)
 - [PaymentTokenPreAuthTransaction](docs/PaymentTokenPreAuthTransaction.md)
 - [PaymentTokenPreAuthTransactionAllOf](docs/PaymentTokenPreAuthTransactionAllOf.md)
 - [PaymentTokenSaleTransaction](docs/PaymentTokenSaleTransaction.md)
 - [PaymentTokenSaleTransactionAllOf](docs/PaymentTokenSaleTransactionAllOf.md)
 - [PaymentTokenUpdateResponse](docs/PaymentTokenUpdateResponse.md)
 - [PaymentTokenVerificationRequest](docs/PaymentTokenVerificationRequest.md)
 - [PaymentTokenVerificationRequestAllOf](docs/PaymentTokenVerificationRequestAllOf.md)
 - [PaymentTokenizationErrorResponse](docs/PaymentTokenizationErrorResponse.md)
 - [PaymentTokenizationRequest](docs/PaymentTokenizationRequest.md)
 - [PaymentTokenizationResponse](docs/PaymentTokenizationResponse.md)
 - [PaymentUrlDetail](docs/PaymentUrlDetail.md)
 - [PaymentUrlDetailResponse](docs/PaymentUrlDetailResponse.md)
 - [PaymentUrlErrorResponse](docs/PaymentUrlErrorResponse.md)
 - [PaymentUrlRequest](docs/PaymentUrlRequest.md)
 - [PaymentUrlResponse](docs/PaymentUrlResponse.md)
 - [PaymentUrlStatus](docs/PaymentUrlStatus.md)
 - [PaypalCreditTransaction](docs/PaypalCreditTransaction.md)
 - [PaypalCreditTransactionAllOf](docs/PaypalCreditTransactionAllOf.md)
 - [Phone](docs/Phone.md)
 - [PostAuthTransaction](docs/PostAuthTransaction.md)
 - [PostAuthTransactionAllOf](docs/PostAuthTransactionAllOf.md)
 - [Primary](docs/Primary.md)
 - [PrimaryTransaction](docs/PrimaryTransaction.md)
 - [ProcessorData](docs/ProcessorData.md)
 - [Properties](docs/Properties.md)
 - [PurchaseCards](docs/PurchaseCards.md)
 - [PurchaseCardsLevel2](docs/PurchaseCardsLevel2.md)
 - [PurchaseCardsLevel3](docs/PurchaseCardsLevel3.md)
 - [PurchaseCardsLevel3LineItems](docs/PurchaseCardsLevel3LineItems.md)
 - [Receipt](docs/Receipt.md)
 - [ReceiptLine](docs/ReceiptLine.md)
 - [ReceiptRequestInfo](docs/ReceiptRequestInfo.md)
 - [ReceiverInfo](docs/ReceiverInfo.md)
 - [RecurringPaymentDetails](docs/RecurringPaymentDetails.md)
 - [RecurringPaymentDetailsResponse](docs/RecurringPaymentDetailsResponse.md)
 - [ReferencedOrderPaymentSchedulesRequest](docs/ReferencedOrderPaymentSchedulesRequest.md)
 - [ReferencedOrderPaymentSchedulesRequestAllOf](docs/ReferencedOrderPaymentSchedulesRequestAllOf.md)
 - [ReferencedOrderPaymentTokenizationRequest](docs/ReferencedOrderPaymentTokenizationRequest.md)
 - [ReferencedOrderPaymentTokenizationRequestAllOf](docs/ReferencedOrderPaymentTokenizationRequestAllOf.md)
 - [RegistrationMethod](docs/RegistrationMethod.md)
 - [RemoveFraudBlockedItemsResponse](docs/RemoveFraudBlockedItemsResponse.md)
 - [ResponseAmountComponents](docs/ResponseAmountComponents.md)
 - [ResponseAmountComponentsAllOf](docs/ResponseAmountComponentsAllOf.md)
 - [ResponseType](docs/ResponseType.md)
 - [ReturnTransaction](docs/ReturnTransaction.md)
 - [ReturnTransactionAllOf](docs/ReturnTransactionAllOf.md)
 - [ScoreOnlyRequest](docs/ScoreOnlyRequest.md)
 - [ScoreOnlyResponse](docs/ScoreOnlyResponse.md)
 - [ScoreOnlyResponseFraudScore](docs/ScoreOnlyResponseFraudScore.md)
 - [ScoreOnlyResponseFraudScoreExplanations](docs/ScoreOnlyResponseFraudScoreExplanations.md)
 - [SecondaryTransaction](docs/SecondaryTransaction.md)
 - [Secure3D10AuthenticationRequest](docs/Secure3D10AuthenticationRequest.md)
 - [Secure3D10AuthenticationResult](docs/Secure3D10AuthenticationResult.md)
 - [Secure3D10AuthenticationResultAllOf](docs/Secure3D10AuthenticationResultAllOf.md)
 - [Secure3D10AuthenticationUpdateRequest](docs/Secure3D10AuthenticationUpdateRequest.md)
 - [Secure3D10AuthenticationUpdateRequestAllOf](docs/Secure3D10AuthenticationUpdateRequestAllOf.md)
 - [Secure3D21AuthenticationRequest](docs/Secure3D21AuthenticationRequest.md)
 - [Secure3D21AuthenticationRequestAllOf](docs/Secure3D21AuthenticationRequestAllOf.md)
 - [Secure3D21AuthenticationResult](docs/Secure3D21AuthenticationResult.md)
 - [Secure3D21AuthenticationResultAllOf](docs/Secure3D21AuthenticationResultAllOf.md)
 - [Secure3D21AuthenticationUpdateRequest](docs/Secure3D21AuthenticationUpdateRequest.md)
 - [Secure3D21AuthenticationUpdateRequestAllOf](docs/Secure3D21AuthenticationUpdateRequestAllOf.md)
 - [Secure3DAuthenticationResponse](docs/Secure3DAuthenticationResponse.md)
 - [Secure3DAuthenticationResponseParams](docs/Secure3DAuthenticationResponseParams.md)
 - [Secure3DAuthenticationResponseSecure3dMethod](docs/Secure3DAuthenticationResponseSecure3dMethod.md)
 - [Secure3dResponse](docs/Secure3dResponse.md)
 - [SenderInfo](docs/SenderInfo.md)
 - [Sepa](docs/Sepa.md)
 - [SepaMandate](docs/SepaMandate.md)
 - [SepaPaymentMethod](docs/SepaPaymentMethod.md)
 - [SepaPaymentMethodAllOf](docs/SepaPaymentMethodAllOf.md)
 - [SepaSaleTransaction](docs/SepaSaleTransaction.md)
 - [SepaSaleTransactionAllOf](docs/SepaSaleTransactionAllOf.md)
 - [SharedSecretConfigurationRequest](docs/SharedSecretConfigurationRequest.md)
 - [SharedSecretConfigurationResponse](docs/SharedSecretConfigurationResponse.md)
 - [ShipToAddress](docs/ShipToAddress.md)
 - [Shipping](docs/Shipping.md)
 - [SoftDescriptor](docs/SoftDescriptor.md)
 - [SplitShipment](docs/SplitShipment.md)
 - [StoreBrandingStyleConfiguration](docs/StoreBrandingStyleConfiguration.md)
 - [StoreEmailSettings](docs/StoreEmailSettings.md)
 - [StoreEmailSettingsResult](docs/StoreEmailSettingsResult.md)
 - [StoreFraudSettings](docs/StoreFraudSettings.md)
 - [StoreFraudSettingsResult](docs/StoreFraudSettingsResult.md)
 - [StoreUrlConfiguration](docs/StoreUrlConfiguration.md)
 - [StoreUrlConfigurationRequest](docs/StoreUrlConfigurationRequest.md)
 - [StoreUrlConfigurationResponse](docs/StoreUrlConfigurationResponse.md)
 - [StoreUrlConfigurationResult](docs/StoreUrlConfigurationResult.md)
 - [StoredCredential](docs/StoredCredential.md)
 - [SubMerchantData](docs/SubMerchantData.md)
 - [SubMerchantSplit](docs/SubMerchantSplit.md)
 - [TeleCheckAchPaymentMethod](docs/TeleCheckAchPaymentMethod.md)
 - [TeleCheckAchPaymentMethodAchBillTo](docs/TeleCheckAchPaymentMethodAchBillTo.md)
 - [TeleCheckCBPPaymentMethod](docs/TeleCheckCBPPaymentMethod.md)
 - [TeleCheckICAPaymentMethod](docs/TeleCheckICAPaymentMethod.md)
 - [TeleCheckICAPaymentMethodAllOf](docs/TeleCheckICAPaymentMethodAllOf.md)
 - [Text](docs/Text.md)
 - [Title](docs/Title.md)
 - [TokenIdentifier](docs/TokenIdentifier.md)
 - [TopBar](docs/TopBar.md)
 - [TransactionErrorResponse](docs/TransactionErrorResponse.md)
 - [TransactionOrigin](docs/TransactionOrigin.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [TransactionType](docs/TransactionType.md)
 - [UnionPayAuthenticationRequest](docs/UnionPayAuthenticationRequest.md)
 - [UnionPayAuthenticationRequestAllOf](docs/UnionPayAuthenticationRequestAllOf.md)
 - [UnionPayAuthenticationUpdateRequest](docs/UnionPayAuthenticationUpdateRequest.md)
 - [UnionPayAuthenticationUpdateRequestAllOf](docs/UnionPayAuthenticationUpdateRequestAllOf.md)
 - [UpdateEmailSettingsRequest](docs/UpdateEmailSettingsRequest.md)
 - [UpdateEmailSettingsResponse](docs/UpdateEmailSettingsResponse.md)
 - [UpdateFraudSettingsRequest](docs/UpdateFraudSettingsRequest.md)
 - [UpdateFraudSettingsResponse](docs/UpdateFraudSettingsResponse.md)
 - [UpdatePaymentToken](docs/UpdatePaymentToken.md)
 - [UsePaymentToken](docs/UsePaymentToken.md)
 - [Verification3ds](docs/Verification3ds.md)
 - [VerificationAvs](docs/VerificationAvs.md)
 - [VerificationCvv](docs/VerificationCvv.md)
 - [VoidPreAuthTransactions](docs/VoidPreAuthTransactions.md)
 - [VoidTransaction](docs/VoidTransaction.md)
 - [VoidTransactionAllOf](docs/VoidTransactionAllOf.md)
 - [WalletPaymentMethod](docs/WalletPaymentMethod.md)
 - [WalletPreAuthTransaction](docs/WalletPreAuthTransaction.md)
 - [WalletPreAuthTransactionAllOf](docs/WalletPreAuthTransactionAllOf.md)
 - [WalletSaleTransaction](docs/WalletSaleTransaction.md)
 - [WalletSaleTransactionAllOf](docs/WalletSaleTransactionAllOf.md)


## Documentation For Authorization

 All endpoints do not require authorization.
