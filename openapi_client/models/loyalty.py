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


class Loyalty(object):
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
        'program': 'str',
        'balance': 'float'
    }

    attribute_map = {
        'id': 'id',
        'program': 'program',
        'balance': 'balance'
    }

    def __init__(self, id=None, program=None, balance=None, local_vars_configuration=None):  # noqa: E501
        """Loyalty - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._program = None
        self._balance = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if program is not None:
            self.program = program
        if balance is not None:
            self.balance = balance

    @property
    def id(self):
        """Gets the id of this Loyalty.  # noqa: E501

        A unique ID associated with the loyalty program account. Must be unique within the merchants system. Depending on loyalty programs the account might also serve as a credit/bank account. If this is the case the ID must be not be the PAN.  # noqa: E501

        :return: The id of this Loyalty.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Loyalty.

        A unique ID associated with the loyalty program account. Must be unique within the merchants system. Depending on loyalty programs the account might also serve as a credit/bank account. If this is the case the ID must be not be the PAN.  # noqa: E501

        :param id: The id of this Loyalty.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def program(self):
        """Gets the program of this Loyalty.  # noqa: E501

        A string that identifies the program in which the customer is enrolled if the merchant supports several programs or levels.  # noqa: E501

        :return: The program of this Loyalty.  # noqa: E501
        :rtype: str
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this Loyalty.

        A string that identifies the program in which the customer is enrolled if the merchant supports several programs or levels.  # noqa: E501

        :param program: The program of this Loyalty.  # noqa: E501
        :type: str
        """

        self._program = program

    @property
    def balance(self):
        """Gets the balance of this Loyalty.  # noqa: E501

        The balance of the loyalty program account in a program specific currency (e.g. points).  # noqa: E501

        :return: The balance of this Loyalty.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Loyalty.

        The balance of the loyalty program account in a program specific currency (e.g. points).  # noqa: E501

        :param balance: The balance of this Loyalty.  # noqa: E501
        :type: float
        """

        self._balance = balance

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
        if not isinstance(other, Loyalty):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Loyalty):
            return True

        return self.to_dict() != other.to_dict()
