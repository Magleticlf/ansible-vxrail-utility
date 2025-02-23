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

class AsyncLcmRequestSuccessResponse(object):
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
        'request_id': 'str',
        'error_code': 'int',
        'message': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'error_code': 'error_code',
        'message': 'message'
    }

    def __init__(self, request_id=None, error_code=None, message=None):  # noqa: E501
        """AsyncLcmRequestSuccessResponse - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._error_code = None
        self._message = None
        self.discriminator = None
        if request_id is not None:
            self.request_id = request_id
        if error_code is not None:
            self.error_code = error_code
        if message is not None:
            self.message = message

    @property
    def request_id(self):
        """Gets the request_id of this AsyncLcmRequestSuccessResponse.  # noqa: E501


        :return: The request_id of this AsyncLcmRequestSuccessResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AsyncLcmRequestSuccessResponse.


        :param request_id: The request_id of this AsyncLcmRequestSuccessResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def error_code(self):
        """Gets the error_code of this AsyncLcmRequestSuccessResponse.  # noqa: E501


        :return: The error_code of this AsyncLcmRequestSuccessResponse.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AsyncLcmRequestSuccessResponse.


        :param error_code: The error_code of this AsyncLcmRequestSuccessResponse.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this AsyncLcmRequestSuccessResponse.  # noqa: E501


        :return: The message of this AsyncLcmRequestSuccessResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AsyncLcmRequestSuccessResponse.


        :param message: The message of this AsyncLcmRequestSuccessResponse.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(AsyncLcmRequestSuccessResponse, dict):
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
        if not isinstance(other, AsyncLcmRequestSuccessResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
