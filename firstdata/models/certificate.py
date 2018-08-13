from base_model import BaseModel

class Certificate(BaseModel):

	ATTR = [
		'certificate',
		'app_label',
		'wallet_provider',
		'status',
	]

	def __init__(self, params):
		self.set_attributes(params)