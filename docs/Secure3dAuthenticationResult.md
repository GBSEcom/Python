# Secure3dAuthenticationResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Indicates what kind of authentication scheme the merchant wants to use on the card. | [optional] 
**verification_response** | **str** | Card enrollment result from the Verification Response (VeRes). | [optional] 
**authentication_attempt_result** | **str** | Result of authentication attempt from Payer Authentication Response (PaRes). | [optional] 
**authentication_value** | **str** | The Cardholder Authentication Verification Value (CAVV) is a cryptographic value derived by the issuer during payment authentication that can provide evidence of the results of payment authentication during an online purchase. | [optional] 
**xid** | **str** | The transaction identifier (XID) is a unique tracking number set by the merchant. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


