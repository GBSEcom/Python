# Airline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passenger_name** | **str** |  | [optional] 
**ticket_number** | **str** |  | [optional] 
**issuing_carrier** | **str** |  | [optional] 
**carrier_name** | **str** |  | [optional] 
**travel_agency_iata_code** | **str** |  | [optional] 
**travel_agency_name** | **str** |  | [optional] 
**airline_plan_number** | **str** |  | [optional] 
**airline_invoice_number** | **str** |  | [optional] 
**reservation_system** | **str** |  | [optional] 
**restricted** | **bool** |  | [optional] 
**travel_route** | [**list[AirlineTravelRoute]**](AirlineTravelRoute.md) |  | [optional] 
**related_ticket_number** | **str** |  | [optional] 
**ancillary_service_category** | [**list[AirlineAncillaryServiceCategory]**](AirlineAncillaryServiceCategory.md) | Identify the purchase of ancillary goods or services with a false value. If this element is not provided, the transaction is assumed to be a purchase of an airline ticket. | [optional] 
**ticket_purchase** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


