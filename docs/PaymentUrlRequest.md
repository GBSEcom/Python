# PaymentUrlRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** | An optional Outlet ID for clients that support multiple stores in the same developer app. | [optional] 
**client_locale** | [**ClientLocale**](ClientLocale.md) |  | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | 
**transaction_type** | [**TransactionType**](TransactionType.md) |  | 
**order_id** | **str** | Client order ID if supplied by client, otherwise the order ID. | [optional] 
**billing** | [**Billing**](Billing.md) |  | [optional] 
**shipping** | [**Shipping**](Shipping.md) |  | [optional] 
**transaction_notification_url** | **str** | URL for notifying merchant of payment result. | [optional] 
**expiration** | **int** | Time until payment URL expires. | [optional] 
**authenticate_transaction** | **bool** | If 3D secure should be applied. | [optional] 
**dynamic_merchant_name** | **str** | Dynamic merchant name for the cardholder&#39;s statement. | [optional] 
**invoice_number** | **str** | Invoice number. | [optional] 
**purchase_order_number** | **str** | Purchase order number. | [optional] 
**hosted_payment_page_text** | **str** | The text to be displayed to the payer on the hosted payment page. | [optional] 
**ip** | **str** | IPv4 or IPv6 network address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


