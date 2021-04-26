# ReturnTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Object name of the secondary transaction request. | 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same developer app. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request, if supplied. | [optional] 
**comments** | **str** | Comment for the secondary transaction. | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | 
**soft_descriptor** | [**SoftDescriptor**](SoftDescriptor.md) |  | [optional] 
**stored_credentials** | [**StoredCredential**](StoredCredential.md) |  | [optional] 
**currency_conversion** | [**CurrencyConversion**](CurrencyConversion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


