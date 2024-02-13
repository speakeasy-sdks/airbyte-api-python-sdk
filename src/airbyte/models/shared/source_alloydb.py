"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Dict, Final, List, Optional, Union

class SourceAlloydbSchemasReplicationMethodMethod(str, Enum):
    STANDARD = 'Standard'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydbStandard:
    r"""Standard replication requires no setup on the DB side but will not be able to represent deletions incrementally."""
    METHOD: Final[SourceAlloydbSchemasReplicationMethodMethod] = dataclasses.field(default=SourceAlloydbSchemasReplicationMethodMethod.STANDARD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    


class LSNCommitBehaviour(str, Enum):
    r"""Determines when Airbtye should flush the LSN of processed WAL logs in the source database. `After loading Data in the destination` is default. If `While reading Data` is selected, in case of a downstream failure (while loading data into the destination), next sync would result in a full sync."""
    WHILE_READING_DATA = 'While reading Data'
    AFTER_LOADING_DATA_IN_THE_DESTINATION = 'After loading Data in the destination'

class SourceAlloydbSchemasMethod(str, Enum):
    CDC = 'CDC'

class Plugin(str, Enum):
    r"""A logical decoding plugin installed on the PostgreSQL server."""
    PGOUTPUT = 'pgoutput'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LogicalReplicationCDC:
    r"""Logical replication uses the Postgres write-ahead log (WAL) to detect inserts, updates, and deletes. This needs to be configured on the source database itself. Only available on Postgres 10 and above. Read the <a href=\\"https://docs.airbyte.com/integrations/sources/postgres\\">docs</a>."""
    UNSET='__SPEAKEASY_UNSET__'
    publication: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('publication') }})
    r"""A Postgres publication used for consuming changes. Read about <a href=\\"https://docs.airbyte.com/integrations/sources/postgres#step-4-create-publications-and-replication-identities-for-tables\\">publications and replication identities</a>."""
    replication_slot: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_slot') }})
    r"""A plugin logical replication slot. Read about <a href=\\"https://docs.airbyte.com/integrations/sources/postgres#step-3-create-replication-slot\\">replication slots</a>."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    initial_waiting_seconds: Optional[int] = dataclasses.field(default=300, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initial_waiting_seconds'), 'exclude': lambda f: f is None }})
    r"""The amount of time the connector will wait when it launches to determine if there is new data to sync or not. Defaults to 300 seconds. Valid range: 120 seconds to 1200 seconds. Read about <a href=\\"https://docs.airbyte.com/integrations/sources/postgres#step-5-optional-set-up-initial-waiting-time\\">initial waiting time</a>."""
    lsn_commit_behaviour: Optional[LSNCommitBehaviour] = dataclasses.field(default=LSNCommitBehaviour.AFTER_LOADING_DATA_IN_THE_DESTINATION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lsn_commit_behaviour'), 'exclude': lambda f: f is None }})
    r"""Determines when Airbtye should flush the LSN of processed WAL logs in the source database. `After loading Data in the destination` is default. If `While reading Data` is selected, in case of a downstream failure (while loading data into the destination), next sync would result in a full sync."""
    METHOD: Final[SourceAlloydbSchemasMethod] = dataclasses.field(default=SourceAlloydbSchemasMethod.CDC, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    plugin: Optional[Plugin] = dataclasses.field(default=Plugin.PGOUTPUT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plugin'), 'exclude': lambda f: f is None }})
    r"""A logical decoding plugin installed on the PostgreSQL server."""
    queue_size: Optional[int] = dataclasses.field(default=10000, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('queue_size'), 'exclude': lambda f: f is None }})
    r"""The size of the internal queue. This may interfere with memory consumption and efficiency of the connector, please be careful."""
    


class SourceAlloydbMethod(str, Enum):
    XMIN = 'Xmin'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StandardXmin:
    r"""Xmin replication requires no setup on the DB side but will not be able to represent deletions incrementally."""
    METHOD: Final[SourceAlloydbMethod] = dataclasses.field(default=SourceAlloydbMethod.XMIN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    


class Alloydb(str, Enum):
    ALLOYDB = 'alloydb'

class SourceAlloydbSchemasSSLModeSSLModes6Mode(str, Enum):
    VERIFY_FULL = 'verify-full'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydbVerifyFull:
    r"""This is the most secure mode. Always require encryption and verifies the identity of the source database server."""
    UNSET='__SPEAKEASY_UNSET__'
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})
    r"""CA certificate"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    client_certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_certificate'), 'exclude': lambda f: f is None }})
    r"""Client certificate"""
    client_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key'), 'exclude': lambda f: f is None }})
    r"""Client key"""
    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})
    r"""Password for keystorage. If you do not add it - the password will be generated automatically."""
    MODE: Final[SourceAlloydbSchemasSSLModeSSLModes6Mode] = dataclasses.field(default=SourceAlloydbSchemasSSLModeSSLModes6Mode.VERIFY_FULL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    


class SourceAlloydbSchemasSSLModeSSLModes5Mode(str, Enum):
    VERIFY_CA = 'verify-ca'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydbVerifyCa:
    r"""Always require encryption and verifies that the source database server has a valid SSL certificate."""
    UNSET='__SPEAKEASY_UNSET__'
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})
    r"""CA certificate"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    client_certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_certificate'), 'exclude': lambda f: f is None }})
    r"""Client certificate"""
    client_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key'), 'exclude': lambda f: f is None }})
    r"""Client key"""
    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})
    r"""Password for keystorage. If you do not add it - the password will be generated automatically."""
    MODE: Final[SourceAlloydbSchemasSSLModeSSLModes5Mode] = dataclasses.field(default=SourceAlloydbSchemasSSLModeSSLModes5Mode.VERIFY_CA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    


class SourceAlloydbSchemasSSLModeSSLModesMode(str, Enum):
    REQUIRE = 'require'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydbRequire:
    r"""Always require encryption. If the source database server does not support encryption, connection will fail."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    MODE: Final[SourceAlloydbSchemasSSLModeSSLModesMode] = dataclasses.field(default=SourceAlloydbSchemasSSLModeSSLModesMode.REQUIRE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    


class SourceAlloydbSchemasSslModeMode(str, Enum):
    PREFER = 'prefer'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydbPrefer:
    r"""Allows unencrypted connection only if the source database does not support encryption."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    MODE: Final[SourceAlloydbSchemasSslModeMode] = dataclasses.field(default=SourceAlloydbSchemasSslModeMode.PREFER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    


class SourceAlloydbSchemasMode(str, Enum):
    ALLOW = 'allow'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydbAllow:
    r"""Enables encryption only when required by the source database."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    MODE: Final[SourceAlloydbSchemasMode] = dataclasses.field(default=SourceAlloydbSchemasMode.ALLOW, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    


class SourceAlloydbMode(str, Enum):
    DISABLE = 'disable'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydbDisable:
    r"""Disables encryption of communication between Airbyte and source database."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    MODE: Final[SourceAlloydbMode] = dataclasses.field(default=SourceAlloydbMode.DISABLE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    


class SourceAlloydbSchemasTunnelMethodTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydbPasswordAuthentication:
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    TUNNEL_METHOD: Final[SourceAlloydbSchemasTunnelMethodTunnelMethod] = dataclasses.field(default=SourceAlloydbSchemasTunnelMethodTunnelMethod.SSH_PASSWORD_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    


class SourceAlloydbSchemasTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydbSSHKeyAuthentication:
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    TUNNEL_METHOD: Final[SourceAlloydbSchemasTunnelMethod] = dataclasses.field(default=SourceAlloydbSchemasTunnelMethod.SSH_KEY_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    


class SourceAlloydbTunnelMethod(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydbNoTunnel:
    TUNNEL_METHOD: Final[SourceAlloydbTunnelMethod] = dataclasses.field(default=SourceAlloydbTunnelMethod.NO_TUNNEL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAlloydb:
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Name of the database."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Hostname of the database."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to access the database."""
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (Eg. key1=value1&key2=value2&key3=value3). For more information read about <a href=\\"https://jdbc.postgresql.org/documentation/head/connect.html\\">JDBC URL parameters</a>."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password associated with the username."""
    port: Optional[int] = dataclasses.field(default=5432, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""Port of the database."""
    replication_method: Optional[Union[StandardXmin, LogicalReplicationCDC, SourceAlloydbStandard]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_method'), 'exclude': lambda f: f is None }})
    r"""Replication method for extracting data from the database."""
    schemas: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemas'), 'exclude': lambda f: f is None }})
    r"""The list of schemas (case sensitive) to sync from. Defaults to public."""
    SOURCE_TYPE: Final[Alloydb] = dataclasses.field(default=Alloydb.ALLOYDB, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    ssl_mode: Optional[Union[SourceAlloydbDisable, SourceAlloydbAllow, SourceAlloydbPrefer, SourceAlloydbRequire, SourceAlloydbVerifyCa, SourceAlloydbVerifyFull]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_mode'), 'exclude': lambda f: f is None }})
    r"""SSL connection modes.
      Read more <a href=\"https://jdbc.postgresql.org/documentation/head/ssl-client.html\"> in the docs</a>.
    """
    tunnel_method: Optional[Union[SourceAlloydbNoTunnel, SourceAlloydbSSHKeyAuthentication, SourceAlloydbPasswordAuthentication]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    

