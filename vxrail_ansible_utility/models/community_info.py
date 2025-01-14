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

class CommunityInfo(object):
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
        'home_url': 'str',
        'messages_link': 'str'
    }

    attribute_map = {
        'home_url': 'homeURL',
        'messages_link': 'messagesLink'
    }

    def __init__(self, home_url=None, messages_link=None):  # noqa: E501
        """CommunityInfo - a model defined in Swagger"""  # noqa: E501
        self._home_url = None
        self._messages_link = None
        self.discriminator = None
        self.home_url = home_url
        if messages_link is not None:
            self.messages_link = messages_link

    @property
    def home_url(self):
        """Gets the home_url of this CommunityInfo.  # noqa: E501

        The home URL of the VxRail community resources  # noqa: E501

        :return: The home_url of this CommunityInfo.  # noqa: E501
        :rtype: str
        """
        return self._home_url

    @home_url.setter
    def home_url(self, home_url):
        """Sets the home_url of this CommunityInfo.

        The home URL of the VxRail community resources  # noqa: E501

        :param home_url: The home_url of this CommunityInfo.  # noqa: E501
        :type: str
        """
        if home_url is None:
            raise ValueError("Invalid value for `home_url`, must not be `None`")  # noqa: E501

        self._home_url = home_url

    @property
    def messages_link(self):
        """Gets the messages_link of this CommunityInfo.  # noqa: E501

        The link for retrieving messages  # noqa: E501

        :return: The messages_link of this CommunityInfo.  # noqa: E501
        :rtype: str
        """
        return self._messages_link

    @messages_link.setter
    def messages_link(self, messages_link):
        """Sets the messages_link of this CommunityInfo.

        The link for retrieving messages  # noqa: E501

        :param messages_link: The messages_link of this CommunityInfo.  # noqa: E501
        :type: str
        """

        self._messages_link = messages_link

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
        if issubclass(CommunityInfo, dict):
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
        if not isinstance(other, CommunityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
