from base_model import BaseModel

class AvsResponse(BaseModel):

	ATTR = [
		'street_number_match',
		'postal_code_match'
	]

	def __init__(self, params):
		self.set_attributes(params)