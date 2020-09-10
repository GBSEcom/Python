# PaymentTokenizationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Object name of tokenization request. | 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same app. | [optional] 
**billing_address** | [**Address**](Address.md) |  | [optional] 
**create_token** | [**CreatePaymentToken**](CreatePaymentToken.md) |  | 
**account_verification** | **bool** | If the account should be verified prior to token creation. | [optional] [default to False]
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request, if supplied. | [optional] 
**additional_details** | [**AdditionalDetails**](AdditionalDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


