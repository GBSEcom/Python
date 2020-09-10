# ScoreOnlyResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Unique trace ID for issue triage. | [optional] 
**transaction_status** | **str** | Please refer to \&quot;Errors Section\&quot; for more info. | [optional] 
**validation_status** | **str** | If status returned is \&quot;failure\&quot;, input validation errors occurred. Please refer to the \&quot;Errors Section\&quot; for more info. Valid values are &#39;success&#39; and &#39;failure&#39;. | [optional] 
**transaction_type** | **str** | The transactionType provided in request. | [optional] 
**fraud_score** | [**ScoreOnlyResponseFraudScore**](ScoreOnlyResponseFraudScore.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


