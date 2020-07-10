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


class Mcc6012(object):
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
        'date_of_birth': 'str',
        'account_first6': 'str',
        'account_last4': 'str',
        'account_num': 'str',
        'post_code': 'str',
        'surname': 'str'
    }

    attribute_map = {
        'date_of_birth': 'dateOfBirth',
        'account_first6': 'accountFirst6',
        'account_last4': 'accountLast4',
        'account_num': 'accountNum',
        'post_code': 'postCode',
        'surname': 'surname'
    }

    def __init__(self, date_of_birth=None, account_first6=None, account_last4=None, account_num=None, post_code=None, surname=None, local_vars_configuration=None):  # noqa: E501
        """Mcc6012 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date_of_birth = None
        self._account_first6 = None
        self._account_last4 = None
        self._account_num = None
        self._post_code = None
        self._surname = None
        self.discriminator = None

        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if account_first6 is not None:
            self.account_first6 = account_first6
        if account_last4 is not None:
            self.account_last4 = account_last4
        if account_num is not None:
            self.account_num = account_num
        if post_code is not None:
            self.post_code = post_code
        if surname is not None:
            self.surname = surname

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this Mcc6012.  # noqa: E501

        The date of birth of the cardholder (YYYYMMDD).  # noqa: E501

        :return: The date_of_birth of this Mcc6012.  # noqa: E501
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this Mcc6012.

        The date of birth of the cardholder (YYYYMMDD).  # noqa: E501

        :param date_of_birth: The date_of_birth of this Mcc6012.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                date_of_birth is not None and len(date_of_birth) > 8):
            raise ValueError("Invalid value for `date_of_birth`, length must be less than or equal to `8`")  # noqa: E501

        self._date_of_birth = date_of_birth

    @property
    def account_first6(self):
        """Gets the account_first6 of this Mcc6012.  # noqa: E501

        The first six digits of the primary account number.  # noqa: E501

        :return: The account_first6 of this Mcc6012.  # noqa: E501
        :rtype: str
        """
        return self._account_first6

    @account_first6.setter
    def account_first6(self, account_first6):
        """Sets the account_first6 of this Mcc6012.

        The first six digits of the primary account number.  # noqa: E501

        :param account_first6: The account_first6 of this Mcc6012.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                account_first6 is not None and len(account_first6) > 6):
            raise ValueError("Invalid value for `account_first6`, length must be less than or equal to `6`")  # noqa: E501

        self._account_first6 = account_first6

    @property
    def account_last4(self):
        """Gets the account_last4 of this Mcc6012.  # noqa: E501

        The last four digits of the primary account number.  # noqa: E501

        :return: The account_last4 of this Mcc6012.  # noqa: E501
        :rtype: str
        """
        return self._account_last4

    @account_last4.setter
    def account_last4(self, account_last4):
        """Sets the account_last4 of this Mcc6012.

        The last four digits of the primary account number.  # noqa: E501

        :param account_last4: The account_last4 of this Mcc6012.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                account_last4 is not None and len(account_last4) > 4):
            raise ValueError("Invalid value for `account_last4`, length must be less than or equal to `4`")  # noqa: E501

        self._account_last4 = account_last4

    @property
    def account_num(self):
        """Gets the account_num of this Mcc6012.  # noqa: E501

        The account number where the primary account number is not a card.  # noqa: E501

        :return: The account_num of this Mcc6012.  # noqa: E501
        :rtype: str
        """
        return self._account_num

    @account_num.setter
    def account_num(self, account_num):
        """Sets the account_num of this Mcc6012.

        The account number where the primary account number is not a card.  # noqa: E501

        :param account_num: The account_num of this Mcc6012.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                account_num is not None and len(account_num) > 50):
            raise ValueError("Invalid value for `account_num`, length must be less than or equal to `50`")  # noqa: E501

        self._account_num = account_num

    @property
    def post_code(self):
        """Gets the post_code of this Mcc6012.  # noqa: E501

        The postal code of the cardholder.  # noqa: E501

        :return: The post_code of this Mcc6012.  # noqa: E501
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this Mcc6012.

        The postal code of the cardholder.  # noqa: E501

        :param post_code: The post_code of this Mcc6012.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                post_code is not None and len(post_code) > 50):
            raise ValueError("Invalid value for `post_code`, length must be less than or equal to `50`")  # noqa: E501

        self._post_code = post_code

    @property
    def surname(self):
        """Gets the surname of this Mcc6012.  # noqa: E501

        Surname or last name of the card holder.  # noqa: E501

        :return: The surname of this Mcc6012.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this Mcc6012.

        Surname or last name of the card holder.  # noqa: E501

        :param surname: The surname of this Mcc6012.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                surname is not None and len(surname) > 100):
            raise ValueError("Invalid value for `surname`, length must be less than or equal to `100`")  # noqa: E501

        self._surname = surname

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
        if not isinstance(other, Mcc6012):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Mcc6012):
            return True

        return self.to_dict() != other.to_dict()
