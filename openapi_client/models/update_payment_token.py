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


class UpdatePaymentToken(object):
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
        'payment_card': 'PaymentCard'
    }

    attribute_map = {
        'value': 'value',
        'reusable': 'reusable',
        'decline_duplicates': 'declineDuplicates',
        'payment_card': 'paymentCard'
    }

    def __init__(self, value=None, reusable=True, decline_duplicates=False, payment_card=None):  # noqa: E501
        """UpdatePaymentToken - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._reusable = None
        self._decline_duplicates = None
        self._payment_card = None
        self.discriminator = None

        self.value = value
        if reusable is not None:
            self.reusable = reusable
        if decline_duplicates is not None:
            self.decline_duplicates = decline_duplicates
        self.payment_card = payment_card

    @property
    def value(self):
        """Gets the value of this UpdatePaymentToken.  # noqa: E501

        Client-supplied payment token value.  # noqa: E501

        :return: The value of this UpdatePaymentToken.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdatePaymentToken.

        Client-supplied payment token value.  # noqa: E501

        :param value: The value of this UpdatePaymentToken.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def reusable(self):
        """Gets the reusable of this UpdatePaymentToken.  # noqa: E501

        If the token is reusable.  # noqa: E501

        :return: The reusable of this UpdatePaymentToken.  # noqa: E501
        :rtype: bool
        """
        return self._reusable

    @reusable.setter
    def reusable(self, reusable):
        """Sets the reusable of this UpdatePaymentToken.

        If the token is reusable.  # noqa: E501

        :param reusable: The reusable of this UpdatePaymentToken.  # noqa: E501
        :type: bool
        """

        self._reusable = reusable

    @property
    def decline_duplicates(self):
        """Gets the decline_duplicates of this UpdatePaymentToken.  # noqa: E501

        Decline duplicate payment info if client token is supplied.  # noqa: E501

        :return: The decline_duplicates of this UpdatePaymentToken.  # noqa: E501
        :rtype: bool
        """
        return self._decline_duplicates

    @decline_duplicates.setter
    def decline_duplicates(self, decline_duplicates):
        """Sets the decline_duplicates of this UpdatePaymentToken.

        Decline duplicate payment info if client token is supplied.  # noqa: E501

        :param decline_duplicates: The decline_duplicates of this UpdatePaymentToken.  # noqa: E501
        :type: bool
        """

        self._decline_duplicates = decline_duplicates

    @property
    def payment_card(self):
        """Gets the payment_card of this UpdatePaymentToken.  # noqa: E501


        :return: The payment_card of this UpdatePaymentToken.  # noqa: E501
        :rtype: PaymentCard
        """
        return self._payment_card

    @payment_card.setter
    def payment_card(self, payment_card):
        """Sets the payment_card of this UpdatePaymentToken.


        :param payment_card: The payment_card of this UpdatePaymentToken.  # noqa: E501
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
        if not isinstance(other, UpdatePaymentToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
