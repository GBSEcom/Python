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


class DynamicPricingAllOf(object):
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
        'foreign_currency': 'str',
        'foreign_amount': 'str'
    }

    attribute_map = {
        'foreign_currency': 'foreignCurrency',
        'foreign_amount': 'foreignAmount'
    }

    def __init__(self, foreign_currency=None, foreign_amount=None, local_vars_configuration=None):  # noqa: E501
        """DynamicPricingAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._foreign_currency = None
        self._foreign_amount = None
        self.discriminator = None

        self.foreign_currency = foreign_currency
        self.foreign_amount = foreign_amount

    @property
    def foreign_currency(self):
        """Gets the foreign_currency of this DynamicPricingAllOf.  # noqa: E501

        The currency code to convert for dynamic pricing in ISO 4217 currency code format.  # noqa: E501

        :return: The foreign_currency of this DynamicPricingAllOf.  # noqa: E501
        :rtype: str
        """
        return self._foreign_currency

    @foreign_currency.setter
    def foreign_currency(self, foreign_currency):
        """Sets the foreign_currency of this DynamicPricingAllOf.

        The currency code to convert for dynamic pricing in ISO 4217 currency code format.  # noqa: E501

        :param foreign_currency: The foreign_currency of this DynamicPricingAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and foreign_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `foreign_currency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                foreign_currency is not None and not re.search(r'([A-Z]{3})|([0-9]{3})', foreign_currency)):  # noqa: E501
            raise ValueError(r"Invalid value for `foreign_currency`, must be a follow pattern or equal to `/([A-Z]{3})|([0-9]{3})/`")  # noqa: E501

        self._foreign_currency = foreign_currency

    @property
    def foreign_amount(self):
        """Gets the foreign_amount of this DynamicPricingAllOf.  # noqa: E501

        Foreign amount.  # noqa: E501

        :return: The foreign_amount of this DynamicPricingAllOf.  # noqa: E501
        :rtype: str
        """
        return self._foreign_amount

    @foreign_amount.setter
    def foreign_amount(self, foreign_amount):
        """Sets the foreign_amount of this DynamicPricingAllOf.

        Foreign amount.  # noqa: E501

        :param foreign_amount: The foreign_amount of this DynamicPricingAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and foreign_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `foreign_amount`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                foreign_amount is not None and not re.search(r'^(?!\s*$).+', foreign_amount)):  # noqa: E501
            raise ValueError(r"Invalid value for `foreign_amount`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._foreign_amount = foreign_amount

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
        if not isinstance(other, DynamicPricingAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DynamicPricingAllOf):
            return True

        return self.to_dict() != other.to_dict()
