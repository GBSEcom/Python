from base_model import BaseModel
from amount import Amount
from payment_card import PaymentCard

class DecryptedData(BaseModel):

	OBJ_ATTR = {
		'transaction_amount' : Amount,
		'payment_card' : PaymentCard
	}

	def __init__(self, params):
		self.set_attributes(params)