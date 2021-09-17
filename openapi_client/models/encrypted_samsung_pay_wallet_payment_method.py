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


class EncryptedSamsungPayWalletPaymentMethod(object):
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
        'wallet_type': 'str',
        'encrypted_samsung_pay': 'EncryptedSamsungPay'
    }

    attribute_map = {
        'wallet_type': 'walletType',
        'encrypted_samsung_pay': 'encryptedSamsungPay'
    }

    def __init__(self, wallet_type=None, encrypted_samsung_pay=None):  # noqa: E501
        """EncryptedSamsungPayWalletPaymentMethod - a model defined in OpenAPI"""  # noqa: E501

        self._wallet_type = None
        self._encrypted_samsung_pay = None
        self.discriminator = None

        self.wallet_type = wallet_type
        self.encrypted_samsung_pay = encrypted_samsung_pay

    @property
    def wallet_type(self):
        """Gets the wallet_type of this EncryptedSamsungPayWalletPaymentMethod.  # noqa: E501

        Type of wallet.  # noqa: E501

        :return: The wallet_type of this EncryptedSamsungPayWalletPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._wallet_type

    @wallet_type.setter
    def wallet_type(self, wallet_type):
        """Sets the wallet_type of this EncryptedSamsungPayWalletPaymentMethod.

        Type of wallet.  # noqa: E501

        :param wallet_type: The wallet_type of this EncryptedSamsungPayWalletPaymentMethod.  # noqa: E501
        :type: str
        """
        if wallet_type is None:
            raise ValueError("Invalid value for `wallet_type`, must not be `None`")  # noqa: E501

        self._wallet_type = wallet_type

    @property
    def encrypted_samsung_pay(self):
        """Gets the encrypted_samsung_pay of this EncryptedSamsungPayWalletPaymentMethod.  # noqa: E501


        :return: The encrypted_samsung_pay of this EncryptedSamsungPayWalletPaymentMethod.  # noqa: E501
        :rtype: EncryptedSamsungPay
        """
        return self._encrypted_samsung_pay

    @encrypted_samsung_pay.setter
    def encrypted_samsung_pay(self, encrypted_samsung_pay):
        """Sets the encrypted_samsung_pay of this EncryptedSamsungPayWalletPaymentMethod.


        :param encrypted_samsung_pay: The encrypted_samsung_pay of this EncryptedSamsungPayWalletPaymentMethod.  # noqa: E501
        :type: EncryptedSamsungPay
        """
        if encrypted_samsung_pay is None:
            raise ValueError("Invalid value for `encrypted_samsung_pay`, must not be `None`")  # noqa: E501

        self._encrypted_samsung_pay = encrypted_samsung_pay

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
        if not isinstance(other, EncryptedSamsungPayWalletPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
