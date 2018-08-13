from base_model import BaseModel
from error import ResponseError

class AccessTokenResponse(BaseModel):

	ATTR = [
		'access_token',
		'client_request_id',
		'api_trace_id',
		'transaction_status'
	]

	OBJ_ATTR = {
		'error' : ResponseError
	}

	def __init__(self, params):
		self.set_attributes(params)

	def valid_token(self):
		return True 