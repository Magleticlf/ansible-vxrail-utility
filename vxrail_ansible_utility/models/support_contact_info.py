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

class SupportContactInfo(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'company': 'str',
        'phone': 'str',
        'site_id': 'list[str]',
        'default_site_id': 'str'
    }

    attribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'company': 'company',
        'phone': 'phone',
        'site_id': 'site_id',
        'default_site_id': 'default_site_id'
    }

    def __init__(self, first_name=None, last_name=None, email=None, company=None, phone=None, site_id=None, default_site_id=None):  # noqa: E501
        """SupportContactInfo - a model defined in Swagger"""  # noqa: E501
        self._first_name = None
        self._last_name = None
        self._email = None
        self._company = None
        self._phone = None
        self._site_id = None
        self._default_site_id = None
        self.discriminator = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.company = company
        self.phone = phone
        self.site_id = site_id
        if default_site_id is not None:
            self.default_site_id = default_site_id

    @property
    def first_name(self):
        """Gets the first_name of this SupportContactInfo.  # noqa: E501

        First name of the support administrator  # noqa: E501

        :return: The first_name of this SupportContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SupportContactInfo.

        First name of the support administrator  # noqa: E501

        :param first_name: The first_name of this SupportContactInfo.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this SupportContactInfo.  # noqa: E501

        Last name of the support administrator  # noqa: E501

        :return: The last_name of this SupportContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SupportContactInfo.

        Last name of the support administrator  # noqa: E501

        :param last_name: The last_name of this SupportContactInfo.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this SupportContactInfo.  # noqa: E501

        Email address of the support account  # noqa: E501

        :return: The email of this SupportContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SupportContactInfo.

        Email address of the support account  # noqa: E501

        :param email: The email of this SupportContactInfo.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def company(self):
        """Gets the company of this SupportContactInfo.  # noqa: E501

        Company name  # noqa: E501

        :return: The company of this SupportContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this SupportContactInfo.

        Company name  # noqa: E501

        :param company: The company of this SupportContactInfo.  # noqa: E501
        :type: str
        """
        if company is None:
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company

    @property
    def phone(self):
        """Gets the phone of this SupportContactInfo.  # noqa: E501

        Phone number of the support administrator  # noqa: E501

        :return: The phone of this SupportContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SupportContactInfo.

        Phone number of the support administrator  # noqa: E501

        :param phone: The phone of this SupportContactInfo.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def site_id(self):
        """Gets the site_id of this SupportContactInfo.  # noqa: E501


        :return: The site_id of this SupportContactInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this SupportContactInfo.


        :param site_id: The site_id of this SupportContactInfo.  # noqa: E501
        :type: list[str]
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def default_site_id(self):
        """Gets the default_site_id of this SupportContactInfo.  # noqa: E501


        :return: The default_site_id of this SupportContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._default_site_id

    @default_site_id.setter
    def default_site_id(self, default_site_id):
        """Sets the default_site_id of this SupportContactInfo.


        :param default_site_id: The default_site_id of this SupportContactInfo.  # noqa: E501
        :type: str
        """

        self._default_site_id = default_site_id

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
        if issubclass(SupportContactInfo, dict):
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
        if not isinstance(other, SupportContactInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
