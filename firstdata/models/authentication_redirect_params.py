from base_model import BaseModel

class AuthenticationRedirectParams(BaseModel):

	ATTR = [
		'PaReq',
		'TermUrl',
		'MD'
	]

	def __init__(self, params):
		self.set_attributes(params)