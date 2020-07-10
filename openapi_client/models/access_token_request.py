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


class AccessTokenRequest(object):
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
        'domain': 'str',
        'token': 'str',
        'public_key_required': 'bool'
    }

    attribute_map = {
        'domain': 'domain',
        'token': 'token',
        'public_key_required': 'publicKeyRequired'
    }

    def __init__(self, domain=None, token=None, public_key_required=None, local_vars_configuration=None):  # noqa: E501
        """AccessTokenRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._domain = None
        self._token = None
        self._public_key_required = None
        self.discriminator = None

        self.domain = domain
        self.token = token
        self.public_key_required = public_key_required

    @property
    def domain(self):
        """Gets the domain of this AccessTokenRequest.  # noqa: E501

        Domain name.  # noqa: E501

        :return: The domain of this AccessTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AccessTokenRequest.

        Domain name.  # noqa: E501

        :param domain: The domain of this AccessTokenRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain is None:  # noqa: E501
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def token(self):
        """Gets the token of this AccessTokenRequest.  # noqa: E501

        The token value.  # noqa: E501

        :return: The token of this AccessTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AccessTokenRequest.

        The token value.  # noqa: E501

        :param token: The token of this AccessTokenRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def public_key_required(self):
        """Gets the public_key_required of this AccessTokenRequest.  # noqa: E501

        Indicates whether public key is requested or not.  # noqa: E501

        :return: The public_key_required of this AccessTokenRequest.  # noqa: E501
        :rtype: bool
        """
        return self._public_key_required

    @public_key_required.setter
    def public_key_required(self, public_key_required):
        """Sets the public_key_required of this AccessTokenRequest.

        Indicates whether public key is requested or not.  # noqa: E501

        :param public_key_required: The public_key_required of this AccessTokenRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and public_key_required is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key_required`, must not be `None`")  # noqa: E501

        self._public_key_required = public_key_required

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
        if not isinstance(other, AccessTokenRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessTokenRequest):
            return True

        return self.to_dict() != other.to_dict()
