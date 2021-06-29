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


class PaymentFacilitator(object):
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
        'external_merchant_id': 'str',
        'payment_facilitator_id': 'str',
        'sale_organization_id': 'str',
        'name': 'str',
        'sub_merchant_data': 'SubMerchantData'
    }

    attribute_map = {
        'external_merchant_id': 'externalMerchantId',
        'payment_facilitator_id': 'paymentFacilitatorId',
        'sale_organization_id': 'saleOrganizationId',
        'name': 'name',
        'sub_merchant_data': 'subMerchantData'
    }

    def __init__(self, external_merchant_id=None, payment_facilitator_id=None, sale_organization_id=None, name=None, sub_merchant_data=None):  # noqa: E501
        """PaymentFacilitator - a model defined in OpenAPI"""  # noqa: E501

        self._external_merchant_id = None
        self._payment_facilitator_id = None
        self._sale_organization_id = None
        self._name = None
        self._sub_merchant_data = None
        self.discriminator = None

        self.external_merchant_id = external_merchant_id
        self.payment_facilitator_id = payment_facilitator_id
        if sale_organization_id is not None:
            self.sale_organization_id = sale_organization_id
        self.name = name
        if sub_merchant_data is not None:
            self.sub_merchant_data = sub_merchant_data

    @property
    def external_merchant_id(self):
        """Gets the external_merchant_id of this PaymentFacilitator.  # noqa: E501

        External merchant ID of the payment facilitator.  # noqa: E501

        :return: The external_merchant_id of this PaymentFacilitator.  # noqa: E501
        :rtype: str
        """
        return self._external_merchant_id

    @external_merchant_id.setter
    def external_merchant_id(self, external_merchant_id):
        """Sets the external_merchant_id of this PaymentFacilitator.

        External merchant ID of the payment facilitator.  # noqa: E501

        :param external_merchant_id: The external_merchant_id of this PaymentFacilitator.  # noqa: E501
        :type: str
        """
        if external_merchant_id is None:
            raise ValueError("Invalid value for `external_merchant_id`, must not be `None`")  # noqa: E501
        if external_merchant_id is not None and not re.search(r'^(?!\s*$).+', external_merchant_id):  # noqa: E501
            raise ValueError(r"Invalid value for `external_merchant_id`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._external_merchant_id = external_merchant_id

    @property
    def payment_facilitator_id(self):
        """Gets the payment_facilitator_id of this PaymentFacilitator.  # noqa: E501

        Payment facilitator ID supplied during boarding.  # noqa: E501

        :return: The payment_facilitator_id of this PaymentFacilitator.  # noqa: E501
        :rtype: str
        """
        return self._payment_facilitator_id

    @payment_facilitator_id.setter
    def payment_facilitator_id(self, payment_facilitator_id):
        """Sets the payment_facilitator_id of this PaymentFacilitator.

        Payment facilitator ID supplied during boarding.  # noqa: E501

        :param payment_facilitator_id: The payment_facilitator_id of this PaymentFacilitator.  # noqa: E501
        :type: str
        """
        if payment_facilitator_id is None:
            raise ValueError("Invalid value for `payment_facilitator_id`, must not be `None`")  # noqa: E501
        if payment_facilitator_id is not None and not re.search(r'\d{1,11}', payment_facilitator_id):  # noqa: E501
            raise ValueError(r"Invalid value for `payment_facilitator_id`, must be a follow pattern or equal to `/\d{1,11}/`")  # noqa: E501

        self._payment_facilitator_id = payment_facilitator_id

    @property
    def sale_organization_id(self):
        """Gets the sale_organization_id of this PaymentFacilitator.  # noqa: E501

        Independent sales organization (ISO) ID provided by Mastercard.  # noqa: E501

        :return: The sale_organization_id of this PaymentFacilitator.  # noqa: E501
        :rtype: str
        """
        return self._sale_organization_id

    @sale_organization_id.setter
    def sale_organization_id(self, sale_organization_id):
        """Sets the sale_organization_id of this PaymentFacilitator.

        Independent sales organization (ISO) ID provided by Mastercard.  # noqa: E501

        :param sale_organization_id: The sale_organization_id of this PaymentFacilitator.  # noqa: E501
        :type: str
        """
        if sale_organization_id is not None and not re.search(r'\d{1,11}', sale_organization_id):  # noqa: E501
            raise ValueError(r"Invalid value for `sale_organization_id`, must be a follow pattern or equal to `/\d{1,11}/`")  # noqa: E501

        self._sale_organization_id = sale_organization_id

    @property
    def name(self):
        """Gets the name of this PaymentFacilitator.  # noqa: E501

        Payment facilitator name.  # noqa: E501

        :return: The name of this PaymentFacilitator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentFacilitator.

        Payment facilitator name.  # noqa: E501

        :param name: The name of this PaymentFacilitator.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if name is not None and not re.search(r'^(?!\s*$).+', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._name = name

    @property
    def sub_merchant_data(self):
        """Gets the sub_merchant_data of this PaymentFacilitator.  # noqa: E501


        :return: The sub_merchant_data of this PaymentFacilitator.  # noqa: E501
        :rtype: SubMerchantData
        """
        return self._sub_merchant_data

    @sub_merchant_data.setter
    def sub_merchant_data(self, sub_merchant_data):
        """Sets the sub_merchant_data of this PaymentFacilitator.


        :param sub_merchant_data: The sub_merchant_data of this PaymentFacilitator.  # noqa: E501
        :type: SubMerchantData
        """

        self._sub_merchant_data = sub_merchant_data

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
        if not isinstance(other, PaymentFacilitator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
