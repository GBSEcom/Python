# FraudSettingsResponseAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** | The outlet ID. | [optional] 
**blocked_card_numbers** | [**list[BlockedCardNumber]**](BlockedCardNumber.md) | List of blocked card numbers. | [optional] 
**blocked_names** | **list[str]** | List of blocked fraud names. | [optional] 
**blocked_domain_names** | **list[str]** | List of blocked fraud domain names. | [optional] 
**blocked_ip_or_class_c_addresses** | **list[str]** | List of blocked fraud IP address/Class C. | [optional] 
**maximum_purchase_amount** | [**list[MaximumPurchaseAmount]**](MaximumPurchaseAmount.md) | Maximum purchase amount limit. | [optional] 
**lockout_time** | [**LockoutTime**](LockoutTime.md) |  | [optional] 
**country_profile** | **str** | Country profile. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


