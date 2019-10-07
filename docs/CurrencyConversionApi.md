# openapi_client.CurrencyConversionApi

All URIs are relative to *https://cert.api.firstdata.com/gateway/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_rate**](CurrencyConversionApi.md#get_exchange_rate) | **POST** /exchange-rates | Generate dynamic currency conversion transactions.


# **get_exchange_rate**
> ExchangeRateResponse get_exchange_rate(content_type, client_request_id, api_key, timestamp, exchange_rate_request, message_signature=message_signature, region=region)

Generate dynamic currency conversion transactions.

Sale, return and lookup exchange rate with dynamic currency conversion option.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.CurrencyConversionApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
exchange_rate_request = openapi_client.ExchangeRateRequest() # ExchangeRateRequest | Accepted request types: DCCExchangeRateRequest and DynamicPricingExchangeRateRequest.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

try:
    # Generate dynamic currency conversion transactions.
    api_response = api_instance.get_exchange_rate(content_type, client_request_id, api_key, timestamp, exchange_rate_request, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrencyConversionApi->get_exchange_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **exchange_rate_request** | [**ExchangeRateRequest**](ExchangeRateRequest.md)| Accepted request types: DCCExchangeRateRequest and DynamicPricingExchangeRateRequest. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**ExchangeRateResponse**](ExchangeRateResponse.md)

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
**500** | An unexpected internal server error occurred. |  -  |
**502** | There was a problem communicating with the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

