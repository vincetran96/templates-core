"""Unit tests
- builtin.IO
- call_args
- call_args_list
- pytest.raises
"""
from unittest.mock import patch, mock_open, call
from io import StringIO

import pandas as pd
import pytest

from services.some_service import (
    load_config,
    read_sql_file,
    check_quality
)


def test_load_config_file_not_found():
    """Test function load_config with invalid path
    """
    with pytest.raises(FileNotFoundError):
        load_config(path="fake_path", db="fake_db")


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="""
        clickhouse:
          check_1:
            'sql_path/check_1.sql'
          check_2:
            'sql_path/check_2.sql'
        """
)
def test_load_config(*_):
    """Test function load_config
    """
    with pytest.raises(KeyError):
        load_config(path="fake_path", db="fake_db")

    assert load_config(path="fake_path", db="clickhouse") == {
        "check_1": "sql_path/check_1.sql",
        "check_2": "sql_path/check_2.sql",
    }


def test_read_sql_file_file_not_found():
    """Test function read_sql_file with invalid path
    """
    with pytest.raises(FileNotFoundError):
        read_sql_file(path="fake_path", date="1970-01-01")


@patch(
    "builtins.open",
    side_effect=[
        StringIO("select * from table1 where 0;"),
        StringIO("select * from table1 where 0 and event_date = '{date}';")
    ]
)
def test_read_sql_file(*_):
    """Test function read_sql_file
    """
    assert read_sql_file(
        path="fake_path", date="1970-01-01"
    ) == "select * from table1 where 0;"

    assert read_sql_file(
        path="fake_path", date="1970-01-01"
    ) == "select * from table1 where 0 and event_date = '1970-01-01';"


@patch(
    "airflow.models.Variable.get",
    return_value="DMP_GRAFANA_ONCALL_URL"
)
@patch(
    "services.some_service.send_to_grafana_oncall"
)
@patch(
    "services.some_service.pd.read_sql",
    side_effect=[
        pd.DataFrame(),
        pd.DataFrame({'col': [0]})
    ]
)
@patch(
    "services.some_service.read_sql_file",
    side_effect=[
        "select * from table1 where 0;",
        "select * from table2 where 1;"
    ]
)
def test_check_quality(mock_read_sql_file, mock_pd_read_sql, mock_grafana, *_):
    """Test function check_quality
    """
    fake_config = {
        "check_1": "sql_path/check_1.sql",
        "check_2": "sql_path/check_2.sql",
    }
    check_quality(
        config=fake_config,
        con="fake_con",
        date="1970-01-01"
    )

    assert mock_read_sql_file.call_args_list == [
        call(path="sql_path/check_1.sql", date="1970-01-01"),
        call(path="sql_path/check_2.sql", date="1970-01-01")
    ]

    assert [call_args.kwargs["sql"] for call_args in mock_pd_read_sql.call_args_list] == [
        "select * from table1 where 0;",
        "select * from table2 where 1;"
    ]

    assert mock_grafana.call_args_list == [
        call(
            url="DMP_GRAFANA_ONCALL_URL", alert_name="check_2",
            message="select * from table2 where 1;", state="firing", cluster="Airflow"
        )
    ]
