# EncryptedApplePay

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | The encrypted wallet payload. | 
**header** | [**EncryptedApplePayHeader**](EncryptedApplePayHeader.md) |  | 
**signature** | **str** | Signature of the payment and header data. | 
**version** | **str** | Version information about the payment token. | [optional] 
**application_data** | **str** | Base64-encoded value of PKPaymentRequest. Required only if applicationDataHash is present. | [optional] 
**merchant_id** | **str** | The merchant ID assigned by the wallet provider. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


