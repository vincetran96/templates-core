"""File caching"""
from functools import wraps
from os import path


def filecache(func):
    """Decorator to check if a CSV file already exists and return the filepath;
    It expects the decorated function to have the `filepath` kwarg

    Args:
        func: A function that needs decoration

    Returns:
        Wrapped function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        filepath = kwargs['filepath']
        if path.isfile(filepath):
            return filepath
        return func(*args, **kwargs)
    return wrapper


@filecache
def fn():
    """Mock for a func that downloads data
    """
    return "Download new data"
