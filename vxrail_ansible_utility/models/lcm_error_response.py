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

class LcmErrorResponse(object):
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
        'error_code': 'int',
        'message': 'str',
        'knowledge_base': 'int'
    }

    attribute_map = {
        'error_code': 'error_code',
        'message': 'message',
        'knowledge_base': 'knowledge_base'
    }

    def __init__(self, error_code=None, message=None, knowledge_base=None):  # noqa: E501
        """LcmErrorResponse - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._message = None
        self._knowledge_base = None
        self.discriminator = None
        if error_code is not None:
            self.error_code = error_code
        if message is not None:
            self.message = message
        if knowledge_base is not None:
            self.knowledge_base = knowledge_base

    @property
    def error_code(self):
        """Gets the error_code of this LcmErrorResponse.  # noqa: E501


        :return: The error_code of this LcmErrorResponse.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this LcmErrorResponse.


        :param error_code: The error_code of this LcmErrorResponse.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this LcmErrorResponse.  # noqa: E501


        :return: The message of this LcmErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LcmErrorResponse.


        :param message: The message of this LcmErrorResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def knowledge_base(self):
        """Gets the knowledge_base of this LcmErrorResponse.  # noqa: E501


        :return: The knowledge_base of this LcmErrorResponse.  # noqa: E501
        :rtype: int
        """
        return self._knowledge_base

    @knowledge_base.setter
    def knowledge_base(self, knowledge_base):
        """Sets the knowledge_base of this LcmErrorResponse.


        :param knowledge_base: The knowledge_base of this LcmErrorResponse.  # noqa: E501
        :type: int
        """

        self._knowledge_base = knowledge_base

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
        if issubclass(LcmErrorResponse, dict):
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
        if not isinstance(other, LcmErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
