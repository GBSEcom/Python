# Secure3D10AuthenticationResult

Submit the result of the authentication managed outside of the gateway for a 3-D Secure 1.0 scheme. For more convenient usage without implementing 3-D Secure yourself see \"authenticationRequest\" section.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | **str** | Specifies the version of 3DS to be used where authentication was managed outside of the gateway. | 
**verification_response** | **str** | Card enrollment result from the Verification Response (VeRes). | [optional] 
**authentication_attempt_result** | **str** | Result of authentication attempt from Payer Authentication Response (PaRes). | [optional] 
**cavv** | **str** | The Cardholder Authentication Verification Value (CAVV) is a cryptographic value derived by the issuer during payment authentication that can provide evidence of the results of payment authentication during an online purchase. | [optional] 
**xid** | **str** | The transaction identifier (XID) is a unique tracking number set by the merchant. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


