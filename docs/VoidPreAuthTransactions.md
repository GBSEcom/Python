# VoidPreAuthTransactions

Request to perform a void of all authorizations associated with the current order. This request type is applicable for voiding preauth and incremental preauth transactions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** |  | 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same developer app. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request, if supplied. | [optional] 
**comments** | **str** | Comment for the secondary transaction. | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


