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
from openapi_client.api.payment_token_api import PaymentTokenApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPaymentTokenApi(unittest.TestCase):
    """PaymentTokenApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.payment_token_api.PaymentTokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_payment_token(self):
        """Test case for create_payment_token

        Create a payment token from a payment card.  # noqa: E501
        """
        pass

    def test_delete_payment_token(self):
        """Test case for delete_payment_token

        Delete a payment token.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()