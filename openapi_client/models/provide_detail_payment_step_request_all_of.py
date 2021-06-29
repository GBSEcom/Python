# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.3.0.20210608.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ProvideDetailPaymentStepRequestAllOf(object):
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
        'hint': 'str',
        'java_script_validation_expression': 'str',
        'key': 'str',
        'label': 'str'
    }

    attribute_map = {
        'hint': 'hint',
        'java_script_validation_expression': 'javaScriptValidationExpression',
        'key': 'key',
        'label': 'label'
    }

    def __init__(self, hint=None, java_script_validation_expression=None, key=None, label=None):  # noqa: E501
        """ProvideDetailPaymentStepRequestAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._hint = None
        self._java_script_validation_expression = None
        self._key = None
        self._label = None
        self.discriminator = None

        if hint is not None:
            self.hint = hint
        if java_script_validation_expression is not None:
            self.java_script_validation_expression = java_script_validation_expression
        if key is not None:
            self.key = key
        if label is not None:
            self.label = label

    @property
    def hint(self):
        """Gets the hint of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501


        :return: The hint of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        """Sets the hint of this ProvideDetailPaymentStepRequestAllOf.


        :param hint: The hint of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501
        :type: str
        """

        self._hint = hint

    @property
    def java_script_validation_expression(self):
        """Gets the java_script_validation_expression of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501


        :return: The java_script_validation_expression of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._java_script_validation_expression

    @java_script_validation_expression.setter
    def java_script_validation_expression(self, java_script_validation_expression):
        """Sets the java_script_validation_expression of this ProvideDetailPaymentStepRequestAllOf.


        :param java_script_validation_expression: The java_script_validation_expression of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501
        :type: str
        """

        self._java_script_validation_expression = java_script_validation_expression

    @property
    def key(self):
        """Gets the key of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501


        :return: The key of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ProvideDetailPaymentStepRequestAllOf.


        :param key: The key of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def label(self):
        """Gets the label of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501


        :return: The label of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ProvideDetailPaymentStepRequestAllOf.


        :param label: The label of this ProvideDetailPaymentStepRequestAllOf.  # noqa: E501
        :type: str
        """

        self._label = label

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
        if not isinstance(other, ProvideDetailPaymentStepRequestAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
