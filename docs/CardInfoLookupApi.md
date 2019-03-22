# openapi_client.CardInfoLookupApi

All URIs are relative to *https://cert.api.firstdata.com/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**card_info_lookup**](CardInfoLookupApi.md#card_info_lookup) | **POST** /v1/card-information | Card information lookUp


# **card_info_lookup**
> CardInfoLookupResponse card_info_lookup(content_type, client_request_id, api_key, timestamp, card_info_lookup_request, message_signature=message_signature, region=region)

Card information lookUp

Use this to look up card related information such as issuer country, card function and card brand.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.CardInfoLookupApi()
content_type = 'application/json' # str | content type (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
card_info_lookup_request = openapi_client.CardInfoLookupRequest() # CardInfoLookupRequest | Card information lookup payload.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | The region where client wants to process the transaction (optional)

try:
    # Card information lookUp
    api_response = api_instance.card_info_lookup(content_type, client_request_id, api_key, timestamp, card_info_lookup_request, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardInfoLookupApi->card_info_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **card_info_lookup_request** | [**CardInfoLookupRequest**](CardInfoLookupRequest.md)| Card information lookup payload. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| The region where client wants to process the transaction | [optional] 

### Return type

[**CardInfoLookupResponse**](CardInfoLookupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

