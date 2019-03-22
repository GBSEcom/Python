# PaymentCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Payment card number | [optional] 
**expiry_date** | [**Expiration**](Expiration.md) |  | [optional] 
**security_code** | **str** | Card Verification Value/Number | [optional] 
**payment_tokenization** | [**PaymentTokenization**](PaymentTokenization.md) |  | [optional] 
**card_function** | **str** | Card function. Optional, valid values are CREDIT or DEBIT. | [optional] 
**cardholder_name** | **str** | Name of the cardholder on the card | [optional] 
**authentication_request** | [**AuthenticationRequest**](AuthenticationRequest.md) |  | [optional] 
**authentication_result** | [**PaymentCardAuthenticationResult**](PaymentCardAuthenticationResult.md) |  | [optional] 
**bin** | **str** | The payment card BIN | [optional] 
**last4** | **str** | The last 4 payment card numbers | [optional] 
**brand** | **str** | Optional, required only if using dual branded card | [optional] 
**issuing_country** | **str** | The issuing country | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


