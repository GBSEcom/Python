from base_model import BaseModel
from travel_route import TravelRoute
from ancillary_service_category import AncillaryServiceCategory

class Airline(BaseModel):

	ATTR = [
		'passenger_name',
		'ticket_number',
		'issuing_carrier',
		'carrier_name',
		'travel_agency_iata_code',
		'travel_agency_name',
		'airline_plan_number',
		'airline_invoice_number',
		'reservation_system',
		'restricted',
		'travel_route',
		'related_ticket_number',
		'ancillary_service_category',
		'ticket_purchase'
	]

	def __init__(self, params):
		self.set_attributes(params)
		if hasattr(self, 'travel_route'):
			self.set_list_items('travel_route', TravelRoute)
		if hasattr(self, 'ancillary_service_category'):
			self.set_list_items('ancillary_service_category', AncillaryServiceCategory)