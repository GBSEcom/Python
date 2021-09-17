# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.4.0.20210824.002
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ScoreOnlyResponseFraudScoreExplanations(object):
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
        'description': 'str',
        'rule': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'rule': 'rule',
        'type': 'type'
    }

    def __init__(self, description=None, rule=None, type=None):  # noqa: E501
        """ScoreOnlyResponseFraudScoreExplanations - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._rule = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if rule is not None:
            self.rule = rule
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this ScoreOnlyResponseFraudScoreExplanations.  # noqa: E501

        Description of the fraud score explanation.  # noqa: E501

        :return: The description of this ScoreOnlyResponseFraudScoreExplanations.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScoreOnlyResponseFraudScoreExplanations.

        Description of the fraud score explanation.  # noqa: E501

        :param description: The description of this ScoreOnlyResponseFraudScoreExplanations.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rule(self):
        """Gets the rule of this ScoreOnlyResponseFraudScoreExplanations.  # noqa: E501

        ID of the rule being triggered.  # noqa: E501

        :return: The rule of this ScoreOnlyResponseFraudScoreExplanations.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ScoreOnlyResponseFraudScoreExplanations.

        ID of the rule being triggered.  # noqa: E501

        :param rule: The rule of this ScoreOnlyResponseFraudScoreExplanations.  # noqa: E501
        :type: str
        """

        self._rule = rule

    @property
    def type(self):
        """Gets the type of this ScoreOnlyResponseFraudScoreExplanations.  # noqa: E501

        Type of the explanation (model or rule).  # noqa: E501

        :return: The type of this ScoreOnlyResponseFraudScoreExplanations.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScoreOnlyResponseFraudScoreExplanations.

        Type of the explanation (model or rule).  # noqa: E501

        :param type: The type of this ScoreOnlyResponseFraudScoreExplanations.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, ScoreOnlyResponseFraudScoreExplanations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
