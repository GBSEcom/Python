# PaymentTokenization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** | Client supplied Payment Token value | [optional] 
**reusable** | **bool** | One time or reusable token | [optional] [default to True]
**decline_duplicates** | **bool** | Decline duplicate payment info if client token is supplied | [optional] [default to False]
**last4** | **str** | The last 4 payment card numbers | [optional] 
**brand** | **str** | Only for tokenization with payment | [optional] 
**country** | **str** | Only for tokenization with payment | [optional] 
**account_verification** | **bool** |  | [optional] [default to False]
**security_code** | **str** | Card Verification Value/Number | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


