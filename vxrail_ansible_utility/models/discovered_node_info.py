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


class DiscoveredNodeInfo(object):
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
        'id': 'DiscoveredNodeIdInfo',
        'primary_ip': 'str',
        'fallback_ip': 'str',
        'idrac_ip': 'str',
        'prerecoded_ip': 'str',
        'ip': 'str',
        'asset_tag': 'str',
        'serial_number': 'str',
        'primary': 'bool',
        'cluster_affinity': 'str',
        'rsa_public_key': 'str',
        'ssl_thumbprint': 'str',
        'uuid': 'DiscoveredNodeUuidInfo',
        'hardware_profile': 'DiscoveredNodeHardwareProfileInfo',
        'discovered_date': 'int',
        'configuration_state': 'str',
        'model': 'str',
        'ip_set': 'object',
        'node_version_info': 'DiscoveredNodeVersionInfo',
        'vsan_repair_timeout_value': 'int'
    }

    attribute_map = {
        'id': 'id',
        'primary_ip': 'primary_ip',
        'fallback_ip': 'fallback_ip',
        'idrac_ip': 'idrac_ip',
        'prerecoded_ip': 'prerecoded_ip',
        'ip': 'ip',
        'asset_tag': 'asset_tag',
        'serial_number': 'serial_number',
        'primary': 'primary',
        'cluster_affinity': 'cluster_affinity',
        'rsa_public_key': 'rsa_public_key',
        'ssl_thumbprint': 'ssl_thumbprint',
        'uuid': 'uuid',
        'hardware_profile': 'hardware_profile',
        'discovered_date': 'discovered_date',
        'configuration_state': 'configuration_state',
        'model': 'model',
        'ip_set': 'ip_set',
        'node_version_info': 'node_version_info',
        'vsan_repair_timeout_value': 'vsan_repair_timeout_value'
    }

    def __init__(self, id=None, primary_ip=None, fallback_ip=None, idrac_ip=None, prerecoded_ip=None, ip=None, asset_tag=None, serial_number=None, primary=None, cluster_affinity=None, rsa_public_key=None, ssl_thumbprint=None, uuid=None, hardware_profile=None, discovered_date=None, configuration_state=None, model=None, ip_set=None, node_version_info=None, vsan_repair_timeout_value=None):  # noqa: E501
        """DiscoveredNodeInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._primary_ip = None
        self._fallback_ip = None
        self._idrac_ip = None
        self._prerecoded_ip = None
        self._ip = None
        self._asset_tag = None
        self._serial_number = None
        self._primary = None
        self._cluster_affinity = None
        self._rsa_public_key = None
        self._ssl_thumbprint = None
        self._uuid = None
        self._hardware_profile = None
        self._discovered_date = None
        self._configuration_state = None
        self._model = None
        self._ip_set = None
        self._node_version_info = None
        self._vsan_repair_timeout_value = None
        self.discriminator = None
        self.id = id
        self.primary_ip = primary_ip
        if fallback_ip is not None:
            self.fallback_ip = fallback_ip
        self.idrac_ip = idrac_ip
        if prerecoded_ip is not None:
            self.prerecoded_ip = prerecoded_ip
        if ip is not None:
            self.ip = ip
        self.asset_tag = asset_tag
        self.serial_number = serial_number
        self.primary = primary
        if cluster_affinity is not None:
            self.cluster_affinity = cluster_affinity
        if rsa_public_key is not None:
            self.rsa_public_key = rsa_public_key
        if ssl_thumbprint is not None:
            self.ssl_thumbprint = ssl_thumbprint
        if uuid is not None:
            self.uuid = uuid
        self.hardware_profile = hardware_profile
        if discovered_date is not None:
            self.discovered_date = discovered_date
        if configuration_state is not None:
            self.configuration_state = configuration_state
        self.model = model
        if ip_set is not None:
            self.ip_set = ip_set
        if node_version_info is not None:
            self.node_version_info = node_version_info
        if vsan_repair_timeout_value is not None:
            self.vsan_repair_timeout_value = vsan_repair_timeout_value

    @property
    def id(self):
        """Gets the id of this DiscoveredNodeInfo.  # noqa: E501


        :return: The id of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: DiscoveredNodeIdInfo
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiscoveredNodeInfo.


        :param id: The id of this DiscoveredNodeInfo.  # noqa: E501
        :type: DiscoveredNodeIdInfo
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def primary_ip(self):
        """Gets the primary_ip of this DiscoveredNodeInfo.  # noqa: E501

        primary ip to use of the node  # noqa: E501

        :return: The primary_ip of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._primary_ip

    @primary_ip.setter
    def primary_ip(self, primary_ip):
        """Sets the primary_ip of this DiscoveredNodeInfo.

        primary ip to use of the node  # noqa: E501

        :param primary_ip: The primary_ip of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if primary_ip is None:
            raise ValueError("Invalid value for `primary_ip`, must not be `None`")  # noqa: E501

        self._primary_ip = primary_ip

    @property
    def fallback_ip(self):
        """Gets the fallback_ip of this DiscoveredNodeInfo.  # noqa: E501

        secondary ip to use of the node  # noqa: E501

        :return: The fallback_ip of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._fallback_ip

    @fallback_ip.setter
    def fallback_ip(self, fallback_ip):
        """Sets the fallback_ip of this DiscoveredNodeInfo.

        secondary ip to use of the node  # noqa: E501

        :param fallback_ip: The fallback_ip of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """

        self._fallback_ip = fallback_ip

    @property
    def idrac_ip(self):
        """Gets the idrac_ip of this DiscoveredNodeInfo.  # noqa: E501

        idrac ip of the node  # noqa: E501

        :return: The idrac_ip of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._idrac_ip

    @idrac_ip.setter
    def idrac_ip(self, idrac_ip):
        """Sets the idrac_ip of this DiscoveredNodeInfo.

        idrac ip of the node  # noqa: E501

        :param idrac_ip: The idrac_ip of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if idrac_ip is None:
            raise ValueError("Invalid value for `idrac_ip`, must not be `None`")  # noqa: E501

        self._idrac_ip = idrac_ip

    @property
    def prerecoded_ip(self):
        """Gets the prerecoded_ip of this DiscoveredNodeInfo.  # noqa: E501

        prerecoded ip of the node  # noqa: E501

        :return: The prerecoded_ip of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._prerecoded_ip

    @prerecoded_ip.setter
    def prerecoded_ip(self, prerecoded_ip):
        """Sets the prerecoded_ip of this DiscoveredNodeInfo.

        prerecoded ip of the node  # noqa: E501

        :param prerecoded_ip: The prerecoded_ip of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """

        self._prerecoded_ip = prerecoded_ip

    @property
    def ip(self):
        """Gets the ip of this DiscoveredNodeInfo.  # noqa: E501

        ipv4 of the node  # noqa: E501

        :return: The ip of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this DiscoveredNodeInfo.

        ipv4 of the node  # noqa: E501

        :param ip: The ip of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def asset_tag(self):
        """Gets the asset_tag of this DiscoveredNodeInfo.  # noqa: E501

        asset tag of the node  # noqa: E501

        :return: The asset_tag of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """Sets the asset_tag of this DiscoveredNodeInfo.

        asset tag of the node  # noqa: E501

        :param asset_tag: The asset_tag of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if asset_tag is None:
            raise ValueError("Invalid value for `asset_tag`, must not be `None`")  # noqa: E501

        self._asset_tag = asset_tag

    @property
    def serial_number(self):
        """Gets the serial_number of this DiscoveredNodeInfo.  # noqa: E501

        serial number of the node  # noqa: E501

        :return: The serial_number of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this DiscoveredNodeInfo.

        serial number of the node  # noqa: E501

        :param serial_number: The serial_number of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def primary(self):
        """Gets the primary of this DiscoveredNodeInfo.  # noqa: E501

        is the node a primary node  # noqa: E501

        :return: The primary of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this DiscoveredNodeInfo.

        is the node a primary node  # noqa: E501

        :param primary: The primary of this DiscoveredNodeInfo.  # noqa: E501
        :type: bool
        """
        if primary is None:
            raise ValueError("Invalid value for `primary`, must not be `None`")  # noqa: E501

        self._primary = primary

    @property
    def cluster_affinity(self):
        """Gets the cluster_affinity of this DiscoveredNodeInfo.  # noqa: E501

        cluster_affinity of the node  # noqa: E501

        :return: The cluster_affinity of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._cluster_affinity

    @cluster_affinity.setter
    def cluster_affinity(self, cluster_affinity):
        """Sets the cluster_affinity of this DiscoveredNodeInfo.

        cluster_affinity of the node  # noqa: E501

        :param cluster_affinity: The cluster_affinity of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "MINE", "OTHER"]  # noqa: E501
        if cluster_affinity not in allowed_values:
            raise ValueError(
                "Invalid value for `cluster_affinity` ({0}), must be one of {1}"  # noqa: E501
                .format(cluster_affinity, allowed_values)
            )

        self._cluster_affinity = cluster_affinity

    @property
    def rsa_public_key(self):
        """Gets the rsa_public_key of this DiscoveredNodeInfo.  # noqa: E501

        RSA public key of the node  # noqa: E501

        :return: The rsa_public_key of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._rsa_public_key

    @rsa_public_key.setter
    def rsa_public_key(self, rsa_public_key):
        """Sets the rsa_public_key of this DiscoveredNodeInfo.

        RSA public key of the node  # noqa: E501

        :param rsa_public_key: The rsa_public_key of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """

        self._rsa_public_key = rsa_public_key

    @property
    def ssl_thumbprint(self):
        """Gets the ssl_thumbprint of this DiscoveredNodeInfo.  # noqa: E501

        ssl thumbprint of the node  # noqa: E501

        :return: The ssl_thumbprint of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._ssl_thumbprint

    @ssl_thumbprint.setter
    def ssl_thumbprint(self, ssl_thumbprint):
        """Sets the ssl_thumbprint of this DiscoveredNodeInfo.

        ssl thumbprint of the node  # noqa: E501

        :param ssl_thumbprint: The ssl_thumbprint of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """

        self._ssl_thumbprint = ssl_thumbprint

    @property
    def uuid(self):
        """Gets the uuid of this DiscoveredNodeInfo.  # noqa: E501


        :return: The uuid of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: DiscoveredNodeUuidInfo
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DiscoveredNodeInfo.


        :param uuid: The uuid of this DiscoveredNodeInfo.  # noqa: E501
        :type: DiscoveredNodeUuidInfo
        """

        self._uuid = uuid

    @property
    def hardware_profile(self):
        """Gets the hardware_profile of this DiscoveredNodeInfo.  # noqa: E501


        :return: The hardware_profile of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: DiscoveredNodeHardwareProfileInfo
        """
        return self._hardware_profile

    @hardware_profile.setter
    def hardware_profile(self, hardware_profile):
        """Sets the hardware_profile of this DiscoveredNodeInfo.


        :param hardware_profile: The hardware_profile of this DiscoveredNodeInfo.  # noqa: E501
        :type: DiscoveredNodeHardwareProfileInfo
        """
        if hardware_profile is None:
            raise ValueError("Invalid value for `hardware_profile`, must not be `None`")  # noqa: E501

        self._hardware_profile = hardware_profile

    @property
    def discovered_date(self):
        """Gets the discovered_date of this DiscoveredNodeInfo.  # noqa: E501

        discovered date of the node  # noqa: E501

        :return: The discovered_date of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._discovered_date

    @discovered_date.setter
    def discovered_date(self, discovered_date):
        """Sets the discovered_date of this DiscoveredNodeInfo.

        discovered date of the node  # noqa: E501

        :param discovered_date: The discovered_date of this DiscoveredNodeInfo.  # noqa: E501
        :type: int
        """

        self._discovered_date = discovered_date

    @property
    def configuration_state(self):
        """Gets the configuration_state of this DiscoveredNodeInfo.  # noqa: E501

        configuration state of the node  # noqa: E501

        :return: The configuration_state of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._configuration_state

    @configuration_state.setter
    def configuration_state(self, configuration_state):
        """Sets the configuration_state of this DiscoveredNodeInfo.

        configuration state of the node  # noqa: E501

        :param configuration_state: The configuration_state of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNCONFIGURED", "CONFIGURING", "CONFIGURED"]  # noqa: E501
        if configuration_state not in allowed_values:
            raise ValueError(
                "Invalid value for `configuration_state` ({0}), must be one of {1}"  # noqa: E501
                .format(configuration_state, allowed_values)
            )

        self._configuration_state = configuration_state

    @property
    def model(self):
        """Gets the model of this DiscoveredNodeInfo.  # noqa: E501

        platform model of the node  # noqa: E501

        :return: The model of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DiscoveredNodeInfo.

        platform model of the node  # noqa: E501

        :param model: The model of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def ip_set(self):
        """Gets the ip_set of this DiscoveredNodeInfo.  # noqa: E501

        ip set info of the node  # noqa: E501

        :return: The ip_set of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: object
        """
        return self._ip_set

    @ip_set.setter
    def ip_set(self, ip_set):
        """Sets the ip_set of this DiscoveredNodeInfo.

        ip set info of the node  # noqa: E501

        :param ip_set: The ip_set of this DiscoveredNodeInfo.  # noqa: E501
        :type: object
        """

        self._ip_set = ip_set

    @property
    def node_version_info(self):
        """Gets the node_version_info of this DiscoveredNodeInfo.  # noqa: E501


        :return: The node_version_info of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: DiscoveredNodeVersionInfo
        """
        return self._node_version_info

    @node_version_info.setter
    def node_version_info(self, node_version_info):
        """Sets the node_version_info of this DiscoveredNodeInfo.


        :param node_version_info: The node_version_info of this DiscoveredNodeInfo.  # noqa: E501
        :type: DiscoveredNodeVersionInfo
        """

        self._node_version_info = node_version_info

    @property
    def vsan_repair_timeout_value(self):
        """Gets the vsan_repair_timeout_value of this DiscoveredNodeInfo.  # noqa: E501

        vsan repair timeout value of the node  # noqa: E501

        :return: The vsan_repair_timeout_value of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._vsan_repair_timeout_value

    @vsan_repair_timeout_value.setter
    def vsan_repair_timeout_value(self, vsan_repair_timeout_value):
        """Sets the vsan_repair_timeout_value of this DiscoveredNodeInfo.

        vsan repair timeout value of the node  # noqa: E501

        :param vsan_repair_timeout_value: The vsan_repair_timeout_value of this DiscoveredNodeInfo.  # noqa: E501
        :type: int
        """

        self._vsan_repair_timeout_value = vsan_repair_timeout_value

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
        if issubclass(DiscoveredNodeInfo, dict):
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
        if not isinstance(other, DiscoveredNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
