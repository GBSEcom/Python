from base_model import BaseModel

class ExtraCharge(BaseModel):

	ATTR = [
		'charge_item'
	]

	def __init__(self, params):
		self.set_attributes(params)