# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.1.0.20210122.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GenerateCertificateFromCsrResponse(object):
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
        'certificate': 'str'
    }

    attribute_map = {
        'client_request_id': 'clientRequestId',
        'api_trace_id': 'apiTraceId',
        'response_type': 'responseType',
        'certificate': 'certificate'
    }

    def __init__(self, client_request_id=None, api_trace_id=None, response_type=None, certificate=None):  # noqa: E501
        """GenerateCertificateFromCsrResponse - a model defined in OpenAPI"""  # noqa: E501

        self._client_request_id = None
        self._api_trace_id = None
        self._response_type = None
        self._certificate = None
        self.discriminator = None

        if client_request_id is not None:
            self.client_request_id = client_request_id
        if api_trace_id is not None:
            self.api_trace_id = api_trace_id
        if response_type is not None:
            self.response_type = response_type
        self.certificate = certificate

    @property
    def client_request_id(self):
        """Gets the client_request_id of this GenerateCertificateFromCsrResponse.  # noqa: E501

        Echoes back the value in the request header for tracking.  # noqa: E501

        :return: The client_request_id of this GenerateCertificateFromCsrResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this GenerateCertificateFromCsrResponse.

        Echoes back the value in the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this GenerateCertificateFromCsrResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = client_request_id

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this GenerateCertificateFromCsrResponse.  # noqa: E501

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :return: The api_trace_id of this GenerateCertificateFromCsrResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(self, api_trace_id):
        """Sets the api_trace_id of this GenerateCertificateFromCsrResponse.

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :param api_trace_id: The api_trace_id of this GenerateCertificateFromCsrResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = api_trace_id

    @property
    def response_type(self):
        """Gets the response_type of this GenerateCertificateFromCsrResponse.  # noqa: E501


        :return: The response_type of this GenerateCertificateFromCsrResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this GenerateCertificateFromCsrResponse.


        :param response_type: The response_type of this GenerateCertificateFromCsrResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = response_type

    @property
    def certificate(self):
        """Gets the certificate of this GenerateCertificateFromCsrResponse.  # noqa: E501

        Certificate file (x509) encoded in Base64.  # noqa: E501

        :return: The certificate of this GenerateCertificateFromCsrResponse.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this GenerateCertificateFromCsrResponse.

        Certificate file (x509) encoded in Base64.  # noqa: E501

        :param certificate: The certificate of this GenerateCertificateFromCsrResponse.  # noqa: E501
        :type: str
        """
        if certificate is None:
            raise ValueError("Invalid value for `certificate`, must not be `None`")  # noqa: E501

        self._certificate = certificate

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
        if not isinstance(other, GenerateCertificateFromCsrResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other