# PrimaryTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Object name of the primary transaction request. | 
**transaction_amount** | [**Amount**](Amount.md) |  | 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same app. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request header, if supplied. | [optional] 
**transaction_origin** | [**TransactionOrigin**](TransactionOrigin.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**allow_partial_approval** | **bool** | Indicates if the particular transaction is a partial approval transaction, if supplied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


