"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourcePexelsAPI:
    r"""The values required to configure the source."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API key is required to access pexels api, For getting your's goto https://www.pexels.com/api/documentation and create account for free."""
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    r"""Optional, the search query, Example Ocean, Tigers, Pears, etc."""
    SOURCE_TYPE: Final[str] = dataclasses.field(default='pexels-api', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    color: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('color'), 'exclude': lambda f: f is None }})
    r"""Optional, Desired photo color. Supported colors red, orange, yellow, green, turquoise, blue, violet, pink, brown, black, gray, white or any hexidecimal color code."""
    locale: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('locale'), 'exclude': lambda f: f is None }})
    r"""Optional, The locale of the search you are performing. The current supported locales are 'en-US' 'pt-BR' 'es-ES' 'ca-ES' 'de-DE' 'it-IT' 'fr-FR' 'sv-SE' 'id-ID' 'pl-PL' 'ja-JP' 'zh-TW' 'zh-CN' 'ko-KR' 'th-TH' 'nl-NL' 'hu-HU' 'vi-VN' 'cs-CZ' 'da-DK' 'fi-FI' 'uk-UA' 'el-GR' 'ro-RO' 'nb-NO' 'sk-SK' 'tr-TR' 'ru-RU'."""
    orientation: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orientation'), 'exclude': lambda f: f is None }})
    r"""Optional, Desired photo orientation. The current supported orientations are landscape, portrait or square"""
    size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    r"""Optional, Minimum photo size. The current supported sizes are large(24MP), medium(12MP) or small(4MP)."""
    

