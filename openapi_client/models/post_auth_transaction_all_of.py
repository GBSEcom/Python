# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.9.1.20191223.002
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
        'request_type': 'str',
        'store_id': 'str',
        'comments': 'str',
        'transaction_amount': 'Amount',
        'transaction_origin': 'TransactionOrigin',
        'split_shipment': 'SplitShipment',
        'soft_descriptor': 'SoftDescriptor'
    }

    attribute_map = {
        'request_type': 'requestType',
        'store_id': 'storeId',
        'comments': 'comments',
        'transaction_amount': 'transactionAmount',
        'transaction_origin': 'transactionOrigin',
        'split_shipment': 'splitShipment',
        'soft_descriptor': 'softDescriptor'
    }

    def __init__(self, request_type=None, store_id=None, comments=None, transaction_amount=None, transaction_origin=None, split_shipment=None, soft_descriptor=None):  # noqa: E501
        """PostAuthTransactionAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._request_type = None
        self._store_id = None
        self._comments = None
        self._transaction_amount = None
        self._transaction_origin = None
        self._split_shipment = None
        self._soft_descriptor = None
        self.discriminator = None

        if request_type is not None:
            self.request_type = request_type
        if store_id is not None:
            self.store_id = store_id
        if comments is not None:
            self.comments = comments
        self.transaction_amount = transaction_amount
        if transaction_origin is not None:
            self.transaction_origin = transaction_origin
        if split_shipment is not None:
            self.split_shipment = split_shipment
        if soft_descriptor is not None:
            self.soft_descriptor = soft_descriptor

    @property
    def request_type(self):
        """Gets the request_type of this PostAuthTransactionAllOf.  # noqa: E501

        Object name of the secondary transaction request.  # noqa: E501

        :return: The request_type of this PostAuthTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this PostAuthTransactionAllOf.

        Object name of the secondary transaction request.  # noqa: E501

        :param request_type: The request_type of this PostAuthTransactionAllOf.  # noqa: E501
        :type: str
        """

        self._request_type = request_type

    @property
    def store_id(self):
        """Gets the store_id of this PostAuthTransactionAllOf.  # noqa: E501

        An optional outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :return: The store_id of this PostAuthTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this PostAuthTransactionAllOf.

        An optional outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :param store_id: The store_id of this PostAuthTransactionAllOf.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def comments(self):
        """Gets the comments of this PostAuthTransactionAllOf.  # noqa: E501

        Comment for the secondary transaction.  # noqa: E501

        :return: The comments of this PostAuthTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this PostAuthTransactionAllOf.

        Comment for the secondary transaction.  # noqa: E501

        :param comments: The comments of this PostAuthTransactionAllOf.  # noqa: E501
        :type: str
        """

        self._comments = comments

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
