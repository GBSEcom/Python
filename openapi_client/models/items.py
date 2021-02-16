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


class Items(object):
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
        'phone_number': 'str',
        'carrier_name': 'str',
        'mobile_country_code': 'str',
        'mobile_network_code': 'str',
        'subscription_identification_number': 'str',
        'location_area_code': 'str',
        'cell_id': 'str',
        'standard': 'str',
        'mac': 'str',
        'ssid': 'str',
        'bssid': 'str',
        'user_defined': 'object'
    }

    attribute_map = {
        'network_type': 'networkType',
        'ip': 'ip',
        'phone_number': 'phoneNumber',
        'carrier_name': 'carrierName',
        'mobile_country_code': 'mobileCountryCode',
        'mobile_network_code': 'mobileNetworkCode',
        'subscription_identification_number': 'subscriptionIdentificationNumber',
        'location_area_code': 'locationAreaCode',
        'cell_id': 'cellId',
        'standard': 'standard',
        'mac': 'mac',
        'ssid': 'ssid',
        'bssid': 'bssid',
        'user_defined': 'userDefined'
    }

    def __init__(self, network_type=None, ip=None, phone_number=None, carrier_name=None, mobile_country_code=None, mobile_network_code=None, subscription_identification_number=None, location_area_code=None, cell_id=None, standard=None, mac=None, ssid=None, bssid=None, user_defined=None):  # noqa: E501
        """Items - a model defined in OpenAPI"""  # noqa: E501

        self._network_type = None
        self._ip = None
        self._phone_number = None
        self._carrier_name = None
        self._mobile_country_code = None
        self._mobile_network_code = None
        self._subscription_identification_number = None
        self._location_area_code = None
        self._cell_id = None
        self._standard = None
        self._mac = None
        self._ssid = None
        self._bssid = None
        self._user_defined = None
        self.discriminator = None

        self.network_type = network_type
        if ip is not None:
            self.ip = ip
        if phone_number is not None:
            self.phone_number = phone_number
        if carrier_name is not None:
            self.carrier_name = carrier_name
        if mobile_country_code is not None:
            self.mobile_country_code = mobile_country_code
        if mobile_network_code is not None:
            self.mobile_network_code = mobile_network_code
        if subscription_identification_number is not None:
            self.subscription_identification_number = subscription_identification_number
        if location_area_code is not None:
            self.location_area_code = location_area_code
        if cell_id is not None:
            self.cell_id = cell_id
        if standard is not None:
            self.standard = standard
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
        """Gets the network_type of this Items.  # noqa: E501

        Defines the type of network associated with the device.  # noqa: E501

        :return: The network_type of this Items.  # noqa: E501
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this Items.

        Defines the type of network associated with the device.  # noqa: E501

        :param network_type: The network_type of this Items.  # noqa: E501
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
        """Gets the ip of this Items.  # noqa: E501

        The IPv4 or IPv6 address of the device if the network assigned one.  # noqa: E501

        :return: The ip of this Items.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Items.

        The IPv4 or IPv6 address of the device if the network assigned one.  # noqa: E501

        :param ip: The ip of this Items.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def phone_number(self):
        """Gets the phone_number of this Items.  # noqa: E501

        The devices primary phone number. This value should be supplied directly without any transformation (e.g. removal of spaces, hyphens or parentheses). If this data is available in segregated fields, it should be concatenated using a blank space (\" \") as a separator.  # noqa: E501

        :return: The phone_number of this Items.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Items.

        The devices primary phone number. This value should be supplied directly without any transformation (e.g. removal of spaces, hyphens or parentheses). If this data is available in segregated fields, it should be concatenated using a blank space (\" \") as a separator.  # noqa: E501

        :param phone_number: The phone_number of this Items.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def carrier_name(self):
        """Gets the carrier_name of this Items.  # noqa: E501

        The network carrier name.  # noqa: E501

        :return: The carrier_name of this Items.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this Items.

        The network carrier name.  # noqa: E501

        :param carrier_name: The carrier_name of this Items.  # noqa: E501
        :type: str
        """

        self._carrier_name = carrier_name

    @property
    def mobile_country_code(self):
        """Gets the mobile_country_code of this Items.  # noqa: E501

        The Mobile Country Code (MCC) as described in the ITUs E.212 specification.  # noqa: E501

        :return: The mobile_country_code of this Items.  # noqa: E501
        :rtype: str
        """
        return self._mobile_country_code

    @mobile_country_code.setter
    def mobile_country_code(self, mobile_country_code):
        """Sets the mobile_country_code of this Items.

        The Mobile Country Code (MCC) as described in the ITUs E.212 specification.  # noqa: E501

        :param mobile_country_code: The mobile_country_code of this Items.  # noqa: E501
        :type: str
        """

        self._mobile_country_code = mobile_country_code

    @property
    def mobile_network_code(self):
        """Gets the mobile_network_code of this Items.  # noqa: E501

        The Mobile Network Code (MNC) as described in the ITUs E.212 specification.  # noqa: E501

        :return: The mobile_network_code of this Items.  # noqa: E501
        :rtype: str
        """
        return self._mobile_network_code

    @mobile_network_code.setter
    def mobile_network_code(self, mobile_network_code):
        """Sets the mobile_network_code of this Items.

        The Mobile Network Code (MNC) as described in the ITUs E.212 specification.  # noqa: E501

        :param mobile_network_code: The mobile_network_code of this Items.  # noqa: E501
        :type: str
        """

        self._mobile_network_code = mobile_network_code

    @property
    def subscription_identification_number(self):
        """Gets the subscription_identification_number of this Items.  # noqa: E501

        The Mobile Subscription Identification Number code (MSIN) as described in the ITUs E.212 specification.  # noqa: E501

        :return: The subscription_identification_number of this Items.  # noqa: E501
        :rtype: str
        """
        return self._subscription_identification_number

    @subscription_identification_number.setter
    def subscription_identification_number(self, subscription_identification_number):
        """Sets the subscription_identification_number of this Items.

        The Mobile Subscription Identification Number code (MSIN) as described in the ITUs E.212 specification.  # noqa: E501

        :param subscription_identification_number: The subscription_identification_number of this Items.  # noqa: E501
        :type: str
        """

        self._subscription_identification_number = subscription_identification_number

    @property
    def location_area_code(self):
        """Gets the location_area_code of this Items.  # noqa: E501

        The Location Area Code (LAC) is a 16-bit identifier for a region that is covered by a set of network antennas.  # noqa: E501

        :return: The location_area_code of this Items.  # noqa: E501
        :rtype: str
        """
        return self._location_area_code

    @location_area_code.setter
    def location_area_code(self, location_area_code):
        """Sets the location_area_code of this Items.

        The Location Area Code (LAC) is a 16-bit identifier for a region that is covered by a set of network antennas.  # noqa: E501

        :param location_area_code: The location_area_code of this Items.  # noqa: E501
        :type: str
        """

        self._location_area_code = location_area_code

    @property
    def cell_id(self):
        """Gets the cell_id of this Items.  # noqa: E501

        The Cell ID (CID) is identifier for a specific Base Transceiver Station (BTS) within a specific Location Area Code (LAC).  # noqa: E501

        :return: The cell_id of this Items.  # noqa: E501
        :rtype: str
        """
        return self._cell_id

    @cell_id.setter
    def cell_id(self, cell_id):
        """Sets the cell_id of this Items.

        The Cell ID (CID) is identifier for a specific Base Transceiver Station (BTS) within a specific Location Area Code (LAC).  # noqa: E501

        :param cell_id: The cell_id of this Items.  # noqa: E501
        :type: str
        """

        self._cell_id = cell_id

    @property
    def standard(self):
        """Gets the standard of this Items.  # noqa: E501

        An identifier of the network standard used.  # noqa: E501

        :return: The standard of this Items.  # noqa: E501
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this Items.

        An identifier of the network standard used.  # noqa: E501

        :param standard: The standard of this Items.  # noqa: E501
        :type: str
        """

        self._standard = standard

    @property
    def mac(self):
        """Gets the mac of this Items.  # noqa: E501

        The MAC address of the device that is connected to the Wi-Fi network.  # noqa: E501

        :return: The mac of this Items.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this Items.

        The MAC address of the device that is connected to the Wi-Fi network.  # noqa: E501

        :param mac: The mac of this Items.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def ssid(self):
        """Gets the ssid of this Items.  # noqa: E501

        The Wi-Fi networks Service Set Identifier (SSID).  # noqa: E501

        :return: The ssid of this Items.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this Items.

        The Wi-Fi networks Service Set Identifier (SSID).  # noqa: E501

        :param ssid: The ssid of this Items.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    @property
    def bssid(self):
        """Gets the bssid of this Items.  # noqa: E501

        The Wi-Fi networks Basic Service Set Identifier (BSSID).  # noqa: E501

        :return: The bssid of this Items.  # noqa: E501
        :rtype: str
        """
        return self._bssid

    @bssid.setter
    def bssid(self, bssid):
        """Sets the bssid of this Items.

        The Wi-Fi networks Basic Service Set Identifier (BSSID).  # noqa: E501

        :param bssid: The bssid of this Items.  # noqa: E501
        :type: str
        """

        self._bssid = bssid

    @property
    def user_defined(self):
        """Gets the user_defined of this Items.  # noqa: E501

        A JSON object that can carry any additional information about the network that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this Items.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this Items.

        A JSON object that can carry any additional information about the network that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this Items.  # noqa: E501
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
        if not isinstance(other, Items):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
