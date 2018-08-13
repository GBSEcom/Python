from base_model import BaseModel
from airline import Airline
from lodging import Lodging
from car_rental import CarRental

class IndustrySpecificExtensions(BaseModel):

	OBJ_ATTR = {
		'airline' : Airline,
		'lodging' : Lodging,
		'car_rental' : CarRental
	}

	def __init__(self, params):
		self.set_attributes(params)