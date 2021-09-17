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


class AchPostAuthTransaction(object):
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
        'merchant_transaction_id': 'str',
        'comments': 'str',
        'order': 'Order',
        'transaction_amount': 'Amount'
    }

    attribute_map = {
        'request_type': 'requestType',
        'store_id': 'storeId',
        'merchant_transaction_id': 'merchantTransactionId',
        'comments': 'comments',
        'order': 'order',
        'transaction_amount': 'transactionAmount'
    }

    def __init__(self, request_type=None, store_id=None, merchant_transaction_id=None, comments=None, order=None, transaction_amount=None):  # noqa: E501
        """AchPostAuthTransaction - a model defined in OpenAPI"""  # noqa: E501

        self._request_type = None
        self._store_id = None
        self._merchant_transaction_id = None
        self._comments = None
        self._order = None
        self._transaction_amount = None
        self.discriminator = None

        self.request_type = request_type
        if store_id is not None:
            self.store_id = store_id
        if merchant_transaction_id is not None:
            self.merchant_transaction_id = merchant_transaction_id
        if comments is not None:
            self.comments = comments
        if order is not None:
            self.order = order
        self.transaction_amount = transaction_amount

    @property
    def request_type(self):
        """Gets the request_type of this AchPostAuthTransaction.  # noqa: E501

        Object name of the secondary transaction request.  # noqa: E501

        :return: The request_type of this AchPostAuthTransaction.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this AchPostAuthTransaction.

        Object name of the secondary transaction request.  # noqa: E501

        :param request_type: The request_type of this AchPostAuthTransaction.  # noqa: E501
        :type: str
        """
        if request_type is None:
            raise ValueError("Invalid value for `request_type`, must not be `None`")  # noqa: E501

        self._request_type = request_type

    @property
    def store_id(self):
        """Gets the store_id of this AchPostAuthTransaction.  # noqa: E501

        An optional outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :return: The store_id of this AchPostAuthTransaction.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this AchPostAuthTransaction.

        An optional outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :param store_id: The store_id of this AchPostAuthTransaction.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def merchant_transaction_id(self):
        """Gets the merchant_transaction_id of this AchPostAuthTransaction.  # noqa: E501

        The unique merchant transaction ID from the request, if supplied.  # noqa: E501

        :return: The merchant_transaction_id of this AchPostAuthTransaction.  # noqa: E501
        :rtype: str
        """
        return self._merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(self, merchant_transaction_id):
        """Sets the merchant_transaction_id of this AchPostAuthTransaction.

        The unique merchant transaction ID from the request, if supplied.  # noqa: E501

        :param merchant_transaction_id: The merchant_transaction_id of this AchPostAuthTransaction.  # noqa: E501
        :type: str
        """
        if merchant_transaction_id is not None and len(merchant_transaction_id) > 40:
            raise ValueError("Invalid value for `merchant_transaction_id`, length must be less than or equal to `40`")  # noqa: E501

        self._merchant_transaction_id = merchant_transaction_id

    @property
    def comments(self):
        """Gets the comments of this AchPostAuthTransaction.  # noqa: E501

        Comment for the secondary transaction.  # noqa: E501

        :return: The comments of this AchPostAuthTransaction.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this AchPostAuthTransaction.

        Comment for the secondary transaction.  # noqa: E501

        :param comments: The comments of this AchPostAuthTransaction.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def order(self):
        """Gets the order of this AchPostAuthTransaction.  # noqa: E501


        :return: The order of this AchPostAuthTransaction.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this AchPostAuthTransaction.


        :param order: The order of this AchPostAuthTransaction.  # noqa: E501
        :type: Order
        """

        self._order = order

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this AchPostAuthTransaction.  # noqa: E501


        :return: The transaction_amount of this AchPostAuthTransaction.  # noqa: E501
        :rtype: Amount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this AchPostAuthTransaction.


        :param transaction_amount: The transaction_amount of this AchPostAuthTransaction.  # noqa: E501
        :type: Amount
        """
        if transaction_amount is None:
            raise ValueError("Invalid value for `transaction_amount`, must not be `None`")  # noqa: E501

        self._transaction_amount = transaction_amount

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
        if not isinstance(other, AchPostAuthTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
