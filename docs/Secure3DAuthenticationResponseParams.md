# Secure3DAuthenticationResponseParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer_authentication_request** | **str** | Message sent from merchant server to authenticate the cardholder. | [optional] 
**term_url** | **str** | Terminal URL for processing request. | [optional] 
**merchant_data** | **str** | Formatted string encoding transaction time, order ID, and return URL data. | [optional] 
**acs_url** | **str** | The URL for the authentication redirect for the merchant. | [optional] 
**c_req** | **str** | The CReq message initiates cardholder interaction in a 3DS 2.x challenge flow and carries authentication data from the cardholder. | [optional] 
**session_data** | **str** | Customer web browser session data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


