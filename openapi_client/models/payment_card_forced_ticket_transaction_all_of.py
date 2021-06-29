# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.3.0.20210608.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaymentCardForcedTicketTransactionAllOf(object):
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
        'payment_method': 'PaymentCardPaymentMethod',
        'reference_number': 'str'
    }

    attribute_map = {
        'payment_method': 'paymentMethod',
        'reference_number': 'referenceNumber'
    }

    def __init__(self, payment_method=None, reference_number=None):  # noqa: E501
        """PaymentCardForcedTicketTransactionAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._payment_method = None
        self._reference_number = None
        self.discriminator = None

        self.payment_method = payment_method
        self.reference_number = reference_number

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501


        :return: The payment_method of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :rtype: PaymentCardPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentCardForcedTicketTransactionAllOf.


        :param payment_method: The payment_method of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :type: PaymentCardPaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def reference_number(self):
        """Gets the reference_number of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501

        Stores the six-digit reference number you have received as the result of a successful external authorization (e.g. by phone). The gateway needs this number for uniquely mapping a ForcedTicket transaction to a previously performed external authorization.  # noqa: E501

        :return: The reference_number of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this PaymentCardForcedTicketTransactionAllOf.

        Stores the six-digit reference number you have received as the result of a successful external authorization (e.g. by phone). The gateway needs this number for uniquely mapping a ForcedTicket transaction to a previously performed external authorization.  # noqa: E501

        :param reference_number: The reference_number of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :type: str
        """
        if reference_number is None:
            raise ValueError("Invalid value for `reference_number`, must not be `None`")  # noqa: E501
        if reference_number is not None and len(reference_number) > 8:
            raise ValueError("Invalid value for `reference_number`, length must be less than or equal to `8`")  # noqa: E501
        if reference_number is not None and not re.search(r'^(?!\s*$).+', reference_number):  # noqa: E501
            raise ValueError(r"Invalid value for `reference_number`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._reference_number = reference_number

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
        if not isinstance(other, PaymentCardForcedTicketTransactionAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
