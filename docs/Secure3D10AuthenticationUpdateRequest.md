# Secure3D10AuthenticationUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** | An optional Outlet ID for clients that support multiple stores in the same developer app. | [optional] 
**authentication_type** | **str** | Object name of the authentication update request. | 
**billing_address** | [**Address**](Address.md) |  | [optional] 
**payer_authentication_response** | **str** | A formatted message providing results of the issuer’s cardholder authentication. | 
**merchant_data** | **str** | Formatted string encoding transaction time, order ID, and return URL data. | 
**security_code** | **str** | Card security code if required by merchant. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


