# PaymentUrlDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_url** | **str** | URL for embedded payment link. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request, if supplied. | [optional] 
**order_id** | **str** | Note - Client Order ID if supplied by client. If not supplied by client, IPG will generate. The first 12 alphanumeric digits are passed down to Fiserv Enterprise reporting tool, Clientline and Data File Manager (DFM). | [optional] 
**request_time** | **int** | The transaction time in seconds since epoch. | [optional] 
**status** | [**PaymentUrlStatus**](PaymentUrlStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


