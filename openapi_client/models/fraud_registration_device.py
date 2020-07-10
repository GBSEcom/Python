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


class FraudRegistrationDevice(object):
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
        'device_type': 'str',
        'device_id': 'str',
        'networks': 'list[FraudRegistrationDeviceItems]',
        'latitude': 'float',
        'longitude': 'float',
        'imei': 'str',
        'model': 'str',
        'manufacturer': 'str',
        'timezone_offset': 'str',
        'rooted': 'bool',
        'malware_detected': 'bool',
        'user_defined': 'object'
    }

    attribute_map = {
        'device_type': 'deviceType',
        'device_id': 'deviceId',
        'networks': 'networks',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'imei': 'imei',
        'model': 'model',
        'manufacturer': 'manufacturer',
        'timezone_offset': 'timezoneOffset',
        'rooted': 'rooted',
        'malware_detected': 'malwareDetected',
        'user_defined': 'userDefined'
    }

    def __init__(self, device_type=None, device_id=None, networks=None, latitude=None, longitude=None, imei=None, model=None, manufacturer=None, timezone_offset=None, rooted=None, malware_detected=None, user_defined=None, local_vars_configuration=None):  # noqa: E501
        """FraudRegistrationDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_type = None
        self._device_id = None
        self._networks = None
        self._latitude = None
        self._longitude = None
        self._imei = None
        self._model = None
        self._manufacturer = None
        self._timezone_offset = None
        self._rooted = None
        self._malware_detected = None
        self._user_defined = None
        self.discriminator = None

        self.device_type = device_type
        self.device_id = device_id
        if networks is not None:
            self.networks = networks
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if imei is not None:
            self.imei = imei
        if model is not None:
            self.model = model
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if timezone_offset is not None:
            self.timezone_offset = timezone_offset
        if rooted is not None:
            self.rooted = rooted
        if malware_detected is not None:
            self.malware_detected = malware_detected
        if user_defined is not None:
            self.user_defined = user_defined

    @property
    def device_type(self):
        """Gets the device_type of this FraudRegistrationDevice.  # noqa: E501

        Defines the type of this object.  # noqa: E501

        :return: The device_type of this FraudRegistrationDevice.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this FraudRegistrationDevice.

        Defines the type of this object.  # noqa: E501

        :param device_type: The device_type of this FraudRegistrationDevice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_type is None:  # noqa: E501
            raise ValueError("Invalid value for `device_type`, must not be `None`")  # noqa: E501
        allowed_values = ["device/pos", "device/mobile"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and device_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def device_id(self):
        """Gets the device_id of this FraudRegistrationDevice.  # noqa: E501

        The unique ID of the device. Must be unique for the entire system (not just within a specific merchant or industry).  # noqa: E501

        :return: The device_id of this FraudRegistrationDevice.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this FraudRegistrationDevice.

        The unique ID of the device. Must be unique for the entire system (not just within a specific merchant or industry).  # noqa: E501

        :param device_id: The device_id of this FraudRegistrationDevice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                device_id is not None and not re.search(r'^(?!\s*$).+', device_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `device_id`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._device_id = device_id

    @property
    def networks(self):
        """Gets the networks of this FraudRegistrationDevice.  # noqa: E501

        Information about the networks associated with the device.  # noqa: E501

        :return: The networks of this FraudRegistrationDevice.  # noqa: E501
        :rtype: list[FraudRegistrationDeviceItems]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this FraudRegistrationDevice.

        Information about the networks associated with the device.  # noqa: E501

        :param networks: The networks of this FraudRegistrationDevice.  # noqa: E501
        :type: list[FraudRegistrationDeviceItems]
        """

        self._networks = networks

    @property
    def latitude(self):
        """Gets the latitude of this FraudRegistrationDevice.  # noqa: E501

        The GPS decimal latitude, ranging from (-90.0 to 90.0) where positive numbers indicate locations North of the equator.  # noqa: E501

        :return: The latitude of this FraudRegistrationDevice.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this FraudRegistrationDevice.

        The GPS decimal latitude, ranging from (-90.0 to 90.0) where positive numbers indicate locations North of the equator.  # noqa: E501

        :param latitude: The latitude of this FraudRegistrationDevice.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this FraudRegistrationDevice.  # noqa: E501

        The GPS decimal longitude, ranging from (-180.0 to 180.0) where positive numbers indicate locations East of the IERS Reference Meridian.  # noqa: E501

        :return: The longitude of this FraudRegistrationDevice.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this FraudRegistrationDevice.

        The GPS decimal longitude, ranging from (-180.0 to 180.0) where positive numbers indicate locations East of the IERS Reference Meridian.  # noqa: E501

        :param longitude: The longitude of this FraudRegistrationDevice.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def imei(self):
        """Gets the imei of this FraudRegistrationDevice.  # noqa: E501

        The device's International Mobile Equipment Identity (IMEI) as described in IETF RFC7254.  # noqa: E501

        :return: The imei of this FraudRegistrationDevice.  # noqa: E501
        :rtype: str
        """
        return self._imei

    @imei.setter
    def imei(self, imei):
        """Sets the imei of this FraudRegistrationDevice.

        The device's International Mobile Equipment Identity (IMEI) as described in IETF RFC7254.  # noqa: E501

        :param imei: The imei of this FraudRegistrationDevice.  # noqa: E501
        :type: str
        """

        self._imei = imei

    @property
    def model(self):
        """Gets the model of this FraudRegistrationDevice.  # noqa: E501

        The device's model name.  # noqa: E501

        :return: The model of this FraudRegistrationDevice.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this FraudRegistrationDevice.

        The device's model name.  # noqa: E501

        :param model: The model of this FraudRegistrationDevice.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def manufacturer(self):
        """Gets the manufacturer of this FraudRegistrationDevice.  # noqa: E501

        The device's manufacturer.  # noqa: E501

        :return: The manufacturer of this FraudRegistrationDevice.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this FraudRegistrationDevice.

        The device's manufacturer.  # noqa: E501

        :param manufacturer: The manufacturer of this FraudRegistrationDevice.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def timezone_offset(self):
        """Gets the timezone_offset of this FraudRegistrationDevice.  # noqa: E501

        The timezone offset from UTC to the devices timezone configuration, specified in the format +hh:mm.  # noqa: E501

        :return: The timezone_offset of this FraudRegistrationDevice.  # noqa: E501
        :rtype: str
        """
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, timezone_offset):
        """Sets the timezone_offset of this FraudRegistrationDevice.

        The timezone offset from UTC to the devices timezone configuration, specified in the format +hh:mm.  # noqa: E501

        :param timezone_offset: The timezone_offset of this FraudRegistrationDevice.  # noqa: E501
        :type: str
        """

        self._timezone_offset = timezone_offset

    @property
    def rooted(self):
        """Gets the rooted of this FraudRegistrationDevice.  # noqa: E501

        A flag indicating that the device has been altered to allow privileged access to users. This flag should only be set to false if a test was performed and the result was negative. Leave unset otherwise.  # noqa: E501

        :return: The rooted of this FraudRegistrationDevice.  # noqa: E501
        :rtype: bool
        """
        return self._rooted

    @rooted.setter
    def rooted(self, rooted):
        """Sets the rooted of this FraudRegistrationDevice.

        A flag indicating that the device has been altered to allow privileged access to users. This flag should only be set to false if a test was performed and the result was negative. Leave unset otherwise.  # noqa: E501

        :param rooted: The rooted of this FraudRegistrationDevice.  # noqa: E501
        :type: bool
        """

        self._rooted = rooted

    @property
    def malware_detected(self):
        """Gets the malware_detected of this FraudRegistrationDevice.  # noqa: E501

        A flag indicating that malware was detected on the mobile phone. This flag should only be set to false if a test was performed and the result was negative. Leave unset otherwise.  # noqa: E501

        :return: The malware_detected of this FraudRegistrationDevice.  # noqa: E501
        :rtype: bool
        """
        return self._malware_detected

    @malware_detected.setter
    def malware_detected(self, malware_detected):
        """Sets the malware_detected of this FraudRegistrationDevice.

        A flag indicating that malware was detected on the mobile phone. This flag should only be set to false if a test was performed and the result was negative. Leave unset otherwise.  # noqa: E501

        :param malware_detected: The malware_detected of this FraudRegistrationDevice.  # noqa: E501
        :type: bool
        """

        self._malware_detected = malware_detected

    @property
    def user_defined(self):
        """Gets the user_defined of this FraudRegistrationDevice.  # noqa: E501

        A JSON object that can carry any additional information about the device that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this FraudRegistrationDevice.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this FraudRegistrationDevice.

        A JSON object that can carry any additional information about the device that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this FraudRegistrationDevice.  # noqa: E501
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
        if not isinstance(other, FraudRegistrationDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FraudRegistrationDevice):
            return True

        return self.to_dict() != other.to_dict()
