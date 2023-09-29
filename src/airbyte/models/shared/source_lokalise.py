"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceLokalise:
    r"""The values required to configure the source."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Lokalise API Key with read-access. Available at Profile settings > API tokens. See <a href=\\"https://docs.lokalise.com/en/articles/1929556-api-tokens\\">here</a>."""
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    r"""Lokalise project ID. Available at Project Settings > General."""
    SOURCE_TYPE: Final[str] = dataclasses.field(default='lokalise', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

