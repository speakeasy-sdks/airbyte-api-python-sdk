"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from airbyte.models import operations, shared
from typing import Optional

class Workspaces:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def create_or_update_workspace_o_auth_credentials(self, request: operations.CreateOrUpdateWorkspaceOAuthCredentialsRequest) -> operations.CreateOrUpdateWorkspaceOAuthCredentialsResponse:
        r"""Create OAuth override credentials for a workspace and source type.
        Create/update a set of OAuth credentials to override the Airbyte-provided OAuth credentials used for source/destination OAuth.
        In order to determine what the credential configuration needs to be, please see the connector specification of the relevant  source/destination.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateOrUpdateWorkspaceOAuthCredentialsRequest, base_url, '/workspaces/{workspaceId}/oauthCredentials', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "workspace_o_auth_credentials_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateOrUpdateWorkspaceOAuthCredentialsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def create_workspace(self, request: shared.WorkspaceCreateRequest) -> operations.CreateWorkspaceResponse:
        r"""Create a workspace"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/workspaces'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateWorkspaceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.WorkspaceResponse])
                res.workspace_response = out
        elif http_res.status_code in [400, 403]:
            pass

        return res

    
    def get_workspace(self, request: operations.GetWorkspaceRequest) -> operations.GetWorkspaceResponse:
        r"""Get Workspace details"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetWorkspaceRequest, base_url, '/workspaces/{workspaceId}', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetWorkspaceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.WorkspaceResponse])
                res.workspace_response = out
        elif http_res.status_code in [403, 404]:
            pass

        return res

    
    def list_workspaces(self, request: operations.ListWorkspacesRequest) -> operations.ListWorkspacesResponse:
        r"""List workspaces"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/workspaces'
        
        headers = {}
        query_params = utils.get_query_params(operations.ListWorkspacesRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListWorkspacesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.WorkspacesResponse])
                res.workspaces_response = out
        elif http_res.status_code in [403, 404]:
            pass

        return res

    