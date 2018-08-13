from base_model import BaseModel
from decrypted_data import DecryptedData

class WalletDecryptionResponse(BaseModel):

	OBJ_ATTR = {
		'decrypted_data' : DecryptedData
	}

	def __init__(self, params):
		self.set_attributes(params)
