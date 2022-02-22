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


class RequestStatusApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_request_id_get(self, id, **kwargs):  # noqa: E501
        """Get the status of a request  # noqa: E501

        Retrieve the operation status and progress report of the specified request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_request_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The request ID of any long running operation. (required)
        :return: RequestStatusInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_request_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_request_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_request_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get the status of a request  # noqa: E501

        Retrieve the operation status and progress report of the specified request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_request_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The request ID of any long running operation. (required)
        :return: RequestStatusInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_request_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1_request_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v1/requests/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RequestStatusInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_requests_get(self, **kwargs):  # noqa: E501
        """Query all requests  # noqa: E501

        Query all of the requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_requests_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: Query condictions for requests. Equal(eq), in(in) and not equal(ne) supported fields: id, state, owner, target, step. Equal(eq), not equal(ne), in(in), greater than(gt), less than(lt), greater or equal to(ge) and less or equal to(le) supported fields: start_time, end_time, progress. Example: $filter=id eq 'e9082a79-12c8-484f-9b11-76c1a6e2f36b' and owner eq 'LOG_BUNDLE' and state in ('FAILED','IN_PROGRESS') and start_time gt 10000.
        :return: list[RequestStatusInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_requests_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_requests_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_requests_get_with_http_info(self, **kwargs):  # noqa: E501
        """Query all requests  # noqa: E501

        Query all of the requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_requests_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: Query condictions for requests. Equal(eq), in(in) and not equal(ne) supported fields: id, state, owner, target, step. Equal(eq), not equal(ne), in(in), greater than(gt), less than(lt), greater or equal to(ge) and less or equal to(le) supported fields: start_time, end_time, progress. Example: $filter=id eq 'e9082a79-12c8-484f-9b11-76c1a6e2f36b' and owner eq 'LOG_BUNDLE' and state in ('FAILED','IN_PROGRESS') and start_time gt 10000.
        :return: list[RequestStatusInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_requests_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('$filter', params['filter']))  # noqa: E501

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
            '/v1/requests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RequestStatusInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
