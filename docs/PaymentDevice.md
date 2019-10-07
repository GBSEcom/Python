# PaymentDevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_type** | **str** | The data format. | 
**data** | **str** | Data from device containing, at a minimum, a transaction-unique key serial number (KSN) and track 2 card data. | 
**security_code** | **str** | Card verification value/number. | [optional] 
**cardholder_name** | **str** | Name of cardholder. | [optional] 
**card_function** | [**CardFunction**](CardFunction.md) |  | [optional] 
**brand** | **str** | The card brand. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


