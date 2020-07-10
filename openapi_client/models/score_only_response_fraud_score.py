# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.12.0.20200706.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ScoreOnlyResponseFraudScore(object):
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
        'score': 'str',
        'warnings': 'list[str]',
        'explanations': 'list[ScoreOnlyResponseFraudScoreExplanations]',
        'recommended_decision': 'str'
    }

    attribute_map = {
        'score': 'score',
        'warnings': 'warnings',
        'explanations': 'explanations',
        'recommended_decision': 'recommendedDecision'
    }

    def __init__(self, score=None, warnings=None, explanations=None, recommended_decision=None):  # noqa: E501
        """ScoreOnlyResponseFraudScore - a model defined in OpenAPI"""  # noqa: E501

        self._score = None
        self._warnings = None
        self._explanations = None
        self._recommended_decision = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if warnings is not None:
            self.warnings = warnings
        if explanations is not None:
            self.explanations = explanations
        if recommended_decision is not None:
            self.recommended_decision = recommended_decision

    @property
    def score(self):
        """Gets the score of this ScoreOnlyResponseFraudScore.  # noqa: E501

        The score attributed to this request by our machine learning system, ranging from 0 (less likely to be fraud) to 1000 (more likely to be fraud).  # noqa: E501

        :return: The score of this ScoreOnlyResponseFraudScore.  # noqa: E501
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ScoreOnlyResponseFraudScore.

        The score attributed to this request by our machine learning system, ranging from 0 (less likely to be fraud) to 1000 (more likely to be fraud).  # noqa: E501

        :param score: The score of this ScoreOnlyResponseFraudScore.  # noqa: E501
        :type: str
        """

        self._score = score

    @property
    def warnings(self):
        """Gets the warnings of this ScoreOnlyResponseFraudScore.  # noqa: E501

        A list of non-critical warnings raised while processing the request. Warnings included in this list will have integration and data-quality related messages.  # noqa: E501

        :return: The warnings of this ScoreOnlyResponseFraudScore.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this ScoreOnlyResponseFraudScore.

        A list of non-critical warnings raised while processing the request. Warnings included in this list will have integration and data-quality related messages.  # noqa: E501

        :param warnings: The warnings of this ScoreOnlyResponseFraudScore.  # noqa: E501
        :type: list[str]
        """

        self._warnings = warnings

    @property
    def explanations(self):
        """Gets the explanations of this ScoreOnlyResponseFraudScore.  # noqa: E501

        Explanation of the fraud score applied consisting of a description, type of the explanation, and rule (if applicable).  # noqa: E501

        :return: The explanations of this ScoreOnlyResponseFraudScore.  # noqa: E501
        :rtype: list[ScoreOnlyResponseFraudScoreExplanations]
        """
        return self._explanations

    @explanations.setter
    def explanations(self, explanations):
        """Sets the explanations of this ScoreOnlyResponseFraudScore.

        Explanation of the fraud score applied consisting of a description, type of the explanation, and rule (if applicable).  # noqa: E501

        :param explanations: The explanations of this ScoreOnlyResponseFraudScore.  # noqa: E501
        :type: list[ScoreOnlyResponseFraudScoreExplanations]
        """

        self._explanations = explanations

    @property
    def recommended_decision(self):
        """Gets the recommended_decision of this ScoreOnlyResponseFraudScore.  # noqa: E501

        The action that should be taken for the request that was sent.  # noqa: E501

        :return: The recommended_decision of this ScoreOnlyResponseFraudScore.  # noqa: E501
        :rtype: str
        """
        return self._recommended_decision

    @recommended_decision.setter
    def recommended_decision(self, recommended_decision):
        """Sets the recommended_decision of this ScoreOnlyResponseFraudScore.

        The action that should be taken for the request that was sent.  # noqa: E501

        :param recommended_decision: The recommended_decision of this ScoreOnlyResponseFraudScore.  # noqa: E501
        :type: str
        """

        self._recommended_decision = recommended_decision

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
        if not isinstance(other, ScoreOnlyResponseFraudScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
