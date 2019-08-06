# openapi-client# First Data Gateway
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
from simple import ObjectBuilder
from openapi_client.rest import ApiException
from pprint import pprint

api_key = "Your API Key here"
api_secret = "Your API Secret here"

credentials = MerchantCredentials(api_key, api_secret)

gateway = Gateway.create(credentials)

json_payload = 	"""{ 
			\"amount\":{
					\"currency\":\"USD\",
					\"total\":\"12.10\"
				},
				\"paymentMethod\":{
					\"paymentCard\":{
						\"expiryDate\":{
							\"month\":\"12\",
							\"year\":\"21\"
						},
						\"number\":\"4111111111111111\"
					},
					\"type\":\"PAYMENT_CARD\"
				},
				\"transactionType\":\"SALE\"
			}"""

payload = ObjectBuilder.build("PrimaryTransaction", json_payload)

result = gateway.primary_payment_transaction(payload)
pprint(result)

```

## Documentation for API Endpoints

All URIs are relative to *https://cert.api.firstdata.com/gateway/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**authentication_access_tokens_post**](docs/AuthenticationApi.md#authentication_access_tokens_post) | **POST** /authentication/access-tokens | Generate an access token for user authentication.
*CardInfoLookupApi* | [**card_info_lookup**](docs/CardInfoLookupApi.md#card_info_lookup) | **POST** /card-information | Card information lookup.
*CardVerificationApi* | [**verify_card**](docs/CardVerificationApi.md#verify_card) | **POST** /card-verification | Verify a payment card.
*CurrencyConversionApi* | [**get_exchange_rate**](docs/CurrencyConversionApi.md#get_exchange_rate) | **POST** /exchange-rates | Generate dynamic currency conversion transactions.
*FraudDetectApi* | [**score_only**](docs/FraudDetectApi.md#score_only) | **POST** /fraud/score-only | Score a transaction for fraud.
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
*PaymentURLApi* | [**create_payment_url**](docs/PaymentURLApi.md#create_payment_url) | **POST** /payment-url | Create a payment URL.


## Documentation For Models

 - [AVSResponse](docs/AVSResponse.md)
 - [AccessTokenResponse](docs/AccessTokenResponse.md)
 - [AccountUpdaterResponse](docs/AccountUpdaterResponse.md)
 - [AdditionalAmountRate](docs/AdditionalAmountRate.md)
 - [AdditionalDetails](docs/AdditionalDetails.md)
 - [AdditionalTransactionDetails](docs/AdditionalTransactionDetails.md)
 - [Address](docs/Address.md)
 - [Airline](docs/Airline.md)
 - [AirlineAncillaryServiceCategory](docs/AirlineAncillaryServiceCategory.md)
 - [AirlineTravelRoute](docs/AirlineTravelRoute.md)
 - [AliPay](docs/AliPay.md)
 - [AliPayPaymentMethod](docs/AliPayPaymentMethod.md)
 - [AliPaySaleTransaction](docs/AliPaySaleTransaction.md)
 - [Amount](docs/Amount.md)
 - [AmountComponents](docs/AmountComponents.md)
 - [Authentication](docs/Authentication.md)
 - [AuthenticationRedirect](docs/AuthenticationRedirect.md)
 - [AuthenticationRedirectParams](docs/AuthenticationRedirectParams.md)
 - [AuthenticationVerificationRequest](docs/AuthenticationVerificationRequest.md)
 - [BasicResponse](docs/BasicResponse.md)
 - [Billing](docs/Billing.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [BillingAddressPhone](docs/BillingAddressPhone.md)
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
 - [ChinaPnRSaleTransaction](docs/ChinaPnRSaleTransaction.md)
 - [ClientLocale](docs/ClientLocale.md)
 - [Contact](docs/Contact.md)
 - [CreatePaymentToken](docs/CreatePaymentToken.md)
 - [CurrencyConversion](docs/CurrencyConversion.md)
 - [Customer](docs/Customer.md)
 - [CustomerAddress](docs/CustomerAddress.md)
 - [CustomerAddressPhone](docs/CustomerAddressPhone.md)
 - [DCCExchangeRateRequest](docs/DCCExchangeRateRequest.md)
 - [Dcc](docs/Dcc.md)
 - [Device](docs/Device.md)
 - [DeviceNetworks](docs/DeviceNetworks.md)
 - [Document](docs/Document.md)
 - [DynamicPricing](docs/DynamicPricing.md)
 - [DynamicPricingExchangeRateRequest](docs/DynamicPricingExchangeRateRequest.md)
 - [Error](docs/Error.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExchangeRateRequest](docs/ExchangeRateRequest.md)
 - [ExchangeRateResponse](docs/ExchangeRateResponse.md)
 - [Expiration](docs/Expiration.md)
 - [FraudOrder](docs/FraudOrder.md)
 - [FraudOrderItems](docs/FraudOrderItems.md)
 - [FraudOrderShipToAddress](docs/FraudOrderShipToAddress.md)
 - [Frequency](docs/Frequency.md)
 - [IndustrySpecificExtensions](docs/IndustrySpecificExtensions.md)
 - [InstallmentOptions](docs/InstallmentOptions.md)
 - [Lodging](docs/Lodging.md)
 - [LodgingExtraCharges](docs/LodgingExtraCharges.md)
 - [Loyalty](docs/Loyalty.md)
 - [Merchant](docs/Merchant.md)
 - [MerchantLocation](docs/MerchantLocation.md)
 - [MerchantLocationMerchantAddress](docs/MerchantLocationMerchantAddress.md)
 - [Order](docs/Order.md)
 - [OrderErrorResponse](docs/OrderErrorResponse.md)
 - [OrderResponse](docs/OrderResponse.md)
 - [PayPal](docs/PayPal.md)
 - [PayPalPaymentMethod](docs/PayPalPaymentMethod.md)
 - [Payment](docs/Payment.md)
 - [PaymentCard](docs/PaymentCard.md)
 - [PaymentCardCreditTransaction](docs/PaymentCardCreditTransaction.md)
 - [PaymentCardForcedTicketTransaction](docs/PaymentCardForcedTicketTransaction.md)
 - [PaymentCardPayerAuthTransaction](docs/PaymentCardPayerAuthTransaction.md)
 - [PaymentCardPaymentMethod](docs/PaymentCardPaymentMethod.md)
 - [PaymentCardPaymentTokenizationRequest](docs/PaymentCardPaymentTokenizationRequest.md)
 - [PaymentCardPreAuthTransaction](docs/PaymentCardPreAuthTransaction.md)
 - [PaymentCardSaleTransaction](docs/PaymentCardSaleTransaction.md)
 - [PaymentFacilitator](docs/PaymentFacilitator.md)
 - [PaymentIssuerResponse](docs/PaymentIssuerResponse.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentMethodDetails](docs/PaymentMethodDetails.md)
 - [PaymentMethodPaymentSchedulesRequest](docs/PaymentMethodPaymentSchedulesRequest.md)
 - [PaymentMethodType](docs/PaymentMethodType.md)
 - [PaymentPayMethod](docs/PaymentPayMethod.md)
 - [PaymentSchedulesErrorResponse](docs/PaymentSchedulesErrorResponse.md)
 - [PaymentSchedulesRequest](docs/PaymentSchedulesRequest.md)
 - [PaymentSchedulesResponse](docs/PaymentSchedulesResponse.md)
 - [PaymentTokenCreditTransaction](docs/PaymentTokenCreditTransaction.md)
 - [PaymentTokenDetails](docs/PaymentTokenDetails.md)
 - [PaymentTokenPaymentMethod](docs/PaymentTokenPaymentMethod.md)
 - [PaymentTokenPreAuthTransaction](docs/PaymentTokenPreAuthTransaction.md)
 - [PaymentTokenSaleTransaction](docs/PaymentTokenSaleTransaction.md)
 - [PaymentTokenizationErrorResponse](docs/PaymentTokenizationErrorResponse.md)
 - [PaymentTokenizationRequest](docs/PaymentTokenizationRequest.md)
 - [PaymentTokenizationResponse](docs/PaymentTokenizationResponse.md)
 - [PaymentUrlErrorResponse](docs/PaymentUrlErrorResponse.md)
 - [PaymentUrlRequest](docs/PaymentUrlRequest.md)
 - [PaymentUrlResponse](docs/PaymentUrlResponse.md)
 - [PaymentVerification3ds](docs/PaymentVerification3ds.md)
 - [PaymentVerificationAvs](docs/PaymentVerificationAvs.md)
 - [PaymentVerificationCvv](docs/PaymentVerificationCvv.md)
 - [PaypalCreditTransaction](docs/PaypalCreditTransaction.md)
 - [PostAuthTransaction](docs/PostAuthTransaction.md)
 - [PrimaryTransaction](docs/PrimaryTransaction.md)
 - [ProcessorData](docs/ProcessorData.md)
 - [PurchaseCards](docs/PurchaseCards.md)
 - [PurchaseCardsLevel2](docs/PurchaseCardsLevel2.md)
 - [PurchaseCardsLevel3](docs/PurchaseCardsLevel3.md)
 - [PurchaseCardsLevel3LineItems](docs/PurchaseCardsLevel3LineItems.md)
 - [RecurringPaymentDetails](docs/RecurringPaymentDetails.md)
 - [RecurringPaymentDetailsResponse](docs/RecurringPaymentDetailsResponse.md)
 - [ReferencedOrderPaymentSchedulesRequest](docs/ReferencedOrderPaymentSchedulesRequest.md)
 - [ReferencedOrderPaymentTokenizationRequest](docs/ReferencedOrderPaymentTokenizationRequest.md)
 - [ResponseAmountComponents](docs/ResponseAmountComponents.md)
 - [ResponseType](docs/ResponseType.md)
 - [ReturnTransaction](docs/ReturnTransaction.md)
 - [ScoreOnlyRequest](docs/ScoreOnlyRequest.md)
 - [ScoreOnlyResponse](docs/ScoreOnlyResponse.md)
 - [ScoreOnlyResponseFraudScore](docs/ScoreOnlyResponseFraudScore.md)
 - [ScoreOnlyResponseFraudScoreExplanations](docs/ScoreOnlyResponseFraudScoreExplanations.md)
 - [SecondaryTransaction](docs/SecondaryTransaction.md)
 - [Secure3dAuthenticationRequest](docs/Secure3dAuthenticationRequest.md)
 - [Secure3dAuthenticationResult](docs/Secure3dAuthenticationResult.md)
 - [Secure3dAuthenticationVerificationRequest](docs/Secure3dAuthenticationVerificationRequest.md)
 - [Secure3dResponse](docs/Secure3dResponse.md)
 - [Sepa](docs/Sepa.md)
 - [SepaMandate](docs/SepaMandate.md)
 - [SepaPaymentMethod](docs/SepaPaymentMethod.md)
 - [SepaSaleTransaction](docs/SepaSaleTransaction.md)
 - [Shipping](docs/Shipping.md)
 - [SoftDescriptor](docs/SoftDescriptor.md)
 - [SplitShipment](docs/SplitShipment.md)
 - [StoredCredential](docs/StoredCredential.md)
 - [SubMerchantData](docs/SubMerchantData.md)
 - [SubMerchantSplit](docs/SubMerchantSplit.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionErrorResponse](docs/TransactionErrorResponse.md)
 - [TransactionOrigin](docs/TransactionOrigin.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [TransactionType](docs/TransactionType.md)
 - [UnionPayAuthenticationRequest](docs/UnionPayAuthenticationRequest.md)
 - [UnionPayAuthenticationVerificationRequest](docs/UnionPayAuthenticationVerificationRequest.md)
 - [UsePaymentToken](docs/UsePaymentToken.md)
 - [VoidTransaction](docs/VoidTransaction.md)
