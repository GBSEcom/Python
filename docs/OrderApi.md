# swagger_client.OrderApi

All URIs are relative to *https://cert.api.firstdata.com/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_payment_post_authorisation**](OrderApi.md#perform_payment_post_authorisation) | **POST** /v1/orders/{order-id}/postauth | Use this to capture/complete a transaction. Partial postauths are allowed.
[**return_transaction**](OrderApi.md#return_transaction) | **POST** /v1/orders/{order-id}/return | Use this to return/refund on the order. Partial returns are allowed.


# **perform_payment_post_authorisation**
> TransactionResponse perform_payment_post_authorisation(content_type, client_request_id, api_key, timestamp, order_id, payload, message_signature=message_signature, store_id=store_id)

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
api_instance = swagger_client.OrderApi()
content_type = 'application/json' # str | content type (default to application/json)
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 789 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
order_id = 'order_id_example' # str | Gateway order identifier as returned in the parameter orderId
payload = swagger_client.SecondaryTransaction() # SecondaryTransaction | 
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
store_id = 'store_id_example' # str | an optional outlet id for clients that support multiple store in the same developer app (optional)

try:
    # Use this to capture/complete a transaction. Partial postauths are allowed.
    api_response = api_instance.perform_payment_post_authorisation(content_type, client_request_id, api_key, timestamp, order_id, payload, message_signature=message_signature, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->perform_payment_post_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to application/json]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **order_id** | **str**| Gateway order identifier as returned in the parameter orderId | 
 **payload** | [**SecondaryTransaction**](SecondaryTransaction.md)|  | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **store_id** | **str**| an optional outlet id for clients that support multiple store in the same developer app | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_transaction**
> TransactionResponse return_transaction(content_type, client_request_id, api_key, timestamp, order_id, payload, message_signature=message_signature, store_id=store_id)

Use this to return/refund on the order. Partial returns are allowed.

This can be used for Returns and Partial Returns.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrderApi()
content_type = 'application/json' # str | content type (default to application/json)
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 789 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
order_id = 'order_id_example' # str | Gateway order identifier as returned in the parameter orderId
payload = swagger_client.SecondaryTransaction() # SecondaryTransaction | 
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
store_id = 'store_id_example' # str | an optional outlet id for clients that support multiple store in the same developer app (optional)

try:
    # Use this to return/refund on the order. Partial returns are allowed.
    api_response = api_instance.return_transaction(content_type, client_request_id, api_key, timestamp, order_id, payload, message_signature=message_signature, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->return_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to application/json]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **order_id** | **str**| Gateway order identifier as returned in the parameter orderId | 
 **payload** | [**SecondaryTransaction**](SecondaryTransaction.md)|  | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **store_id** | **str**| an optional outlet id for clients that support multiple store in the same developer app | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

