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
from openapi_client.models.fraud_registration_response import FraudRegistrationResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestFraudRegistrationResponse(unittest.TestCase):
    """FraudRegistrationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FraudRegistrationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.fraud_registration_response.FraudRegistrationResponse()  # noqa: E501
        if include_optional :
            return FraudRegistrationResponse(
                correlation_id = '228.6277057434761', 
                transaction_status = 'Not Processed', 
                validation_status = 'success', 
                transaction_type = 'registration', 
                fraud_score = {"score":"100","recommendedDecision":"approve","warnings":["warning1","warning2"],"explanations":[{"description":"Suspicious transaction amount.","type":"explanation/model"},{"description":"Suspicious pattern compared to number of transactions in the past 1 month for the card.","type":"explanation/rule","rule":"QSR_14"}]}, 
                error = {"messages":[{"code":"invalid_transaction_type","description":"The transaction type is not supported"},{"code":"missing_originalTransactionType","description":"Original Transaction Type is missing or invalid"}]}
            )
        else :
            return FraudRegistrationResponse(
        )

    def testFraudRegistrationResponse(self):
        """Test FraudRegistrationResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
