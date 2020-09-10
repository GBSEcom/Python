# EncryptedApplePayHeader

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_data_hash** | **str** | Merchant supplied information about the payment request. Contains Base64-encoded SHA256 hash of the applicationData property of the original PKPaymentRequest. Note - applicationData from PaymentData of PKPaymentToken Refer to Apple Pay documentation. | [optional] 
**ephemeral_public_key** | **str** | Temporary key for generating shared secret from a device. | 
**public_key_hash** | **str** | Hash of the X.509 encoded public key bytes of the merchant’s certificate. | 
**transaction_id** | **str** | Transaction identifier, generated on the device. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


