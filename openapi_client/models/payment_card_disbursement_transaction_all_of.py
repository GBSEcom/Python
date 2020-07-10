# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.12.0.20200605.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class PaymentCardDisbursementTransactionAllOf(object):
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
        'disbursement': 'Disbursement',
        'payment_method': 'PaymentCardPaymentMethod',
        'stored_credentials': 'StoredCredential',
        'create_token': 'CreatePaymentToken'
    }

    attribute_map = {
        'disbursement': 'disbursement',
        'payment_method': 'paymentMethod',
        'stored_credentials': 'storedCredentials',
        'create_token': 'createToken'
    }

    def __init__(self, disbursement=None, payment_method=None, stored_credentials=None, create_token=None, local_vars_configuration=None):  # noqa: E501
        """PaymentCardDisbursementTransactionAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._disbursement = None
        self._payment_method = None
        self._stored_credentials = None
        self._create_token = None
        self.discriminator = None

        self.disbursement = disbursement
        self.payment_method = payment_method
        if stored_credentials is not None:
            self.stored_credentials = stored_credentials
        if create_token is not None:
            self.create_token = create_token

    @property
    def disbursement(self):
        """Gets the disbursement of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501


        :return: The disbursement of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501
        :rtype: Disbursement
        """
        return self._disbursement

    @disbursement.setter
    def disbursement(self, disbursement):
        """Sets the disbursement of this PaymentCardDisbursementTransactionAllOf.


        :param disbursement: The disbursement of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501
        :type: Disbursement
        """
        if self.local_vars_configuration.client_side_validation and disbursement is None:  # noqa: E501
            raise ValueError("Invalid value for `disbursement`, must not be `None`")  # noqa: E501

        self._disbursement = disbursement

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501


        :return: The payment_method of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501
        :rtype: PaymentCardPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentCardDisbursementTransactionAllOf.


        :param payment_method: The payment_method of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501
        :type: PaymentCardPaymentMethod
        """
        if self.local_vars_configuration.client_side_validation and payment_method is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def stored_credentials(self):
        """Gets the stored_credentials of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501


        :return: The stored_credentials of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501
        :rtype: StoredCredential
        """
        return self._stored_credentials

    @stored_credentials.setter
    def stored_credentials(self, stored_credentials):
        """Sets the stored_credentials of this PaymentCardDisbursementTransactionAllOf.


        :param stored_credentials: The stored_credentials of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501
        :type: StoredCredential
        """

        self._stored_credentials = stored_credentials

    @property
    def create_token(self):
        """Gets the create_token of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501


        :return: The create_token of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501
        :rtype: CreatePaymentToken
        """
        return self._create_token

    @create_token.setter
    def create_token(self, create_token):
        """Sets the create_token of this PaymentCardDisbursementTransactionAllOf.


        :param create_token: The create_token of this PaymentCardDisbursementTransactionAllOf.  # noqa: E501
        :type: CreatePaymentToken
        """

        self._create_token = create_token

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
        if not isinstance(other, PaymentCardDisbursementTransactionAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentCardDisbursementTransactionAllOf):
            return True

        return self.to_dict() != other.to_dict()
