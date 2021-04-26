# PaymentCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Payment card number. | 
**expiry_date** | [**Expiration**](Expiration.md) |  | [optional] 
**security_code** | **str** | Card verification value/number. | [optional] 
**card_function** | [**CardFunction**](CardFunction.md) |  | [optional] 
**cardholder_name** | **str** | Name of the cardholder. Note - Only supported with request payload. | [optional] 
**bin** | **str** | The payment card BIN. | [optional] 
**last4** | **str** | The last 4 numbers of a payment card. | [optional] 
**brand** | **str** | Required only if using dual branded card. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


