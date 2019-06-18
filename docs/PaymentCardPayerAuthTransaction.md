# PaymentCardPayerAuthTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Object name of the primary transaction request. | [optional] 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same app. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request header, if supplied. | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | [optional] 
**transaction_origin** | [**TransactionOrigin**](TransactionOrigin.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**payment_method** | [**PaymentCardPaymentMethod**](PaymentCardPaymentMethod.md) |  | 
**currency_conversion** | [**CurrencyConversion**](CurrencyConversion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


