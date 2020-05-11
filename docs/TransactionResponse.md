# TransactionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_request_id** | **str** | Echoes back the value in the request header for tracking. | [optional] 
**api_trace_id** | **str** | Request identifier in API, can be used to request logs from the support team. | [optional] 
**response_type** | [**ResponseType**](ResponseType.md) |  | [optional] 
**ipg_transaction_id** | **str** | The response transaction ID. | [optional] 
**order_id** | **str** | Client order ID if supplied by client, otherwise the order ID. | [optional] 
**transaction_type** | [**TransactionType**](TransactionType.md) |  | [optional] 
**payment_token** | [**PaymentTokenDetails**](PaymentTokenDetails.md) |  | [optional] 
**transaction_origin** | [**TransactionOrigin**](TransactionOrigin.md) |  | [optional] 
**payment_method_details** | [**PaymentMethodDetails**](PaymentMethodDetails.md) |  | [optional] 
**country** | **str** | Country of the card issuer. | [optional] 
**terminal_id** | **str** | The terminal that is processing the transaction. | [optional] 
**merchant_transaction_id** | **str** | The unique merchant transaction ID from the request header, if supplied. | [optional] 
**transaction_time** | **int** | The transaction time in seconds since epoch. | [optional] 
**approved_amount** | [**Amount**](Amount.md) |  | [optional] 
**transaction_status** | **str** | The status of the transaction. APPROVED/WAITING are returned by the endpoints.  VALIDATION_FAILED/DECLINED are errors. See ErrorResponse object for details. | [optional] 
**transaction_state** | **str** | The state of the transaction. | [optional] 
**secure3d_response** | [**Secure3dResponse**](Secure3dResponse.md) |  | [optional] 
**redirect_url** | **str** | The endpoint redirection URL. | [optional] 
**authentication_response** | [**Secure3DAuthenticationResponse**](Secure3DAuthenticationResponse.md) |  | [optional] 
**scheme_transaction_id** | **str** | The transaction ID received from schemes for the initial transaction of card on file flows. | [optional] 
**processor** | [**ProcessorData**](ProcessorData.md) |  | [optional] 
**additional_details** | [**AdditionalTransactionDetails**](AdditionalTransactionDetails.md) |  | [optional] 
**account_updater_response** | [**AccountUpdaterResponse**](AccountUpdaterResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


