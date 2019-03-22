# PaymentSchedulesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_status** | **str** | Result of requested operation. If it&#39;s anything other than &#39;SUCCESS&#39;, please refer to 400s HTTP error codes or decline. See Error object for details. | [optional] 
**order_id** | **str** | Client order ID if supplied by client, otherwise the order ID. | [optional] 
**transaction_response** | [**TransactionResponse**](TransactionResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


