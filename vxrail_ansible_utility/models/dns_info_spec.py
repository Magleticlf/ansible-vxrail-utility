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

class DNSInfoSpec(object):
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
        'components': 'str',
        'vcenter': 'User',
        'servers': 'list[str]'
    }

    attribute_map = {
        'components': 'components',
        'vcenter': 'vcenter',
        'servers': 'servers'
    }

    def __init__(self, components=None, vcenter=None, servers=None):  # noqa: E501
        """DNSInfoSpec - a model defined in Swagger"""  # noqa: E501
        self._components = None
        self._vcenter = None
        self._servers = None
        self.discriminator = None
        self.components = components
        self.vcenter = vcenter
        self.servers = servers

    @property
    def components(self):
        """Gets the components of this DNSInfoSpec.  # noqa: E501

        Indicates which DNS servers are updated. Supported values are \"VXM\" or \"ALL\". \"ALL\" is the default. If ALL is set, all DNS servers in the cluster are replaced. If VXM is set, only the DNS server for VxRail Manager is replaced.  # noqa: E501

        :return: The components of this DNSInfoSpec.  # noqa: E501
        :rtype: str
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this DNSInfoSpec.

        Indicates which DNS servers are updated. Supported values are \"VXM\" or \"ALL\". \"ALL\" is the default. If ALL is set, all DNS servers in the cluster are replaced. If VXM is set, only the DNS server for VxRail Manager is replaced.  # noqa: E501

        :param components: The components of this DNSInfoSpec.  # noqa: E501
        :type: str
        """
        if components is None:
            raise ValueError("Invalid value for `components`, must not be `None`")  # noqa: E501

        self._components = components

    @property
    def vcenter(self):
        """Gets the vcenter of this DNSInfoSpec.  # noqa: E501


        :return: The vcenter of this DNSInfoSpec.  # noqa: E501
        :rtype: User
        """
        return self._vcenter

    @vcenter.setter
    def vcenter(self, vcenter):
        """Sets the vcenter of this DNSInfoSpec.


        :param vcenter: The vcenter of this DNSInfoSpec.  # noqa: E501
        :type: User
        """
        if vcenter is None:
            raise ValueError("Invalid value for `vcenter`, must not be `None`")  # noqa: E501

        self._vcenter = vcenter

    @property
    def servers(self):
        """Gets the servers of this DNSInfoSpec.  # noqa: E501

        A list of IP addresses for the DNS servers  # noqa: E501

        :return: The servers of this DNSInfoSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this DNSInfoSpec.

        A list of IP addresses for the DNS servers  # noqa: E501

        :param servers: The servers of this DNSInfoSpec.  # noqa: E501
        :type: list[str]
        """
        if servers is None:
            raise ValueError("Invalid value for `servers`, must not be `None`")  # noqa: E501

        self._servers = servers

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
        if issubclass(DNSInfoSpec, dict):
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
        if not isinstance(other, DNSInfoSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
