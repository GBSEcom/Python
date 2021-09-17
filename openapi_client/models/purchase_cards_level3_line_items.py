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


class PurchaseCardsLevel3LineItems(object):
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
        'commodity_code': 'str',
        'product_code': 'str',
        'description': 'str',
        'quantity': 'int',
        'unit_measure': 'str',
        'unit_price': 'float',
        'vat_amount_and_rate': 'AdditionalAmountRate',
        'discount_amount_and_rate': 'AdditionalAmountRate',
        'line_item_total': 'float'
    }

    attribute_map = {
        'commodity_code': 'commodityCode',
        'product_code': 'productCode',
        'description': 'description',
        'quantity': 'quantity',
        'unit_measure': 'unitMeasure',
        'unit_price': 'unitPrice',
        'vat_amount_and_rate': 'vatAmountAndRate',
        'discount_amount_and_rate': 'discountAmountAndRate',
        'line_item_total': 'lineItemTotal'
    }

    def __init__(self, commodity_code=None, product_code=None, description=None, quantity=None, unit_measure=None, unit_price=None, vat_amount_and_rate=None, discount_amount_and_rate=None, line_item_total=None):  # noqa: E501
        """PurchaseCardsLevel3LineItems - a model defined in OpenAPI"""  # noqa: E501

        self._commodity_code = None
        self._product_code = None
        self._description = None
        self._quantity = None
        self._unit_measure = None
        self._unit_price = None
        self._vat_amount_and_rate = None
        self._discount_amount_and_rate = None
        self._line_item_total = None
        self.discriminator = None

        if commodity_code is not None:
            self.commodity_code = commodity_code
        if product_code is not None:
            self.product_code = product_code
        if description is not None:
            self.description = description
        if quantity is not None:
            self.quantity = quantity
        if unit_measure is not None:
            self.unit_measure = unit_measure
        if unit_price is not None:
            self.unit_price = unit_price
        if vat_amount_and_rate is not None:
            self.vat_amount_and_rate = vat_amount_and_rate
        if discount_amount_and_rate is not None:
            self.discount_amount_and_rate = discount_amount_and_rate
        if line_item_total is not None:
            self.line_item_total = line_item_total

    @property
    def commodity_code(self):
        """Gets the commodity_code of this PurchaseCardsLevel3LineItems.  # noqa: E501

        The commodity code used to classify the item purchased.  # noqa: E501

        :return: The commodity_code of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :rtype: str
        """
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, commodity_code):
        """Sets the commodity_code of this PurchaseCardsLevel3LineItems.

        The commodity code used to classify the item purchased.  # noqa: E501

        :param commodity_code: The commodity_code of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :type: str
        """
        if commodity_code is not None and len(commodity_code) > 4:
            raise ValueError("Invalid value for `commodity_code`, length must be less than or equal to `4`")  # noqa: E501

        self._commodity_code = commodity_code

    @property
    def product_code(self):
        """Gets the product_code of this PurchaseCardsLevel3LineItems.  # noqa: E501

        Merchant product identifier/the Universal Product Code (UPC) of the item purchased.  # noqa: E501

        :return: The product_code of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this PurchaseCardsLevel3LineItems.

        Merchant product identifier/the Universal Product Code (UPC) of the item purchased.  # noqa: E501

        :param product_code: The product_code of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :type: str
        """
        if product_code is not None and len(product_code) > 20:
            raise ValueError("Invalid value for `product_code`, length must be less than or equal to `20`")  # noqa: E501

        self._product_code = product_code

    @property
    def description(self):
        """Gets the description of this PurchaseCardsLevel3LineItems.  # noqa: E501

        The description.  # noqa: E501

        :return: The description of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PurchaseCardsLevel3LineItems.

        The description.  # noqa: E501

        :param description: The description of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 30:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `30`")  # noqa: E501

        self._description = description

    @property
    def quantity(self):
        """Gets the quantity of this PurchaseCardsLevel3LineItems.  # noqa: E501

        The quantity.  # noqa: E501

        :return: The quantity of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PurchaseCardsLevel3LineItems.

        The quantity.  # noqa: E501

        :param quantity: The quantity of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :type: int
        """
        if quantity is not None and quantity < 1:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")  # noqa: E501

        self._quantity = quantity

    @property
    def unit_measure(self):
        """Gets the unit_measure of this PurchaseCardsLevel3LineItems.  # noqa: E501

        The unit of measure.  # noqa: E501

        :return: The unit_measure of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :rtype: str
        """
        return self._unit_measure

    @unit_measure.setter
    def unit_measure(self, unit_measure):
        """Sets the unit_measure of this PurchaseCardsLevel3LineItems.

        The unit of measure.  # noqa: E501

        :param unit_measure: The unit_measure of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :type: str
        """
        if unit_measure is not None and len(unit_measure) > 3:
            raise ValueError("Invalid value for `unit_measure`, length must be less than or equal to `3`")  # noqa: E501

        self._unit_measure = unit_measure

    @property
    def unit_price(self):
        """Gets the unit_price of this PurchaseCardsLevel3LineItems.  # noqa: E501

        Rate amount in 3 decimal 12 bytes total digit.  # noqa: E501

        :return: The unit_price of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this PurchaseCardsLevel3LineItems.

        Rate amount in 3 decimal 12 bytes total digit.  # noqa: E501

        :param unit_price: The unit_price of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def vat_amount_and_rate(self):
        """Gets the vat_amount_and_rate of this PurchaseCardsLevel3LineItems.  # noqa: E501


        :return: The vat_amount_and_rate of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :rtype: AdditionalAmountRate
        """
        return self._vat_amount_and_rate

    @vat_amount_and_rate.setter
    def vat_amount_and_rate(self, vat_amount_and_rate):
        """Sets the vat_amount_and_rate of this PurchaseCardsLevel3LineItems.


        :param vat_amount_and_rate: The vat_amount_and_rate of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :type: AdditionalAmountRate
        """

        self._vat_amount_and_rate = vat_amount_and_rate

    @property
    def discount_amount_and_rate(self):
        """Gets the discount_amount_and_rate of this PurchaseCardsLevel3LineItems.  # noqa: E501


        :return: The discount_amount_and_rate of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :rtype: AdditionalAmountRate
        """
        return self._discount_amount_and_rate

    @discount_amount_and_rate.setter
    def discount_amount_and_rate(self, discount_amount_and_rate):
        """Sets the discount_amount_and_rate of this PurchaseCardsLevel3LineItems.


        :param discount_amount_and_rate: The discount_amount_and_rate of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :type: AdditionalAmountRate
        """

        self._discount_amount_and_rate = discount_amount_and_rate

    @property
    def line_item_total(self):
        """Gets the line_item_total of this PurchaseCardsLevel3LineItems.  # noqa: E501

        Rate amount in 3 decimal 12 bytes total digit.  # noqa: E501

        :return: The line_item_total of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :rtype: float
        """
        return self._line_item_total

    @line_item_total.setter
    def line_item_total(self, line_item_total):
        """Sets the line_item_total of this PurchaseCardsLevel3LineItems.

        Rate amount in 3 decimal 12 bytes total digit.  # noqa: E501

        :param line_item_total: The line_item_total of this PurchaseCardsLevel3LineItems.  # noqa: E501
        :type: float
        """

        self._line_item_total = line_item_total

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
        if not isinstance(other, PurchaseCardsLevel3LineItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
