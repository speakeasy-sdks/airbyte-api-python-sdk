"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceAzureTableAzureTableEnum(str, Enum):
    AZURE_TABLE = 'azure-table'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAzureTable:
    r"""The values required to configure the source."""
    
    source_type: SourceAzureTableAzureTableEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    storage_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_access_key') }})
    r"""Azure Table Storage Access Key. See the <a href=\\"https://docs.airbyte.com/integrations/sources/azure-table\\">docs</a> for more information on how to obtain this key."""
    storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_account_name') }})
    r"""The name of your storage account."""
    storage_endpoint_suffix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_endpoint_suffix'), 'exclude': lambda f: f is None }})
    r"""Azure Table Storage service account URL suffix. See the <a href=\\"https://docs.airbyte.com/integrations/sources/azure-table\\">docs</a> for more information on how to obtain endpoint suffix"""
    