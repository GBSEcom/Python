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


class PaymentDevicePaymentTokenizationRequestAllOf(object):
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
        'payment_device': 'PaymentDevice'
    }

    attribute_map = {
        'payment_device': 'paymentDevice'
    }

    def __init__(self, payment_device=None, local_vars_configuration=None):  # noqa: E501
        """PaymentDevicePaymentTokenizationRequestAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payment_device = None
        self.discriminator = None

        self.payment_device = payment_device

    @property
    def payment_device(self):
        """Gets the payment_device of this PaymentDevicePaymentTokenizationRequestAllOf.  # noqa: E501


        :return: The payment_device of this PaymentDevicePaymentTokenizationRequestAllOf.  # noqa: E501
        :rtype: PaymentDevice
        """
        return self._payment_device

    @payment_device.setter
    def payment_device(self, payment_device):
        """Sets the payment_device of this PaymentDevicePaymentTokenizationRequestAllOf.


        :param payment_device: The payment_device of this PaymentDevicePaymentTokenizationRequestAllOf.  # noqa: E501
        :type: PaymentDevice
        """
        if self.local_vars_configuration.client_side_validation and payment_device is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_device`, must not be `None`")  # noqa: E501

        self._payment_device = payment_device

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
        if not isinstance(other, PaymentDevicePaymentTokenizationRequestAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentDevicePaymentTokenizationRequestAllOf):
            return True

        return self.to_dict() != other.to_dict()
