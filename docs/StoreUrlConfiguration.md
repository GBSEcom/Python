# StoreUrlConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An optional outlet id for clients that support multiple stores in the same developer app. | 
**transaction_notification_url** | **str** | Transaction notification URL for Connect. | [optional] 
**recurring_transaction_notification_url** | **str** | Recurring transaction notification URL for recurring payments. | [optional] 
**response_success_url** | **str** | Response success URL for Connect. | [optional] 
**response_failure_url** | **str** | Response failure URL for Connect. | [optional] 
**skip_result_page_for_success** | **bool** | Skip connect result page when transaction is approved. | [optional] 
**skip_result_page_for_failure** | **bool** | Skip connect result page when transaction is not approved. | [optional] 
**overwrite_url_allowed** | **bool** | Overwrite URLs in database by those from request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


