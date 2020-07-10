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
from openapi_client.models.purchase_cards_level2 import PurchaseCardsLevel2  # noqa: E501
from openapi_client.rest import ApiException

class TestPurchaseCardsLevel2(unittest.TestCase):
    """PurchaseCardsLevel2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PurchaseCardsLevel2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.purchase_cards_level2.PurchaseCardsLevel2()  # noqa: E501
        if include_optional :
            return PurchaseCardsLevel2(
                customer_reference_id = 'abcdef123xyz', 
                supplier_invoice_number = '0000000065348', 
                supplier_vat_registration_number = '10001174242', 
                total_discount_amount_and_rate = {"amount":5.145,"rate":1.175}, 
                vat_shipping_amount_and_rate = {"amount":5.145,"rate":1.175}
            )
        else :
            return PurchaseCardsLevel2(
        )

    def testPurchaseCardsLevel2(self):
        """Test PurchaseCardsLevel2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
