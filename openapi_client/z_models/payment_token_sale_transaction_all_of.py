# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.13.0.20200810.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaymentTokenSaleTransactionAllOf(object):
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
        'payment_method': 'PaymentTokenPaymentMethod',
        'stored_credentials': 'StoredCredential',
        'settlement_split': 'list[SubMerchantSplit]',
        'currency_conversion': 'CurrencyConversion',
        'authentication_request': 'AuthenticationRequest',
        'authentication_result': 'AuthenticationResult',
    }

    attribute_map = {
        'payment_method': 'paymentMethod',  # noqa: E501
        'stored_credentials': 'storedCredentials',  # noqa: E501
        'settlement_split': 'settlementSplit',  # noqa: E501
        'currency_conversion': 'currencyConversion',  # noqa: E501
        'authentication_request': 'authenticationRequest',  # noqa: E501
        'authentication_result': 'authenticationResult',  # noqa: E501
    }

    def __init__(self, payment_method, stored_credentials=None, settlement_split=None, currency_conversion=None, authentication_request=None, authentication_result=None):  # noqa: E501
        """PaymentTokenSaleTransactionAllOf - a model defined in OpenAPI

        Args:
            payment_method (PaymentTokenPaymentMethod):

        Keyword Args:  # noqa: E501
            stored_credentials (StoredCredential): [optional]  # noqa: E501
            settlement_split (list[SubMerchantSplit]): Settle with multiple sub-merchants, sale and preAuth only.. [optional]  # noqa: E501
            currency_conversion (CurrencyConversion): [optional]  # noqa: E501
            authentication_request (AuthenticationRequest): [optional]  # noqa: E501
            authentication_result (AuthenticationResult): [optional]  # noqa: E501
        """

        self._payment_method = None
        self._stored_credentials = None
        self._settlement_split = None
        self._currency_conversion = None
        self._authentication_request = None
        self._authentication_result = None
        self.discriminator = None

        self.payment_method = payment_method
        if stored_credentials is not None:
            self.stored_credentials = stored_credentials  # noqa: E501
        if settlement_split is not None:
            self.settlement_split = settlement_split  # noqa: E501
        if currency_conversion is not None:
            self.currency_conversion = currency_conversion  # noqa: E501
        if authentication_request is not None:
            self.authentication_request = authentication_request  # noqa: E501
        if authentication_result is not None:
            self.authentication_result = authentication_result  # noqa: E501

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentTokenSaleTransactionAllOf.  # noqa: E501


        :return: The payment_method of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :rtype: PaymentTokenPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(
            self,
            payment_method):
        """Sets the payment_method of this PaymentTokenSaleTransactionAllOf.


        :param payment_method: The payment_method of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :type: PaymentTokenPaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = (
            payment_method)

    @property
    def stored_credentials(self):
        """Gets the stored_credentials of this PaymentTokenSaleTransactionAllOf.  # noqa: E501


        :return: The stored_credentials of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :rtype: StoredCredential
        """
        return self._stored_credentials

    @stored_credentials.setter
    def stored_credentials(
            self,
            stored_credentials):
        """Sets the stored_credentials of this PaymentTokenSaleTransactionAllOf.


        :param stored_credentials: The stored_credentials of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :type: StoredCredential
        """

        self._stored_credentials = (
            stored_credentials)

    @property
    def settlement_split(self):
        """Gets the settlement_split of this PaymentTokenSaleTransactionAllOf.  # noqa: E501

        Settle with multiple sub-merchants, sale and preAuth only.  # noqa: E501

        :return: The settlement_split of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :rtype: list[SubMerchantSplit]
        """
        return self._settlement_split

    @settlement_split.setter
    def settlement_split(
            self,
            settlement_split):
        """Sets the settlement_split of this PaymentTokenSaleTransactionAllOf.

        Settle with multiple sub-merchants, sale and preAuth only.  # noqa: E501

        :param settlement_split: The settlement_split of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :type: list[SubMerchantSplit]
        """

        self._settlement_split = (
            settlement_split)

    @property
    def currency_conversion(self):
        """Gets the currency_conversion of this PaymentTokenSaleTransactionAllOf.  # noqa: E501


        :return: The currency_conversion of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :rtype: CurrencyConversion
        """
        return self._currency_conversion

    @currency_conversion.setter
    def currency_conversion(
            self,
            currency_conversion):
        """Sets the currency_conversion of this PaymentTokenSaleTransactionAllOf.


        :param currency_conversion: The currency_conversion of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :type: CurrencyConversion
        """

        self._currency_conversion = (
            currency_conversion)

    @property
    def authentication_request(self):
        """Gets the authentication_request of this PaymentTokenSaleTransactionAllOf.  # noqa: E501


        :return: The authentication_request of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :rtype: AuthenticationRequest
        """
        return self._authentication_request

    @authentication_request.setter
    def authentication_request(
            self,
            authentication_request):
        """Sets the authentication_request of this PaymentTokenSaleTransactionAllOf.


        :param authentication_request: The authentication_request of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :type: AuthenticationRequest
        """

        self._authentication_request = (
            authentication_request)

    @property
    def authentication_result(self):
        """Gets the authentication_result of this PaymentTokenSaleTransactionAllOf.  # noqa: E501


        :return: The authentication_result of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :rtype: AuthenticationResult
        """
        return self._authentication_result

    @authentication_result.setter
    def authentication_result(
            self,
            authentication_result):
        """Sets the authentication_result of this PaymentTokenSaleTransactionAllOf.


        :param authentication_result: The authentication_result of this PaymentTokenSaleTransactionAllOf.  # noqa: E501
        :type: AuthenticationResult
        """

        self._authentication_result = (
            authentication_result)

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
        if not isinstance(other, PaymentTokenSaleTransactionAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other