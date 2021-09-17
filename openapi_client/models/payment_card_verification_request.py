# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.4.0.20210824.002
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaymentCardVerificationRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'request_type': 'str',
        'billing_address': 'Address',
        'store_id': 'str',
        'merchant_transaction_id': 'str',
        'additional_details': 'AdditionalDetails',
        'payment_card': 'PaymentCard'
    }

    attribute_map = {
        'request_type': 'requestType',
        'billing_address': 'billingAddress',
        'store_id': 'storeId',
        'merchant_transaction_id': 'merchantTransactionId',
        'additional_details': 'additionalDetails',
        'payment_card': 'paymentCard'
    }

    def __init__(self, request_type=None, billing_address=None, store_id=None, merchant_transaction_id=None, additional_details=None, payment_card=None):  # noqa: E501
        """PaymentCardVerificationRequest - a model defined in OpenAPI"""  # noqa: E501

        self._request_type = None
        self._billing_address = None
        self._store_id = None
        self._merchant_transaction_id = None
        self._additional_details = None
        self._payment_card = None
        self.discriminator = None

        self.request_type = request_type
        if billing_address is not None:
            self.billing_address = billing_address
        if store_id is not None:
            self.store_id = store_id
        if merchant_transaction_id is not None:
            self.merchant_transaction_id = merchant_transaction_id
        if additional_details is not None:
            self.additional_details = additional_details
        self.payment_card = payment_card

    @property
    def request_type(self):
        """Gets the request_type of this PaymentCardVerificationRequest.  # noqa: E501

        Object name of the account verification request.  # noqa: E501

        :return: The request_type of this PaymentCardVerificationRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this PaymentCardVerificationRequest.

        Object name of the account verification request.  # noqa: E501

        :param request_type: The request_type of this PaymentCardVerificationRequest.  # noqa: E501
        :type: str
        """
        if request_type is None:
            raise ValueError("Invalid value for `request_type`, must not be `None`")  # noqa: E501

        self._request_type = request_type

    @property
    def billing_address(self):
        """Gets the billing_address of this PaymentCardVerificationRequest.  # noqa: E501


        :return: The billing_address of this PaymentCardVerificationRequest.  # noqa: E501
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this PaymentCardVerificationRequest.


        :param billing_address: The billing_address of this PaymentCardVerificationRequest.  # noqa: E501
        :type: Address
        """

        self._billing_address = billing_address

    @property
    def store_id(self):
        """Gets the store_id of this PaymentCardVerificationRequest.  # noqa: E501

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :return: The store_id of this PaymentCardVerificationRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this PaymentCardVerificationRequest.

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :param store_id: The store_id of this PaymentCardVerificationRequest.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def merchant_transaction_id(self):
        """Gets the merchant_transaction_id of this PaymentCardVerificationRequest.  # noqa: E501

        The unique merchant transaction ID from the request, if supplied.  # noqa: E501

        :return: The merchant_transaction_id of this PaymentCardVerificationRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(self, merchant_transaction_id):
        """Sets the merchant_transaction_id of this PaymentCardVerificationRequest.

        The unique merchant transaction ID from the request, if supplied.  # noqa: E501

        :param merchant_transaction_id: The merchant_transaction_id of this PaymentCardVerificationRequest.  # noqa: E501
        :type: str
        """
        if merchant_transaction_id is not None and len(merchant_transaction_id) > 40:
            raise ValueError("Invalid value for `merchant_transaction_id`, length must be less than or equal to `40`")  # noqa: E501

        self._merchant_transaction_id = merchant_transaction_id

    @property
    def additional_details(self):
        """Gets the additional_details of this PaymentCardVerificationRequest.  # noqa: E501


        :return: The additional_details of this PaymentCardVerificationRequest.  # noqa: E501
        :rtype: AdditionalDetails
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """Sets the additional_details of this PaymentCardVerificationRequest.


        :param additional_details: The additional_details of this PaymentCardVerificationRequest.  # noqa: E501
        :type: AdditionalDetails
        """

        self._additional_details = additional_details

    @property
    def payment_card(self):
        """Gets the payment_card of this PaymentCardVerificationRequest.  # noqa: E501


        :return: The payment_card of this PaymentCardVerificationRequest.  # noqa: E501
        :rtype: PaymentCard
        """
        return self._payment_card

    @payment_card.setter
    def payment_card(self, payment_card):
        """Sets the payment_card of this PaymentCardVerificationRequest.


        :param payment_card: The payment_card of this PaymentCardVerificationRequest.  # noqa: E501
        :type: PaymentCard
        """
        if payment_card is None:
            raise ValueError("Invalid value for `payment_card`, must not be `None`")  # noqa: E501

        self._payment_card = payment_card

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentCardVerificationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
