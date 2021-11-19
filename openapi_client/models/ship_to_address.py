# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.5.0.20211029.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ShipToAddress(object):
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
        'phone': 'str',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'country': 'str'
    }

    attribute_map = {
        'phone': 'phone',
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'country': 'country'
    }

    def __init__(self, phone=None, address1=None, address2=None, city=None, state=None, zip=None, country=None):  # noqa: E501
        """ShipToAddress - a model defined in OpenAPI"""  # noqa: E501

        self._phone = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._state = None
        self._zip = None
        self._country = None
        self.discriminator = None

        if phone is not None:
            self.phone = phone
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip
        if country is not None:
            self.country = country

    @property
    def phone(self):
        """Gets the phone of this ShipToAddress.  # noqa: E501

        Free-form phone number associated with the ship-to address.  # noqa: E501

        :return: The phone of this ShipToAddress.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ShipToAddress.

        Free-form phone number associated with the ship-to address.  # noqa: E501

        :param phone: The phone of this ShipToAddress.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def address1(self):
        """Gets the address1 of this ShipToAddress.  # noqa: E501

        First line of street address.  # noqa: E501

        :return: The address1 of this ShipToAddress.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this ShipToAddress.

        First line of street address.  # noqa: E501

        :param address1: The address1 of this ShipToAddress.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this ShipToAddress.  # noqa: E501

        Second line of street address.  # noqa: E501

        :return: The address2 of this ShipToAddress.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this ShipToAddress.

        Second line of street address.  # noqa: E501

        :param address2: The address2 of this ShipToAddress.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this ShipToAddress.  # noqa: E501

        City.  # noqa: E501

        :return: The city of this ShipToAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ShipToAddress.

        City.  # noqa: E501

        :param city: The city of this ShipToAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this ShipToAddress.  # noqa: E501

        State or province.  # noqa: E501

        :return: The state of this ShipToAddress.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShipToAddress.

        State or province.  # noqa: E501

        :param state: The state of this ShipToAddress.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this ShipToAddress.  # noqa: E501

        Postal Code, free form.  # noqa: E501

        :return: The zip of this ShipToAddress.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this ShipToAddress.

        Postal Code, free form.  # noqa: E501

        :param zip: The zip of this ShipToAddress.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def country(self):
        """Gets the country of this ShipToAddress.  # noqa: E501

        Country.  # noqa: E501

        :return: The country of this ShipToAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ShipToAddress.

        Country.  # noqa: E501

        :param country: The country of this ShipToAddress.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if not isinstance(other, ShipToAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
