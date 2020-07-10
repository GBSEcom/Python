# PaymentUrlResponseAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_status** | **str** | Request status. If it is anything other than &#39;SUCCESS&#39;, please refer to 400s HTTP error codes or decline. See Error object for details. | [optional] 
**order_id** | **str** | Client order ID if supplied by client, otherwise the order ID. | [optional] 
**payment_url** | **str** | URL for embedded payment link. | [optional] 
**transaction_id** | **str** | ID code from the transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


