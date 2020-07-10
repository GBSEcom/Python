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


class Button(object):
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
        'primary': 'Primary',
        'hover': 'Hover'
    }

    attribute_map = {
        'primary': 'primary',
        'hover': 'hover'
    }

    def __init__(self, primary=None, hover=None, local_vars_configuration=None):  # noqa: E501
        """Button - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._primary = None
        self._hover = None
        self.discriminator = None

        if primary is not None:
            self.primary = primary
        if hover is not None:
            self.hover = hover

    @property
    def primary(self):
        """Gets the primary of this Button.  # noqa: E501


        :return: The primary of this Button.  # noqa: E501
        :rtype: Primary
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this Button.


        :param primary: The primary of this Button.  # noqa: E501
        :type: Primary
        """

        self._primary = primary

    @property
    def hover(self):
        """Gets the hover of this Button.  # noqa: E501


        :return: The hover of this Button.  # noqa: E501
        :rtype: Hover
        """
        return self._hover

    @hover.setter
    def hover(self, hover):
        """Sets the hover of this Button.


        :param hover: The hover of this Button.  # noqa: E501
        :type: Hover
        """

        self._hover = hover

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
        if not isinstance(other, Button):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Button):
            return True

        return self.to_dict() != other.to_dict()
