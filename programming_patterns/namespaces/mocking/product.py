'''A sample product file to test for
'''
from os import listdir
from pathlib import Path


def list_current_dir():
    '''Lists all files in current dir
    '''
    files = listdir(Path(__file__).parent)
    return files
