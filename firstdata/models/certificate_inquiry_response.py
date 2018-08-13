from base_model import BaseModel
from certificate import Certificate

class CertificateInquiryResponse(BaseModel):

	ATTR = [
		'client_request_id',
		'api_trace_id',
		'certificates'
	]

	def __init__(self, params):
		self.set_attributes(params)
		if hasattr(self,'certificates'):
			self.set_list_items('certificates', Certificate)