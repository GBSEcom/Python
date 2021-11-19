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


class TeleCheckAchPaymentMethodAchBillTo(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'address_one': 'str',
        'address_two': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'phone': 'str',
        'email': 'str',
        'country_code': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'address_one': 'addressOne',
        'address_two': 'addressTwo',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'phone': 'phone',
        'email': 'email',
        'country_code': 'countryCode'
    }

    def __init__(self, first_name=None, last_name=None, address_one=None, address_two=None, city=None, state=None, zip=None, phone=None, email=None, country_code=None):  # noqa: E501
        """TeleCheckAchPaymentMethodAchBillTo - a model defined in OpenAPI"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._address_one = None
        self._address_two = None
        self._city = None
        self._state = None
        self._zip = None
        self._phone = None
        self._email = None
        self._country_code = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        self.last_name = last_name
        self.address_one = address_one
        if address_two is not None:
            self.address_two = address_two
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        if email is not None:
            self.email = email
        if country_code is not None:
            self.country_code = country_code

    @property
    def first_name(self):
        """Gets the first_name of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501

        Customer billing first name.  # noqa: E501

        :return: The first_name of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this TeleCheckAchPaymentMethodAchBillTo.

        Customer billing first name.  # noqa: E501

        :param first_name: The first_name of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :type: str
        """
        if first_name is not None and len(first_name) > 30:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `30`")  # noqa: E501
        if first_name is not None and not re.search(r'(?=.*[^\s])^[^|]+$', first_name):  # noqa: E501
            raise ValueError(r"Invalid value for `first_name`, must be a follow pattern or equal to `/(?=.*[^\s])^[^|]+$/`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501

        Customer billing last name.  # noqa: E501

        :return: The last_name of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this TeleCheckAchPaymentMethodAchBillTo.

        Customer billing last name.  # noqa: E501

        :param last_name: The last_name of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if last_name is not None and len(last_name) > 30:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `30`")  # noqa: E501
        if last_name is not None and not re.search(r'(?=.*[^\s])^[^|]+$', last_name):  # noqa: E501
            raise ValueError(r"Invalid value for `last_name`, must be a follow pattern or equal to `/(?=.*[^\s])^[^|]+$/`")  # noqa: E501

        self._last_name = last_name

    @property
    def address_one(self):
        """Gets the address_one of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501

        Customer billing address, first line.  # noqa: E501

        :return: The address_one of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :rtype: str
        """
        return self._address_one

    @address_one.setter
    def address_one(self, address_one):
        """Sets the address_one of this TeleCheckAchPaymentMethodAchBillTo.

        Customer billing address, first line.  # noqa: E501

        :param address_one: The address_one of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :type: str
        """
        if address_one is None:
            raise ValueError("Invalid value for `address_one`, must not be `None`")  # noqa: E501
        if address_one is not None and len(address_one) > 50:
            raise ValueError("Invalid value for `address_one`, length must be less than or equal to `50`")  # noqa: E501
        if address_one is not None and not re.search(r'(?=.*[^\s])^[^|]+$', address_one):  # noqa: E501
            raise ValueError(r"Invalid value for `address_one`, must be a follow pattern or equal to `/(?=.*[^\s])^[^|]+$/`")  # noqa: E501

        self._address_one = address_one

    @property
    def address_two(self):
        """Gets the address_two of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501

        Customer billing address, second line.  # noqa: E501

        :return: The address_two of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :rtype: str
        """
        return self._address_two

    @address_two.setter
    def address_two(self, address_two):
        """Sets the address_two of this TeleCheckAchPaymentMethodAchBillTo.

        Customer billing address, second line.  # noqa: E501

        :param address_two: The address_two of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :type: str
        """
        if address_two is not None and len(address_two) > 30:
            raise ValueError("Invalid value for `address_two`, length must be less than or equal to `30`")  # noqa: E501
        if address_two is not None and not re.search(r'(?=.*[^\s])^[^|]+$', address_two):  # noqa: E501
            raise ValueError(r"Invalid value for `address_two`, must be a follow pattern or equal to `/(?=.*[^\s])^[^|]+$/`")  # noqa: E501

        self._address_two = address_two

    @property
    def city(self):
        """Gets the city of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501

        Customer billing city.  # noqa: E501

        :return: The city of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this TeleCheckAchPaymentMethodAchBillTo.

        Customer billing city.  # noqa: E501

        :param city: The city of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501
        if city is not None and len(city) > 30:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `30`")  # noqa: E501
        if city is not None and not re.search(r'(?=.*[^\s])^[^|]+$', city):  # noqa: E501
            raise ValueError(r"Invalid value for `city`, must be a follow pattern or equal to `/(?=.*[^\s])^[^|]+$/`")  # noqa: E501

        self._city = city

    @property
    def state(self):
        """Gets the state of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501

        Customer billing state.  # noqa: E501

        :return: The state of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TeleCheckAchPaymentMethodAchBillTo.

        Customer billing state.  # noqa: E501

        :param state: The state of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        if state is not None and len(state) > 2:
            raise ValueError("Invalid value for `state`, length must be less than or equal to `2`")  # noqa: E501
        if state is not None and not re.search(r'^[A-Z]{2}$', state):  # noqa: E501
            raise ValueError(r"Invalid value for `state`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")  # noqa: E501

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501

        Customer billing zip code.  # noqa: E501

        :return: The zip of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this TeleCheckAchPaymentMethodAchBillTo.

        Customer billing zip code.  # noqa: E501

        :param zip: The zip of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :type: str
        """
        if zip is None:
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501
        if zip is not None and len(zip) > 11:
            raise ValueError("Invalid value for `zip`, length must be less than or equal to `11`")  # noqa: E501
        if zip is not None and not re.search(r'(?=.*[^\s])^[^|]+$', zip):  # noqa: E501
            raise ValueError(r"Invalid value for `zip`, must be a follow pattern or equal to `/(?=.*[^\s])^[^|]+$/`")  # noqa: E501

        self._zip = zip

    @property
    def phone(self):
        """Gets the phone of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501

        Customer billing phone number.  # noqa: E501

        :return: The phone of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this TeleCheckAchPaymentMethodAchBillTo.

        Customer billing phone number.  # noqa: E501

        :param phone: The phone of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501
        if phone is not None and len(phone) > 10:
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `10`")  # noqa: E501
        if phone is not None and not re.search(r'^[0-9]+$', phone):  # noqa: E501
            raise ValueError(r"Invalid value for `phone`, must be a follow pattern or equal to `/^[0-9]+$/`")  # noqa: E501

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501

        Customer billing email. Required if performing an ICA transaction.  # noqa: E501

        :return: The email of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TeleCheckAchPaymentMethodAchBillTo.

        Customer billing email. Required if performing an ICA transaction.  # noqa: E501

        :param email: The email of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 100:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `100`")  # noqa: E501
        if email is not None and not re.search(r'(?=.*[^\s])^[^|]+$', email):  # noqa: E501
            raise ValueError(r"Invalid value for `email`, must be a follow pattern or equal to `/(?=.*[^\s])^[^|]+$/`")  # noqa: E501

        self._email = email

    @property
    def country_code(self):
        """Gets the country_code of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501

        ISO country code. Required if performing an ICA transaction.  # noqa: E501

        :return: The country_code of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this TeleCheckAchPaymentMethodAchBillTo.

        ISO country code. Required if performing an ICA transaction.  # noqa: E501

        :param country_code: The country_code of this TeleCheckAchPaymentMethodAchBillTo.  # noqa: E501
        :type: str
        """
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")  # noqa: E501
        if country_code is not None and not re.search(r'^[A-Z]{2}$', country_code):  # noqa: E501
            raise ValueError(r"Invalid value for `country_code`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")  # noqa: E501

        self._country_code = country_code

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
        if not isinstance(other, TeleCheckAchPaymentMethodAchBillTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
