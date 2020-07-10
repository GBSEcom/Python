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
from openapi_client.models.payment_url_detail_response_all_of import PaymentUrlDetailResponseAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestPaymentUrlDetailResponseAllOf(unittest.TestCase):
    """PaymentUrlDetailResponseAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentUrlDetailResponseAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.payment_url_detail_response_all_of.PaymentUrlDetailResponseAllOf()  # noqa: E501
        if include_optional :
            return PaymentUrlDetailResponseAllOf(
                payment_url_details = [
                    openapi_client.models.payment_url_detail.PaymentUrlDetail(
                        payment_url = 'https://api.firstdata.com/connect/gateway/processing?storename=123456789&oid=R-96cdbaa4-c22e-4598-a2f1-c2b5fed79ef1&paymentUrlId=d3eb74fe-cf63-47e1-b89f-52ba0cc7965c', 
                        merchant_transaction_id = 'lsk23532djljff3', 
                        order_id = '123456', 
                        request_time = 1518811817, 
                        status = 'Created', )
                    ]
            )
        else :
            return PaymentUrlDetailResponseAllOf(
        )

    def testPaymentUrlDetailResponseAllOf(self):
        """Test PaymentUrlDetailResponseAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
