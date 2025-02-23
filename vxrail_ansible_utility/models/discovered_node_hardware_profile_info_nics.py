# coding: utf-8

"""
    Day1 Bring Up Configuration

    The set of Day 1 Bring Up Configuration API(s) are used to deploy VxRail cluster.  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class DiscoveredNodeHardwareProfileInfoNics(object):
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
        'name': 'str',
        'speed': 'float',
        'port_info': 'str',
        'product_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'speed': 'speed',
        'port_info': 'port_info',
        'product_name': 'product_name'
    }

    def __init__(self, name=None, speed=None, port_info=None, product_name=None):  # noqa: E501
        """DiscoveredNodeHardwareProfileInfoNics - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._speed = None
        self._port_info = None
        self._product_name = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if speed is not None:
            self.speed = speed
        if port_info is not None:
            self.port_info = port_info
        if product_name is not None:
            self.product_name = product_name

    @property
    def name(self):
        """Gets the name of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501

        NIC device name  # noqa: E501

        :return: The name of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiscoveredNodeHardwareProfileInfoNics.

        NIC device name  # noqa: E501

        :param name: The name of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def speed(self):
        """Gets the speed of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501

        NIC speed in MB  # noqa: E501

        :return: The speed of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this DiscoveredNodeHardwareProfileInfoNics.

        NIC speed in MB  # noqa: E501

        :param speed: The speed of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501
        :type: float
        """

        self._speed = speed

    @property
    def port_info(self):
        """Gets the port_info of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501

        Physical port information about the NIC  # noqa: E501

        :return: The port_info of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501
        :rtype: str
        """
        return self._port_info

    @port_info.setter
    def port_info(self, port_info):
        """Sets the port_info of this DiscoveredNodeHardwareProfileInfoNics.

        Physical port information about the NIC  # noqa: E501

        :param port_info: The port_info of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501
        :type: str
        """

        self._port_info = port_info

    @property
    def product_name(self):
        """Gets the product_name of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501

        NIC product name  # noqa: E501

        :return: The product_name of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this DiscoveredNodeHardwareProfileInfoNics.

        NIC product name  # noqa: E501

        :param product_name: The product_name of this DiscoveredNodeHardwareProfileInfoNics.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

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
        if issubclass(DiscoveredNodeHardwareProfileInfoNics, dict):
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
        if not isinstance(other, DiscoveredNodeHardwareProfileInfoNics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
