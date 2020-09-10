# openapi_client.FraudDetectApi

All URIs are relative to *https://cert.api.firstdata.com/gateway/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fraud_client_registration_post**](FraudDetectApi.md#fraud_client_registration_post) | **POST** /fraud/client-registration | Client registration for fraud detect transaction.
[**fraud_payment_registration_post**](FraudDetectApi.md#fraud_payment_registration_post) | **POST** /fraud/payment-registration | Payment registration for fraud detect transaction.
[**score_only**](FraudDetectApi.md#score_only) | **POST** /fraud/score-only | Score a transaction for fraud.


# **fraud_client_registration_post**
> FraudRegistrationResponse fraud_client_registration_post(content_type, client_request_id, api_key, timestamp, client_registration, message_signature=message_signature, region=region)

Client registration for fraud detect transaction.

Use this to register client for fraud detect transaction.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.FraudDetectApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
client_registration = openapi_client.ClientRegistration() # ClientRegistration | 
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

try:
    # Client registration for fraud detect transaction.
    api_response = api_instance.fraud_client_registration_post(content_type, client_request_id, api_key, timestamp, client_registration, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FraudDetectApi->fraud_client_registration_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **client_registration** | [**ClientRegistration**](ClientRegistration.md)|  | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**FraudRegistrationResponse**](FraudRegistrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |
**201** | Success response. |  -  |
**400** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fraud_payment_registration_post**
> FraudRegistrationResponse fraud_payment_registration_post(content_type, client_request_id, api_key, timestamp, payment_registration, message_signature=message_signature, region=region)

Payment registration for fraud detect transaction.

Use this to register payment for fraud detect transaction.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.FraudDetectApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
payment_registration = openapi_client.PaymentRegistration() # PaymentRegistration | 
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

try:
    # Payment registration for fraud detect transaction.
    api_response = api_instance.fraud_payment_registration_post(content_type, client_request_id, api_key, timestamp, payment_registration, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FraudDetectApi->fraud_payment_registration_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **payment_registration** | [**PaymentRegistration**](PaymentRegistration.md)|  | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**FraudRegistrationResponse**](FraudRegistrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |
**201** | Success response. |  -  |
**400** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **score_only**
> ScoreOnlyResponse score_only(content_type, client_request_id, api_key, timestamp, score_only_request, message_signature=message_signature, region=region)

Score a transaction for fraud.

Use this to obtain a fraud score for a transaction.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.FraudDetectApi()
content_type = 'application/json' # str | Content type. (default to 'application/json')
client_request_id = 'client_request_id_example' # str | A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format.
api_key = 'api_key_example' # str | Key given to merchant after boarding associating their requests with the appropriate app in Apigee.
timestamp = 56 # int | Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins).
score_only_request = openapi_client.ScoreOnlyRequest() # ScoreOnlyRequest | Accepted request type: ScoreOnlyRequest.
message_signature = 'message_signature_example' # str | Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. (optional)
region = 'region_example' # str | Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. (optional)

try:
    # Score a transaction for fraud.
    api_response = api_instance.score_only(content_type, client_request_id, api_key, timestamp, score_only_request, message_signature=message_signature, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FraudDetectApi->score_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Content type. | [default to &#39;application/json&#39;]
 **client_request_id** | **str**| A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. | 
 **api_key** | **str**| Key given to merchant after boarding associating their requests with the appropriate app in Apigee. | 
 **timestamp** | **int**| Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). | 
 **score_only_request** | [**ScoreOnlyRequest**](ScoreOnlyRequest.md)| Accepted request type: ScoreOnlyRequest. | 
 **message_signature** | **str**| Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal. | [optional] 
 **region** | **str**| Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing. | [optional] 

### Return type

[**ScoreOnlyResponse**](ScoreOnlyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |
**201** | Success response. |  -  |
**400** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

