"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceTvmazeScheduleTvmazeSchedule(str, Enum):
    TVMAZE_SCHEDULE = 'tvmaze-schedule'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceTvmazeSchedule:
    r"""The values required to configure the source."""
    domestic_schedule_country_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domestic_schedule_country_code') }})
    r"""Country code for domestic TV schedule retrieval."""
    source_type: SourceTvmazeScheduleTvmazeSchedule = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""Start date for TV schedule retrieval. May be in the future."""
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    r"""End date for TV schedule retrieval. May be in the future. Optional."""
    web_schedule_country_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('web_schedule_country_code'), 'exclude': lambda f: f is None }})
    r"""ISO 3166-1 country code for web TV schedule retrieval. Leave blank for
    all countries plus global web channels (e.g. Netflix). Alternatively,
    set to 'global' for just global web channels.
    """
    

