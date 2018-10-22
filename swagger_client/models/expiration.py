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


class Expiration(object):
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
        'month': 'str',
        'year': 'str'
    }

    attribute_map = {
        'month': 'month',
        'year': 'year'
    }

    def __init__(self, month=None, year=None):  # noqa: E501
        """Expiration - a model defined in Swagger"""  # noqa: E501

        self._month = None
        self._year = None
        self.discriminator = None

        self.month = month
        self.year = year

    @property
    def month(self):
        """Gets the month of this Expiration.  # noqa: E501


        :return: The month of this Expiration.  # noqa: E501
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this Expiration.


        :param month: The month of this Expiration.  # noqa: E501
        :type: str
        """
        if month is None:
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def year(self):
        """Gets the year of this Expiration.  # noqa: E501


        :return: The year of this Expiration.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Expiration.


        :param year: The year of this Expiration.  # noqa: E501
        :type: str
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

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
        if not isinstance(other, Expiration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other