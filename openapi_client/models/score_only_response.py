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


class ScoreOnlyResponse(object):
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
        'correlation_id': 'str',
        'transaction_status': 'str',
        'validation_status': 'str',
        'transaction_type': 'str',
        'fraud_score': 'ScoreOnlyResponseFraudScore'
    }

    attribute_map = {
        'correlation_id': 'correlationId',
        'transaction_status': 'transactionStatus',
        'validation_status': 'validationStatus',
        'transaction_type': 'transactionType',
        'fraud_score': 'fraudScore'
    }

    def __init__(self, correlation_id=None, transaction_status=None, validation_status=None, transaction_type=None, fraud_score=None):  # noqa: E501
        """ScoreOnlyResponse - a model defined in OpenAPI"""  # noqa: E501

        self._correlation_id = None
        self._transaction_status = None
        self._validation_status = None
        self._transaction_type = None
        self._fraud_score = None
        self.discriminator = None

        if correlation_id is not None:
            self.correlation_id = correlation_id
        if transaction_status is not None:
            self.transaction_status = transaction_status
        if validation_status is not None:
            self.validation_status = validation_status
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if fraud_score is not None:
            self.fraud_score = fraud_score

    @property
    def correlation_id(self):
        """Gets the correlation_id of this ScoreOnlyResponse.  # noqa: E501

        Unique trace ID for issue triage.  # noqa: E501

        :return: The correlation_id of this ScoreOnlyResponse.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this ScoreOnlyResponse.

        Unique trace ID for issue triage.  # noqa: E501

        :param correlation_id: The correlation_id of this ScoreOnlyResponse.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def transaction_status(self):
        """Gets the transaction_status of this ScoreOnlyResponse.  # noqa: E501

        Please refer to \"Errors Section\" for more info.  # noqa: E501

        :return: The transaction_status of this ScoreOnlyResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this ScoreOnlyResponse.

        Please refer to \"Errors Section\" for more info.  # noqa: E501

        :param transaction_status: The transaction_status of this ScoreOnlyResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Scored Successfully", "Not Processed"]  # noqa: E501
        if transaction_status not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_status` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_status, allowed_values)
            )

        self._transaction_status = transaction_status

    @property
    def validation_status(self):
        """Gets the validation_status of this ScoreOnlyResponse.  # noqa: E501

        If status returned is \"failure\", input validation errors occurred. Please refer to the \"Errors Section\" for more info. Valid values are 'success' and 'failure'.  # noqa: E501

        :return: The validation_status of this ScoreOnlyResponse.  # noqa: E501
        :rtype: str
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """Sets the validation_status of this ScoreOnlyResponse.

        If status returned is \"failure\", input validation errors occurred. Please refer to the \"Errors Section\" for more info. Valid values are 'success' and 'failure'.  # noqa: E501

        :param validation_status: The validation_status of this ScoreOnlyResponse.  # noqa: E501
        :type: str
        """

        self._validation_status = validation_status

    @property
    def transaction_type(self):
        """Gets the transaction_type of this ScoreOnlyResponse.  # noqa: E501

        The transactionType provided in request.  # noqa: E501

        :return: The transaction_type of this ScoreOnlyResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this ScoreOnlyResponse.

        The transactionType provided in request.  # noqa: E501

        :param transaction_type: The transaction_type of this ScoreOnlyResponse.  # noqa: E501
        :type: str
        """

        self._transaction_type = transaction_type

    @property
    def fraud_score(self):
        """Gets the fraud_score of this ScoreOnlyResponse.  # noqa: E501


        :return: The fraud_score of this ScoreOnlyResponse.  # noqa: E501
        :rtype: ScoreOnlyResponseFraudScore
        """
        return self._fraud_score

    @fraud_score.setter
    def fraud_score(self, fraud_score):
        """Sets the fraud_score of this ScoreOnlyResponse.


        :param fraud_score: The fraud_score of this ScoreOnlyResponse.  # noqa: E501
        :type: ScoreOnlyResponseFraudScore
        """

        self._fraud_score = fraud_score

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
        if not isinstance(other, ScoreOnlyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
