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


class LockoutTime(object):
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
        'auto_lockout_time': 'int',
        'duplicate_lockout_time': 'int'
    }

    attribute_map = {
        'auto_lockout_time': 'autoLockoutTime',
        'duplicate_lockout_time': 'duplicateLockoutTime'
    }

    def __init__(self, auto_lockout_time=None, duplicate_lockout_time=None):  # noqa: E501
        """LockoutTime - a model defined in OpenAPI"""  # noqa: E501

        self._auto_lockout_time = None
        self._duplicate_lockout_time = None
        self.discriminator = None

        if auto_lockout_time is not None:
            self.auto_lockout_time = auto_lockout_time
        if duplicate_lockout_time is not None:
            self.duplicate_lockout_time = duplicate_lockout_time

    @property
    def auto_lockout_time(self):
        """Gets the auto_lockout_time of this LockoutTime.  # noqa: E501

        Auto-lockout time.  # noqa: E501

        :return: The auto_lockout_time of this LockoutTime.  # noqa: E501
        :rtype: int
        """
        return self._auto_lockout_time

    @auto_lockout_time.setter
    def auto_lockout_time(self, auto_lockout_time):
        """Sets the auto_lockout_time of this LockoutTime.

        Auto-lockout time.  # noqa: E501

        :param auto_lockout_time: The auto_lockout_time of this LockoutTime.  # noqa: E501
        :type: int
        """

        self._auto_lockout_time = auto_lockout_time

    @property
    def duplicate_lockout_time(self):
        """Gets the duplicate_lockout_time of this LockoutTime.  # noqa: E501

        Duplicate lockout time.  # noqa: E501

        :return: The duplicate_lockout_time of this LockoutTime.  # noqa: E501
        :rtype: int
        """
        return self._duplicate_lockout_time

    @duplicate_lockout_time.setter
    def duplicate_lockout_time(self, duplicate_lockout_time):
        """Sets the duplicate_lockout_time of this LockoutTime.

        Duplicate lockout time.  # noqa: E501

        :param duplicate_lockout_time: The duplicate_lockout_time of this LockoutTime.  # noqa: E501
        :type: int
        """

        self._duplicate_lockout_time = duplicate_lockout_time

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
        if not isinstance(other, LockoutTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
