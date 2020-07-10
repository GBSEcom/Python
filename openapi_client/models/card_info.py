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


class CardInfo(object):
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
        'brand': 'str',
        'brand_product_id': 'str',
        'card_function': 'CardFunction',
        'commercial_card': 'str',
        'issuer_country': 'str',
        'issuer_name': 'str'
    }

    attribute_map = {
        'brand': 'brand',
        'brand_product_id': 'brandProductId',
        'card_function': 'cardFunction',
        'commercial_card': 'commercialCard',
        'issuer_country': 'issuerCountry',
        'issuer_name': 'issuerName'
    }

    def __init__(self, brand=None, brand_product_id=None, card_function=None, commercial_card=None, issuer_country=None, issuer_name=None, local_vars_configuration=None):  # noqa: E501
        """CardInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._brand = None
        self._brand_product_id = None
        self._card_function = None
        self._commercial_card = None
        self._issuer_country = None
        self._issuer_name = None
        self.discriminator = None

        if brand is not None:
            self.brand = brand
        if brand_product_id is not None:
            self.brand_product_id = brand_product_id
        if card_function is not None:
            self.card_function = card_function
        if commercial_card is not None:
            self.commercial_card = commercial_card
        if issuer_country is not None:
            self.issuer_country = issuer_country
        if issuer_name is not None:
            self.issuer_name = issuer_name

    @property
    def brand(self):
        """Gets the brand of this CardInfo.  # noqa: E501

        The card brand.  # noqa: E501

        :return: The brand of this CardInfo.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this CardInfo.

        The card brand.  # noqa: E501

        :param brand: The brand of this CardInfo.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def brand_product_id(self):
        """Gets the brand_product_id of this CardInfo.  # noqa: E501

        The product ID of the brand.  # noqa: E501

        :return: The brand_product_id of this CardInfo.  # noqa: E501
        :rtype: str
        """
        return self._brand_product_id

    @brand_product_id.setter
    def brand_product_id(self, brand_product_id):
        """Sets the brand_product_id of this CardInfo.

        The product ID of the brand.  # noqa: E501

        :param brand_product_id: The brand_product_id of this CardInfo.  # noqa: E501
        :type: str
        """

        self._brand_product_id = brand_product_id

    @property
    def card_function(self):
        """Gets the card_function of this CardInfo.  # noqa: E501


        :return: The card_function of this CardInfo.  # noqa: E501
        :rtype: CardFunction
        """
        return self._card_function

    @card_function.setter
    def card_function(self, card_function):
        """Sets the card_function of this CardInfo.


        :param card_function: The card_function of this CardInfo.  # noqa: E501
        :type: CardFunction
        """

        self._card_function = card_function

    @property
    def commercial_card(self):
        """Gets the commercial_card of this CardInfo.  # noqa: E501

        Indicates whether it is a corporate or non-corporate card.  # noqa: E501

        :return: The commercial_card of this CardInfo.  # noqa: E501
        :rtype: str
        """
        return self._commercial_card

    @commercial_card.setter
    def commercial_card(self, commercial_card):
        """Sets the commercial_card of this CardInfo.

        Indicates whether it is a corporate or non-corporate card.  # noqa: E501

        :param commercial_card: The commercial_card of this CardInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["CORPORATE", "NON_CORPORATE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and commercial_card not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `commercial_card` ({0}), must be one of {1}"  # noqa: E501
                .format(commercial_card, allowed_values)
            )

        self._commercial_card = commercial_card

    @property
    def issuer_country(self):
        """Gets the issuer_country of this CardInfo.  # noqa: E501

        The country of the issuer.  # noqa: E501

        :return: The issuer_country of this CardInfo.  # noqa: E501
        :rtype: str
        """
        return self._issuer_country

    @issuer_country.setter
    def issuer_country(self, issuer_country):
        """Sets the issuer_country of this CardInfo.

        The country of the issuer.  # noqa: E501

        :param issuer_country: The issuer_country of this CardInfo.  # noqa: E501
        :type: str
        """

        self._issuer_country = issuer_country

    @property
    def issuer_name(self):
        """Gets the issuer_name of this CardInfo.  # noqa: E501

        The name of the issuer.  # noqa: E501

        :return: The issuer_name of this CardInfo.  # noqa: E501
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """Sets the issuer_name of this CardInfo.

        The name of the issuer.  # noqa: E501

        :param issuer_name: The issuer_name of this CardInfo.  # noqa: E501
        :type: str
        """

        self._issuer_name = issuer_name

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
        if not isinstance(other, CardInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CardInfo):
            return True

        return self.to_dict() != other.to_dict()
