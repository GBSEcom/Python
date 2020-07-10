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


class PaymentTokenUpdateResponse(object):
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
        'client_request_id': 'str',
        'api_trace_id': 'str',
        'response_type': 'ResponseType',
        'request_status': 'str',
        'request_time': 'int',
        'errors': 'list[Error]'
    }

    attribute_map = {
        'client_request_id': 'clientRequestId',
        'api_trace_id': 'apiTraceId',
        'response_type': 'responseType',
        'request_status': 'requestStatus',
        'request_time': 'requestTime',
        'errors': 'errors'
    }

    def __init__(self, client_request_id=None, api_trace_id=None, response_type=None, request_status=None, request_time=None, errors=None, local_vars_configuration=None):  # noqa: E501
        """PaymentTokenUpdateResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_request_id = None
        self._api_trace_id = None
        self._response_type = None
        self._request_status = None
        self._request_time = None
        self._errors = None
        self.discriminator = None

        if client_request_id is not None:
            self.client_request_id = client_request_id
        if api_trace_id is not None:
            self.api_trace_id = api_trace_id
        if response_type is not None:
            self.response_type = response_type
        if request_status is not None:
            self.request_status = request_status
        if request_time is not None:
            self.request_time = request_time
        if errors is not None:
            self.errors = errors

    @property
    def client_request_id(self):
        """Gets the client_request_id of this PaymentTokenUpdateResponse.  # noqa: E501

        Echoes back the value in the request header for tracking.  # noqa: E501

        :return: The client_request_id of this PaymentTokenUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this PaymentTokenUpdateResponse.

        Echoes back the value in the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this PaymentTokenUpdateResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = client_request_id

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this PaymentTokenUpdateResponse.  # noqa: E501

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :return: The api_trace_id of this PaymentTokenUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(self, api_trace_id):
        """Sets the api_trace_id of this PaymentTokenUpdateResponse.

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :param api_trace_id: The api_trace_id of this PaymentTokenUpdateResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = api_trace_id

    @property
    def response_type(self):
        """Gets the response_type of this PaymentTokenUpdateResponse.  # noqa: E501


        :return: The response_type of this PaymentTokenUpdateResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this PaymentTokenUpdateResponse.


        :param response_type: The response_type of this PaymentTokenUpdateResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = response_type

    @property
    def request_status(self):
        """Gets the request_status of this PaymentTokenUpdateResponse.  # noqa: E501

        The status of the request.  # noqa: E501

        :return: The request_status of this PaymentTokenUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_status

    @request_status.setter
    def request_status(self, request_status):
        """Sets the request_status of this PaymentTokenUpdateResponse.

        The status of the request.  # noqa: E501

        :param request_status: The request_status of this PaymentTokenUpdateResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["FAILED", "SUCCESS", "PARTIAL_SUCCESS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and request_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `request_status` ({0}), must be one of {1}"  # noqa: E501
                .format(request_status, allowed_values)
            )

        self._request_status = request_status

    @property
    def request_time(self):
        """Gets the request_time of this PaymentTokenUpdateResponse.  # noqa: E501

        Time of the request.  # noqa: E501

        :return: The request_time of this PaymentTokenUpdateResponse.  # noqa: E501
        :rtype: int
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        """Sets the request_time of this PaymentTokenUpdateResponse.

        Time of the request.  # noqa: E501

        :param request_time: The request_time of this PaymentTokenUpdateResponse.  # noqa: E501
        :type: int
        """

        self._request_time = request_time

    @property
    def errors(self):
        """Gets the errors of this PaymentTokenUpdateResponse.  # noqa: E501


        :return: The errors of this PaymentTokenUpdateResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this PaymentTokenUpdateResponse.


        :param errors: The errors of this PaymentTokenUpdateResponse.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

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
        if not isinstance(other, PaymentTokenUpdateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentTokenUpdateResponse):
            return True

        return self.to_dict() != other.to_dict()
