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


class StoreUrlConfiguration(object):
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
        'id': 'str',
        'transaction_notification_url': 'str',
        'recurring_transaction_notification_url': 'str',
        'response_success_url': 'str',
        'response_failure_url': 'str',
        'skip_result_page_for_success': 'bool',
        'skip_result_page_for_failure': 'bool',
        'overwrite_url_allowed': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'transaction_notification_url': 'transactionNotificationUrl',
        'recurring_transaction_notification_url': 'recurringTransactionNotificationUrl',
        'response_success_url': 'responseSuccessUrl',
        'response_failure_url': 'responseFailureUrl',
        'skip_result_page_for_success': 'skipResultPageForSuccess',
        'skip_result_page_for_failure': 'skipResultPageForFailure',
        'overwrite_url_allowed': 'overwriteUrlAllowed'
    }

    def __init__(self, id=None, transaction_notification_url=None, recurring_transaction_notification_url=None, response_success_url=None, response_failure_url=None, skip_result_page_for_success=None, skip_result_page_for_failure=None, overwrite_url_allowed=None):  # noqa: E501
        """StoreUrlConfiguration - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._transaction_notification_url = None
        self._recurring_transaction_notification_url = None
        self._response_success_url = None
        self._response_failure_url = None
        self._skip_result_page_for_success = None
        self._skip_result_page_for_failure = None
        self._overwrite_url_allowed = None
        self.discriminator = None

        self.id = id
        if transaction_notification_url is not None:
            self.transaction_notification_url = transaction_notification_url
        if recurring_transaction_notification_url is not None:
            self.recurring_transaction_notification_url = recurring_transaction_notification_url
        if response_success_url is not None:
            self.response_success_url = response_success_url
        if response_failure_url is not None:
            self.response_failure_url = response_failure_url
        if skip_result_page_for_success is not None:
            self.skip_result_page_for_success = skip_result_page_for_success
        if skip_result_page_for_failure is not None:
            self.skip_result_page_for_failure = skip_result_page_for_failure
        if overwrite_url_allowed is not None:
            self.overwrite_url_allowed = overwrite_url_allowed

    @property
    def id(self):
        """Gets the id of this StoreUrlConfiguration.  # noqa: E501

        An optional outlet id for clients that support multiple stores in the same developer app.  # noqa: E501

        :return: The id of this StoreUrlConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoreUrlConfiguration.

        An optional outlet id for clients that support multiple stores in the same developer app.  # noqa: E501

        :param id: The id of this StoreUrlConfiguration.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def transaction_notification_url(self):
        """Gets the transaction_notification_url of this StoreUrlConfiguration.  # noqa: E501

        Transaction notification URL for Connect.  # noqa: E501

        :return: The transaction_notification_url of this StoreUrlConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._transaction_notification_url

    @transaction_notification_url.setter
    def transaction_notification_url(self, transaction_notification_url):
        """Sets the transaction_notification_url of this StoreUrlConfiguration.

        Transaction notification URL for Connect.  # noqa: E501

        :param transaction_notification_url: The transaction_notification_url of this StoreUrlConfiguration.  # noqa: E501
        :type: str
        """

        self._transaction_notification_url = transaction_notification_url

    @property
    def recurring_transaction_notification_url(self):
        """Gets the recurring_transaction_notification_url of this StoreUrlConfiguration.  # noqa: E501

        Recurring transaction notification URL for recurring payments.  # noqa: E501

        :return: The recurring_transaction_notification_url of this StoreUrlConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._recurring_transaction_notification_url

    @recurring_transaction_notification_url.setter
    def recurring_transaction_notification_url(self, recurring_transaction_notification_url):
        """Sets the recurring_transaction_notification_url of this StoreUrlConfiguration.

        Recurring transaction notification URL for recurring payments.  # noqa: E501

        :param recurring_transaction_notification_url: The recurring_transaction_notification_url of this StoreUrlConfiguration.  # noqa: E501
        :type: str
        """

        self._recurring_transaction_notification_url = recurring_transaction_notification_url

    @property
    def response_success_url(self):
        """Gets the response_success_url of this StoreUrlConfiguration.  # noqa: E501

        Response success URL for Connect.  # noqa: E501

        :return: The response_success_url of this StoreUrlConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._response_success_url

    @response_success_url.setter
    def response_success_url(self, response_success_url):
        """Sets the response_success_url of this StoreUrlConfiguration.

        Response success URL for Connect.  # noqa: E501

        :param response_success_url: The response_success_url of this StoreUrlConfiguration.  # noqa: E501
        :type: str
        """

        self._response_success_url = response_success_url

    @property
    def response_failure_url(self):
        """Gets the response_failure_url of this StoreUrlConfiguration.  # noqa: E501

        Response failure URL for Connect.  # noqa: E501

        :return: The response_failure_url of this StoreUrlConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._response_failure_url

    @response_failure_url.setter
    def response_failure_url(self, response_failure_url):
        """Sets the response_failure_url of this StoreUrlConfiguration.

        Response failure URL for Connect.  # noqa: E501

        :param response_failure_url: The response_failure_url of this StoreUrlConfiguration.  # noqa: E501
        :type: str
        """

        self._response_failure_url = response_failure_url

    @property
    def skip_result_page_for_success(self):
        """Gets the skip_result_page_for_success of this StoreUrlConfiguration.  # noqa: E501

        Skip connect result page when transaction is approved.  # noqa: E501

        :return: The skip_result_page_for_success of this StoreUrlConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._skip_result_page_for_success

    @skip_result_page_for_success.setter
    def skip_result_page_for_success(self, skip_result_page_for_success):
        """Sets the skip_result_page_for_success of this StoreUrlConfiguration.

        Skip connect result page when transaction is approved.  # noqa: E501

        :param skip_result_page_for_success: The skip_result_page_for_success of this StoreUrlConfiguration.  # noqa: E501
        :type: bool
        """

        self._skip_result_page_for_success = skip_result_page_for_success

    @property
    def skip_result_page_for_failure(self):
        """Gets the skip_result_page_for_failure of this StoreUrlConfiguration.  # noqa: E501

        Skip connect result page when transaction is not approved.  # noqa: E501

        :return: The skip_result_page_for_failure of this StoreUrlConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._skip_result_page_for_failure

    @skip_result_page_for_failure.setter
    def skip_result_page_for_failure(self, skip_result_page_for_failure):
        """Sets the skip_result_page_for_failure of this StoreUrlConfiguration.

        Skip connect result page when transaction is not approved.  # noqa: E501

        :param skip_result_page_for_failure: The skip_result_page_for_failure of this StoreUrlConfiguration.  # noqa: E501
        :type: bool
        """

        self._skip_result_page_for_failure = skip_result_page_for_failure

    @property
    def overwrite_url_allowed(self):
        """Gets the overwrite_url_allowed of this StoreUrlConfiguration.  # noqa: E501

        Overwrite URLs in database by those from request.  # noqa: E501

        :return: The overwrite_url_allowed of this StoreUrlConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._overwrite_url_allowed

    @overwrite_url_allowed.setter
    def overwrite_url_allowed(self, overwrite_url_allowed):
        """Sets the overwrite_url_allowed of this StoreUrlConfiguration.

        Overwrite URLs in database by those from request.  # noqa: E501

        :param overwrite_url_allowed: The overwrite_url_allowed of this StoreUrlConfiguration.  # noqa: E501
        :type: bool
        """

        self._overwrite_url_allowed = overwrite_url_allowed

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
        if not isinstance(other, StoreUrlConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
