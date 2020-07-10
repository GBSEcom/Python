# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.12.0.20200605.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class DCCExchangeRateRequest(object):
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
        'base_amount': 'float',
        'store_id': 'str',
        'bin': 'str'
    }

    attribute_map = {
        'request_type': 'requestType',
        'base_amount': 'baseAmount',
        'store_id': 'storeId',
        'bin': 'bin'
    }

    def __init__(self, request_type=None, base_amount=None, store_id=None, bin=None, local_vars_configuration=None):  # noqa: E501
        """DCCExchangeRateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._request_type = None
        self._base_amount = None
        self._store_id = None
        self._bin = None
        self.discriminator = None

        self.request_type = request_type
        self.base_amount = base_amount
        if store_id is not None:
            self.store_id = store_id
        self.bin = bin

    @property
    def request_type(self):
        """Gets the request_type of this DCCExchangeRateRequest.  # noqa: E501

        Object name of the exchange rate request.  # noqa: E501

        :return: The request_type of this DCCExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this DCCExchangeRateRequest.

        Object name of the exchange rate request.  # noqa: E501

        :param request_type: The request_type of this DCCExchangeRateRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and request_type is None:  # noqa: E501
            raise ValueError("Invalid value for `request_type`, must not be `None`")  # noqa: E501

        self._request_type = request_type

    @property
    def base_amount(self):
        """Gets the base_amount of this DCCExchangeRateRequest.  # noqa: E501

        The original amount of the merchant currency for calculation.  # noqa: E501

        :return: The base_amount of this DCCExchangeRateRequest.  # noqa: E501
        :rtype: float
        """
        return self._base_amount

    @base_amount.setter
    def base_amount(self, base_amount):
        """Sets the base_amount of this DCCExchangeRateRequest.

        The original amount of the merchant currency for calculation.  # noqa: E501

        :param base_amount: The base_amount of this DCCExchangeRateRequest.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and base_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `base_amount`, must not be `None`")  # noqa: E501

        self._base_amount = base_amount

    @property
    def store_id(self):
        """Gets the store_id of this DCCExchangeRateRequest.  # noqa: E501

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :return: The store_id of this DCCExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this DCCExchangeRateRequest.

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :param store_id: The store_id of this DCCExchangeRateRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                store_id is not None and len(store_id) > 20):
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def bin(self):
        """Gets the bin of this DCCExchangeRateRequest.  # noqa: E501

        The bank identification number (BIN) of the card to be used for DCC. The BIN is the first 6 digits of the card number.  # noqa: E501

        :return: The bin of this DCCExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """Sets the bin of this DCCExchangeRateRequest.

        The bank identification number (BIN) of the card to be used for DCC. The BIN is the first 6 digits of the card number.  # noqa: E501

        :param bin: The bin of this DCCExchangeRateRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bin is None:  # noqa: E501
            raise ValueError("Invalid value for `bin`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bin is not None and len(bin) > 6):
            raise ValueError("Invalid value for `bin`, length must be less than or equal to `6`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bin is not None and not re.search(r'[0-9]{6}', bin)):  # noqa: E501
            raise ValueError(r"Invalid value for `bin`, must be a follow pattern or equal to `/[0-9]{6}/`")  # noqa: E501

        self._bin = bin

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
        if not isinstance(other, DCCExchangeRateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DCCExchangeRateRequest):
            return True

        return self.to_dict() != other.to_dict()
