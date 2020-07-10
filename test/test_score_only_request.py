# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.12.0.20200605.001
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.score_only_request import ScoreOnlyRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestScoreOnlyRequest(unittest.TestCase):
    """ScoreOnlyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScoreOnlyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.score_only_request.ScoreOnlyRequest()  # noqa: E501
        if include_optional :
            return ScoreOnlyRequest(
                merchant_ref = 'ffd031516002', 
                transaction_type = 'score_only', 
                original_transaction_type = 'transaction/authorization', 
                original_transaction_id = 'fraudFAPI1231231', 
                amount = '1100', 
                currency_code = 'USD', 
                customer = {"id":"125Xasdf57D","startDate":"2017-01-04","firstName":"John","lastName":"Smith","middleName":"Joseph","email":"accept@xyz.com","sessionId":"session-1","username":"username","gender":"male","dateOfBirth":"1982","address":{"street":"Apartment 123","street2":"123 Main Street","stateProvince":"NY","city":"New York","country":"US","phone":{"type":"mobile","number":"212-515-1212"},"zipPostalCode":"11375"},"userDefined":{"previouslyAffected":"Y"}}, 
                billing_address = {"firstName":"John","lastName":"Smith","middleName":"Joseph","street":"Apartment 123","street2":"123 Main Street","stateProvince":"NY","city":"New York","country":"US","phone":{"type":"mobile","number":"212-515-1212"},"zipPostalCode":"11375"}, 
                device = {"deviceType":"device/mobile","deviceId":"BDE000:008945:58AC03:F02569","networks":{"networkType":"network/wifi","ip":"10.201.0.244","phoneNumber":"302-123-4567","carrierName":"T-Mobile","mobileCountryCode":"310","mobileNetworkCode":"004","subscriptionIdentificationNumber":"123456789","locationAreaCode":"12345","cellId":"2224","standard":"GSM","mac":"02:00:00:00:00:00","ssid":"Boston-5G-1","bssid":"e8:fc:af:fb:4b:8c","userDefined":{"usedData":"50MB"}},"latitude":41.14961,"longitude":-8.61099,"imei":"49-015420-323751","model":"iPhone 10","manufacturer":"Apple","timezoneOffset":"+02:00","rooted":false,"malwareDetected":false,"userDefined":{"battery":"95%"}}, 
                loyalty = {"id":"AK0123456789","program":"gold","balance":163}, 
                payment = {"paymentType":"payment/card","method":{"methodType":"method/card","methodId":"300fa792-bf5f-418e-aa74-d5b3c81298d2","methodAlias":"card one","card":{"taToken":"7591787425749818","taTokenKey":"ab56","cardholderName":"John F. Doe","cardNumber":"5424180279791732","expDate":"122028","cvv":"true","issuer":"Bank of America","cardReissuedNumber":"2"},"provider":"apple"},"pinPresent":true,"entryMethod":"remote","issuerResponse":{"code":"100","status":"approved","scheme":"visa"},"issuerApprovedAmount":"1234","issuerCardBalance":"2000","verificationAvs":{"code":"+Z","status":"zip match","scheme":"amex"},"verification3ds":{"code":"4","status":"approved","scheme":"6"},"verificationCvv":{"code":"7","status":"approved","scheme":"9"},"userDefined":{"failedPinAttempts":3}}, 
                merchant = {"mcc":"7311","merchantUniqueId":"9a0f5fe8-f907-4b06-88e9-8dd5141cbf44","location":{"locationId":"3","merchantAddress":{"street":"5565 Glenridge Connector","city":"Atlanta","state":"GA","zipPostalCode":"30342","country":"US"},"hierarchy":"FDC","timezoneOffset":"+02:00","userDefined":{"validAddress":false}},"userDefined":{"highFraudVolume":true}}, 
                order = {"shipToAddress":{"phone":"404-404-4040","address1":"5565 Glenridge Connector","city":"Atlanta","state":"GA","zip":"30342","country":"US"},"items":[{"id":"PRODCODE1","name":"The Art of Computer Programming","quantity":"litre","unit":10.23,"unitPrice":{"value":7300,"currency":"USD"},"categories":"[[\"Books\", \"Computers & Technology\", \"Programming\"], [\"Books\", \"Text Books\", \"Computer Science\"]]","detailsUrl":"https://mystore.domain/product/PRODCODE1","userDefined":{"weight":5021.23,"vat":0.06}}],"userDefined":{"delivery":"express","carrier":"ups"}}, 
                user_defined = {"inauthTransId":1234}
            )
        else :
            return ScoreOnlyRequest(
                transaction_type = 'score_only',
                original_transaction_type = 'transaction/authorization',
                original_transaction_id = 'fraudFAPI1231231',
                amount = '1100',
                currency_code = 'USD',
                payment = {"paymentType":"payment/card","method":{"methodType":"method/card","methodId":"300fa792-bf5f-418e-aa74-d5b3c81298d2","methodAlias":"card one","card":{"taToken":"7591787425749818","taTokenKey":"ab56","cardholderName":"John F. Doe","cardNumber":"5424180279791732","expDate":"122028","cvv":"true","issuer":"Bank of America","cardReissuedNumber":"2"},"provider":"apple"},"pinPresent":true,"entryMethod":"remote","issuerResponse":{"code":"100","status":"approved","scheme":"visa"},"issuerApprovedAmount":"1234","issuerCardBalance":"2000","verificationAvs":{"code":"+Z","status":"zip match","scheme":"amex"},"verification3ds":{"code":"4","status":"approved","scheme":"6"},"verificationCvv":{"code":"7","status":"approved","scheme":"9"},"userDefined":{"failedPinAttempts":3}},
                merchant = {"mcc":"7311","merchantUniqueId":"9a0f5fe8-f907-4b06-88e9-8dd5141cbf44","location":{"locationId":"3","merchantAddress":{"street":"5565 Glenridge Connector","city":"Atlanta","state":"GA","zipPostalCode":"30342","country":"US"},"hierarchy":"FDC","timezoneOffset":"+02:00","userDefined":{"validAddress":false}},"userDefined":{"highFraudVolume":true}},
        )

    def testScoreOnlyRequest(self):
        """Test ScoreOnlyRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
