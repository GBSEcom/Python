# openapi_client.PaymentURLApi

All URIs are relative to *https://cert.api.firstdata.com/gateway/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_url**](PaymentURLApi.md#create_payment_url) | **POST** /payment-url | Create a payment URL.
[**delete_payment_url**](PaymentURLApi.md#delete_payment_url) | **DELETE** /payment-url | Delete a payment URL.
[**payment_url_detail**](PaymentURLApi.md#payment_url_detail) | **GET** /payment-url | Retrieve the state of payment URL.


# **create_payment_url**
> PaymentUrlResponse create_payment_url(content_type, client_request_id, api_key, timestamp, payment_url_request, message_signature=message_signature, region=region)

Create a payment URL.

Use this to generate an embedding payment link.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.PaymentURLApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
payment_url_request = openapi_client.PaymentUrlRequest() # PaymentUrlRequest | Accepted request type: PaymentUrlRequest.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

try:
    # Create a payment URL.
    api_response = api_instance.create_payment_url(content_type, client_request_id, api_key, timestamp, payment_url_request, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentURLApi->create_payment_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **payment_url_request** | [**PaymentUrlRequest**](PaymentUrlRequest.md)| Accepted request type: PaymentUrlRequest. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**PaymentUrlResponse**](PaymentUrlResponse.md)

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
**409** | There was a problem communicating with the endpoint. |  -  |
**415** | Format that is not supported by the server for the HTTP method. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_url**
> PaymentUrlResponse delete_payment_url(content_type, client_request_id, api_key, timestamp, message_signature=message_signature, region=region, store_id=store_id, transaction_id=transaction_id, order_id=order_id, payment_url_id=payment_url_id, transaction_time=transaction_time)

Delete a payment URL.

Use this to delete an embedding payment link.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.PaymentURLApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)
store_id = 'store_id_example' # str | An optional outlet ID for clients that support multiple stores in the same developer app. (optional)
transaction_id = 'transaction_id_example' # str | Gateway transaction identifier as returned in the parameter ipgTransactionId or merchantTransactionId. (optional)
order_id = 'order_id_example' # str | Gateway order identifier as returned in the parameter orderId. (optional)
payment_url_id = 'payment_url_id_example' # str | The ID code from the payment URL. (optional)
transaction_time = 'transaction_time_example' # str | The transaction time in seconds since epoch. (optional)

try:
    # Delete a payment URL.
    api_response = api_instance.delete_payment_url(content_type, client_request_id, api_key, timestamp, message_signature=message_signature, region=region, store_id=store_id, transaction_id=transaction_id, order_id=order_id, payment_url_id=payment_url_id, transaction_time=transaction_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentURLApi->delete_payment_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 
 **store_id** | **str**| An optional outlet ID for clients that support multiple stores in the same developer app. | [optional] 
 **transaction_id** | **str**| Gateway transaction identifier as returned in the parameter ipgTransactionId or merchantTransactionId. | [optional] 
 **order_id** | **str**| Gateway order identifier as returned in the parameter orderId. | [optional] 
 **payment_url_id** | **str**| The ID code from the payment URL. | [optional] 
 **transaction_time** | **str**| The transaction time in seconds since epoch. | [optional] 

### Return type

[**PaymentUrlResponse**](PaymentUrlResponse.md)

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
**409** | There was a problem communicating with the endpoint. |  -  |
**415** | Format that is not supported by the server for the HTTP method. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_url_detail**
> PaymentUrlDetailResponse payment_url_detail(content_type, client_request_id, api_key, timestamp, from_date, to_date, message_signature=message_signature, region=region, store_id=store_id, order_id=order_id, merchant_transaction_id=merchant_transaction_id, status=status)

Retrieve the state of payment URL.

Use this query to get the current state of an existing paymentURL.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.PaymentURLApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
from_date = 'from_date_example' # str | The start date for payment URL in seconds since epoch.
to_date = 'to_date_example' # str | The end date for payment URL search query in seconds since epoch.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)
store_id = 'store_id_example' # str | An optional outlet ID for clients that support multiple stores in the same developer app. (optional)
order_id = 'order_id_example' # str | Gateway order identifier as returned in the parameter orderId. (optional)
merchant_transaction_id = 'merchant_transaction_id_example' # str | Gateway merchant identifier as returned in the parameter merchantTransactionId. (optional)
status = 'status_example' # str | The status of payment URL. (optional)

try:
    # Retrieve the state of payment URL.
    api_response = api_instance.payment_url_detail(content_type, client_request_id, api_key, timestamp, from_date, to_date, message_signature=message_signature, region=region, store_id=store_id, order_id=order_id, merchant_transaction_id=merchant_transaction_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentURLApi->payment_url_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **from_date** | **str**| The start date for payment URL in seconds since epoch. | 
 **to_date** | **str**| The end date for payment URL search query in seconds since epoch. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 
 **store_id** | **str**| An optional outlet ID for clients that support multiple stores in the same developer app. | [optional] 
 **order_id** | **str**| Gateway order identifier as returned in the parameter orderId. | [optional] 
 **merchant_transaction_id** | **str**| Gateway merchant identifier as returned in the parameter merchantTransactionId. | [optional] 
 **status** | **str**| The status of payment URL. | [optional] 

### Return type

[**PaymentUrlDetailResponse**](PaymentUrlDetailResponse.md)

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
**409** | There was a problem communicating with the endpoint. |  -  |
**415** | Format that is not supported by the server for the HTTP method. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

