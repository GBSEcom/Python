from base_model import BaseModel

class AncillaryServiceCategory(BaseModel):

	ATTR = [
		'service_category'
	]

	def __init__(self, params):
		self.set_attributes(params)