from base_model import BaseModel
from expiry_date import ExpiryDate
from authentication_request import AuthenticationRequest
from authentication_result import AuthenticationResult

class PaymentCard(BaseModel):

	ATTR = [
		'number',
		'security_code',
		'card_function',
		'cardholder_name',
		'brand',
		'wallet_provider_id',
		'enable_tokenization'
	]

	OBJ_ATTR = {
		'expiry_date' : ExpiryDate,
		'authentication_request' : AuthenticationRequest,
		'authentication_result' : AuthenticationResult
	}

	def __init__(self, params):
		if 'expiry_date' in params :
			params['expiry_date'] = self.format_expiration(params['expiry_date'])
		self.set_attributes(params)

	def format_expiration(self, exp):
		if isinstance(exp, str) or isinstance(exp, int):
			return ExpiryDate({'expiry_date': exp})
		else:
			return exp