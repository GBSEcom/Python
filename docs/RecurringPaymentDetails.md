# RecurringPaymentDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** | Store ID number. | [optional] 
**purchase_order_number** | **str** | Purchase order number. | [optional] 
**invoice_number** | **str** | Invoice number. | [optional] 
**creation_date** | **str** | Date recurring payment was created. | [optional] 
**start_date** | **str** | Date of mandate signature. | [optional] 
**next_attempt_date** | **str** | Date of next transaction process attempt. | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | [optional] 
**payment_method_details** | [**PaymentMethodDetails**](PaymentMethodDetails.md) |  | [optional] 
**frequency** | [**Frequency**](Frequency.md) |  | [optional] 
**number_of_payments** | **int** | Number of times the recurring payment will process. | [optional] 
**run_count** | **int** | Times the recurring payment has already run. | [optional] 
**state** | **str** | State of the recurring payment. | [optional] 
**comments** | **str** | User supplied comments. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


