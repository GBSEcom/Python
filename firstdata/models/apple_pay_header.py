from base_model import BaseModel

class ApplePayHeader(BaseModel):

	ATTR = [
		'application_data_hash',
		'ephemeral_public_key',
		'public_key_hash',
		'transaction_id'
	]

	def __init__(self, params):
		self.set_attributes(params)