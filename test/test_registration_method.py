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
from openapi_client.models.registration_method import RegistrationMethod  # noqa: E501
from openapi_client.rest import ApiException

class TestRegistrationMethod(unittest.TestCase):
    """RegistrationMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RegistrationMethod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.registration_method.RegistrationMethod()  # noqa: E501
        if include_optional :
            return RegistrationMethod(
                method_type = 'method/card', 
                method_id = '300fa792-bf5f-418e-aa74-d5b3c81298d2', 
                user_defined = {"failedPinAttempts":3}, 
                billing_phone_number = '123456789', 
                method_alias = 'card one', 
                card = {"cardholderName":"John F. Doe","cardNumber":"5424180279791732","expDate":"122028","cvvPresent":"true","issuer":"Bank of America","cardReissuedNumber":"2"}, 
                method_address = {"street":"Apartment 123","street2":"123 Main Street","stateProvince":"NY","city":"New York","country":"US"}
            )
        else :
            return RegistrationMethod(
                method_type = 'method/card',
                card = {"cardholderName":"John F. Doe","cardNumber":"5424180279791732","expDate":"122028","cvvPresent":"true","issuer":"Bank of America","cardReissuedNumber":"2"},
        )

    def testRegistrationMethod(self):
        """Test RegistrationMethod"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
