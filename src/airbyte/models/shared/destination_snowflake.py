"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationSnowflakeCredentialsUsernameAndPasswordAuthTypeEnum(str, Enum):
    USERNAME_AND_PASSWORD = 'Username and Password'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCredentialsUsernameAndPassword:
    
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Enter the password associated with the username."""
    auth_type: Optional[DestinationSnowflakeCredentialsUsernameAndPasswordAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    
class DestinationSnowflakeCredentialsKeyPairAuthenticationAuthTypeEnum(str, Enum):
    KEY_PAIR_AUTHENTICATION = 'Key Pair Authentication'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCredentialsKeyPairAuthentication:
    
    private_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key') }})
    r"""RSA Private key to use for Snowflake connection. See the <a href=\\"https://docs.airbyte.com/integrations/destinations/snowflake\\">docs</a> for more information on how to obtain this key."""
    auth_type: Optional[DestinationSnowflakeCredentialsKeyPairAuthenticationAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    private_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key_password'), 'exclude': lambda f: f is None }})
    r"""Passphrase for private key"""
    
class DestinationSnowflakeCredentialsOAuth20AuthTypeEnum(str, Enum):
    O_AUTH2_0 = 'OAuth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCredentialsOAuth20:
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Enter you application's Access Token"""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Enter your application's Refresh Token"""
    auth_type: Optional[DestinationSnowflakeCredentialsOAuth20AuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Enter your application's Client ID"""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""Enter your application's Client secret"""
    
class DestinationSnowflakeSnowflakeEnum(str, Enum):
    SNOWFLAKE = 'snowflake'

class DestinationSnowflakeLoadingMethodAzureBlobStorageStagingMethodEnum(str, Enum):
    AZURE_BLOB_STAGING = 'Azure Blob Staging'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodAzureBlobStorageStaging:
    r"""Recommended for large production workloads for better speed and scalability."""
    
    azure_blob_storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_name') }})
    r"""Enter your Azure Blob Storage account name"""
    azure_blob_storage_container_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_container_name') }})
    r"""Enter your Azure Blob Storage <a href=\\"https://docs.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata#container-names\\">container name</a>"""
    azure_blob_storage_sas_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_sas_token') }})
    r"""Enter the <a href=\\"https://docs.snowflake.com/en/user-guide/data-load-azure-config.html#option-2-generating-a-sas-token\\">Shared access signature</a> (SAS) token to grant Snowflake limited access to objects in your Azure Blob Storage account"""
    method: DestinationSnowflakeLoadingMethodAzureBlobStorageStagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    azure_blob_storage_endpoint_domain_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_endpoint_domain_name'), 'exclude': lambda f: f is None }})
    r"""Enter the Azure Blob Storage <a href=\\"https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview#storage-account-endpoints\\">endpoint domain name</a>"""
    
class DestinationSnowflakeLoadingMethodGoogleCloudStorageStagingMethodEnum(str, Enum):
    GCS_STAGING = 'GCS Staging'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodGoogleCloudStorageStaging:
    r"""Recommended for large production workloads for better speed and scalability."""
    
    bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket_name') }})
    r"""Enter the <a href=\\"https://cloud.google.com/storage/docs/creating-buckets\\">Cloud Storage bucket name</a>"""
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    r"""Enter your <a href=\\"https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys\\">Google Cloud service account key</a> in the JSON format with read/write access to your Cloud Storage staging bucket"""
    method: DestinationSnowflakeLoadingMethodGoogleCloudStorageStagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    r"""Enter the <a href=\\"https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects\\">Google Cloud project ID</a>"""
    
class DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionAESCBCEnvelopeEncryptionEncryptionTypeEnum(str, Enum):
    AES_CBC_ENVELOPE = 'aes_cbc_envelope'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionAESCBCEnvelopeEncryption:
    r"""Staging data will be encrypted using AES-CBC envelope encryption."""
    
    encryption_type: DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionAESCBCEnvelopeEncryptionEncryptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_type') }})
    key_encrypting_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key_encrypting_key'), 'exclude': lambda f: f is None }})
    r"""The key, base64-encoded. Must be either 128, 192, or 256 bits. Leave blank to have Airbyte generate an ephemeral key for each sync."""
    
class DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionNoEncryptionEncryptionTypeEnum(str, Enum):
    NONE = 'none'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionNoEncryption:
    r"""Staging data will be stored in plaintext."""
    
    encryption_type: DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionNoEncryptionEncryptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_type') }})
    
class DestinationSnowflakeLoadingMethodAWSS3StagingMethodEnum(str, Enum):
    S3_STAGING = 'S3 Staging'

class DestinationSnowflakeLoadingMethodAWSS3StagingS3BucketRegionEnum(str, Enum):
    r"""Enter the region where your S3 bucket resides"""
    UNKNOWN = ''
    US_EAST_1 = 'us-east-1'
    US_EAST_2 = 'us-east-2'
    US_WEST_1 = 'us-west-1'
    US_WEST_2 = 'us-west-2'
    AF_SOUTH_1 = 'af-south-1'
    AP_EAST_1 = 'ap-east-1'
    AP_SOUTH_1 = 'ap-south-1'
    AP_NORTHEAST_1 = 'ap-northeast-1'
    AP_NORTHEAST_2 = 'ap-northeast-2'
    AP_NORTHEAST_3 = 'ap-northeast-3'
    AP_SOUTHEAST_1 = 'ap-southeast-1'
    AP_SOUTHEAST_2 = 'ap-southeast-2'
    CA_CENTRAL_1 = 'ca-central-1'
    CN_NORTH_1 = 'cn-north-1'
    CN_NORTHWEST_1 = 'cn-northwest-1'
    EU_CENTRAL_1 = 'eu-central-1'
    EU_WEST_1 = 'eu-west-1'
    EU_WEST_2 = 'eu-west-2'
    EU_WEST_3 = 'eu-west-3'
    EU_SOUTH_1 = 'eu-south-1'
    EU_NORTH_1 = 'eu-north-1'
    SA_EAST_1 = 'sa-east-1'
    ME_SOUTH_1 = 'me-south-1'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodAWSS3Staging:
    r"""Recommended for large production workloads for better speed and scalability."""
    
    access_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key_id') }})
    r"""Enter your <a href=\\"https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html\\">AWS access key ID</a>. Airbyte requires Read and Write permissions on your S3 bucket"""
    method: DestinationSnowflakeLoadingMethodAWSS3StagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    s3_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_name') }})
    r"""Enter your S3 bucket name"""
    secret_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_access_key') }})
    r"""Enter your <a href=\\"https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html\\">AWS secret access key</a>"""
    encryption: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    r"""Choose a data encryption method for the staging data"""
    file_name_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name_pattern'), 'exclude': lambda f: f is None }})
    r"""The pattern allows you to set the file-name format for the S3 staging file(s)"""
    purge_staging_data: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purge_staging_data'), 'exclude': lambda f: f is None }})
    r"""Toggle to delete staging files from the S3 bucket after a successful sync"""
    s3_bucket_region: Optional[DestinationSnowflakeLoadingMethodAWSS3StagingS3BucketRegionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region'), 'exclude': lambda f: f is None }})
    r"""Enter the region where your S3 bucket resides"""
    
class DestinationSnowflakeLoadingMethodRecommendedInternalStagingMethodEnum(str, Enum):
    INTERNAL_STAGING = 'Internal Staging'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodRecommendedInternalStaging:
    r"""Recommended for large production workloads for better speed and scalability."""
    
    method: DestinationSnowflakeLoadingMethodRecommendedInternalStagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    
class DestinationSnowflakeLoadingMethodSelectAnotherOptionMethodEnum(str, Enum):
    STANDARD = 'Standard'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodSelectAnotherOption:
    r"""Select another option"""
    
    method: DestinationSnowflakeLoadingMethodSelectAnotherOptionMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflake:
    r"""The values required to configure the destination."""
    
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Enter the name of the <a href=\\"https://docs.snowflake.com/en/sql-reference/ddl-database.html#database-schema-share-ddl\\">database</a> you want to sync data into"""
    destination_type: DestinationSnowflakeSnowflakeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Enter your Snowflake account's <a href=\\"https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#using-an-account-locator-as-an-identifier\\">locator</a> (in the format <account_locator>.<region>.<cloud>.snowflakecomputing.com)"""
    role: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""Enter the <a href=\\"https://docs.snowflake.com/en/user-guide/security-access-control-overview.html#roles\\">role</a> that you want to use to access Snowflake"""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    r"""Enter the name of the default <a href=\\"https://docs.snowflake.com/en/sql-reference/ddl-database.html#database-schema-share-ddl\\">schema</a>"""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Enter the name of the user you want to use to access the database"""
    warehouse: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warehouse') }})
    r"""Enter the name of the <a href=\\"https://docs.snowflake.com/en/user-guide/warehouses-overview.html#overview-of-warehouses\\">warehouse</a> that you want to sync data into"""
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    file_buffer_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_buffer_count'), 'exclude': lambda f: f is None }})
    r"""Number of file buffers allocated for writing data. Increasing this number is beneficial for connections using Change Data Capture (CDC) and up to the number of streams within a connection. Increasing the number of file buffers past the maximum number of streams has deteriorating effects"""
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Enter the additional properties to pass to the JDBC URL string when connecting to the database (formatted as key=value pairs separated by the symbol &). Example: key1=value1&key2=value2&key3=value3"""
    loading_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loading_method'), 'exclude': lambda f: f is None }})
    r"""Select a data staging method"""
    