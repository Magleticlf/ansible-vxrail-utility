# coding: utf-8

"""
    VxRail Cluster and System Management

    APIs for cluster management and system management  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExpansionValidateSpec(object):
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
        'hosts': 'list[PrivateExpansionNodeSpec]',
        'vcenter': 'Account',
        'skipped_validators': 'list[str]'
    }

    attribute_map = {
        'hosts': 'hosts',
        'vcenter': 'vcenter',
        'skipped_validators': 'skipped_validators'
    }

    def __init__(self, hosts=None, vcenter=None, skipped_validators=None):  # noqa: E501
        """ExpansionValidateSpec - a model defined in Swagger"""  # noqa: E501
        self._hosts = None
        self._vcenter = None
        self._skipped_validators = None
        self.discriminator = None
        self.hosts = hosts
        self.vcenter = vcenter
        if skipped_validators is not None:
            self.skipped_validators = skipped_validators

    @property
    def hosts(self):
        """Gets the hosts of this ExpansionValidateSpec.  # noqa: E501

        Host(s) inforamtion to validate.  # noqa: E501

        :return: The hosts of this ExpansionValidateSpec.  # noqa: E501
        :rtype: list[PrivateExpansionNodeSpec]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ExpansionValidateSpec.

        Host(s) inforamtion to validate.  # noqa: E501

        :param hosts: The hosts of this ExpansionValidateSpec.  # noqa: E501
        :type: list[PrivateExpansionNodeSpec]
        """
        if hosts is None:
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

    @property
    def vcenter(self):
        """Gets the vcenter of this ExpansionValidateSpec.  # noqa: E501


        :return: The vcenter of this ExpansionValidateSpec.  # noqa: E501
        :rtype: Account
        """
        return self._vcenter

    @vcenter.setter
    def vcenter(self, vcenter):
        """Sets the vcenter of this ExpansionValidateSpec.


        :param vcenter: The vcenter of this ExpansionValidateSpec.  # noqa: E501
        :type: Account
        """
        if vcenter is None:
            raise ValueError("Invalid value for `vcenter`, must not be `None`")  # noqa: E501

        self._vcenter = vcenter

    @property
    def skipped_validators(self):
        """Gets the skipped_validators of this ExpansionValidateSpec.  # noqa: E501


        :return: The skipped_validators of this ExpansionValidateSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._skipped_validators

    @skipped_validators.setter
    def skipped_validators(self, skipped_validators):
        """Sets the skipped_validators of this ExpansionValidateSpec.


        :param skipped_validators: The skipped_validators of this ExpansionValidateSpec.  # noqa: E501
        :type: list[str]
        """

        self._skipped_validators = skipped_validators

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
        if issubclass(ExpansionValidateSpec, dict):
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
        if not isinstance(other, ExpansionValidateSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
