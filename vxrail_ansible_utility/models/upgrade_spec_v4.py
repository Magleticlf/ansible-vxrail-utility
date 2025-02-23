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

class UpgradeSpecV4(object):
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
        'bundle_file_locator': 'str',
        'vxrail': 'VxRailManagerSpec',
        'vcenter': 'VcenterEmbeddedPSCSpecV4',
        'target_hosts': 'list[HostBaseSpec]'
    }

    attribute_map = {
        'bundle_file_locator': 'bundle_file_locator',
        'vxrail': 'vxrail',
        'vcenter': 'vcenter',
        'target_hosts': 'target_hosts'
    }

    def __init__(self, bundle_file_locator=None, vxrail=None, vcenter=None, target_hosts=None):  # noqa: E501
        """UpgradeSpecV4 - a model defined in Swagger"""  # noqa: E501
        self._bundle_file_locator = None
        self._vxrail = None
        self._vcenter = None
        self._target_hosts = None
        self.discriminator = None
        self.bundle_file_locator = bundle_file_locator
        self.vxrail = vxrail
        self.vcenter = vcenter
        if target_hosts is not None:
            self.target_hosts = target_hosts

    @property
    def bundle_file_locator(self):
        """Gets the bundle_file_locator of this UpgradeSpecV4.  # noqa: E501

        The full path of the single upgrade bundle or first package of a multiple part upgrade bundle. [Note] Multi-part upgrades must follow required naming conventions -- (1) The first file (the installer file) contains \"installer\" in the name. (2) Users must not rename any files belonging to the multi-part bundle.  # noqa: E501

        :return: The bundle_file_locator of this UpgradeSpecV4.  # noqa: E501
        :rtype: str
        """
        return self._bundle_file_locator

    @bundle_file_locator.setter
    def bundle_file_locator(self, bundle_file_locator):
        """Sets the bundle_file_locator of this UpgradeSpecV4.

        The full path of the single upgrade bundle or first package of a multiple part upgrade bundle. [Note] Multi-part upgrades must follow required naming conventions -- (1) The first file (the installer file) contains \"installer\" in the name. (2) Users must not rename any files belonging to the multi-part bundle.  # noqa: E501

        :param bundle_file_locator: The bundle_file_locator of this UpgradeSpecV4.  # noqa: E501
        :type: str
        """
        if bundle_file_locator is None:
            raise ValueError("Invalid value for `bundle_file_locator`, must not be `None`")  # noqa: E501

        self._bundle_file_locator = bundle_file_locator

    @property
    def vxrail(self):
        """Gets the vxrail of this UpgradeSpecV4.  # noqa: E501


        :return: The vxrail of this UpgradeSpecV4.  # noqa: E501
        :rtype: VxRailManagerSpec
        """
        return self._vxrail

    @vxrail.setter
    def vxrail(self, vxrail):
        """Sets the vxrail of this UpgradeSpecV4.


        :param vxrail: The vxrail of this UpgradeSpecV4.  # noqa: E501
        :type: VxRailManagerSpec
        """
        if vxrail is None:
            raise ValueError("Invalid value for `vxrail`, must not be `None`")  # noqa: E501

        self._vxrail = vxrail

    @property
    def vcenter(self):
        """Gets the vcenter of this UpgradeSpecV4.  # noqa: E501


        :return: The vcenter of this UpgradeSpecV4.  # noqa: E501
        :rtype: VcenterEmbeddedPSCSpecV4
        """
        return self._vcenter

    @vcenter.setter
    def vcenter(self, vcenter):
        """Sets the vcenter of this UpgradeSpecV4.


        :param vcenter: The vcenter of this UpgradeSpecV4.  # noqa: E501
        :type: VcenterEmbeddedPSCSpecV4
        """
        if vcenter is None:
            raise ValueError("Invalid value for `vcenter`, must not be `None`")  # noqa: E501

        self._vcenter = vcenter

    @property
    def target_hosts(self):
        """Gets the target_hosts of this UpgradeSpecV4.  # noqa: E501

        Hosts to be upgraded  # noqa: E501

        :return: The target_hosts of this UpgradeSpecV4.  # noqa: E501
        :rtype: list[HostBaseSpec]
        """
        return self._target_hosts

    @target_hosts.setter
    def target_hosts(self, target_hosts):
        """Sets the target_hosts of this UpgradeSpecV4.

        Hosts to be upgraded  # noqa: E501

        :param target_hosts: The target_hosts of this UpgradeSpecV4.  # noqa: E501
        :type: list[HostBaseSpec]
        """

        self._target_hosts = target_hosts

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
        if issubclass(UpgradeSpecV4, dict):
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
        if not isinstance(other, UpgradeSpecV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
