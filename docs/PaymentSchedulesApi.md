# openapi_client.PaymentSchedulesApi

All URIs are relative to *https://cert.api.firstdata.com/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_payment_schedule**](PaymentSchedulesApi.md#cancel_payment_schedule) | **DELETE** /v1/payment-schedules/{order-id} | Cancel a gateway payment schedule.
[**create_payment_schedule**](PaymentSchedulesApi.md#create_payment_schedule) | **POST** /v1/payment-schedules | Use this to create a gateway payment schedule.
[**inquiry_payment_schedule**](PaymentSchedulesApi.md#inquiry_payment_schedule) | **GET** /v1/payment-schedules/{order-id} | View a gateway payment schedule.
[**update_payment_schedule**](PaymentSchedulesApi.md#update_payment_schedule) | **PATCH** /v1/payment-schedules/{order-id} | Update a gateway payment schedule.


# **cancel_payment_schedule**
> PaymentSchedulesResponse cancel_payment_schedule(content_type, client_request_id, api_key, timestamp, order_id, message_signature=message_signature, region=region, store_id=store_id)

Cancel a gateway payment schedule.

Use this to cancel an existing gateway payment schedule.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.PaymentSchedulesApi()
content_type = 'application/json' # str | content type (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
order_id = 'order_id_example' # str | Gateway order identifier as returned in the parameter orderId
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | The region where client wants to process the transaction (optional)
store_id = 'store_id_example' # str | An optional outlet ID for clients that support multiple stores in the same developer app (optional)

try:
    # Cancel a gateway payment schedule.
    api_response = api_instance.cancel_payment_schedule(content_type, client_request_id, api_key, timestamp, order_id, message_signature=message_signature, region=region, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentSchedulesApi->cancel_payment_schedule: %s\n" % e)
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

[**PaymentSchedulesResponse**](PaymentSchedulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_schedule**
> PaymentSchedulesResponse create_payment_schedule(content_type, client_request_id, api_key, timestamp, payment_schedules_request, message_signature=message_signature, region=region)

Use this to create a gateway payment schedule.

This can be used to create a gateway payment schedule.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.PaymentSchedulesApi()
content_type = 'application/json' # str | content type (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
payment_schedules_request = openapi_client.PaymentSchedulesRequest() # PaymentSchedulesRequest | 
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | The region where client wants to process the transaction (optional)

try:
    # Use this to create a gateway payment schedule.
    api_response = api_instance.create_payment_schedule(content_type, client_request_id, api_key, timestamp, payment_schedules_request, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentSchedulesApi->create_payment_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **payment_schedules_request** | [**PaymentSchedulesRequest**](PaymentSchedulesRequest.md)|  | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| The region where client wants to process the transaction | [optional] 

### Return type

[**PaymentSchedulesResponse**](PaymentSchedulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inquiry_payment_schedule**
> RecurringPaymentDetailsResponse inquiry_payment_schedule(content_type, client_request_id, api_key, timestamp, order_id, message_signature=message_signature, region=region, store_id=store_id)

View a gateway payment schedule.

This can be used to view an existing gateway payment schedule.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.PaymentSchedulesApi()
content_type = 'application/json' # str | content type (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
order_id = 'order_id_example' # str | Gateway order identifier as returned in the parameter orderId
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | The region where client wants to process the transaction (optional)
store_id = 'store_id_example' # str | An optional outlet ID for clients that support multiple stores in the same developer app (optional)

try:
    # View a gateway payment schedule.
    api_response = api_instance.inquiry_payment_schedule(content_type, client_request_id, api_key, timestamp, order_id, message_signature=message_signature, region=region, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentSchedulesApi->inquiry_payment_schedule: %s\n" % e)
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

[**RecurringPaymentDetailsResponse**](RecurringPaymentDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_schedule**
> PaymentSchedulesResponse update_payment_schedule(content_type, client_request_id, api_key, timestamp, order_id, payment_schedules_request, message_signature=message_signature, region=region, store_id=store_id)

Update a gateway payment schedule.

This can be used to update a gateway payment schedule.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.PaymentSchedulesApi()
content_type = 'application/json' # str | content type (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
order_id = 'order_id_example' # str | Gateway order identifier as returned in the parameter orderId
payment_schedules_request = openapi_client.PaymentSchedulesRequest() # PaymentSchedulesRequest | 
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | The region where client wants to process the transaction (optional)
store_id = 'store_id_example' # str | An optional outlet ID for clients that support multiple stores in the same developer app (optional)

try:
    # Update a gateway payment schedule.
    api_response = api_instance.update_payment_schedule(content_type, client_request_id, api_key, timestamp, order_id, payment_schedules_request, message_signature=message_signature, region=region, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentSchedulesApi->update_payment_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **order_id** | **str**| Gateway order identifier as returned in the parameter orderId | 
 **payment_schedules_request** | [**PaymentSchedulesRequest**](PaymentSchedulesRequest.md)|  | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| The region where client wants to process the transaction | [optional] 
 **store_id** | **str**| An optional outlet ID for clients that support multiple stores in the same developer app | [optional] 

### Return type

[**PaymentSchedulesResponse**](PaymentSchedulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

