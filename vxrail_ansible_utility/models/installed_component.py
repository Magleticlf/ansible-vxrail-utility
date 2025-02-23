# coding: utf-8

"""
    VxRail Cluster and System Management

    APIs for cluster management and system management  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InstalledComponent(object):
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
        'component': 'str',
        'name': 'str',
        'description': 'str',
        'current_version': 'str',
        'upgrade_status': 'str',
        'baseline': 'str',
        'installed_time': 'int',
        'incompatibilities': 'list[str]',
        'multiple_version': 'bool',
        'baseline_drifted': 'bool',
        'supported': 'bool'
    }

    attribute_map = {
        'component': 'component',
        'name': 'name',
        'description': 'description',
        'current_version': 'current_version',
        'upgrade_status': 'upgrade_status',
        'baseline': 'baseline',
        'installed_time': 'installed_time',
        'incompatibilities': 'incompatibilities',
        'multiple_version': 'multiple_version',
        'baseline_drifted': 'baseline_drifted',
        'supported': 'supported'
    }

    def __init__(self, component=None, name=None, description=None, current_version=None, upgrade_status=None, baseline=None, installed_time=None, incompatibilities=None, multiple_version=None, baseline_drifted=None, supported=None):  # noqa: E501
        """InstalledComponent - a model defined in Swagger"""  # noqa: E501
        self._component = None
        self._name = None
        self._description = None
        self._current_version = None
        self._upgrade_status = None
        self._baseline = None
        self._installed_time = None
        self._incompatibilities = None
        self._multiple_version = None
        self._baseline_drifted = None
        self._supported = None
        self.discriminator = None
        if component is not None:
            self.component = component
        self.name = name
        self.description = description
        self.current_version = current_version
        if upgrade_status is not None:
            self.upgrade_status = upgrade_status
        if baseline is not None:
            self.baseline = baseline
        if installed_time is not None:
            self.installed_time = installed_time
        if incompatibilities is not None:
            self.incompatibilities = incompatibilities
        if multiple_version is not None:
            self.multiple_version = multiple_version
        if baseline_drifted is not None:
            self.baseline_drifted = baseline_drifted
        if supported is not None:
            self.supported = supported

    @property
    def component(self):
        """Gets the component of this InstalledComponent.  # noqa: E501

        Type of software component installed  # noqa: E501

        :return: The component of this InstalledComponent.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this InstalledComponent.

        Type of software component installed  # noqa: E501

        :param component: The component of this InstalledComponent.  # noqa: E501
        :type: str
        """

        self._component = component

    @property
    def name(self):
        """Gets the name of this InstalledComponent.  # noqa: E501

        Installed component name  # noqa: E501

        :return: The name of this InstalledComponent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstalledComponent.

        Installed component name  # noqa: E501

        :param name: The name of this InstalledComponent.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this InstalledComponent.  # noqa: E501

        Installed component description  # noqa: E501

        :return: The description of this InstalledComponent.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstalledComponent.

        Installed component description  # noqa: E501

        :param description: The description of this InstalledComponent.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def current_version(self):
        """Gets the current_version of this InstalledComponent.  # noqa: E501

        Installed component version  # noqa: E501

        :return: The current_version of this InstalledComponent.  # noqa: E501
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this InstalledComponent.

        Installed component version  # noqa: E501

        :param current_version: The current_version of this InstalledComponent.  # noqa: E501
        :type: str
        """
        if current_version is None:
            raise ValueError("Invalid value for `current_version`, must not be `None`")  # noqa: E501

        self._current_version = current_version

    @property
    def upgrade_status(self):
        """Gets the upgrade_status of this InstalledComponent.  # noqa: E501

        Description of the upgrade status of the installed software component  # noqa: E501

        :return: The upgrade_status of this InstalledComponent.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        """Sets the upgrade_status of this InstalledComponent.

        Description of the upgrade status of the installed software component  # noqa: E501

        :param upgrade_status: The upgrade_status of this InstalledComponent.  # noqa: E501
        :type: str
        """
        allowed_values = ["CANCELLED", "DOWNLOADED", "DOWNLOADING", "ERR_DOWNLOAD", "ERR_PROFILE_PRECHECKER", "ERR_UPGRADED", "ERR_UPGRADE_PRECHECKER", "ERR_UPLOAD", "HAS_NEWER", "LATEST", "PROFILE_PRECHECKED", "UPGRADED", "UPGRADE_PRECHECKING", "UPGRADING", "UPLOADED", "UPLOADING"]  # noqa: E501
        if upgrade_status not in allowed_values:
            raise ValueError(
                "Invalid value for `upgrade_status` ({0}), must be one of {1}"  # noqa: E501
                .format(upgrade_status, allowed_values)
            )

        self._upgrade_status = upgrade_status

    @property
    def baseline(self):
        """Gets the baseline of this InstalledComponent.  # noqa: E501

        Software version of component at the time the component was initially installed  # noqa: E501

        :return: The baseline of this InstalledComponent.  # noqa: E501
        :rtype: str
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        """Sets the baseline of this InstalledComponent.

        Software version of component at the time the component was initially installed  # noqa: E501

        :param baseline: The baseline of this InstalledComponent.  # noqa: E501
        :type: str
        """

        self._baseline = baseline

    @property
    def installed_time(self):
        """Gets the installed_time of this InstalledComponent.  # noqa: E501

        The time that the software component was initially installed (in milliseconds)  # noqa: E501

        :return: The installed_time of this InstalledComponent.  # noqa: E501
        :rtype: int
        """
        return self._installed_time

    @installed_time.setter
    def installed_time(self, installed_time):
        """Sets the installed_time of this InstalledComponent.

        The time that the software component was initially installed (in milliseconds)  # noqa: E501

        :param installed_time: The installed_time of this InstalledComponent.  # noqa: E501
        :type: int
        """

        self._installed_time = installed_time

    @property
    def incompatibilities(self):
        """Gets the incompatibilities of this InstalledComponent.  # noqa: E501

        A list of other software components that the installed component is incompatible with  # noqa: E501

        :return: The incompatibilities of this InstalledComponent.  # noqa: E501
        :rtype: list[str]
        """
        return self._incompatibilities

    @incompatibilities.setter
    def incompatibilities(self, incompatibilities):
        """Sets the incompatibilities of this InstalledComponent.

        A list of other software components that the installed component is incompatible with  # noqa: E501

        :param incompatibilities: The incompatibilities of this InstalledComponent.  # noqa: E501
        :type: list[str]
        """

        self._incompatibilities = incompatibilities

    @property
    def multiple_version(self):
        """Gets the multiple_version of this InstalledComponent.  # noqa: E501

        Whether the software component has different versions installed in other nodes in the cluster  # noqa: E501

        :return: The multiple_version of this InstalledComponent.  # noqa: E501
        :rtype: bool
        """
        return self._multiple_version

    @multiple_version.setter
    def multiple_version(self, multiple_version):
        """Sets the multiple_version of this InstalledComponent.

        Whether the software component has different versions installed in other nodes in the cluster  # noqa: E501

        :param multiple_version: The multiple_version of this InstalledComponent.  # noqa: E501
        :type: bool
        """

        self._multiple_version = multiple_version

    @property
    def baseline_drifted(self):
        """Gets the baseline_drifted of this InstalledComponent.  # noqa: E501

        Whether the current configuration of the installed software component is different than the initial configuration  # noqa: E501

        :return: The baseline_drifted of this InstalledComponent.  # noqa: E501
        :rtype: bool
        """
        return self._baseline_drifted

    @baseline_drifted.setter
    def baseline_drifted(self, baseline_drifted):
        """Sets the baseline_drifted of this InstalledComponent.

        Whether the current configuration of the installed software component is different than the initial configuration  # noqa: E501

        :param baseline_drifted: The baseline_drifted of this InstalledComponent.  # noqa: E501
        :type: bool
        """

        self._baseline_drifted = baseline_drifted

    @property
    def supported(self):
        """Gets the supported of this InstalledComponent.  # noqa: E501

        Whether the current version of the installed software component is supported  # noqa: E501

        :return: The supported of this InstalledComponent.  # noqa: E501
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        """Sets the supported of this InstalledComponent.

        Whether the current version of the installed software component is supported  # noqa: E501

        :param supported: The supported of this InstalledComponent.  # noqa: E501
        :type: bool
        """

        self._supported = supported

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
        if issubclass(InstalledComponent, dict):
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
        if not isinstance(other, InstalledComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
