# PrimaryTransactionAdditionalDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_number** | **str** | For FORCED_TICKET only. Stores the six digit reference number you have received as the result of a successful external authorization (e.g. by phone). The Gateway needs this number for uniquely mapping a ForcedTicket transaction to a previously performed external authorization.]  | [optional] 
**comments** | **str** | Comments for the payment | [optional] 
**dynamic_merchant_name** | **str** | The name of sub-merchant for the payment facilitator | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**purchase_order_number** | **str** | Purchase order number | [optional] 
**recurring_type** | **str** | Valid values are &#39;FIRST&#39;, &#39;REPEAT&#39; and &#39;STANDING_INSTRUCTION&#39;. | [optional] 
**installment_options** | [**InstallmentOptions**](InstallmentOptions.md) |  | [optional] 
**mcc** | **str** | Use this field to override merchant configured MCC value | [optional] 
**dcc** | [**Dcc**](Dcc.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


