import unittest
import os
from unittest.mock import patch

import oceandb
import oceandb.config


class GetDBTest(unittest.TestCase):
    @patch("oceandb.db.duckdb.DuckDB", autospec=True)
    def test_default_db(self, mock):
        oceandb.get_db(oceandb.config.Settings(persist_directory="./foo"))
        assert mock.called

    @patch("oceandb.db.duckdb.PersistentDuckDB", autospec=True)
    def test_persistent_duckdb(self, mock):
        oceandb.get_db(
            oceandb.config.Settings(
                ocean_db_impl="duckdb+parquet", persist_directory="./foo"
            )
        )
        assert mock.called

    @patch("oceandb.db.clickhouse.Clickhouse", autospec=True)
    def test_clickhouse(self, mock):
        oceandb.get_db(
            oceandb.config.Settings(
                ocean_db_impl="clickhouse",
                persist_directory="./foo",
                clickhouse_host="foo",
                clickhouse_port=666,
            )
        )
        assert mock.called


class GetAPITest(unittest.TestCase):
    @patch("oceandb.db.duckdb.DuckDB", autospec=True)
    @patch("oceandb.api.local.LocalAPI", autospec=True)
    @patch.dict(os.environ, {}, clear=True)
    def test_local(self, mock_api, mock_db):
        oceandb.Client(oceandb.config.Settings(persist_directory="./foo"))
        assert mock_api.called
        assert mock_db.called

    @patch("oceandb.api.fastapi.FastAPI", autospec=True)
    @patch.dict(os.environ, {}, clear=True)
    def test_fastapi(self, mock):
        oceandb.Client(
            oceandb.config.Settings(
                ocean_api_impl="rest",
                persist_directory="./foo",
                ocean_server_host="foo",
                ocean_server_http_port="80",
            )
        )
        assert mock.called
