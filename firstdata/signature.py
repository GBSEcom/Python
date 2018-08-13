import base64
import uuid
import time
import hashlib
import hmac

class Signature:
	
	nonce = str(uuid.uuid4())
	timestamp = str(int(round(time.time()*1000)))

	def __init__(self, params):
		self.api_key = params['api_key']
		self.api_secret = params['api_secret']

	def sign(self, payload=None):
		data = self.api_key + self.nonce + self.timestamp
		if payload:
			data += payload.to_json()
		h = hmac.new(self.api_secret, data, hashlib.sha256).hexdigest()
		return base64.b64encode(h)