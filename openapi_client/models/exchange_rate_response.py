# coding: utf-8

"""
    Payment Gateway API Specification.

    Payment Gateway API for payment processing. Version 6.4.0.20181018.001   # noqa: E501

    OpenAPI spec version: 6.4.0.20181018.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ExchangeRateResponse(object):
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
        'response_type': 'ResponseType',
        'client_request_id': 'str',
        'api_trace_id': 'str',
        'ipg_transaction_id': 'str',
        'request_time': 'str',
        'inquiry_rate_id': 'str',
        'foreign_currency_code': 'str',
        'foreign_amount': 'str',
        'exchange_rate': 'str',
        'dcc_offered': 'str',
        'exchange_rate_source_timestamp': 'str',
        'expiration_timestamp': 'str',
        'margin_rate_percentage': 'str',
        'exchange_rate_source_name': 'str'
    }

    attribute_map = {
        'response_type': 'responseType',
        'client_request_id': 'clientRequestId',
        'api_trace_id': 'apiTraceId',
        'ipg_transaction_id': 'ipgTransactionId',
        'request_time': 'requestTime',
        'inquiry_rate_id': 'inquiryRateId',
        'foreign_currency_code': 'foreignCurrencyCode',
        'foreign_amount': 'foreignAmount',
        'exchange_rate': 'exchangeRate',
        'dcc_offered': 'dccOffered',
        'exchange_rate_source_timestamp': 'exchangeRateSourceTimestamp',
        'expiration_timestamp': 'expirationTimestamp',
        'margin_rate_percentage': 'marginRatePercentage',
        'exchange_rate_source_name': 'exchangeRateSourceName'
    }

    def __init__(self, response_type=None, client_request_id=None, api_trace_id=None, ipg_transaction_id=None, request_time=None, inquiry_rate_id=None, foreign_currency_code=None, foreign_amount=None, exchange_rate=None, dcc_offered=None, exchange_rate_source_timestamp=None, expiration_timestamp=None, margin_rate_percentage=None, exchange_rate_source_name=None):  # noqa: E501
        """ExchangeRateResponse - a model defined in OpenAPI"""  # noqa: E501

        self._response_type = None
        self._client_request_id = None
        self._api_trace_id = None
        self._ipg_transaction_id = None
        self._request_time = None
        self._inquiry_rate_id = None
        self._foreign_currency_code = None
        self._foreign_amount = None
        self._exchange_rate = None
        self._dcc_offered = None
        self._exchange_rate_source_timestamp = None
        self._expiration_timestamp = None
        self._margin_rate_percentage = None
        self._exchange_rate_source_name = None
        self.discriminator = None

        if response_type is not None:
            self.response_type = response_type
        if client_request_id is not None:
            self.client_request_id = client_request_id
        if api_trace_id is not None:
            self.api_trace_id = api_trace_id
        if ipg_transaction_id is not None:
            self.ipg_transaction_id = ipg_transaction_id
        if request_time is not None:
            self.request_time = request_time
        if inquiry_rate_id is not None:
            self.inquiry_rate_id = inquiry_rate_id
        if foreign_currency_code is not None:
            self.foreign_currency_code = foreign_currency_code
        if foreign_amount is not None:
            self.foreign_amount = foreign_amount
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if dcc_offered is not None:
            self.dcc_offered = dcc_offered
        if exchange_rate_source_timestamp is not None:
            self.exchange_rate_source_timestamp = exchange_rate_source_timestamp
        if expiration_timestamp is not None:
            self.expiration_timestamp = expiration_timestamp
        if margin_rate_percentage is not None:
            self.margin_rate_percentage = margin_rate_percentage
        if exchange_rate_source_name is not None:
            self.exchange_rate_source_name = exchange_rate_source_name

    @property
    def response_type(self):
        """Gets the response_type of this ExchangeRateResponse.  # noqa: E501


        :return: The response_type of this ExchangeRateResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this ExchangeRateResponse.


        :param response_type: The response_type of this ExchangeRateResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = response_type

    @property
    def client_request_id(self):
        """Gets the client_request_id of this ExchangeRateResponse.  # noqa: E501

        Echoes back the value in the request header  # noqa: E501

        :return: The client_request_id of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this ExchangeRateResponse.

        Echoes back the value in the request header  # noqa: E501

        :param client_request_id: The client_request_id of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = client_request_id

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this ExchangeRateResponse.  # noqa: E501

        Echoes back the value in the request header  # noqa: E501

        :return: The api_trace_id of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(self, api_trace_id):
        """Sets the api_trace_id of this ExchangeRateResponse.

        Echoes back the value in the request header  # noqa: E501

        :param api_trace_id: The api_trace_id of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = api_trace_id

    @property
    def ipg_transaction_id(self):
        """Gets the ipg_transaction_id of this ExchangeRateResponse.  # noqa: E501

        The response transaction ID  # noqa: E501

        :return: The ipg_transaction_id of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._ipg_transaction_id

    @ipg_transaction_id.setter
    def ipg_transaction_id(self, ipg_transaction_id):
        """Sets the ipg_transaction_id of this ExchangeRateResponse.

        The response transaction ID  # noqa: E501

        :param ipg_transaction_id: The ipg_transaction_id of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._ipg_transaction_id = ipg_transaction_id

    @property
    def request_time(self):
        """Gets the request_time of this ExchangeRateResponse.  # noqa: E501

        Time of the request  # noqa: E501

        :return: The request_time of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        """Sets the request_time of this ExchangeRateResponse.

        Time of the request  # noqa: E501

        :param request_time: The request_time of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._request_time = request_time

    @property
    def inquiry_rate_id(self):
        """Gets the inquiry_rate_id of this ExchangeRateResponse.  # noqa: E501

        Inquiry rate ID.  # noqa: E501

        :return: The inquiry_rate_id of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_rate_id

    @inquiry_rate_id.setter
    def inquiry_rate_id(self, inquiry_rate_id):
        """Sets the inquiry_rate_id of this ExchangeRateResponse.

        Inquiry rate ID.  # noqa: E501

        :param inquiry_rate_id: The inquiry_rate_id of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._inquiry_rate_id = inquiry_rate_id

    @property
    def foreign_currency_code(self):
        """Gets the foreign_currency_code of this ExchangeRateResponse.  # noqa: E501

        Foreign currency code  # noqa: E501

        :return: The foreign_currency_code of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._foreign_currency_code

    @foreign_currency_code.setter
    def foreign_currency_code(self, foreign_currency_code):
        """Sets the foreign_currency_code of this ExchangeRateResponse.

        Foreign currency code  # noqa: E501

        :param foreign_currency_code: The foreign_currency_code of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._foreign_currency_code = foreign_currency_code

    @property
    def foreign_amount(self):
        """Gets the foreign_amount of this ExchangeRateResponse.  # noqa: E501

        Foreign amount  # noqa: E501

        :return: The foreign_amount of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._foreign_amount

    @foreign_amount.setter
    def foreign_amount(self, foreign_amount):
        """Sets the foreign_amount of this ExchangeRateResponse.

        Foreign amount  # noqa: E501

        :param foreign_amount: The foreign_amount of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._foreign_amount = foreign_amount

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this ExchangeRateResponse.  # noqa: E501

        Exchange rate  # noqa: E501

        :return: The exchange_rate of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this ExchangeRateResponse.

        Exchange rate  # noqa: E501

        :param exchange_rate: The exchange_rate of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._exchange_rate = exchange_rate

    @property
    def dcc_offered(self):
        """Gets the dcc_offered of this ExchangeRateResponse.  # noqa: E501

        Dcc offered.  # noqa: E501

        :return: The dcc_offered of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._dcc_offered

    @dcc_offered.setter
    def dcc_offered(self, dcc_offered):
        """Sets the dcc_offered of this ExchangeRateResponse.

        Dcc offered.  # noqa: E501

        :param dcc_offered: The dcc_offered of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._dcc_offered = dcc_offered

    @property
    def exchange_rate_source_timestamp(self):
        """Gets the exchange_rate_source_timestamp of this ExchangeRateResponse.  # noqa: E501

        Exchange rate source timestamp  # noqa: E501

        :return: The exchange_rate_source_timestamp of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._exchange_rate_source_timestamp

    @exchange_rate_source_timestamp.setter
    def exchange_rate_source_timestamp(self, exchange_rate_source_timestamp):
        """Sets the exchange_rate_source_timestamp of this ExchangeRateResponse.

        Exchange rate source timestamp  # noqa: E501

        :param exchange_rate_source_timestamp: The exchange_rate_source_timestamp of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._exchange_rate_source_timestamp = exchange_rate_source_timestamp

    @property
    def expiration_timestamp(self):
        """Gets the expiration_timestamp of this ExchangeRateResponse.  # noqa: E501

        Expiration timestamp  # noqa: E501

        :return: The expiration_timestamp of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._expiration_timestamp

    @expiration_timestamp.setter
    def expiration_timestamp(self, expiration_timestamp):
        """Sets the expiration_timestamp of this ExchangeRateResponse.

        Expiration timestamp  # noqa: E501

        :param expiration_timestamp: The expiration_timestamp of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._expiration_timestamp = expiration_timestamp

    @property
    def margin_rate_percentage(self):
        """Gets the margin_rate_percentage of this ExchangeRateResponse.  # noqa: E501

        Margin rate percentage.  # noqa: E501

        :return: The margin_rate_percentage of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._margin_rate_percentage

    @margin_rate_percentage.setter
    def margin_rate_percentage(self, margin_rate_percentage):
        """Sets the margin_rate_percentage of this ExchangeRateResponse.

        Margin rate percentage.  # noqa: E501

        :param margin_rate_percentage: The margin_rate_percentage of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._margin_rate_percentage = margin_rate_percentage

    @property
    def exchange_rate_source_name(self):
        """Gets the exchange_rate_source_name of this ExchangeRateResponse.  # noqa: E501

        Exchange rate source name  # noqa: E501

        :return: The exchange_rate_source_name of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._exchange_rate_source_name

    @exchange_rate_source_name.setter
    def exchange_rate_source_name(self, exchange_rate_source_name):
        """Sets the exchange_rate_source_name of this ExchangeRateResponse.

        Exchange rate source name  # noqa: E501

        :param exchange_rate_source_name: The exchange_rate_source_name of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """

        self._exchange_rate_source_name = exchange_rate_source_name

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
        if not isinstance(other, ExchangeRateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other