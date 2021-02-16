# openapi_client.PaymentApi

All URIs are relative to *https://cert.api.firstdata.com/gateway/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finalize_secure_transaction**](PaymentApi.md#finalize_secure_transaction) | **PATCH** /payments/{transaction-id} | Update a 3DSecure or UnionPay payment and continue processing.
[**submit_primary_transaction**](PaymentApi.md#submit_primary_transaction) | **POST** /payments | Generate a primary transaction.
[**submit_secondary_transaction**](PaymentApi.md#submit_secondary_transaction) | **POST** /payments/{transaction-id} | Perform a secondary transaction.
[**transaction_inquiry**](PaymentApi.md#transaction_inquiry) | **GET** /payments/{transaction-id} | Retrieve the state of a transaction.


# **finalize_secure_transaction**
> TransactionResponse finalize_secure_transaction(content_type, client_request_id, api_key, timestamp, transaction_id, authentication_update_request, message_signature=message_signature, region=region)

Update a 3DSecure or UnionPay payment and continue processing.

Use this to handle a 3DSecure redirect response or UnionPay authentication, updating the transaction and continuing processing.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.PaymentApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
transaction_id = 'transaction_id_example' # str | Gateway transaction identifier as returned in the parameter ipgTransactionId or merchantTransactionId.
authentication_update_request = openapi_client.AuthenticationUpdateRequest() # AuthenticationUpdateRequest | Accepted request types: Secure3DAuthenticationUpdateRequest, Secure3D10AuthenticationUpdateRequest, Secure3D21AuthenticationUpdateRequest and UnionPayAuthenticationUpdateRequest.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

try:
    # Update a 3DSecure or UnionPay payment and continue processing.
    api_response = api_instance.finalize_secure_transaction(content_type, client_request_id, api_key, timestamp, transaction_id, authentication_update_request, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->finalize_secure_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **transaction_id** | **str**| Gateway transaction identifier as returned in the parameter ipgTransactionId or merchantTransactionId. | 
 **authentication_update_request** | [**AuthenticationUpdateRequest**](AuthenticationUpdateRequest.md)| Accepted request types: Secure3DAuthenticationUpdateRequest, Secure3D10AuthenticationUpdateRequest, Secure3D21AuthenticationUpdateRequest and UnionPayAuthenticationUpdateRequest. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |
**400** | The request cannot be validated. |  -  |
**401** | The request cannot be authenticated or was submitted with the wrong credentials. |  -  |
**403** | The request was unauthorized. |  -  |
**404** | The requested resource doesn&#39;t exist. |  -  |
**409** | The attempted action is not valid according to gateway rules. For example, the merchant is not set-up or the order already exists. |  -  |
**415** | Format that is not supported by the server for the HTTP method. |  -  |
**422** | The processor declined the transaction. |  -  |
**500** | An unexpected internal server error occurred. |  -  |
**502** | There was a problem communicating with the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_primary_transaction**
> TransactionResponse submit_primary_transaction(content_type, client_request_id, api_key, timestamp, primary_transaction, message_signature=message_signature, region=region)

Generate a primary transaction.

Use this to originate a financial transaction like a sale, preauthorization, or credit.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.PaymentApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
primary_transaction = openapi_client.PrimaryTransaction() # PrimaryTransaction | Accepted request types: AliPaySaleTransaction, ChinaPnRSaleTransaction, PaymentCardCreditTransaction, PaymentCardForcedTicketTransaction, PaymentCardSaleTransaction, PaymentCardPreAuthTransaction, PaymentCardPayerAuthTransaction, PaymentCardDisbursementTransaction, PaymentTokenCreditTransaction, PaymentTokenPreAuthTransaction, PaymentTokenSaleTransaction, PaymentTokenDisbursementTransaction, PaypalCreditTransaction, SepaSaleTransaction, WalletSaleTransaction, and WalletPreAuthTransaction, PaymentDeviceSaleTransaction, PaymentDevicePreAuthTransaction, PaymentDeviceCreditTransaction, PaymentDeviceDisbursementTransaction, AchPreAuthTransaction, AchSaleTransaction, AchCreditTransaction.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

try:
    # Generate a primary transaction.
    api_response = api_instance.submit_primary_transaction(content_type, client_request_id, api_key, timestamp, primary_transaction, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->submit_primary_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **primary_transaction** | [**PrimaryTransaction**](PrimaryTransaction.md)| Accepted request types: AliPaySaleTransaction, ChinaPnRSaleTransaction, PaymentCardCreditTransaction, PaymentCardForcedTicketTransaction, PaymentCardSaleTransaction, PaymentCardPreAuthTransaction, PaymentCardPayerAuthTransaction, PaymentCardDisbursementTransaction, PaymentTokenCreditTransaction, PaymentTokenPreAuthTransaction, PaymentTokenSaleTransaction, PaymentTokenDisbursementTransaction, PaypalCreditTransaction, SepaSaleTransaction, WalletSaleTransaction, and WalletPreAuthTransaction, PaymentDeviceSaleTransaction, PaymentDevicePreAuthTransaction, PaymentDeviceCreditTransaction, PaymentDeviceDisbursementTransaction, AchPreAuthTransaction, AchSaleTransaction, AchCreditTransaction. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |
**400** | The request cannot be validated. |  -  |
**401** | The request cannot be authenticated or was submitted with the wrong credentials. |  -  |
**403** | The request was unauthorized. |  -  |
**404** | The requested resource doesn&#39;t exist. |  -  |
**409** | The attempted action is not valid according to gateway rules. For example, the merchant is not set-up or the order already exists. |  -  |
**415** | Format that is not supported by the server for the HTTP method. |  -  |
**422** | The processor declined the transaction. |  -  |
**500** | An unexpected internal server error occurred. |  -  |
**502** | There was a problem communicating with the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_secondary_transaction**
> TransactionResponse submit_secondary_transaction(content_type, client_request_id, api_key, timestamp, transaction_id, secondary_transaction, message_signature=message_signature, region=region, store_id=store_id)

Perform a secondary transaction.

Use this to perform a void, postAuth or return secondary transaction. Partial postAuths and returns are allowed.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.PaymentApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
transaction_id = 'transaction_id_example' # str | Gateway transaction identifier as returned in the parameter ipgTransactionId or merchantTransactionId.
secondary_transaction = openapi_client.SecondaryTransaction() # SecondaryTransaction | Accepted request types: PostAuthTransaction, VoidTransaction, VoidPreAuthTransactions, ReturnTransaction, AchPostAuthTransaction, AchVoidTransaction and AchReturnTransaction.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)
store_id = 'store_id_example' # str | An optional outlet ID for clients that support multiple stores in the same developer app. (optional)

try:
    # Perform a secondary transaction.
    api_response = api_instance.submit_secondary_transaction(content_type, client_request_id, api_key, timestamp, transaction_id, secondary_transaction, message_signature=message_signature, region=region, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->submit_secondary_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **transaction_id** | **str**| Gateway transaction identifier as returned in the parameter ipgTransactionId or merchantTransactionId. | 
 **secondary_transaction** | [**SecondaryTransaction**](SecondaryTransaction.md)| Accepted request types: PostAuthTransaction, VoidTransaction, VoidPreAuthTransactions, ReturnTransaction, AchPostAuthTransaction, AchVoidTransaction and AchReturnTransaction. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 
 **store_id** | **str**| An optional outlet ID for clients that support multiple stores in the same developer app. | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |
**400** | The request cannot be validated. |  -  |
**401** | The request cannot be authenticated or was submitted with the wrong credentials. |  -  |
**403** | The request was unauthorized. |  -  |
**404** | The requested resource doesn&#39;t exist. |  -  |
**409** | The attempted action is not valid according to gateway rules. For example, the merchant is not set-up or the order already exists. |  -  |
**415** | Format that is not supported by the server for the HTTP method. |  -  |
**422** | The processor declined the transaction. |  -  |
**500** | An unexpected internal server error occurred. |  -  |
**502** | There was a problem communicating with the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_inquiry**
> TransactionResponse transaction_inquiry(content_type, client_request_id, api_key, timestamp, transaction_id, message_signature=message_signature, region=region, store_id=store_id)

Retrieve the state of a transaction.

Use this query to get the current state of an existing transaction.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.PaymentApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
transaction_id = 'transaction_id_example' # str | Gateway transaction identifier as returned in the parameter ipgTransactionId or merchantTransactionId.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)
store_id = 'store_id_example' # str | An optional outlet ID for clients that support multiple stores in the same developer app. (optional)

try:
    # Retrieve the state of a transaction.
    api_response = api_instance.transaction_inquiry(content_type, client_request_id, api_key, timestamp, transaction_id, message_signature=message_signature, region=region, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->transaction_inquiry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **transaction_id** | **str**| Gateway transaction identifier as returned in the parameter ipgTransactionId or merchantTransactionId. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 
 **store_id** | **str**| An optional outlet ID for clients that support multiple stores in the same developer app. | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |
**400** | The request cannot be validated. |  -  |
**401** | The request cannot be authenticated or was submitted with the wrong credentials. |  -  |
**403** | The request was unauthorized. |  -  |
**404** | The requested resource doesn&#39;t exist. |  -  |
**409** | The attempted action is not valid according to gateway rules. For example, the merchant is not set-up or the order already exists. |  -  |
**415** | Format that is not supported by the server for the HTTP method. |  -  |
**422** | The processor declined the transaction. |  -  |
**500** | An unexpected internal server error occurred. |  -  |
**502** | There was a problem communicating with the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

