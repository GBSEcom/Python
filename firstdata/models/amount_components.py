from base_model import BaseModel

class AmountComponents(BaseModel):

	ATTR = [
		'subtotal',
		'vat_amount',
		'local_tax',
		'shipping',
		'cashback',
		'tip',
		'convenience_fee'
	]

	def __init__(self, params):
		self.set_attributes(params)