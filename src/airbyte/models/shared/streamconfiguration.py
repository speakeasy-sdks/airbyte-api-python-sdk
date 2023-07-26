"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import connectionsyncmodeenum as shared_connectionsyncmodeenum
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StreamConfiguration:
    r"""Configurations for a single stream."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    cursor_field: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursorField'), 'exclude': lambda f: f is None }})
    r"""Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if `sync_mode` is `incremental` unless there is a default."""
    primary_key: Optional[list[list[str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryKey'), 'exclude': lambda f: f is None }})
    r"""Paths to the fields that will be used as primary key. This field is REQUIRED if `destination_sync_mode` is `*_dedup` unless it is already supplied by the source schema."""
    sync_mode: Optional[shared_connectionsyncmodeenum.ConnectionSyncModeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncMode'), 'exclude': lambda f: f is None }})
    

