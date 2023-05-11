from pydantic import BaseSettings
from typing import List

TELEMETRY_WHITELISTED_SETTINGS = [
    "ocean_db_impl",
    "ocean_api_impl",
    "ocean_server_ssl_enabled",
]


class Settings(BaseSettings):
    environment: str = ""

    ocean_db_impl: str = "duckdb"
    ocean_api_impl: str = "local"

    clickhouse_host: str = None # type: ignore
    clickhouse_port: str = None

    persist_directory: str = ".ocean"

    ocean_server_host: str = None
    ocean_server_http_port: str = None
    ocean_server_ssl_enabled: bool = False
    ocean_server_grpc_port: str = None
    ocean_server_cors_allow_origins: List[str] = []  # eg ["http://localhost:3000"]

    anonymized_telemetry: bool = True

    def __getitem__(self, item):
        return getattr(self, item)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
