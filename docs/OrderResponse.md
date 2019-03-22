# OrderResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipg_transaction_id** | **str** | The response transaction ID | [optional] 
**order_id** | **str** | Client order ID if supplied by client, otherwise the order ID | [optional] 
**transaction_time** | **int** | The transaction time in seconds since Epoch | [optional] 
**billing** | [**Billing**](Billing.md) |  | [optional] 
**shipping** | [**Shipping**](Shipping.md) |  | [optional] 
**mandate** | [**SepaMandate**](SepaMandate.md) |  | [optional] 
**transactions** | [**list[Transaction]**](Transaction.md) | Required for some payment methods (for example, Klarna) | [optional] 
**processor** | [**ProcessorData**](ProcessorData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


