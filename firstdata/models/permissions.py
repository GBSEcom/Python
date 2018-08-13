from base_model import BaseModel

class Permissions(BaseModel):

	ATTR = [
		'auth_type',
		'auth_id'		
	]

	def __init__(self, params):
		self.set_attributes(params)