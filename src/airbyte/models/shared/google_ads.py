"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GoogleAdsCredentials:
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""Access Token for making authenticated requests. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>"""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The Client ID of your Google Ads developer application. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>"""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The Client Secret of your Google Ads developer application. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>"""
    developer_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('developer_token'), 'exclude': lambda f: f is None }})
    r"""Developer token granted by Google to use their APIs. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>"""
    refresh_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token'), 'exclude': lambda f: f is None }})
    r"""The token for obtaining a new access token. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GoogleAds:
    r"""The values required to configure the source."""
    credentials: Optional[GoogleAdsCredentials] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    

