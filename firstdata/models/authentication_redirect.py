from base_model import BaseModel
from authentication_redirect_params import AuthenticationRedirectParams as Params

class AuthenticationRedirect(BaseModel):

	ATTR = [
		'type',
		'target_url'
	]

	OBJ_ATTR = {
		'params' : Params
	}

	def __init__(self, params):
		self.set_attributes(params)