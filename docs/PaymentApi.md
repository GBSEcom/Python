# swagger_client.PaymentApi

All URIs are relative to *https://cert.api.firstdata.com/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_payment_post_authorisation**](PaymentApi.md#perform_payment_post_authorisation) | **POST** /v1/payments/{transaction-id}/postauth | Use this to capture/complete a transaction. Partial postauths are allowed.
[**primary_payment_transaction**](PaymentApi.md#primary_payment_transaction) | **POST** /v1/payments | Generate a primary transaction
[**return_transaction**](PaymentApi.md#return_transaction) | **POST** /v1/payments/{transaction-id}/return | Return/refund a transaction.
[**transaction_inquiry**](PaymentApi.md#transaction_inquiry) | **GET** /v1/payments/{transaction-id} | Retrieve the state of a transaction
[**void_transaction**](PaymentApi.md#void_transaction) | **POST** /v1/payments/{transaction-id}/void | Reverse a previous action on an existing transaction


# **perform_payment_post_authorisation**
> TransactionResponse perform_payment_post_authorisation(content_type, client_request_id, api_key, timestamp, message_signature, transaction_id, payload, store_id=store_id)

Use this to capture/complete a transaction. Partial postauths are allowed.

This can be used for postauth and partial postauths.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentApi()
content_type = 'application/json' # str | content type (default to application/json)
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 789 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal.
transaction_id = 'transaction_id_example' # str | Gateway transaction identifier as returned in the parameter ipgTransactionId
payload = swagger_client.SecondaryTransaction() # SecondaryTransaction | 
store_id = 'store_id_example' # str | an optional outlet id for clients that support multiple store in the same developer app (optional)

try:
    # Use this to capture/complete a transaction. Partial postauths are allowed.
    api_response = api_instance.perform_payment_post_authorisation(content_type, client_request_id, api_key, timestamp, message_signature, transaction_id, payload, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->perform_payment_post_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to application/json]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | 
 **transaction_id** | **str**| Gateway transaction identifier as returned in the parameter ipgTransactionId | 
 **payload** | [**SecondaryTransaction**](SecondaryTransaction.md)|  | 
 **store_id** | **str**| an optional outlet id for clients that support multiple store in the same developer app | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **primary_payment_transaction**
> TransactionResponse primary_payment_transaction(content_type, client_request_id, api_key, timestamp, message_signature, payload)

Generate a primary transaction

Use this to originate a financial transaction, like a sale, preauthorization, or credit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentApi()
content_type = 'application/json' # str | content type (default to application/json)
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 789 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal.
payload = swagger_client.PrimaryTransaction() # PrimaryTransaction | Primary Transaction request

try:
    # Generate a primary transaction
    api_response = api_instance.primary_payment_transaction(content_type, client_request_id, api_key, timestamp, message_signature, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->primary_payment_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to application/json]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | 
 **payload** | [**PrimaryTransaction**](PrimaryTransaction.md)| Primary Transaction request | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_transaction**
> TransactionResponse return_transaction(content_type, client_request_id, api_key, timestamp, message_signature, transaction_id, payload, store_id=store_id)

Return/refund a transaction.

Use this to return/refund an existing transaction.  Partial returns are allowed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentApi()
content_type = 'application/json' # str | content type (default to application/json)
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 789 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal.
transaction_id = 'transaction_id_example' # str | Gateway transaction identifier as returned in the parameter ipgTransactionId
payload = swagger_client.SecondaryTransaction() # SecondaryTransaction | 
store_id = 'store_id_example' # str | an optional outlet id for clients that support multiple store in the same developer app (optional)

try:
    # Return/refund a transaction.
    api_response = api_instance.return_transaction(content_type, client_request_id, api_key, timestamp, message_signature, transaction_id, payload, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->return_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to application/json]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | 
 **transaction_id** | **str**| Gateway transaction identifier as returned in the parameter ipgTransactionId | 
 **payload** | [**SecondaryTransaction**](SecondaryTransaction.md)|  | 
 **store_id** | **str**| an optional outlet id for clients that support multiple store in the same developer app | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_inquiry**
> TransactionResponse transaction_inquiry(content_type, client_request_id, api_key, timestamp, message_signature, transaction_id, store_id=store_id)

Retrieve the state of a transaction

Use this query to get the current state of an existing transaction.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentApi()
content_type = 'application/json' # str | content type (default to application/json)
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 789 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal.
transaction_id = 'transaction_id_example' # str | Gateway transaction identifier as returned in the parameter ipgTransactionId
store_id = 'store_id_example' # str | an optional outlet id for clients that support multiple store in the same developer app (optional)

try:
    # Retrieve the state of a transaction
    api_response = api_instance.transaction_inquiry(content_type, client_request_id, api_key, timestamp, message_signature, transaction_id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->transaction_inquiry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to application/json]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | 
 **transaction_id** | **str**| Gateway transaction identifier as returned in the parameter ipgTransactionId | 
 **store_id** | **str**| an optional outlet id for clients that support multiple store in the same developer app | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_transaction**
> TransactionResponse void_transaction(content_type, client_request_id, api_key, timestamp, message_signature, transaction_id, store_id=store_id)

Reverse a previous action on an existing transaction

Use this to reverse a postauth/completion, credit, preauth, or sale.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentApi()
content_type = 'application/json' # str | content type (default to application/json)
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 789 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal.
transaction_id = 'transaction_id_example' # str | Gateway transaction identifier as returned in the parameter ipgTransactionId
store_id = 'store_id_example' # str | an optional outlet id for clients that support multiple store in the same developer app (optional)

try:
    # Reverse a previous action on an existing transaction
    api_response = api_instance.void_transaction(content_type, client_request_id, api_key, timestamp, message_signature, transaction_id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->void_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to application/json]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | 
 **transaction_id** | **str**| Gateway transaction identifier as returned in the parameter ipgTransactionId | 
 **store_id** | **str**| an optional outlet id for clients that support multiple store in the same developer app | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

