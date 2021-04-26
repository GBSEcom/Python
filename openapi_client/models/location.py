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


class Location(object):
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
        'location_id': 'str',
        'merchant_address': 'FraudAddress',
        'hierarchy': 'str',
        'timezone_offset': 'str',
        'user_defined': 'object'
    }

    attribute_map = {
        'location_id': 'locationId',
        'merchant_address': 'merchantAddress',
        'hierarchy': 'hierarchy',
        'timezone_offset': 'timezoneOffset',
        'user_defined': 'userDefined'
    }

    def __init__(self, location_id=None, merchant_address=None, hierarchy=None, timezone_offset=None, user_defined=None):  # noqa: E501
        """Location - a model defined in OpenAPI"""  # noqa: E501

        self._location_id = None
        self._merchant_address = None
        self._hierarchy = None
        self._timezone_offset = None
        self._user_defined = None
        self.discriminator = None

        if location_id is not None:
            self.location_id = location_id
        if merchant_address is not None:
            self.merchant_address = merchant_address
        if hierarchy is not None:
            self.hierarchy = hierarchy
        if timezone_offset is not None:
            self.timezone_offset = timezone_offset
        if user_defined is not None:
            self.user_defined = user_defined

    @property
    def location_id(self):
        """Gets the location_id of this Location.  # noqa: E501

        The unique ID of this location.  # noqa: E501

        :return: The location_id of this Location.  # noqa: E501
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this Location.

        The unique ID of this location.  # noqa: E501

        :param location_id: The location_id of this Location.  # noqa: E501
        :type: str
        """

        self._location_id = location_id

    @property
    def merchant_address(self):
        """Gets the merchant_address of this Location.  # noqa: E501


        :return: The merchant_address of this Location.  # noqa: E501
        :rtype: FraudAddress
        """
        return self._merchant_address

    @merchant_address.setter
    def merchant_address(self, merchant_address):
        """Sets the merchant_address of this Location.


        :param merchant_address: The merchant_address of this Location.  # noqa: E501
        :type: FraudAddress
        """

        self._merchant_address = merchant_address

    @property
    def hierarchy(self):
        """Gets the hierarchy of this Location.  # noqa: E501

        Free-text field to describe a hierarchy the merchant would like to provide.  # noqa: E501

        :return: The hierarchy of this Location.  # noqa: E501
        :rtype: str
        """
        return self._hierarchy

    @hierarchy.setter
    def hierarchy(self, hierarchy):
        """Sets the hierarchy of this Location.

        Free-text field to describe a hierarchy the merchant would like to provide.  # noqa: E501

        :param hierarchy: The hierarchy of this Location.  # noqa: E501
        :type: str
        """

        self._hierarchy = hierarchy

    @property
    def timezone_offset(self):
        """Gets the timezone_offset of this Location.  # noqa: E501

        The timezone offset from UTC to the merchants timezone configuration, specified in the format +hh:mm.  # noqa: E501

        :return: The timezone_offset of this Location.  # noqa: E501
        :rtype: str
        """
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, timezone_offset):
        """Sets the timezone_offset of this Location.

        The timezone offset from UTC to the merchants timezone configuration, specified in the format +hh:mm.  # noqa: E501

        :param timezone_offset: The timezone_offset of this Location.  # noqa: E501
        :type: str
        """

        self._timezone_offset = timezone_offset

    @property
    def user_defined(self):
        """Gets the user_defined of this Location.  # noqa: E501

        A JSON object that can carry any additional information about the location that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this Location.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this Location.

        A JSON object that can carry any additional information about the location that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this Location.  # noqa: E501
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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
