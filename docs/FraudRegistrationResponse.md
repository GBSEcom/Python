# FraudRegistrationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | The value used to track the transaction. | [optional] 
**transaction_status** | **str** | Status of the transaction. Valid values are &#39;Not Processed&#39; and &#39;Scored successfully&#39; | [optional] 
**validation_status** | **str** | If status returned is \&quot;failure\&quot;, input validation errors occurred. Please refer to the \&quot;Errors Section\&quot; for more info. Valid values are &#39;success&#39; and &#39;failed&#39;. | [optional] 
**transaction_type** | **str** | The transactionType provided in request. | [optional] 
**fraud_score** | [**FraudScore**](FraudScore.md) |  | [optional] 
**error** | [**FraudRegistrationError**](FraudRegistrationError.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


