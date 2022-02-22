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

class StorageInfo(object):
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
        'disk_group_type': 'str',
        'slot_claims': 'list[StorageInfoSlotClaims]'
    }

    attribute_map = {
        'disk_group_type': 'disk_group_type',
        'slot_claims': 'slot_claims'
    }

    def __init__(self, disk_group_type=None, slot_claims=None):  # noqa: E501
        """StorageInfo - a model defined in Swagger"""  # noqa: E501
        self._disk_group_type = None
        self._slot_claims = None
        self.discriminator = None
        if disk_group_type is not None:
            self.disk_group_type = disk_group_type
        if slot_claims is not None:
            self.slot_claims = slot_claims

    @property
    def disk_group_type(self):
        """Gets the disk_group_type of this StorageInfo.  # noqa: E501


        :return: The disk_group_type of this StorageInfo.  # noqa: E501
        :rtype: str
        """
        return self._disk_group_type

    @disk_group_type.setter
    def disk_group_type(self, disk_group_type):
        """Sets the disk_group_type of this StorageInfo.


        :param disk_group_type: The disk_group_type of this StorageInfo.  # noqa: E501
        :type: str
        """

        self._disk_group_type = disk_group_type

    @property
    def slot_claims(self):
        """Gets the slot_claims of this StorageInfo.  # noqa: E501


        :return: The slot_claims of this StorageInfo.  # noqa: E501
        :rtype: list[StorageInfoSlotClaims]
        """
        return self._slot_claims

    @slot_claims.setter
    def slot_claims(self, slot_claims):
        """Sets the slot_claims of this StorageInfo.


        :param slot_claims: The slot_claims of this StorageInfo.  # noqa: E501
        :type: list[StorageInfoSlotClaims]
        """

        self._slot_claims = slot_claims

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
        if issubclass(StorageInfo, dict):
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
        if not isinstance(other, StorageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
