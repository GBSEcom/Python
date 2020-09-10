# openapi_client.PaymentTokenApi

All URIs are relative to *https://cert.api.firstdata.com/gateway/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_token**](PaymentTokenApi.md#create_payment_token) | **POST** /payment-tokens | Create a payment token from a payment card.
[**delete_payment_token**](PaymentTokenApi.md#delete_payment_token) | **DELETE** /payment-tokens/{token-id} | Delete a payment token.
[**get_payment_token_details**](PaymentTokenApi.md#get_payment_token_details) | **GET** /payment-tokens/{token-id} | Get payment card details associated with token.
[**update_payment_token**](PaymentTokenApi.md#update_payment_token) | **PATCH** /payment-tokens | Update one or more payment tokens.


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

# Create an instance of the API class
api_instance = openapi_client.PaymentTokenApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
payment_tokenization_request = openapi_client.PaymentTokenizationRequest() # PaymentTokenizationRequest | Accepted request types: PaymentCardPaymentTokenizationRequest, PaymentDevicePaymentTokenizationRequest, and ReferencedOrderPaymentTokenizationRequest.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
authorization = 'authorization_example' # str | The access token previously generated with the access-tokens call. Use the format 'Bearer {access-token}'. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

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
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **payment_tokenization_request** | [**PaymentTokenizationRequest**](PaymentTokenizationRequest.md)| Accepted request types: PaymentCardPaymentTokenizationRequest, PaymentDevicePaymentTokenizationRequest, and ReferencedOrderPaymentTokenizationRequest. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **authorization** | **str**| The access token previously generated with the access-tokens call. Use the format &#39;Bearer {access-token}&#39;. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**PaymentTokenizationResponse**](PaymentTokenizationResponse.md)

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
**401** | The request was unauthorized. |  -  |
**404** | The requested resource doesn&#39;t exist. |  -  |
**409** | The attempted action is not valid according to gateway rules. For example, when the gateway is too busy then the transaction is not processed. |  -  |
**422** | The processor declined the transaction. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

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

# Create an instance of the API class
api_instance = openapi_client.PaymentTokenApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
token_id = 'token_id_example' # str | Identifies a payment token.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
authorization = 'authorization_example' # str | The access token previously generated with the access-tokens call. Use the format 'Bearer {access-token}'. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)
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
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **token_id** | **str**| Identifies a payment token. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **authorization** | **str**| The access token previously generated with the access-tokens call. Use the format &#39;Bearer {access-token}&#39;. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 
 **store_id** | **str**|  | [optional] 

### Return type

[**PaymentTokenizationResponse**](PaymentTokenizationResponse.md)

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
**401** | The request was unauthorized. |  -  |
**404** | The requested resource doesn&#39;t exist. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_token_details**
> PaymentTokenizationResponse get_payment_token_details(content_type, client_request_id, api_key, timestamp, token_id, message_signature=message_signature, authorization=authorization, region=region, store_id=store_id)

Get payment card details associated with token.

Get payment card details associated with token.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.PaymentTokenApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
token_id = 'token_id_example' # str | Identifies a payment token.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
authorization = 'authorization_example' # str | The access token previously generated with the access-tokens call. Use the format 'Bearer {access-token}'. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)
store_id = 'store_id_example' # str |  (optional)

try:
    # Get payment card details associated with token.
    api_response = api_instance.get_payment_token_details(content_type, client_request_id, api_key, timestamp, token_id, message_signature=message_signature, authorization=authorization, region=region, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTokenApi->get_payment_token_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **token_id** | **str**| Identifies a payment token. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **authorization** | **str**| The access token previously generated with the access-tokens call. Use the format &#39;Bearer {access-token}&#39;. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 
 **store_id** | **str**|  | [optional] 

### Return type

[**PaymentTokenizationResponse**](PaymentTokenizationResponse.md)

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
**401** | The request was unauthorized. |  -  |
**404** | The requested resource doesn&#39;t exist. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_token**
> PaymentTokenUpdateResponse update_payment_token(content_type, client_request_id, api_key, timestamp, payment_card_payment_token_update_request, message_signature=message_signature, authorization=authorization, region=region)

Update one or more payment tokens.

Use this update one or more payment tokens.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.PaymentTokenApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
payment_card_payment_token_update_request = openapi_client.PaymentCardPaymentTokenUpdateRequest() # PaymentCardPaymentTokenUpdateRequest | Accepted request type: PaymentCardPaymentTokenUpdateRequest.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
authorization = 'authorization_example' # str | The access token previously generated with the access-tokens call. Use the format 'Bearer {access-token}'. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

try:
    # Update one or more payment tokens.
    api_response = api_instance.update_payment_token(content_type, client_request_id, api_key, timestamp, payment_card_payment_token_update_request, message_signature=message_signature, authorization=authorization, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTokenApi->update_payment_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **payment_card_payment_token_update_request** | [**PaymentCardPaymentTokenUpdateRequest**](PaymentCardPaymentTokenUpdateRequest.md)| Accepted request type: PaymentCardPaymentTokenUpdateRequest. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **authorization** | **str**| The access token previously generated with the access-tokens call. Use the format &#39;Bearer {access-token}&#39;. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**PaymentTokenUpdateResponse**](PaymentTokenUpdateResponse.md)

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
**401** | The request was unauthorized. |  -  |
**404** | The requested resource doesn&#39;t exist. |  -  |
**409** | The attempted action is not valid according to gateway rules. For example, when the gateway is too busy then the transaction is not processed. |  -  |
**422** | The processor declined the transaction. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

