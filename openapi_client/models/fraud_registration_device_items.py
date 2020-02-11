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


class FraudRegistrationDeviceItems(object):
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
        'network_type': 'str',
        'ip': 'str',
        'mac': 'str',
        'ssid': 'str',
        'bssid': 'str',
        'user_defined': 'object'
    }

    attribute_map = {
        'network_type': 'networkType',
        'ip': 'ip',
        'mac': 'mac',
        'ssid': 'ssid',
        'bssid': 'bssid',
        'user_defined': 'userDefined'
    }

    def __init__(self, network_type=None, ip=None, mac=None, ssid=None, bssid=None, user_defined=None):  # noqa: E501
        """FraudRegistrationDeviceItems - a model defined in OpenAPI"""  # noqa: E501

        self._network_type = None
        self._ip = None
        self._mac = None
        self._ssid = None
        self._bssid = None
        self._user_defined = None
        self.discriminator = None

        self.network_type = network_type
        if ip is not None:
            self.ip = ip
        if mac is not None:
            self.mac = mac
        if ssid is not None:
            self.ssid = ssid
        if bssid is not None:
            self.bssid = bssid
        if user_defined is not None:
            self.user_defined = user_defined

    @property
    def network_type(self):
        """Gets the network_type of this FraudRegistrationDeviceItems.  # noqa: E501

        Defines the type of network associated with the device.  # noqa: E501

        :return: The network_type of this FraudRegistrationDeviceItems.  # noqa: E501
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this FraudRegistrationDeviceItems.

        Defines the type of network associated with the device.  # noqa: E501

        :param network_type: The network_type of this FraudRegistrationDeviceItems.  # noqa: E501
        :type: str
        """
        if network_type is None:
            raise ValueError("Invalid value for `network_type`, must not be `None`")  # noqa: E501
        allowed_values = ["network/mobile", "network/wifi"]  # noqa: E501
        if network_type not in allowed_values:
            raise ValueError(
                "Invalid value for `network_type` ({0}), must be one of {1}"  # noqa: E501
                .format(network_type, allowed_values)
            )

        self._network_type = network_type

    @property
    def ip(self):
        """Gets the ip of this FraudRegistrationDeviceItems.  # noqa: E501

        The IPv4 or IPv6 address of the device if the network assigned one.  # noqa: E501

        :return: The ip of this FraudRegistrationDeviceItems.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this FraudRegistrationDeviceItems.

        The IPv4 or IPv6 address of the device if the network assigned one.  # noqa: E501

        :param ip: The ip of this FraudRegistrationDeviceItems.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def mac(self):
        """Gets the mac of this FraudRegistrationDeviceItems.  # noqa: E501

        The MAC address of the device that is connected to the Wi-Fi network.  # noqa: E501

        :return: The mac of this FraudRegistrationDeviceItems.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this FraudRegistrationDeviceItems.

        The MAC address of the device that is connected to the Wi-Fi network.  # noqa: E501

        :param mac: The mac of this FraudRegistrationDeviceItems.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def ssid(self):
        """Gets the ssid of this FraudRegistrationDeviceItems.  # noqa: E501

        The Wi-Fi networks Service Set Identifier (SSID).  # noqa: E501

        :return: The ssid of this FraudRegistrationDeviceItems.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this FraudRegistrationDeviceItems.

        The Wi-Fi networks Service Set Identifier (SSID).  # noqa: E501

        :param ssid: The ssid of this FraudRegistrationDeviceItems.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    @property
    def bssid(self):
        """Gets the bssid of this FraudRegistrationDeviceItems.  # noqa: E501

        The Wi-Fi networks Basic Service Set Identifier (BSSID).  # noqa: E501

        :return: The bssid of this FraudRegistrationDeviceItems.  # noqa: E501
        :rtype: str
        """
        return self._bssid

    @bssid.setter
    def bssid(self, bssid):
        """Sets the bssid of this FraudRegistrationDeviceItems.

        The Wi-Fi networks Basic Service Set Identifier (BSSID).  # noqa: E501

        :param bssid: The bssid of this FraudRegistrationDeviceItems.  # noqa: E501
        :type: str
        """

        self._bssid = bssid

    @property
    def user_defined(self):
        """Gets the user_defined of this FraudRegistrationDeviceItems.  # noqa: E501

        A JSON object that can carry any additional information about the network that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this FraudRegistrationDeviceItems.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this FraudRegistrationDeviceItems.

        A JSON object that can carry any additional information about the network that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this FraudRegistrationDeviceItems.  # noqa: E501
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
        if not isinstance(other, FraudRegistrationDeviceItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
