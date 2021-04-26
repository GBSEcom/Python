# PreAuthSecondaryTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Object name of the secondary transaction request. | 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same developer app. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request, if supplied. | [optional] 
**comments** | **str** | Comment for the secondary transaction. | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | 
**decremental_flag** | **bool** | This flag can only be used in a preAuth transaction that updates the amount of a previous preAuth transaction to either increase the preAuth amount (DecrementalPreAuthFlag &#x3D; false) or decrease the preAuth amount (DecrementalPreAuthFlag &#x3D; true). | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


