# SharedSecretConfigurationResponse

Response from a shared secret configuration request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_request_id** | **str** | Echoes back the value in the request header for tracking. | [optional] 
**api_trace_id** | **str** | Request identifier in API, can be used to request logs from the support team. | [optional] 
**response_type** | [**ResponseType**](ResponseType.md) |  | [optional] 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same developer app. | [optional] 
**shared_secret** | **str** | Shared secret/password for Connect. | [optional] 
**response_message** | **str** | The message/status received after updating shared secret service config. | [optional] 
**response_timestamp** | **int** | Response timestamp. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


