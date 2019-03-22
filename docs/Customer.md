# Customer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID for the customer, if registered. This field is required if the parent object is present. | 
**start_date** | **str** | The timestamp of the customers registration in the merchants platform. Format is CCYY-MM-DD. | [optional] 
**first_name** | **str** | Customers first name. | [optional] 
**last_name** | **str** | Customers last name. | [optional] 
**middle_name** | **str** | Customers middle name. | [optional] 
**email** | **str** | Customers email address. | [optional] 
**session_id** | **str** | The unique ID of the current login session. Must be unique for the customer. | [optional] 
**username** | **str** | The username of this customer in the merchants system. This field should contain customer-supplied data if available instead of a generated ID. This field can contain the clients email address if it is also used for authentication purposes. | [optional] 
**gender** | **str** | The customers gender. Do not set this property if the customer does not specify a gender. | [optional] 
**date_of_birth** | **str** | The customers year of birth. Format is CCYY. | [optional] 
**address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**user_defined** | [**object**](.md) | A JSON object that can carry any additional information about the customer that might be helpful for fraud detection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


