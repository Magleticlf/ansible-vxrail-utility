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

class SRSUpgradeSpec(object):
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
        'admin_pwd': 'str',
        'root_pwd': 'str'
    }

    attribute_map = {
        'admin_pwd': 'admin_pwd',
        'root_pwd': 'root_pwd'
    }

    def __init__(self, admin_pwd=None, root_pwd=None):  # noqa: E501
        """SRSUpgradeSpec - a model defined in Swagger"""  # noqa: E501
        self._admin_pwd = None
        self._root_pwd = None
        self.discriminator = None
        self.admin_pwd = admin_pwd
        self.root_pwd = root_pwd

    @property
    def admin_pwd(self):
        """Gets the admin_pwd of this SRSUpgradeSpec.  # noqa: E501

        Administrator password for accessing the internal SRS server  # noqa: E501

        :return: The admin_pwd of this SRSUpgradeSpec.  # noqa: E501
        :rtype: str
        """
        return self._admin_pwd

    @admin_pwd.setter
    def admin_pwd(self, admin_pwd):
        """Sets the admin_pwd of this SRSUpgradeSpec.

        Administrator password for accessing the internal SRS server  # noqa: E501

        :param admin_pwd: The admin_pwd of this SRSUpgradeSpec.  # noqa: E501
        :type: str
        """
        if admin_pwd is None:
            raise ValueError("Invalid value for `admin_pwd`, must not be `None`")  # noqa: E501

        self._admin_pwd = admin_pwd

    @property
    def root_pwd(self):
        """Gets the root_pwd of this SRSUpgradeSpec.  # noqa: E501

        Root password for accessing the internal SRS server  # noqa: E501

        :return: The root_pwd of this SRSUpgradeSpec.  # noqa: E501
        :rtype: str
        """
        return self._root_pwd

    @root_pwd.setter
    def root_pwd(self, root_pwd):
        """Sets the root_pwd of this SRSUpgradeSpec.

        Root password for accessing the internal SRS server  # noqa: E501

        :param root_pwd: The root_pwd of this SRSUpgradeSpec.  # noqa: E501
        :type: str
        """
        if root_pwd is None:
            raise ValueError("Invalid value for `root_pwd`, must not be `None`")  # noqa: E501

        self._root_pwd = root_pwd

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
        if issubclass(SRSUpgradeSpec, dict):
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
        if not isinstance(other, SRSUpgradeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
