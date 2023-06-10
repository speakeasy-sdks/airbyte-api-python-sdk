"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourcePocketContentType(str, Enum):
    r"""Select the content type of the items to retrieve."""
    ARTICLE = 'article'
    VIDEO = 'video'
    IMAGE = 'image'

class SourcePocketDetailType(str, Enum):
    r"""Select the granularity of the information about each item."""
    SIMPLE = 'simple'
    COMPLETE = 'complete'

class SourcePocketSortBy(str, Enum):
    r"""Sort retrieved items by the given criteria."""
    NEWEST = 'newest'
    OLDEST = 'oldest'
    TITLE = 'title'
    SITE = 'site'

class SourcePocketPocket(str, Enum):
    POCKET = 'pocket'

class SourcePocketState(str, Enum):
    r"""Select the state of the items to retrieve."""
    UNREAD = 'unread'
    ARCHIVE = 'archive'
    ALL = 'all'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourcePocket:
    r"""The values required to configure the source."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The user's Pocket access token."""
    consumer_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consumer_key') }})
    r"""Your application's Consumer Key."""
    source_type: SourcePocketPocket = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    content_type: Optional[SourcePocketContentType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content_type'), 'exclude': lambda f: f is None }})
    r"""Select the content type of the items to retrieve."""
    detail_type: Optional[SourcePocketDetailType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detail_type'), 'exclude': lambda f: f is None }})
    r"""Select the granularity of the information about each item."""
    domain: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain'), 'exclude': lambda f: f is None }})
    r"""Only return items from a particular `domain`."""
    favorite: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('favorite'), 'exclude': lambda f: f is None }})
    r"""Retrieve only favorited items."""
    search: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search'), 'exclude': lambda f: f is None }})
    r"""Only return items whose title or url contain the `search` string."""
    since: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('since'), 'exclude': lambda f: f is None }})
    r"""Only return items modified since the given timestamp."""
    sort: Optional[SourcePocketSortBy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sort'), 'exclude': lambda f: f is None }})
    r"""Sort retrieved items by the given criteria."""
    state: Optional[SourcePocketState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    r"""Select the state of the items to retrieve."""
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tag'), 'exclude': lambda f: f is None }})
    r"""Return only items tagged with this tag name. Use _untagged_ for retrieving only untagged items."""
    

