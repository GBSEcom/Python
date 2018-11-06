# swagger_client.AuthenticationApi

All URIs are relative to *https://cert.api.firstdata.com/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_authentication_access_tokens_post**](AuthenticationApi.md#v1_authentication_access_tokens_post) | **POST** /v1/authentication/access-tokens | Generate an access token for user authentication


# **v1_authentication_access_tokens_post**
> AccessTokenResponse v1_authentication_access_tokens_post(content_type, client_request_id, api_key, timestamp, message_signature=message_signature)

Generate an access token for user authentication

This is the access token generation call for authorizing subsequent financial transactions. A valid access token is required for web client requests. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
content_type = 'application/json' # str | content type (default to application/json)
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | 
timestamp = 789 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)

try:
    # Generate an access token for user authentication
    api_response = api_instance.v1_authentication_access_tokens_post(content_type, client_request_id, api_key, timestamp, message_signature=message_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->v1_authentication_access_tokens_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| content type | [default to application/json]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**|  | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256  algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

