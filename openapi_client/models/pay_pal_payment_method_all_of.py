# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.9.1.20191223.002
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PayPalPaymentMethodAllOf(object):
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
        'pay_pal': 'PayPal'
    }

    attribute_map = {
        'pay_pal': 'payPal'
    }

    def __init__(self, pay_pal=None):  # noqa: E501
        """PayPalPaymentMethodAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._pay_pal = None
        self.discriminator = None

        self.pay_pal = pay_pal

    @property
    def pay_pal(self):
        """Gets the pay_pal of this PayPalPaymentMethodAllOf.  # noqa: E501


        :return: The pay_pal of this PayPalPaymentMethodAllOf.  # noqa: E501
        :rtype: PayPal
        """
        return self._pay_pal

    @pay_pal.setter
    def pay_pal(self, pay_pal):
        """Sets the pay_pal of this PayPalPaymentMethodAllOf.


        :param pay_pal: The pay_pal of this PayPalPaymentMethodAllOf.  # noqa: E501
        :type: PayPal
        """
        if pay_pal is None:
            raise ValueError("Invalid value for `pay_pal`, must not be `None`")  # noqa: E501

        self._pay_pal = pay_pal

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
        if not isinstance(other, PayPalPaymentMethodAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
