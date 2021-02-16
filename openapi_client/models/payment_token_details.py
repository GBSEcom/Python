# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.1.0.20210122.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaymentTokenDetails(object):
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
        'value': 'str',
        'reusable': 'bool',
        'decline_duplicates': 'bool',
        'last4': 'str',
        'brand': 'str',
        'account_verification': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'value': 'value',
        'reusable': 'reusable',
        'decline_duplicates': 'declineDuplicates',
        'last4': 'last4',
        'brand': 'brand',
        'account_verification': 'accountVerification',
        'type': 'type'
    }

    def __init__(self, value=None, reusable=True, decline_duplicates=False, last4=None, brand=None, account_verification=None, type=None):  # noqa: E501
        """PaymentTokenDetails - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._reusable = None
        self._decline_duplicates = None
        self._last4 = None
        self._brand = None
        self._account_verification = None
        self._type = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if reusable is not None:
            self.reusable = reusable
        if decline_duplicates is not None:
            self.decline_duplicates = decline_duplicates
        if last4 is not None:
            self.last4 = last4
        if brand is not None:
            self.brand = brand
        if account_verification is not None:
            self.account_verification = account_verification
        if type is not None:
            self.type = type

    @property
    def value(self):
        """Gets the value of this PaymentTokenDetails.  # noqa: E501

        Client-supplied payment token value. Only applicable for DataVault tokenization scheme.  # noqa: E501

        :return: The value of this PaymentTokenDetails.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PaymentTokenDetails.

        Client-supplied payment token value. Only applicable for DataVault tokenization scheme.  # noqa: E501

        :param value: The value of this PaymentTokenDetails.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def reusable(self):
        """Gets the reusable of this PaymentTokenDetails.  # noqa: E501

        If the token is reusable.  # noqa: E501

        :return: The reusable of this PaymentTokenDetails.  # noqa: E501
        :rtype: bool
        """
        return self._reusable

    @reusable.setter
    def reusable(self, reusable):
        """Sets the reusable of this PaymentTokenDetails.

        If the token is reusable.  # noqa: E501

        :param reusable: The reusable of this PaymentTokenDetails.  # noqa: E501
        :type: bool
        """

        self._reusable = reusable

    @property
    def decline_duplicates(self):
        """Gets the decline_duplicates of this PaymentTokenDetails.  # noqa: E501

        Decline duplicate payment info if client token is supplied.  # noqa: E501

        :return: The decline_duplicates of this PaymentTokenDetails.  # noqa: E501
        :rtype: bool
        """
        return self._decline_duplicates

    @decline_duplicates.setter
    def decline_duplicates(self, decline_duplicates):
        """Sets the decline_duplicates of this PaymentTokenDetails.

        Decline duplicate payment info if client token is supplied.  # noqa: E501

        :param decline_duplicates: The decline_duplicates of this PaymentTokenDetails.  # noqa: E501
        :type: bool
        """

        self._decline_duplicates = decline_duplicates

    @property
    def last4(self):
        """Gets the last4 of this PaymentTokenDetails.  # noqa: E501

        The last 4 numbers of a payment card.  # noqa: E501

        :return: The last4 of this PaymentTokenDetails.  # noqa: E501
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """Sets the last4 of this PaymentTokenDetails.

        The last 4 numbers of a payment card.  # noqa: E501

        :param last4: The last4 of this PaymentTokenDetails.  # noqa: E501
        :type: str
        """

        self._last4 = last4

    @property
    def brand(self):
        """Gets the brand of this PaymentTokenDetails.  # noqa: E501

        Card brand, only for tokenization with payment.  # noqa: E501

        :return: The brand of this PaymentTokenDetails.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentTokenDetails.

        Card brand, only for tokenization with payment.  # noqa: E501

        :param brand: The brand of this PaymentTokenDetails.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def account_verification(self):
        """Gets the account_verification of this PaymentTokenDetails.  # noqa: E501

        If the account the token was created from has been verified.  # noqa: E501

        :return: The account_verification of this PaymentTokenDetails.  # noqa: E501
        :rtype: bool
        """
        return self._account_verification

    @account_verification.setter
    def account_verification(self, account_verification):
        """Sets the account_verification of this PaymentTokenDetails.

        If the account the token was created from has been verified.  # noqa: E501

        :param account_verification: The account_verification of this PaymentTokenDetails.  # noqa: E501
        :type: bool
        """

        self._account_verification = account_verification

    @property
    def type(self):
        """Gets the type of this PaymentTokenDetails.  # noqa: E501

        Inidcates the type of tokenization source.  # noqa: E501

        :return: The type of this PaymentTokenDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentTokenDetails.

        Inidcates the type of tokenization source.  # noqa: E501

        :param type: The type of this PaymentTokenDetails.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, PaymentTokenDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
