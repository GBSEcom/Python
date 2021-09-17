# ManagedRedirectRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_amount** | [**Amount**](Amount.md) |  | 
**store_id** | **str** | An optional Outlet ID for clients that support multiple stores in the same developer app. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request, if supplied. | [optional] 
**transaction_type** | [**ManagedRedirectTransactionType**](ManagedRedirectTransactionType.md) |  | 
**order** | [**Order**](Order.md) |  | [optional] 
**redirect_attributes** | [**RedirectAttributes**](RedirectAttributes.md) |  | [optional] 
**payment_method** | [**object**](.md) | Various payment methods the Gateway supports. Abstract class, do not use this class directly, use one of its children. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


