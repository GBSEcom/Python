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


class PaymentSchedulesResponseAllOf(object):
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
        'request_status': 'str',
        'order_id': 'str',
        'transaction_response': 'TransactionResponse'
    }

    attribute_map = {
        'request_status': 'requestStatus',
        'order_id': 'orderId',
        'transaction_response': 'transactionResponse'
    }

    def __init__(self, request_status=None, order_id=None, transaction_response=None, local_vars_configuration=None):  # noqa: E501
        """PaymentSchedulesResponseAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._request_status = None
        self._order_id = None
        self._transaction_response = None
        self.discriminator = None

        if request_status is not None:
            self.request_status = request_status
        if order_id is not None:
            self.order_id = order_id
        if transaction_response is not None:
            self.transaction_response = transaction_response

    @property
    def request_status(self):
        """Gets the request_status of this PaymentSchedulesResponseAllOf.  # noqa: E501

        Result of requested operation. If it's anything other than 'SUCCESS', please refer to 400s HTTP error codes or decline. See Error object for details.  # noqa: E501

        :return: The request_status of this PaymentSchedulesResponseAllOf.  # noqa: E501
        :rtype: str
        """
        return self._request_status

    @request_status.setter
    def request_status(self, request_status):
        """Sets the request_status of this PaymentSchedulesResponseAllOf.

        Result of requested operation. If it's anything other than 'SUCCESS', please refer to 400s HTTP error codes or decline. See Error object for details.  # noqa: E501

        :param request_status: The request_status of this PaymentSchedulesResponseAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "VALIDATION_FAILED", "PROCESSING_FAILED", "FAILURE", "DECLINED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and request_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `request_status` ({0}), must be one of {1}"  # noqa: E501
                .format(request_status, allowed_values)
            )

        self._request_status = request_status

    @property
    def order_id(self):
        """Gets the order_id of this PaymentSchedulesResponseAllOf.  # noqa: E501

        Client order ID if supplied by client, otherwise the order ID.  # noqa: E501

        :return: The order_id of this PaymentSchedulesResponseAllOf.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PaymentSchedulesResponseAllOf.

        Client order ID if supplied by client, otherwise the order ID.  # noqa: E501

        :param order_id: The order_id of this PaymentSchedulesResponseAllOf.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def transaction_response(self):
        """Gets the transaction_response of this PaymentSchedulesResponseAllOf.  # noqa: E501


        :return: The transaction_response of this PaymentSchedulesResponseAllOf.  # noqa: E501
        :rtype: TransactionResponse
        """
        return self._transaction_response

    @transaction_response.setter
    def transaction_response(self, transaction_response):
        """Sets the transaction_response of this PaymentSchedulesResponseAllOf.


        :param transaction_response: The transaction_response of this PaymentSchedulesResponseAllOf.  # noqa: E501
        :type: TransactionResponse
        """

        self._transaction_response = transaction_response

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
        if not isinstance(other, PaymentSchedulesResponseAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentSchedulesResponseAllOf):
            return True

        return self.to_dict() != other.to_dict()
