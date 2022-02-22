# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.350
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vxrail_ansible_utility.api_client import ApiClient


class SystemPreCheckApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_system_precheck_post(self, body, **kwargs):  # noqa: E501
        """Perform a pre-check  # noqa: E501

        Perform a system pre-check.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_precheck_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PrecheckSpec body: (required)
        :return: AsyncPrecheckSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_precheck_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_precheck_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_system_precheck_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Perform a pre-check  # noqa: E501

        Perform a system pre-check.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_precheck_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PrecheckSpec body: (required)
        :return: AsyncPrecheckSuccessResponse
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
                    " to method v1_system_precheck_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_system_precheck_post`")  # noqa: E501

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
            '/v1/system/precheck', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncPrecheckSuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_precheck_results_get(self, **kwargs):  # noqa: E501
        """Get all pre-check reports  # noqa: E501

        Get a list of pre-check reports, which include the current running status and historical results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_precheck_results_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PrecheckReportsInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_precheck_results_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_precheck_results_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_system_precheck_results_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all pre-check reports  # noqa: E501

        Get a list of pre-check reports, which include the current running status and historical results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_precheck_results_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PrecheckReportsInfo
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
                    " to method v1_system_precheck_results_get" % key
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
            '/v1/system/prechecks/results', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrecheckReportsInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_precheck_results_id_get(self, id, **kwargs):  # noqa: E501
        """Get a pre-check result  # noqa: E501

        Get a pre-check result using a specified request ID. Available reports include a status report from a currently running pre-check process or a report from previously run pre-check.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_precheck_results_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Request ID of the pre-check status that you want to query (required)
        :param bool verbose: Whether to return a full or simplified report. The default is true. Set to true to return a full pre -check result report. Set to falsefor a simplified report.
        :return: PrecheckReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_precheck_results_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_precheck_results_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_system_precheck_results_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a pre-check result  # noqa: E501

        Get a pre-check result using a specified request ID. Available reports include a status report from a currently running pre-check process or a report from previously run pre-check.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_precheck_results_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Request ID of the pre-check status that you want to query (required)
        :param bool verbose: Whether to return a full or simplified report. The default is true. Set to true to return a full pre -check result report. Set to falsefor a simplified report.
        :return: PrecheckReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'verbose']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_system_precheck_results_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1_system_precheck_results_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'verbose' in params:
            query_params.append(('verbose', params['verbose']))  # noqa: E501

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
            '/v1/system/prechecks/{id}/result', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrecheckReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_prechecks_profiles_get(self, **kwargs):  # noqa: E501
        """List pre-check profiles  # noqa: E501

        Get a list of available pre-check profiles. Each profile represents a different type of pre-check that you can perform.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_prechecks_profiles_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ProfileInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_prechecks_profiles_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_prechecks_profiles_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_system_prechecks_profiles_get_with_http_info(self, **kwargs):  # noqa: E501
        """List pre-check profiles  # noqa: E501

        Get a list of available pre-check profiles. Each profile represents a different type of pre-check that you can perform.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_prechecks_profiles_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ProfileInfo]
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
                    " to method v1_system_prechecks_profiles_get" % key
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
            '/v1/system/prechecks/profiles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProfileInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_prechecks_version_get(self, **kwargs):  # noqa: E501
        """Get the pre-check version  # noqa: E501

        Get the current version of the pre-check service in the VxRail system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_prechecks_version_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PrecheckVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_prechecks_version_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_prechecks_version_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_system_prechecks_version_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get the pre-check version  # noqa: E501

        Get the current version of the pre-check service in the VxRail system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_prechecks_version_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PrecheckVersion
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
                    " to method v1_system_prechecks_version_get" % key
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
            '/v1/system/prechecks/precheck-service-version', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrecheckVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
