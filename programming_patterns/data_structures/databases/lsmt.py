"""Log-Structured Merge Tree,
used in databases like ClickHouse

Some resources:
- https://dev.to/creativcoder/what-is-a-lsm-tree-3d75
- https://careers.coccoc.com/blogs/from-log-structured-merge-tree-storage-engine-to-a-toy-database
- https://github.com/wintdw/python-lsmtdb/blob/master/db.py
- https://www.youtube.com/watch?v=I6jB0nM9SKU
"""
import os
import json
import logging
from pathlib import Path
from pprint import pprint


logging.basicConfig(level=logging.DEBUG)
DBPATH = "temp/lsmt"


class LSMTree():
    """Implementation of LSMTree

    - Keys: str
    - Values: int
    """
    def __init__(self, dbpath: str = DBPATH):
        """Creates a LSMTree

        Args:
            dbpath: (str) Path to the db file
        """
        self.memtable = {}
        self.dbpath = dbpath
        self.dbfile = dbpath + "/db"
        self.jrnlfile = dbpath + "/journalfile"

        Path(self.dbpath).mkdir(exist_ok=True, parents=True)
        Path(self.dbfile).touch(exist_ok=True)
        Path(self.jrnlfile).touch(exist_ok=True)

    def set(self, key: str, value: int):
        """Public method to set key
        """
        self.memtable[key] = value

    def get(self, key: str):
        """Public method to get key
        """
        return self.memtable.get(key, None)

    def flush(self):
        """Flushes the memtable to the db file
        """
        with open(self.dbfile, "w", encoding="utf-8") as outfile:
            json.dump(self.memtable, outfile)

    def shutdown(self):
        """Shuts down
        """
        logging.debug("Event: Shutting down")
        self.flush()

    def startup(self):
        """Starts up by opening its existing dbfile

        Only loads the persisted file if its size > 0
        """
        logging.debug("Event: Starting up")
        if os.path.getsize(self.dbfile) > 0:
            with open(self.dbfile, "r", encoding="utf-8") as infile:
                data = json.load(infile)
                self.memtable = data

    def describe(self):
        """Describes itself
        """
        pprint(self.memtable)

    # For use as context manager
    def __enter__(self):
        self.startup()
        return self

    def __exit__(self, *_):
        self.shutdown()


if __name__ == "__main__":
    with LSMTree() as tree:
        tree.set('a', 1)
        tree.set('b', 2)
        tree.describe()
