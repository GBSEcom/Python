import sys
import json
import six
from six.moves import urllib
from six.moves.urllib.request import Request, urlopen
from six.moves.urllib.error import URLError, HTTPError

class HTTP():

	def __init__(self, config):
		self.config = config

	def post(self, path, body):
		return self.http_request("POST", path, body)

	def get(self, path):
		self.http_request("GET")
		response = "request"

	def http_request(self, verb, path, body):
		signature = self.config.signature()
		request_headers = {
			"Content-Type" : self.config.content_type(),
			"Api-Key" : self.config.api_key,
			"Client-Request-Id" : signature.nonce,
			"Timestamp" : signature.timestamp,
			"Message-Signature" : signature.sign(body)
		}

		print ("Path: " + self.config.base_url() + path)
		print ("Body: " + body.to_json())
		print ("Client-Request-Id: " + signature.nonce)

		return self._http_request(request_headers, verb, path, body)

	def _http_request(self, headers, verb, path, body):
		try:
			req = Request(self.config.base_url() + path, body.to_json(), headers=headers)
			if verb is not req.get_method():
				req.get_method = lambda: verb
			r = urlopen(req)
			res = r.read()
			return json.loads(res)
		except HTTPError as e:
			return json.loads(e.read())