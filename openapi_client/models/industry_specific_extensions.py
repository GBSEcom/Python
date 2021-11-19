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


class IndustrySpecificExtensions(object):
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
        'airline': 'Airline',
        'lodging': 'Lodging',
        'car_rental': 'CarRental',
        'mcc6012': 'Mcc6012'
    }

    attribute_map = {
        'airline': 'airline',
        'lodging': 'lodging',
        'car_rental': 'carRental',
        'mcc6012': 'mcc6012'
    }

    def __init__(self, airline=None, lodging=None, car_rental=None, mcc6012=None):  # noqa: E501
        """IndustrySpecificExtensions - a model defined in OpenAPI"""  # noqa: E501

        self._airline = None
        self._lodging = None
        self._car_rental = None
        self._mcc6012 = None
        self.discriminator = None

        if airline is not None:
            self.airline = airline
        if lodging is not None:
            self.lodging = lodging
        if car_rental is not None:
            self.car_rental = car_rental
        if mcc6012 is not None:
            self.mcc6012 = mcc6012

    @property
    def airline(self):
        """Gets the airline of this IndustrySpecificExtensions.  # noqa: E501


        :return: The airline of this IndustrySpecificExtensions.  # noqa: E501
        :rtype: Airline
        """
        return self._airline

    @airline.setter
    def airline(self, airline):
        """Sets the airline of this IndustrySpecificExtensions.


        :param airline: The airline of this IndustrySpecificExtensions.  # noqa: E501
        :type: Airline
        """

        self._airline = airline

    @property
    def lodging(self):
        """Gets the lodging of this IndustrySpecificExtensions.  # noqa: E501


        :return: The lodging of this IndustrySpecificExtensions.  # noqa: E501
        :rtype: Lodging
        """
        return self._lodging

    @lodging.setter
    def lodging(self, lodging):
        """Sets the lodging of this IndustrySpecificExtensions.


        :param lodging: The lodging of this IndustrySpecificExtensions.  # noqa: E501
        :type: Lodging
        """

        self._lodging = lodging

    @property
    def car_rental(self):
        """Gets the car_rental of this IndustrySpecificExtensions.  # noqa: E501


        :return: The car_rental of this IndustrySpecificExtensions.  # noqa: E501
        :rtype: CarRental
        """
        return self._car_rental

    @car_rental.setter
    def car_rental(self, car_rental):
        """Sets the car_rental of this IndustrySpecificExtensions.


        :param car_rental: The car_rental of this IndustrySpecificExtensions.  # noqa: E501
        :type: CarRental
        """

        self._car_rental = car_rental

    @property
    def mcc6012(self):
        """Gets the mcc6012 of this IndustrySpecificExtensions.  # noqa: E501


        :return: The mcc6012 of this IndustrySpecificExtensions.  # noqa: E501
        :rtype: Mcc6012
        """
        return self._mcc6012

    @mcc6012.setter
    def mcc6012(self, mcc6012):
        """Sets the mcc6012 of this IndustrySpecificExtensions.


        :param mcc6012: The mcc6012 of this IndustrySpecificExtensions.  # noqa: E501
        :type: Mcc6012
        """

        self._mcc6012 = mcc6012

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
        if not isinstance(other, IndustrySpecificExtensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
