# AdditionalDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Comments for the payment. | [optional] 
**invoice_number** | **str** | Invoice number. | [optional] 
**purchase_order_number** | **str** | Purchase order number. | [optional] 
**operator_id** | **str** | The operator ID. | [optional] 
**sales_system_id** | **str** | The sales system ID. | [optional] 
**ipg_deferred_auth** | **bool** | Indicates if the particular transaction is a deferred authorization. | [optional] 
**high_risk_purchase_indicator** | **bool** | this is highRiskPurchaseIndicator. | [optional] 
**receipts** | [**list[ReceiptRequestInfo]**](ReceiptRequestInfo.md) | Provides request information that is necessary to generate receipts. | [optional] 
**sca_exemption_type** | **str** | Strong customer authentication exemption type indicator. | [optional] 
**sca_visa_merchant_id** | **str** | Eight-character Visa merchant identifier (VMID) assigned by Visa, required for trusted merchant and delegated authentication. | [optional] 
**business_application_identifier** | **str** | Indicates the indended use of the Account Funding Transaction. For Visa Only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


