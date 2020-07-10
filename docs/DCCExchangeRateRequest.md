# DCCExchangeRateRequest

Request to perform a DCC exchange rate inquiry.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Object name of the exchange rate request. | 
**base_amount** | **float** | The original amount of the merchant currency for calculation. | 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same app. | [optional] 
**bin** | **str** | The bank identification number (BIN) of the card to be used for DCC. The BIN is the first 6 digits of the card number. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


