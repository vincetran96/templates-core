'''Tests for product module

There are 2 versions of testing the list_current_dir function,
one of which will fail because we did not patch the to-patch
object where it is used
'''
from unittest.mock import patch

from programming_patterns.namespaces.mocking.product import list_current_dir


@patch(
    "os.listdir",
    return_value=["a.txt", "b.txt"]
)
def test_list_current_dir(mock_func, *_):
    '''Tests list_current_dir
    '''
    assert list_current_dir() == mock_func.return_value


@patch(
    "programming_patterns.namespaces.mocking.product.listdir",
    return_value=["a.txt", "b.txt"]
)
def test_list_current_dir_1(mock_func, *_):
    '''Tests list_current_dir

    Note in here that we mock the function where IT IS USED
    '''
    assert list_current_dir() == mock_func.return_value
