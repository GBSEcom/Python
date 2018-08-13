from base_model import BaseModel
from amount import Amount
from payment_method import PaymentMethod
from order import Order
from split_shipment import SplitShipment
from industry_specific_extensions import IndustrySpecificExtensions
from basket_item import BasketItem
from pt_additional_details import AdditionalDetails
from payment_method import PaymentMethod

class PrimaryTransaction(BaseModel):

	ATTR = [
		'transaction_type',
		'store_id',
		'client_transaction_id',
		'basket_items'
	]

	OBJ_ATTR = {
		'amount' : Amount,
		'payment_method' : PaymentMethod,
		'order' : Order,
		'split_shipment' : SplitShipment,
		'additional_details' : AdditionalDetails,
		'industry_specific_extensions' : IndustrySpecificExtensions
	}

	def __init__(self, params):
		if 'payment_method' not in params:
			self.set_payment_method(params) 
		self.set_attributes(params)
		if hasattr(self, 'basket_items'):
			self.set_list_items('basket_items', BasketItem)

	def set_payment_method(self, params):
		if 'payment_card' in params:
			params['payment_method'] = PaymentMethod({'payment_card' : params['payment_card']})
		elif 'sepa_direct_debit' in params:
			params['payment_method'] = PaymentMethod({'sepa_direct_debit' : params['sepa_direct_debit']})
		elif 'apple_pay' in params:
			params['payment_method'] = PaymentMethod({'apple_pay' : params['apple_pay']})