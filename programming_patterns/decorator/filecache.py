"""File caching"""
import logging
from functools import wraps
from typing import Callable
from os import path, makedirs


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


def dataframe_cache(location: str):
    """Decorator to check if a CSV file already exists and return
    a DataFrame from the file;

    ```
    dataframe_cache('zxc') == decorator
    dataframe_cache('zxc')(somefunc) == decorator(somefunc) == wrapper = new_def_func
    new_def_func(args, kwargs) == wrapper(args, kwargs)
    ```

    Args:
        location(str): Directory to the cached file

    Returns:
        DataFrame
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            parentpath = path.join("root", location)
            filepath = path.join(parentpath, args[0])
            if path.isfile(filepath):
                logging.info(f"Data already cached at: {filepath}")
                return pd.read_csv(filepath, compression='gzip', sep="\t")
            makedirs(location, exist_ok=True)
            data = func(*args, **kwargs)
            data.to_csv(filepath, compression='gzip', sep="\t", index=False)
            return data
        return wrapper
    return decorator


@filecache
def fn():
    """Mock for a func that downloads data
    """
    return "Download new data"
