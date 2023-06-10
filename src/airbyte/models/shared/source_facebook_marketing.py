"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceFacebookMarketingInsightConfigValidActionBreakdowns(str, Enum):
    r"""Generic enumeration.
    
    Derive from this class to define new enumerations.
    """
    ACTION_CANVAS_COMPONENT_NAME = 'action_canvas_component_name'
    ACTION_CAROUSEL_CARD_ID = 'action_carousel_card_id'
    ACTION_CAROUSEL_CARD_NAME = 'action_carousel_card_name'
    ACTION_DESTINATION = 'action_destination'
    ACTION_DEVICE = 'action_device'
    ACTION_REACTION = 'action_reaction'
    ACTION_TARGET_ID = 'action_target_id'
    ACTION_TYPE = 'action_type'
    ACTION_VIDEO_SOUND = 'action_video_sound'
    ACTION_VIDEO_TYPE = 'action_video_type'

class SourceFacebookMarketingInsightConfigValidBreakdowns(str, Enum):
    r"""Generic enumeration.
    
    Derive from this class to define new enumerations.
    """
    AD_FORMAT_ASSET = 'ad_format_asset'
    AGE = 'age'
    APP_ID = 'app_id'
    BODY_ASSET = 'body_asset'
    CALL_TO_ACTION_ASSET = 'call_to_action_asset'
    COUNTRY = 'country'
    DESCRIPTION_ASSET = 'description_asset'
    DEVICE_PLATFORM = 'device_platform'
    DMA = 'dma'
    FREQUENCY_VALUE = 'frequency_value'
    GENDER = 'gender'
    HOURLY_STATS_AGGREGATED_BY_ADVERTISER_TIME_ZONE = 'hourly_stats_aggregated_by_advertiser_time_zone'
    HOURLY_STATS_AGGREGATED_BY_AUDIENCE_TIME_ZONE = 'hourly_stats_aggregated_by_audience_time_zone'
    IMAGE_ASSET = 'image_asset'
    IMPRESSION_DEVICE = 'impression_device'
    IS_CONVERSION_ID_MODELED = 'is_conversion_id_modeled'
    LINK_URL_ASSET = 'link_url_asset'
    MMM = 'mmm'
    PLACE_PAGE_ID = 'place_page_id'
    PLATFORM_POSITION = 'platform_position'
    PRODUCT_ID = 'product_id'
    PUBLISHER_PLATFORM = 'publisher_platform'
    REGION = 'region'
    SKAN_CAMPAIGN_ID = 'skan_campaign_id'
    SKAN_CONVERSION_ID = 'skan_conversion_id'
    TITLE_ASSET = 'title_asset'
    VIDEO_ASSET = 'video_asset'

class SourceFacebookMarketingInsightConfigValidEnums(str, Enum):
    r"""Generic enumeration.
    
    Derive from this class to define new enumerations.
    """
    ACCOUNT_CURRENCY = 'account_currency'
    ACCOUNT_ID = 'account_id'
    ACCOUNT_NAME = 'account_name'
    ACTION_VALUES = 'action_values'
    ACTIONS = 'actions'
    AD_BID_VALUE = 'ad_bid_value'
    AD_CLICK_ACTIONS = 'ad_click_actions'
    AD_ID = 'ad_id'
    AD_IMPRESSION_ACTIONS = 'ad_impression_actions'
    AD_NAME = 'ad_name'
    ADSET_BID_VALUE = 'adset_bid_value'
    ADSET_END = 'adset_end'
    ADSET_ID = 'adset_id'
    ADSET_NAME = 'adset_name'
    ADSET_START = 'adset_start'
    AGE_TARGETING = 'age_targeting'
    ATTRIBUTION_SETTING = 'attribution_setting'
    AUCTION_BID = 'auction_bid'
    AUCTION_COMPETITIVENESS = 'auction_competitiveness'
    AUCTION_MAX_COMPETITOR_BID = 'auction_max_competitor_bid'
    BUYING_TYPE = 'buying_type'
    CAMPAIGN_ID = 'campaign_id'
    CAMPAIGN_NAME = 'campaign_name'
    CANVAS_AVG_VIEW_PERCENT = 'canvas_avg_view_percent'
    CANVAS_AVG_VIEW_TIME = 'canvas_avg_view_time'
    CATALOG_SEGMENT_ACTIONS = 'catalog_segment_actions'
    CATALOG_SEGMENT_VALUE = 'catalog_segment_value'
    CATALOG_SEGMENT_VALUE_MOBILE_PURCHASE_ROAS = 'catalog_segment_value_mobile_purchase_roas'
    CATALOG_SEGMENT_VALUE_OMNI_PURCHASE_ROAS = 'catalog_segment_value_omni_purchase_roas'
    CATALOG_SEGMENT_VALUE_WEBSITE_PURCHASE_ROAS = 'catalog_segment_value_website_purchase_roas'
    CLICKS = 'clicks'
    CONVERSION_RATE_RANKING = 'conversion_rate_ranking'
    CONVERSION_VALUES = 'conversion_values'
    CONVERSIONS = 'conversions'
    CONVERTED_PRODUCT_QUANTITY = 'converted_product_quantity'
    CONVERTED_PRODUCT_VALUE = 'converted_product_value'
    COST_PER_15_SEC_VIDEO_VIEW = 'cost_per_15_sec_video_view'
    COST_PER_2_SEC_CONTINUOUS_VIDEO_VIEW = 'cost_per_2_sec_continuous_video_view'
    COST_PER_ACTION_TYPE = 'cost_per_action_type'
    COST_PER_AD_CLICK = 'cost_per_ad_click'
    COST_PER_CONVERSION = 'cost_per_conversion'
    COST_PER_DDA_COUNTBY_CONVS = 'cost_per_dda_countby_convs'
    COST_PER_ESTIMATED_AD_RECALLERS = 'cost_per_estimated_ad_recallers'
    COST_PER_INLINE_LINK_CLICK = 'cost_per_inline_link_click'
    COST_PER_INLINE_POST_ENGAGEMENT = 'cost_per_inline_post_engagement'
    COST_PER_ONE_THOUSAND_AD_IMPRESSION = 'cost_per_one_thousand_ad_impression'
    COST_PER_OUTBOUND_CLICK = 'cost_per_outbound_click'
    COST_PER_THRUPLAY = 'cost_per_thruplay'
    COST_PER_UNIQUE_ACTION_TYPE = 'cost_per_unique_action_type'
    COST_PER_UNIQUE_CLICK = 'cost_per_unique_click'
    COST_PER_UNIQUE_CONVERSION = 'cost_per_unique_conversion'
    COST_PER_UNIQUE_INLINE_LINK_CLICK = 'cost_per_unique_inline_link_click'
    COST_PER_UNIQUE_OUTBOUND_CLICK = 'cost_per_unique_outbound_click'
    CPC = 'cpc'
    CPM = 'cpm'
    CPP = 'cpp'
    CREATED_TIME = 'created_time'
    CTR = 'ctr'
    DATE_START = 'date_start'
    DATE_STOP = 'date_stop'
    DDA_COUNTBY_CONVS = 'dda_countby_convs'
    DDA_RESULTS = 'dda_results'
    ENGAGEMENT_RATE_RANKING = 'engagement_rate_ranking'
    ESTIMATED_AD_RECALL_RATE = 'estimated_ad_recall_rate'
    ESTIMATED_AD_RECALL_RATE_LOWER_BOUND = 'estimated_ad_recall_rate_lower_bound'
    ESTIMATED_AD_RECALL_RATE_UPPER_BOUND = 'estimated_ad_recall_rate_upper_bound'
    ESTIMATED_AD_RECALLERS = 'estimated_ad_recallers'
    ESTIMATED_AD_RECALLERS_LOWER_BOUND = 'estimated_ad_recallers_lower_bound'
    ESTIMATED_AD_RECALLERS_UPPER_BOUND = 'estimated_ad_recallers_upper_bound'
    FREQUENCY = 'frequency'
    FULL_VIEW_IMPRESSIONS = 'full_view_impressions'
    FULL_VIEW_REACH = 'full_view_reach'
    GENDER_TARGETING = 'gender_targeting'
    IMPRESSIONS = 'impressions'
    INLINE_LINK_CLICK_CTR = 'inline_link_click_ctr'
    INLINE_LINK_CLICKS = 'inline_link_clicks'
    INLINE_POST_ENGAGEMENT = 'inline_post_engagement'
    INSTANT_EXPERIENCE_CLICKS_TO_OPEN = 'instant_experience_clicks_to_open'
    INSTANT_EXPERIENCE_CLICKS_TO_START = 'instant_experience_clicks_to_start'
    INSTANT_EXPERIENCE_OUTBOUND_CLICKS = 'instant_experience_outbound_clicks'
    INTERACTIVE_COMPONENT_TAP = 'interactive_component_tap'
    LABELS = 'labels'
    LOCATION = 'location'
    MOBILE_APP_PURCHASE_ROAS = 'mobile_app_purchase_roas'
    OBJECTIVE = 'objective'
    OPTIMIZATION_GOAL = 'optimization_goal'
    OUTBOUND_CLICKS = 'outbound_clicks'
    OUTBOUND_CLICKS_CTR = 'outbound_clicks_ctr'
    PLACE_PAGE_NAME = 'place_page_name'
    PURCHASE_ROAS = 'purchase_roas'
    QUALIFYING_QUESTION_QUALIFY_ANSWER_RATE = 'qualifying_question_qualify_answer_rate'
    QUALITY_RANKING = 'quality_ranking'
    QUALITY_SCORE_ECTR = 'quality_score_ectr'
    QUALITY_SCORE_ECVR = 'quality_score_ecvr'
    QUALITY_SCORE_ORGANIC = 'quality_score_organic'
    REACH = 'reach'
    SOCIAL_SPEND = 'social_spend'
    SPEND = 'spend'
    TOTAL_POSTBACKS = 'total_postbacks'
    TOTAL_POSTBACKS_DETAILED = 'total_postbacks_detailed'
    UNIQUE_ACTIONS = 'unique_actions'
    UNIQUE_CLICKS = 'unique_clicks'
    UNIQUE_CONVERSIONS = 'unique_conversions'
    UNIQUE_CTR = 'unique_ctr'
    UNIQUE_INLINE_LINK_CLICK_CTR = 'unique_inline_link_click_ctr'
    UNIQUE_INLINE_LINK_CLICKS = 'unique_inline_link_clicks'
    UNIQUE_LINK_CLICKS_CTR = 'unique_link_clicks_ctr'
    UNIQUE_OUTBOUND_CLICKS = 'unique_outbound_clicks'
    UNIQUE_OUTBOUND_CLICKS_CTR = 'unique_outbound_clicks_ctr'
    UNIQUE_VIDEO_CONTINUOUS_2_SEC_WATCHED_ACTIONS = 'unique_video_continuous_2_sec_watched_actions'
    UNIQUE_VIDEO_VIEW_15_SEC = 'unique_video_view_15_sec'
    UPDATED_TIME = 'updated_time'
    VIDEO_15_SEC_WATCHED_ACTIONS = 'video_15_sec_watched_actions'
    VIDEO_30_SEC_WATCHED_ACTIONS = 'video_30_sec_watched_actions'
    VIDEO_AVG_TIME_WATCHED_ACTIONS = 'video_avg_time_watched_actions'
    VIDEO_CONTINUOUS_2_SEC_WATCHED_ACTIONS = 'video_continuous_2_sec_watched_actions'
    VIDEO_P100_WATCHED_ACTIONS = 'video_p100_watched_actions'
    VIDEO_P25_WATCHED_ACTIONS = 'video_p25_watched_actions'
    VIDEO_P50_WATCHED_ACTIONS = 'video_p50_watched_actions'
    VIDEO_P75_WATCHED_ACTIONS = 'video_p75_watched_actions'
    VIDEO_P95_WATCHED_ACTIONS = 'video_p95_watched_actions'
    VIDEO_PLAY_ACTIONS = 'video_play_actions'
    VIDEO_PLAY_CURVE_ACTIONS = 'video_play_curve_actions'
    VIDEO_PLAY_RETENTION_0_TO_15S_ACTIONS = 'video_play_retention_0_to_15s_actions'
    VIDEO_PLAY_RETENTION_20_TO_60S_ACTIONS = 'video_play_retention_20_to_60s_actions'
    VIDEO_PLAY_RETENTION_GRAPH_ACTIONS = 'video_play_retention_graph_actions'
    VIDEO_THRUPLAY_WATCHED_ACTIONS = 'video_thruplay_watched_actions'
    VIDEO_TIME_WATCHED_ACTIONS = 'video_time_watched_actions'
    WEBSITE_CTR = 'website_ctr'
    WEBSITE_PURCHASE_ROAS = 'website_purchase_roas'
    WISH_BID = 'wish_bid'

class SourceFacebookMarketingInsightConfigLevel(str, Enum):
    r"""Chosen level for API"""
    AD = 'ad'
    ADSET = 'adset'
    CAMPAIGN = 'campaign'
    ACCOUNT = 'account'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceFacebookMarketingInsightConfig:
    r"""Config for custom insights"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name value of insight"""
    action_breakdowns: Optional[list[SourceFacebookMarketingInsightConfigValidActionBreakdowns]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action_breakdowns'), 'exclude': lambda f: f is None }})
    r"""A list of chosen action_breakdowns for action_breakdowns"""
    breakdowns: Optional[list[SourceFacebookMarketingInsightConfigValidBreakdowns]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('breakdowns'), 'exclude': lambda f: f is None }})
    r"""A list of chosen breakdowns for breakdowns"""
    end_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date until which you'd like to replicate data for this stream, in the format YYYY-MM-DDT00:00:00Z. All data generated between the start date and this end date will be replicated. Not setting this option will result in always syncing the latest data."""
    fields_: Optional[list[SourceFacebookMarketingInsightConfigValidEnums]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fields'), 'exclude': lambda f: f is None }})
    r"""A list of chosen fields for fields parameter"""
    insights_lookback_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('insights_lookback_window'), 'exclude': lambda f: f is None }})
    r"""The attribution window"""
    level: Optional[SourceFacebookMarketingInsightConfigLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('level'), 'exclude': lambda f: f is None }})
    r"""Chosen level for API"""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date from which you'd like to replicate data for this stream, in the format YYYY-MM-DDT00:00:00Z."""
    time_increment: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time_increment'), 'exclude': lambda f: f is None }})
    r"""Time window in days by which to aggregate statistics. The sync will be chunked into N day intervals, where N is the number of days you specified. For example, if you set this value to 7, then all statistics will be reported as 7-day aggregates by starting from the start_date. If the start and end dates are October 1st and October 30th, then the connector will output 5 records: 01 - 06, 07 - 13, 14 - 20, 21 - 27, and 28 - 30 (3 days only)."""
    


class SourceFacebookMarketingFacebookMarketing(str, Enum):
    FACEBOOK_MARKETING = 'facebook-marketing'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceFacebookMarketing:
    r"""The values required to configure the source."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The value of the generated access token. From your App’s Dashboard, click on \\"Marketing API\\" then \\"Tools\\". Select permissions <b>ads_management, ads_read, read_insights, business_management</b>. Then click on \\"Get token\\". See the <a href=\\"https://docs.airbyte.com/integrations/sources/facebook-marketing\\">docs</a> for more information."""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The Facebook Ad account ID to use when pulling data from the Facebook Marketing API. Open your Meta Ads Manager. The Ad account ID number is in the account dropdown menu or in your browser's address bar. See the <a href=\\"https://www.facebook.com/business/help/1492627900875762\\">docs</a> for more information."""
    source_type: SourceFacebookMarketingFacebookMarketing = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date from which you'd like to replicate data for all incremental streams, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    action_breakdowns_allow_empty: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action_breakdowns_allow_empty'), 'exclude': lambda f: f is None }})
    r"""Allows action_breakdowns to be an empty list"""
    custom_insights: Optional[list[SourceFacebookMarketingInsightConfig]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_insights'), 'exclude': lambda f: f is None }})
    r"""A list which contains ad statistics entries, each entry must have a name and can contains fields, breakdowns or action_breakdowns. Click on \\"add\\" to fill this field."""
    end_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date until which you'd like to replicate data for all incremental streams, in the format YYYY-MM-DDT00:00:00Z. All data generated between the start date and this end date will be replicated. Not setting this option will result in always syncing the latest data."""
    fetch_thumbnail_images: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fetch_thumbnail_images'), 'exclude': lambda f: f is None }})
    r"""Set to active if you want to fetch the thumbnail_url and store the result in thumbnail_data_url for each Ad Creative."""
    include_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_deleted'), 'exclude': lambda f: f is None }})
    r"""Set to active if you want to include data from deleted Campaigns, Ads, and AdSets."""
    insights_lookback_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('insights_lookback_window'), 'exclude': lambda f: f is None }})
    r"""The attribution window. Facebook freezes insight data 28 days after it was generated, which means that all data from the past 28 days may have changed since we last emitted it, so you can retrieve refreshed insights from the past by setting this parameter. If you set a custom lookback window value in Facebook account, please provide the same value here."""
    max_batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_batch_size'), 'exclude': lambda f: f is None }})
    r"""Maximum batch size used when sending batch requests to Facebook API. Most users do not need to set this field unless they specifically need to tune the connector to address specific issues or use cases."""
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size'), 'exclude': lambda f: f is None }})
    r"""Page size used when sending requests to Facebook API to specify number of records per page when response has pagination. Most users do not need to set this field unless they specifically need to tune the connector to address specific issues or use cases."""
    

