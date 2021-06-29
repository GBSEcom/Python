# TransactionErrorResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_request_id** | **str** | Echoes back the value in the request header for tracking. | [optional] 
**api_trace_id** | **str** | Request identifier in API, can be used to request logs from the support team. | [optional] 
**response_type** | [**ResponseType**](ResponseType.md) |  | [optional] 
**ipg_transaction_id** | **str** | The response transaction ID. | [optional] 
**order_id** | **str** | Note - Client Order ID if supplied by client. If not supplied by client, IPG will generate. The first 12 alphanumeric digits are passed down to Fiserv Enterprise reporting tool, Clientline and Data File Manager (DFM). | [optional] 
**transaction_type** | [**TransactionType**](TransactionType.md) |  | [optional] 
**payment_token** | [**PaymentTokenDetails**](PaymentTokenDetails.md) |  | [optional] 
**transaction_origin** | [**TransactionOrigin**](TransactionOrigin.md) |  | [optional] 
**payment_method_details** | [**PaymentMethodDetails**](PaymentMethodDetails.md) |  | [optional] 
**country** | **str** | Country of the card issuer. | [optional] 
**terminal_id** | **str** | The terminal that is processing the transaction. | [optional] 
**merchant_id** | **str** | The unique (on Acquirer level) mechant ID. Usually this value has been chosen from the merchant itself and will be used in communication with the endpoint. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request header, if supplied. | [optional] 
**transaction_time** | **int** | The transaction time in seconds since epoch. | [optional] 
**approved_amount** | [**Amount**](Amount.md) |  | [optional] 
**transaction_status** | **str** | Represents the status of a transaction immediately following the original processing request. This value is not stored for the transaction and is only available in the response when the transaction is processed. TransactionStatus is not returned on either the transaction inquiry or on the order inquiry. | [optional] 
**transaction_state** | **str** | Shows the state of the current transaction. | [optional] 
**payment_account_reference_number** | **str** | Payment Account Reference Number from response, if supplied. | [optional] 
**secure3d_response** | [**Secure3dResponse**](Secure3dResponse.md) |  | [optional] 
**standin_response_details** | [**StandinResponseDetails**](StandinResponseDetails.md) |  | [optional] 
**redirect_url** | **str** | The endpoint redirection URL. | [optional] 
**authentication_response** | [**Secure3DAuthenticationResponse**](Secure3DAuthenticationResponse.md) |  | [optional] 
**scheme_transaction_id** | **str** | The transaction ID received from schemes for the initial transaction of card on file flows. | [optional] 
**processor** | [**ProcessorData**](ProcessorData.md) |  | [optional] 
**additional_details** | [**AdditionalTransactionDetails**](AdditionalTransactionDetails.md) |  | [optional] 
**account_updater_response** | [**AccountUpdaterResponse**](AccountUpdaterResponse.md) |  | [optional] 
**ach_response** | [**AchResponse**](AchResponse.md) |  | [optional] 
**currency_conversion_response** | [**CurrencyConversionResponse**](CurrencyConversionResponse.md) |  | [optional] 
**steps** | [**list[PaymentStepRequest]**](PaymentStepRequest.md) | Steps to be performed by the payer. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


