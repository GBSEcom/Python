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


class Secure3D21AuthenticationRequestAllOf(object):
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
        'term_url': 'str',
        'method_notification_url': 'str',
        'challenge_indicator': 'str',
        'challenge_window_size': 'str'
    }

    attribute_map = {
        'term_url': 'termURL',
        'method_notification_url': 'methodNotificationURL',
        'challenge_indicator': 'challengeIndicator',
        'challenge_window_size': 'challengeWindowSize'
    }

    def __init__(self, term_url=None, method_notification_url=None, challenge_indicator='01', challenge_window_size=None, local_vars_configuration=None):  # noqa: E501
        """Secure3D21AuthenticationRequestAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._term_url = None
        self._method_notification_url = None
        self._challenge_indicator = None
        self._challenge_window_size = None
        self.discriminator = None

        if term_url is not None:
            self.term_url = term_url
        if method_notification_url is not None:
            self.method_notification_url = method_notification_url
        if challenge_indicator is not None:
            self.challenge_indicator = challenge_indicator
        if challenge_window_size is not None:
            self.challenge_window_size = challenge_window_size

    @property
    def term_url(self):
        """Gets the term_url of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501

        The result of the authentication will be sent to this URL. If not provided, a term URL will be dynamically generated.  # noqa: E501

        :return: The term_url of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._term_url

    @term_url.setter
    def term_url(self, term_url):
        """Sets the term_url of this Secure3D21AuthenticationRequestAllOf.

        The result of the authentication will be sent to this URL. If not provided, a term URL will be dynamically generated.  # noqa: E501

        :param term_url: The term_url of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501
        :type: str
        """

        self._term_url = term_url

    @property
    def method_notification_url(self):
        """Gets the method_notification_url of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501

        The 3DS method iframe and transaction ID will be sent here.  # noqa: E501

        :return: The method_notification_url of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._method_notification_url

    @method_notification_url.setter
    def method_notification_url(self, method_notification_url):
        """Sets the method_notification_url of this Secure3D21AuthenticationRequestAllOf.

        The 3DS method iframe and transaction ID will be sent here.  # noqa: E501

        :param method_notification_url: The method_notification_url of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501
        :type: str
        """

        self._method_notification_url = method_notification_url

    @property
    def challenge_indicator(self):
        """Gets the challenge_indicator of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501

        Indicates whether or not a challenge should be performed. 01 = No preference (You have no preference whether a challenge should be performed. This is the default value) 02 = No challenge requested (You prefer that no challenge should be performed) 03 = Challenge requested: 3DS Requestor Preference (You prefer that a challenge should be performed) 04 = Challenge requested: Mandate (There are local or regional mandates that mean that a challenge must be performed)   # noqa: E501

        :return: The challenge_indicator of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._challenge_indicator

    @challenge_indicator.setter
    def challenge_indicator(self, challenge_indicator):
        """Sets the challenge_indicator of this Secure3D21AuthenticationRequestAllOf.

        Indicates whether or not a challenge should be performed. 01 = No preference (You have no preference whether a challenge should be performed. This is the default value) 02 = No challenge requested (You prefer that no challenge should be performed) 03 = Challenge requested: 3DS Requestor Preference (You prefer that a challenge should be performed) 04 = Challenge requested: Mandate (There are local or regional mandates that mean that a challenge must be performed)   # noqa: E501

        :param challenge_indicator: The challenge_indicator of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["01", "02", "03", "04"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and challenge_indicator not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `challenge_indicator` ({0}), must be one of {1}"  # noqa: E501
                .format(challenge_indicator, allowed_values)
            )

        self._challenge_indicator = challenge_indicator

    @property
    def challenge_window_size(self):
        """Gets the challenge_window_size of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501

        Defines the size of the challenge window displayed to customers during authentication. 01 = 250 x 400 02 = 390 x 400 03 = 500 x 600 04 = 600 x 400 05 = Full screen   # noqa: E501

        :return: The challenge_window_size of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._challenge_window_size

    @challenge_window_size.setter
    def challenge_window_size(self, challenge_window_size):
        """Sets the challenge_window_size of this Secure3D21AuthenticationRequestAllOf.

        Defines the size of the challenge window displayed to customers during authentication. 01 = 250 x 400 02 = 390 x 400 03 = 500 x 600 04 = 600 x 400 05 = Full screen   # noqa: E501

        :param challenge_window_size: The challenge_window_size of this Secure3D21AuthenticationRequestAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["01", "02", "03", "04", "05"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and challenge_window_size not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `challenge_window_size` ({0}), must be one of {1}"  # noqa: E501
                .format(challenge_window_size, allowed_values)
            )

        self._challenge_window_size = challenge_window_size

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
        if not isinstance(other, Secure3D21AuthenticationRequestAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Secure3D21AuthenticationRequestAllOf):
            return True

        return self.to_dict() != other.to_dict()
