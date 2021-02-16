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


class FontProperties(object):
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
        'font_face': 'FontFace',
        'font_size': 'str',
        'font_weight': 'FontWeight',
        'font_color': 'str'
    }

    attribute_map = {
        'font_face': 'fontFace',
        'font_size': 'fontSize',
        'font_weight': 'fontWeight',
        'font_color': 'fontColor'
    }

    def __init__(self, font_face=None, font_size=None, font_weight=None, font_color=None):  # noqa: E501
        """FontProperties - a model defined in OpenAPI"""  # noqa: E501

        self._font_face = None
        self._font_size = None
        self._font_weight = None
        self._font_color = None
        self.discriminator = None

        if font_face is not None:
            self.font_face = font_face
        if font_size is not None:
            self.font_size = font_size
        if font_weight is not None:
            self.font_weight = font_weight
        if font_color is not None:
            self.font_color = font_color

    @property
    def font_face(self):
        """Gets the font_face of this FontProperties.  # noqa: E501


        :return: The font_face of this FontProperties.  # noqa: E501
        :rtype: FontFace
        """
        return self._font_face

    @font_face.setter
    def font_face(self, font_face):
        """Sets the font_face of this FontProperties.


        :param font_face: The font_face of this FontProperties.  # noqa: E501
        :type: FontFace
        """

        self._font_face = font_face

    @property
    def font_size(self):
        """Gets the font_size of this FontProperties.  # noqa: E501

        Font size property.  # noqa: E501

        :return: The font_size of this FontProperties.  # noqa: E501
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this FontProperties.

        Font size property.  # noqa: E501

        :param font_size: The font_size of this FontProperties.  # noqa: E501
        :type: str
        """

        self._font_size = font_size

    @property
    def font_weight(self):
        """Gets the font_weight of this FontProperties.  # noqa: E501


        :return: The font_weight of this FontProperties.  # noqa: E501
        :rtype: FontWeight
        """
        return self._font_weight

    @font_weight.setter
    def font_weight(self, font_weight):
        """Sets the font_weight of this FontProperties.


        :param font_weight: The font_weight of this FontProperties.  # noqa: E501
        :type: FontWeight
        """

        self._font_weight = font_weight

    @property
    def font_color(self):
        """Gets the font_color of this FontProperties.  # noqa: E501

        Hexadecimal color value.  # noqa: E501

        :return: The font_color of this FontProperties.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this FontProperties.

        Hexadecimal color value.  # noqa: E501

        :param font_color: The font_color of this FontProperties.  # noqa: E501
        :type: str
        """
        if font_color is not None and not re.search(r'(^(0[xX]){1}[A-Fa-f0-9]+$)|(^#[A-Fa-f0-9]{6}$)', font_color):  # noqa: E501
            raise ValueError(r"Invalid value for `font_color`, must be a follow pattern or equal to `/(^(0[xX]){1}[A-Fa-f0-9]+$)|(^#[A-Fa-f0-9]{6}$)/`")  # noqa: E501

        self._font_color = font_color

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
        if not isinstance(other, FontProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
