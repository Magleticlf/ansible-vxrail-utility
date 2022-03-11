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

class HostDiskSlotMappingRequest(object):
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
        'host_serial_number': 'str',
        'customer_supplied': 'CustomerSuppliedNodeInfo'
    }

    attribute_map = {
        'host_serial_number': 'host_serial_number',
        'customer_supplied': 'customer_supplied'
    }

    def __init__(self, host_serial_number=None, customer_supplied=None):  # noqa: E501
        """HostDiskSlotMappingRequest - a model defined in Swagger"""  # noqa: E501
        self._host_serial_number = None
        self._customer_supplied = None
        self.discriminator = None
        self.host_serial_number = host_serial_number
        self.customer_supplied = customer_supplied

    @property
    def host_serial_number(self):
        """Gets the host_serial_number of this HostDiskSlotMappingRequest.  # noqa: E501

        Serial number of the host. This property is mandatory if the customer_supplied property is not supplied  # noqa: E501

        :return: The host_serial_number of this HostDiskSlotMappingRequest.  # noqa: E501
        :rtype: str
        """
        return self._host_serial_number

    @host_serial_number.setter
    def host_serial_number(self, host_serial_number):
        """Sets the host_serial_number of this HostDiskSlotMappingRequest.

        Serial number of the host. This property is mandatory if the customer_supplied property is not supplied  # noqa: E501

        :param host_serial_number: The host_serial_number of this HostDiskSlotMappingRequest.  # noqa: E501
        :type: str
        """
        if host_serial_number is None:
            raise ValueError("Invalid value for `host_serial_number`, must not be `None`")  # noqa: E501

        self._host_serial_number = host_serial_number

    @property
    def customer_supplied(self):
        """Gets the customer_supplied of this HostDiskSlotMappingRequest.  # noqa: E501


        :return: The customer_supplied of this HostDiskSlotMappingRequest.  # noqa: E501
        :rtype: CustomerSuppliedNodeInfo
        """
        return self._customer_supplied

    @customer_supplied.setter
    def customer_supplied(self, customer_supplied):
        """Sets the customer_supplied of this HostDiskSlotMappingRequest.


        :param customer_supplied: The customer_supplied of this HostDiskSlotMappingRequest.  # noqa: E501
        :type: CustomerSuppliedNodeInfo
        """
        if customer_supplied is None:
            raise ValueError("Invalid value for `customer_supplied`, must not be `None`")  # noqa: E501

        self._customer_supplied = customer_supplied

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
        if issubclass(HostDiskSlotMappingRequest, dict):
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
        if not isinstance(other, HostDiskSlotMappingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
