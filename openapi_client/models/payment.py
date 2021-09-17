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


class Payment(object):
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
        'payment_type': 'str',
        'method': 'Method',
        'pin_present': 'bool',
        'entry_method': 'str',
        'issuer_response': 'IssuerResponse',
        'issuer_approved_amount': 'str',
        'issuer_card_balance': 'str',
        'verification_avs': 'VerificationAvs',
        'verification3ds': 'Verification3ds',
        'verification_cvv': 'VerificationCvv',
        'user_defined': 'object'
    }

    attribute_map = {
        'payment_type': 'paymentType',
        'method': 'method',
        'pin_present': 'pinPresent',
        'entry_method': 'entryMethod',
        'issuer_response': 'issuerResponse',
        'issuer_approved_amount': 'issuerApprovedAmount',
        'issuer_card_balance': 'issuerCardBalance',
        'verification_avs': 'verificationAvs',
        'verification3ds': 'verification3ds',
        'verification_cvv': 'verificationCvv',
        'user_defined': 'userDefined'
    }

    def __init__(self, payment_type=None, method=None, pin_present=None, entry_method=None, issuer_response=None, issuer_approved_amount=None, issuer_card_balance=None, verification_avs=None, verification3ds=None, verification_cvv=None, user_defined=None):  # noqa: E501
        """Payment - a model defined in OpenAPI"""  # noqa: E501

        self._payment_type = None
        self._method = None
        self._pin_present = None
        self._entry_method = None
        self._issuer_response = None
        self._issuer_approved_amount = None
        self._issuer_card_balance = None
        self._verification_avs = None
        self._verification3ds = None
        self._verification_cvv = None
        self._user_defined = None
        self.discriminator = None

        self.payment_type = payment_type
        self.method = method
        self.pin_present = pin_present
        self.entry_method = entry_method
        if issuer_response is not None:
            self.issuer_response = issuer_response
        if issuer_approved_amount is not None:
            self.issuer_approved_amount = issuer_approved_amount
        if issuer_card_balance is not None:
            self.issuer_card_balance = issuer_card_balance
        if verification_avs is not None:
            self.verification_avs = verification_avs
        if verification3ds is not None:
            self.verification3ds = verification3ds
        if verification_cvv is not None:
            self.verification_cvv = verification_cvv
        if user_defined is not None:
            self.user_defined = user_defined

    @property
    def payment_type(self):
        """Gets the payment_type of this Payment.  # noqa: E501

        Defines the type of the payment.  # noqa: E501

        :return: The payment_type of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this Payment.

        Defines the type of the payment.  # noqa: E501

        :param payment_type: The payment_type of this Payment.  # noqa: E501
        :type: str
        """
        if payment_type is None:
            raise ValueError("Invalid value for `payment_type`, must not be `None`")  # noqa: E501
        allowed_values = ["payment/card", "payment/wallet"]  # noqa: E501
        if payment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_type, allowed_values)
            )

        self._payment_type = payment_type

    @property
    def method(self):
        """Gets the method of this Payment.  # noqa: E501


        :return: The method of this Payment.  # noqa: E501
        :rtype: Method
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Payment.


        :param method: The method of this Payment.  # noqa: E501
        :type: Method
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def pin_present(self):
        """Gets the pin_present of this Payment.  # noqa: E501

        Indicates if the cards Personal Identification Number was supplied.  # noqa: E501

        :return: The pin_present of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._pin_present

    @pin_present.setter
    def pin_present(self, pin_present):
        """Sets the pin_present of this Payment.

        Indicates if the cards Personal Identification Number was supplied.  # noqa: E501

        :param pin_present: The pin_present of this Payment.  # noqa: E501
        :type: bool
        """
        if pin_present is None:
            raise ValueError("Invalid value for `pin_present`, must not be `None`")  # noqa: E501

        self._pin_present = pin_present

    @property
    def entry_method(self):
        """Gets the entry_method of this Payment.  # noqa: E501

        The method in which the card information entered the system.  # noqa: E501

        :return: The entry_method of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._entry_method

    @entry_method.setter
    def entry_method(self, entry_method):
        """Sets the entry_method of this Payment.

        The method in which the card information entered the system.  # noqa: E501

        :param entry_method: The entry_method of this Payment.  # noqa: E501
        :type: str
        """
        if entry_method is None:
            raise ValueError("Invalid value for `entry_method`, must not be `None`")  # noqa: E501
        allowed_values = ["manual", "stripe", "ocr", "emv", "nfc", "remote", "pin_present"]  # noqa: E501
        if entry_method not in allowed_values:
            raise ValueError(
                "Invalid value for `entry_method` ({0}), must be one of {1}"  # noqa: E501
                .format(entry_method, allowed_values)
            )

        self._entry_method = entry_method

    @property
    def issuer_response(self):
        """Gets the issuer_response of this Payment.  # noqa: E501


        :return: The issuer_response of this Payment.  # noqa: E501
        :rtype: IssuerResponse
        """
        return self._issuer_response

    @issuer_response.setter
    def issuer_response(self, issuer_response):
        """Sets the issuer_response of this Payment.


        :param issuer_response: The issuer_response of this Payment.  # noqa: E501
        :type: IssuerResponse
        """

        self._issuer_response = issuer_response

    @property
    def issuer_approved_amount(self):
        """Gets the issuer_approved_amount of this Payment.  # noqa: E501

        The actual approved amount. This field should be filled in when the message has already passed through the issuer (e.g. post-authorization). For transaction/authorization this amount refers to the amount that was locked on the card-holders account.  # noqa: E501

        :return: The issuer_approved_amount of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._issuer_approved_amount

    @issuer_approved_amount.setter
    def issuer_approved_amount(self, issuer_approved_amount):
        """Sets the issuer_approved_amount of this Payment.

        The actual approved amount. This field should be filled in when the message has already passed through the issuer (e.g. post-authorization). For transaction/authorization this amount refers to the amount that was locked on the card-holders account.  # noqa: E501

        :param issuer_approved_amount: The issuer_approved_amount of this Payment.  # noqa: E501
        :type: str
        """

        self._issuer_approved_amount = issuer_approved_amount

    @property
    def issuer_card_balance(self):
        """Gets the issuer_card_balance of this Payment.  # noqa: E501

        The payment methods account balance if available. This field should be filled in when the message has already passed through the issuer (e.g. post-authorization).  # noqa: E501

        :return: The issuer_card_balance of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._issuer_card_balance

    @issuer_card_balance.setter
    def issuer_card_balance(self, issuer_card_balance):
        """Sets the issuer_card_balance of this Payment.

        The payment methods account balance if available. This field should be filled in when the message has already passed through the issuer (e.g. post-authorization).  # noqa: E501

        :param issuer_card_balance: The issuer_card_balance of this Payment.  # noqa: E501
        :type: str
        """

        self._issuer_card_balance = issuer_card_balance

    @property
    def verification_avs(self):
        """Gets the verification_avs of this Payment.  # noqa: E501


        :return: The verification_avs of this Payment.  # noqa: E501
        :rtype: VerificationAvs
        """
        return self._verification_avs

    @verification_avs.setter
    def verification_avs(self, verification_avs):
        """Sets the verification_avs of this Payment.


        :param verification_avs: The verification_avs of this Payment.  # noqa: E501
        :type: VerificationAvs
        """

        self._verification_avs = verification_avs

    @property
    def verification3ds(self):
        """Gets the verification3ds of this Payment.  # noqa: E501


        :return: The verification3ds of this Payment.  # noqa: E501
        :rtype: Verification3ds
        """
        return self._verification3ds

    @verification3ds.setter
    def verification3ds(self, verification3ds):
        """Sets the verification3ds of this Payment.


        :param verification3ds: The verification3ds of this Payment.  # noqa: E501
        :type: Verification3ds
        """

        self._verification3ds = verification3ds

    @property
    def verification_cvv(self):
        """Gets the verification_cvv of this Payment.  # noqa: E501


        :return: The verification_cvv of this Payment.  # noqa: E501
        :rtype: VerificationCvv
        """
        return self._verification_cvv

    @verification_cvv.setter
    def verification_cvv(self, verification_cvv):
        """Sets the verification_cvv of this Payment.


        :param verification_cvv: The verification_cvv of this Payment.  # noqa: E501
        :type: VerificationCvv
        """

        self._verification_cvv = verification_cvv

    @property
    def user_defined(self):
        """Gets the user_defined of this Payment.  # noqa: E501

        A JSON object that carries any additional information that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this Payment.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this Payment.

        A JSON object that carries any additional information that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this Payment.  # noqa: E501
        :type: object
        """

        self._user_defined = user_defined

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
        if not isinstance(other, Payment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
