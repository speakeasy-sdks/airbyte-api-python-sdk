"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final, Optional, Union



@dataclasses.dataclass
class DestinationDatabricksDataSource:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationDatabricks:
    r"""The values required to configure the destination."""
    data_source: Optional[Union[]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_source') }})
    r"""Storage on which the delta lake is built."""
    databricks_http_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_http_path') }})
    r"""Databricks Cluster HTTP Path."""
    databricks_personal_access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_personal_access_token') }})
    r"""Databricks Personal Access Token for making authenticated requests."""
    databricks_server_hostname: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_server_hostname') }})
    r"""Databricks Cluster Server Hostname."""
    DESTINATION_TYPE: Final[str] = dataclasses.field(default='databricks', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    accept_terms: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accept_terms'), 'exclude': lambda f: f is None }})
    r"""You must agree to the Databricks JDBC Driver <a href=\\"https://databricks.com/jdbc-odbc-driver-license\\">Terms & Conditions</a> to use this connector."""
    database: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database'), 'exclude': lambda f: f is None }})
    r"""The name of the catalog. If not specified otherwise, the \\"hive_metastore\\" will be used."""
    databricks_port: Optional[str] = dataclasses.field(default='443', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_port'), 'exclude': lambda f: f is None }})
    r"""Databricks Cluster Port."""
    enable_schema_evolution: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable_schema_evolution'), 'exclude': lambda f: f is None }})
    r"""Support schema evolution for all streams. If \\"false\\", the connector might fail when a stream's schema changes."""
    purge_staging_data: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purge_staging_data'), 'exclude': lambda f: f is None }})
    r"""Default to 'true'. Switch it to 'false' for debugging purpose."""
    schema: Optional[str] = dataclasses.field(default='default', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""The default schema tables are written. If not specified otherwise, the \\"default\\" will be used."""
    

