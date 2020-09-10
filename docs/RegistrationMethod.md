# RegistrationMethod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method_type** | **str** | Unique ID for the payment method type. | 
**method_id** | **str** | The unique ID of this payment method if it was previously registered with a registration/method or if it is currently being registered. Must be unique for the entire system (not just within a specific merchant or industry). Mandatory if being used inside a registration/method. | [optional] 
**user_defined** | [**object**](.md) | A JSON object that carries any additional information that might be helpful for fraud detection. | [optional] 
**billing_phone_number** | **str** | The address that should be used to send billing information for this payment method. | [optional] 
**method_alias** | **str** | The address that should be used to send billing information for this payment method. | [optional] 
**card** | [**FraudRegistrationCard**](FraudRegistrationCard.md) |  | 
**method_address** | [**FraudAddress**](FraudAddress.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


