# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.350
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BayInfoWithDGBayId(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'slots': 'list[BayInfoWithDGBayIdSlots]'
    }

    attribute_map = {
        'slots': 'slots'
    }

    def __init__(self, slots=None):  # noqa: E501
        """BayInfoWithDGBayId - a model defined in Swagger"""  # noqa: E501
        self._slots = None
        self.discriminator = None
        if slots is not None:
            self.slots = slots

    @property
    def slots(self):
        """Gets the slots of this BayInfoWithDGBayId.  # noqa: E501

        A list of all vSAN slots  # noqa: E501

        :return: The slots of this BayInfoWithDGBayId.  # noqa: E501
        :rtype: list[BayInfoWithDGBayIdSlots]
        """
        return self._slots

    @slots.setter
    def slots(self, slots):
        """Sets the slots of this BayInfoWithDGBayId.

        A list of all vSAN slots  # noqa: E501

        :param slots: The slots of this BayInfoWithDGBayId.  # noqa: E501
        :type: list[BayInfoWithDGBayIdSlots]
        """

        self._slots = slots

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(BayInfoWithDGBayId, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BayInfoWithDGBayId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
