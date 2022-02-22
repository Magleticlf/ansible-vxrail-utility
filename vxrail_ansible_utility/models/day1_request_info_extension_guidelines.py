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

class Day1RequestInfoExtensionGuidelines(object):
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
        'message': 'str',
        'kb': 'str'
    }

    attribute_map = {
        'message': 'message',
        'kb': 'kb'
    }

    def __init__(self, message=None, kb=None):  # noqa: E501
        """Day1RequestInfoExtensionGuidelines - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._kb = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if kb is not None:
            self.kb = kb

    @property
    def message(self):
        """Gets the message of this Day1RequestInfoExtensionGuidelines.  # noqa: E501

        Guidance messages  # noqa: E501

        :return: The message of this Day1RequestInfoExtensionGuidelines.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Day1RequestInfoExtensionGuidelines.

        Guidance messages  # noqa: E501

        :param message: The message of this Day1RequestInfoExtensionGuidelines.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def kb(self):
        """Gets the kb of this Day1RequestInfoExtensionGuidelines.  # noqa: E501

        Optional Knowledge Base ID number  # noqa: E501

        :return: The kb of this Day1RequestInfoExtensionGuidelines.  # noqa: E501
        :rtype: str
        """
        return self._kb

    @kb.setter
    def kb(self, kb):
        """Sets the kb of this Day1RequestInfoExtensionGuidelines.

        Optional Knowledge Base ID number  # noqa: E501

        :param kb: The kb of this Day1RequestInfoExtensionGuidelines.  # noqa: E501
        :type: str
        """

        self._kb = kb

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
        if issubclass(Day1RequestInfoExtensionGuidelines, dict):
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
        if not isinstance(other, Day1RequestInfoExtensionGuidelines):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
