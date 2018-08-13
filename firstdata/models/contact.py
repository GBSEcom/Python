from base_model import BaseModel

class Contact(BaseModel):

	ATTR = [
		'phone',
		'mobile_phone',
		'fax',
		'email'
	]

	def __init__(self, params):
		self.set_attributes(params)