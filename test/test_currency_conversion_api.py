# coding: utf-8

"""
    Payment Gateway API Specification.

    Payment Gateway API for payment processing. Version 6.4.0.20181018.001   # noqa: E501

    OpenAPI spec version: 6.4.0.20181018.001
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

        Generate dynamic currency conversion transactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()