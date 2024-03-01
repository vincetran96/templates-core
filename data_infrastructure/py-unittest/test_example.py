"""Unit tests
- builtin.IO
- call_args_list
- mock_calls
- pytest.raises
- context manager (__enter__)
"""
from unittest.mock import patch, call
from io import StringIO

import pytest

from services.some_service import (
    load_config,
    read_sql_file,
    insert_test_data
)


def test_load_config_file_not_found():
    """Test function load_config with invalid path
    """
    with pytest.raises(FileNotFoundError):
        load_config(path="fake_path")


@patch(
    "builtins.open",
    side_effect=[
        StringIO("""
            fake_key:
              example_test: 'services/some_service/sql/example_test.sql'"""),
        StringIO("""
            tests:
              example_test: 'services/some_service/sql/example_test.sql'"""),
    ]
)
def test_load_config(*_):
    """Test function load_config
    """
    with pytest.raises(KeyError):
        load_config(path="fake_path")

    assert load_config(path="fake_path") == {
        "example_test": "services/some_service/sql/example_test.sql"
    }


def test_read_sql_file_file_not_found():
    """Test function read_sql_file with invalid path
    """
    with pytest.raises(FileNotFoundError):
        read_sql_file(path="fake_path", test_name="fake_test", date="1970-01-01")


@patch(
    "builtins.open",
    side_effect=[
        StringIO("select 1;"),
        StringIO("select '{date}', '{test_name}';")
    ]
)
def test_read_sql_file(*_):
    """Test function read_sql_file
    """
    assert read_sql_file(
        path="fake_path", test_name="fake_test", date="1970-01-01"
    ) == "select 1;"

    assert read_sql_file(
        path="fake_path", test_name="fake_test", date="1970-01-01"
    ) == "select '1970-01-01', 'fake_test';"


@patch(
    "services.some_service.some_service.create_conn"
)
@patch(
    "services.some_service.some_service.read_sql_file",
    return_value="select 1;"
)
def test_insert_test_data(mock_read_sql_file, mock_conn, *_):
    """Test function insert_test_data
    """
    insert_test_data(
        sql_path="fake_path",
        test_name="fake_test",
        date="1970-01-01"
    )

    assert mock_read_sql_file.call_args_list == [
        call(path="fake_path", test_name="fake_test", date="1970-01-01")
    ]

    conn_context = mock_conn.return_value.__enter__.return_value
    mock_query = """INSERT INTO ab_testing.ab_tests (
    event_date,
    test_name,
    start_date,
    end_date,
    metric,
    test_group,
    dimension_1,
    dimension_2,
    dimension_3,
    value
    )
    select 1;"""
    assert conn_context.mock_calls == [
        call.execute(query=mock_query)
    ]
