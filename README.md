# FirstApiClient
## Requirements

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install first_api_client
```
(you may need to run `pip` with root permission: `sudo pip install first_api_client`)

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
import swagger_client
import simple
from simple import MerchantCredentials
from simple import Gateway
from swagger_client.rest import ApiException
from pprint import pprint

api_key = "Your API Key here"
api_secret = "Your API Secret here"

credentials = MerchantCredentials(api_key, api_secret)

gateway = Gateway.create(credentials)

payload = 	"""{ 
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

result = gateway.primary_payment_transaction(payload)
pprint(result)

```

## Documentation for API Endpoints

All URIs are relative to *https://cert.api.firstdata.com/gateway*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**v1_authentication_access_tokens_post**](docs/AuthenticationApi.md#v1_authentication_access_tokens_post) | **POST** /v1/authentication/access-tokens | Generate an access token for user authentication
*OrderApi* | [**perform_payment_post_authorisation**](docs/OrderApi.md#perform_payment_post_authorisation) | **POST** /v1/orders/{order-id}/postauth | Use this to capture/complete a transaction. Partial postauths are allowed.
*OrderApi* | [**return_transaction**](docs/OrderApi.md#return_transaction) | **POST** /v1/orders/{order-id}/return | Use this to return/refund on the order. Partial returns are allowed.
*PaymentApi* | [**perform_payment_post_authorisation**](docs/PaymentApi.md#perform_payment_post_authorisation) | **POST** /v1/payments/{transaction-id}/postauth | Use this to capture/complete a transaction. Partial postauths are allowed.
*PaymentApi* | [**primary_payment_transaction**](docs/PaymentApi.md#primary_payment_transaction) | **POST** /v1/payments | Generate a primary transaction
*PaymentApi* | [**return_transaction**](docs/PaymentApi.md#return_transaction) | **POST** /v1/payments/{transaction-id}/return | Return/refund a transaction.
*PaymentApi* | [**transaction_inquiry**](docs/PaymentApi.md#transaction_inquiry) | **GET** /v1/payments/{transaction-id} | Retrieve the state of a transaction
*PaymentApi* | [**void_transaction**](docs/PaymentApi.md#void_transaction) | **POST** /v1/payments/{transaction-id}/void | Reverse a previous action on an existing transaction


## Documentation For Models

 - [AccessTokenResponse](docs/AccessTokenResponse.md)
 - [Address](docs/Address.md)
 - [Airline](docs/Airline.md)
 - [AirlineAncillaryServiceCategory](docs/AirlineAncillaryServiceCategory.md)
 - [AirlineTravelRoute](docs/AirlineTravelRoute.md)
 - [Amount](docs/Amount.md)
 - [AmountComponents](docs/AmountComponents.md)
 - [AuthenticationResponseVerification](docs/AuthenticationResponseVerification.md)
 - [BasketItem](docs/BasketItem.md)
 - [Billing](docs/Billing.md)
 - [CarRental](docs/CarRental.md)
 - [CarRentalExtraCharges](docs/CarRentalExtraCharges.md)
 - [CardVerificationsTransaction](docs/CardVerificationsTransaction.md)
 - [ClientLocale](docs/ClientLocale.md)
 - [Contact](docs/Contact.md)
 - [Error](docs/Error.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Expiration](docs/Expiration.md)
 - [Frequency](docs/Frequency.md)
 - [IndustrySpecificExtensions](docs/IndustrySpecificExtensions.md)
 - [InstallmentOptions](docs/InstallmentOptions.md)
 - [Lodging](docs/Lodging.md)
 - [LodgingExtraCharges](docs/LodgingExtraCharges.md)
 - [Order](docs/Order.md)
 - [PayPal](docs/PayPal.md)
 - [PaymentCard](docs/PaymentCard.md)
 - [PaymentCardAuthenticationRequest](docs/PaymentCardAuthenticationRequest.md)
 - [PaymentCardAuthenticationResult](docs/PaymentCardAuthenticationResult.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentSchedulesRequest](docs/PaymentSchedulesRequest.md)
 - [PaymentSchedulesResponse](docs/PaymentSchedulesResponse.md)
 - [PaymentUrlRequest](docs/PaymentUrlRequest.md)
 - [PaymentUrlResponse](docs/PaymentUrlResponse.md)
 - [PrimaryTransaction](docs/PrimaryTransaction.md)
 - [PrimaryTransactionAdditionalDetails](docs/PrimaryTransactionAdditionalDetails.md)
 - [ProcessorData](docs/ProcessorData.md)
 - [ResponseType](docs/ResponseType.md)
 - [SecondaryTransaction](docs/SecondaryTransaction.md)
 - [Sepa](docs/Sepa.md)
 - [SepaMandate](docs/SepaMandate.md)
 - [Shipping](docs/Shipping.md)
 - [SplitShipment](docs/SplitShipment.md)
 - [StoredCredential](docs/StoredCredential.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [TransactionResponseAuthenticationRedirect](docs/TransactionResponseAuthenticationRedirect.md)
 - [TransactionResponseAuthenticationRedirectParams](docs/TransactionResponseAuthenticationRedirectParams.md)
 - [TransactionType](docs/TransactionType.md)
 - [TransactionErrorResponse](docs/TransactionErrorResponse.md)

