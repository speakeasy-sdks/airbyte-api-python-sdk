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

class SourceTwitterTwitter(str, Enum):
    TWITTER = 'twitter'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceTwitter:
    r"""The values required to configure the source."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""App only Bearer Token. See the <a href=\\"https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens\\">docs</a> for more information on how to obtain this token."""
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    r"""Query for matching Tweets. You can learn how to build this query by reading <a href=\\"https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query\\"> build a query guide </a>."""
    source_type: SourceTwitterTwitter = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    end_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The end date for retrieving tweets must be a minimum of 10 seconds prior to the request time."""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The start date for retrieving tweets cannot be more than 7 days in the past."""
    

