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

class VcConversionSpec(object):
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
        'vc_admin_user': 'UserSpec',
        'vc_mode': 'str',
        'psc_mode': 'str'
    }

    attribute_map = {
        'vc_admin_user': 'vc_admin_user',
        'vc_mode': 'vc_mode',
        'psc_mode': 'psc_mode'
    }

    def __init__(self, vc_admin_user=None, vc_mode=None, psc_mode=None):  # noqa: E501
        """VcConversionSpec - a model defined in Swagger"""  # noqa: E501
        self._vc_admin_user = None
        self._vc_mode = None
        self._psc_mode = None
        self.discriminator = None
        self.vc_admin_user = vc_admin_user
        self.vc_mode = vc_mode
        self.psc_mode = psc_mode

    @property
    def vc_admin_user(self):
        """Gets the vc_admin_user of this VcConversionSpec.  # noqa: E501


        :return: The vc_admin_user of this VcConversionSpec.  # noqa: E501
        :rtype: UserSpec
        """
        return self._vc_admin_user

    @vc_admin_user.setter
    def vc_admin_user(self, vc_admin_user):
        """Sets the vc_admin_user of this VcConversionSpec.


        :param vc_admin_user: The vc_admin_user of this VcConversionSpec.  # noqa: E501
        :type: UserSpec
        """
        if vc_admin_user is None:
            raise ValueError("Invalid value for `vc_admin_user`, must not be `None`")  # noqa: E501

        self._vc_admin_user = vc_admin_user

    @property
    def vc_mode(self):
        """Gets the vc_mode of this VcConversionSpec.  # noqa: E501

        Target vCenter mode  # noqa: E501

        :return: The vc_mode of this VcConversionSpec.  # noqa: E501
        :rtype: str
        """
        return self._vc_mode

    @vc_mode.setter
    def vc_mode(self, vc_mode):
        """Sets the vc_mode of this VcConversionSpec.

        Target vCenter mode  # noqa: E501

        :param vc_mode: The vc_mode of this VcConversionSpec.  # noqa: E501
        :type: str
        """
        if vc_mode is None:
            raise ValueError("Invalid value for `vc_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["EXTERNAL", "EMBEDDED"]  # noqa: E501
        if vc_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `vc_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(vc_mode, allowed_values)
            )

        self._vc_mode = vc_mode

    @property
    def psc_mode(self):
        """Gets the psc_mode of this VcConversionSpec.  # noqa: E501

        Target PSC mode  # noqa: E501

        :return: The psc_mode of this VcConversionSpec.  # noqa: E501
        :rtype: str
        """
        return self._psc_mode

    @psc_mode.setter
    def psc_mode(self, psc_mode):
        """Sets the psc_mode of this VcConversionSpec.

        Target PSC mode  # noqa: E501

        :param psc_mode: The psc_mode of this VcConversionSpec.  # noqa: E501
        :type: str
        """
        if psc_mode is None:
            raise ValueError("Invalid value for `psc_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["EMBEDDED", "EXTERNAL"]  # noqa: E501
        if psc_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `psc_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(psc_mode, allowed_values)
            )

        self._psc_mode = psc_mode

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
        if issubclass(VcConversionSpec, dict):
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
        if not isinstance(other, VcConversionSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
