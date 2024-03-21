"""Tests performance of pandas DataFrame with string columns,
when we want to filter it based on some string-related condition
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
import numpy as np

def random_substr(st: str):
    start = random.randint(0, len(st) - 1)
    end = random.randint(start + 1, len(st))
    return st[start:end]

def process(line):
    return "e" in line

base_st = string.ascii_lowercase
st_arr = [random_substr(base_st) for _ in range(999999)]
st_arr1 = [random_substr(base_st) for _ in range(999999)]
st_arr2 = [random_substr(base_st) for _ in range(999999)]
df = pd.DataFrame({"st": st_arr, "st1": st_arr1, "st2": st_arr2})
"""

stmt_str_method = """
df_filtered = df[(df['st'].str.contains("e")) | (df['st1'].str.contains("e")) | (df['st2'].str.contains("e"))]
"""

stmt_bool_array = """
from functools import reduce
st_mask = np.fromiter(map(process, df['st'].values), dtype=bool)
st1_mask = np.fromiter(map(process, df['st1'].values), dtype=bool)
st2_mask = np.fromiter(map(process, df['st2'].values), dtype=bool)
full_mask = reduce(np.logical_or, [st_mask, st1_mask, st2_mask])
df_filtered = df[full_mask]
"""

stmt_bool_array_native_list = """
st_mask = map(process, df['st'].values.tolist())
st1_mask = map(process, df['st1'].values.tolist())
st2_mask = map(process, df['st2'].values.tolist())
full_mask = [any(t) for t in zip(st_mask, st1_mask, st2_mask)]
df_filtered = df[full_mask]
"""

stmt_bool_array_pyfunc = """
from functools import reduce
process_arr = np.frompyfunc(process, 1, 1)
st_mask = process_arr(df['st'].values)
st1_mask = process_arr(df['st1'].values)
st2_mask = process_arr(df['st2'].values)
full_mask = reduce(np.logical_or, [st_mask, st1_mask, st2_mask])
df_filtered = df[full_mask]
"""

# Concat all string columns, then use str method
stmt_concat_str_str_method = """
df['st_full'] = df['st'] + df['st1'] + df['st2']
df_filtered = df[df['st_full'].str.contains("e")]
"""

# Concat all string columns, then use bool array
stmt_concat_str_bool_array = """
df['st_full1'] = df['st'] + df['st1'] + df['st2']
st_mask = np.fromiter(map(process, df['st_full1'].values), dtype=bool)
df_filtered = df[st_mask]
"""


if __name__ == "__main__":
    RESULTS['str_method'] = timeit.timeit(
        setup=SETUP,
        stmt=stmt_str_method,
        number=TEST_TIMES
    )
    RESULTS['bool_array'] = timeit.timeit(
        setup=SETUP,
        stmt=stmt_bool_array,
        number=TEST_TIMES
    )
    RESULTS['bool_array_native_list'] = timeit.timeit(
        setup=SETUP,
        stmt=stmt_bool_array_native_list,
        number=TEST_TIMES
    )
    RESULTS['bool_array_pyfunc'] = timeit.timeit(
        setup=SETUP,
        stmt=stmt_bool_array_pyfunc,
        number=TEST_TIMES
    )
    # RESULTS['concat_str_str_method'] = timeit.timeit(
    #     setup=SETUP,
    #     stmt=stmt_concat_str_str_method,
    #     number=TEST_TIMES
    # )
    # RESULTS['concat_str_bool_array'] = timeit.timeit(
    #     setup=SETUP,
    #     stmt=stmt_concat_str_bool_array,
    #     number=TEST_TIMES
    # )
    pprint(sorted(RESULTS.items(), key=lambda x: x[1]))
