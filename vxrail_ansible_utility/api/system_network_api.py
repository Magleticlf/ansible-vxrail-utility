# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vxrail_ansible_utility.api_client import ApiClient


class SystemNetworkApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_system_cluster_portgroups_node_fqdn_get(self, node_fqdn, **kwargs):  # noqa: E501
        """Get information about cluster portgroups  # noqa: E501

        Retrieve information about cluster portgroups used by a node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_cluster_portgroups_node_fqdn_get(node_fqdn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_fqdn: The FQDN of the node that you want to query (required)
        :return: list[ClusterPortgroupInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_cluster_portgroups_node_fqdn_get_with_http_info(node_fqdn, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_cluster_portgroups_node_fqdn_get_with_http_info(node_fqdn, **kwargs)  # noqa: E501
            return data

    def v1_system_cluster_portgroups_node_fqdn_get_with_http_info(self, node_fqdn, **kwargs):  # noqa: E501
        """Get information about cluster portgroups  # noqa: E501

        Retrieve information about cluster portgroups used by a node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_cluster_portgroups_node_fqdn_get_with_http_info(node_fqdn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_fqdn: The FQDN of the node that you want to query (required)
        :return: list[ClusterPortgroupInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_fqdn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_system_cluster_portgroups_node_fqdn_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_fqdn' is set
        if ('node_fqdn' not in params or
                params['node_fqdn'] is None):
            raise ValueError("Missing the required parameter `node_fqdn` when calling `v1_system_cluster_portgroups_node_fqdn_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_fqdn' in params:
            path_params['node_fqdn'] = params['node_fqdn']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/system/cluster-portgroups/{node_fqdn}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ClusterPortgroupInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_internet_mode_get(self, **kwargs):  # noqa: E501
        """Get VxRail system network status  # noqa: E501

        Retrieve VxRail system network status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_internet_mode_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InternetMode
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_internet_mode_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_internet_mode_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_system_internet_mode_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get VxRail system network status  # noqa: E501

        Retrieve VxRail system network status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_internet_mode_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InternetMode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_system_internet_mode_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/system/internet-mode', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InternetMode',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_internet_mode_put(self, body, **kwargs):  # noqa: E501
        """Update the VxRail system network parameters  # noqa: E501

        Update the VxRail system network parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_internet_mode_put(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InternetMode body: Configure VxRail system network mode to darksite or not (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_internet_mode_put_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_internet_mode_put_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_system_internet_mode_put_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update the VxRail system network parameters  # noqa: E501

        Update the VxRail system network parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_internet_mode_put_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InternetMode body: Configure VxRail system network mode to darksite or not (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_system_internet_mode_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_system_internet_mode_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/system/internet-mode', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
