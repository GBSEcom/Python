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


class StandInDetails(object):
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
        'stand_in_type': 'str',
        'number_of_debits': 'str',
        'si_validated': 'bool',
        'maximum_transaction_amount': 'float',
        'si_hub_id': 'str',
        'frequency': 'str'
    }

    attribute_map = {
        'stand_in_type': 'standInType',
        'number_of_debits': 'numberOfDebits',
        'si_validated': 'siValidated',
        'maximum_transaction_amount': 'maximumTransactionAmount',
        'si_hub_id': 'siHubId',
        'frequency': 'frequency'
    }

    def __init__(self, stand_in_type=None, number_of_debits=None, si_validated=None, maximum_transaction_amount=None, si_hub_id=None, frequency=None):  # noqa: E501
        """StandInDetails - a model defined in OpenAPI"""  # noqa: E501

        self._stand_in_type = None
        self._number_of_debits = None
        self._si_validated = None
        self._maximum_transaction_amount = None
        self._si_hub_id = None
        self._frequency = None
        self.discriminator = None

        self.stand_in_type = stand_in_type
        self.number_of_debits = number_of_debits
        self.si_validated = si_validated
        self.maximum_transaction_amount = maximum_transaction_amount
        self.si_hub_id = si_hub_id
        self.frequency = frequency

    @property
    def stand_in_type(self):
        """Gets the stand_in_type of this StandInDetails.  # noqa: E501

        Indicates standin instruction type.  # noqa: E501

        :return: The stand_in_type of this StandInDetails.  # noqa: E501
        :rtype: str
        """
        return self._stand_in_type

    @stand_in_type.setter
    def stand_in_type(self, stand_in_type):
        """Sets the stand_in_type of this StandInDetails.

        Indicates standin instruction type.  # noqa: E501

        :param stand_in_type: The stand_in_type of this StandInDetails.  # noqa: E501
        :type: str
        """
        if stand_in_type is None:
            raise ValueError("Invalid value for `stand_in_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FIXED_AMOUNT", "MAXIMUM_AMOUNT"]  # noqa: E501
        if stand_in_type not in allowed_values:
            raise ValueError(
                "Invalid value for `stand_in_type` ({0}), must be one of {1}"  # noqa: E501
                .format(stand_in_type, allowed_values)
            )

        self._stand_in_type = stand_in_type

    @property
    def number_of_debits(self):
        """Gets the number_of_debits of this StandInDetails.  # noqa: E501

        Indicates number of standin instruction debits.Possible values can be two digit number or UN (Until it is cancelled) or ND (Not defined).  # noqa: E501

        :return: The number_of_debits of this StandInDetails.  # noqa: E501
        :rtype: str
        """
        return self._number_of_debits

    @number_of_debits.setter
    def number_of_debits(self, number_of_debits):
        """Sets the number_of_debits of this StandInDetails.

        Indicates number of standin instruction debits.Possible values can be two digit number or UN (Until it is cancelled) or ND (Not defined).  # noqa: E501

        :param number_of_debits: The number_of_debits of this StandInDetails.  # noqa: E501
        :type: str
        """
        if number_of_debits is None:
            raise ValueError("Invalid value for `number_of_debits`, must not be `None`")  # noqa: E501
        if number_of_debits is not None and not re.search(r'(UN)|(ND)|([0-9]{2})', number_of_debits):  # noqa: E501
            raise ValueError(r"Invalid value for `number_of_debits`, must be a follow pattern or equal to `/(UN)|(ND)|([0-9]{2})/`")  # noqa: E501

        self._number_of_debits = number_of_debits

    @property
    def si_validated(self):
        """Gets the si_validated of this StandInDetails.  # noqa: E501

        Indicates standin instruction validation flag, it can be true or false. \"false\" - Not validated, \"true\" - Validated.  # noqa: E501

        :return: The si_validated of this StandInDetails.  # noqa: E501
        :rtype: bool
        """
        return self._si_validated

    @si_validated.setter
    def si_validated(self, si_validated):
        """Sets the si_validated of this StandInDetails.

        Indicates standin instruction validation flag, it can be true or false. \"false\" - Not validated, \"true\" - Validated.  # noqa: E501

        :param si_validated: The si_validated of this StandInDetails.  # noqa: E501
        :type: bool
        """
        if si_validated is None:
            raise ValueError("Invalid value for `si_validated`, must not be `None`")  # noqa: E501

        self._si_validated = si_validated

    @property
    def maximum_transaction_amount(self):
        """Gets the maximum_transaction_amount of this StandInDetails.  # noqa: E501

        Maximum debit amount per standin instruction transaction.  # noqa: E501

        :return: The maximum_transaction_amount of this StandInDetails.  # noqa: E501
        :rtype: float
        """
        return self._maximum_transaction_amount

    @maximum_transaction_amount.setter
    def maximum_transaction_amount(self, maximum_transaction_amount):
        """Sets the maximum_transaction_amount of this StandInDetails.

        Maximum debit amount per standin instruction transaction.  # noqa: E501

        :param maximum_transaction_amount: The maximum_transaction_amount of this StandInDetails.  # noqa: E501
        :type: float
        """
        if maximum_transaction_amount is None:
            raise ValueError("Invalid value for `maximum_transaction_amount`, must not be `None`")  # noqa: E501

        self._maximum_transaction_amount = maximum_transaction_amount

    @property
    def si_hub_id(self):
        """Gets the si_hub_id of this StandInDetails.  # noqa: E501

        Unique identifier for standin instruction.  # noqa: E501

        :return: The si_hub_id of this StandInDetails.  # noqa: E501
        :rtype: str
        """
        return self._si_hub_id

    @si_hub_id.setter
    def si_hub_id(self, si_hub_id):
        """Sets the si_hub_id of this StandInDetails.

        Unique identifier for standin instruction.  # noqa: E501

        :param si_hub_id: The si_hub_id of this StandInDetails.  # noqa: E501
        :type: str
        """
        if si_hub_id is None:
            raise ValueError("Invalid value for `si_hub_id`, must not be `None`")  # noqa: E501
        if si_hub_id is not None and len(si_hub_id) > 10:
            raise ValueError("Invalid value for `si_hub_id`, length must be less than or equal to `10`")  # noqa: E501

        self._si_hub_id = si_hub_id

    @property
    def frequency(self):
        """Gets the frequency of this StandInDetails.  # noqa: E501

        Indicates frequency of the standin instruction debit.  # noqa: E501

        :return: The frequency of this StandInDetails.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this StandInDetails.

        Indicates frequency of the standin instruction debit.  # noqa: E501

        :param frequency: The frequency of this StandInDetails.  # noqa: E501
        :type: str
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501
        allowed_values = ["WEEKLY", "FORTNIGHTLY", "MONTHLY", "QUARTERLY", "HALFYEARLY", "YEARLY", "UNSCHEDULED"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

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
        if not isinstance(other, StandInDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other