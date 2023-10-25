'''Log-Structured Merge Tree

Some resources:
- https://dev.to/creativcoder/what-is-a-lsm-tree-3d75
- https://careers.coccoc.com/blogs/from-log-structured-merge-tree-storage-engine-to-a-toy-database
- https://github.com/wintdw/python-lsmtdb/blob/master/db.py
- https://www.youtube.com/watch?v=I6jB0nM9SKU
'''
import json
import logging
from pathlib import Path


logging.basicConfig(level=logging.DEBUG)
DBPATH = "temp/lsm"


class LSMTree():
    '''Implementation of LSMTree

    - Keys: str
    - Values: int
    '''
    def __init__(self, dbpath: str = DBPATH):
        '''Creates a LSMTree

        ---
        params
        ---
            - dbpath (str): Path to the db file
        '''
        self.memtable = {}
        self.dbpath = dbpath

        Path(self.dbpath).parent.mkdir(exist_ok=True, parents=True)
        Path(self.dbpath).touch(exist_ok=True)

    def set(self, key: str, value: int):
        '''Public method to set key
        '''
        self.memtable[key] = value

    def get(self, key: str):
        '''Public method to get key
        '''
        return self.memtable.get(key, None)

    def flush(self):
        '''Flushes the memtable to the db file
        '''
        with open(self.dbpath, "w", encoding="utf-8") as outfile:
            json.dump(self.memtable, outfile)


if __name__ == "__main__":
    t = LSMTree()
