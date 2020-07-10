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
from openapi_client.models.account_updater_response import AccountUpdaterResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestAccountUpdaterResponse(unittest.TestCase):
    """AccountUpdaterResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountUpdaterResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.account_updater_response.AccountUpdaterResponse()  # noqa: E501
        if include_optional :
            return AccountUpdaterResponse(
                updated_card = '4012000066660018', 
                updated_token = '1235325235236', 
                updated_expiration_date = '1220', 
                updated_account_status = 'A', 
                updated_account_error_code = 'VAU002'
            )
        else :
            return AccountUpdaterResponse(
        )

    def testAccountUpdaterResponse(self):
        """Test AccountUpdaterResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
