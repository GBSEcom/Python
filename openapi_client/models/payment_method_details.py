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


class PaymentMethodDetails(object):
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
        'payment_card': 'PaymentCard',
        'payment_method_type': 'PaymentMethodType'
    }

    attribute_map = {
        'payment_card': 'paymentCard',
        'payment_method_type': 'paymentMethodType'
    }

    def __init__(self, payment_card=None, payment_method_type=None):  # noqa: E501
        """PaymentMethodDetails - a model defined in OpenAPI"""  # noqa: E501

        self._payment_card = None
        self._payment_method_type = None
        self.discriminator = None

        if payment_card is not None:
            self.payment_card = payment_card
        if payment_method_type is not None:
            self.payment_method_type = payment_method_type

    @property
    def payment_card(self):
        """Gets the payment_card of this PaymentMethodDetails.  # noqa: E501


        :return: The payment_card of this PaymentMethodDetails.  # noqa: E501
        :rtype: PaymentCard
        """
        return self._payment_card

    @payment_card.setter
    def payment_card(self, payment_card):
        """Sets the payment_card of this PaymentMethodDetails.


        :param payment_card: The payment_card of this PaymentMethodDetails.  # noqa: E501
        :type: PaymentCard
        """

        self._payment_card = payment_card

    @property
    def payment_method_type(self):
        """Gets the payment_method_type of this PaymentMethodDetails.  # noqa: E501


        :return: The payment_method_type of this PaymentMethodDetails.  # noqa: E501
        :rtype: PaymentMethodType
        """
        return self._payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, payment_method_type):
        """Sets the payment_method_type of this PaymentMethodDetails.


        :param payment_method_type: The payment_method_type of this PaymentMethodDetails.  # noqa: E501
        :type: PaymentMethodType
        """

        self._payment_method_type = payment_method_type

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
        if not isinstance(other, PaymentMethodDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
