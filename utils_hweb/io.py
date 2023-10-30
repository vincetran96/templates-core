"""IO utils
"""
import sys
import os
import time
import random
import shutil
import asyncio
from pathlib import Path
from urllib.parse import urlparse
from typing import Union, Iterable, Hashable

import httpx
import requests
from requests import Response
from bs4 import BeautifulSoup as bsoup

from utils.configs import WRITE_CHUNKSIZE, READ_CHUNKSIZE
from utils.misc import flatten_list
from utils.ext.bolton_fileutils import atomic_save


CPU_COUNT = os.cpu_count()

def is_iterable(var):
    try:
        iter(var)
        return True
    except TypeError:
        return False

def read_stdin_batch(batch_size: int=10000):
    """Reads stdin in batches of lines

    Returns a generator of list of strings
    """
    i = 0
    line_arr = []
    while True:
        line = sys.stdin.readline()
        if i == batch_size:
            yield line_arr
            i = 0
            line_arr = []
        elif not line:
            yield line_arr
            break
        line_arr.append(line)
        i += 1

def read_text_batch(path: Union[str,Path,Iterable], batch_size: int=10000):
    """Reads content of a text file in batches of lines

    Returns a generator of list of strings

    ---
    :params:
    ---
        - path: str - full path to the text file OR iterable - file paths
    """
    line_generator = readline_files(path)
    line_arr = []
    while True:
        for _ in range(batch_size):
            try:
                line = next(line_generator)
                line_arr.append(line)
            except StopIteration:
                break
        if not line_arr:
            break
        yield line_arr
        line_arr = []

def readline_files(
    path: Union[str,Path,Iterable], separator: str=None, encoding: str="utf-8"
):
    """Reads lines from multiple text files or a text file
    
    Returns a generator of strings, or of tuples of strings if seperator is provided;
    Please note that among the fields yielded, only the last field contains
    the newline character

    ---
    :params:
    ---
        - path: str - full path to the text file OR iterable - file paths
        - separator: str - field separator of the file
    """
    if separator and not isinstance(separator, str):
        raise TypeError("Separator must be string")
    
    yield_value = lambda x: x.split(separator) if separator else x
    
    if isinstance(path, str) or isinstance(path, Path):
        with open(path, 'r', encoding=encoding) as infile:
            for line in infile:
                yield yield_value(line)
    elif is_iterable(path):
        for file in path:
            with open(file, 'r', encoding=encoding) as infile:
                for line in infile:
                    yield yield_value(line)
    else:
        raise ValueError("Please check the value of `path`")
    
def readlines_file(
    path: Union[str,Path], n_shuff: int=None,
    seed: Hashable=None, encoding: str="utf-8"
):
    """Reads all lines from a text file; You can optionally only
    read a random set of `n_shuff` lines

    Returns a list of lines

    ---
    :params:
    ---
        - seed: Hashable - seed for the random generator
    """
    with open(path, 'r', encoding=encoding) as infile:
        lines = infile.readlines()
        if n_shuff:
            random.seed(seed)
            lines_out = random.sample(lines, min(n_shuff, len(lines)))
        else:
            lines_out = lines
        return lines_out

def write_text_data(
    path, mode,
    data: str, encoding="utf-8",
    chunksize: int=None, overwrite: bool=False
):
    """Writes text data to a file

    Mode must be = a if want to write in chunks

    Will raise a FileExist exception if writing in chunks and the file path exists

    ---
    :params:
    ---
        - chunksize: a chunk in bytes
    """
    ppath = Path(path)
    ppath.parent.mkdir(parents=True, exist_ok=True)
    if chunksize:
        with atomic_save(str(path), text_mode=True, overwrite=overwrite) as outfile:
            for i in range(0, len(data), chunksize):
                outfile.write(data[i:i+chunksize])
    else:
        with atomic_save(str(path), text_mode=True, overwrite=overwrite) as outfile:
            outfile.write(data)
    # print(f"Wrote data to: {path}")

def write_response_data(
    path: Union[str,Path],
    mode: str,
    response: Response, encoding="utf-8",
    chunksize: int=READ_CHUNKSIZE, overwrite: bool=False
):
    """Writes a Requests **text** response data to a file

    Default is to write in chunks; Mode must be = a if write in chunks

    Will raise a FileExist exception if writing in chunks and the file path exists

    ---
    :params:
    ---
        - encoding: str - encoding of the response object
    """
    response.encoding = encoding

    # It's OK to wrap Path() around a Path object as it returns the same path
    ppath = Path(path)
    ppath.parent.mkdir(parents=True, exist_ok=True)

    if chunksize:
        with atomic_save(str(path), text_mode=True, overwrite=overwrite) as outfile:
            for chunk in response.iter_content(chunk_size=chunksize, decode_unicode=True):
                outfile.write(chunk)
    else:
        with atomic_save(str(path), text_mode=True, overwrite=overwrite) as outfile:
            outfile.write(response.text)
    # print(f"Wrote data to: {path}")

def write_list_data(path: Union[str,Path], data: list, overwrite: bool=False):
    """Writes a list of strings to a file
    """
    ppath = Path(path)
    ppath.parent.mkdir(parents=True, exist_ok=True)
    with atomic_save(str(path), text_mode=True, overwrite=overwrite) as outfile:
        for string_ in data:
            outfile.write(string_)

def file_time_comp(expire_time: int):
    """Returns a string representing the time component
    to attach to a filename;

    It simply divides the current time in epoch seconds by the `expire_time`,
    to get an integer indicating if the file is "expired"
    """
    return str(int(time.time()/expire_time))

def filesize(path: Union[str,Path]):
    """Returns the file size in bytes

    Will raise an exception if the file does not exist
    """
    ppath = Path(path)
    return ppath.stat().st_size

def copy_files(source_paths: Iterable, dest_path: Union[str,Path]):
    """Copies source files to destination

    Returns the destination path
    """
    source_paths = flatten_list(source_paths)
    Path(dest_path).mkdir(parents=True, exist_ok=True)
    for source in source_paths:
        shutil.copy(source, dest_path)

    return dest_path

def list_files_dir(dir: Union[str,Path], rglob_patt: str="*"):
    """Lists files in directory
    
    ---
    :params:
    ---
        - rglob_patt: pattern for file
    """
    dir = Path(dir)
    return dir.rglob(rglob_patt)

def remove_allFiles_dir(dir: Union[str,Path]):
    """Removes all files from dir
    """
    dir = Path(dir)
    for path in dir.rglob("*"):
        if path.is_file():
            path.unlink()

async def download_file_url(
    url, dest: Union[str,Path], overwrite: bool=True
):
    """Async downloads file from url

    Returns the full path to the file
    
    ---
    :params:
    ---
        - dest: Destination
        - overwrite: bool - whether to overwrite the file if it exists in dest
    """
    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        if resp.status_code == 200:
            filename = Path(urlparse(url).path).name
            outpath = dest / filename
            with atomic_save(str(outpath), text_mode=False, overwrite=overwrite) as outfile:
                outfile.write(resp.content)
    
    print(f"Saved file to {outpath}")
    return outpath

async def download_files_url(
    urls: list, dest: Union[str,Path], overwrite: bool=True, timeout: int=7200
):
    """Async downloads files from urls

    Returns the dest

    ---
    :params:
    ---
        - dest: Destination
        - overwrite: bool - whether to overwrite the file if it exists in dest
        - timeout: int - timeout to wait for the download tasks (default 2 hours)
    """
    dest = Path(dest)

    # task_arr = [ raiser(x) for x in range(10) ]
    # aDone, aPending = await asyncio.wait(*task_arr, return_when=asyncio.FIRST_EXCEPTION)

    try:
        task_arr = [
            asyncio.create_task(download_file_url(url, dest, overwrite)) for url in urls
        ]
        _, aPending = await asyncio.wait(
            task_arr, timeout=timeout, return_when=asyncio.FIRST_EXCEPTION
        )
        if len(aPending) > 0:
            for p in aPending:
                p.cancel()
            raise TimeoutError("Task timed out")
    except Exception as exc:        
        remove_allFiles_dir(dest)
        raise exc

    return dest

def get_filelinks_url(url: str, fullpath: bool=True):
    """Gets file links from an URL

    Setting fullpath = False has not been tested

    ---
    :params:
    ---
        - fullpath: bool - whether to get the full path to each file
    """
    resp = requests.get(url)
    resp.raise_for_status()
    if resp.status_code == 200:
        parsed_url = urlparse(url)
        soup = bsoup(resp.content, "html.parser")
        protocol = parsed_url.scheme
        domain = ""
        if fullpath:
            domain = parsed_url.netloc
        filelinks = [
            f"{protocol}://{domain}{link.get('href')}" for link in soup.find_all('a')
        ]
        return filelinks

def file_exists(filepath: Union[str,Path]):
    """Checks if a file exists
    """
    return Path(filepath).is_file()

def files_exist(filepaths: Iterable[Union[str,Path]]):
    """Checks for the existence of multiple files
    """
    for filepath in filepaths:
        if not file_exists(filepath):
            return False
    return True
