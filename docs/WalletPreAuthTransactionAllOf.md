# WalletPreAuthTransactionAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_payment_method** | [**WalletPaymentMethod**](WalletPaymentMethod.md) |  | 
**split_shipment** | [**SplitShipment**](SplitShipment.md) |  | [optional] 
**payment_facilitator** | [**PaymentFacilitator**](PaymentFacilitator.md) |  | [optional] 
**decremental_flag** | **bool** | This flag can only be used in a preAuth transaction that updates the amount of a previous preAuth transaction to either increase the preAuth amount (DecrementalPreAuthFlag &#x3D; false) or decrease the preAuth amount (DecrementalPreAuthFlag &#x3D; true). | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


