# PaymentRegistration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_ref** | **str** | Merchant reference code. Used by FirstAPI and reflected in settlement records and webhook notifications. Typically, the merchantRef field is the purchase order number or unique sequence value associated to a given transaction. | [optional] 
**transaction_type** | **str** | Type of transaction merchant wants to process. | 
**customer** | [**Customer**](Customer.md) |  | 
**merchant** | [**Merchant**](Merchant.md) |  | 
**device** | [**FraudRegistrationDevice**](FraudRegistrationDevice.md) |  | [optional] 
**user_defined** | [**object**](.md) | A JSON object that can carry any additional information that might be helpful for fraud detection. | [optional] 
**original_transaction_type** | **str** | Defines the type of the original transaction that is being evaluated for the Fraud Score. | 
**issuer_response** | [**IssuerResponse**](IssuerResponse.md) |  | [optional] 
**verification_avs** | [**VerificationAvs**](VerificationAvs.md) |  | [optional] 
**verification3ds** | [**Verification3ds**](Verification3ds.md) |  | [optional] 
**verification_cvv** | [**VerificationCvv**](VerificationCvv.md) |  | [optional] 
**registration_method** | [**RegistrationMethod**](RegistrationMethod.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


