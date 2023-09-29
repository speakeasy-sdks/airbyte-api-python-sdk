"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final, Optional, Union



@dataclasses.dataclass
class DestinationPostgresSSLModes:
    pass



@dataclasses.dataclass
class DestinationPostgresSSHTunnelMethod:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationPostgres:
    r"""The values required to configure the destination."""
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Name of the database."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Hostname of the database."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to use to access the database."""
    DESTINATION_TYPE: Final[str] = dataclasses.field(default='postgres', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3)."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password associated with the username."""
    port: Optional[int] = dataclasses.field(default=5432, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""Port of the database."""
    schema: Optional[str] = dataclasses.field(default='public', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""The default schema tables are written to if the source does not specify a namespace. The usual value for this field is \\"public\\"."""
    ssl_mode: Optional[Union[]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_mode') }})
    r"""SSL connection modes.
     <b>disable</b> - Chose this mode to disable encryption of communication between Airbyte and destination database
     <b>allow</b> - Chose this mode to enable encryption only when required by the source database
     <b>prefer</b> - Chose this mode to allow unencrypted connection only if the source database does not support encryption
     <b>require</b> - Chose this mode to always require encryption. If the source database server does not support encryption, connection will fail
      <b>verify-ca</b> - Chose this mode to always require encryption and to verify that the source database server has a valid SSL certificate
      <b>verify-full</b> - This is the most secure mode. Chose this mode to always require encryption and to verify the identity of the source database server
     See more information - <a href=\"https://jdbc.postgresql.org/documentation/head/ssl-client.html\"> in the docs</a>.
    """
    tunnel_method: Optional[Union[]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    

