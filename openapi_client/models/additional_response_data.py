# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.4.0.20210824.002
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AdditionalResponseData(object):
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
        'issuing_bank_name': 'str',
        'country_of_issuance': 'str',
        'card_product_id': 'str',
        'detailed_product_id': 'str',
        'association_response_code_adtl': 'str',
        'card_brand': 'str'
    }

    attribute_map = {
        'issuing_bank_name': 'issuingBankName',
        'country_of_issuance': 'countryOfIssuance',
        'card_product_id': 'cardProductID',
        'detailed_product_id': 'detailedProductID',
        'association_response_code_adtl': 'associationResponseCodeAdtl',
        'card_brand': 'cardBrand'
    }

    def __init__(self, issuing_bank_name=None, country_of_issuance=None, card_product_id=None, detailed_product_id=None, association_response_code_adtl=None, card_brand=None):  # noqa: E501
        """AdditionalResponseData - a model defined in OpenAPI"""  # noqa: E501

        self._issuing_bank_name = None
        self._country_of_issuance = None
        self._card_product_id = None
        self._detailed_product_id = None
        self._association_response_code_adtl = None
        self._card_brand = None
        self.discriminator = None

        if issuing_bank_name is not None:
            self.issuing_bank_name = issuing_bank_name
        if country_of_issuance is not None:
            self.country_of_issuance = country_of_issuance
        if card_product_id is not None:
            self.card_product_id = card_product_id
        if detailed_product_id is not None:
            self.detailed_product_id = detailed_product_id
        if association_response_code_adtl is not None:
            self.association_response_code_adtl = association_response_code_adtl
        if card_brand is not None:
            self.card_brand = card_brand

    @property
    def issuing_bank_name(self):
        """Gets the issuing_bank_name of this AdditionalResponseData.  # noqa: E501

        Issuing Bank Name.  # noqa: E501

        :return: The issuing_bank_name of this AdditionalResponseData.  # noqa: E501
        :rtype: str
        """
        return self._issuing_bank_name

    @issuing_bank_name.setter
    def issuing_bank_name(self, issuing_bank_name):
        """Sets the issuing_bank_name of this AdditionalResponseData.

        Issuing Bank Name.  # noqa: E501

        :param issuing_bank_name: The issuing_bank_name of this AdditionalResponseData.  # noqa: E501
        :type: str
        """
        if issuing_bank_name is not None and len(issuing_bank_name) > 18:
            raise ValueError("Invalid value for `issuing_bank_name`, length must be less than or equal to `18`")  # noqa: E501

        self._issuing_bank_name = issuing_bank_name

    @property
    def country_of_issuance(self):
        """Gets the country_of_issuance of this AdditionalResponseData.  # noqa: E501

        Country of Issuance.  # noqa: E501

        :return: The country_of_issuance of this AdditionalResponseData.  # noqa: E501
        :rtype: str
        """
        return self._country_of_issuance

    @country_of_issuance.setter
    def country_of_issuance(self, country_of_issuance):
        """Sets the country_of_issuance of this AdditionalResponseData.

        Country of Issuance.  # noqa: E501

        :param country_of_issuance: The country_of_issuance of this AdditionalResponseData.  # noqa: E501
        :type: str
        """
        if country_of_issuance is not None and len(country_of_issuance) > 3:
            raise ValueError("Invalid value for `country_of_issuance`, length must be less than or equal to `3`")  # noqa: E501

        self._country_of_issuance = country_of_issuance

    @property
    def card_product_id(self):
        """Gets the card_product_id of this AdditionalResponseData.  # noqa: E501

        Card Product ID.  # noqa: E501

        :return: The card_product_id of this AdditionalResponseData.  # noqa: E501
        :rtype: str
        """
        return self._card_product_id

    @card_product_id.setter
    def card_product_id(self, card_product_id):
        """Sets the card_product_id of this AdditionalResponseData.

        Card Product ID.  # noqa: E501

        :param card_product_id: The card_product_id of this AdditionalResponseData.  # noqa: E501
        :type: str
        """
        if card_product_id is not None and len(card_product_id) > 1:
            raise ValueError("Invalid value for `card_product_id`, length must be less than or equal to `1`")  # noqa: E501

        self._card_product_id = card_product_id

    @property
    def detailed_product_id(self):
        """Gets the detailed_product_id of this AdditionalResponseData.  # noqa: E501

        Detailed Product ID.  # noqa: E501

        :return: The detailed_product_id of this AdditionalResponseData.  # noqa: E501
        :rtype: str
        """
        return self._detailed_product_id

    @detailed_product_id.setter
    def detailed_product_id(self, detailed_product_id):
        """Sets the detailed_product_id of this AdditionalResponseData.

        Detailed Product ID.  # noqa: E501

        :param detailed_product_id: The detailed_product_id of this AdditionalResponseData.  # noqa: E501
        :type: str
        """
        if detailed_product_id is not None and len(detailed_product_id) > 3:
            raise ValueError("Invalid value for `detailed_product_id`, length must be less than or equal to `3`")  # noqa: E501

        self._detailed_product_id = detailed_product_id

    @property
    def association_response_code_adtl(self):
        """Gets the association_response_code_adtl of this AdditionalResponseData.  # noqa: E501

        Association Response Code.  # noqa: E501

        :return: The association_response_code_adtl of this AdditionalResponseData.  # noqa: E501
        :rtype: str
        """
        return self._association_response_code_adtl

    @association_response_code_adtl.setter
    def association_response_code_adtl(self, association_response_code_adtl):
        """Sets the association_response_code_adtl of this AdditionalResponseData.

        Association Response Code.  # noqa: E501

        :param association_response_code_adtl: The association_response_code_adtl of this AdditionalResponseData.  # noqa: E501
        :type: str
        """
        if association_response_code_adtl is not None and len(association_response_code_adtl) > 3:
            raise ValueError("Invalid value for `association_response_code_adtl`, length must be less than or equal to `3`")  # noqa: E501

        self._association_response_code_adtl = association_response_code_adtl

    @property
    def card_brand(self):
        """Gets the card_brand of this AdditionalResponseData.  # noqa: E501

        Card Brand.  # noqa: E501

        :return: The card_brand of this AdditionalResponseData.  # noqa: E501
        :rtype: str
        """
        return self._card_brand

    @card_brand.setter
    def card_brand(self, card_brand):
        """Sets the card_brand of this AdditionalResponseData.

        Card Brand.  # noqa: E501

        :param card_brand: The card_brand of this AdditionalResponseData.  # noqa: E501
        :type: str
        """
        if card_brand is not None and len(card_brand) > 1:
            raise ValueError("Invalid value for `card_brand`, length must be less than or equal to `1`")  # noqa: E501

        self._card_brand = card_brand

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
        if not isinstance(other, AdditionalResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
