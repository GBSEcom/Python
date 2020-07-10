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
from openapi_client.models.payment_card_disbursement_transaction_all_of import PaymentCardDisbursementTransactionAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestPaymentCardDisbursementTransactionAllOf(unittest.TestCase):
    """PaymentCardDisbursementTransactionAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentCardDisbursementTransactionAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.payment_card_disbursement_transaction_all_of.PaymentCardDisbursementTransactionAllOf()  # noqa: E501
        if include_optional :
            return PaymentCardDisbursementTransactionAllOf(
                disbursement = {"disbursementType":"DisbursementTransactionType","senderInfo":{"name":"Franklin Sender Roosevelt","streetAddress":"5565 Glenridge Connector","city":"Atlanta","stateCode":"GA","countryCode":"US","postalCode":"30342","phoneNumber":"4044040740","birthDate":"19560121","referenceNumber":"12345678","accountNumber":"135246"},"receiverInfo":{"name":"Abraham Receiver Lincoln","streetAddress":"5565 Glenridge Connector","city":"Atlanta","stateCode":"GA","countryCode":"US","postalCode":"30342","phoneNumber":"4044040740","referenceNumber":"12345678","accountNumber":"135246"}}, 
                payment_method = {"paymentCard":{"number":"5424180279791732","expiryDate":{"month":"03","year":"21"},"securityCode":"977"},"paymentFacilitator":{"externalMerchantId":"12345","paymentFacilitatorId":"123123123","saleOrganizationId":"123124214","name":"First Reseller","subMerchantData":{"mcc":"1432","legalName":"First Merchant","timezone":"Europe/London","address":{"address1":"123 Main St.","city":"Sandy Springs","region":"Georgia","postalCode":"30303","country":"USA"},"document":{"type":"NATIONAL_IDENTITY","number":"12345666544"},"merchantId":"12435325235"}}}, 
                stored_credentials = {"sequence":"SUBSEQUENT","scheduled":false,"referencedSchemeTransactionId":"019087868716215","initiator":"CARDHOLDER"}, 
                create_token = {"value":"234ljl124l12","reusable":true,"declineDuplicates":false}
            )
        else :
            return PaymentCardDisbursementTransactionAllOf(
                disbursement = {"disbursementType":"DisbursementTransactionType","senderInfo":{"name":"Franklin Sender Roosevelt","streetAddress":"5565 Glenridge Connector","city":"Atlanta","stateCode":"GA","countryCode":"US","postalCode":"30342","phoneNumber":"4044040740","birthDate":"19560121","referenceNumber":"12345678","accountNumber":"135246"},"receiverInfo":{"name":"Abraham Receiver Lincoln","streetAddress":"5565 Glenridge Connector","city":"Atlanta","stateCode":"GA","countryCode":"US","postalCode":"30342","phoneNumber":"4044040740","referenceNumber":"12345678","accountNumber":"135246"}},
                payment_method = {"paymentCard":{"number":"5424180279791732","expiryDate":{"month":"03","year":"21"},"securityCode":"977"},"paymentFacilitator":{"externalMerchantId":"12345","paymentFacilitatorId":"123123123","saleOrganizationId":"123124214","name":"First Reseller","subMerchantData":{"mcc":"1432","legalName":"First Merchant","timezone":"Europe/London","address":{"address1":"123 Main St.","city":"Sandy Springs","region":"Georgia","postalCode":"30303","country":"USA"},"document":{"type":"NATIONAL_IDENTITY","number":"12345666544"},"merchantId":"12435325235"}}},
        )

    def testPaymentCardDisbursementTransactionAllOf(self):
        """Test PaymentCardDisbursementTransactionAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
