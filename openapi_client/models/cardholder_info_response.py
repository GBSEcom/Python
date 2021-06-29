# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.3.0.20210608.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CardholderInfoResponse(object):
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
        'postal_code_or_zip_match': 'str',
        'address_match': 'str',
        'name_match': 'str',
        'telephone_match': 'str',
        'email_match': 'str',
        'association_cardholder_info_response': 'str'
    }

    attribute_map = {
        'postal_code_or_zip_match': 'postalCodeOrZipMatch',
        'address_match': 'addressMatch',
        'name_match': 'nameMatch',
        'telephone_match': 'telephoneMatch',
        'email_match': 'emailMatch',
        'association_cardholder_info_response': 'associationCardholderInfoResponse'
    }

    def __init__(self, postal_code_or_zip_match=None, address_match=None, name_match=None, telephone_match=None, email_match=None, association_cardholder_info_response=None):  # noqa: E501
        """CardholderInfoResponse - a model defined in OpenAPI"""  # noqa: E501

        self._postal_code_or_zip_match = None
        self._address_match = None
        self._name_match = None
        self._telephone_match = None
        self._email_match = None
        self._association_cardholder_info_response = None
        self.discriminator = None

        if postal_code_or_zip_match is not None:
            self.postal_code_or_zip_match = postal_code_or_zip_match
        if address_match is not None:
            self.address_match = address_match
        if name_match is not None:
            self.name_match = name_match
        if telephone_match is not None:
            self.telephone_match = telephone_match
        if email_match is not None:
            self.email_match = email_match
        if association_cardholder_info_response is not None:
            self.association_cardholder_info_response = association_cardholder_info_response

    @property
    def postal_code_or_zip_match(self):
        """Gets the postal_code_or_zip_match of this CardholderInfoResponse.  # noqa: E501

        Response if card holder postal code matches that on file.  # noqa: E501

        :return: The postal_code_or_zip_match of this CardholderInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._postal_code_or_zip_match

    @postal_code_or_zip_match.setter
    def postal_code_or_zip_match(self, postal_code_or_zip_match):
        """Sets the postal_code_or_zip_match of this CardholderInfoResponse.

        Response if card holder postal code matches that on file.  # noqa: E501

        :param postal_code_or_zip_match: The postal_code_or_zip_match of this CardholderInfoResponse.  # noqa: E501
        :type: str
        """

        self._postal_code_or_zip_match = postal_code_or_zip_match

    @property
    def address_match(self):
        """Gets the address_match of this CardholderInfoResponse.  # noqa: E501

        Response if card holder address matches that on file.  # noqa: E501

        :return: The address_match of this CardholderInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._address_match

    @address_match.setter
    def address_match(self, address_match):
        """Sets the address_match of this CardholderInfoResponse.

        Response if card holder address matches that on file.  # noqa: E501

        :param address_match: The address_match of this CardholderInfoResponse.  # noqa: E501
        :type: str
        """

        self._address_match = address_match

    @property
    def name_match(self):
        """Gets the name_match of this CardholderInfoResponse.  # noqa: E501

        Response if card holder name matches that on file.  # noqa: E501

        :return: The name_match of this CardholderInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._name_match

    @name_match.setter
    def name_match(self, name_match):
        """Sets the name_match of this CardholderInfoResponse.

        Response if card holder name matches that on file.  # noqa: E501

        :param name_match: The name_match of this CardholderInfoResponse.  # noqa: E501
        :type: str
        """

        self._name_match = name_match

    @property
    def telephone_match(self):
        """Gets the telephone_match of this CardholderInfoResponse.  # noqa: E501

        Response if card holder telephone matches that on file.  # noqa: E501

        :return: The telephone_match of this CardholderInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._telephone_match

    @telephone_match.setter
    def telephone_match(self, telephone_match):
        """Sets the telephone_match of this CardholderInfoResponse.

        Response if card holder telephone matches that on file.  # noqa: E501

        :param telephone_match: The telephone_match of this CardholderInfoResponse.  # noqa: E501
        :type: str
        """

        self._telephone_match = telephone_match

    @property
    def email_match(self):
        """Gets the email_match of this CardholderInfoResponse.  # noqa: E501

        Response if card holder email matches that on file.  # noqa: E501

        :return: The email_match of this CardholderInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_match

    @email_match.setter
    def email_match(self, email_match):
        """Sets the email_match of this CardholderInfoResponse.

        Response if card holder email matches that on file.  # noqa: E501

        :param email_match: The email_match of this CardholderInfoResponse.  # noqa: E501
        :type: str
        """

        self._email_match = email_match

    @property
    def association_cardholder_info_response(self):
        """Gets the association_cardholder_info_response of this CardholderInfoResponse.  # noqa: E501

        Raw cardholder info response from AMEX with no mapping.  # noqa: E501

        :return: The association_cardholder_info_response of this CardholderInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._association_cardholder_info_response

    @association_cardholder_info_response.setter
    def association_cardholder_info_response(self, association_cardholder_info_response):
        """Sets the association_cardholder_info_response of this CardholderInfoResponse.

        Raw cardholder info response from AMEX with no mapping.  # noqa: E501

        :param association_cardholder_info_response: The association_cardholder_info_response of this CardholderInfoResponse.  # noqa: E501
        :type: str
        """

        self._association_cardholder_info_response = association_cardholder_info_response

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
        if not isinstance(other, CardholderInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
