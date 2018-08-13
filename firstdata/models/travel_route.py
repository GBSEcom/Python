from base_model import BaseModel

class TravelRoute(BaseModel):

	ATTR = [
		'departure_date',
		'origin',
		'destination',
		'carrier_code',
		'service_class',
		'stopover_type',
		'fare_basis_code',
		'departure_tax',
		'flight_number'
	]

	def __init__(self, params):
		self.set_attributes(params)