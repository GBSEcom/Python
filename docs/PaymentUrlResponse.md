# PaymentUrlResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_request_id** | **str** | Echoes back the value in the Request header for tracking. | 
**api_trace_id** | **str** | Request identifier in API, can be used to request logs from the support. | 
**request_status** | **str** | Request status. If it&#39;s anything other than &#39;SUCCESS&#39;, please refer to 400s HTTP error codes or decline. See Error object for details. | 
**order_id** | **str** | Client Order ID if supplied by client, otherwise the Order ID. | [optional] 
**payment_url** | **str** |  | [optional] 
**transaction_id** | **str** | ID code from the transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


