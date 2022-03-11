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

class RemoveHostSpec(object):
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
        'serial_number': 'str',
        'vc_admin_user': 'UserSpec',
        'vcsa_root_user': 'UserSpec'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'vc_admin_user': 'vc_admin_user',
        'vcsa_root_user': 'vcsa_root_user'
    }

    def __init__(self, serial_number=None, vc_admin_user=None, vcsa_root_user=None):  # noqa: E501
        """RemoveHostSpec - a model defined in Swagger"""  # noqa: E501
        self._serial_number = None
        self._vc_admin_user = None
        self._vcsa_root_user = None
        self.discriminator = None
        self.serial_number = serial_number
        self.vc_admin_user = vc_admin_user
        self.vcsa_root_user = vcsa_root_user

    @property
    def serial_number(self):
        """Gets the serial_number of this RemoveHostSpec.  # noqa: E501

        Serial number of the host to be removed  # noqa: E501

        :return: The serial_number of this RemoveHostSpec.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this RemoveHostSpec.

        Serial number of the host to be removed  # noqa: E501

        :param serial_number: The serial_number of this RemoveHostSpec.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def vc_admin_user(self):
        """Gets the vc_admin_user of this RemoveHostSpec.  # noqa: E501


        :return: The vc_admin_user of this RemoveHostSpec.  # noqa: E501
        :rtype: UserSpec
        """
        return self._vc_admin_user

    @vc_admin_user.setter
    def vc_admin_user(self, vc_admin_user):
        """Sets the vc_admin_user of this RemoveHostSpec.


        :param vc_admin_user: The vc_admin_user of this RemoveHostSpec.  # noqa: E501
        :type: UserSpec
        """
        if vc_admin_user is None:
            raise ValueError("Invalid value for `vc_admin_user`, must not be `None`")  # noqa: E501

        self._vc_admin_user = vc_admin_user

    @property
    def vcsa_root_user(self):
        """Gets the vcsa_root_user of this RemoveHostSpec.  # noqa: E501


        :return: The vcsa_root_user of this RemoveHostSpec.  # noqa: E501
        :rtype: UserSpec
        """
        return self._vcsa_root_user

    @vcsa_root_user.setter
    def vcsa_root_user(self, vcsa_root_user):
        """Sets the vcsa_root_user of this RemoveHostSpec.


        :param vcsa_root_user: The vcsa_root_user of this RemoveHostSpec.  # noqa: E501
        :type: UserSpec
        """
        if vcsa_root_user is None:
            raise ValueError("Invalid value for `vcsa_root_user`, must not be `None`")  # noqa: E501

        self._vcsa_root_user = vcsa_root_user

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
        if issubclass(RemoveHostSpec, dict):
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
        if not isinstance(other, RemoveHostSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
