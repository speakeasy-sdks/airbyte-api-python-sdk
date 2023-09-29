"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class SourceAmazonAdsRegion(str, Enum):
    r"""Region to pull data from (EU/NA/FE). See <a href=\\"https://advertising.amazon.com/API/docs/en-us/info/api-overview#api-endpoints\\">docs</a> for more details."""
    NA = 'NA'
    EU = 'EU'
    FE = 'FE'

class SourceAmazonAdsReportRecordTypes(str, Enum):
    AD_GROUPS = 'adGroups'
    ASINS = 'asins'
    ASINS_KEYWORDS = 'asins_keywords'
    ASINS_TARGETS = 'asins_targets'
    CAMPAIGNS = 'campaigns'
    KEYWORDS = 'keywords'
    PRODUCT_ADS = 'productAds'
    TARGETS = 'targets'

class SourceAmazonAdsStateFilter(str, Enum):
    ENABLED = 'enabled'
    PAUSED = 'paused'
    ARCHIVED = 'archived'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceAmazonAds:
    r"""The values required to configure the source."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The client ID of your Amazon Ads developer application. See the <a href=\\"https://advertising.amazon.com/API/docs/en-us/get-started/generate-api-tokens#retrieve-your-client-id-and-client-secret\\">docs</a> for more information."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret of your Amazon Ads developer application. See the <a href=\\"https://advertising.amazon.com/API/docs/en-us/get-started/generate-api-tokens#retrieve-your-client-id-and-client-secret\\">docs</a> for more information."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Amazon Ads refresh token. See the <a href=\\"https://advertising.amazon.com/API/docs/en-us/get-started/generate-api-tokens\\">docs</a> for more information on how to obtain this token."""
    SOURCE_TYPE: Final[str] = dataclasses.field(default='amazon-ads', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    AUTH_TYPE: Final[Optional[str]] = dataclasses.field(default='oauth2.0', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    look_back_window: Optional[int] = dataclasses.field(default=3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('look_back_window'), 'exclude': lambda f: f is None }})
    r"""The amount of days to go back in time to get the updated data from Amazon Ads"""
    marketplace_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('marketplace_ids'), 'exclude': lambda f: f is None }})
    r"""Marketplace IDs you want to fetch data for. Note: If Profile IDs are also selected, profiles will be selected if they match the Profile ID OR the Marketplace ID."""
    profiles: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profiles'), 'exclude': lambda f: f is None }})
    r"""Profile IDs you want to fetch data for. See <a href=\\"https://advertising.amazon.com/API/docs/en-us/concepts/authorization/profiles\\">docs</a> for more details. Note: If Marketplace IDs are also selected, profiles will be selected if they match the Profile ID OR the Marketplace ID."""
    region: Optional[SourceAmazonAdsRegion] = dataclasses.field(default=SourceAmazonAdsRegion.NA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""Region to pull data from (EU/NA/FE). See <a href=\\"https://advertising.amazon.com/API/docs/en-us/info/api-overview#api-endpoints\\">docs</a> for more details."""
    report_record_types: Optional[list[SourceAmazonAdsReportRecordTypes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('report_record_types'), 'exclude': lambda f: f is None }})
    r"""Optional configuration which accepts an array of string of record types. Leave blank for default behaviour to pull all report types. Use this config option only if you want to pull specific report type(s). See <a href=\\"https://advertising.amazon.com/API/docs/en-us/reporting/v2/report-types\\">docs</a> for more details"""
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    r"""The Start date for collecting reports, should not be more than 60 days in the past. In YYYY-MM-DD format"""
    state_filter: Optional[list[SourceAmazonAdsStateFilter]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state_filter'), 'exclude': lambda f: f is None }})
    r"""Reflects the state of the Display, Product, and Brand Campaign streams as enabled, paused, or archived. If you do not populate this field, it will be ignored completely."""
    

