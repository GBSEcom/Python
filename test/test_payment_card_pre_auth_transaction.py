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
from openapi_client.models.payment_card_pre_auth_transaction import PaymentCardPreAuthTransaction  # noqa: E501
from openapi_client.rest import ApiException

class TestPaymentCardPreAuthTransaction(unittest.TestCase):
    """PaymentCardPreAuthTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentCardPreAuthTransaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.payment_card_pre_auth_transaction.PaymentCardPreAuthTransaction()  # noqa: E501
        if include_optional :
            return PaymentCardPreAuthTransaction(
                request_type = 'PaymentCardCreditTransaction', 
                transaction_amount = {"total":10.24,"currency":"USD","components":{"subtotal":8.0,"localTax":1.0,"shipping":1.24}}, 
                store_id = '12345500000', 
                merchant_transaction_id = '30dd879c-ee2f-11db-8314-0800200c9a66', 
                transaction_origin = 'ECOM', 
                order = {"orderId":"ABC12345","billing":{"name":"John Doe","customerId":"1234567890"},"shipping":{"name":"John Doe","address":{"address1":"123 Main St.","city":"Sandy Springs","region":"Georgia","postalCode":"30303","country":"USA"}}}, 
                payment_method = {"paymentCard":{"number":"5424180279791732","expiryDate":{"month":"03","year":"21"},"securityCode":"977"},"paymentFacilitator":{"externalMerchantId":"12345","paymentFacilitatorId":"123123123","saleOrganizationId":"123124214","name":"First Reseller","subMerchantData":{"mcc":"1432","legalName":"First Merchant","timezone":"Europe/London","address":{"address1":"123 Main St.","city":"Sandy Springs","region":"Georgia","postalCode":"30303","country":"USA"},"document":{"type":"NATIONAL_IDENTITY","number":"12345666544"},"merchantId":"12435325235"}}}, 
                stored_credentials = {"sequence":"SUBSEQUENT","scheduled":false,"referencedSchemeTransactionId":"019087868716215","initiator":"CARDHOLDER"}, 
                create_token = {"value":"234ljl124l12","reusable":true,"declineDuplicates":false}, 
                split_shipment = {"totalCount":1,"finalShipment":true}, 
                settlement_split = [{"merchantID":"100000001","amount":25.06},{"merchantID":"100000002","amount":15.07}], 
                authentication_request = {"authenticationType":"UnionPayAuthenticationRequest"}, 
                authentication_result = {"authenticationType":"Secure3D10AuthenticationResult"}, 
                decremental_flag = False
            )
        else :
            return PaymentCardPreAuthTransaction(
                request_type = 'PaymentCardCreditTransaction',
                transaction_amount = {"total":10.24,"currency":"USD","components":{"subtotal":8.0,"localTax":1.0,"shipping":1.24}},
                payment_method = {"paymentCard":{"number":"5424180279791732","expiryDate":{"month":"03","year":"21"},"securityCode":"977"},"paymentFacilitator":{"externalMerchantId":"12345","paymentFacilitatorId":"123123123","saleOrganizationId":"123124214","name":"First Reseller","subMerchantData":{"mcc":"1432","legalName":"First Merchant","timezone":"Europe/London","address":{"address1":"123 Main St.","city":"Sandy Springs","region":"Georgia","postalCode":"30303","country":"USA"},"document":{"type":"NATIONAL_IDENTITY","number":"12345666544"},"merchantId":"12435325235"}}},
        )

    def testPaymentCardPreAuthTransaction(self):
        """Test PaymentCardPreAuthTransaction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
