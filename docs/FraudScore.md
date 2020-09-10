# FraudScore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **str** | The score attributed to this request by our machine learning system, ranging from 0 (less likely to be fraud) to 1000 (more likely to be fraud). | [optional] 
**warnings** | **list[str]** | A list of non-critical warnings raised while processing the request. Warnings included in this list will have integration and data-quality related messages. | [optional] 
**explanations** | **list[object]** | Explanation of the fraud score applied consisting of a description, type of the explanation, and rule (if applicable). | [optional] 
**recommended_decision** | **str** | The score attributed to this request by our machine learning system, ranging from 0 (less likely to be fraud) to 1000 (more likely to be fraud). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


