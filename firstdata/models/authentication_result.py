from base_model import BaseModel
from auth_result_apple_pay import AuthResultApplePay as ApplePay
from auth_result_secure3d import AuthResultSecure3d as Secure3d


class AuthenticationResult(BaseModel):

	OBJ_ATTR = {
		'apple_pay' : ApplePay,
		'secure_3d' : Secure3d
	}

	def __init__(self, params):
		self.set_attributes(params)
