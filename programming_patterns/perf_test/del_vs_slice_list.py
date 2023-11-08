"""Tests del vs slice of list
"""
import timeit
from pprint import pprint


TEST_TIMES = 1000
RESULTS = {}


setup_del = "lst = [1 for _ in range(2**25)]"
setup_slice = "lst = [1 for _ in range(2**25)]"

stmt_del = """batch_size = 2**10
while lst:
    out = lst[:batch_size]
    del lst[:batch_size]
"""
stmt_slice = """batch_size = 2**10
while lst:
    out = lst[:batch_size]
    lst = lst[batch_size:]
"""


if __name__ == "__main__":
    RESULTS['del'] = timeit.timeit(
        setup=setup_del,
        stmt=stmt_del,
        number=TEST_TIMES
    )
    RESULTS['slice'] = timeit.timeit(
        setup=setup_slice,
        stmt=stmt_slice,
        number=TEST_TIMES
    )
    pprint(sorted(RESULTS.items(), key=lambda x: x[1]))
