# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.3.0.20210608.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaymentMethodPaymentSchedulesRequest(object):
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
        'start_date': 'date',
        'number_of_payments': 'int',
        'maximum_failures': 'int',
        'invoice_number': 'str',
        'purchase_order_number': 'str',
        'transaction_origin': 'TransactionOrigin',
        'dynamic_merchant_name': 'str',
        'frequency': 'Frequency',
        'transaction_amount': 'Amount',
        'client_locale': 'ClientLocale',
        'order_id': 'str',
        'billing': 'Billing',
        'shipping': 'Shipping',
        'comments': 'str',
        'payment_method': 'PaymentCardPaymentMethod'
    }

    attribute_map = {
        'request_type': 'requestType',
        'store_id': 'storeId',
        'start_date': 'startDate',
        'number_of_payments': 'numberOfPayments',
        'maximum_failures': 'maximumFailures',
        'invoice_number': 'invoiceNumber',
        'purchase_order_number': 'purchaseOrderNumber',
        'transaction_origin': 'transactionOrigin',
        'dynamic_merchant_name': 'dynamicMerchantName',
        'frequency': 'frequency',
        'transaction_amount': 'transactionAmount',
        'client_locale': 'clientLocale',
        'order_id': 'orderId',
        'billing': 'billing',
        'shipping': 'shipping',
        'comments': 'comments',
        'payment_method': 'paymentMethod'
    }

    def __init__(self, request_type=None, store_id=None, start_date=None, number_of_payments=None, maximum_failures=None, invoice_number=None, purchase_order_number=None, transaction_origin=None, dynamic_merchant_name=None, frequency=None, transaction_amount=None, client_locale=None, order_id=None, billing=None, shipping=None, comments=None, payment_method=None):  # noqa: E501
        """PaymentMethodPaymentSchedulesRequest - a model defined in OpenAPI"""  # noqa: E501

        self._request_type = None
        self._store_id = None
        self._start_date = None
        self._number_of_payments = None
        self._maximum_failures = None
        self._invoice_number = None
        self._purchase_order_number = None
        self._transaction_origin = None
        self._dynamic_merchant_name = None
        self._frequency = None
        self._transaction_amount = None
        self._client_locale = None
        self._order_id = None
        self._billing = None
        self._shipping = None
        self._comments = None
        self._payment_method = None
        self.discriminator = None

        self.request_type = request_type
        if store_id is not None:
            self.store_id = store_id
        self.start_date = start_date
        if number_of_payments is not None:
            self.number_of_payments = number_of_payments
        if maximum_failures is not None:
            self.maximum_failures = maximum_failures
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if transaction_origin is not None:
            self.transaction_origin = transaction_origin
        if dynamic_merchant_name is not None:
            self.dynamic_merchant_name = dynamic_merchant_name
        self.frequency = frequency
        self.transaction_amount = transaction_amount
        if client_locale is not None:
            self.client_locale = client_locale
        if order_id is not None:
            self.order_id = order_id
        if billing is not None:
            self.billing = billing
        if shipping is not None:
            self.shipping = shipping
        if comments is not None:
            self.comments = comments
        self.payment_method = payment_method

    @property
    def request_type(self):
        """Gets the request_type of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501

        Object name of the payment schedules request.  # noqa: E501

        :return: The request_type of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this PaymentMethodPaymentSchedulesRequest.

        Object name of the payment schedules request.  # noqa: E501

        :param request_type: The request_type of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: str
        """
        if request_type is None:
            raise ValueError("Invalid value for `request_type`, must not be `None`")  # noqa: E501

        self._request_type = request_type

    @property
    def store_id(self):
        """Gets the store_id of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501

        Store ID number.  # noqa: E501

        :return: The store_id of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this PaymentMethodPaymentSchedulesRequest.

        Store ID number.  # noqa: E501

        :param store_id: The store_id of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def start_date(self):
        """Gets the start_date of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501

        Date of mandate signature.  # noqa: E501

        :return: The start_date of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PaymentMethodPaymentSchedulesRequest.

        Date of mandate signature.  # noqa: E501

        :param start_date: The start_date of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def number_of_payments(self):
        """Gets the number_of_payments of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501

        Number of times the recurring payment will process.  # noqa: E501

        :return: The number_of_payments of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: int
        """
        return self._number_of_payments

    @number_of_payments.setter
    def number_of_payments(self, number_of_payments):
        """Sets the number_of_payments of this PaymentMethodPaymentSchedulesRequest.

        Number of times the recurring payment will process.  # noqa: E501

        :param number_of_payments: The number_of_payments of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: int
        """
        if number_of_payments is not None and number_of_payments > 999:  # noqa: E501
            raise ValueError("Invalid value for `number_of_payments`, must be a value less than or equal to `999`")  # noqa: E501
        if number_of_payments is not None and number_of_payments < 1:  # noqa: E501
            raise ValueError("Invalid value for `number_of_payments`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_payments = number_of_payments

    @property
    def maximum_failures(self):
        """Gets the maximum_failures of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501

        Number of failures that can be encountered before re-tries cease.  # noqa: E501

        :return: The maximum_failures of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: int
        """
        return self._maximum_failures

    @maximum_failures.setter
    def maximum_failures(self, maximum_failures):
        """Sets the maximum_failures of this PaymentMethodPaymentSchedulesRequest.

        Number of failures that can be encountered before re-tries cease.  # noqa: E501

        :param maximum_failures: The maximum_failures of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: int
        """
        if maximum_failures is not None and maximum_failures > 999:  # noqa: E501
            raise ValueError("Invalid value for `maximum_failures`, must be a value less than or equal to `999`")  # noqa: E501
        if maximum_failures is not None and maximum_failures < 1:  # noqa: E501
            raise ValueError("Invalid value for `maximum_failures`, must be a value greater than or equal to `1`")  # noqa: E501

        self._maximum_failures = maximum_failures

    @property
    def invoice_number(self):
        """Gets the invoice_number of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501

        Invoice number.  # noqa: E501

        :return: The invoice_number of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this PaymentMethodPaymentSchedulesRequest.

        Invoice number.  # noqa: E501

        :param invoice_number: The invoice_number of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501

        Purchase order number.  # noqa: E501

        :return: The purchase_order_number of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this PaymentMethodPaymentSchedulesRequest.

        Purchase order number.  # noqa: E501

        :param purchase_order_number: The purchase_order_number of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def transaction_origin(self):
        """Gets the transaction_origin of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501


        :return: The transaction_origin of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: TransactionOrigin
        """
        return self._transaction_origin

    @transaction_origin.setter
    def transaction_origin(self, transaction_origin):
        """Sets the transaction_origin of this PaymentMethodPaymentSchedulesRequest.


        :param transaction_origin: The transaction_origin of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: TransactionOrigin
        """

        self._transaction_origin = transaction_origin

    @property
    def dynamic_merchant_name(self):
        """Gets the dynamic_merchant_name of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501

        Dynamic merchant name for the cardholder's statement.  # noqa: E501

        :return: The dynamic_merchant_name of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_merchant_name

    @dynamic_merchant_name.setter
    def dynamic_merchant_name(self, dynamic_merchant_name):
        """Sets the dynamic_merchant_name of this PaymentMethodPaymentSchedulesRequest.

        Dynamic merchant name for the cardholder's statement.  # noqa: E501

        :param dynamic_merchant_name: The dynamic_merchant_name of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._dynamic_merchant_name = dynamic_merchant_name

    @property
    def frequency(self):
        """Gets the frequency of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501


        :return: The frequency of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: Frequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this PaymentMethodPaymentSchedulesRequest.


        :param frequency: The frequency of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: Frequency
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501

        self._frequency = frequency

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501


        :return: The transaction_amount of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this PaymentMethodPaymentSchedulesRequest.


        :param transaction_amount: The transaction_amount of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: Amount
        """
        if transaction_amount is None:
            raise ValueError("Invalid value for `transaction_amount`, must not be `None`")  # noqa: E501

        self._transaction_amount = transaction_amount

    @property
    def client_locale(self):
        """Gets the client_locale of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501


        :return: The client_locale of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: ClientLocale
        """
        return self._client_locale

    @client_locale.setter
    def client_locale(self, client_locale):
        """Sets the client_locale of this PaymentMethodPaymentSchedulesRequest.


        :param client_locale: The client_locale of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: ClientLocale
        """

        self._client_locale = client_locale

    @property
    def order_id(self):
        """Gets the order_id of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501

        Note - Client Order ID if supplied by client. If not supplied by client, IPG will generate. The first 12 alphanumeric digits are passed down to Fiserv Enterprise reporting tool, Clientline and Data File Manager (DFM).  # noqa: E501

        :return: The order_id of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PaymentMethodPaymentSchedulesRequest.

        Note - Client Order ID if supplied by client. If not supplied by client, IPG will generate. The first 12 alphanumeric digits are passed down to Fiserv Enterprise reporting tool, Clientline and Data File Manager (DFM).  # noqa: E501

        :param order_id: The order_id of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def billing(self):
        """Gets the billing of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501


        :return: The billing of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: Billing
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this PaymentMethodPaymentSchedulesRequest.


        :param billing: The billing of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: Billing
        """

        self._billing = billing

    @property
    def shipping(self):
        """Gets the shipping of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501


        :return: The shipping of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: Shipping
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this PaymentMethodPaymentSchedulesRequest.


        :param shipping: The shipping of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: Shipping
        """

        self._shipping = shipping

    @property
    def comments(self):
        """Gets the comments of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501

        User supplied comments.  # noqa: E501

        :return: The comments of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this PaymentMethodPaymentSchedulesRequest.

        User supplied comments.  # noqa: E501

        :param comments: The comments of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501


        :return: The payment_method of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :rtype: PaymentCardPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentMethodPaymentSchedulesRequest.


        :param payment_method: The payment_method of this PaymentMethodPaymentSchedulesRequest.  # noqa: E501
        :type: PaymentCardPaymentMethod
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
        if not isinstance(other, PaymentMethodPaymentSchedulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
