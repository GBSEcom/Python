from base_model import BaseModel

class AuthenticationRequest(BaseModel):

	ATTR = [
		'type'
	]

	def __init__(self, params):
		self.set_attributes(params)