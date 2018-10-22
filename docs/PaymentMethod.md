# PaymentMethod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of payment method. Note that PayPal can only process a &#39;Credit&#39;  primary transaction with Order.Billing.Contact.email being mandatory. PayPal secondary transactions (void/return/postauth) are processed the same as any other secondary transactions. | 
**payment_card** | [**PaymentCard**](PaymentCard.md) |  | [optional] 
**sepa** | [**Sepa**](Sepa.md) |  | [optional] 
**pay_pal** | [**PayPal**](PayPal.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


