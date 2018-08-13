from base_model import BaseModel
from avs_response import AvsResponse
from amount import Amount
from authentication_redirect import AuthenticationRedirect
from error import ResponseError

class TransactionResponse(BaseModel):

	ATTR = [
		'client_request_id',
		'api_trace_id',
		'ipg_transaction_id',
		'order_id',
		'transaction_type',
		'authorization_code',
		'security_code_response',
		'brand',
		'country',
		'terminal_id',
		'clientTransaction_id',
		'transaction_time',
		'transaction_status'
	]

	OBJ_ATTR = {
		'avs_response' : AvsResponse,
		'approved_amount' : Amount,
		'authentication_redirect' : AuthenticationRedirect,
		'error' : ResponseError
	}

	def __init__(self, params):
		self.set_attributes(params)

	def is_successful(self):
		return self.transaction_status is 'APPROVED'