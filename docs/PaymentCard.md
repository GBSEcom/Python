# PaymentCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Payment card number | 
**expiry_date** | [**Expiration**](Expiration.md) |  | [optional] 
**security_code** | **str** | CVV | [optional] 
**card_function** | **str** |  | [optional] [default to 'CREDIT']
**cardholder_name** | **str** |  | [optional] 
**authentication_request** | [**PaymentCardAuthenticationRequest**](PaymentCardAuthenticationRequest.md) |  | [optional] 
**authentication_result** | [**PaymentCardAuthenticationResult**](PaymentCardAuthenticationResult.md) |  | [optional] 
**brand** | **str** | Optional, required only if using dual branded card | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


