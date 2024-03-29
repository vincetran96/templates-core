"""Tests performance of pandas Series vs Python lists
with regards to string filtering
"""
import timeit
from pprint import pprint


TEST_TIMES = 100
RESULTS = {}

SETUP = """
import random
import string
import timeit

import pandas as pd

def random_substr(st: str):
    start = random.randint(0, len(st) - 1)
    end = random.randint(start + 1, len(st))
    return st[start:end]

def process(line):
    return "e" in line.st

base_st = string.ascii_lowercase
st_arr = [random_substr(base_st) for _ in range(999999)]
pd_series = pd.Series(st_arr)
pd_df = pd.DataFrame({"st": st_arr})
"""

stmt_series = """
pd_series_filtered = pd_series[pd_series.str.contains("e")]
"""

stmt_list = """
st_arr_filtered = [st for st in st_arr if "e" in st]
"""

stmt_df = """
pd_df['filter'] = [process(line) for line in pd_df.itertuples()]
pd_df_filtered = pd_df[pd_df['filter']]['st'].values.tolist()
"""


if __name__ == "__main__":
    RESULTS['pd_series'] = timeit.timeit(
        setup=SETUP,
        stmt=stmt_series,
        number=TEST_TIMES
    )
    RESULTS['list'] = timeit.timeit(
        setup=SETUP,
        stmt=stmt_list,
        number=TEST_TIMES
    )
    RESULTS['pd_df'] = timeit.timeit(
        setup=SETUP,
        stmt=stmt_df,
        number=TEST_TIMES
    )
    pprint(sorted(RESULTS.items(), key=lambda x: x[1]))
