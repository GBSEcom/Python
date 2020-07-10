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


class AccountUpdaterResponse(object):
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
        'updated_card': 'str',
        'updated_token': 'str',
        'updated_expiration_date': 'str',
        'updated_account_status': 'str',
        'updated_account_error_code': 'str'
    }

    attribute_map = {
        'updated_card': 'updatedCard',
        'updated_token': 'updatedToken',
        'updated_expiration_date': 'updatedExpirationDate',
        'updated_account_status': 'updatedAccountStatus',
        'updated_account_error_code': 'updatedAccountErrorCode'
    }

    def __init__(self, updated_card=None, updated_token=None, updated_expiration_date=None, updated_account_status=None, updated_account_error_code=None, local_vars_configuration=None):  # noqa: E501
        """AccountUpdaterResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._updated_card = None
        self._updated_token = None
        self._updated_expiration_date = None
        self._updated_account_status = None
        self._updated_account_error_code = None
        self.discriminator = None

        if updated_card is not None:
            self.updated_card = updated_card
        if updated_token is not None:
            self.updated_token = updated_token
        if updated_expiration_date is not None:
            self.updated_expiration_date = updated_expiration_date
        if updated_account_status is not None:
            self.updated_account_status = updated_account_status
        if updated_account_error_code is not None:
            self.updated_account_error_code = updated_account_error_code

    @property
    def updated_card(self):
        """Gets the updated_card of this AccountUpdaterResponse.  # noqa: E501

        Account updater replacement PAN or TransArmor token.  # noqa: E501

        :return: The updated_card of this AccountUpdaterResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_card

    @updated_card.setter
    def updated_card(self, updated_card):
        """Sets the updated_card of this AccountUpdaterResponse.

        Account updater replacement PAN or TransArmor token.  # noqa: E501

        :param updated_card: The updated_card of this AccountUpdaterResponse.  # noqa: E501
        :type: str
        """

        self._updated_card = updated_card

    @property
    def updated_token(self):
        """Gets the updated_token of this AccountUpdaterResponse.  # noqa: E501

        Updated value of token.  # noqa: E501

        :return: The updated_token of this AccountUpdaterResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_token

    @updated_token.setter
    def updated_token(self, updated_token):
        """Sets the updated_token of this AccountUpdaterResponse.

        Updated value of token.  # noqa: E501

        :param updated_token: The updated_token of this AccountUpdaterResponse.  # noqa: E501
        :type: str
        """

        self._updated_token = updated_token

    @property
    def updated_expiration_date(self):
        """Gets the updated_expiration_date of this AccountUpdaterResponse.  # noqa: E501

        New account number expiration date in MMYY format.  # noqa: E501

        :return: The updated_expiration_date of this AccountUpdaterResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_expiration_date

    @updated_expiration_date.setter
    def updated_expiration_date(self, updated_expiration_date):
        """Sets the updated_expiration_date of this AccountUpdaterResponse.

        New account number expiration date in MMYY format.  # noqa: E501

        :param updated_expiration_date: The updated_expiration_date of this AccountUpdaterResponse.  # noqa: E501
        :type: str
        """

        self._updated_expiration_date = updated_expiration_date

    @property
    def updated_account_status(self):
        """Gets the updated_account_status of this AccountUpdaterResponse.  # noqa: E501

        Status of the updated account. An account may have closed (C), the expiry date may have changed (E), the account may have changed (A), or the cardholder should be contacted (Q).  # noqa: E501

        :return: The updated_account_status of this AccountUpdaterResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_account_status

    @updated_account_status.setter
    def updated_account_status(self, updated_account_status):
        """Sets the updated_account_status of this AccountUpdaterResponse.

        Status of the updated account. An account may have closed (C), the expiry date may have changed (E), the account may have changed (A), or the cardholder should be contacted (Q).  # noqa: E501

        :param updated_account_status: The updated_account_status of this AccountUpdaterResponse.  # noqa: E501
        :type: str
        """

        self._updated_account_status = updated_account_status

    @property
    def updated_account_error_code(self):
        """Gets the updated_account_error_code of this AccountUpdaterResponse.  # noqa: E501

        Code for the error encountered when updating account.  # noqa: E501

        :return: The updated_account_error_code of this AccountUpdaterResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_account_error_code

    @updated_account_error_code.setter
    def updated_account_error_code(self, updated_account_error_code):
        """Sets the updated_account_error_code of this AccountUpdaterResponse.

        Code for the error encountered when updating account.  # noqa: E501

        :param updated_account_error_code: The updated_account_error_code of this AccountUpdaterResponse.  # noqa: E501
        :type: str
        """

        self._updated_account_error_code = updated_account_error_code

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
        if not isinstance(other, AccountUpdaterResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountUpdaterResponse):
            return True

        return self.to_dict() != other.to_dict()
