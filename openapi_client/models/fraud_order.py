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


class FraudOrder(object):
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
        'ship_to_address': 'ShipToAddress',
        'items': 'list[FraudOrderItems]',
        'user_defined': 'object'
    }

    attribute_map = {
        'ship_to_address': 'shipToAddress',
        'items': 'items',
        'user_defined': 'userDefined'
    }

    def __init__(self, ship_to_address=None, items=None, user_defined=None):  # noqa: E501
        """FraudOrder - a model defined in OpenAPI"""  # noqa: E501

        self._ship_to_address = None
        self._items = None
        self._user_defined = None
        self.discriminator = None

        if ship_to_address is not None:
            self.ship_to_address = ship_to_address
        if items is not None:
            self.items = items
        if user_defined is not None:
            self.user_defined = user_defined

    @property
    def ship_to_address(self):
        """Gets the ship_to_address of this FraudOrder.  # noqa: E501


        :return: The ship_to_address of this FraudOrder.  # noqa: E501
        :rtype: ShipToAddress
        """
        return self._ship_to_address

    @ship_to_address.setter
    def ship_to_address(self, ship_to_address):
        """Sets the ship_to_address of this FraudOrder.


        :param ship_to_address: The ship_to_address of this FraudOrder.  # noqa: E501
        :type: ShipToAddress
        """

        self._ship_to_address = ship_to_address

    @property
    def items(self):
        """Gets the items of this FraudOrder.  # noqa: E501

        The list of items included in the order.  # noqa: E501

        :return: The items of this FraudOrder.  # noqa: E501
        :rtype: list[FraudOrderItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this FraudOrder.

        The list of items included in the order.  # noqa: E501

        :param items: The items of this FraudOrder.  # noqa: E501
        :type: list[FraudOrderItems]
        """

        self._items = items

    @property
    def user_defined(self):
        """Gets the user_defined of this FraudOrder.  # noqa: E501

        A JSON object that can carry any additional information about the order that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this FraudOrder.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this FraudOrder.

        A JSON object that can carry any additional information about the order that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this FraudOrder.  # noqa: E501
        :type: object
        """

        self._user_defined = user_defined

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
        if not isinstance(other, FraudOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
