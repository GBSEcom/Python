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
from openapi_client.models.shared_secret_configuration_response import SharedSecretConfigurationResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestSharedSecretConfigurationResponse(unittest.TestCase):
    """SharedSecretConfigurationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SharedSecretConfigurationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shared_secret_configuration_response.SharedSecretConfigurationResponse()  # noqa: E501
        if include_optional :
            return SharedSecretConfigurationResponse(
                client_request_id = '30dd879c-ee2f-11db-8314-0800200c9a66', 
                api_trace_id = 'rrt-0bd552c12342d3448-b-ea-1142-12938318-7', 
                response_type = 'Unauthenticated', 
                store_id = '12345500000', 
                shared_secret = '6768tr457r', 
                response_message = 'SUCCESS', 
                response_timestamp = 1561035070
            )
        else :
            return SharedSecretConfigurationResponse(
        )

    def testSharedSecretConfigurationResponse(self):
        """Test SharedSecretConfigurationResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
