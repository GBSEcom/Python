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


class CustomerAddress(object):
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
        'street': 'str',
        'street2': 'str',
        'state_province': 'str',
        'city': 'str',
        'country': 'str',
        'zip_postal_code': 'str',
        'phone': 'Phone'
    }

    attribute_map = {
        'street': 'street',
        'street2': 'street2',
        'state_province': 'stateProvince',
        'city': 'city',
        'country': 'country',
        'zip_postal_code': 'zipPostalCode',
        'phone': 'phone'
    }

    def __init__(self, street=None, street2=None, state_province=None, city=None, country=None, zip_postal_code=None, phone=None, local_vars_configuration=None):  # noqa: E501
        """CustomerAddress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._street = None
        self._street2 = None
        self._state_province = None
        self._city = None
        self._country = None
        self._zip_postal_code = None
        self._phone = None
        self.discriminator = None

        self.street = street
        if street2 is not None:
            self.street2 = street2
        if state_province is not None:
            self.state_province = state_province
        if city is not None:
            self.city = city
        self.country = country
        self.zip_postal_code = zip_postal_code
        if phone is not None:
            self.phone = phone

    @property
    def street(self):
        """Gets the street of this CustomerAddress.  # noqa: E501

        First line of street address.  # noqa: E501

        :return: The street of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this CustomerAddress.

        First line of street address.  # noqa: E501

        :param street: The street of this CustomerAddress.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and street is None:  # noqa: E501
            raise ValueError("Invalid value for `street`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                street is not None and not re.search(r'^(?!\s*$).+', street)):  # noqa: E501
            raise ValueError(r"Invalid value for `street`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._street = street

    @property
    def street2(self):
        """Gets the street2 of this CustomerAddress.  # noqa: E501

        Second line of street address.  # noqa: E501

        :return: The street2 of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """Sets the street2 of this CustomerAddress.

        Second line of street address.  # noqa: E501

        :param street2: The street2 of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._street2 = street2

    @property
    def state_province(self):
        """Gets the state_province of this CustomerAddress.  # noqa: E501

        State or province.  # noqa: E501

        :return: The state_province of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._state_province

    @state_province.setter
    def state_province(self, state_province):
        """Sets the state_province of this CustomerAddress.

        State or province.  # noqa: E501

        :param state_province: The state_province of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._state_province = state_province

    @property
    def city(self):
        """Gets the city of this CustomerAddress.  # noqa: E501

        City.  # noqa: E501

        :return: The city of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CustomerAddress.

        City.  # noqa: E501

        :param city: The city of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this CustomerAddress.  # noqa: E501

        Country.  # noqa: E501

        :return: The country of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CustomerAddress.

        Country.  # noqa: E501

        :param country: The country of this CustomerAddress.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                country is not None and not re.search(r'^(?!\s*$).+', country)):  # noqa: E501
            raise ValueError(r"Invalid value for `country`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._country = country

    @property
    def zip_postal_code(self):
        """Gets the zip_postal_code of this CustomerAddress.  # noqa: E501

        Postal code.  # noqa: E501

        :return: The zip_postal_code of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._zip_postal_code

    @zip_postal_code.setter
    def zip_postal_code(self, zip_postal_code):
        """Sets the zip_postal_code of this CustomerAddress.

        Postal code.  # noqa: E501

        :param zip_postal_code: The zip_postal_code of this CustomerAddress.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and zip_postal_code is None:  # noqa: E501
            raise ValueError("Invalid value for `zip_postal_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                zip_postal_code is not None and not re.search(r'^(?!\s*$).+', zip_postal_code)):  # noqa: E501
            raise ValueError(r"Invalid value for `zip_postal_code`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._zip_postal_code = zip_postal_code

    @property
    def phone(self):
        """Gets the phone of this CustomerAddress.  # noqa: E501


        :return: The phone of this CustomerAddress.  # noqa: E501
        :rtype: Phone
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CustomerAddress.


        :param phone: The phone of this CustomerAddress.  # noqa: E501
        :type: Phone
        """

        self._phone = phone

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
        if not isinstance(other, CustomerAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerAddress):
            return True

        return self.to_dict() != other.to_dict()
