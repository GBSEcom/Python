import firstdata

class TransactionPortal:

	def __init__(self, portal):
		self.config = portal.config

	def sale(self, params):
		params.update({'transactionType' : 'SALE'})
		pt = firstdata.PrimaryTransaction(params)
		return self.process(pt)

	def process(self, body='', path=''):
		return self._process('/payments' + path, body)

	def _process(self, path, body):
		response = self.config.http().post(path, body)
		return firstdata.TransactionResponse(response)