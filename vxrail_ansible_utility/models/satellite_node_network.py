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

class SatelliteNodeNetwork(object):
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
        'type': 'str',
        'ip': 'str',
        'netmask': 'str',
        'gateway': 'str',
        'vlan': 'int'
    }

    attribute_map = {
        'type': 'type',
        'ip': 'ip',
        'netmask': 'netmask',
        'gateway': 'gateway',
        'vlan': 'vlan'
    }

    def __init__(self, type=None, ip=None, netmask=None, gateway=None, vlan=None):  # noqa: E501
        """SatelliteNodeNetwork - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._ip = None
        self._netmask = None
        self._gateway = None
        self._vlan = None
        self.discriminator = None
        self.type = type
        self.ip = ip
        self.netmask = netmask
        self.gateway = gateway
        self.vlan = vlan

    @property
    def type(self):
        """Gets the type of this SatelliteNodeNetwork.  # noqa: E501

        Type of component. Supported values include MANAGEMENT  # noqa: E501

        :return: The type of this SatelliteNodeNetwork.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SatelliteNodeNetwork.

        Type of component. Supported values include MANAGEMENT  # noqa: E501

        :param type: The type of this SatelliteNodeNetwork.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def ip(self):
        """Gets the ip of this SatelliteNodeNetwork.  # noqa: E501

        IP address of the component  # noqa: E501

        :return: The ip of this SatelliteNodeNetwork.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SatelliteNodeNetwork.

        IP address of the component  # noqa: E501

        :param ip: The ip of this SatelliteNodeNetwork.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def netmask(self):
        """Gets the netmask of this SatelliteNodeNetwork.  # noqa: E501

        Netmask the component  # noqa: E501

        :return: The netmask of this SatelliteNodeNetwork.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this SatelliteNodeNetwork.

        Netmask the component  # noqa: E501

        :param netmask: The netmask of this SatelliteNodeNetwork.  # noqa: E501
        :type: str
        """
        if netmask is None:
            raise ValueError("Invalid value for `netmask`, must not be `None`")  # noqa: E501

        self._netmask = netmask

    @property
    def gateway(self):
        """Gets the gateway of this SatelliteNodeNetwork.  # noqa: E501

        Gateway of the component  # noqa: E501

        :return: The gateway of this SatelliteNodeNetwork.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this SatelliteNodeNetwork.

        Gateway of the component  # noqa: E501

        :param gateway: The gateway of this SatelliteNodeNetwork.  # noqa: E501
        :type: str
        """
        if gateway is None:
            raise ValueError("Invalid value for `gateway`, must not be `None`")  # noqa: E501

        self._gateway = gateway

    @property
    def vlan(self):
        """Gets the vlan of this SatelliteNodeNetwork.  # noqa: E501

        Vlan of the component  # noqa: E501

        :return: The vlan of this SatelliteNodeNetwork.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this SatelliteNodeNetwork.

        Vlan of the component  # noqa: E501

        :param vlan: The vlan of this SatelliteNodeNetwork.  # noqa: E501
        :type: int
        """
        if vlan is None:
            raise ValueError("Invalid value for `vlan`, must not be `None`")  # noqa: E501

        self._vlan = vlan

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
        if issubclass(SatelliteNodeNetwork, dict):
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
        if not isinstance(other, SatelliteNodeNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other