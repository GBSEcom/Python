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


class PaymentCardForcedTicketTransactionAllOf(object):
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
        'transaction_amount': 'Amount',
        'store_id': 'str',
        'merchant_transaction_id': 'str',
        'transaction_origin': 'TransactionOrigin',
        'order': 'Order',
        'payment_method': 'PaymentCardPaymentMethod',
        'reference_number': 'str'
    }

    attribute_map = {
        'request_type': 'requestType',
        'transaction_amount': 'transactionAmount',
        'store_id': 'storeId',
        'merchant_transaction_id': 'merchantTransactionId',
        'transaction_origin': 'transactionOrigin',
        'order': 'order',
        'payment_method': 'paymentMethod',
        'reference_number': 'referenceNumber'
    }

    def __init__(self, request_type=None, transaction_amount=None, store_id=None, merchant_transaction_id=None, transaction_origin=None, order=None, payment_method=None, reference_number=None):  # noqa: E501
        """PaymentCardForcedTicketTransactionAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._request_type = None
        self._transaction_amount = None
        self._store_id = None
        self._merchant_transaction_id = None
        self._transaction_origin = None
        self._order = None
        self._payment_method = None
        self._reference_number = None
        self.discriminator = None

        if request_type is not None:
            self.request_type = request_type
        if transaction_amount is not None:
            self.transaction_amount = transaction_amount
        if store_id is not None:
            self.store_id = store_id
        if merchant_transaction_id is not None:
            self.merchant_transaction_id = merchant_transaction_id
        if transaction_origin is not None:
            self.transaction_origin = transaction_origin
        if order is not None:
            self.order = order
        self.payment_method = payment_method
        self.reference_number = reference_number

    @property
    def request_type(self):
        """Gets the request_type of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501

        Object name of the primary transaction request.  # noqa: E501

        :return: The request_type of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this PaymentCardForcedTicketTransactionAllOf.

        Object name of the primary transaction request.  # noqa: E501

        :param request_type: The request_type of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :type: str
        """

        self._request_type = request_type

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501


        :return: The transaction_amount of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :rtype: Amount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this PaymentCardForcedTicketTransactionAllOf.


        :param transaction_amount: The transaction_amount of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :type: Amount
        """

        self._transaction_amount = transaction_amount

    @property
    def store_id(self):
        """Gets the store_id of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :return: The store_id of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this PaymentCardForcedTicketTransactionAllOf.

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :param store_id: The store_id of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def merchant_transaction_id(self):
        """Gets the merchant_transaction_id of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501

        The unique merchant transaction ID from the request header, if supplied.  # noqa: E501

        :return: The merchant_transaction_id of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(self, merchant_transaction_id):
        """Sets the merchant_transaction_id of this PaymentCardForcedTicketTransactionAllOf.

        The unique merchant transaction ID from the request header, if supplied.  # noqa: E501

        :param merchant_transaction_id: The merchant_transaction_id of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :type: str
        """
        if merchant_transaction_id is not None and len(merchant_transaction_id) > 40:
            raise ValueError("Invalid value for `merchant_transaction_id`, length must be less than or equal to `40`")  # noqa: E501

        self._merchant_transaction_id = merchant_transaction_id

    @property
    def transaction_origin(self):
        """Gets the transaction_origin of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501


        :return: The transaction_origin of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :rtype: TransactionOrigin
        """
        return self._transaction_origin

    @transaction_origin.setter
    def transaction_origin(self, transaction_origin):
        """Sets the transaction_origin of this PaymentCardForcedTicketTransactionAllOf.


        :param transaction_origin: The transaction_origin of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :type: TransactionOrigin
        """

        self._transaction_origin = transaction_origin

    @property
    def order(self):
        """Gets the order of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501


        :return: The order of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this PaymentCardForcedTicketTransactionAllOf.


        :param order: The order of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :type: Order
        """

        self._order = order

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501


        :return: The payment_method of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :rtype: PaymentCardPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentCardForcedTicketTransactionAllOf.


        :param payment_method: The payment_method of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :type: PaymentCardPaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def reference_number(self):
        """Gets the reference_number of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501

        Stores the six-digit reference number you have received as the result of a successful external authorization (e.g. by phone). The gateway needs this number for uniquely mapping a ForcedTicket transaction to a previously performed external authorization.  # noqa: E501

        :return: The reference_number of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this PaymentCardForcedTicketTransactionAllOf.

        Stores the six-digit reference number you have received as the result of a successful external authorization (e.g. by phone). The gateway needs this number for uniquely mapping a ForcedTicket transaction to a previously performed external authorization.  # noqa: E501

        :param reference_number: The reference_number of this PaymentCardForcedTicketTransactionAllOf.  # noqa: E501
        :type: str
        """
        if reference_number is None:
            raise ValueError("Invalid value for `reference_number`, must not be `None`")  # noqa: E501
        if reference_number is not None and len(reference_number) > 8:
            raise ValueError("Invalid value for `reference_number`, length must be less than or equal to `8`")  # noqa: E501
        if reference_number is not None and not re.search(r'^(?!\s*$).+', reference_number):  # noqa: E501
            raise ValueError(r"Invalid value for `reference_number`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._reference_number = reference_number

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
        if not isinstance(other, PaymentCardForcedTicketTransactionAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
