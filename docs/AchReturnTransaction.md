# AchReturnTransaction

Request to perform ACH TeleCheck return transaction. Note - If the ACH transaction to be refunded has not yet been sent to Telecheck, the original transaction will be automatically voided instead.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Object name of the secondary transaction request. | 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same developer app. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request, if supplied. | [optional] 
**comments** | **str** | Comment for the secondary transaction. | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


