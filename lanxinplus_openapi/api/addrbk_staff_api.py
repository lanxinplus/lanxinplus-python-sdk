"""
    LanXin+ OpenAPI

    LanXin+ OpenAPI Platform  # noqa: E501

    Generated by: https://openapi.lanxin.cn
"""


import re  # noqa: F401
import sys  # noqa: F401

from lanxinplus_openapi.api_client import ApiClient, Endpoint as _Endpoint
from lanxinplus_openapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from lanxinplus_openapi.model.v1_org_extra_field_ids_fetch_response import V1OrgExtraFieldIdsFetchResponse
from lanxinplus_openapi.model.v1_staffs_create_request_body import V1StaffsCreateRequestBody
from lanxinplus_openapi.model.v1_staffs_create_response import V1StaffsCreateResponse
from lanxinplus_openapi.model.v1_staffs_delete_response import V1StaffsDeleteResponse
from lanxinplus_openapi.model.v1_staffs_dept_ancestors_fetch_response import V1StaffsDeptAncestorsFetchResponse
from lanxinplus_openapi.model.v1_staffs_fetch_response import V1StaffsFetchResponse
from lanxinplus_openapi.model.v1_staffs_infor_fetch_response import V1StaffsInforFetchResponse
from lanxinplus_openapi.model.v1_staffs_update_request_body import V1StaffsUpdateRequestBody
from lanxinplus_openapi.model.v1_staffs_update_response import V1StaffsUpdateResponse
from lanxinplus_openapi.model.v1_tags_fetch_request_body import V1TagsFetchRequestBody
from lanxinplus_openapi.model.v1_tags_fetch_response import V1TagsFetchResponse
from lanxinplus_openapi.model.v2_staffs_id_mapping_fetch_response import V2StaffsIdMappingFetchResponse
from lanxinplus_openapi.model.v2_staffs_search_request_body import V2StaffsSearchRequestBody
from lanxinplus_openapi.model.v2_staffs_search_response import V2StaffsSearchResponse


class AddrbkStaffApi(object):
    """NOTE: This class is auto generated by LanXin+
    Ref: https://openapi.lanxin.cn

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.v1_org_extra_field_ids_fetch_endpoint = _Endpoint(
            settings={
                'response_type': (V1OrgExtraFieldIdsFetchResponse,),
                'auth': [],
                'endpoint_path': '/v1/org/{orgid}/extrafieldids/fetch',
                'operation_id': 'v1_org_extra_field_ids_fetch',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'orgid',
                    'user_token',
                    'page',
                    'page_size',
                ],
                'required': [
                    'app_token',
                    'orgid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'orgid':
                        (str,),
                    'user_token':
                        (str,),
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'orgid': 'orgid',
                    'user_token': 'user_token',
                    'page': 'page',
                    'page_size': 'page_size',
                },
                'location_map': {
                    'app_token': 'query',
                    'orgid': 'path',
                    'user_token': 'query',
                    'page': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.v1_staffs_create_endpoint = _Endpoint(
            settings={
                'response_type': (V1StaffsCreateResponse,),
                'auth': [],
                'endpoint_path': '/v1/staffs/create',
                'operation_id': 'v1_staffs_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'v1_staffs_create_request_body',
                    'user_token',
                ],
                'required': [
                    'app_token',
                    'v1_staffs_create_request_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'v1_staffs_create_request_body':
                        (V1StaffsCreateRequestBody,),
                    'user_token':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'user_token': 'user_token',
                },
                'location_map': {
                    'app_token': 'query',
                    'v1_staffs_create_request_body': 'body',
                    'user_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.v1_staffs_delete_endpoint = _Endpoint(
            settings={
                'response_type': (V1StaffsDeleteResponse,),
                'auth': [],
                'endpoint_path': '/v1/staffs/{staffid}/delete',
                'operation_id': 'v1_staffs_delete',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'staffid',
                    'user_token',
                ],
                'required': [
                    'app_token',
                    'staffid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'staffid':
                        (str,),
                    'user_token':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'staffid': 'staffid',
                    'user_token': 'user_token',
                },
                'location_map': {
                    'app_token': 'query',
                    'staffid': 'path',
                    'user_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.v1_staffs_dept_ancestors_fetch_endpoint = _Endpoint(
            settings={
                'response_type': (V1StaffsDeptAncestorsFetchResponse,),
                'auth': [],
                'endpoint_path': '/v1/staffs/{staffid}/departmentancestors/fetch',
                'operation_id': 'v1_staffs_dept_ancestors_fetch',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'staffid',
                    'user_token',
                ],
                'required': [
                    'app_token',
                    'staffid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'staffid':
                        (str,),
                    'user_token':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'staffid': 'staffid',
                    'user_token': 'user_token',
                },
                'location_map': {
                    'app_token': 'query',
                    'staffid': 'path',
                    'user_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.v1_staffs_fetch_endpoint = _Endpoint(
            settings={
                'response_type': (V1StaffsFetchResponse,),
                'auth': [],
                'endpoint_path': '/v1/staffs/{staffid}/fetch',
                'operation_id': 'v1_staffs_fetch',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'staffid',
                    'user_token',
                ],
                'required': [
                    'app_token',
                    'staffid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'staffid':
                        (str,),
                    'user_token':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'staffid': 'staffid',
                    'user_token': 'user_token',
                },
                'location_map': {
                    'app_token': 'query',
                    'staffid': 'path',
                    'user_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.v1_staffs_infor_fetch_endpoint = _Endpoint(
            settings={
                'response_type': (V1StaffsInforFetchResponse,),
                'auth': [],
                'endpoint_path': '/v1/staffs/{staffid}/infor/fetch',
                'operation_id': 'v1_staffs_infor_fetch',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'staffid',
                    'user_token',
                ],
                'required': [
                    'app_token',
                    'staffid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'staffid':
                        (str,),
                    'user_token':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'staffid': 'staffid',
                    'user_token': 'user_token',
                },
                'location_map': {
                    'app_token': 'query',
                    'staffid': 'path',
                    'user_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.v1_staffs_update_endpoint = _Endpoint(
            settings={
                'response_type': (V1StaffsUpdateResponse,),
                'auth': [],
                'endpoint_path': '/v1/staffs/{staffid}/update',
                'operation_id': 'v1_staffs_update',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'staffid',
                    'v1_staffs_update_request_body',
                    'user_token',
                ],
                'required': [
                    'app_token',
                    'staffid',
                    'v1_staffs_update_request_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'staffid':
                        (str,),
                    'v1_staffs_update_request_body':
                        (V1StaffsUpdateRequestBody,),
                    'user_token':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'staffid': 'staffid',
                    'user_token': 'user_token',
                },
                'location_map': {
                    'app_token': 'query',
                    'staffid': 'path',
                    'v1_staffs_update_request_body': 'body',
                    'user_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.v1_tags_fetch_endpoint = _Endpoint(
            settings={
                'response_type': (V1TagsFetchResponse,),
                'auth': [],
                'endpoint_path': '/v1/tags/staffids/fetch',
                'operation_id': 'v1_tags_fetch',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'v1_tags_fetch_request_body',
                    'user_token',
                    'page',
                    'page_size',
                ],
                'required': [
                    'app_token',
                    'v1_tags_fetch_request_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'v1_tags_fetch_request_body':
                        (V1TagsFetchRequestBody,),
                    'user_token':
                        (str,),
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'user_token': 'user_token',
                    'page': 'page',
                    'page_size': 'page_size',
                },
                'location_map': {
                    'app_token': 'query',
                    'v1_tags_fetch_request_body': 'body',
                    'user_token': 'query',
                    'page': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.v2_staffs_id_mapping_fetch_endpoint = _Endpoint(
            settings={
                'response_type': (V2StaffsIdMappingFetchResponse,),
                'auth': [],
                'endpoint_path': '/v2/staffs/id_mapping/fetch',
                'operation_id': 'v2_staffs_id_mapping_fetch',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'org_id',
                    'id_type',
                    'id_value',
                    'user_token',
                ],
                'required': [
                    'app_token',
                    'org_id',
                    'id_type',
                    'id_value',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'org_id':
                        (str,),
                    'id_type':
                        (str,),
                    'id_value':
                        (str,),
                    'user_token':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'org_id': 'org_id',
                    'id_type': 'id_type',
                    'id_value': 'id_value',
                    'user_token': 'user_token',
                },
                'location_map': {
                    'app_token': 'query',
                    'org_id': 'query',
                    'id_type': 'query',
                    'id_value': 'query',
                    'user_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.v2_staffs_search_endpoint = _Endpoint(
            settings={
                'response_type': (V2StaffsSearchResponse,),
                'auth': [],
                'endpoint_path': '/v2/staffs/search',
                'operation_id': 'v2_staffs_search',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'user_id',
                    'v2_staffs_search_request_body',
                    'user_token',
                ],
                'required': [
                    'app_token',
                    'user_id',
                    'v2_staffs_search_request_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'user_id':
                        (str,),
                    'v2_staffs_search_request_body':
                        (V2StaffsSearchRequestBody,),
                    'user_token':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'user_id': 'user_id',
                    'user_token': 'user_token',
                },
                'location_map': {
                    'app_token': 'query',
                    'user_id': 'query',
                    'v2_staffs_search_request_body': 'body',
                    'user_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def v1_org_extra_field_ids_fetch(
        self,
        app_token,
        orgid,
        **kwargs
    ):
        """获取人员信息扩展字段id列表  # noqa: E501

        获取组织内人员信息的扩展字段ID列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_org_extra_field_ids_fetch(app_token, orgid, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            orgid (str): orgid

        Keyword Args:
            user_token (str): user_token. [optional]
            page (int): 起始页码从1开始,默认值为1. [optional]
            page_size (int): 每页显示个数，默认值是1000，最大值是100000. [optional]

        Returns:
            V1OrgExtraFieldIdsFetchResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['orgid'] = \
            orgid
        return self.v1_org_extra_field_ids_fetch_endpoint.call_with_http_info(**kwargs)

    def v1_staffs_create(
        self,
        app_token,
        v1_staffs_create_request_body,
        **kwargs
    ):
        """创建人员  # noqa: E501

        通过此接口，可以创建人员。仅组织内应用经过授权可以调用该接口。 特别说明：目前蓝信不支持应用并发调用人员创建接口，否则会出现添加人员到部门的操作失败，应用需要保证串行化调用该接口  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_staffs_create(app_token, v1_staffs_create_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            v1_staffs_create_request_body (V1StaffsCreateRequestBody): Request Body

        Keyword Args:
            user_token (str): user_token. [optional]

        Returns:
            V1StaffsCreateResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['v1_staffs_create_request_body'] = \
            v1_staffs_create_request_body
        return self.v1_staffs_create_endpoint.call_with_http_info(**kwargs)

    def v1_staffs_delete(
        self,
        app_token,
        staffid,
        **kwargs
    ):
        """人员删除接口  # noqa: E501

        通过此接口，删除人员  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_staffs_delete(app_token, staffid, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            staffid (str): 人员 id

        Keyword Args:
            user_token (str): user_token. [optional]

        Returns:
            V1StaffsDeleteResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['staffid'] = \
            staffid
        return self.v1_staffs_delete_endpoint.call_with_http_info(**kwargs)

    def v1_staffs_dept_ancestors_fetch(
        self,
        app_token,
        staffid,
        **kwargs
    ):
        """获取人员分支祖先列表  # noqa: E501

        获取某个人员所在的所有分支的祖先列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_staffs_dept_ancestors_fetch(app_token, staffid, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            staffid (str): staffid

        Keyword Args:
            user_token (str): user_token. [optional]

        Returns:
            V1StaffsDeptAncestorsFetchResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['staffid'] = \
            staffid
        return self.v1_staffs_dept_ancestors_fetch_endpoint.call_with_http_info(**kwargs)

    def v1_staffs_fetch(
        self,
        app_token,
        staffid,
        **kwargs
    ):
        """获取人员基本信息  # noqa: E501

        可以获人员的基本信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_staffs_fetch(app_token, staffid, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            staffid (str): staffid

        Keyword Args:
            user_token (str): user_token. [optional]

        Returns:
            V1StaffsFetchResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['staffid'] = \
            staffid
        return self.v1_staffs_fetch_endpoint.call_with_http_info(**kwargs)

    def v1_staffs_infor_fetch(
        self,
        app_token,
        staffid,
        **kwargs
    ):
        """获取人员详细信息  # noqa: E501

        通过此接口，可以获取人员详细信息。需要组织授权或者个人授权  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_staffs_infor_fetch(app_token, staffid, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            staffid (str): staffid

        Keyword Args:
            user_token (str): user_token. [optional]

        Returns:
            V1StaffsInforFetchResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['staffid'] = \
            staffid
        return self.v1_staffs_infor_fetch_endpoint.call_with_http_info(**kwargs)

    def v1_staffs_update(
        self,
        app_token,
        staffid,
        v1_staffs_update_request_body,
        **kwargs
    ):
        """更新人员  # noqa: E501

        通过此接口，可以更新人员信息。仅组织内应用经过授权可以调用该接口。 特别说明：如果涉及人员的部门信息更新，目前蓝信不支持应用并发调用人员更新接口，否则会出现更新人员部门的操作失败，应用需要保证串行化调用该接口  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_staffs_update(app_token, staffid, v1_staffs_update_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            staffid (str): 人员 id
            v1_staffs_update_request_body (V1StaffsUpdateRequestBody): Request Body

        Keyword Args:
            user_token (str): user_token. [optional]

        Returns:
            V1StaffsUpdateResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['staffid'] = \
            staffid
        kwargs['v1_staffs_update_request_body'] = \
            v1_staffs_update_request_body
        return self.v1_staffs_update_endpoint.call_with_http_info(**kwargs)

    def v1_tags_fetch(
        self,
        app_token,
        v1_tags_fetch_request_body,
        **kwargs
    ):
        """通过标签获取人员的id列表  # noqa: E501

        在组织内，通过指定标签过滤规则来筛选目标人员。 EMC管理后台和开放平台接口都提供关于标签的创建、修改、删除、给人员添加标签等功能，开发人员可以调用开放平台接口获取到已创建的所有标签分组， 然后根据指定的分组ID再获取到该分组下的所有标签  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_tags_fetch(app_token, v1_tags_fetch_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            v1_tags_fetch_request_body (V1TagsFetchRequestBody): Request Body

        Keyword Args:
            user_token (str): user_token. [optional]
            page (int): 起始页码从1开始，默认值为1. [optional]
            page_size (int): 每页显示个数，默认值是1000，最大值是100000. [optional]

        Returns:
            V1TagsFetchResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['v1_tags_fetch_request_body'] = \
            v1_tags_fetch_request_body
        return self.v1_tags_fetch_endpoint.call_with_http_info(**kwargs)

    def v2_staffs_id_mapping_fetch(
        self,
        app_token,
        org_id,
        id_type,
        id_value,
        **kwargs
    ):
        """获取人员详细信息  # noqa: E501

        通过此接口，可以获取人员详细信息。需要组织授权或者个人授权  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_staffs_id_mapping_fetch(app_token, org_id, id_type, id_value, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            org_id (str): 查询人员所在的组织Id
            id_type (str): employ_id/mobile/mail/login/external_id
            id_value (str): id_type 对应的值：人员编号，手机号...

        Keyword Args:
            user_token (str): user_token. [optional]

        Returns:
            V2StaffsIdMappingFetchResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['org_id'] = \
            org_id
        kwargs['id_type'] = \
            id_type
        kwargs['id_value'] = \
            id_value
        return self.v2_staffs_id_mapping_fetch_endpoint.call_with_http_info(**kwargs)

    def v2_staffs_search(
        self,
        app_token,
        user_id,
        v2_staffs_search_request_body,
        **kwargs
    ):
        """搜索人员  # noqa: E501

        搜索人员  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_staffs_search(app_token, user_id, v2_staffs_search_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            user_id (str): user_id
            v2_staffs_search_request_body (V2StaffsSearchRequestBody): Request Body

        Keyword Args:
            user_token (str): user_token. [optional]

        Returns:
            V2StaffsSearchResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['user_id'] = \
            user_id
        kwargs['v2_staffs_search_request_body'] = \
            v2_staffs_search_request_body
        return self.v2_staffs_search_endpoint.call_with_http_info(**kwargs)

