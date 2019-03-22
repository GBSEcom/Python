# PrimaryTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_type** | [**TransactionType**](TransactionType.md) |  | 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same app. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the Request header, if supplied. | [optional] 
**transaction_origin** | [**TransactionOrigin**](TransactionOrigin.md) |  | [optional] 
**amount** | [**Amount**](Amount.md) |  | 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | 
**order** | [**Order**](Order.md) |  | [optional] 
**basket_items** | [**list[BasketItem]**](BasketItem.md) | Required for some payment methods (for example, Klarna) | [optional] 
**split_shipment** | [**SplitShipment**](SplitShipment.md) |  | [optional] 
**additional_details** | [**PrimaryTransactionAdditionalDetails**](PrimaryTransactionAdditionalDetails.md) |  | [optional] 
**industry_specific_extensions** | [**IndustrySpecificExtensions**](IndustrySpecificExtensions.md) |  | [optional] 
**stored_credentials** | [**StoredCredential**](StoredCredential.md) |  | [optional] 
**purchase_card** | [**PurchaseCards**](PurchaseCards.md) |  | [optional] 
**payment_facilitator** | [**PaymentFacilitator**](PaymentFacilitator.md) |  | [optional] 
**soft_descriptor** | [**SoftDescriptor**](SoftDescriptor.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


