# RecurringPaymentDetailsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_request_id** | **str** | Echoes back the value in the request header for tracking. | [optional] 
**api_trace_id** | **str** | Request identifier in API, can be used to request logs from the support team. | [optional] 
**response_type** | [**ResponseType**](ResponseType.md) |  | [optional] 
**order_id** | **str** | Client order ID if supplied by client, otherwise the order ID. | [optional] 
**transaction_time** | **int** | The transaction time in seconds since epoch. | [optional] 
**billing** | [**Billing**](Billing.md) |  | [optional] 
**shipping** | [**Shipping**](Shipping.md) |  | [optional] 
**mandate** | [**SepaMandate**](SepaMandate.md) |  | [optional] 
**transactions** | [**list[Transaction]**](Transaction.md) | Required for some payment methods (for example, Klarna). | [optional] 
**processor** | [**ProcessorData**](ProcessorData.md) |  | [optional] 
**recurring_payment_details** | [**RecurringPaymentDetails**](RecurringPaymentDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


