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

class CallhomeInfo(object):
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
        'status': 'str',
        'integrated': 'bool',
        'ip_list': 'list[Ip]',
        'site_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'integrated': 'integrated',
        'ip_list': 'ip_list',
        'site_id': 'site_id'
    }

    def __init__(self, status=None, integrated=None, ip_list=None, site_id=None):  # noqa: E501
        """CallhomeInfo - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._integrated = None
        self._ip_list = None
        self._site_id = None
        self.discriminator = None
        self.status = status
        self.integrated = integrated
        if ip_list is not None:
            self.ip_list = ip_list
        self.site_id = site_id

    @property
    def status(self):
        """Gets the status of this CallhomeInfo.  # noqa: E501

        Status of the SRS server. Supported values are deploying, deployed, registering, and registered.  # noqa: E501

        :return: The status of this CallhomeInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CallhomeInfo.

        Status of the SRS server. Supported values are deploying, deployed, registering, and registered.  # noqa: E501

        :param status: The status of this CallhomeInfo.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def integrated(self):
        """Gets the integrated of this CallhomeInfo.  # noqa: E501

        Whether the SRS server is integrated (internal) or external  # noqa: E501

        :return: The integrated of this CallhomeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._integrated

    @integrated.setter
    def integrated(self, integrated):
        """Sets the integrated of this CallhomeInfo.

        Whether the SRS server is integrated (internal) or external  # noqa: E501

        :param integrated: The integrated of this CallhomeInfo.  # noqa: E501
        :type: bool
        """
        if integrated is None:
            raise ValueError("Invalid value for `integrated`, must not be `None`")  # noqa: E501

        self._integrated = integrated

    @property
    def ip_list(self):
        """Gets the ip_list of this CallhomeInfo.  # noqa: E501

        An array of SRS server addresses with associated information  # noqa: E501

        :return: The ip_list of this CallhomeInfo.  # noqa: E501
        :rtype: list[Ip]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this CallhomeInfo.

        An array of SRS server addresses with associated information  # noqa: E501

        :param ip_list: The ip_list of this CallhomeInfo.  # noqa: E501
        :type: list[Ip]
        """

        self._ip_list = ip_list

    @property
    def site_id(self):
        """Gets the site_id of this CallhomeInfo.  # noqa: E501

        Site ID for the SRS server  # noqa: E501

        :return: The site_id of this CallhomeInfo.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this CallhomeInfo.

        Site ID for the SRS server  # noqa: E501

        :param site_id: The site_id of this CallhomeInfo.  # noqa: E501
        :type: str
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

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
        if issubclass(CallhomeInfo, dict):
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
        if not isinstance(other, CallhomeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
