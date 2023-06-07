"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceWhiskyHunterWhiskyHunter(str, Enum):
    WHISKY_HUNTER = 'whisky-hunter'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceWhiskyHunter:
    r"""The values required to configure the source."""
    
    source_type: Optional[SourceWhiskyHunterWhiskyHunter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    