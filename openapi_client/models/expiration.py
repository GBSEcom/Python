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


class Expiration(object):
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
        'month': 'str',
        'year': 'str'
    }

    attribute_map = {
        'month': 'month',
        'year': 'year'
    }

    def __init__(self, month=None, year=None, local_vars_configuration=None):  # noqa: E501
        """Expiration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._month = None
        self._year = None
        self.discriminator = None

        self.month = month
        self.year = year

    @property
    def month(self):
        """Gets the month of this Expiration.  # noqa: E501

        Month of the card expiration date in MM format.  # noqa: E501

        :return: The month of this Expiration.  # noqa: E501
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this Expiration.

        Month of the card expiration date in MM format.  # noqa: E501

        :param month: The month of this Expiration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and month is None:  # noqa: E501
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                month is not None and not re.search(r'^(0[1-9]|1[012])$', month)):  # noqa: E501
            raise ValueError(r"Invalid value for `month`, must be a follow pattern or equal to `/^(0[1-9]|1[012])$/`")  # noqa: E501

        self._month = month

    @property
    def year(self):
        """Gets the year of this Expiration.  # noqa: E501

        Year of the card expiration date in YY format.  # noqa: E501

        :return: The year of this Expiration.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Expiration.

        Year of the card expiration date in YY format.  # noqa: E501

        :param year: The year of this Expiration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and year is None:  # noqa: E501
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                year is not None and not re.search(r'^([0-9]{2,4})$', year)):  # noqa: E501
            raise ValueError(r"Invalid value for `year`, must be a follow pattern or equal to `/^([0-9]{2,4})$/`")  # noqa: E501

        self._year = year

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
        if not isinstance(other, Expiration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Expiration):
            return True

        return self.to_dict() != other.to_dict()
