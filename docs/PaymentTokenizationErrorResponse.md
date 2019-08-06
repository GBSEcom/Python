# PaymentTokenizationErrorResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_request_id** | **str** | Echoes back the value in the request header for tracking. | [optional] 
**api_trace_id** | **str** | Request identifier in API, can be used to request logs from the support team. | [optional] 
**response_type** | [**ResponseType**](ResponseType.md) |  | [optional] 
**request_status** | **str** | The status of the request. | [optional] 
**request_time** | **int** | Time of the request. | [optional] 
**brand** | **str** | Card brand. | [optional] 
**country** | **str** | Country of the card issued. | [optional] 
**payment_token** | [**PaymentTokenDetails**](PaymentTokenDetails.md) |  | [optional] 
**payment_card** | [**PaymentCard**](PaymentCard.md) |  | [optional] 
**processor** | [**ProcessorData**](ProcessorData.md) |  | [optional] 
**order_id** | **str** | Client order ID if supplied by client, otherwise the order ID. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


