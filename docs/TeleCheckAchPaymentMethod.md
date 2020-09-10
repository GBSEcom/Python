# TeleCheckAchPaymentMethod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ach_type** | **str** | ACH application type values will be one of either TeleCheckICAPaymentMethod or TeleCheckCBPPaymentMethod. | 
**routing_number** | **str** | Bank routing number. | 
**account_number** | **str** | Bank account number. | 
**account_type** | **str** | Identifies if the account type is checking or savings. | 
**check_number** | **str** | Check number. | [optional] 
**check_type** | **str** | Identifies if the check type is personal or company. | 
**product_code** | **str** | Identifies the product code in the transaction. | [optional] 
**manual_id_info** | [**IdInfo**](IdInfo.md) |  | [optional] 
**supplement_id_info** | [**IdInfo**](IdInfo.md) |  | [optional] 
**agent_id** | **str** | Used to track the agent transaction activity. | [optional] 
**terminal_id** | **str** | Identifies the register or lane number where the original sale transaction occurred. | [optional] 
**registration_id** | **str** | Unique ID assigned by the merchant for the consumer (never recycled). It is an additional level of authentication. To use this feature, the merchant must work with TeleCheck Risk to discuss. Registration IDs must not be generated for an existing or returning consumer returns. The single registration ID must be unique per consumer. | [optional] 
**registration_date** | **date** | Date the consumer originally registered in format MMDDYYYY. | [optional] 
**release_type** | **str** | Release type is used as a risk variable to gauge risk level when the merchant is releasing the purchased merchandise. | [optional] 
**vip_customer** | **str** | Flags a transaction as a VIP order (based on merchant criteria). This field should not be sent for non-VIP orders. | [optional] 
**session_id** | **str** | Session identifier. | 
**terminal_state** | **str** | Identifies the US state or territory where the original sale transaction occurred. | [optional] 
**terminal_city** | **str** | Identifies the city where the original sale transaction occurred. | [optional] 
**ach_bill_to** | [**TeleCheckAchPaymentMethodAchBillTo**](TeleCheckAchPaymentMethodAchBillTo.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


