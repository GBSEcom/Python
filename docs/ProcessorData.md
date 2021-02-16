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
**cardholder_info_response** | [**CardholderInfoResponse**](CardholderInfoResponse.md) |  | [optional] 
**security_code_response** | **str** | Code returned for CVV. | [optional] 
**merchant_advice_code_indicator** | **str** | Code to map merchant advice code to ISO specification. | [optional] 
**response_indicator** | **str** | Indicates whether the transaction was routed through the payment card&#39;s own network or through a different network. | [optional] 
**debit_receipt_number** | **str** | Receipt number from debit network provider. | [optional] 
**transaction_integrity_class** | **str** | MasterCard provided Transaction Integrity Class for Point of Sale (POS) Purchase and Purchase with Cash Back transactions initiated on the Authorization Platform. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


