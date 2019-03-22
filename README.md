# First Data Gateway
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

All URIs are relative to *https://cert.api.firstdata.com/gateway*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**v1_authentication_access_tokens_post**](docs/AuthenticationApi.md#v1_authentication_access_tokens_post) | **POST** /v1/authentication/access-tokens | Generate an access token for user authentication.
*CardInfoLookupApi* | [**card_info_lookup**](docs/CardInfoLookupApi.md#card_info_lookup) | **POST** /v1/card-information | Card information lookUp
*CardVerificationApi* | [**verify_card**](docs/CardVerificationApi.md#verify_card) | **POST** /v1/card-verification | Verify a payment card.
*CurrencyConversionApi* | [**get_exchange_rate**](docs/CurrencyConversionApi.md#get_exchange_rate) | **POST** /v1/exchange-rates | Generate dynamic currency conversion transactions
*FraudDetectApi* | [**score_only**](docs/FraudDetectApi.md#score_only) | **POST** /v1/fraud/score-only | Score a transaction for fraud.
*OrderApi* | [**order_inquiry**](docs/OrderApi.md#order_inquiry) | **GET** /v1/orders/{order-id} | Retrieve the state of an order
*OrderApi* | [**order_post_auth**](docs/OrderApi.md#order_post_auth) | **POST** /v1/orders/{order-id}/postauth | Capture/complete an already existing order.
*OrderApi* | [**order_return_transaction**](docs/OrderApi.md#order_return_transaction) | **POST** /v1/orders/{order-id}/return | Return/refund an order.
*PaymentApi* | [**finalize_secure_transaction**](docs/PaymentApi.md#finalize_secure_transaction) | **PATCH** /v1/payments/{transaction-id} | Update a 3DSecure or UnionPay payment and continue processing.
*PaymentApi* | [**perform_payment_post_authorisation**](docs/PaymentApi.md#perform_payment_post_authorisation) | **POST** /v1/payments/{transaction-id}/postauth | Capture/complete a transaction.
*PaymentApi* | [**primary_payment_transaction**](docs/PaymentApi.md#primary_payment_transaction) | **POST** /v1/payments | Generate a primary transaction.
*PaymentApi* | [**return_transaction**](docs/PaymentApi.md#return_transaction) | **POST** /v1/payments/{transaction-id}/return | Return/refund a transaction.
*PaymentApi* | [**transaction_inquiry**](docs/PaymentApi.md#transaction_inquiry) | **GET** /v1/payments/{transaction-id} | Retrieve the state of a transaction.
*PaymentApi* | [**void_transaction**](docs/PaymentApi.md#void_transaction) | **POST** /v1/payments/{transaction-id}/void | Reverse a previous action on an existing transaction.
*PaymentSchedulesApi* | [**cancel_payment_schedule**](docs/PaymentSchedulesApi.md#cancel_payment_schedule) | **DELETE** /v1/payment-schedules/{order-id} | Cancel a gateway payment schedule.
*PaymentSchedulesApi* | [**create_payment_schedule**](docs/PaymentSchedulesApi.md#create_payment_schedule) | **POST** /v1/payment-schedules | Use this to create a gateway payment schedule.
*PaymentSchedulesApi* | [**inquiry_payment_schedule**](docs/PaymentSchedulesApi.md#inquiry_payment_schedule) | **GET** /v1/payment-schedules/{order-id} | View a gateway payment schedule.
*PaymentSchedulesApi* | [**update_payment_schedule**](docs/PaymentSchedulesApi.md#update_payment_schedule) | **PATCH** /v1/payment-schedules/{order-id} | Update a gateway payment schedule.
*PaymentTokenApi* | [**create_payment_token**](docs/PaymentTokenApi.md#create_payment_token) | **POST** /v1/payment-tokens | Create a payment token from a payment card.
*PaymentTokenApi* | [**delete_payment_token**](docs/PaymentTokenApi.md#delete_payment_token) | **DELETE** /v1/payment-tokens/{token-id} | Delete a payment token.
*PaymentURLApi* | [**create_payment_url**](docs/PaymentURLApi.md#create_payment_url) | **POST** /v1/payment-url | Create a payment URL.


## Documentation For Models

 - [AVSResponse](docs/AVSResponse.md)
 - [AccessTokenResponse](docs/AccessTokenResponse.md)
 - [AdditionalAmountRate](docs/AdditionalAmountRate.md)
 - [AdditionalTransactionDetails](docs/AdditionalTransactionDetails.md)
 - [Address](docs/Address.md)
 - [Airline](docs/Airline.md)
 - [AirlineAncillaryServiceCategory](docs/AirlineAncillaryServiceCategory.md)
 - [AirlineTravelRoute](docs/AirlineTravelRoute.md)
 - [AliPay](docs/AliPay.md)
 - [Amount](docs/Amount.md)
 - [AmountComponents](docs/AmountComponents.md)
 - [AuthenticationRequest](docs/AuthenticationRequest.md)
 - [AuthenticationResponseVerification](docs/AuthenticationResponseVerification.md)
 - [AuthenticationResponseVerificationRequest](docs/AuthenticationResponseVerificationRequest.md)
 - [BasicResponse](docs/BasicResponse.md)
 - [BasketItem](docs/BasketItem.md)
 - [Billing](docs/Billing.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [BillingAddressPhone](docs/BillingAddressPhone.md)
 - [CarRental](docs/CarRental.md)
 - [CarRentalExtraCharges](docs/CarRentalExtraCharges.md)
 - [Card](docs/Card.md)
 - [CardInfo](docs/CardInfo.md)
 - [CardInfoLookupRequest](docs/CardInfoLookupRequest.md)
 - [CardInfoLookupResponse](docs/CardInfoLookupResponse.md)
 - [CardVerificationRequest](docs/CardVerificationRequest.md)
 - [CardVerificationsTransaction](docs/CardVerificationsTransaction.md)
 - [ChinaDomestic](docs/ChinaDomestic.md)
 - [ClientLocale](docs/ClientLocale.md)
 - [Contact](docs/Contact.md)
 - [Customer](docs/Customer.md)
 - [CustomerAddress](docs/CustomerAddress.md)
 - [CustomerAddressPhone](docs/CustomerAddressPhone.md)
 - [Dcc](docs/Dcc.md)
 - [Device](docs/Device.md)
 - [DeviceNetworks](docs/DeviceNetworks.md)
 - [Document](docs/Document.md)
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
 - [Payment](docs/Payment.md)
 - [PaymentCard](docs/PaymentCard.md)
 - [PaymentCardAuthenticationResult](docs/PaymentCardAuthenticationResult.md)
 - [PaymentFacilitator](docs/PaymentFacilitator.md)
 - [PaymentIssuerResponse](docs/PaymentIssuerResponse.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentPayMethod](docs/PaymentPayMethod.md)
 - [PaymentSchedulesErrorResponse](docs/PaymentSchedulesErrorResponse.md)
 - [PaymentSchedulesRequest](docs/PaymentSchedulesRequest.md)
 - [PaymentSchedulesResponse](docs/PaymentSchedulesResponse.md)
 - [PaymentTokenization](docs/PaymentTokenization.md)
 - [PaymentTokenizationErrorResponse](docs/PaymentTokenizationErrorResponse.md)
 - [PaymentTokenizationRequest](docs/PaymentTokenizationRequest.md)
 - [PaymentTokenizationResponse](docs/PaymentTokenizationResponse.md)
 - [PaymentUrlErrorResponse](docs/PaymentUrlErrorResponse.md)
 - [PaymentUrlRequest](docs/PaymentUrlRequest.md)
 - [PaymentUrlResponse](docs/PaymentUrlResponse.md)
 - [PaymentVerification3ds](docs/PaymentVerification3ds.md)
 - [PaymentVerificationAvs](docs/PaymentVerificationAvs.md)
 - [PaymentVerificationCvv](docs/PaymentVerificationCvv.md)
 - [PrimaryTransaction](docs/PrimaryTransaction.md)
 - [PrimaryTransactionAdditionalDetails](docs/PrimaryTransactionAdditionalDetails.md)
 - [ProcessorData](docs/ProcessorData.md)
 - [PurchaseCards](docs/PurchaseCards.md)
 - [PurchaseCardsLevel2](docs/PurchaseCardsLevel2.md)
 - [PurchaseCardsLevel3](docs/PurchaseCardsLevel3.md)
 - [PurchaseCardsLevel3LineItems](docs/PurchaseCardsLevel3LineItems.md)
 - [RecurringPaymentDetails](docs/RecurringPaymentDetails.md)
 - [RecurringPaymentDetailsResponse](docs/RecurringPaymentDetailsResponse.md)
 - [ReferencedOrder](docs/ReferencedOrder.md)
 - [ResponseType](docs/ResponseType.md)
 - [ScoreOnlyRequest](docs/ScoreOnlyRequest.md)
 - [ScoreOnlyResponse](docs/ScoreOnlyResponse.md)
 - [ScoreOnlyResponseFraudScore](docs/ScoreOnlyResponseFraudScore.md)
 - [ScoreOnlyResponseFraudScoreExplanations](docs/ScoreOnlyResponseFraudScoreExplanations.md)
 - [SecondaryTransaction](docs/SecondaryTransaction.md)
 - [SecondaryTransactionAdditionalDetails](docs/SecondaryTransactionAdditionalDetails.md)
 - [Secure3dResponse](docs/Secure3dResponse.md)
 - [Sepa](docs/Sepa.md)
 - [SepaMandate](docs/SepaMandate.md)
 - [Shipping](docs/Shipping.md)
 - [SoftDescriptor](docs/SoftDescriptor.md)
 - [SplitShipment](docs/SplitShipment.md)
 - [StoredCredential](docs/StoredCredential.md)
 - [SubMerchantData](docs/SubMerchantData.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionErrorResponse](docs/TransactionErrorResponse.md)
 - [TransactionOrigin](docs/TransactionOrigin.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [TransactionType](docs/TransactionType.md)




