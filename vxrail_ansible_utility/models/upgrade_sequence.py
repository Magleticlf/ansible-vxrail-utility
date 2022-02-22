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

class UpgradeSequence(object):
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
        'preferred_fault_domain_first': 'bool'
    }

    attribute_map = {
        'preferred_fault_domain_first': 'preferred_fault_domain_first'
    }

    def __init__(self, preferred_fault_domain_first=None):  # noqa: E501
        """UpgradeSequence - a model defined in Swagger"""  # noqa: E501
        self._preferred_fault_domain_first = None
        self.discriminator = None
        self.preferred_fault_domain_first = preferred_fault_domain_first

    @property
    def preferred_fault_domain_first(self):
        """Gets the preferred_fault_domain_first of this UpgradeSequence.  # noqa: E501

        Upgrade preferred fault domain hosts first  # noqa: E501

        :return: The preferred_fault_domain_first of this UpgradeSequence.  # noqa: E501
        :rtype: bool
        """
        return self._preferred_fault_domain_first

    @preferred_fault_domain_first.setter
    def preferred_fault_domain_first(self, preferred_fault_domain_first):
        """Sets the preferred_fault_domain_first of this UpgradeSequence.

        Upgrade preferred fault domain hosts first  # noqa: E501

        :param preferred_fault_domain_first: The preferred_fault_domain_first of this UpgradeSequence.  # noqa: E501
        :type: bool
        """
        if preferred_fault_domain_first is None:
            raise ValueError("Invalid value for `preferred_fault_domain_first`, must not be `None`")  # noqa: E501

        self._preferred_fault_domain_first = preferred_fault_domain_first

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
        if issubclass(UpgradeSequence, dict):
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
        if not isinstance(other, UpgradeSequence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
