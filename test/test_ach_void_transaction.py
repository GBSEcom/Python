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
from openapi_client.models.ach_void_transaction import AchVoidTransaction  # noqa: E501
from openapi_client.rest import ApiException

class TestAchVoidTransaction(unittest.TestCase):
    """AchVoidTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AchVoidTransaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.ach_void_transaction.AchVoidTransaction()  # noqa: E501
        if include_optional :
            return AchVoidTransaction(
                request_type = 'PostAuthTransaction', 
                store_id = '12345500000', 
                merchant_transaction_id = 'lsk23532djljff3', 
                comments = 'This is a comment', 
                order = {"orderId":"ABC12345","billing":{"name":"John Doe","customerId":"1234567890"},"shipping":{"name":"John Doe","address":{"address1":"123 Main St.","city":"Sandy Springs","region":"Georgia","postalCode":"30303","country":"USA"}}}, 
                transaction_amount = {"total":10.24,"currency":"USD","components":{"subtotal":8.0,"localTax":1.0,"shipping":1.24}}
            )
        else :
            return AchVoidTransaction(
                request_type = 'PostAuthTransaction',
                transaction_amount = {"total":10.24,"currency":"USD","components":{"subtotal":8.0,"localTax":1.0,"shipping":1.24}},
        )

    def testAchVoidTransaction(self):
        """Test AchVoidTransaction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
