"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceConvex:
    r"""The values required to configure the source."""
    access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key') }})
    r"""API access key used to retrieve data from Convex."""
    deployment_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deployment_url') }})
    SOURCE_TYPE: Final[str] = dataclasses.field(default='convex', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

