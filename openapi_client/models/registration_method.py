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


class RegistrationMethod(object):
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
        'method_type': 'str',
        'method_id': 'str',
        'user_defined': 'object',
        'billing_phone_number': 'str',
        'method_alias': 'str',
        'card': 'FraudRegistrationCard',
        'method_address': 'FraudAddress'
    }

    attribute_map = {
        'method_type': 'methodType',
        'method_id': 'methodId',
        'user_defined': 'userDefined',
        'billing_phone_number': 'billingPhoneNumber',
        'method_alias': 'methodAlias',
        'card': 'card',
        'method_address': 'methodAddress'
    }

    def __init__(self, method_type=None, method_id=None, user_defined=None, billing_phone_number=None, method_alias=None, card=None, method_address=None):  # noqa: E501
        """RegistrationMethod - a model defined in OpenAPI"""  # noqa: E501

        self._method_type = None
        self._method_id = None
        self._user_defined = None
        self._billing_phone_number = None
        self._method_alias = None
        self._card = None
        self._method_address = None
        self.discriminator = None

        self.method_type = method_type
        if method_id is not None:
            self.method_id = method_id
        if user_defined is not None:
            self.user_defined = user_defined
        if billing_phone_number is not None:
            self.billing_phone_number = billing_phone_number
        if method_alias is not None:
            self.method_alias = method_alias
        self.card = card
        if method_address is not None:
            self.method_address = method_address

    @property
    def method_type(self):
        """Gets the method_type of this RegistrationMethod.  # noqa: E501

        Unique ID for the payment method type.  # noqa: E501

        :return: The method_type of this RegistrationMethod.  # noqa: E501
        :rtype: str
        """
        return self._method_type

    @method_type.setter
    def method_type(self, method_type):
        """Sets the method_type of this RegistrationMethod.

        Unique ID for the payment method type.  # noqa: E501

        :param method_type: The method_type of this RegistrationMethod.  # noqa: E501
        :type: str
        """
        if method_type is None:
            raise ValueError("Invalid value for `method_type`, must not be `None`")  # noqa: E501
        allowed_values = ["method/card", "method/wallet"]  # noqa: E501
        if method_type not in allowed_values:
            raise ValueError(
                "Invalid value for `method_type` ({0}), must be one of {1}"  # noqa: E501
                .format(method_type, allowed_values)
            )

        self._method_type = method_type

    @property
    def method_id(self):
        """Gets the method_id of this RegistrationMethod.  # noqa: E501

        The unique ID of this payment method if it was previously registered with a registration/method or if it is currently being registered. Must be unique for the entire system (not just within a specific merchant or industry). Mandatory if being used inside a registration/method.  # noqa: E501

        :return: The method_id of this RegistrationMethod.  # noqa: E501
        :rtype: str
        """
        return self._method_id

    @method_id.setter
    def method_id(self, method_id):
        """Sets the method_id of this RegistrationMethod.

        The unique ID of this payment method if it was previously registered with a registration/method or if it is currently being registered. Must be unique for the entire system (not just within a specific merchant or industry). Mandatory if being used inside a registration/method.  # noqa: E501

        :param method_id: The method_id of this RegistrationMethod.  # noqa: E501
        :type: str
        """

        self._method_id = method_id

    @property
    def user_defined(self):
        """Gets the user_defined of this RegistrationMethod.  # noqa: E501

        A JSON object that carries any additional information that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this RegistrationMethod.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this RegistrationMethod.

        A JSON object that carries any additional information that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this RegistrationMethod.  # noqa: E501
        :type: object
        """

        self._user_defined = user_defined

    @property
    def billing_phone_number(self):
        """Gets the billing_phone_number of this RegistrationMethod.  # noqa: E501

        The address that should be used to send billing information for this payment method.  # noqa: E501

        :return: The billing_phone_number of this RegistrationMethod.  # noqa: E501
        :rtype: str
        """
        return self._billing_phone_number

    @billing_phone_number.setter
    def billing_phone_number(self, billing_phone_number):
        """Sets the billing_phone_number of this RegistrationMethod.

        The address that should be used to send billing information for this payment method.  # noqa: E501

        :param billing_phone_number: The billing_phone_number of this RegistrationMethod.  # noqa: E501
        :type: str
        """

        self._billing_phone_number = billing_phone_number

    @property
    def method_alias(self):
        """Gets the method_alias of this RegistrationMethod.  # noqa: E501

        The address that should be used to send billing information for this payment method.  # noqa: E501

        :return: The method_alias of this RegistrationMethod.  # noqa: E501
        :rtype: str
        """
        return self._method_alias

    @method_alias.setter
    def method_alias(self, method_alias):
        """Sets the method_alias of this RegistrationMethod.

        The address that should be used to send billing information for this payment method.  # noqa: E501

        :param method_alias: The method_alias of this RegistrationMethod.  # noqa: E501
        :type: str
        """

        self._method_alias = method_alias

    @property
    def card(self):
        """Gets the card of this RegistrationMethod.  # noqa: E501


        :return: The card of this RegistrationMethod.  # noqa: E501
        :rtype: FraudRegistrationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this RegistrationMethod.


        :param card: The card of this RegistrationMethod.  # noqa: E501
        :type: FraudRegistrationCard
        """
        if card is None:
            raise ValueError("Invalid value for `card`, must not be `None`")  # noqa: E501

        self._card = card

    @property
    def method_address(self):
        """Gets the method_address of this RegistrationMethod.  # noqa: E501


        :return: The method_address of this RegistrationMethod.  # noqa: E501
        :rtype: FraudAddress
        """
        return self._method_address

    @method_address.setter
    def method_address(self, method_address):
        """Sets the method_address of this RegistrationMethod.


        :param method_address: The method_address of this RegistrationMethod.  # noqa: E501
        :type: FraudAddress
        """

        self._method_address = method_address

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
        if not isinstance(other, RegistrationMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
