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


class ManagedRedirectPaymentMethod(object):
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
        'payment_method_type': 'str',
        'payment_details': 'list[ManagedRedirectPaymentMethodPaymentDetails]'
    }

    attribute_map = {
        'payment_method_type': 'paymentMethodType',
        'payment_details': 'paymentDetails'
    }

    def __init__(self, payment_method_type=None, payment_details=None):  # noqa: E501
        """ManagedRedirectPaymentMethod - a model defined in OpenAPI"""  # noqa: E501

        self._payment_method_type = None
        self._payment_details = None
        self.discriminator = None

        if payment_method_type is not None:
            self.payment_method_type = payment_method_type
        if payment_details is not None:
            self.payment_details = payment_details

    @property
    def payment_method_type(self):
        """Gets the payment_method_type of this ManagedRedirectPaymentMethod.  # noqa: E501

        Payment Method Type Enum  # noqa: E501

        :return: The payment_method_type of this ManagedRedirectPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, payment_method_type):
        """Sets the payment_method_type of this ManagedRedirectPaymentMethod.

        Payment Method Type Enum  # noqa: E501

        :param payment_method_type: The payment_method_type of this ManagedRedirectPaymentMethod.  # noqa: E501
        :type: str
        """
        allowed_values = ["APPLEPAY", "BCMC_APM", "GOOGLEPAY", "IDEAL", "INDIAWALLET"]  # noqa: E501
        if payment_method_type not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_method_type` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_method_type, allowed_values)
            )

        self._payment_method_type = payment_method_type

    @property
    def payment_details(self):
        """Gets the payment_details of this ManagedRedirectPaymentMethod.  # noqa: E501

        Key Value pairs of Payment detail appropriate for the Payment Method Type  # noqa: E501

        :return: The payment_details of this ManagedRedirectPaymentMethod.  # noqa: E501
        :rtype: list[ManagedRedirectPaymentMethodPaymentDetails]
        """
        return self._payment_details

    @payment_details.setter
    def payment_details(self, payment_details):
        """Sets the payment_details of this ManagedRedirectPaymentMethod.

        Key Value pairs of Payment detail appropriate for the Payment Method Type  # noqa: E501

        :param payment_details: The payment_details of this ManagedRedirectPaymentMethod.  # noqa: E501
        :type: list[ManagedRedirectPaymentMethodPaymentDetails]
        """

        self._payment_details = payment_details

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
        if not isinstance(other, ManagedRedirectPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
