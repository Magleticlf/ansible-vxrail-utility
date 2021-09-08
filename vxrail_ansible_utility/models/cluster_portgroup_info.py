# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ClusterPortgroupInfo(object):
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
        'portgroups': 'list[ClusterPortgroup]'
    }

    attribute_map = {
        'portgroups': 'portgroups'
    }

    def __init__(self, portgroups=None):  # noqa: E501
        """ClusterPortgroupInfo - a model defined in Swagger"""  # noqa: E501
        self._portgroups = None
        self.discriminator = None
        self.portgroups = portgroups

    @property
    def portgroups(self):
        """Gets the portgroups of this ClusterPortgroupInfo.  # noqa: E501

        Information about the portgroup  # noqa: E501

        :return: The portgroups of this ClusterPortgroupInfo.  # noqa: E501
        :rtype: list[ClusterPortgroup]
        """
        return self._portgroups

    @portgroups.setter
    def portgroups(self, portgroups):
        """Sets the portgroups of this ClusterPortgroupInfo.

        Information about the portgroup  # noqa: E501

        :param portgroups: The portgroups of this ClusterPortgroupInfo.  # noqa: E501
        :type: list[ClusterPortgroup]
        """
        if portgroups is None:
            raise ValueError("Invalid value for `portgroups`, must not be `None`")  # noqa: E501

        self._portgroups = portgroups

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
        if issubclass(ClusterPortgroupInfo, dict):
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
        if not isinstance(other, ClusterPortgroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other