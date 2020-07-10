# PaymentDevicePreAuthTransactionAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | [**PaymentDevicePaymentMethod**](PaymentDevicePaymentMethod.md) |  | 
**create_token** | [**CreatePaymentToken**](CreatePaymentToken.md) |  | [optional] 
**settlement_split** | [**list[SubMerchantSplit]**](SubMerchantSplit.md) | Settle with multiple sub-merchants, sale and preAuth only. | [optional] 
**stored_credentials** | [**StoredCredential**](StoredCredential.md) |  | [optional] 
**split_shipment** | [**SplitShipment**](SplitShipment.md) |  | [optional] 
**decremental_flag** | **bool** | This flag can only be used in a preAuth transaction that updates the amount of a previous preAuth transaction to either increase the preAuth amount (DecrementalPreAuthFlag &#x3D; false) or decrease the preAuth amount (DecrementalPreAuthFlag &#x3D; true). | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


