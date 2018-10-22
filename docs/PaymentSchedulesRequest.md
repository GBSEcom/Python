# PaymentSchedulesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** | Store ID number. | [optional] 
**reference_order_id** | **str** | Order ID used to create recurring payment from existing transaction. | [optional] 
**start_date** | **date** | Date of mandate signature. | [optional] 
**number_of_payments** | **int** | Number of times the recurring payment will process. | [optional] 
**maximum_failures** | **int** | Number of failures that can be encountered before re-tries cease. | [optional] 
**invoice_number** | **str** | Invoice number. | [optional] 
**po_number** | **str** | Purchase order number. | [optional] 
**transaction_origin** | **str** | The source of the transaction. The possible values are ECI (if the order was received via email or Internet), MOTO (mail order / telephone order) and RETAIL (face to face). | [optional] 
**dynamic_merchant_name** | **str** | Dynamic merchant name for the cardholder‘s statement. | [optional] 
**frequency** | [**Frequency**](Frequency.md) |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**amount** | [**Amount**](Amount.md) |  | [optional] 
**client_locale** | [**ClientLocale**](ClientLocale.md) |  | [optional] 
**order_id** | **str** | Client Order ID if supplied by client. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


