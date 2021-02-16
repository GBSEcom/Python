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


class InstallmentOptions(object):
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
        'number_of_installments': 'int',
        'installments_interest': 'bool',
        'installment_delay_months': 'int',
        'recurring_type': 'str',
        'merchant_advice_code_supported': 'bool'
    }

    attribute_map = {
        'number_of_installments': 'numberOfInstallments',
        'installments_interest': 'installmentsInterest',
        'installment_delay_months': 'installmentDelayMonths',
        'recurring_type': 'recurringType',
        'merchant_advice_code_supported': 'merchantAdviceCodeSupported'
    }

    def __init__(self, number_of_installments=None, installments_interest=None, installment_delay_months=None, recurring_type=None, merchant_advice_code_supported=None):  # noqa: E501
        """InstallmentOptions - a model defined in OpenAPI"""  # noqa: E501

        self._number_of_installments = None
        self._installments_interest = None
        self._installment_delay_months = None
        self._recurring_type = None
        self._merchant_advice_code_supported = None
        self.discriminator = None

        if number_of_installments is not None:
            self.number_of_installments = number_of_installments
        if installments_interest is not None:
            self.installments_interest = installments_interest
        if installment_delay_months is not None:
            self.installment_delay_months = installment_delay_months
        if recurring_type is not None:
            self.recurring_type = recurring_type
        if merchant_advice_code_supported is not None:
            self.merchant_advice_code_supported = merchant_advice_code_supported

    @property
    def number_of_installments(self):
        """Gets the number_of_installments of this InstallmentOptions.  # noqa: E501

        Number of installments for a sale transaction if the customer pays the total amount in multiple transactions.  # noqa: E501

        :return: The number_of_installments of this InstallmentOptions.  # noqa: E501
        :rtype: int
        """
        return self._number_of_installments

    @number_of_installments.setter
    def number_of_installments(self, number_of_installments):
        """Sets the number_of_installments of this InstallmentOptions.

        Number of installments for a sale transaction if the customer pays the total amount in multiple transactions.  # noqa: E501

        :param number_of_installments: The number_of_installments of this InstallmentOptions.  # noqa: E501
        :type: int
        """
        if number_of_installments is not None and number_of_installments > 99:  # noqa: E501
            raise ValueError("Invalid value for `number_of_installments`, must be a value less than or equal to `99`")  # noqa: E501
        if number_of_installments is not None and number_of_installments < 1:  # noqa: E501
            raise ValueError("Invalid value for `number_of_installments`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_installments = number_of_installments

    @property
    def installments_interest(self):
        """Gets the installments_interest of this InstallmentOptions.  # noqa: E501

        Indicates whether the installment interest amount has been applied.  # noqa: E501

        :return: The installments_interest of this InstallmentOptions.  # noqa: E501
        :rtype: bool
        """
        return self._installments_interest

    @installments_interest.setter
    def installments_interest(self, installments_interest):
        """Sets the installments_interest of this InstallmentOptions.

        Indicates whether the installment interest amount has been applied.  # noqa: E501

        :param installments_interest: The installments_interest of this InstallmentOptions.  # noqa: E501
        :type: bool
        """

        self._installments_interest = installments_interest

    @property
    def installment_delay_months(self):
        """Gets the installment_delay_months of this InstallmentOptions.  # noqa: E501

        The number of months the first installment payment will be delayed.  # noqa: E501

        :return: The installment_delay_months of this InstallmentOptions.  # noqa: E501
        :rtype: int
        """
        return self._installment_delay_months

    @installment_delay_months.setter
    def installment_delay_months(self, installment_delay_months):
        """Sets the installment_delay_months of this InstallmentOptions.

        The number of months the first installment payment will be delayed.  # noqa: E501

        :param installment_delay_months: The installment_delay_months of this InstallmentOptions.  # noqa: E501
        :type: int
        """
        if installment_delay_months is not None and installment_delay_months > 99:  # noqa: E501
            raise ValueError("Invalid value for `installment_delay_months`, must be a value less than or equal to `99`")  # noqa: E501
        if installment_delay_months is not None and installment_delay_months < 1:  # noqa: E501
            raise ValueError("Invalid value for `installment_delay_months`, must be a value greater than or equal to `1`")  # noqa: E501

        self._installment_delay_months = installment_delay_months

    @property
    def recurring_type(self):
        """Gets the recurring_type of this InstallmentOptions.  # noqa: E501

        The type of recurring payment.  # noqa: E501

        :return: The recurring_type of this InstallmentOptions.  # noqa: E501
        :rtype: str
        """
        return self._recurring_type

    @recurring_type.setter
    def recurring_type(self, recurring_type):
        """Sets the recurring_type of this InstallmentOptions.

        The type of recurring payment.  # noqa: E501

        :param recurring_type: The recurring_type of this InstallmentOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIRST", "REPEAT", "STANDING_INSTRUCTION"]  # noqa: E501
        if recurring_type not in allowed_values:
            raise ValueError(
                "Invalid value for `recurring_type` ({0}), must be one of {1}"  # noqa: E501
                .format(recurring_type, allowed_values)
            )

        self._recurring_type = recurring_type

    @property
    def merchant_advice_code_supported(self):
        """Gets the merchant_advice_code_supported of this InstallmentOptions.  # noqa: E501

        Indicates if the merchant supports merchant advice code (MAC) in order to receive table 55 code for a declined recurring transaction.  # noqa: E501

        :return: The merchant_advice_code_supported of this InstallmentOptions.  # noqa: E501
        :rtype: bool
        """
        return self._merchant_advice_code_supported

    @merchant_advice_code_supported.setter
    def merchant_advice_code_supported(self, merchant_advice_code_supported):
        """Sets the merchant_advice_code_supported of this InstallmentOptions.

        Indicates if the merchant supports merchant advice code (MAC) in order to receive table 55 code for a declined recurring transaction.  # noqa: E501

        :param merchant_advice_code_supported: The merchant_advice_code_supported of this InstallmentOptions.  # noqa: E501
        :type: bool
        """

        self._merchant_advice_code_supported = merchant_advice_code_supported

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
        if not isinstance(other, InstallmentOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
