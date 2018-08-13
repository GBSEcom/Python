from base_model import BaseModel
from error_details import ErrorDetails

class ResponseError(BaseModel):

	ATTR = [
		'code',
		'message'
	]

	OBJ_ATTR = {
		'details' : ErrorDetails 
	}

	def __init__(self, params):
		self.set_attributes(params)
		if hasattr(self, 'details'):
			set_list_items('details', ErrorDetails)