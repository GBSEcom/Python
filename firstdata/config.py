import firstdata

class Config:

	BASE_URL = "api-qa.payeezy.com/globalApi/v1"

	def __init__(self, params):
		self.api_key = params["api_key"]
		self.api_secret = params["api_secret"]
		self.app_id = params["app_id"]

	def base_url(self):
		return self.http_protocol() + self.BASE_URL

	def http_protocol(self):
		return "https://"

	def content_type(self):
		return "application/json"

	def user_agent(self):
		return "First Data Python Package {0}".format(version.ReleaseVersion.NUMBER)

	def signature(self):
		return firstdata.Signature({
			"api_key":self.api_key,
			"api_secret":self.api_secret
		})

	def http(self):
		return firstdata.HTTP(self)

	# def access_token()
	#	return access_tokens

	# def get_access_token()
	# 	return token call
