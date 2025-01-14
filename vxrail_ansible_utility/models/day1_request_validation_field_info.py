# coding: utf-8

"""
    Day1 Bring Up Configuration

    The set of Day 1 Bring Up Configuration API(s) are used to deploy VxRail cluster.  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Day1RequestValidationFieldInfo(object):
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
        'path': 'str',
        'messages': 'str'
    }

    attribute_map = {
        'path': 'path',
        'messages': 'messages'
    }

    def __init__(self, path=None, messages=None):  # noqa: E501
        """Day1RequestValidationFieldInfo - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._messages = None
        self.discriminator = None
        self.path = path
        self.messages = messages

    @property
    def path(self):
        """Gets the path of this Day1RequestValidationFieldInfo.  # noqa: E501

        The parameter path for the error result in the input JSON file  # noqa: E501

        :return: The path of this Day1RequestValidationFieldInfo.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Day1RequestValidationFieldInfo.

        The parameter path for the error result in the input JSON file  # noqa: E501

        :param path: The path of this Day1RequestValidationFieldInfo.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def messages(self):
        """Gets the message of this Day1RequestValidationFieldInfo.  # noqa: E501

        The error or warning message  # noqa: E501

        :return: The message of this Day1RequestValidationFieldInfo.  # noqa: E501
        :rtype: str
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the message of this Day1RequestValidationFieldInfo.

        The error or warning message  # noqa: E501

        :param messages: The message of this Day1RequestValidationFieldInfo.  # noqa: E501
        :type: str
        """
        # if message is None:
        #     raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._messages = messages

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
        if issubclass(Day1RequestValidationFieldInfo, dict):
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
        if not isinstance(other, Day1RequestValidationFieldInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
