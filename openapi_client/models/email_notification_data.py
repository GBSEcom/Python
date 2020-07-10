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


class EmailNotificationData(object):
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
        'enable_notification': 'bool',
        'merchant_name': 'str',
        'receiver_email': 'str',
        'sender_email': 'str',
        'locale': 'str'
    }

    attribute_map = {
        'enable_notification': 'enableNotification',
        'merchant_name': 'merchantName',
        'receiver_email': 'receiverEmail',
        'sender_email': 'senderEmail',
        'locale': 'locale'
    }

    def __init__(self, enable_notification=None, merchant_name=None, receiver_email=None, sender_email=None, locale=None, local_vars_configuration=None):  # noqa: E501
        """EmailNotificationData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable_notification = None
        self._merchant_name = None
        self._receiver_email = None
        self._sender_email = None
        self._locale = None
        self.discriminator = None

        if enable_notification is not None:
            self.enable_notification = enable_notification
        if merchant_name is not None:
            self.merchant_name = merchant_name
        if receiver_email is not None:
            self.receiver_email = receiver_email
        if sender_email is not None:
            self.sender_email = sender_email
        if locale is not None:
            self.locale = locale

    @property
    def enable_notification(self):
        """Gets the enable_notification of this EmailNotificationData.  # noqa: E501

        Use this to enable/disable email notifications.  # noqa: E501

        :return: The enable_notification of this EmailNotificationData.  # noqa: E501
        :rtype: bool
        """
        return self._enable_notification

    @enable_notification.setter
    def enable_notification(self, enable_notification):
        """Sets the enable_notification of this EmailNotificationData.

        Use this to enable/disable email notifications.  # noqa: E501

        :param enable_notification: The enable_notification of this EmailNotificationData.  # noqa: E501
        :type: bool
        """

        self._enable_notification = enable_notification

    @property
    def merchant_name(self):
        """Gets the merchant_name of this EmailNotificationData.  # noqa: E501

        The merchant name to be displayed in the email to customer.  # noqa: E501

        :return: The merchant_name of this EmailNotificationData.  # noqa: E501
        :rtype: str
        """
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, merchant_name):
        """Sets the merchant_name of this EmailNotificationData.

        The merchant name to be displayed in the email to customer.  # noqa: E501

        :param merchant_name: The merchant_name of this EmailNotificationData.  # noqa: E501
        :type: str
        """

        self._merchant_name = merchant_name

    @property
    def receiver_email(self):
        """Gets the receiver_email of this EmailNotificationData.  # noqa: E501

        The email address(es) for receiving transaction notifications.  # noqa: E501

        :return: The receiver_email of this EmailNotificationData.  # noqa: E501
        :rtype: str
        """
        return self._receiver_email

    @receiver_email.setter
    def receiver_email(self, receiver_email):
        """Sets the receiver_email of this EmailNotificationData.

        The email address(es) for receiving transaction notifications.  # noqa: E501

        :param receiver_email: The receiver_email of this EmailNotificationData.  # noqa: E501
        :type: str
        """

        self._receiver_email = receiver_email

    @property
    def sender_email(self):
        """Gets the sender_email of this EmailNotificationData.  # noqa: E501

        The email address for sending transaction notifications to customer.  # noqa: E501

        :return: The sender_email of this EmailNotificationData.  # noqa: E501
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """Sets the sender_email of this EmailNotificationData.

        The email address for sending transaction notifications to customer.  # noqa: E501

        :param sender_email: The sender_email of this EmailNotificationData.  # noqa: E501
        :type: str
        """

        self._sender_email = sender_email

    @property
    def locale(self):
        """Gets the locale of this EmailNotificationData.  # noqa: E501

        The locale for received notifications.  # noqa: E501

        :return: The locale of this EmailNotificationData.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this EmailNotificationData.

        The locale for received notifications.  # noqa: E501

        :param locale: The locale of this EmailNotificationData.  # noqa: E501
        :type: str
        """

        self._locale = locale

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
        if not isinstance(other, EmailNotificationData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailNotificationData):
            return True

        return self.to_dict() != other.to_dict()
