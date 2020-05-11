# StoredCredential

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence** | **str** | Indicates if the transaction is first or subsequent. Valid values are &#39;FIRST&#39; and &#39;SUBSEQUENT&#39;. | 
**scheduled** | **bool** | Indicates if the transaction is scheduled or part of an installment. | 
**referenced_scheme_transaction_id** | **str** | The transaction ID received from schemes for the initial transaction. May be required if sequence is &#39;SUBSEQUENT&#39;. | [optional] 
**initiator** | **str** | Indicates whether it is a merchant-initiated or explicitly consented to by card holder. Valid values are &#39;MERCHANT&#39; and &#39;CARDHOLDER&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


