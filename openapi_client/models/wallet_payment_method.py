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


class WalletPaymentMethod(object):
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
        'wallet_type': 'str'
    }

    attribute_map = {
        'wallet_type': 'walletType'
    }

    discriminator_value_class_map = {
        'DecryptedGooglePayWalletPaymentMethod': 'DecryptedGooglePayWalletPaymentMethod',
        'DecryptedSamsungPayWalletPaymentMethod': 'DecryptedSamsungPayWalletPaymentMethod',
        'EncryptedGooglePayWalletPaymentMethod': 'EncryptedGooglePayWalletPaymentMethod',
        'MasterpassWalletPaymentMethod': 'MasterpassWalletPaymentMethod',
        'DecryptedApplePayWalletPaymentMethod': 'DecryptedApplePayWalletPaymentMethod',
        'EncryptedApplePayWalletPaymentMethod': 'EncryptedApplePayWalletPaymentMethod',
        'EncryptedSamsungPayWalletPaymentMethod': 'EncryptedSamsungPayWalletPaymentMethod'
    }

    def __init__(self, wallet_type=None):  # noqa: E501
        """WalletPaymentMethod - a model defined in OpenAPI"""  # noqa: E501

        self._wallet_type = None
        self.discriminator = 'wallet_type'

        self.wallet_type = wallet_type

    @property
    def wallet_type(self):
        """Gets the wallet_type of this WalletPaymentMethod.  # noqa: E501

        Type of wallet.  # noqa: E501

        :return: The wallet_type of this WalletPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._wallet_type

    @wallet_type.setter
    def wallet_type(self, wallet_type):
        """Sets the wallet_type of this WalletPaymentMethod.

        Type of wallet.  # noqa: E501

        :param wallet_type: The wallet_type of this WalletPaymentMethod.  # noqa: E501
        :type: str
        """
        if wallet_type is None:
            raise ValueError("Invalid value for `wallet_type`, must not be `None`")  # noqa: E501

        self._wallet_type = wallet_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, WalletPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
