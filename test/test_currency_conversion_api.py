# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.4.0.20210824.002
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.currency_conversion_api import CurrencyConversionApi  # noqa: E501
from openapi_client.rest import ApiException


class TestCurrencyConversionApi(unittest.TestCase):
    """CurrencyConversionApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.currency_conversion_api.CurrencyConversionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_exchange_rate(self):
        """Test case for get_exchange_rate

        Generate dynamic currency conversion transactions.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
