from base_model import BaseModel
from amount import Amount
from split_shipment import SplitShipment

class BasketItem(BaseModel):

	ATTR = [
		'id',
		'description',
		'count'
	]

	OBJ_ATTR = {
		'unit_price' : Amount,
	}

	def __init__(self, params):
		self.set_attributes(params)
