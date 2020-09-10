# PaymentTokenDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Client-supplied payment token value. Only applicable for DataVault tokenization scheme. | [optional] 
**reusable** | **bool** | If the token is reusable. | [optional] [default to True]
**decline_duplicates** | **bool** | Decline duplicate payment info if client token is supplied. | [optional] [default to False]
**last4** | **str** | The last 4 numbers of a payment card. | [optional] 
**brand** | **str** | Card brand, only for tokenization with payment. | [optional] 
**account_verification** | **bool** | If the account the token was created from has been verified. | [optional] 
**type** | **str** | Inidcates the type of tokenization source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


