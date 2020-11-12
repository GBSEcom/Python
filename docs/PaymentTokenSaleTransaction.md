# PaymentTokenSaleTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Object name of the primary transaction request. | 
**transaction_amount** | [**Amount**](Amount.md) |  | 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same app. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request header, if supplied. | [optional] 
**transaction_origin** | [**TransactionOrigin**](TransactionOrigin.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**payment_method** | [**PaymentTokenPaymentMethod**](PaymentTokenPaymentMethod.md) |  | 
**stored_credentials** | [**StoredCredential**](StoredCredential.md) |  | [optional] 
**settlement_split** | [**list[SubMerchantSplit]**](SubMerchantSplit.md) | Settle with multiple sub-merchants, sale and preAuth only. | [optional] 
**currency_conversion** | [**CurrencyConversion**](CurrencyConversion.md) |  | [optional] 
**authentication_request** | [**AuthenticationRequest**](AuthenticationRequest.md) |  | [optional] 
**authentication_result** | [**AuthenticationResult**](AuthenticationResult.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


