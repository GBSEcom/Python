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


class ManagedRedirectRequest(object):
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
        'store_id': 'str',
        'merchant_transaction_id': 'str',
        'transaction_type': 'ManagedRedirectTransactionType',
        'order': 'Order',
        'redirect_attributes': 'RedirectAttributes',
        'payment_method': 'object'
    }

    attribute_map = {
        'transaction_amount': 'transactionAmount',
        'store_id': 'storeId',
        'merchant_transaction_id': 'merchantTransactionId',
        'transaction_type': 'transactionType',
        'order': 'order',
        'redirect_attributes': 'redirectAttributes',
        'payment_method': 'paymentMethod'
    }

    def __init__(self, transaction_amount=None, store_id=None, merchant_transaction_id=None, transaction_type=None, order=None, redirect_attributes=None, payment_method=None):  # noqa: E501
        """ManagedRedirectRequest - a model defined in OpenAPI"""  # noqa: E501

        self._transaction_amount = None
        self._store_id = None
        self._merchant_transaction_id = None
        self._transaction_type = None
        self._order = None
        self._redirect_attributes = None
        self._payment_method = None
        self.discriminator = None

        self.transaction_amount = transaction_amount
        if store_id is not None:
            self.store_id = store_id
        if merchant_transaction_id is not None:
            self.merchant_transaction_id = merchant_transaction_id
        self.transaction_type = transaction_type
        if order is not None:
            self.order = order
        if redirect_attributes is not None:
            self.redirect_attributes = redirect_attributes
        self.payment_method = payment_method

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this ManagedRedirectRequest.  # noqa: E501


        :return: The transaction_amount of this ManagedRedirectRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this ManagedRedirectRequest.


        :param transaction_amount: The transaction_amount of this ManagedRedirectRequest.  # noqa: E501
        :type: Amount
        """
        if transaction_amount is None:
            raise ValueError("Invalid value for `transaction_amount`, must not be `None`")  # noqa: E501

        self._transaction_amount = transaction_amount

    @property
    def store_id(self):
        """Gets the store_id of this ManagedRedirectRequest.  # noqa: E501

        An optional Outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :return: The store_id of this ManagedRedirectRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this ManagedRedirectRequest.

        An optional Outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :param store_id: The store_id of this ManagedRedirectRequest.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def merchant_transaction_id(self):
        """Gets the merchant_transaction_id of this ManagedRedirectRequest.  # noqa: E501

        The unique merchant transaction ID from the request, if supplied.  # noqa: E501

        :return: The merchant_transaction_id of this ManagedRedirectRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(self, merchant_transaction_id):
        """Sets the merchant_transaction_id of this ManagedRedirectRequest.

        The unique merchant transaction ID from the request, if supplied.  # noqa: E501

        :param merchant_transaction_id: The merchant_transaction_id of this ManagedRedirectRequest.  # noqa: E501
        :type: str
        """
        if merchant_transaction_id is not None and len(merchant_transaction_id) > 40:
            raise ValueError("Invalid value for `merchant_transaction_id`, length must be less than or equal to `40`")  # noqa: E501

        self._merchant_transaction_id = merchant_transaction_id

    @property
    def transaction_type(self):
        """Gets the transaction_type of this ManagedRedirectRequest.  # noqa: E501


        :return: The transaction_type of this ManagedRedirectRequest.  # noqa: E501
        :rtype: ManagedRedirectTransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this ManagedRedirectRequest.


        :param transaction_type: The transaction_type of this ManagedRedirectRequest.  # noqa: E501
        :type: ManagedRedirectTransactionType
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def order(self):
        """Gets the order of this ManagedRedirectRequest.  # noqa: E501


        :return: The order of this ManagedRedirectRequest.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ManagedRedirectRequest.


        :param order: The order of this ManagedRedirectRequest.  # noqa: E501
        :type: Order
        """

        self._order = order

    @property
    def redirect_attributes(self):
        """Gets the redirect_attributes of this ManagedRedirectRequest.  # noqa: E501


        :return: The redirect_attributes of this ManagedRedirectRequest.  # noqa: E501
        :rtype: RedirectAttributes
        """
        return self._redirect_attributes

    @redirect_attributes.setter
    def redirect_attributes(self, redirect_attributes):
        """Sets the redirect_attributes of this ManagedRedirectRequest.


        :param redirect_attributes: The redirect_attributes of this ManagedRedirectRequest.  # noqa: E501
        :type: RedirectAttributes
        """

        self._redirect_attributes = redirect_attributes

    @property
    def payment_method(self):
        """Gets the payment_method of this ManagedRedirectRequest.  # noqa: E501

        Various payment methods the Gateway supports. Abstract class, do not use this class directly, use one of its children.  # noqa: E501

        :return: The payment_method of this ManagedRedirectRequest.  # noqa: E501
        :rtype: object
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this ManagedRedirectRequest.

        Various payment methods the Gateway supports. Abstract class, do not use this class directly, use one of its children.  # noqa: E501

        :param payment_method: The payment_method of this ManagedRedirectRequest.  # noqa: E501
        :type: object
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

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
        if not isinstance(other, ManagedRedirectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
