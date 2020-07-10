# Secure3D21AuthenticationResultAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cavv** | **str** | The Cardholder Authentication Verification Value (CAVV) is a cryptographic value derived by the issuer during payment authentication that can provide evidence of the results of payment authentication during an online purchase. | [optional] 
**xid** | **str** | The transaction identifier (XID) is a unique tracking number set by the merchant. | [optional] 
**transaction_id** | **str** | The response transaction UUID. Only applicable to MasterCard. | [optional] 
**authentication_response** | **str** | The result of authentication attempt returned by the 3D Secure authentication process (PaRes). | [optional] [default to 'Y']
**transaction_status** | **str** | The transaction status as returned by the 3D Secure authentication process. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


