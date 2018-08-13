from base_model import BaseModel
from extra_charge import ExtraCharge

class CarRental(BaseModel):

	ATTR = [
		'agreement_number',
		'renter_name',
		'return_city',
		'return_date',
		'pickup_date',
		'rental_class_id',
		'extra_charges',
		'no_show_indicator'
	]

	def __init__(self, params):
		self.set_attributes(params)
		if hasattr(self, 'extra_charges'):
			set_list_items('extra_charges', ExtraCharge)