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

class IdracNetworkInfoVlan(object):
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
        'vlan_id': 'int',
        'vlan_priority': 'int'
    }

    attribute_map = {
        'vlan_id': 'vlan_id',
        'vlan_priority': 'vlan_priority'
    }

    def __init__(self, vlan_id=None, vlan_priority=None):  # noqa: E501
        """IdracNetworkInfoVlan - a model defined in Swagger"""  # noqa: E501
        self._vlan_id = None
        self._vlan_priority = None
        self.discriminator = None
        if vlan_id is not None:
            self.vlan_id = vlan_id
        if vlan_priority is not None:
            self.vlan_priority = vlan_priority

    @property
    def vlan_id(self):
        """Gets the vlan_id of this IdracNetworkInfoVlan.  # noqa: E501

        The VLAN ID setting of the iDRAC  # noqa: E501

        :return: The vlan_id of this IdracNetworkInfoVlan.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this IdracNetworkInfoVlan.

        The VLAN ID setting of the iDRAC  # noqa: E501

        :param vlan_id: The vlan_id of this IdracNetworkInfoVlan.  # noqa: E501
        :type: int
        """

        self._vlan_id = vlan_id

    @property
    def vlan_priority(self):
        """Gets the vlan_priority of this IdracNetworkInfoVlan.  # noqa: E501

        The VLAN priority setting of the iDRAC  # noqa: E501

        :return: The vlan_priority of this IdracNetworkInfoVlan.  # noqa: E501
        :rtype: int
        """
        return self._vlan_priority

    @vlan_priority.setter
    def vlan_priority(self, vlan_priority):
        """Sets the vlan_priority of this IdracNetworkInfoVlan.

        The VLAN priority setting of the iDRAC  # noqa: E501

        :param vlan_priority: The vlan_priority of this IdracNetworkInfoVlan.  # noqa: E501
        :type: int
        """

        self._vlan_priority = vlan_priority

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
        if issubclass(IdracNetworkInfoVlan, dict):
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
        if not isinstance(other, IdracNetworkInfoVlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
