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


class Secure3D10AuthenticationResultAllOf(object):
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
        'verification_response': 'str',
        'authentication_attempt_result': 'str',
        'cavv': 'str',
        'xid': 'str'
    }

    attribute_map = {
        'verification_response': 'verificationResponse',
        'authentication_attempt_result': 'authenticationAttemptResult',
        'cavv': 'cavv',
        'xid': 'xid'
    }

    def __init__(self, verification_response=None, authentication_attempt_result=None, cavv=None, xid=None, local_vars_configuration=None):  # noqa: E501
        """Secure3D10AuthenticationResultAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._verification_response = None
        self._authentication_attempt_result = None
        self._cavv = None
        self._xid = None
        self.discriminator = None

        if verification_response is not None:
            self.verification_response = verification_response
        if authentication_attempt_result is not None:
            self.authentication_attempt_result = authentication_attempt_result
        if cavv is not None:
            self.cavv = cavv
        if xid is not None:
            self.xid = xid

    @property
    def verification_response(self):
        """Gets the verification_response of this Secure3D10AuthenticationResultAllOf.  # noqa: E501

        Card enrollment result from the Verification Response (VeRes).  # noqa: E501

        :return: The verification_response of this Secure3D10AuthenticationResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._verification_response

    @verification_response.setter
    def verification_response(self, verification_response):
        """Sets the verification_response of this Secure3D10AuthenticationResultAllOf.

        Card enrollment result from the Verification Response (VeRes).  # noqa: E501

        :param verification_response: The verification_response of this Secure3D10AuthenticationResultAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and verification_response not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `verification_response` ({0}), must be one of {1}"  # noqa: E501
                .format(verification_response, allowed_values)
            )

        self._verification_response = verification_response

    @property
    def authentication_attempt_result(self):
        """Gets the authentication_attempt_result of this Secure3D10AuthenticationResultAllOf.  # noqa: E501

        Result of authentication attempt from Payer Authentication Response (PaRes).  # noqa: E501

        :return: The authentication_attempt_result of this Secure3D10AuthenticationResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._authentication_attempt_result

    @authentication_attempt_result.setter
    def authentication_attempt_result(self, authentication_attempt_result):
        """Sets the authentication_attempt_result of this Secure3D10AuthenticationResultAllOf.

        Result of authentication attempt from Payer Authentication Response (PaRes).  # noqa: E501

        :param authentication_attempt_result: The authentication_attempt_result of this Secure3D10AuthenticationResultAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N", "U", "A"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and authentication_attempt_result not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `authentication_attempt_result` ({0}), must be one of {1}"  # noqa: E501
                .format(authentication_attempt_result, allowed_values)
            )

        self._authentication_attempt_result = authentication_attempt_result

    @property
    def cavv(self):
        """Gets the cavv of this Secure3D10AuthenticationResultAllOf.  # noqa: E501

        The Cardholder Authentication Verification Value (CAVV) is a cryptographic value derived by the issuer during payment authentication that can provide evidence of the results of payment authentication during an online purchase.  # noqa: E501

        :return: The cavv of this Secure3D10AuthenticationResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._cavv

    @cavv.setter
    def cavv(self, cavv):
        """Sets the cavv of this Secure3D10AuthenticationResultAllOf.

        The Cardholder Authentication Verification Value (CAVV) is a cryptographic value derived by the issuer during payment authentication that can provide evidence of the results of payment authentication during an online purchase.  # noqa: E501

        :param cavv: The cavv of this Secure3D10AuthenticationResultAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cavv is not None and len(cavv) > 32):
            raise ValueError("Invalid value for `cavv`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cavv is not None and len(cavv) < 20):
            raise ValueError("Invalid value for `cavv`, length must be greater than or equal to `20`")  # noqa: E501

        self._cavv = cavv

    @property
    def xid(self):
        """Gets the xid of this Secure3D10AuthenticationResultAllOf.  # noqa: E501

        The transaction identifier (XID) is a unique tracking number set by the merchant.  # noqa: E501

        :return: The xid of this Secure3D10AuthenticationResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._xid

    @xid.setter
    def xid(self, xid):
        """Sets the xid of this Secure3D10AuthenticationResultAllOf.

        The transaction identifier (XID) is a unique tracking number set by the merchant.  # noqa: E501

        :param xid: The xid of this Secure3D10AuthenticationResultAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                xid is not None and len(xid) > 32):
            raise ValueError("Invalid value for `xid`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                xid is not None and len(xid) < 20):
            raise ValueError("Invalid value for `xid`, length must be greater than or equal to `20`")  # noqa: E501

        self._xid = xid

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
        if not isinstance(other, Secure3D10AuthenticationResultAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Secure3D10AuthenticationResultAllOf):
            return True

        return self.to_dict() != other.to_dict()
