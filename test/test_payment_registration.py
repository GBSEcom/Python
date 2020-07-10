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
from openapi_client.models.payment_registration import PaymentRegistration  # noqa: E501
from openapi_client.rest import ApiException

class TestPaymentRegistration(unittest.TestCase):
    """PaymentRegistration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentRegistration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.payment_registration.PaymentRegistration()  # noqa: E501
        if include_optional :
            return PaymentRegistration(
                merchant_ref = 'ffd031516002', 
                transaction_type = 'registration', 
                customer = {"id":"125Xasdf57D","startDate":"2017-01-04","firstName":"John","lastName":"Smith","middleName":"Joseph","email":"accept@xyz.com","sessionId":"session-1","username":"username","gender":"male","dateOfBirth":"1982","address":{"street":"Apartment 123","street2":"123 Main Street","stateProvince":"NY","city":"New York","country":"US","phone":{"type":"mobile","number":"212-515-1212"},"zipPostalCode":"11375"},"userDefined":{"previouslyAffected":"Y"}}, 
                merchant = {"mcc":"7311","merchantUniqueId":"9a0f5fe8-f907-4b06-88e9-8dd5141cbf44","location":{"locationId":"3","merchantAddress":{"street":"5565 Glenridge Connector","city":"Atlanta","state":"GA","zipPostalCode":"30342","country":"US"},"hierarchy":"FDC","timezoneOffset":"+02:00","userDefined":{"validAddress":false}},"userDefined":{"highFraudVolume":true}}, 
                device = {"deviceType":"device/mobile","deviceId":"BDE000:008945:58AC03:F02569","networks":[{"networkType":"network/wifi","ip":"10.201.0.244","mac":"02:00:00:00:00:00","ssid":"Boston-5G-1","bssid":"e8:fc:af:fb:4b:8c","userDefined":{"battery":"5h 10m"}}],"latitude":41.14961,"longitude":-8.61099,"imei":"49-015420-323751","model":"iPhone 10","manufacturer":"Apple","timezoneOffset":"+02:00","rooted":false,"malwareDetected":false,"userDefined":{"battery":"95%"}}, 
                user_defined = {"inauthTransId":"1234"}, 
                original_transaction_type = 'registration/method/card', 
                issuer_response = {"code":"100","status":"approved","scheme":"visa"}, 
                verification_avs = {"code":"+Z","status":"zip match","scheme":"amex"}, 
                verification3ds = {"code":"4","status":"approved","scheme":"6"}, 
                verification_cvv = {"code":"7","status":"approved","scheme":"9"}, 
                registration_method = {"methodType":"method/card","methodId":"300fa792-bf5f-418e-aa74-d5b3c81298d2","methodAlias":"card one","billingPhoneNumber":"123456789","userDefined":{"failedPinAttempts":20},"card":{"cardholderName":"John F. Doe","cardNumber":"5424180279791732","expDate":"122028","cvvPresent":"true","issuer":"Bank of America","cardReissuedNumber":"2"},"methodAddress":{"street":"125 Main Street","street2":"Apartment 123","stateProvince":"NY","city":"New York","country":"US","zipPostalCode":"11375"}}
            )
        else :
            return PaymentRegistration(
                transaction_type = 'registration',
                customer = {"id":"125Xasdf57D","startDate":"2017-01-04","firstName":"John","lastName":"Smith","middleName":"Joseph","email":"accept@xyz.com","sessionId":"session-1","username":"username","gender":"male","dateOfBirth":"1982","address":{"street":"Apartment 123","street2":"123 Main Street","stateProvince":"NY","city":"New York","country":"US","phone":{"type":"mobile","number":"212-515-1212"},"zipPostalCode":"11375"},"userDefined":{"previouslyAffected":"Y"}},
                merchant = {"mcc":"7311","merchantUniqueId":"9a0f5fe8-f907-4b06-88e9-8dd5141cbf44","location":{"locationId":"3","merchantAddress":{"street":"5565 Glenridge Connector","city":"Atlanta","state":"GA","zipPostalCode":"30342","country":"US"},"hierarchy":"FDC","timezoneOffset":"+02:00","userDefined":{"validAddress":false}},"userDefined":{"highFraudVolume":true}},
                original_transaction_type = 'registration/method/card',
                registration_method = {"methodType":"method/card","methodId":"300fa792-bf5f-418e-aa74-d5b3c81298d2","methodAlias":"card one","billingPhoneNumber":"123456789","userDefined":{"failedPinAttempts":20},"card":{"cardholderName":"John F. Doe","cardNumber":"5424180279791732","expDate":"122028","cvvPresent":"true","issuer":"Bank of America","cardReissuedNumber":"2"},"methodAddress":{"street":"125 Main Street","street2":"Apartment 123","stateProvince":"NY","city":"New York","country":"US","zipPostalCode":"11375"}},
        )

    def testPaymentRegistration(self):
        """Test PaymentRegistration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
