from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient

class ClientContext:

	PRODUCTION_URL = "https://prod.api.firstdata.com/gateway/v2"
	SANDBOX_URL = "https://cert.api.firstdata.com/gateway/v2"

	@staticmethod
	def create(creds):
		return ClientContext(creds)

	def __init__(self, creds, env="CERT"):
		self.config = Configuration(host=self.PRODUCTION_URL) if env is "PROD" else Configuration(host=self.SANDBOX_URL)
		self.client = ApiClient(self.config)
		self.credentials = creds
