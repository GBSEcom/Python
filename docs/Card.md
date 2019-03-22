# Card

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ta_token** | **str** | TransArmor Token value. Either the ta token fields or card number field must contain a value. | [optional] 
**ta_token_key** | **str** | TransArmor Token Key to identify the merchant. | [optional] 
**cardholder_name** | **str** | The cardholder name as it appears on the card. | [optional] 
**card_number** | **str** | Use this field to send Clear PAN or tokens other than TransArmor Token. | [optional] 
**exp_date** | **str** | Payment method expiration date. Format is MMCCYY. | [optional] 
**cvv** | **str** | CVV Present indicator. | [optional] 
**issuer** | **str** | The company (usually a bank) that issued the card. | [optional] 
**card_reissued_number** | **str** | A number that distinguishes between two plastic cards with the same card number in the event of the card being re-issued). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


