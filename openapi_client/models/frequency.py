# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.1.0.20210122.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Frequency(object):
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
        'every': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'every': 'every',
        'unit': 'unit'
    }

    def __init__(self, every=None, unit=None):  # noqa: E501
        """Frequency - a model defined in OpenAPI"""  # noqa: E501

        self._every = None
        self._unit = None
        self.discriminator = None

        self.every = every
        self.unit = unit

    @property
    def every(self):
        """Gets the every of this Frequency.  # noqa: E501

        Rate of frequency.  # noqa: E501

        :return: The every of this Frequency.  # noqa: E501
        :rtype: int
        """
        return self._every

    @every.setter
    def every(self, every):
        """Sets the every of this Frequency.

        Rate of frequency.  # noqa: E501

        :param every: The every of this Frequency.  # noqa: E501
        :type: int
        """
        if every is None:
            raise ValueError("Invalid value for `every`, must not be `None`")  # noqa: E501
        if every is not None and every > 1000:  # noqa: E501
            raise ValueError("Invalid value for `every`, must be a value less than or equal to `1000`")  # noqa: E501
        if every is not None and every < 1:  # noqa: E501
            raise ValueError("Invalid value for `every`, must be a value greater than or equal to `1`")  # noqa: E501

        self._every = every

    @property
    def unit(self):
        """Gets the unit of this Frequency.  # noqa: E501

        Unit which defines the frequency.  # noqa: E501

        :return: The unit of this Frequency.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Frequency.

        Unit which defines the frequency.  # noqa: E501

        :param unit: The unit of this Frequency.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501
        allowed_values = ["DAY", "WEEK", "MONTH", "YEAR"]  # noqa: E501
        if unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit

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
        if not isinstance(other, Frequency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
