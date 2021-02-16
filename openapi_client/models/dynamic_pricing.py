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


class DynamicPricing(object):
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
        'conversion_type': 'str',
        'inquiry_rate_id': 'str',
        'foreign_currency': 'str',
        'foreign_amount': 'str'
    }

    attribute_map = {
        'conversion_type': 'conversionType',
        'inquiry_rate_id': 'inquiryRateId',
        'foreign_currency': 'foreignCurrency',
        'foreign_amount': 'foreignAmount'
    }

    def __init__(self, conversion_type=None, inquiry_rate_id=None, foreign_currency=None, foreign_amount=None):  # noqa: E501
        """DynamicPricing - a model defined in OpenAPI"""  # noqa: E501

        self._conversion_type = None
        self._inquiry_rate_id = None
        self._foreign_currency = None
        self._foreign_amount = None
        self.discriminator = None

        self.conversion_type = conversion_type
        self.inquiry_rate_id = inquiry_rate_id
        self.foreign_currency = foreign_currency
        self.foreign_amount = foreign_amount

    @property
    def conversion_type(self):
        """Gets the conversion_type of this DynamicPricing.  # noqa: E501

        Type of currency conversion.  # noqa: E501

        :return: The conversion_type of this DynamicPricing.  # noqa: E501
        :rtype: str
        """
        return self._conversion_type

    @conversion_type.setter
    def conversion_type(self, conversion_type):
        """Sets the conversion_type of this DynamicPricing.

        Type of currency conversion.  # noqa: E501

        :param conversion_type: The conversion_type of this DynamicPricing.  # noqa: E501
        :type: str
        """
        if conversion_type is None:
            raise ValueError("Invalid value for `conversion_type`, must not be `None`")  # noqa: E501

        self._conversion_type = conversion_type

    @property
    def inquiry_rate_id(self):
        """Gets the inquiry_rate_id of this DynamicPricing.  # noqa: E501

        Inquiry rate id.  # noqa: E501

        :return: The inquiry_rate_id of this DynamicPricing.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_rate_id

    @inquiry_rate_id.setter
    def inquiry_rate_id(self, inquiry_rate_id):
        """Sets the inquiry_rate_id of this DynamicPricing.

        Inquiry rate id.  # noqa: E501

        :param inquiry_rate_id: The inquiry_rate_id of this DynamicPricing.  # noqa: E501
        :type: str
        """
        if inquiry_rate_id is None:
            raise ValueError("Invalid value for `inquiry_rate_id`, must not be `None`")  # noqa: E501
        if inquiry_rate_id is not None and not re.search(r'^(?!\s*$).+', inquiry_rate_id):  # noqa: E501
            raise ValueError(r"Invalid value for `inquiry_rate_id`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._inquiry_rate_id = inquiry_rate_id

    @property
    def foreign_currency(self):
        """Gets the foreign_currency of this DynamicPricing.  # noqa: E501

        The currency code to convert for dynamic pricing in ISO 4217 currency code format.  # noqa: E501

        :return: The foreign_currency of this DynamicPricing.  # noqa: E501
        :rtype: str
        """
        return self._foreign_currency

    @foreign_currency.setter
    def foreign_currency(self, foreign_currency):
        """Sets the foreign_currency of this DynamicPricing.

        The currency code to convert for dynamic pricing in ISO 4217 currency code format.  # noqa: E501

        :param foreign_currency: The foreign_currency of this DynamicPricing.  # noqa: E501
        :type: str
        """
        if foreign_currency is None:
            raise ValueError("Invalid value for `foreign_currency`, must not be `None`")  # noqa: E501
        if foreign_currency is not None and not re.search(r'([A-Z]{3})|([0-9]{3})', foreign_currency):  # noqa: E501
            raise ValueError(r"Invalid value for `foreign_currency`, must be a follow pattern or equal to `/([A-Z]{3})|([0-9]{3})/`")  # noqa: E501

        self._foreign_currency = foreign_currency

    @property
    def foreign_amount(self):
        """Gets the foreign_amount of this DynamicPricing.  # noqa: E501

        Foreign amount.  # noqa: E501

        :return: The foreign_amount of this DynamicPricing.  # noqa: E501
        :rtype: str
        """
        return self._foreign_amount

    @foreign_amount.setter
    def foreign_amount(self, foreign_amount):
        """Sets the foreign_amount of this DynamicPricing.

        Foreign amount.  # noqa: E501

        :param foreign_amount: The foreign_amount of this DynamicPricing.  # noqa: E501
        :type: str
        """
        if foreign_amount is None:
            raise ValueError("Invalid value for `foreign_amount`, must not be `None`")  # noqa: E501
        if foreign_amount is not None and not re.search(r'^(?!\s*$).+', foreign_amount):  # noqa: E501
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
        if not isinstance(other, DynamicPricing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
