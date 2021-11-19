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


class Customer(object):
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
        'id': 'str',
        'start_date': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'middle_name': 'str',
        'email': 'str',
        'session_id': 'str',
        'username': 'str',
        'gender': 'str',
        'date_of_birth': 'str',
        'address': 'CustomerAddress',
        'user_defined': 'object'
    }

    attribute_map = {
        'id': 'id',
        'start_date': 'startDate',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'middle_name': 'middleName',
        'email': 'email',
        'session_id': 'sessionId',
        'username': 'username',
        'gender': 'gender',
        'date_of_birth': 'dateOfBirth',
        'address': 'address',
        'user_defined': 'userDefined'
    }

    def __init__(self, id=None, start_date=None, first_name=None, last_name=None, middle_name=None, email=None, session_id=None, username=None, gender=None, date_of_birth=None, address=None, user_defined=None):  # noqa: E501
        """Customer - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._start_date = None
        self._first_name = None
        self._last_name = None
        self._middle_name = None
        self._email = None
        self._session_id = None
        self._username = None
        self._gender = None
        self._date_of_birth = None
        self._address = None
        self._user_defined = None
        self.discriminator = None

        self.id = id
        if start_date is not None:
            self.start_date = start_date
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if middle_name is not None:
            self.middle_name = middle_name
        if email is not None:
            self.email = email
        if session_id is not None:
            self.session_id = session_id
        if username is not None:
            self.username = username
        if gender is not None:
            self.gender = gender
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if address is not None:
            self.address = address
        if user_defined is not None:
            self.user_defined = user_defined

    @property
    def id(self):
        """Gets the id of this Customer.  # noqa: E501

        Unique ID for the customer, if registered. This field is required if the parent object is present.  # noqa: E501

        :return: The id of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Customer.

        Unique ID for the customer, if registered. This field is required if the parent object is present.  # noqa: E501

        :param id: The id of this Customer.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and not re.search(r'^(?!\s*$).+', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._id = id

    @property
    def start_date(self):
        """Gets the start_date of this Customer.  # noqa: E501

        The timestamp of the customers registration in the merchants platform. Format is YYYY-MM-DD.  # noqa: E501

        :return: The start_date of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Customer.

        The timestamp of the customers registration in the merchants platform. Format is YYYY-MM-DD.  # noqa: E501

        :param start_date: The start_date of this Customer.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def first_name(self):
        """Gets the first_name of this Customer.  # noqa: E501

        Customer's first name.  # noqa: E501

        :return: The first_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Customer.

        Customer's first name.  # noqa: E501

        :param first_name: The first_name of this Customer.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Customer.  # noqa: E501

        Customer's last name.  # noqa: E501

        :return: The last_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Customer.

        Customer's last name.  # noqa: E501

        :param last_name: The last_name of this Customer.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def middle_name(self):
        """Gets the middle_name of this Customer.  # noqa: E501

        Customer's middle name.  # noqa: E501

        :return: The middle_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this Customer.

        Customer's middle name.  # noqa: E501

        :param middle_name: The middle_name of this Customer.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def email(self):
        """Gets the email of this Customer.  # noqa: E501

        Customer's email address.  # noqa: E501

        :return: The email of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Customer.

        Customer's email address.  # noqa: E501

        :param email: The email of this Customer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def session_id(self):
        """Gets the session_id of this Customer.  # noqa: E501

        The unique ID of the current login session. Must be unique for the customer.  # noqa: E501

        :return: The session_id of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this Customer.

        The unique ID of the current login session. Must be unique for the customer.  # noqa: E501

        :param session_id: The session_id of this Customer.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def username(self):
        """Gets the username of this Customer.  # noqa: E501

        The username of this customer in the merchants system. This field should contain customer-supplied data if available instead of a generated ID. This field can contain the clients email address if it is also used for authentication purposes.  # noqa: E501

        :return: The username of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Customer.

        The username of this customer in the merchants system. This field should contain customer-supplied data if available instead of a generated ID. This field can contain the clients email address if it is also used for authentication purposes.  # noqa: E501

        :param username: The username of this Customer.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def gender(self):
        """Gets the gender of this Customer.  # noqa: E501

        The customers gender. Do not set this property if the customer does not specify a gender.  # noqa: E501

        :return: The gender of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Customer.

        The customers gender. Do not set this property if the customer does not specify a gender.  # noqa: E501

        :param gender: The gender of this Customer.  # noqa: E501
        :type: str
        """
        allowed_values = ["male", "female", "other"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this Customer.  # noqa: E501

        The customer's year of birth. Format is YYYY.  # noqa: E501

        :return: The date_of_birth of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this Customer.

        The customer's year of birth. Format is YYYY.  # noqa: E501

        :param date_of_birth: The date_of_birth of this Customer.  # noqa: E501
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def address(self):
        """Gets the address of this Customer.  # noqa: E501


        :return: The address of this Customer.  # noqa: E501
        :rtype: CustomerAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Customer.


        :param address: The address of this Customer.  # noqa: E501
        :type: CustomerAddress
        """

        self._address = address

    @property
    def user_defined(self):
        """Gets the user_defined of this Customer.  # noqa: E501

        A JSON object that can carry any additional information about the customer that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this Customer.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this Customer.

        A JSON object that can carry any additional information about the customer that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this Customer.  # noqa: E501
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
        if not isinstance(other, Customer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
