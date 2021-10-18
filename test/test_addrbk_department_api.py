"""
    LanXin+ OpenAPI

    LanXin+ OpenAPI Platform  # noqa: E501

    Generated by: https://openapi.lanxin.cn
"""

import unittest

from pprint import pprint
try:
    import lanxinplus_openapi
except ImportError:
    import sys
    sys.path.append(sys.argv[0].replace("\\test\\test_addrbk_department_api.py", "\\"))  # noqa: E501
    import lanxinplus_openapi
from lanxinplus_openapi.api.addrbk_department_api import AddrbkDepartmentApi  # noqa: E501
from lanxinplus_openapi import Configuration
from lanxinplus_openapi.model.v1_depts_children_fetch_response import V1DeptsChildrenFetchResponse
from lanxinplus_openapi.model.v1_depts_create_request_body import V1DeptsCreateRequestBody
from lanxinplus_openapi.model.v1_depts_create_response import V1DeptsCreateResponse
from lanxinplus_openapi.model.v1_depts_delete_response import V1DeptsDeleteResponse
from lanxinplus_openapi.model.v1_depts_fetch_response import V1DeptsFetchResponse
from lanxinplus_openapi.model.v1_depts_staffs_create_response import V1DeptsStaffsCreateResponse
from lanxinplus_openapi.model.v1_depts_staffs_delete_response import V1DeptsStaffsDeleteResponse
from lanxinplus_openapi.model.v1_depts_staffs_fetch_response import V1DeptsStaffsFetchResponse
from lanxinplus_openapi.model.v1_depts_update_request_body import V1DeptsUpdateRequestBody
from lanxinplus_openapi.model.v1_depts_update_response import V1DeptsUpdateResponse
from lanxinplus_openapi.api.auth_api import AuthApi


class TestAddrbkDepartmentApi(unittest.TestCase):
    """AddrbkDepartmentApi unit test stubs"""

    @classmethod
    def setUpClass(cls):
        # 蓝信开放平台网关地址, e.g.: https://example.com/open/apigw
        host = "host"
        # 应用ID, e.g.: 1234567-7654321
        app_id = "app_id"
        # 应用密钥, e.g.: D25F65E65D887AEFD9C92B00310286FA
        app_secret = "app_secret"

        cls.config = Configuration(host, app_id, app_secret)
        # Configuration.set_default(cls.config)
        cls.client = lanxinplus_openapi.ApiClient(configuration=cls.config)
        cls.api = AddrbkDepartmentApi(api_client=cls.client)  # noqa: E501
        # get app_token
        try:
            api = AuthApi(api_client=cls.client)
            resp = api.v1_app_token_create("client_credential", cls.config.app_id, cls.config.app_secret)
            if resp.errCode == 0:
                cls.config.set_app_token(resp.data.appToken, resp.data.expiresIn)
            else:
                raise lanxinplus_openapi.ApiException(reason=resp.errMsg)
        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AuthApi->v1_apptoken_create: %s\n" % e)


    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_v1_depts_children_fetch(self):
        """Test case for v1_depts_children_fetch
        获取子分支列表  # noqa: E501
        """
        
        app_token = self.config.app_token # str | app_token
        departmentid = "departmentid_example" # str | departmentid
        user_token = self.config.user_token # str | user_token (optional)

        # example passing only required values which don't have defaults set
        try:
            # 获取子分支列表
            resp = self.api.v1_depts_children_fetch(app_token, departmentid)
            print("TestCase AddrbkDepartmentApi->v1_depts_children_fetch: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)
        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_children_fetch: %s\n" % e)

        '''
        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # 获取子分支列表
            resp = self.api.v1_depts_children_fetch(app_token, departmentid, user_token=user_token)
            print("TestCase AddrbkDepartmentApi->v1_depts_children_fetch: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)

        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_children_fetch: %s\n" % e)
        '''


    def test_v1_depts_create(self):
        """Test case for v1_depts_create
        创建分支  # noqa: E501
        """
        
        app_token = self.config.app_token # str | app_token
        v1_depts_create_request_body = V1DeptsCreateRequestBody(
        externalId="externalId_example",
        name="name_example",
        orderNumber=1,
        parentId="parentId_example",
        tags=[
            "tags_example",
        ],
    ) # V1DeptsCreateRequestBody | Request Body
        user_token = self.config.user_token # str | user_token (optional)

        # example passing only required values which don't have defaults set
        try:
            # 创建分支
            resp = self.api.v1_depts_create(app_token, v1_depts_create_request_body)
            print("TestCase AddrbkDepartmentApi->v1_depts_create: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)
        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_create: %s\n" % e)

        '''
        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # 创建分支
            resp = self.api.v1_depts_create(app_token, v1_depts_create_request_body, user_token=user_token)
            print("TestCase AddrbkDepartmentApi->v1_depts_create: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)

        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_create: %s\n" % e)
        '''


    def test_v1_depts_delete(self):
        """Test case for v1_depts_delete
        删除分支  # noqa: E501
        """
        
        app_token = self.config.app_token # str | app_token
        departmentid = "departmentid_example" # str | departmentid
        user_token = self.config.user_token # str | user_token (optional)

        # example passing only required values which don't have defaults set
        try:
            # 删除分支
            resp = self.api.v1_depts_delete(app_token, departmentid)
            print("TestCase AddrbkDepartmentApi->v1_depts_delete: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)
        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_delete: %s\n" % e)

        '''
        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # 删除分支
            resp = self.api.v1_depts_delete(app_token, departmentid, user_token=user_token)
            print("TestCase AddrbkDepartmentApi->v1_depts_delete: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)

        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_delete: %s\n" % e)
        '''


    def test_v1_depts_fetch(self):
        """Test case for v1_depts_fetch
        获取分支详情  # noqa: E501
        """
        
        app_token = self.config.app_token # str | app_token
        departmentid = "departmentid_example" # str | departmentid
        user_token = self.config.user_token # str | user_token (optional)

        # example passing only required values which don't have defaults set
        try:
            # 获取分支详情
            resp = self.api.v1_depts_fetch(app_token, departmentid)
            print("TestCase AddrbkDepartmentApi->v1_depts_fetch: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)
        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_fetch: %s\n" % e)

        '''
        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # 获取分支详情
            resp = self.api.v1_depts_fetch(app_token, departmentid, user_token=user_token)
            print("TestCase AddrbkDepartmentApi->v1_depts_fetch: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)

        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_fetch: %s\n" % e)
        '''


    def test_v1_depts_staffs_create(self):
        """Test case for v1_depts_staffs_create
        添加分支成员  # noqa: E501
        """
        
        app_token = self.config.app_token # str | app_token
        departmentid = "departmentid_example" # str | departmentid
        staffid = "staffid_example" # str | staffid
        user_token = self.config.user_token # str | user_token (optional)

        # example passing only required values which don't have defaults set
        try:
            # 添加分支成员
            resp = self.api.v1_depts_staffs_create(app_token, departmentid, staffid)
            print("TestCase AddrbkDepartmentApi->v1_depts_staffs_create: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)
        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_staffs_create: %s\n" % e)

        '''
        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # 添加分支成员
            resp = self.api.v1_depts_staffs_create(app_token, departmentid, staffid, user_token=user_token)
            print("TestCase AddrbkDepartmentApi->v1_depts_staffs_create: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)

        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_staffs_create: %s\n" % e)
        '''


    def test_v1_depts_staffs_delete(self):
        """Test case for v1_depts_staffs_delete
        删除分支成员  # noqa: E501
        """
        
        app_token = self.config.app_token # str | app_token
        departmentid = "departmentid_example" # str | departmentid
        staffid = "staffid_example" # str | staffid
        user_token = self.config.user_token # str | user_token (optional)

        # example passing only required values which don't have defaults set
        try:
            # 删除分支成员
            resp = self.api.v1_depts_staffs_delete(app_token, departmentid, staffid)
            print("TestCase AddrbkDepartmentApi->v1_depts_staffs_delete: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)
        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_staffs_delete: %s\n" % e)

        '''
        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # 删除分支成员
            resp = self.api.v1_depts_staffs_delete(app_token, departmentid, staffid, user_token=user_token)
            print("TestCase AddrbkDepartmentApi->v1_depts_staffs_delete: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)

        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_staffs_delete: %s\n" % e)
        '''


    def test_v1_depts_staffs_fetch(self):
        """Test case for v1_depts_staffs_fetch
        获取分支成员列表  # noqa: E501
        """
        
        app_token = self.config.app_token # str | app_token
        departmentid = "departmentid_example" # str | departmentid
        user_token = self.config.user_token # str | user_token (optional)
        page = 1 # int | 起始页码从1开始，默认值为1 (optional)
        page_size = 1 # int | 每页显示个数，默认值是100，最大值是100 (optional)

        # example passing only required values which don't have defaults set
        try:
            # 获取分支成员列表
            resp = self.api.v1_depts_staffs_fetch(app_token, departmentid)
            print("TestCase AddrbkDepartmentApi->v1_depts_staffs_fetch: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)
        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_staffs_fetch: %s\n" % e)

        '''
        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # 获取分支成员列表
            resp = self.api.v1_depts_staffs_fetch(app_token, departmentid, user_token=user_token, page=page, page_size=page_size)
            print("TestCase AddrbkDepartmentApi->v1_depts_staffs_fetch: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)

        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_staffs_fetch: %s\n" % e)
        '''


    def test_v1_depts_update(self):
        """Test case for v1_depts_update
        更新分支  # noqa: E501
        """
        
        app_token = self.config.app_token # str | app_token
        departmentid = "departmentid_example" # str | departmentid
        v1_depts_update_request_body = V1DeptsUpdateRequestBody(
        name="name_example",
        orderNumber=1,
        parentId="parentId_example",
        tags=[
            "tags_example",
        ],
    ) # V1DeptsUpdateRequestBody | Request Body
        user_token = self.config.user_token # str | user_token (optional)

        # example passing only required values which don't have defaults set
        try:
            # 更新分支
            resp = self.api.v1_depts_update(app_token, departmentid, v1_depts_update_request_body)
            print("TestCase AddrbkDepartmentApi->v1_depts_update: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)
        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_update: %s\n" % e)

        '''
        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # 更新分支
            resp = self.api.v1_depts_update(app_token, departmentid, v1_depts_update_request_body, user_token=user_token)
            print("TestCase AddrbkDepartmentApi->v1_depts_update: ")
            pprint(resp)
            self.assertEqual(resp.errCode, 0)

        except lanxinplus_openapi.ApiException as e:
            print("Exception when calling AddrbkDepartmentApi->v1_depts_update: %s\n" % e)
        '''



if __name__ == '__main__':
    unittest.main()
