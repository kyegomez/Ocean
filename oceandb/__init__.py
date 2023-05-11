import oceandb.config
import logging
from oceandb.telemetry.events import ClientStartEvent
from oceandb.telemetry.posthog import Posthog

logger = logging.getLogger(__name__)

__settings = oceandb.config.Settings()

__version__ = "0.3.22"


def configure(**kwargs):
    """Override Ocean's default settings, environment variables or .env files"""
    global __settings
    __settings = oceandb.config.Settings(**kwargs)


def get_settings():
    return __settings


def get_db(settings=__settings):
    """Return a ocean.DB instance based on the provided or environmental settings."""

    setting = settings.ocean_db_impl.lower()

    def require(key):
        assert settings[
            key
        ], f"Setting '{key}' is required when ocean_db_impl={setting}"

    if setting == "clickhouse":
        require("clickhouse_host")
        require("clickhouse_port")
        require("persist_directory")
        logger.info("Using Clickhouse for database")
        import oceandb.db.clickhouse

        return oceandb.db.clickhouse.Clickhouse(settings)
    elif setting == "duckdb+parquet":
        require("persist_directory")
        logger.warning(
            f"Using embedded DuckDB with persistence: data will be stored in: {settings.persist_directory}"
        )
        import oceandb.db.duckdb

        return oceandb.db.duckdb.PersistentDuckDB(settings)
    elif setting == "duckdb":
        require("persist_directory")
        logger.warning(
            "Using embedded DuckDB without persistence: data will be transient"
        )
        import oceandb.db.duckdb

        return oceandb.db.duckdb.DuckDB(settings)
    else:
        raise ValueError(
            f"Expected ocean_db_impl to be one of clickhouse, duckdb, duckdb+parquet, got {setting}"
        )


def Client(settings=__settings):
    """Return a ocean.API instance based on the provided or environmental
    settings, optionally overriding the DB instance."""

    setting = settings.ocean_api_impl.lower()
    telemetry_client = Posthog(settings)

    # Submit event for client start
    telemetry_client.capture(ClientStartEvent())

    def require(key):
        assert settings[
            key
        ], f"Setting '{key}' is required when ocean_api_impl={setting}"

    if setting == "rest":
        require("ocean_server_host")
        require("ocean_server_http_port")
        logger.info(
            "Running Ocean in client mode using REST to connect to remote server"
        )
        import oceandb.api.fastapi

        return oceandb.api.fastapi.FastAPI(settings, telemetry_client)
    elif setting == "local":
        logger.info("Running Ocean using direct local API.")
        import oceandb.api.local

        return oceandb.api.local.LocalAPI(settings, get_db(settings), telemetry_client)
    else:
        raise ValueError(
            f"Expected ocean_api_impl to be one of rest, local, got {setting}"
        )
