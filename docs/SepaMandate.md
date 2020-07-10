# SepaMandate

Model for the SEPA Mandate information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Existing mandate reference, managed by merchant. Must match [A-Za-z0-9:?/+(),. -]{1,35} and not start with two slashes (\&quot;//\&quot;). Also known as the mandate ID. | 
**url** | **str** | Valid URL pointing to the SEPA mandate (PDF / HTML format recommended). | 
**signature_date** | **date** | Date of mandate signature. | 
**type** | **str** | Sequence type of the direct debit. This defaults to &#39;SINGLE&#39; if not provided. | [default to 'SINGLE']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


