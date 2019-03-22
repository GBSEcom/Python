# openapi_client.PaymentTokenApi

All URIs are relative to *https://cert.api.firstdata.com/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_token**](PaymentTokenApi.md#create_payment_token) | **POST** /v1/payment-tokens | Create a payment token from a payment card.
[**delete_payment_token**](PaymentTokenApi.md#delete_payment_token) | **DELETE** /v1/payment-tokens/{token-id} | Delete a payment token.


# **create_payment_token**
> PaymentTokenizationResponse create_payment_token(content_type, client_request_id, api_key, timestamp, payment_tokenization_request, message_signature=message_signature, authorization=authorization, region=region)

Create a payment token from a payment card.

Use this to create a payment token from a payment card.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.PaymentTokenApi()
content_type = 'application/json' # str | content type (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
payment_tokenization_request = openapi_client.PaymentTokenizationRequest() # PaymentTokenizationRequest | 
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
authorization = 'authorization_example' # str | The access token previously generated with the access-tokens call. Use the format 'Bearer {access-token}'. (optional)
region = 'region_example' # str | The region where client wants to process the transaction (optional)

try:
    # Create a payment token from a payment card.
    api_response = api_instance.create_payment_token(content_type, client_request_id, api_key, timestamp, payment_tokenization_request, message_signature=message_signature, authorization=authorization, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTokenApi->create_payment_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **payment_tokenization_request** | [**PaymentTokenizationRequest**](PaymentTokenizationRequest.md)|  | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **authorization** | **str**| The access token previously generated with the access-tokens call. Use the format &#39;Bearer {access-token}&#39;. | [optional] 
 **region** | **str**| The region where client wants to process the transaction | [optional] 

### Return type

[**PaymentTokenizationResponse**](PaymentTokenizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_token**
> PaymentTokenizationResponse delete_payment_token(content_type, client_request_id, api_key, timestamp, token_id, message_signature=message_signature, authorization=authorization, region=region, store_id=store_id)

Delete a payment token.

Use this to delete a payment token.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.PaymentTokenApi()
content_type = 'application/json' # str | content type (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
token_id = 'token_id_example' # str | Identifies a payment token
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
authorization = 'authorization_example' # str | The access token previously generated with the access-tokens call. Use the format 'Bearer {access-token}'. (optional)
region = 'region_example' # str | The region where client wants to process the transaction (optional)
store_id = 'store_id_example' # str |  (optional)

try:
    # Delete a payment token.
    api_response = api_instance.delete_payment_token(content_type, client_request_id, api_key, timestamp, token_id, message_signature=message_signature, authorization=authorization, region=region, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTokenApi->delete_payment_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **token_id** | **str**| Identifies a payment token | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **authorization** | **str**| The access token previously generated with the access-tokens call. Use the format &#39;Bearer {access-token}&#39;. | [optional] 
 **region** | **str**| The region where client wants to process the transaction | [optional] 
 **store_id** | **str**|  | [optional] 

### Return type

[**PaymentTokenizationResponse**](PaymentTokenizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

