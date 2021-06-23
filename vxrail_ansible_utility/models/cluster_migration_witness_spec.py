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

class ClusterMigrationWitnessSpec(object):
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
        'hostname': 'str',
        'ip': 'str',
        'account': 'Account'
    }

    attribute_map = {
        'hostname': 'hostname',
        'ip': 'ip',
        'account': 'account'
    }

    def __init__(self, hostname=None, ip=None, account=None):  # noqa: E501
        """ClusterMigrationWitnessSpec - a model defined in Swagger"""  # noqa: E501
        self._hostname = None
        self._ip = None
        self._account = None
        self.discriminator = None
        self.hostname = hostname
        self.ip = ip
        self.account = account

    @property
    def hostname(self):
        """Gets the hostname of this ClusterMigrationWitnessSpec.  # noqa: E501


        :return: The hostname of this ClusterMigrationWitnessSpec.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ClusterMigrationWitnessSpec.


        :param hostname: The hostname of this ClusterMigrationWitnessSpec.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def ip(self):
        """Gets the ip of this ClusterMigrationWitnessSpec.  # noqa: E501


        :return: The ip of this ClusterMigrationWitnessSpec.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ClusterMigrationWitnessSpec.


        :param ip: The ip of this ClusterMigrationWitnessSpec.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def account(self):
        """Gets the account of this ClusterMigrationWitnessSpec.  # noqa: E501


        :return: The account of this ClusterMigrationWitnessSpec.  # noqa: E501
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ClusterMigrationWitnessSpec.


        :param account: The account of this ClusterMigrationWitnessSpec.  # noqa: E501
        :type: Account
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

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
        if issubclass(ClusterMigrationWitnessSpec, dict):
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
        if not isinstance(other, ClusterMigrationWitnessSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
