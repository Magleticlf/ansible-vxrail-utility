# coding: utf-8

"""
    VxRail Host Management

    APIs for host management  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class FirmwareInfoV2(object):
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
        'bios_revision': 'str',
        'bmc_revision': 'str',
        'hba_version': 'str',
        'expander_bpf_version': 'str',
        'nonexpander_bpf_version': 'str',
        'boss_version': 'str',
        'cpld_version': 'str',
        'dcpm_version': 'str'
    }

    attribute_map = {
        'bios_revision': 'bios_revision',
        'bmc_revision': 'bmc_revision',
        'hba_version': 'hba_version',
        'expander_bpf_version': 'expander_bpf_version',
        'nonexpander_bpf_version': 'nonexpander_bpf_version',
        'boss_version': 'boss_version',
        'cpld_version': 'cpld_version',
        'dcpm_version': 'dcpm_version'
    }

    def __init__(self, bios_revision=None, bmc_revision=None, hba_version=None, expander_bpf_version=None, nonexpander_bpf_version=None, boss_version=None, cpld_version=None, dcpm_version=None):  # noqa: E501
        """FirmwareInfoV2 - a model defined in Swagger"""  # noqa: E501
        self._bios_revision = None
        self._bmc_revision = None
        self._hba_version = None
        self._expander_bpf_version = None
        self._nonexpander_bpf_version = None
        self._boss_version = None
        self._cpld_version = None
        self._dcpm_version = None
        self.discriminator = None
        if bios_revision is not None:
            self.bios_revision = bios_revision
        if bmc_revision is not None:
            self.bmc_revision = bmc_revision
        if hba_version is not None:
            self.hba_version = hba_version
        if expander_bpf_version is not None:
            self.expander_bpf_version = expander_bpf_version
        if nonexpander_bpf_version is not None:
            self.nonexpander_bpf_version = nonexpander_bpf_version
        if boss_version is not None:
            self.boss_version = boss_version
        if cpld_version is not None:
            self.cpld_version = cpld_version
        if dcpm_version is not None:
            self.dcpm_version = dcpm_version

    @property
    def bios_revision(self):
        """Gets the bios_revision of this FirmwareInfoV2.  # noqa: E501

        Version of the BIOS firmware  # noqa: E501

        :return: The bios_revision of this FirmwareInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._bios_revision

    @bios_revision.setter
    def bios_revision(self, bios_revision):
        """Sets the bios_revision of this FirmwareInfoV2.

        Version of the BIOS firmware  # noqa: E501

        :param bios_revision: The bios_revision of this FirmwareInfoV2.  # noqa: E501
        :type: str
        """

        self._bios_revision = bios_revision

    @property
    def bmc_revision(self):
        """Gets the bmc_revision of this FirmwareInfoV2.  # noqa: E501

        Version of the baseboard management controller (BMC) firmware  # noqa: E501

        :return: The bmc_revision of this FirmwareInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._bmc_revision

    @bmc_revision.setter
    def bmc_revision(self, bmc_revision):
        """Sets the bmc_revision of this FirmwareInfoV2.

        Version of the baseboard management controller (BMC) firmware  # noqa: E501

        :param bmc_revision: The bmc_revision of this FirmwareInfoV2.  # noqa: E501
        :type: str
        """

        self._bmc_revision = bmc_revision

    @property
    def hba_version(self):
        """Gets the hba_version of this FirmwareInfoV2.  # noqa: E501

        Version of the host bus adapter (HBA) firmware  # noqa: E501

        :return: The hba_version of this FirmwareInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._hba_version

    @hba_version.setter
    def hba_version(self, hba_version):
        """Sets the hba_version of this FirmwareInfoV2.

        Version of the host bus adapter (HBA) firmware  # noqa: E501

        :param hba_version: The hba_version of this FirmwareInfoV2.  # noqa: E501
        :type: str
        """

        self._hba_version = hba_version

    @property
    def expander_bpf_version(self):
        """Gets the expander_bpf_version of this FirmwareInfoV2.  # noqa: E501

        Version of the expander backplane firmware  # noqa: E501

        :return: The expander_bpf_version of this FirmwareInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._expander_bpf_version

    @expander_bpf_version.setter
    def expander_bpf_version(self, expander_bpf_version):
        """Sets the expander_bpf_version of this FirmwareInfoV2.

        Version of the expander backplane firmware  # noqa: E501

        :param expander_bpf_version: The expander_bpf_version of this FirmwareInfoV2.  # noqa: E501
        :type: str
        """

        self._expander_bpf_version = expander_bpf_version

    @property
    def nonexpander_bpf_version(self):
        """Gets the nonexpander_bpf_version of this FirmwareInfoV2.  # noqa: E501

        Version of the non-expander storage backplane firmware  # noqa: E501

        :return: The nonexpander_bpf_version of this FirmwareInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._nonexpander_bpf_version

    @nonexpander_bpf_version.setter
    def nonexpander_bpf_version(self, nonexpander_bpf_version):
        """Sets the nonexpander_bpf_version of this FirmwareInfoV2.

        Version of the non-expander storage backplane firmware  # noqa: E501

        :param nonexpander_bpf_version: The nonexpander_bpf_version of this FirmwareInfoV2.  # noqa: E501
        :type: str
        """

        self._nonexpander_bpf_version = nonexpander_bpf_version

    @property
    def boss_version(self):
        """Gets the boss_version of this FirmwareInfoV2.  # noqa: E501

        Version of the BOSS firmware  # noqa: E501

        :return: The boss_version of this FirmwareInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._boss_version

    @boss_version.setter
    def boss_version(self, boss_version):
        """Sets the boss_version of this FirmwareInfoV2.

        Version of the BOSS firmware  # noqa: E501

        :param boss_version: The boss_version of this FirmwareInfoV2.  # noqa: E501
        :type: str
        """

        self._boss_version = boss_version

    @property
    def cpld_version(self):
        """Gets the cpld_version of this FirmwareInfoV2.  # noqa: E501

        Version of the complex logical device (CPLD) firmware  # noqa: E501

        :return: The cpld_version of this FirmwareInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._cpld_version

    @cpld_version.setter
    def cpld_version(self, cpld_version):
        """Sets the cpld_version of this FirmwareInfoV2.

        Version of the complex logical device (CPLD) firmware  # noqa: E501

        :param cpld_version: The cpld_version of this FirmwareInfoV2.  # noqa: E501
        :type: str
        """

        self._cpld_version = cpld_version

    @property
    def dcpm_version(self):
        """Gets the dcpm_version of this FirmwareInfoV2.  # noqa: E501

        Version of the DC Persistent Memory (DCPM) firmware  # noqa: E501

        :return: The dcpm_version of this FirmwareInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._dcpm_version

    @dcpm_version.setter
    def dcpm_version(self, dcpm_version):
        """Sets the dcpm_version of this FirmwareInfoV2.

        Version of the DC Persistent Memory (DCPM) firmware  # noqa: E501

        :param dcpm_version: The dcpm_version of this FirmwareInfoV2.  # noqa: E501
        :type: str
        """

        self._dcpm_version = dcpm_version

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
        if issubclass(FirmwareInfoV2, dict):
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
        if not isinstance(other, FirmwareInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
