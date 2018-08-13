from base_model import BaseModel

class AuthResultApplePay(BaseModel):

	ATTR = [
		'online_payment_cryptogram',
		'eci_indicator'
	]

	def __init__(self, params):
		self.set_attributes(params)
