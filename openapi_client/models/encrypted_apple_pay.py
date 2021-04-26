# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.2.0.20210406.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class EncryptedApplePay(object):
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
        'data': 'str',
        'header': 'EncryptedApplePayHeader',
        'signature': 'str',
        'version': 'str',
        'application_data': 'str',
        'merchant_id': 'str'
    }

    attribute_map = {
        'data': 'data',
        'header': 'header',
        'signature': 'signature',
        'version': 'version',
        'application_data': 'applicationData',
        'merchant_id': 'merchantId'
    }

    def __init__(self, data=None, header=None, signature=None, version=None, application_data=None, merchant_id=None):  # noqa: E501
        """EncryptedApplePay - a model defined in OpenAPI"""  # noqa: E501

        self._data = None
        self._header = None
        self._signature = None
        self._version = None
        self._application_data = None
        self._merchant_id = None
        self.discriminator = None

        self.data = data
        self.header = header
        self.signature = signature
        if version is not None:
            self.version = version
        if application_data is not None:
            self.application_data = application_data
        self.merchant_id = merchant_id

    @property
    def data(self):
        """Gets the data of this EncryptedApplePay.  # noqa: E501

        The encrypted wallet payload.  # noqa: E501

        :return: The data of this EncryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EncryptedApplePay.

        The encrypted wallet payload.  # noqa: E501

        :param data: The data of this EncryptedApplePay.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501
        if data is not None and not re.search(r'^(?!\s*$).+', data):  # noqa: E501
            raise ValueError(r"Invalid value for `data`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._data = data

    @property
    def header(self):
        """Gets the header of this EncryptedApplePay.  # noqa: E501


        :return: The header of this EncryptedApplePay.  # noqa: E501
        :rtype: EncryptedApplePayHeader
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this EncryptedApplePay.


        :param header: The header of this EncryptedApplePay.  # noqa: E501
        :type: EncryptedApplePayHeader
        """
        if header is None:
            raise ValueError("Invalid value for `header`, must not be `None`")  # noqa: E501

        self._header = header

    @property
    def signature(self):
        """Gets the signature of this EncryptedApplePay.  # noqa: E501

        Signature of the payment and header data.  # noqa: E501

        :return: The signature of this EncryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this EncryptedApplePay.

        Signature of the payment and header data.  # noqa: E501

        :param signature: The signature of this EncryptedApplePay.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501
        if signature is not None and not re.search(r'^(?!\s*$).+', signature):  # noqa: E501
            raise ValueError(r"Invalid value for `signature`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._signature = signature

    @property
    def version(self):
        """Gets the version of this EncryptedApplePay.  # noqa: E501

        Version information about the payment token.  # noqa: E501

        :return: The version of this EncryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EncryptedApplePay.

        Version information about the payment token.  # noqa: E501

        :param version: The version of this EncryptedApplePay.  # noqa: E501
        :type: str
        """
        allowed_values = ["EC_v1"]  # noqa: E501
        if version not in allowed_values:
            raise ValueError(
                "Invalid value for `version` ({0}), must be one of {1}"  # noqa: E501
                .format(version, allowed_values)
            )

        self._version = version

    @property
    def application_data(self):
        """Gets the application_data of this EncryptedApplePay.  # noqa: E501

        Base64-encoded value of PKPaymentRequest. Required only if applicationDataHash is present.  # noqa: E501

        :return: The application_data of this EncryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._application_data

    @application_data.setter
    def application_data(self, application_data):
        """Sets the application_data of this EncryptedApplePay.

        Base64-encoded value of PKPaymentRequest. Required only if applicationDataHash is present.  # noqa: E501

        :param application_data: The application_data of this EncryptedApplePay.  # noqa: E501
        :type: str
        """

        self._application_data = application_data

    @property
    def merchant_id(self):
        """Gets the merchant_id of this EncryptedApplePay.  # noqa: E501

        The merchant ID assigned by the wallet provider.  # noqa: E501

        :return: The merchant_id of this EncryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this EncryptedApplePay.

        The merchant ID assigned by the wallet provider.  # noqa: E501

        :param merchant_id: The merchant_id of this EncryptedApplePay.  # noqa: E501
        :type: str
        """
        if merchant_id is None:
            raise ValueError("Invalid value for `merchant_id`, must not be `None`")  # noqa: E501
        if merchant_id is not None and not re.search(r'^(?!\s*$).+', merchant_id):  # noqa: E501
            raise ValueError(r"Invalid value for `merchant_id`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._merchant_id = merchant_id

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
        if not isinstance(other, EncryptedApplePay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
