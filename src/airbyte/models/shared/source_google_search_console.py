"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceGoogleSearchConsoleAuthenticationTypeServiceAccountKeyAuthentication:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""The email of the user which has permissions to access the Google Workspace Admin APIs."""
    service_account_info: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_account_info') }})
    r"""The JSON key of the service account to use for authorization. Read more <a href=\\"https://cloud.google.com/iam/docs/creating-managing-service-account-keys\\">here</a>."""
    AUTH_TYPE: Final[str] = dataclasses.field(default='Service', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceGoogleSearchConsoleAuthenticationTypeOAuth:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The client ID of your Google Search Console developer application. Read more <a href=\\"https://developers.google.com/webmaster-tools/v1/how-tos/authorizing\\">here</a>."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret of your Google Search Console developer application. Read more <a href=\\"https://developers.google.com/webmaster-tools/v1/how-tos/authorizing\\">here</a>."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The token for obtaining a new access token. Read more <a href=\\"https://developers.google.com/webmaster-tools/v1/how-tos/authorizing\\">here</a>."""
    AUTH_TYPE: Final[str] = dataclasses.field(default='Client', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""Access token for making authenticated requests. Read more <a href=\\"https://developers.google.com/webmaster-tools/v1/how-tos/authorizing\\">here</a>."""
    




@dataclasses.dataclass
class SourceGoogleSearchConsoleAuthenticationType:
    pass

class SourceGoogleSearchConsoleCustomReportConfigValidEnums(str, Enum):
    r"""An enumeration of dimensions."""
    COUNTRY = 'country'
    DATE = 'date'
    DEVICE = 'device'
    PAGE = 'page'
    QUERY = 'query'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceGoogleSearchConsoleCustomReportConfig:
    dimensions: list[SourceGoogleSearchConsoleCustomReportConfigValidEnums] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dimensions') }})
    r"""A list of dimensions (country, date, device, page, query)"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the custom report, this name would be used as stream name"""
    


class SourceGoogleSearchConsoleDataFreshness(str, Enum):
    r"""If set to 'final', the returned data will include only finalized, stable data. If set to 'all', fresh data will be included. When using Incremental sync mode, we do not recommend setting this parameter to 'all' as it may cause data loss. More information can be found in our <a href='https://docs.airbyte.com/integrations/source/google-search-console'>full documentation</a>."""
    FINAL = 'final'
    ALL = 'all'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceGoogleSearchConsole:
    r"""The values required to configure the source."""
    authorization: Union[SourceGoogleSearchConsoleAuthenticationTypeOAuth, SourceGoogleSearchConsoleAuthenticationTypeServiceAccountKeyAuthentication] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization') }})
    site_urls: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site_urls') }})
    r"""The URLs of the website property attached to your GSC account. Learn more about properties <a href=\\"https://support.google.com/webmasters/answer/34592?hl=en\\">here</a>."""
    SOURCE_TYPE: Final[str] = dataclasses.field(default='google-search-console', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    custom_reports: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports'), 'exclude': lambda f: f is None }})
    r"""(DEPRCATED) A JSON array describing the custom reports you want to sync from Google Search Console. See our <a href='https://docs.airbyte.com/integrations/sources/google-search-console'>documentation</a> for more information on formulating custom reports."""
    custom_reports_array: Optional[list[SourceGoogleSearchConsoleCustomReportConfig]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports_array'), 'exclude': lambda f: f is None }})
    r"""You can add your Custom Analytics report by creating one."""
    data_state: Optional[SourceGoogleSearchConsoleDataFreshness] = dataclasses.field(default=SourceGoogleSearchConsoleDataFreshness.FINAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_state'), 'exclude': lambda f: f is None }})
    r"""If set to 'final', the returned data will include only finalized, stable data. If set to 'all', fresh data will be included. When using Incremental sync mode, we do not recommend setting this parameter to 'all' as it may cause data loss. More information can be found in our <a href='https://docs.airbyte.com/integrations/source/google-search-console'>full documentation</a>."""
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""UTC date in the format YYYY-MM-DD. Any data created after this date will not be replicated. Must be greater or equal to the start date field. Leaving this field blank will replicate all data from the start date onward."""
    start_date: Optional[date] = dataclasses.field(default=dateutil.parser.parse('2021-01-01').date(), metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""UTC date in the format YYYY-MM-DD. Any data before this date will not be replicated."""
    

