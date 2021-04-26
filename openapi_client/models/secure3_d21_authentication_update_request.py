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


class Secure3D21AuthenticationUpdateRequest(object):
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
        'store_id': 'str',
        'authentication_type': 'str',
        'billing_address': 'Address',
        'method_notification_status': 'str',
        'acs_response': 'ACSResponse'
    }

    attribute_map = {
        'store_id': 'storeId',
        'authentication_type': 'authenticationType',
        'billing_address': 'billingAddress',
        'method_notification_status': 'methodNotificationStatus',
        'acs_response': 'acsResponse'
    }

    def __init__(self, store_id=None, authentication_type=None, billing_address=None, method_notification_status=None, acs_response=None):  # noqa: E501
        """Secure3D21AuthenticationUpdateRequest - a model defined in OpenAPI"""  # noqa: E501

        self._store_id = None
        self._authentication_type = None
        self._billing_address = None
        self._method_notification_status = None
        self._acs_response = None
        self.discriminator = None

        if store_id is not None:
            self.store_id = store_id
        self.authentication_type = authentication_type
        if billing_address is not None:
            self.billing_address = billing_address
        if method_notification_status is not None:
            self.method_notification_status = method_notification_status
        if acs_response is not None:
            self.acs_response = acs_response

    @property
    def store_id(self):
        """Gets the store_id of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501

        An optional Outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :return: The store_id of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this Secure3D21AuthenticationUpdateRequest.

        An optional Outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :param store_id: The store_id of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def authentication_type(self):
        """Gets the authentication_type of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501

        Object name of the authentication update request.  # noqa: E501

        :return: The authentication_type of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this Secure3D21AuthenticationUpdateRequest.

        Object name of the authentication update request.  # noqa: E501

        :param authentication_type: The authentication_type of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501
        :type: str
        """
        if authentication_type is None:
            raise ValueError("Invalid value for `authentication_type`, must not be `None`")  # noqa: E501

        self._authentication_type = authentication_type

    @property
    def billing_address(self):
        """Gets the billing_address of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501


        :return: The billing_address of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this Secure3D21AuthenticationUpdateRequest.


        :param billing_address: The billing_address of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501
        :type: Address
        """

        self._billing_address = billing_address

    @property
    def method_notification_status(self):
        """Gets the method_notification_status of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501

        Indicates how the merchant received the 3DS method.  # noqa: E501

        :return: The method_notification_status of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._method_notification_status

    @method_notification_status.setter
    def method_notification_status(self, method_notification_status):
        """Sets the method_notification_status of this Secure3D21AuthenticationUpdateRequest.

        Indicates how the merchant received the 3DS method.  # noqa: E501

        :param method_notification_status: The method_notification_status of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["RECEIVED", "EXPECTED_BUT_NOT_RECEIVED", "NOT_EXPECTED"]  # noqa: E501
        if method_notification_status not in allowed_values:
            raise ValueError(
                "Invalid value for `method_notification_status` ({0}), must be one of {1}"  # noqa: E501
                .format(method_notification_status, allowed_values)
            )

        self._method_notification_status = method_notification_status

    @property
    def acs_response(self):
        """Gets the acs_response of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501


        :return: The acs_response of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501
        :rtype: ACSResponse
        """
        return self._acs_response

    @acs_response.setter
    def acs_response(self, acs_response):
        """Sets the acs_response of this Secure3D21AuthenticationUpdateRequest.


        :param acs_response: The acs_response of this Secure3D21AuthenticationUpdateRequest.  # noqa: E501
        :type: ACSResponse
        """

        self._acs_response = acs_response

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
        if not isinstance(other, Secure3D21AuthenticationUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
