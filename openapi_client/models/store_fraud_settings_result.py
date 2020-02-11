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


class StoreFraudSettingsResult(object):
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
        'blocked_card_identifier': 'TokenIdentifier',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'blocked_card_identifier': 'blockedCardIdentifier',
        'status': 'status'
    }

    def __init__(self, id=None, blocked_card_identifier=None, status=None):  # noqa: E501
        """StoreFraudSettingsResult - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._blocked_card_identifier = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if blocked_card_identifier is not None:
            self.blocked_card_identifier = blocked_card_identifier
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this StoreFraudSettingsResult.  # noqa: E501

        An outlet identificator.  # noqa: E501

        :return: The id of this StoreFraudSettingsResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoreFraudSettingsResult.

        An outlet identificator.  # noqa: E501

        :param id: The id of this StoreFraudSettingsResult.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def blocked_card_identifier(self):
        """Gets the blocked_card_identifier of this StoreFraudSettingsResult.  # noqa: E501


        :return: The blocked_card_identifier of this StoreFraudSettingsResult.  # noqa: E501
        :rtype: TokenIdentifier
        """
        return self._blocked_card_identifier

    @blocked_card_identifier.setter
    def blocked_card_identifier(self, blocked_card_identifier):
        """Sets the blocked_card_identifier of this StoreFraudSettingsResult.


        :param blocked_card_identifier: The blocked_card_identifier of this StoreFraudSettingsResult.  # noqa: E501
        :type: TokenIdentifier
        """

        self._blocked_card_identifier = blocked_card_identifier

    @property
    def status(self):
        """Gets the status of this StoreFraudSettingsResult.  # noqa: E501

        Status from fraud settings.  # noqa: E501

        :return: The status of this StoreFraudSettingsResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StoreFraudSettingsResult.

        Status from fraud settings.  # noqa: E501

        :param status: The status of this StoreFraudSettingsResult.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, StoreFraudSettingsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
