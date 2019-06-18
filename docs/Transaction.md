# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_state** | **str** | The state of the transaction. | [optional] 
**ipg_transaction_id** | **str** | The transaction ID. | [optional] 
**order_id** | **str** | Client order ID if supplied by client. | [optional] 
**transaction_type** | [**TransactionType**](TransactionType.md) |  | [optional] 
**payment_method_details** | [**PaymentMethodDetails**](PaymentMethodDetails.md) |  | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | [optional] 
**submission_component** | **str** | The submission component. | [optional] 
**payer_security_level** | **str** | The payer security level. | [optional] 
**transaction_time** | **int** | The transaction time in seconds since epoch. | [optional] 
**store_id** | **str** | Store ID number. | [optional] 
**user_id** | **str** | The user ID. | [optional] 
**processor** | [**ProcessorData**](ProcessorData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


