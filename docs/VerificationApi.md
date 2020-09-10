# openapi_client.VerificationApi

All URIs are relative to *https://cert.api.firstdata.com/gateway/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_account**](VerificationApi.md#verify_account) | **POST** /account-verification | Verify a payment card or payment token.
[**verify_card**](VerificationApi.md#verify_card) | **POST** /card-verification | Verify a payment card.


# **verify_account**
> TransactionResponse verify_account(content_type, client_request_id, api_key, timestamp, account_verification_request, message_signature=message_signature, region=region)

Verify a payment card or payment token.

Use this to perform an account verification for a payment card or payment token.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.VerificationApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
account_verification_request = openapi_client.AccountVerificationRequest() # AccountVerificationRequest | Accepted request type: PaymentCardVerificationRequest and PaymentTokenVerificationRequest.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

try:
    # Verify a payment card or payment token.
    api_response = api_instance.verify_account(content_type, client_request_id, api_key, timestamp, account_verification_request, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->verify_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **account_verification_request** | [**AccountVerificationRequest**](AccountVerificationRequest.md)| Accepted request type: PaymentCardVerificationRequest and PaymentTokenVerificationRequest. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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
**422** | There was a problem communicating with the endpoint. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_card**
> TransactionResponse verify_card(content_type, client_request_id, api_key, timestamp, card_verification_request, message_signature=message_signature, region=region)

Verify a payment card.

Use this to perform card verification for a payment card. Use the account-verification endpoint instead for this request.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.VerificationApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
card_verification_request = openapi_client.CardVerificationRequest() # CardVerificationRequest | Accepted request type: CardVerificationRequest.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

try:
    # Verify a payment card.
    api_response = api_instance.verify_card(content_type, client_request_id, api_key, timestamp, card_verification_request, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->verify_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **card_verification_request** | [**CardVerificationRequest**](CardVerificationRequest.md)| Accepted request type: CardVerificationRequest. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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
**422** | There was a problem communicating with the endpoint. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

