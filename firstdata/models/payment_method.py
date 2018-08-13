from base_model import BaseModel
from payment_card import PaymentCard
from sepa_direct_debit import SepaDirectDebit
from apple_pay import ApplePay

class PaymentMethod(BaseModel):

	ATTR = [
		'type'
	]

	OBJ_ATTR = {
		'payment_card' : PaymentCard, 
		'sepa_direct_debit' : SepaDirectDebit, 
		'apple_pay' : ApplePay
	}

	def __init__(self, params):
		self.set_attributes(params)
		if not hasattr(self, 'type'):
			self.detect_payment_type()


	def detect_payment_type(self):
		if hasattr(self, 'payment_card'):
			self.type = "PAYMENT_CARD"
		elif hasattr(self, 'sepa_direct_debit'):
			self.type = "SEPA_DIRECT_DEBIT"
		elif hasattr(self, 'apple_pay'):
			self.type = "APPLE_PAY"
