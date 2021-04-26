# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.2.0.20210406.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FraudOrderItems(object):
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
        'id': 'str',
        'name': 'str',
        'quantity': 'str',
        'unit': 'str',
        'unit_price': 'str',
        'categories': 'list[list[str]]',
        'details_url': 'str',
        'user_defined': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'quantity': 'quantity',
        'unit': 'unit',
        'unit_price': 'unitPrice',
        'categories': 'categories',
        'details_url': 'detailsUrl',
        'user_defined': 'userDefined'
    }

    def __init__(self, id=None, name=None, quantity=None, unit=None, unit_price=None, categories=None, details_url=None, user_defined=None):  # noqa: E501
        """FraudOrderItems - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._quantity = None
        self._unit = None
        self._unit_price = None
        self._categories = None
        self._details_url = None
        self._user_defined = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if quantity is not None:
            self.quantity = quantity
        if unit is not None:
            self.unit = unit
        if unit_price is not None:
            self.unit_price = unit_price
        if categories is not None:
            self.categories = categories
        if details_url is not None:
            self.details_url = details_url
        if user_defined is not None:
            self.user_defined = user_defined

    @property
    def id(self):
        """Gets the id of this FraudOrderItems.  # noqa: E501

        A unique ID associated with the product. Must be unique within the merchant's system.  # noqa: E501

        :return: The id of this FraudOrderItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FraudOrderItems.

        A unique ID associated with the product. Must be unique within the merchant's system.  # noqa: E501

        :param id: The id of this FraudOrderItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FraudOrderItems.  # noqa: E501

        A name or short description of the product.  # noqa: E501

        :return: The name of this FraudOrderItems.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FraudOrderItems.

        A name or short description of the product.  # noqa: E501

        :param name: The name of this FraudOrderItems.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def quantity(self):
        """Gets the quantity of this FraudOrderItems.  # noqa: E501

        The unit in which the product is sold (e.g. litre, kilogram, etc). Leave empty if the product is sold as a complete unit.  # noqa: E501

        :return: The quantity of this FraudOrderItems.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this FraudOrderItems.

        The unit in which the product is sold (e.g. litre, kilogram, etc). Leave empty if the product is sold as a complete unit.  # noqa: E501

        :param quantity: The quantity of this FraudOrderItems.  # noqa: E501
        :type: str
        """

        self._quantity = quantity

    @property
    def unit(self):
        """Gets the unit of this FraudOrderItems.  # noqa: E501

        The number of units sold. Set to 1 if there is only one unit of the item. Leave empty if the quantity is unknown at the time of the request.  # noqa: E501

        :return: The unit of this FraudOrderItems.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this FraudOrderItems.

        The number of units sold. Set to 1 if there is only one unit of the item. Leave empty if the quantity is unknown at the time of the request.  # noqa: E501

        :param unit: The unit of this FraudOrderItems.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def unit_price(self):
        """Gets the unit_price of this FraudOrderItems.  # noqa: E501

        The price per unit.  # noqa: E501

        :return: The unit_price of this FraudOrderItems.  # noqa: E501
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this FraudOrderItems.

        The price per unit.  # noqa: E501

        :param unit_price: The unit_price of this FraudOrderItems.  # noqa: E501
        :type: str
        """

        self._unit_price = unit_price

    @property
    def categories(self):
        """Gets the categories of this FraudOrderItems.  # noqa: E501

        The categories that this product belongs to.  # noqa: E501

        :return: The categories of this FraudOrderItems.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this FraudOrderItems.

        The categories that this product belongs to.  # noqa: E501

        :param categories: The categories of this FraudOrderItems.  # noqa: E501
        :type: list[list[str]]
        """

        self._categories = categories

    @property
    def details_url(self):
        """Gets the details_url of this FraudOrderItems.  # noqa: E501

        The URL to the merchant's management system, for reporting and analysis.  # noqa: E501

        :return: The details_url of this FraudOrderItems.  # noqa: E501
        :rtype: str
        """
        return self._details_url

    @details_url.setter
    def details_url(self, details_url):
        """Sets the details_url of this FraudOrderItems.

        The URL to the merchant's management system, for reporting and analysis.  # noqa: E501

        :param details_url: The details_url of this FraudOrderItems.  # noqa: E501
        :type: str
        """

        self._details_url = details_url

    @property
    def user_defined(self):
        """Gets the user_defined of this FraudOrderItems.  # noqa: E501

        A JSON object that can carry any additional information about the order that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this FraudOrderItems.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this FraudOrderItems.

        A JSON object that can carry any additional information about the order that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this FraudOrderItems.  # noqa: E501
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
        if not isinstance(other, FraudOrderItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
