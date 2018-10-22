from simple.client_context import ClientContext
from simple.signature import Signature
from swagger_client.api.authentication_api import AuthenticationApi
from swagger_client.api.order_api import OrderApi
from swagger_client.api.payment_api import PaymentApi

class Gateway:
	
	CONTENT_TYPE = 'application/json'

	@staticmethod
	def create(creds):
		return Gateway(ClientContext(creds))

	def __init__(self, context):
		self.context = context
		self.authentication_api = AuthenticationApi()
	 	self.order_api = OrderApi()
		self.payment_api = PaymentApi()

	def request_access_token(self):
		signature_service = self.get_signature_service()
		message_signature = signature_service.sign()
		return self.authentication_api.v1_authentication_access_tokens_post(
			self.CONTENT_TYPE,
			signature_service.client_request_id,
			self.get_api_key(),
			signature_service.timestamp,
			message_signature
		)

	def primary_payment_transaction(self, payload):
		signature_service = self.get_signature_service()
		message_signature = signature_service.sign(payload)
		return self.payment_api.primary_payment_transaction(
			self.CONTENT_TYPE,
			signature_service.client_request_id,
			self.get_api_key(),
			signature_service.timestamp,
			message_signature,
			payload
		)

	def return_transaction(self, transaction_id, payload, store_id=None):
		signature_service = self.get_signature_service()
		message_signature = signature_service.sign(payload)
		return self.payment_api.return_transaction(
			self.CONTENT_TYPE,
			signature_service.client_request_id,
			self.get_api_key(),
			signature_service.timestamp,
			message_signature,
			transaction_id,
			payload,
			store_id=store_id
		)

	def transaction_inquiry(self, transaction_id, store_id=None):
		signature_service = self.get_signature_service()
		message_signature = signature_service.sign()
		return self.payment_api.transaction_inquiry(
			self.CONTENT_TYPE,
			signature_service.client_request_id,
			self.get_api_key(),
			signature_service.timestamp,
			message_signature,
			transaction_id,
			store_id=store_id
		)

	def void_transaction(self, transaction_id, store_id=None):
		signature_service = self.get_signature_service()
		message_signature = signature_service.sign()
		return self.payment_api.void_transaction(
			self.CONTENT_TYPE,
			signature_service.client_request_id,
			self.get_api_key(),
			signature_service.timestamp,
			message_signature,
			transaction_id,
			store_id=store_id
		)

	def perform_payment_post_authorization_by_order(self, order_id, payload, store_id=None):

		signature_service = self.get_signature_service()
		message_signature = signature_service.sign(payload)
		return self.order_api.perform_payment_post_authorisation(
			self.CONTENT_TYPE,
			signature_service.client_request_id,
			self.get_api_key(),
			signature_service.timestamp,
			message_signature,
			order_id,
			payload,
			store_id=store_id
		)

	def perform_payment_authorization_by_transaction(self, transaction_id, payload, store_id=None):
		signature_service = self.get_signature_service()
		message_signature = signature_service.sign(payload)
		return self.payment_api.perform_payment_post_authorisation(
			self.CONTENT_TYPE,
			signature_service.client_request_id,
			self.get_api_key(),
			signature_service.timestamp,
			message_signature,
			transaction_id,
			payload,
			store_id=store_id
		)

	def return_transaction_by_order(self, order_id, payload, store_id=None):
		signature_service = self.get_signature_service()
		message_signature = signature_service.sign(payload)
		return self.order_api.return_transaction(
			self.CONTENT_TYPE,
			signature_service.client_request_id,
			self.get_api_key(),
			signature_service.timestamp,
			message_signature,
			order_id,
			payload,
			store_id=store_id
		)

	def get_signature_service(self):
		return Signature({
			"api_key":self.get_api_key(),
			"api_secret":self.get_api_secret()
		})

	def get_api_key(self):
		return self.context.credentials.get_api_key()

	def get_api_secret(self):
		return self.context.credentials.get_api_secret()