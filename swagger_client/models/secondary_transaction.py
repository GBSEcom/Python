# coding: utf-8

"""
    Payment Gateway API Specification

    Payment Gateway API for payment processing.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.amount import Amount  # noqa: F401,E501
from swagger_client.models.split_shipment import SplitShipment  # noqa: F401,E501


class SecondaryTransaction(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'amount': 'Amount',
        'split_shipment': 'SplitShipment'
    }

    attribute_map = {
        'amount': 'amount',
        'split_shipment': 'splitShipment'
    }

    def __init__(self, amount=None, split_shipment=None):  # noqa: E501
        """SecondaryTransaction - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._split_shipment = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if split_shipment is not None:
            self.split_shipment = split_shipment

    @property
    def amount(self):
        """Gets the amount of this SecondaryTransaction.  # noqa: E501


        :return: The amount of this SecondaryTransaction.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SecondaryTransaction.


        :param amount: The amount of this SecondaryTransaction.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def split_shipment(self):
        """Gets the split_shipment of this SecondaryTransaction.  # noqa: E501


        :return: The split_shipment of this SecondaryTransaction.  # noqa: E501
        :rtype: SplitShipment
        """
        return self._split_shipment

    @split_shipment.setter
    def split_shipment(self, split_shipment):
        """Sets the split_shipment of this SecondaryTransaction.


        :param split_shipment: The split_shipment of this SecondaryTransaction.  # noqa: E501
        :type: SplitShipment
        """

        self._split_shipment = split_shipment

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, SecondaryTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other