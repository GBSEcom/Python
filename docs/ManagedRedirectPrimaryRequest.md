# ManagedRedirectPrimaryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Object name of the primary transaction request. | 
**transaction_amount** | [**Amount**](Amount.md) |  | 
**store_id** | **str** | An optional Outlet ID for clients that support multiple stores in the same developer app. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request, if supplied. | [optional] 
**transaction_type** | [**ManagedRedirectTransactionType**](ManagedRedirectTransactionType.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**redirect_attributes** | [**RedirectAttributes**](RedirectAttributes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


