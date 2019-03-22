# Payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | **str** | Defines the type of the payment. | 
**pay_method** | [**PaymentPayMethod**](PaymentPayMethod.md) |  | 
**pin_present** | **bool** | Indicates if the cards Personal Identification Number was supplied. | 
**entry_method** | **str** | The method in which the card information entered the system. | 
**issuer_response** | [**PaymentIssuerResponse**](PaymentIssuerResponse.md) |  | [optional] 
**issuer_approved_amount** | **str** | The actual approved amount. This field should be filled in when the message has already passed through the issuer (e.g. post-authorization). For transaction/authorization this amount refers to the amount that was locked on the card-holders account. | [optional] 
**issuer_card_balance** | **str** | The payment methods account balance if available. This field should be filled in when the message has already passed through the issuer (e.g. post-authorization). | [optional] 
**verification_avs** | [**PaymentVerificationAvs**](PaymentVerificationAvs.md) |  | [optional] 
**verification3ds** | [**PaymentVerification3ds**](PaymentVerification3ds.md) |  | [optional] 
**verification_cvv** | [**PaymentVerificationCvv**](PaymentVerificationCvv.md) |  | [optional] 
**user_defined** | [**object**](.md) | A JSON object that carries any additional information that might be helpful for fraud detection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


