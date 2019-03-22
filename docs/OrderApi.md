# openapi_client.OrderApi

All URIs are relative to *https://cert.api.firstdata.com/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_inquiry**](OrderApi.md#order_inquiry) | **GET** /v1/orders/{order-id} | Retrieve the state of an order
[**order_post_auth**](OrderApi.md#order_post_auth) | **POST** /v1/orders/{order-id}/postauth | Capture/complete an already existing order.
[**order_return_transaction**](OrderApi.md#order_return_transaction) | **POST** /v1/orders/{order-id}/return | Return/refund an order.


# **order_inquiry**
> OrderResponse order_inquiry(content_type, client_request_id, api_key, timestamp, order_id, message_signature=message_signature, region=region, store_id=store_id)

Retrieve the state of an order

Use this query to get the current state of an existing order.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.OrderApi()
content_type = 'application/json' # str | content type (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
order_id = 'order_id_example' # str | Gateway order identifier as returned in the parameter orderId
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | The region where client wants to process the transaction (optional)
store_id = 'store_id_example' # str | An optional outlet ID for clients that support multiple stores in the same developer app (optional)

try:
    # Retrieve the state of an order
    api_response = api_instance.order_inquiry(content_type, client_request_id, api_key, timestamp, order_id, message_signature=message_signature, region=region, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_inquiry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **order_id** | **str**| Gateway order identifier as returned in the parameter orderId | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| The region where client wants to process the transaction | [optional] 
 **store_id** | **str**| An optional outlet ID for clients that support multiple stores in the same developer app | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_post_auth**
> TransactionResponse order_post_auth(content_type, client_request_id, api_key, timestamp, order_id, secondary_transaction, message_signature=message_signature, region=region, store_id=store_id)

Capture/complete an already existing order.

Use this to capture/complete an order. Postauths and partial postauths are allowed.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.OrderApi()
content_type = 'application/json' # str | content type (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
order_id = 'order_id_example' # str | Gateway order identifier as returned in the parameter orderId
secondary_transaction = openapi_client.SecondaryTransaction() # SecondaryTransaction | 
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | The region where client wants to process the transaction (optional)
store_id = 'store_id_example' # str | An optional outlet ID for clients that support multiple stores in the same developer app (optional)

try:
    # Capture/complete an already existing order.
    api_response = api_instance.order_post_auth(content_type, client_request_id, api_key, timestamp, order_id, secondary_transaction, message_signature=message_signature, region=region, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_post_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **order_id** | **str**| Gateway order identifier as returned in the parameter orderId | 
 **secondary_transaction** | [**SecondaryTransaction**](SecondaryTransaction.md)|  | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| The region where client wants to process the transaction | [optional] 
 **store_id** | **str**| An optional outlet ID for clients that support multiple stores in the same developer app | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_return_transaction**
> TransactionResponse order_return_transaction(content_type, client_request_id, api_key, timestamp, order_id, secondary_transaction, message_signature=message_signature, region=region, store_id=store_id)

Return/refund an order.

Use this for Returns of an existing order. Partial Returns are allowed.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.OrderApi()
content_type = 'application/json' # str | content type (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
order_id = 'order_id_example' # str | Gateway order identifier as returned in the parameter orderId
secondary_transaction = openapi_client.SecondaryTransaction() # SecondaryTransaction | 
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | The region where client wants to process the transaction (optional)
store_id = 'store_id_example' # str | An optional outlet ID for clients that support multiple stores in the same developer app (optional)

try:
    # Return/refund an order.
    api_response = api_instance.order_return_transaction(content_type, client_request_id, api_key, timestamp, order_id, secondary_transaction, message_signature=message_signature, region=region, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_return_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **order_id** | **str**| Gateway order identifier as returned in the parameter orderId | 
 **secondary_transaction** | [**SecondaryTransaction**](SecondaryTransaction.md)|  | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| The region where client wants to process the transaction | [optional] 
 **store_id** | **str**| An optional outlet ID for clients that support multiple stores in the same developer app | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

