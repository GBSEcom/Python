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
from openapi_client.models.mcc6012 import Mcc6012  # noqa: E501
from openapi_client.rest import ApiException

class TestMcc6012(unittest.TestCase):
    """Mcc6012 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Mcc6012
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.mcc6012.Mcc6012()  # noqa: E501
        if include_optional :
            return Mcc6012(
                date_of_birth = '20200505', 
                account_first6 = '411111', 
                account_last4 = '2343', 
                account_num = '146789900034567', 
                post_code = '30101', 
                surname = 'Walker'
            )
        else :
            return Mcc6012(
        )

    def testMcc6012(self):
        """Test Mcc6012"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
