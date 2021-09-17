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


class PostAuthTransactionAllOf(object):
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
        'transaction_amount': 'Amount',
        'transaction_origin': 'TransactionOrigin',
        'split_shipment': 'SplitShipment',
        'soft_descriptor': 'SoftDescriptor'
    }

    attribute_map = {
        'transaction_amount': 'transactionAmount',
        'transaction_origin': 'transactionOrigin',
        'split_shipment': 'splitShipment',
        'soft_descriptor': 'softDescriptor'
    }

    def __init__(self, transaction_amount=None, transaction_origin=None, split_shipment=None, soft_descriptor=None):  # noqa: E501
        """PostAuthTransactionAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._transaction_amount = None
        self._transaction_origin = None
        self._split_shipment = None
        self._soft_descriptor = None
        self.discriminator = None

        self.transaction_amount = transaction_amount
        if transaction_origin is not None:
            self.transaction_origin = transaction_origin
        if split_shipment is not None:
            self.split_shipment = split_shipment
        if soft_descriptor is not None:
            self.soft_descriptor = soft_descriptor

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this PostAuthTransactionAllOf.  # noqa: E501


        :return: The transaction_amount of this PostAuthTransactionAllOf.  # noqa: E501
        :rtype: Amount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this PostAuthTransactionAllOf.


        :param transaction_amount: The transaction_amount of this PostAuthTransactionAllOf.  # noqa: E501
        :type: Amount
        """
        if transaction_amount is None:
            raise ValueError("Invalid value for `transaction_amount`, must not be `None`")  # noqa: E501

        self._transaction_amount = transaction_amount

    @property
    def transaction_origin(self):
        """Gets the transaction_origin of this PostAuthTransactionAllOf.  # noqa: E501


        :return: The transaction_origin of this PostAuthTransactionAllOf.  # noqa: E501
        :rtype: TransactionOrigin
        """
        return self._transaction_origin

    @transaction_origin.setter
    def transaction_origin(self, transaction_origin):
        """Sets the transaction_origin of this PostAuthTransactionAllOf.


        :param transaction_origin: The transaction_origin of this PostAuthTransactionAllOf.  # noqa: E501
        :type: TransactionOrigin
        """

        self._transaction_origin = transaction_origin

    @property
    def split_shipment(self):
        """Gets the split_shipment of this PostAuthTransactionAllOf.  # noqa: E501


        :return: The split_shipment of this PostAuthTransactionAllOf.  # noqa: E501
        :rtype: SplitShipment
        """
        return self._split_shipment

    @split_shipment.setter
    def split_shipment(self, split_shipment):
        """Sets the split_shipment of this PostAuthTransactionAllOf.


        :param split_shipment: The split_shipment of this PostAuthTransactionAllOf.  # noqa: E501
        :type: SplitShipment
        """

        self._split_shipment = split_shipment

    @property
    def soft_descriptor(self):
        """Gets the soft_descriptor of this PostAuthTransactionAllOf.  # noqa: E501


        :return: The soft_descriptor of this PostAuthTransactionAllOf.  # noqa: E501
        :rtype: SoftDescriptor
        """
        return self._soft_descriptor

    @soft_descriptor.setter
    def soft_descriptor(self, soft_descriptor):
        """Sets the soft_descriptor of this PostAuthTransactionAllOf.


        :param soft_descriptor: The soft_descriptor of this PostAuthTransactionAllOf.  # noqa: E501
        :type: SoftDescriptor
        """

        self._soft_descriptor = soft_descriptor

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
        if not isinstance(other, PostAuthTransactionAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
