from base_model import BaseModel
from amount import Amount
from split_shipment import SplitShipment

class SecondaryTransaction(BaseModel):

	ATTR = [
		'store_id'
	]

	OBJ_ATTR = {
		'amount' : Amount,
		'split_shipment' : SplitShipment
	}

	def __init__(self, params):
		self.set_attributes(params)
