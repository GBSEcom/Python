# openapi_client.AuthenticationApi

All URIs are relative to *https://cert.api.firstdata.com/gateway/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_access_tokens_post**](AuthenticationApi.md#authentication_access_tokens_post) | **POST** /authentication/access-tokens | Generate an access token for user authentication.


# **authentication_access_tokens_post**
> AccessTokenResponse authentication_access_tokens_post(content_type, client_request_id, api_key, timestamp, access_token_request, message_signature=message_signature)

Generate an access token for user authentication.

This is the access token generation call for authorizing subsequent financial transactions. A valid access token is required for web client requests.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AuthenticationApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
access_token_request = openapi_client.AccessTokenRequest() # AccessTokenRequest | Access token request
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)

try:
    # Generate an access token for user authentication.
    api_response = api_instance.authentication_access_tokens_post(content_type, client_request_id, api_key, timestamp, access_token_request, message_signature=message_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_access_tokens_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **access_token_request** | [**AccessTokenRequest**](AccessTokenRequest.md)| Access token request | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

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
**415** | Format that is not supported by the server for the HTTP method. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

