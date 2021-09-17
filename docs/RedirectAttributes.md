# RedirectAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_indicator** | **str** | Indicates whether or not a challenge should be performed. 01 &#x3D; No preference (You have no preference whether a challenge should be performed. This is the default value) 02 &#x3D; No challenge requested (You prefer that no challenge should be performed) 03 &#x3D; Challenge requested: 3DS Requestor Preference (You prefer that a challenge should be performed) 04 &#x3D; Challenge requested: Mandate (There are local or regional mandates that mean that a challenge must be performed)  | [optional] [default to '01']
**authenticate_transaction** | **bool** | If 3D secure should be applied. | [optional] 
**three_ds_emv_co_message_category** | **str** | EmvCo Messag Category | [optional] 
**browser_java_script_enabled** | **bool** | Browser Java Script Enabled flag | [optional] [default to False]
**override3ds_country_exclusion** | **bool** | Override 3ds Country Exclusion flag | [optional] [default to False]
**three_ds_transaction_type** | **str** | Secure 3D Transaction Type | [optional] 
**skip_tra** | **bool** | skip TRA exemption for the transaction | [optional] [default to False]
**full_bypass** | **bool** | Full by pass flag | [optional] [default to False]
**mobile_mode** | **bool** | Mobile mode flag | [optional] [default to False]
**payment_mode** | **str** | Payment Mode | [optional] 
**language** | **str** | Language used by client. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


