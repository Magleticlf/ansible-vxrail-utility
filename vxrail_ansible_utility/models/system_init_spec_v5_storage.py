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

class SystemInitSpecV5Storage(object):
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
        'primary_storage_type': 'str'
    }

    attribute_map = {
        'disk_group_type': 'disk_group_type',
        'primary_storage_type': 'primary_storage_type'
    }

    def __init__(self, disk_group_type=None, primary_storage_type=None):  # noqa: E501
        """SystemInitSpecV5Storage - a model defined in Swagger"""  # noqa: E501
        self._disk_group_type = None
        self._primary_storage_type = None
        self.discriminator = None
        if disk_group_type is not None:
            self.disk_group_type = disk_group_type
        if primary_storage_type is not None:
            self.primary_storage_type = primary_storage_type

    @property
    def disk_group_type(self):
        """Gets the disk_group_type of this SystemInitSpecV5Storage.  # noqa: E501

        The disk group configuration for the appliance. The property is used only for vSAN clusters.  # noqa: E501

        :return: The disk_group_type of this SystemInitSpecV5Storage.  # noqa: E501
        :rtype: str
        """
        return self._disk_group_type

    @disk_group_type.setter
    def disk_group_type(self, disk_group_type):
        """Sets the disk_group_type of this SystemInitSpecV5Storage.

        The disk group configuration for the appliance. The property is used only for vSAN clusters.  # noqa: E501

        :param disk_group_type: The disk_group_type of this SystemInitSpecV5Storage.  # noqa: E501
        :type: str
        """
        allowed_values = ["1001", "1002", "2403", "2404", "2804"]  # noqa: E501
        if disk_group_type not in allowed_values:
            raise ValueError(
                "Invalid value for `disk_group_type` ({0}), must be one of {1}"  # noqa: E501
                .format(disk_group_type, allowed_values)
            )

        self._disk_group_type = disk_group_type

    @property
    def primary_storage_type(self):
        """Gets the primary_storage_type of this SystemInitSpecV5Storage.  # noqa: E501

        The primary storage configuration for the appliance. This property is used only for dynamic node clusters.  # noqa: E501

        :return: The primary_storage_type of this SystemInitSpecV5Storage.  # noqa: E501
        :rtype: str
        """
        return self._primary_storage_type

    @primary_storage_type.setter
    def primary_storage_type(self, primary_storage_type):
        """Sets the primary_storage_type of this SystemInitSpecV5Storage.

        The primary storage configuration for the appliance. This property is used only for dynamic node clusters.  # noqa: E501

        :param primary_storage_type: The primary_storage_type of this SystemInitSpecV5Storage.  # noqa: E501
        :type: str
        """
        allowed_values = ["VMFS_ON_FC", "EXTERNAL"]  # noqa: E501
        if primary_storage_type not in allowed_values:
            raise ValueError(
                "Invalid value for `primary_storage_type` ({0}), must be one of {1}"  # noqa: E501
                .format(primary_storage_type, allowed_values)
            )

        self._primary_storage_type = primary_storage_type

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
        if issubclass(SystemInitSpecV5Storage, dict):
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
        if not isinstance(other, SystemInitSpecV5Storage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
