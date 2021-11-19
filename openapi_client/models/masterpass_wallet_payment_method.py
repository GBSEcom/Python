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


class MasterpassWalletPaymentMethod(object):
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
        'wallet_id': 'str',
        'payment_card': 'PaymentCard'
    }

    attribute_map = {
        'wallet_type': 'walletType',
        'wallet_id': 'walletId',
        'payment_card': 'paymentCard'
    }

    def __init__(self, wallet_type=None, wallet_id=None, payment_card=None):  # noqa: E501
        """MasterpassWalletPaymentMethod - a model defined in OpenAPI"""  # noqa: E501

        self._wallet_type = None
        self._wallet_id = None
        self._payment_card = None
        self.discriminator = None

        self.wallet_type = wallet_type
        self.wallet_id = wallet_id
        self.payment_card = payment_card

    @property
    def wallet_type(self):
        """Gets the wallet_type of this MasterpassWalletPaymentMethod.  # noqa: E501

        Type of wallet.  # noqa: E501

        :return: The wallet_type of this MasterpassWalletPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._wallet_type

    @wallet_type.setter
    def wallet_type(self, wallet_type):
        """Sets the wallet_type of this MasterpassWalletPaymentMethod.

        Type of wallet.  # noqa: E501

        :param wallet_type: The wallet_type of this MasterpassWalletPaymentMethod.  # noqa: E501
        :type: str
        """
        if wallet_type is None:
            raise ValueError("Invalid value for `wallet_type`, must not be `None`")  # noqa: E501

        self._wallet_type = wallet_type

    @property
    def wallet_id(self):
        """Gets the wallet_id of this MasterpassWalletPaymentMethod.  # noqa: E501

        Masterpass Wallet ID.  # noqa: E501

        :return: The wallet_id of this MasterpassWalletPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this MasterpassWalletPaymentMethod.

        Masterpass Wallet ID.  # noqa: E501

        :param wallet_id: The wallet_id of this MasterpassWalletPaymentMethod.  # noqa: E501
        :type: str
        """
        if wallet_id is None:
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501
        if wallet_id is not None and len(wallet_id) > 3:
            raise ValueError("Invalid value for `wallet_id`, length must be less than or equal to `3`")  # noqa: E501
        if wallet_id is not None and not re.search(r'^\S$|^\S.*\S$', wallet_id):  # noqa: E501
            raise ValueError(r"Invalid value for `wallet_id`, must be a follow pattern or equal to `/^\S$|^\S.*\S$/`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def payment_card(self):
        """Gets the payment_card of this MasterpassWalletPaymentMethod.  # noqa: E501


        :return: The payment_card of this MasterpassWalletPaymentMethod.  # noqa: E501
        :rtype: PaymentCard
        """
        return self._payment_card

    @payment_card.setter
    def payment_card(self, payment_card):
        """Sets the payment_card of this MasterpassWalletPaymentMethod.


        :param payment_card: The payment_card of this MasterpassWalletPaymentMethod.  # noqa: E501
        :type: PaymentCard
        """
        if payment_card is None:
            raise ValueError("Invalid value for `payment_card`, must not be `None`")  # noqa: E501

        self._payment_card = payment_card

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
        if not isinstance(other, MasterpassWalletPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
