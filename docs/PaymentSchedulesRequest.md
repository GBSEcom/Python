# PaymentSchedulesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** | Store ID number. | [optional] 
**referenced_order_id** | **str** | Order ID used to create recurring payment from existing transaction. | [optional] 
**start_date** | **date** | Date of mandate signature. | [optional] 
**number_of_payments** | **int** | Number of times the recurring pament will process. | [optional] 
**maximum_failures** | **int** | Number of failures that can be encountered before re-tries cease. | [optional] 
**invoice_number** | **str** | Invoice number. | [optional] 
**purchase_order_number** | **str** | Purchase order number. | [optional] 
**transaction_origin** | [**TransactionOrigin**](TransactionOrigin.md) |  | [optional] 
**dynamic_merchant_name** | **str** | Dynamic merchant name for the cardholder&#39;s statement. | [optional] 
**frequency** | [**Frequency**](Frequency.md) |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**amount** | [**Amount**](Amount.md) |  | [optional] 
**client_locale** | [**ClientLocale**](ClientLocale.md) |  | [optional] 
**order_id** | **str** | Client order ID if supplied by client. | [optional] 
**billing** | [**Billing**](Billing.md) |  | [optional] 
**shipping** | [**Shipping**](Shipping.md) |  | [optional] 
**comments** | **str** | User supplied comments. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


