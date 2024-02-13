"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class Recreation(str, Enum):
    RECREATION = 'recreation'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRecreation:
    apikey: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apikey') }})
    r"""API Key"""
    query_campsites: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query_campsites'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[Recreation] = dataclasses.field(default=Recreation.RECREATION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

