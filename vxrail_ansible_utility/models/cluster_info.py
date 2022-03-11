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

class ClusterInfo(object):
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
        'cluster_id': 'str',
        'product_type': 'str',
        'device_type': 'str',
        'vc_connected': 'bool',
        'health': 'str',
        'operational_status': 'str',
        'chassises': 'list[ChassisBasicInfo]',
        'suppressed': 'bool',
        'last_time': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'product_type': 'product_type',
        'device_type': 'device_type',
        'vc_connected': 'vc_connected',
        'health': 'health',
        'operational_status': 'operational_status',
        'chassises': 'chassises',
        'suppressed': 'suppressed',
        'last_time': 'last_time'
    }

    def __init__(self, cluster_id=None, product_type=None, device_type=None, vc_connected=None, health=None, operational_status=None, chassises=None, suppressed=None, last_time=None):  # noqa: E501
        """ClusterInfo - a model defined in Swagger"""  # noqa: E501
        self._cluster_id = None
        self._product_type = None
        self._device_type = None
        self._vc_connected = None
        self._health = None
        self._operational_status = None
        self._chassises = None
        self._suppressed = None
        self._last_time = None
        self.discriminator = None
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if product_type is not None:
            self.product_type = product_type
        if device_type is not None:
            self.device_type = device_type
        if vc_connected is not None:
            self.vc_connected = vc_connected
        if health is not None:
            self.health = health
        if operational_status is not None:
            self.operational_status = operational_status
        if chassises is not None:
            self.chassises = chassises
        if suppressed is not None:
            self.suppressed = suppressed
        if last_time is not None:
            self.last_time = last_time

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ClusterInfo.  # noqa: E501

        The UUID of the VxRail cluster  # noqa: E501

        :return: The cluster_id of this ClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ClusterInfo.

        The UUID of the VxRail cluster  # noqa: E501

        :param cluster_id: The cluster_id of this ClusterInfo.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def product_type(self):
        """Gets the product_type of this ClusterInfo.  # noqa: E501

        Product type of the host  # noqa: E501

        :return: The product_type of this ClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ClusterInfo.

        Product type of the host  # noqa: E501

        :param product_type: The product_type of this ClusterInfo.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def device_type(self):
        """Gets the device_type of this ClusterInfo.  # noqa: E501

        Device type of the host  # noqa: E501

        :return: The device_type of this ClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ClusterInfo.

        Device type of the host  # noqa: E501

        :param device_type: The device_type of this ClusterInfo.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def vc_connected(self):
        """Gets the vc_connected of this ClusterInfo.  # noqa: E501

        Whether the vCenter is connected  # noqa: E501

        :return: The vc_connected of this ClusterInfo.  # noqa: E501
        :rtype: bool
        """
        return self._vc_connected

    @vc_connected.setter
    def vc_connected(self, vc_connected):
        """Sets the vc_connected of this ClusterInfo.

        Whether the vCenter is connected  # noqa: E501

        :param vc_connected: The vc_connected of this ClusterInfo.  # noqa: E501
        :type: bool
        """

        self._vc_connected = vc_connected

    @property
    def health(self):
        """Gets the health of this ClusterInfo.  # noqa: E501

        Status of the health of the cluster. Supported values are Critical, Error, Warning, and Healthy.  # noqa: E501

        :return: The health of this ClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this ClusterInfo.

        Status of the health of the cluster. Supported values are Critical, Error, Warning, and Healthy.  # noqa: E501

        :param health: The health of this ClusterInfo.  # noqa: E501
        :type: str
        """

        self._health = health

    @property
    def operational_status(self):
        """Gets the operational_status of this ClusterInfo.  # noqa: E501

        Operational status information  # noqa: E501

        :return: The operational_status of this ClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._operational_status

    @operational_status.setter
    def operational_status(self, operational_status):
        """Sets the operational_status of this ClusterInfo.

        Operational status information  # noqa: E501

        :param operational_status: The operational_status of this ClusterInfo.  # noqa: E501
        :type: str
        """

        self._operational_status = operational_status

    @property
    def chassises(self):
        """Gets the chassises of this ClusterInfo.  # noqa: E501


        :return: The chassises of this ClusterInfo.  # noqa: E501
        :rtype: list[ChassisBasicInfo]
        """
        return self._chassises

    @chassises.setter
    def chassises(self, chassises):
        """Sets the chassises of this ClusterInfo.


        :param chassises: The chassises of this ClusterInfo.  # noqa: E501
        :type: list[ChassisBasicInfo]
        """

        self._chassises = chassises

    @property
    def suppressed(self):
        """Gets the suppressed of this ClusterInfo.  # noqa: E501

        Whether under suppression mode or not  # noqa: E501

        :return: The suppressed of this ClusterInfo.  # noqa: E501
        :rtype: bool
        """
        return self._suppressed

    @suppressed.setter
    def suppressed(self, suppressed):
        """Sets the suppressed of this ClusterInfo.

        Whether under suppression mode or not  # noqa: E501

        :param suppressed: The suppressed of this ClusterInfo.  # noqa: E501
        :type: bool
        """

        self._suppressed = suppressed

    @property
    def last_time(self):
        """Gets the last_time of this ClusterInfo.  # noqa: E501

        The last time the cluster was updated  # noqa: E501

        :return: The last_time of this ClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_time

    @last_time.setter
    def last_time(self, last_time):
        """Sets the last_time of this ClusterInfo.

        The last time the cluster was updated  # noqa: E501

        :param last_time: The last_time of this ClusterInfo.  # noqa: E501
        :type: str
        """

        self._last_time = last_time

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
        if issubclass(ClusterInfo, dict):
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
        if not isinstance(other, ClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
