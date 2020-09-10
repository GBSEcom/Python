# Airline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passenger_name** | **str** | The passenger name associated with the transaction. | [optional] 
**ticket_number** | **str** | The airline ticket number associated with the transaction. | [optional] 
**issuing_carrier** | **str** | The carrier that issued the ticket. | [optional] 
**carrier_name** | **str** | The carrier associated with the transaction. | [optional] 
**travel_agency_iata_code** | **str** | The IATA code associated with the travel agency. | [optional] 
**travel_agency_name** | **str** | The business name of the travel agency. | [optional] 
**airline_plan_number** | **str** | The airline plan number associated with the transaction. | [optional] 
**airline_invoice_number** | **str** | The invoice number used by the airline. | [optional] 
**reservation_system** | **str** | The reservation system used to create the ticket. | [optional] 
**restricted** | **bool** | If the transaction is associated with a restricted class fare. | [optional] 
**travel_route** | [**list[AirlineTravelRoute]**](AirlineTravelRoute.md) | Array containing up to 4 items that describe the route associated with the transaction. | [optional] 
**related_ticket_number** | **str** | The number of any other tickets associated with the transaction ticket. | [optional] 
**ancillary_service_category** | [**list[AirlineAncillaryServiceCategory]**](AirlineAncillaryServiceCategory.md) | Identify the purchase of ancillary goods or services with a false value. If this element is not provided, the transaction is assumed to be a purchase of an airline ticket. | [optional] 
**ticket_purchase** | **bool** | Identifies if the transaction is a ticket purchase. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


