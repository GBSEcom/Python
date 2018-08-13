from base_model import BaseModel

class ErrorDetails(BaseModel):

	ATTR = [
		'field',
		'message'
	]

	def __init__(self, params):
		self.set_attributes(params)