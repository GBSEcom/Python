from base_model import BaseModel
from permissions import Permissions

class CertificateRequest(BaseModel):

	ATTR = [
		'app_label',
		'wallet_provider'
	]

	OBJ_ATTR = {
		'permissions' : Permissions
	}

	def __init__(self, params):
		self.set_attributes(params)