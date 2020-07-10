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


class Secure3DAuthenticationResponse(object):
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
        'type': 'str',
        'version': 'str',
        'params': 'Secure3DAuthenticationResponseParams',
        'secure3d_method': 'Secure3DAuthenticationResponseSecure3dMethod'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'params': 'params',
        'secure3d_method': 'secure3dMethod'
    }

    def __init__(self, type=None, version=None, params=None, secure3d_method=None, local_vars_configuration=None):  # noqa: E501
        """Secure3DAuthenticationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._version = None
        self._params = None
        self._secure3d_method = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if params is not None:
            self.params = params
        if secure3d_method is not None:
            self.secure3d_method = secure3d_method

    @property
    def type(self):
        """Gets the type of this Secure3DAuthenticationResponse.  # noqa: E501

        The type of authentication.  # noqa: E501

        :return: The type of this Secure3DAuthenticationResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Secure3DAuthenticationResponse.

        The type of authentication.  # noqa: E501

        :param type: The type of this Secure3DAuthenticationResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["3D_SECURE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def version(self):
        """Gets the version of this Secure3DAuthenticationResponse.  # noqa: E501

        The version of 3DS used to authenticate.  # noqa: E501

        :return: The version of this Secure3DAuthenticationResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Secure3DAuthenticationResponse.

        The version of 3DS used to authenticate.  # noqa: E501

        :param version: The version of this Secure3DAuthenticationResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["1.0", "2.1", "2.2"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and version not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `version` ({0}), must be one of {1}"  # noqa: E501
                .format(version, allowed_values)
            )

        self._version = version

    @property
    def params(self):
        """Gets the params of this Secure3DAuthenticationResponse.  # noqa: E501


        :return: The params of this Secure3DAuthenticationResponse.  # noqa: E501
        :rtype: Secure3DAuthenticationResponseParams
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this Secure3DAuthenticationResponse.


        :param params: The params of this Secure3DAuthenticationResponse.  # noqa: E501
        :type: Secure3DAuthenticationResponseParams
        """

        self._params = params

    @property
    def secure3d_method(self):
        """Gets the secure3d_method of this Secure3DAuthenticationResponse.  # noqa: E501


        :return: The secure3d_method of this Secure3DAuthenticationResponse.  # noqa: E501
        :rtype: Secure3DAuthenticationResponseSecure3dMethod
        """
        return self._secure3d_method

    @secure3d_method.setter
    def secure3d_method(self, secure3d_method):
        """Sets the secure3d_method of this Secure3DAuthenticationResponse.


        :param secure3d_method: The secure3d_method of this Secure3DAuthenticationResponse.  # noqa: E501
        :type: Secure3DAuthenticationResponseSecure3dMethod
        """

        self._secure3d_method = secure3d_method

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
        if not isinstance(other, Secure3DAuthenticationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Secure3DAuthenticationResponse):
            return True

        return self.to_dict() != other.to_dict()
