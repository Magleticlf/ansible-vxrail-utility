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

class LogInfo(object):
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
        'id': 'str',
        'types': 'str',
        'nodes': 'list[str]',
        'creation_time': 'int',
        'path': 'str',
        'size': 'int',
        'details': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'types': 'types',
        'nodes': 'nodes',
        'creation_time': 'creation_time',
        'path': 'path',
        'size': 'size',
        'details': 'details'
    }

    def __init__(self, id=None, types=None, nodes=None, creation_time=None, path=None, size=None, details=None):  # noqa: E501
        """LogInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._types = None
        self._nodes = None
        self._creation_time = None
        self._path = None
        self._size = None
        self._details = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if types is not None:
            self.types = types
        if nodes is not None:
            self.nodes = nodes
        if creation_time is not None:
            self.creation_time = creation_time
        if path is not None:
            self.path = path
        if size is not None:
            self.size = size
        if details is not None:
            self.details = details

    @property
    def id(self):
        """Gets the id of this LogInfo.  # noqa: E501

        The unique identifier for the log  # noqa: E501

        :return: The id of this LogInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogInfo.

        The unique identifier for the log  # noqa: E501

        :param id: The id of this LogInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def types(self):
        """Gets the types of this LogInfo.  # noqa: E501

        The type of component included in the log  # noqa: E501

        :return: The types of this LogInfo.  # noqa: E501
        :rtype: str
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this LogInfo.

        The type of component included in the log  # noqa: E501

        :param types: The types of this LogInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["vxm", "vcenter", "esxi", "idrac", "ptagent", "witness"]  # noqa: E501
        if types not in allowed_values:
            raise ValueError(
                "Invalid value for `types` ({0}), must be one of {1}"  # noqa: E501
                .format(types, allowed_values)
            )

        self._types = types

    @property
    def nodes(self):
        """Gets the nodes of this LogInfo.  # noqa: E501

        An array of serial numbers for the nodes included in the log  # noqa: E501

        :return: The nodes of this LogInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this LogInfo.

        An array of serial numbers for the nodes included in the log  # noqa: E501

        :param nodes: The nodes of this LogInfo.  # noqa: E501
        :type: list[str]
        """

        self._nodes = nodes

    @property
    def creation_time(self):
        """Gets the creation_time of this LogInfo.  # noqa: E501

        Time that the support log was created  # noqa: E501

        :return: The creation_time of this LogInfo.  # noqa: E501
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this LogInfo.

        Time that the support log was created  # noqa: E501

        :param creation_time: The creation_time of this LogInfo.  # noqa: E501
        :type: int
        """

        self._creation_time = creation_time

    @property
    def path(self):
        """Gets the path of this LogInfo.  # noqa: E501

        The file path of the log  # noqa: E501

        :return: The path of this LogInfo.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this LogInfo.

        The file path of the log  # noqa: E501

        :param path: The path of this LogInfo.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def size(self):
        """Gets the size of this LogInfo.  # noqa: E501

        The size of the log  # noqa: E501

        :return: The size of this LogInfo.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LogInfo.

        The size of the log  # noqa: E501

        :param size: The size of this LogInfo.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def details(self):
        """Gets the details of this LogInfo.  # noqa: E501

        An array of details about the logs  # noqa: E501

        :return: The details of this LogInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this LogInfo.

        An array of details about the logs  # noqa: E501

        :param details: The details of this LogInfo.  # noqa: E501
        :type: list[str]
        """

        self._details = details

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
        if issubclass(LogInfo, dict):
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
        if not isinstance(other, LogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
