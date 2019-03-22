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


class AliPay(object):
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
        'payment_data_type': 'str',
        'payment_data': 'str',
        'order_title': 'str',
        'order_details': 'str'
    }

    attribute_map = {
        'payment_data_type': 'paymentDataType',
        'payment_data': 'paymentData',
        'order_title': 'orderTitle',
        'order_details': 'orderDetails'
    }

    def __init__(self, payment_data_type=None, payment_data=None, order_title=None, order_details=None):  # noqa: E501
        """AliPay - a model defined in OpenAPI"""  # noqa: E501

        self._payment_data_type = None
        self._payment_data = None
        self._order_title = None
        self._order_details = None
        self.discriminator = None

        self.payment_data_type = payment_data_type
        self.payment_data = payment_data
        self.order_title = order_title
        self.order_details = order_details

    @property
    def payment_data_type(self):
        """Gets the payment_data_type of this AliPay.  # noqa: E501

        Use this to indicate the type of machine-readable payment data for scanning.  # noqa: E501

        :return: The payment_data_type of this AliPay.  # noqa: E501
        :rtype: str
        """
        return self._payment_data_type

    @payment_data_type.setter
    def payment_data_type(self, payment_data_type):
        """Sets the payment_data_type of this AliPay.

        Use this to indicate the type of machine-readable payment data for scanning.  # noqa: E501

        :param payment_data_type: The payment_data_type of this AliPay.  # noqa: E501
        :type: str
        """
        if payment_data_type is None:
            raise ValueError("Invalid value for `payment_data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["BARCODE", "QRCODE"]  # noqa: E501
        if payment_data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_data_type, allowed_values)
            )

        self._payment_data_type = payment_data_type

    @property
    def payment_data(self):
        """Gets the payment_data of this AliPay.  # noqa: E501

        Use this to send payment related information, such as customer identity ID.  # noqa: E501

        :return: The payment_data of this AliPay.  # noqa: E501
        :rtype: str
        """
        return self._payment_data

    @payment_data.setter
    def payment_data(self, payment_data):
        """Sets the payment_data of this AliPay.

        Use this to send payment related information, such as customer identity ID.  # noqa: E501

        :param payment_data: The payment_data of this AliPay.  # noqa: E501
        :type: str
        """
        if payment_data is None:
            raise ValueError("Invalid value for `payment_data`, must not be `None`")  # noqa: E501
        if payment_data is not None and len(payment_data) > 100:
            raise ValueError("Invalid value for `payment_data`, length must be less than or equal to `100`")  # noqa: E501

        self._payment_data = payment_data

    @property
    def order_title(self):
        """Gets the order_title of this AliPay.  # noqa: E501

        Use this to send an order title that shows up in the statement  # noqa: E501

        :return: The order_title of this AliPay.  # noqa: E501
        :rtype: str
        """
        return self._order_title

    @order_title.setter
    def order_title(self, order_title):
        """Sets the order_title of this AliPay.

        Use this to send an order title that shows up in the statement  # noqa: E501

        :param order_title: The order_title of this AliPay.  # noqa: E501
        :type: str
        """
        if order_title is None:
            raise ValueError("Invalid value for `order_title`, must not be `None`")  # noqa: E501
        if order_title is not None and len(order_title) > 100:
            raise ValueError("Invalid value for `order_title`, length must be less than or equal to `100`")  # noqa: E501

        self._order_title = order_title

    @property
    def order_details(self):
        """Gets the order_details of this AliPay.  # noqa: E501

        Use this to send order details that show up in the statement  # noqa: E501

        :return: The order_details of this AliPay.  # noqa: E501
        :rtype: str
        """
        return self._order_details

    @order_details.setter
    def order_details(self, order_details):
        """Sets the order_details of this AliPay.

        Use this to send order details that show up in the statement  # noqa: E501

        :param order_details: The order_details of this AliPay.  # noqa: E501
        :type: str
        """
        if order_details is None:
            raise ValueError("Invalid value for `order_details`, must not be `None`")  # noqa: E501
        if order_details is not None and len(order_details) > 1024:
            raise ValueError("Invalid value for `order_details`, length must be less than or equal to `1024`")  # noqa: E501

        self._order_details = order_details

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
        if not isinstance(other, AliPay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other