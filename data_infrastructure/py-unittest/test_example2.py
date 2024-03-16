"""Unit tests
- filepath operations
- mock attribute of variable inside function
"""
from unittest.mock import patch, call

import pandas as pd
import pytest

from services.some_service import (
    filecache, get_data
)


@patch(
    "services.some_service.pd.read_csv",
    return_value=pd.DataFrame({'a': [1], 'b': [2]})
)
@patch(
    "services.some_service.path.isfile",
    side_effect=[True, False]
)
def test_filecache(*_):
    """Test function filecache
    """
    with pytest.raises(KeyError):
        @filecache
        def func(): pass
        func()

    @filecache
    def func_1(filepath: str) -> pd.DataFrame:
        return pd.DataFrame({'c': [3], 'd': [4]})

    assert func_1(filepath="fake_path").equals(pd.DataFrame({'a': [1], 'b': [2]}))
    assert func_1(filepath="fake_path").equals(pd.DataFrame({'c': [3], 'd': [4]}))


@patch("services.some_service.dmp_clickhouse_ro")
@patch(
    "services.some_service.pd.read_csv",
    return_value=pd.DataFrame({'a': [1], 'b': [2]})
)
@patch(
    "services.some_service.path.isfile",
    side_effect=[True, False]
)
@patch(
    "services.some_service.pd.read_sql",
    return_value=pd.DataFrame()
)
@patch(
    "services.some_service.makedirs"
)
def test_get_data(mock_makedirs, mock_read_sql, *_):
    """Test function get_data
    """
    assert get_data(filepath="fake_path", query="fake_query").equals(pd.DataFrame({'a': [1], 'b': [2]}))

    with patch.object(mock_read_sql.return_value, attribute="to_csv") as mock_to_csv:
        get_data(filepath="parent/fake_file", query="fake_query")
        assert mock_makedirs.call_args_list == [call("parent", exist_ok=True)]
        assert mock_to_csv.call_args_list == [call("parent/fake_file", compression='gzip', index=False)]
