# ProcessorData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_number** | **str** | Reference transaction ID. | [optional] 
**authorization_code** | **str** | Code returned to confirm transaction. | [optional] 
**response_code** | **str** | Response code from endpoints. | [optional] 
**network** | **str** | Network used for transaction. | [optional] 
**association_response_code** | **str** | Raw response code from issuer. | [optional] 
**response_message** | **str** | Message returned from endpoints. | [optional] 
**avs_response** | [**AVSResponse**](AVSResponse.md) |  | [optional] 
**security_code_response** | **str** | Code returned for CVV. | [optional] 
**merchant_advice_code_indicator** | **str** | Code to map merchant advice code to ISO specification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


